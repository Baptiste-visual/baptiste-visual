#!/usr/bin/env python3
"""Objective checks for a 60 s Moorea soundtrack candidate (we cannot listen, so we measure).

usage: python3 tools/audio/v2/analyze.py <mix.wav> [--cues cues.json] [--out <dir>]

Reports: format/length, integrated LUFS, true peak, loudness per bar, band balance per section,
cue sync (spectral-flux onset near every cue), clicks, isolated high tonal beeps (a "toy" sound
marker), stereo correlation. Writes <out>/analysis.json, <out>/spectrogram.png, <out>/waveform.png.
"""
import argparse, json, os, subprocess
import numpy as np
import soundfile as sf
import pyloudnorm as pyln
from scipy.signal import resample_poly, stft, butter, sosfilt

SECTIONS = [('hook', 0, 4), ('rejouer', 4, 6), ('level', 6, 10), ('powerups', 10, 40),
            ('breakdown', 40, 45), ('build', 45, 50), ('drop', 50, 54), ('outro', 54, 60)]
BANDS = [('sub<60', 20, 60), ('low60-250', 60, 250), ('mid250-2k', 250, 2000),
         ('pres2k-6k', 2000, 6000), ('air>6k', 6000, 20000)]

ap = argparse.ArgumentParser()
ap.add_argument('wav'); ap.add_argument('--cues'); ap.add_argument('--out')
a = ap.parse_args()
out = a.out or os.path.join(os.path.dirname(os.path.abspath(a.wav)), 'analysis')
os.makedirs(out, exist_ok=True)

x, sr = sf.read(a.wav, always_2d=True)
x = x.T.astype(np.float64)
rep = {'file': a.wav, 'sr': sr, 'channels': x.shape[0], 'samples': x.shape[1],
       'duration_s': round(x.shape[1] / sr, 4), 'expected_samples': 60 * 48000,
       'length_ok': x.shape[1] == 60 * 48000 and sr == 48000 and x.shape[0] == 2}
mono = x.mean(0)

meter = pyln.Meter(sr)
rep['lufs_integrated'] = round(float(meter.integrated_loudness(x.T)), 2)
tp = max(np.abs(resample_poly(c, 4, 1)).max() for c in x)
rep['true_peak_dbtp'] = round(float(20 * np.log10(tp + 1e-12)), 2)
rep['sample_peak_dbfs'] = round(float(20 * np.log10(np.abs(x).max() + 1e-12)), 2)
rep['dc_offset'] = [round(float(c.mean()), 5) for c in x]

# loudness per 2 s bar (short-term-ish)
bars = []
for b in range(30):
    seg = x[:, b * 2 * sr:(b + 1) * 2 * sr]
    l = meter.integrated_loudness(seg.T) if seg.shape[1] > sr // 2 else -99
    bars.append(round(float(l), 1))
rep['lufs_per_bar_2s'] = bars


def band_db(sig, lo, hi):
    sos = butter(4, [lo, min(hi, sr / 2 - 100)], btype='band', fs=sr, output='sos')
    y = sosfilt(sos, sig)
    return 10 * np.log10(np.mean(y ** 2) + 1e-15)


sec = {}
for name, t0, t1 in SECTIONS:
    seg = mono[int(t0 * sr):int(t1 * sr)]
    tot = 10 * np.log10(np.mean(seg ** 2) + 1e-15)
    l, r = x[0, int(t0 * sr):int(t1 * sr)], x[1, int(t0 * sr):int(t1 * sr)]
    corr = float(np.sum(l * r) / (np.sqrt(np.sum(l ** 2) * np.sum(r ** 2)) + 1e-15))
    sec[name] = {'rms_dbfs': round(float(tot), 1),
                 'bands_db_rel_total': {bn: round(float(band_db(seg, lo, hi) - tot), 1) for bn, lo, hi in BANDS},
                 'stereo_corr': round(corr, 2)}
rep['sections'] = sec

# clicks: sample jumps far above the local signal slope
d = np.abs(np.diff(x, axis=1)).max(0)
loc = np.convolve(d, np.ones(480) / 480, mode='same')
clicks = np.where((d > 0.25) & (d > 12 * loc + 1e-4))[0]
rep['click_candidates_s'] = sorted(set(round(float(i / sr), 3) for i in clicks))[:40]

# STFT for onsets + tonal beeps
hop, nfft = 256, 2048
f, tt, Z = stft(mono, fs=sr, nperseg=nfft, noverlap=nfft - hop, boundary=None, padded=False)
M = np.abs(Z)
tt = tt  # centre times
logM = np.log1p(100 * M)
flux = np.maximum(0, np.diff(logM, axis=1)).sum(0)
flux = np.concatenate([[0], flux])
med = np.median(flux) + 1e-9

if a.cues:
    cues = json.load(open(a.cues))
    cues = cues['cues'] if isinstance(cues, dict) else cues
    res = []
    for c in cues:
        t = float(c['t'])
        w = (tt >= t - 0.04) & (tt <= t + 0.04)
        if not w.any():
            continue
        i = np.argmax(np.where(w, flux, -1))
        local = np.median(flux[(tt >= t - 0.5) & (tt <= t + 0.5)]) + 1e-9
        res.append({'t': t, 'event': c.get('event', ''), 'weight': c.get('weight', 1),
                    'onset_offset_ms': round(float((tt[i] - t) * 1000), 1),
                    'strength_vs_global_median': round(float(flux[i] / med), 1),
                    'strength_vs_local_median': round(float(flux[i] / local), 1)})
    weak = [r for r in res if r['weight'] >= 2 and (r['strength_vs_local_median'] < 2.0 or abs(r['onset_offset_ms']) > 25)]
    rep['cue_sync'] = {'checked': len(res), 'weak_or_late_weight>=2': weak,
                       'median_abs_offset_ms': round(float(np.median([abs(r['onset_offset_ms']) for r in res])) if res else 0, 1),
                       'all': res}

# isolated high tonal beeps (sine/square blips above 1.8 kHz, 30 ms+): the "toy" marker
hi = f >= 1800
P = 20 * np.log10(M[hi] + 1e-9)
fh = f[hi]
beeps = []
step = max(1, int(0.03 * sr / hop))
for j in range(0, P.shape[1], step):
    col = P[:, j]
    k = int(np.argmax(col))
    prom = col[k] - np.median(col)
    if prom > 32 and col[k] > -45:
        beeps.append((round(float(tt[j]), 2), int(fh[k]), round(float(prom), 1)))
merged = []
for b in beeps:
    if merged and b[0] - merged[-1]['t_end'] <= 0.06 and abs(b[1] - merged[-1]['hz']) < 300:
        merged[-1]['t_end'] = b[0]
    else:
        merged.append({'t': b[0], 't_end': b[0], 'hz': b[1], 'prominence_db': b[2]})
rep['high_tonal_beeps'] = {'count': len(merged), 'events': merged[:60]}

json.dump(rep, open(os.path.join(out, 'analysis.json'), 'w'), indent=1)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', a.wav, '-lavfi',
                'showspectrumpic=s=2400x900:mode=combined:scale=log:fscale=log:legend=1',
                os.path.join(out, 'spectrogram.png')], check=False)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', a.wav, '-lavfi',
                'showwavespic=s=2400x500:split_channels=1:scale=sqrt',
                os.path.join(out, 'waveform.png')], check=False)

print(json.dumps({k: rep[k] for k in ['duration_s', 'length_ok', 'lufs_integrated', 'true_peak_dbtp', 'dc_offset']}))
print('LUFS per bar:', bars)
for n, s in sec.items():
    print(f"{n:10s} rms {s['rms_dbfs']:6.1f}  corr {s['stereo_corr']:.2f}  bands {s['bands_db_rel_total']}")
print('clicks:', rep['click_candidates_s'][:12])
print('high tonal beeps:', rep['high_tonal_beeps']['count'], [(e['t'], e['hz']) for e in merged[:12]])
if a.cues:
    cs = rep['cue_sync']
    print(f"cue sync: {cs['checked']} cues, median |offset| {cs['median_abs_offset_ms']} ms, weak/late weight>=2: {len(cs['weak_or_late_weight>=2'])}")
    for r in cs['weak_or_late_weight>=2'][:20]:
        print('  weak', r)
print('wrote', out)
