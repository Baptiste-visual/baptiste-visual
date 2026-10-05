#!/usr/bin/env python3
"""Moorea promo — original score + sound design, synthesized from scratch.

150 BPM (beat 0.4 s, bar 1.6 s), 22 bars = 35.2 s, F minor. Every SFX is placed on the
storyboard's cue sheet (STORYBOARD.md `sfx:` lines), so picture and sound are locked.
Deterministic: fixed seeds, no external samples. Output: assets/audio/mix.wav (48 kHz, 16-bit stereo).
"""
import numpy as np
import soundfile as sf
from pedalboard import Pedalboard, Reverb, Compressor, Limiter, HighpassFilter, LowpassFilter, Distortion, Delay, Chorus, LowShelfFilter, HighShelfFilter, PeakFilter
from scipy.signal import butter, sosfilt

SR = 48000
DUR = 35.2
N = int(SR * DUR) + SR  # 1 s of tail headroom, trimmed at the end
BEAT = 0.4
RNG = np.random.default_rng(20260605)

music = np.zeros((2, N), np.float32)
sfx = np.zeros((2, N), np.float32)


# ---------------------------------------------------------------- helpers
def t_(d):
    return np.arange(int(SR * d)) / SR


def note(n):  # MIDI -> Hz
    return 440.0 * 2 ** ((n - 69) / 12)


def env_ad(n, a, d, curve=4.0):
    a = max(1, int(a * SR)); x = np.zeros(n, np.float32)
    x[:a] = np.linspace(0, 1, a)
    rest = n - a
    if rest > 0:
        x[a:] = np.exp(-curve * np.linspace(0, 1, rest) * (n / SR) / max(d, 1e-3))
    return x


def place(buf, sig, at, gain=1.0, pan=0.0):
    """Mix mono/stereo sig into buf at time `at` (s), equal-power pan -1..1."""
    i = int(round(at * SR))
    if sig.ndim == 1:
        l = np.cos((pan + 1) * np.pi / 4); r = np.sin((pan + 1) * np.pi / 4)
        sig = np.vstack([sig * l * 1.4142, sig * r * 1.4142])
    n = min(sig.shape[1], buf.shape[1] - i)
    if n > 0 and i >= 0:
        buf[:, i:i + n] += sig[:, :n] * gain


def bp(x, lo, hi, order=2):
    sos = butter(order, [lo, hi], btype='band', fs=SR, output='sos'); return sosfilt(sos, x)


def lp(x, f, order=2):
    sos = butter(order, f, btype='low', fs=SR, output='sos'); return sosfilt(sos, x)


def hp(x, f, order=2):
    sos = butter(order, f, btype='high', fs=SR, output='sos'); return sosfilt(sos, x)


def noise(d):
    return RNG.standard_normal(int(SR * d)).astype(np.float32)


def saw(f, d, phase=0.0):
    t = t_(d); return (2 * ((f * t + phase) % 1.0) - 1).astype(np.float32)


def sq(f, d, duty=0.5):
    t = t_(d); return np.where((f * t) % 1.0 < duty, 1.0, -1.0).astype(np.float32)


def sine_sweep(f0, f1, d, curve='exp'):
    t = t_(d)
    if curve == 'exp':
        f = f0 * (f1 / f0) ** (t / d)
    else:
        f = f0 + (f1 - f0) * (t / d)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph).astype(np.float32)


def resonant_lp(x, cut_env, q=0.85):
    """Time-varying state-variable lowpass (per-sample) for acid stabs. cut_env in Hz, same length as x."""
    y = np.zeros_like(x); low = band = 0.0
    for i in range(len(x)):
        f = 2 * np.sin(np.pi * min(cut_env[i], SR / 6) / SR)
        high = x[i] - low - q * band
        band += f * high; low += f * band
        y[i] = low
    return y


# ---------------------------------------------------------------- instruments
def kick(hard=1.0, tail_note=None, d=0.38):
    t = t_(d)
    f = 48 + 150 * np.exp(-t * 38)
    if tail_note is not None:
        f = note(tail_note) + 170 * np.exp(-t * 30)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * (6.5 if tail_note is None else 3.2))
    click = hp(noise(d), 2500) * np.exp(-t * 300) * 0.5
    k = body + click
    k = np.tanh(k * (1.6 + 3.5 * hard)) / np.tanh(1.6 + 3.5 * hard)
    return (k * 0.95).astype(np.float32)


def hat(open_=False):
    d = 0.16 if open_ else 0.045
    x = hp(noise(d), 7500, 4) * env_ad(int(SR * d), 0.001, d * (0.6 if open_ else 0.35))
    return x.astype(np.float32) * (0.55 if open_ else 0.45)


def clap():
    d = 0.25; x = np.zeros(int(SR * d), np.float32)
    for k, off in enumerate([0, 0.011, 0.022, 0.034]):
        b = bp(noise(0.2), 900, 2600) * env_ad(int(SR * 0.2), 0.001, 0.05 if k < 3 else 0.14)
        i = int(off * SR); x[i:i + len(b)] += b[:len(x) - i]
    return x * 0.8


def snare(d=0.18):
    t = t_(d)
    tone = np.sin(2 * np.pi * 190 * t) * np.exp(-t * 30)
    nz = bp(noise(d), 1200, 7000) * np.exp(-t * 22)
    return ((tone * 0.6 + nz) * 0.7).astype(np.float32)


def bass_hit(n, d=0.14):
    t = t_(d)
    x = saw(note(n), d) * 0.6 + saw(note(n) * 1.005, d) * 0.4
    x = lp(x, 520) * env_ad(len(t), 0.004, d * 0.8, 3)
    return np.tanh(x * 2.2).astype(np.float32) * 0.55


def supersaw(notes, d, cutoff=5200, att=0.02, rel_curve=2.5):
    t = t_(d); out = np.zeros(len(t), np.float32)
    det = [-0.11, -0.06, -0.025, 0, 0.025, 0.06, 0.11]
    for n in notes:
        for k, dt in enumerate(det):
            out += saw(note(n + dt), d, phase=(k * 0.137) % 1)
    out = lp(out / (len(notes) * len(det)) * 3.0, cutoff, 2)
    return (out * env_ad(len(t), att, d, rel_curve)).astype(np.float32)


def acid_stab(n, d=0.22, peak=3200):
    x = saw(note(n), d)
    t = t_(d); cut = 180 + peak * np.exp(-t * 18)
    y = resonant_lp(x, cut, q=0.35)
    return np.tanh(y * 3.0).astype(np.float32) * env_ad(len(t), 0.002, d * 0.7, 2.5) * 0.5


# ---------------------------------------------------------------- sound design
def boom(d=1.6):
    t = t_(d); f = 32 + 120 * np.exp(-t * 9)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 2.2)
    x += lp(noise(d), 300) * np.exp(-t * 6) * 0.6
    return np.tanh(x * 2.5).astype(np.float32) * 0.9


def impact():
    d = 0.9; t = t_(d)
    x = kick(1.0, d=0.5); x = np.pad(x, (0, len(t) - len(x)))
    x += bp(noise(d), 200, 5000) * np.exp(-t * 7) * 0.5
    return x.astype(np.float32)


def crash(d=1.8):
    t = t_(d); x = hp(noise(d), 4000) * np.exp(-t * 2.3)
    x += bp(noise(d), 3000, 9000) * np.exp(-t * 1.4) * 0.5
    return x.astype(np.float32) * 0.45


def whoosh(d=0.35, up=True, lo=300, hi=6000):
    t = t_(d); x = noise(d); y = np.zeros_like(x); seg = 256
    for i in range(0, len(x), seg):
        p = i / len(x); p = p if up else 1 - p
        c = lo * (hi / lo) ** p
        y[i:i + seg] = bp(x[i:i + seg], max(60, c * 0.6), min(SR / 2 - 100, c * 1.6))
    env = np.sin(np.pi * np.linspace(0, 1, len(t))) ** 1.2
    return (y * env * 1.6).astype(np.float32)


def geyser(stab_note):
    d = 0.42; out = np.zeros(int(SR * d), np.float32)
    w = whoosh(0.35, True, 250, 5000) * 0.9
    out[:len(w)] += w
    fire = lp(noise(d), 1800) * env_ad(int(SR * d), 0.02, 0.25) * 0.5
    out += fire
    st = acid_stab(stab_note, 0.24); out[:len(st)] += st * 1.1
    return out


def fall_whistle(d=0.4):
    return (sine_sweep(2200, 380, d) * env_ad(int(SR * d), 0.03, d, 1.2) * 0.22).astype(np.float32)


def thud():
    d = 0.5; t = t_(d)
    x = np.sin(2 * np.pi * np.cumsum(70 + 90 * np.exp(-t * 25)) / SR) * np.exp(-t * 9)
    x += lp(noise(d), 900) * np.exp(-t * 18) * 0.5
    return np.tanh(x * 2).astype(np.float32) * 0.8


def splash():
    d = 0.6; t = t_(d); x = np.zeros(len(t), np.float32)
    for k in range(9):  # bubbly plops
        at = RNG.uniform(0, 0.35); f0 = RNG.uniform(260, 700); dd = 0.08
        b = sine_sweep(f0, f0 * 2.2, dd) * env_ad(int(SR * dd), 0.002, 0.05)
        i = int(at * SR); x[i:i + len(b)] += b[:len(x) - i] * 0.25
    x += bp(noise(d), 500, 3000) * np.exp(-t * 8) * 0.35
    return x


def pssht_ting():
    d = 0.9; t = t_(d)
    hiss = hp(noise(d), 3500) * np.exp(-t * 7) * 0.55
    bell = np.zeros(len(t))
    for f, a, dec in [(2640, 1.0, 4), (3960, 0.55, 5), (5280, 0.3, 7), (7170, 0.2, 9)]:
        bell += np.sin(2 * np.pi * f * t) * a * np.exp(-t * dec)
    bell = np.concatenate([np.zeros(int(0.12 * SR)), bell[:len(t) - int(0.12 * SR)]]) * 0.16
    return (hiss + bell).astype(np.float32)


def coin():
    a = sq(note(83), 0.07, 0.25) * 0.18; b = sq(note(88), 0.22, 0.25) * env_ad(int(SR * 0.22), 0.002, 0.18) * 0.18
    return np.concatenate([a, b]).astype(np.float32)


def stamp():
    d = 0.35; t = t_(d)
    x = np.sin(2 * np.pi * np.cumsum(120 + 200 * np.exp(-t * 40)) / SR) * np.exp(-t * 14)
    x += bp(noise(d), 1500, 6000) * np.exp(-t * 40) * 0.6
    return np.tanh(x * 2.2).astype(np.float32) * 0.6


def boing():
    d = 0.16; return (sq(1, d) * 0 + sine_sweep(300, 1100, d) * env_ad(int(SR * d), 0.003, 0.12) * 0.3).astype(np.float32)


def blip(n, d=0.09, duty=0.5, g=0.2):
    return (sq(note(n), d, duty) * env_ad(int(SR * d), 0.002, d * 0.7) * g).astype(np.float32)


def tick():
    d = 0.03; return (hp(noise(d), 3000) * env_ad(int(SR * d), 0.0005, 0.01) * 0.5).astype(np.float32)


def glitch_buzz(d=0.35):
    x = sq(55, d, 0.3) * 0.5 + saw(110.5, d) * 0.4
    x = np.round(x * 4) / 4  # bitcrush
    gate = (np.floor(t_(d) * 40) % 3 != 1).astype(np.float32)
    return (x * gate * env_ad(int(SR * d), 0.002, d, 1.5) * 0.35).astype(np.float32)


def crt_zap():
    d = 0.22; return (sine_sweep(9000, 120, d) * env_ad(int(SR * d), 0.001, d, 2) * 0.25 + tick()[:1].sum() * 0).astype(np.float32)


def crt_on():
    d = 0.35; t = t_(d)
    x = np.sin(2 * np.pi * 60 * t) * np.exp(-t * 10) * 0.6 + hp(noise(d), 2000) * np.exp(-t * 14) * 0.35
    return x.astype(np.float32)


def heartbeat():
    d = 0.5; t = t_(d); x = np.zeros(len(t))
    for off, a in [(0.0, 1.0), (0.17, 0.7)]:
        i = int(off * SR); tt = t[:len(t) - i]
        x[i:] += np.sin(2 * np.pi * (45 + 30 * np.exp(-tt * 30)) * tt) * np.exp(-tt * 16) * a
    return lp(x, 160).astype(np.float32) * 1.6


def sparkle(d=0.6):
    t = t_(d); x = np.zeros(len(t))
    for k in range(14):
        f = RNG.uniform(3000, 9000); at = RNG.uniform(0, d * 0.6); dd = 0.12
        i = int(at * SR); n = min(int(SR * dd), len(t) - i)
        x[i:i + n] += np.sin(2 * np.pi * f * t[:n]) * np.exp(-t[:n] * 30) * 0.08
    return x.astype(np.float32)


def clang():
    d = 1.0; t = t_(d); x = np.zeros(len(t))
    for f, a, dec in [(420, 1, 3), (1070, 0.7, 4), (1840, 0.5, 5), (2930, 0.35, 6), (4370, 0.25, 8)]:
        x += np.sin(2 * np.pi * f * t) * a * np.exp(-t * dec)
    x += bp(noise(d), 2000, 9000) * np.exp(-t * 25) * 0.8
    return (np.tanh(x * 0.9) * 0.45).astype(np.float32)


def rewind(src_buf, t0, t1, d):
    """Tape-rewind: the last stretch of audio played backwards with rising pitch."""
    seg = src_buf[:, int(t0 * SR):int(t1 * SR)][:, ::-1]
    n = int(d * SR); idx = (np.linspace(0, 1, n) ** 1.7) * (seg.shape[1] - 1)
    out = np.vstack([np.interp(idx, np.arange(seg.shape[1]), seg[c]) for c in range(2)])
    squeal = sine_sweep(600, 3200, d) * 0.08
    return (out * 0.55 + squeal).astype(np.float32)


def riser(d, lo=200, hi=8000):
    w = whoosh(d, True, lo, hi)
    t = t_(d); w *= (t / d) ** 1.5 * 1.6
    tone = sine_sweep(note(41), note(65), d) * (t / d) ** 2 * 0.15
    return (w + tone).astype(np.float32)


def reverse_cymbal(d=0.4):
    return (crash(d)[::-1] * 1.3).astype(np.float32)


# ================================================================ SCORE (music bus)
F1, AB1, C2, DB2, EB2, F2 = 29, 32, 36, 37, 39, 41   # F minor roots (MIDI)
bass_line = [F1, F1, F1, AB1, F1, F1, EB2 - 12, DB2 - 12]  # per beat pattern (2 bars)


def groove(t0, t1, kick_hard=1.0, bass=True, hats=True, claps=True, lead=False, kick_on=True, tail=None):
    b = 0
    t = t0
    while t < t1 - 1e-6:
        if kick_on:
            place(music, kick(kick_hard, tail_note=tail), t, 0.95)
        if bass:
            root = bass_line[b % len(bass_line)]
            for s in (1, 2, 3):  # rolling 16ths after the kick
                place(music, bass_hit(root + (12 if s == 2 else 0)), t + s * BEAT / 4, 0.55 if s != 2 else 0.4)
        if hats:
            place(music, hat(True), t + BEAT / 2, 0.35, pan=0.25)
            for s in range(4):
                place(music, hat(False), t + s * BEAT / 4, 0.18 if s % 2 else 0.1, pan=-0.2)
        if claps and b % 2 == 1:
            place(music, clap(), t, 0.5)
        if lead and b % 4 == 0:
            seq = [65, 68, 72, 70] if (b // 4) % 2 == 0 else [65, 68, 75, 72]
            for k, n in enumerate(seq):
                place(music, acid_stab(n - 12, 0.18, 2200), t + k * BEAT / 2, 0.22, pan=0.3 * (1 if k % 2 else -1))
        t += BEAT; b += 1


# A — hook 0.0–3.2: no groove, lava bed
bed = lp(noise(3.3), 140) * 0.35
place(music, bed, 0.0, 1.0)
for i, n in enumerate([76, 72, 69]):
    place(sfx, blip(n, 0.12, 0.5, 0.18), 0.0 + i * 0.13)
place(sfx, blip(64, 0.3, 0.5, 0.16), 0.39)
place(sfx, splash(), 0.4, 1.0); place(sfx, sine_sweep(320, 55, 0.35) * env_ad(int(SR * 0.35), 0.002, 0.3) * 0.6, 0.4)
place(sfx, hp(noise(0.5), 3000) * env_ad(int(SR * 0.5), 0.01, 0.35) * 0.25, 0.45)
for at in (0.8, 1.2):
    place(music, boom(1.4), at, 1.0); place(music, impact(), at, 0.9); place(music, crash(1.6), at, 0.7)
go = [67, 66, 65, 64, 63, 62, 61, 60]  # chromatic 8-bit game-over descent
for i, n in enumerate(go):
    place(sfx, blip(n, 0.1, 0.25, 0.16), 0.8 + i * 0.1, pan=-0.3 + i * 0.08)
place(sfx, blip(48, 0.5, 0.5, 0.18), 1.6)
place(sfx, glitch_buzz(0.35), 1.6, 1.0)
place(sfx, glitch_buzz(0.18), 2.0, 0.8)

# B — rejouer 3.2–4.8
place(sfx, crt_on(), 3.2); place(sfx, blip(84, 0.06, 0.5, 0.15), 3.22)
for k, at in enumerate([3.2, 3.6, 4.0, 4.4]):
    kk = lp(kick(0.6), 600 if at < 4.0 else 20000)
    place(music, kk, at, 0.9)
place(sfx, tick(), 3.6, 1.2); place(sfx, blip(79, 0.05, 0.5, 0.12), 3.6)
place(sfx, impact(), 4.0, 0.9); place(sfx, coin(), 4.0, 1.4); place(sfx, crash(1.0), 4.0, 0.5)
place(sfx, reverse_cymbal(0.4), 4.4, 1.0)

# C — level 4.8–8.0
place(sfx, impact(), 4.8, 1.0); place(music, crash(1.8), 4.8, 0.6)
for i, n in enumerate([72, 76, 79, 84, 88, 91, 96]):
    place(sfx, blip(n, 0.05, 0.25, 0.14), 4.8 + i * 0.05)
groove(4.8, 8.0, kick_hard=0.7, claps=False, hats=True)
place(sfx, splash(), 5.6, 1.0)
for i in range(8):
    place(sfx, geyser(53 + i), 5.6 + i * 0.2, 0.75, pan=[-0.6, 0.6, 0, -0.4, 0.5, -0.1, 0.6, -0.6][i])
place(sfx, riser(0.8), 7.2, 1.0)
for i in range(16):
    place(music, snare(0.1), 7.2 + i * 0.05, 0.15 + 0.35 * i / 16)

# D — power-ups 8.0–22.4: full groove with acid lead
groove(8.0, 22.4, kick_hard=1.0, lead=True)
place(music, crash(1.8), 8.0, 0.6)
PUS = [8.0, 10.4, 12.8, 15.2, 17.6, 20.0]
for k, P in enumerate(PUS):
    place(sfx, geyser(58 + k), P, 0.8)
    place(sfx, fall_whistle(0.4), P + 0.4, 1.0)
    place(sfx, thud(), P + 0.8, 1.0); place(sfx, splash(), P + 0.8, 0.8); place(sfx, pssht_ting(), P + 0.8, 1.0)
    place(sfx, stamp(), P + 1.2, 1.0); place(sfx, coin(), P + 1.2, 1.2)
    place(sfx, boing(), P + 1.6, 1.0)
    place(sfx, whoosh(0.4, True, 400, 7000), P + 2.0, 0.9, pan=-0.5)
# PU2 branding stamps (local 3.30–3.90 in F04 → 11.30)
for i in range(8):
    b = hp(noise(0.06), 2500) * env_ad(int(SR * 0.06), 0.001, 0.03) * 0.5
    place(sfx, b, 11.3 + i * 0.075, 1.0, pan=-0.6 + i * 0.17)
# PU3 map rise + pins + chip + sonar
place(sfx, lp(noise(0.6), 250) * env_ad(int(SR * 0.6), 0.1, 0.4) * 0.9, 13.2)
place(sfx, clang()[:int(0.3 * SR)] * 0.3, 13.25)
for i, n in enumerate([62, 69, 69, 57, 62, 74]):
    place(sfx, blip(n + 12, 0.07, 0.5, 0.14), 13.6 + i * 0.2, pan=-0.5 + i * 0.2)
place(sfx, blip(86, 0.05, 0.5, 0.12), 13.8)
sonar = (np.sin(2 * np.pi * 1400 * t_(0.9)) * np.exp(-t_(0.9) * 5) * 0.18).astype(np.float32)
place(sfx, sonar, 14.2, 1.0)
# PU4 clash + sheet + checks + valider
place(sfx, clang(), 15.4, 1.1); place(sfx, sparkle(0.4), 15.4, 1.0)
place(sfx, whoosh(0.35, True, 200, 3000), 15.6, 0.8)
for i in range(3):
    place(sfx, tick(), 16.0 + i * 0.2, 1.4); place(sfx, blip(76 + i * 4, 0.06, 0.5, 0.13), 16.0 + i * 0.2)
place(sfx, impact(), 16.6, 0.6); place(sfx, sparkle(0.5), 16.6, 1.0)
# PU5 tiles pops + card slaps
for i in range(4):
    place(sfx, sine_sweep(500, 1300, 0.07) * 0.18, 18.0 + i * 0.2)
    place(sfx, whoosh(0.12, False, 800, 4000) * 0.7 + 0, 18.35 + i * 0.2)
    place(sfx, thud() * 0.5, 18.4 + i * 0.2)
# PU6 numbered pings + cash
for i in range(3):
    place(sfx, blip(79 + i * 5, 0.12, 0.5, 0.15), 20.8 + i * 0.2)
place(sfx, coin(), 21.25, 1.0)

# E — breakdown 22.4–24.8 (no kick): heartbeat + pad
pad = supersaw([53, 56, 60], 2.6, cutoff=900, att=0.4, rel_curve=1.2)
place(music, pad, 22.4, 0.5)
for at in np.arange(22.4, 24.8, 0.8):
    place(music, heartbeat(), at, 0.9)
groove(22.4, 24.8, kick_on=False, bass=False, hats=True, claps=False)
place(sfx, geyser(64), 22.4, 0.6)
place(sfx, thud() * 0.6, 23.2); place(sfx, tick(), 23.2, 1.5); place(sfx, blip(72, 0.05, 0.5, 0.12), 23.22)
for i in range(8):
    place(sfx, tick(), 23.2 + i * 0.05, 0.6)
place(sfx, sonar, 23.6, 1.0)
place(sfx, stamp(), 23.6, 1.0); place(sfx, coin(), 23.6, 1.1)
place(sfx, sparkle(0.5), 23.8, 1.2)
place(sfx, sine_sweep(300, 700, 0.15) * env_ad(int(SR * 0.15), 0.005, 0.1) * 0.25, 24.0)
place(sfx, whoosh(0.4, True, 400, 7000), 24.4, 0.9, pan=-0.5)

# F — build 24.8–27.2
place(sfx, geyser(65), 24.8, 0.8)
roll_t = 24.8
while roll_t < 27.1:
    p = (roll_t - 24.8) / 2.3
    step = 0.2 if p < 0.33 else (0.1 if p < 0.66 else 0.05)
    place(music, snare(0.1), roll_t, 0.2 + 0.5 * p)
    roll_t += step
place(music, riser(2.35, 150, 9000), 24.8, 1.0)
place(music, supersaw([53, 56, 60, 65], 2.35, cutoff=1500, att=1.5, rel_curve=0.3), 24.8, 0.35)
for i in range(12):
    place(sfx, tick(), 25.2 + i * 0.05, 1.0)
place(sfx, whoosh(0.25, True, 600, 8000), 25.8, 0.9)
place(sfx, sine_sweep(600, 1400, 0.08) * 0.22, 26.0); place(sfx, coin(), 26.0, 1.0)
for i in range(4):
    place(sfx, blip(84 + i * 2, 0.04, 0.5, 0.1), 26.2 + i * 0.1)
place(sfx, stamp(), 26.0, 0.8)

# G — DROP 27.2–30.4: hardstyle
place(music, crash(2.0), 27.2, 0.8); place(music, boom(1.2), 27.2, 0.9)
groove(27.2, 30.4, kick_hard=1.6, tail=F1 + 12, bass=False, hats=True, claps=True)
lead_seq = [(0.0, [77, 80, 84]), (0.4, [77, 80, 84]), (0.6, [80, 84, 87]), (0.8, [79, 82, 86]), (1.2, [77, 80, 84]),
            (1.6, [75, 79, 82]), (2.0, [75, 79, 82]), (2.2, [77, 80, 84]), (2.4, [80, 84, 87]), (2.8, [82, 86, 89])]
for off, ch in lead_seq:
    place(music, supersaw([n - 12 for n in ch], 0.36, cutoff=6500, att=0.005, rel_curve=2.0), 27.2 + off, 0.42)
for i in range(8):
    place(sfx, tick(), 27.6 + i * 0.035, 1.0)
for i, n in enumerate([72, 76, 79, 84]):
    place(sfx, blip(n, 0.08, 0.5, 0.14), 27.9 + i * 0.06)
place(sfx, whoosh(0.6, False, 200, 6000), 28.4, 1.0)
for i in range(8):
    place(sfx, blip(67 + i * 2, 0.06, 0.25, 0.12), 28.5 + i * 0.12, pan=-0.6 + i * 0.17)
place(sfx, supersaw([72, 76, 79], 0.5, 7000, 0.005, 2), 29.45, 0.5)
place(sfx, stamp(), 29.6, 1.0); place(sfx, stamp(), 30.0, 1.0)

# H — outro 30.4–35.2
place(music, supersaw([53, 56, 60, 65], 1.6, 4500, 0.15, 0.8), 30.4, 0.5)
place(music, supersaw([49, 53, 56, 61], 1.6, 4500, 0.05, 0.8), 32.0, 0.45)
place(music, supersaw([51, 55, 58, 63], 0.8, 4500, 0.05, 1.0), 33.6, 0.45)
place(music, sparkle(1.2), 30.4, 1.2)
groove(30.4, 34.4, kick_hard=1.0, tail=F1 + 12, bass=False, hats=True, claps=True)
place(sfx, whoosh(0.45, True, 300, 5000), 31.4, 0.8)
place(sfx, impact() * 0.5, 32.0); place(sfx, sparkle(0.7), 32.0, 1.5)
place(sfx, tick(), 32.4, 1.2)
place(sfx, blip(84, 0.07, 0.5, 0.13), 32.8); place(sfx, blip(88, 0.07, 0.5, 0.13), 33.0)
place(sfx, tick(), 33.4, 1.2)
place(sfx, sine_sweep(400, 1000, 0.1) * 0.2, 33.6)
# final hit 34.4
place(music, kick(1.6, tail_note=F1 + 12, d=0.8), 34.4, 1.0); place(music, boom(1.0), 34.4, 0.8)
place(music, crash(1.5), 34.4, 0.8)
place(music, supersaw([53, 56, 60, 65, 72], 0.8, 6000, 0.002, 1.5), 34.4, 0.6)
place(sfx, tick(), 34.4, 1.5); place(sfx, coin(), 34.42, 1.0)

# rewind 2.4–3.0 built from what has been mixed so far (music+sfx of 0.8–2.4)
cur = music + sfx
place(sfx, rewind(cur, 0.8, 2.4, 0.6), 2.4, 1.0)
place(sfx, crt_zap(), 3.0, 1.0)
# silence the music bus under the rewind/CRT gap a bit (tape-stop feel)
g = np.ones(N, np.float32); a, b = int(2.4 * SR), int(3.2 * SR)
g[a:b] = np.linspace(1, 0.15, b - a)
music *= g

# ================================================================ mix
board_music = Pedalboard([HighpassFilter(28), Compressor(threshold_db=-14, ratio=3, attack_ms=5, release_ms=120)])
board_sfx = Pedalboard([HighpassFilter(40), Reverb(room_size=0.32, wet_level=0.12, dry_level=0.9, width=0.9)])
m = board_music(music, SR)
s = board_sfx(sfx, SR)
mix = m * 0.82 + s * 0.95
mix = Pedalboard([LowShelfFilter(cutoff_frequency_hz=55, gain_db=-3.5), PeakFilter(cutoff_frequency_hz=3200, gain_db=2.0, q=0.8), HighShelfFilter(cutoff_frequency_hz=6000, gain_db=2.5), Compressor(threshold_db=-10, ratio=2.5, attack_ms=3, release_ms=80), Limiter(threshold_db=-1.2, release_ms=60)])(mix.astype(np.float32), SR)
mix = mix[:, :int(DUR * SR)]
fade = int(0.25 * SR); mix[:, -fade:] *= np.linspace(1, 0, fade)
peak = np.abs(mix).max(); mix = mix / peak * 0.89
sf.write('assets/audio/mix.wav', mix.T, SR, subtype='PCM_16')
rms = np.sqrt((mix ** 2).mean())
print('written assets/audio/mix.wav', mix.shape, 'peak', np.abs(mix).max().round(3), 'rms dBFS', round(20 * np.log10(rms), 1))
