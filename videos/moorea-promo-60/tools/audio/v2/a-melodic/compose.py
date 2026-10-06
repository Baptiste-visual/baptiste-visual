#!/usr/bin/env python3
"""Moorea promo 60 s -- soundtrack v2, direction A "melodic techno" (Afterlife / Tale Of Us / Anyma school).

CONCEPT
  "GAME OVER : rejoue le Moorea" scored as a dark, cinematic melodic-techno trailer at 120 BPM in F minor
  (with a phrygian Gb colour). The game is told with trailer sound design (braams, sub drops, tape-stop,
  CRT power-down, heavy layered stamps), never with retro-game cliches. A hypnotic mid-register minor arpeggio
  is the musical thread: born filtered under "NIVEAU 1", it opens up power-up after power-up, gets washed in
  delay during the breakdown, rips open through the build and carries the drop and the end card.
  Everything is synthesized in numpy (+ pedalboard ladder filters / EQ / glue comp), deterministic (fixed seed).

REVISION 2 (supervisor critique) -- translation + ending
  * Phone / laptop translation: sub contributors -2..-3 dB (rumble 0.12, lava bed x1.6, sub_boom -2 dB, bass
    sub 0.62, kick -2 dB more in the power-ups, master low shelf -3 dB @ 60 Hz, -1.5 dB @ 220 Hz), audible
    "phone" layers added (kick mid knock + beater, saturated bass mid layer with 2nd harmonic + 700 Hz +4 dB,
    impact crunch 250-2500 Hz), arp opened (fc 330+3000*bright, LP 4.5 kHz), pad ladder floor 1.8-2.6 kHz in
    the power-ups, braam LP 3.2 kHz, presence bell +2.5 dB @ 3.3 kHz on the music bus (with a narrow -2 dB dip
    at 2 kHz for saw harshness), hats reshaped (more 3-6 kHz, less >11 kHz). Phone sim (HP 250 / LP 8 kHz):
    loss <= 2.6 dB in every section (was 5.4 in the power-ups).
  * Ending: the final Fm pad decays (tau 0.3 s), the final kick / sub / braam / crash / metal tails are short,
    the reverb returns decay (tau 0.3 s) after 59.05, and the 0.3 s end fade is applied once.
  * Drop: power-up low end -2 dB and music -0.3 dB, drop music + bass +1 dB, pre-drop vacuum 49.78-50.0
    (everything at -12 dB except the riser top and reverse swell), long crash + sub + braam on the 50.0 downbeat
    (braam blooms with a 25 ms swell into the 50.125 slam, which gets a stamp + choked crash).
  * Hook: GAME braam choked at 1.45 (30 ms); OVER +1.5 dB, deeper sub, 2.6 s braam, more hall.
    "denied" = F1 / Gb1 detuned saws, tanh drive, -3 semitone bend over 120 ms, stutter gate (no bit-crush).
  * PRESS swell voiced C-G-C-Db (b9 cluster), no major third.
  * UI: breakdown / map-pin toks = one fixed 170 Hz body, mostly noise click (dry_tok), no hall; typing = band-
    passed (1-4 kHz) noise-grain cloud with one soft tok at each end; sonar = sub thump + noise ping (no pitch).
    Hop landings: even ticks (hop 1 at 51.770 serves the 51.75 photo pop and the 51.775 landing), the rolling bass,
    shaker and lead delay step back and the music dips under each landing.
  * Development: 3-against-4 arp accent cycle 20-40, new arp contour (ARP_PAT2) 30-40 and in the drop, sparse low
    lead motif (C4-Ab4) 30-40 pre-echoing the drop line.
  * Quiet 9-19 kHz air bed (heat shimmer) under the whole film so the top octave is never an empty hole.

PALETTE (how each sound is made)
  Drums   kick: sine with 2-stage pitch envelope (~400 -> 45 Hz), short round tail, noise click, 150-900 Hz
          knock and 1-3.5 kHz beater (so it reads on phones), tanh saturation; "rumble": kick bus through a dark synthetic IR, low-passed 120 Hz, saturated,
          hard side-chained (sits between kicks).  Closed hats: HP-filtered noise 16ths with swing; open hats
          on off-beats; shaker (band-passed noise, soft attack); clap (3 noise bursts + tail) and rim ghost notes,
          both sent to a big synthetic plate.  Snare rolls (noise + 185 Hz body) for builds.
  Bass    rolling off-beat 16ths (the 3 sixteenths after each kick): sine sub layer folded into 36-72 Hz
          + detuned saw mid layer with a filter envelope and asymmetric drive (2nd harmonic), +4 dB @ 700 Hz,
          mono, side-chained hard to the kick.
  Arp     "pluck": 2 detuned polyBLEP saws + sub-octave sine, filter-envelope crossfade (bright->dark),
          16th pattern over chord tones in F3..C5, brightness/level automated per section, 3/16 ping-pong
          delay with darkening feedback, hall send.  Arp 2: low 3-step polymeter pluck (from 26 s and the drop).
  Pads    "choir supersaw": 5 detuned saws per note, odd/even voices split L/R (wide), slow drift, formant
          peaks at 650 / 1100 Hz, global automated ladder low-pass (dark in the hook, open in breakdown,
          sweeping up through the build, wide open in the drop / end card).
  Lead    low-mid detuned 3-saw lead + sub-octave, filter envelope, saturation, ping-pong delay + plate
          (drop 50-54 and end card 54-58.5).
  Braam   4-note (root-12, root, 5th, octave) detuned saw stack, heavy tanh distortion, swelling filter.
  Impacts sub drop (sine sweep ~75 -> 32 Hz) + distorted low noise body + short noise crack
          + inharmonic low "metal" partials (<700 Hz) + hall tail.  Stamps: tighter version + plate.
  Lava    eruption = low noise "whoomp" (filter crossfade), sub thump, sparse crackle; lava bed = dark
          stereo rumble; quench = wide steam hiss; "cooling sheen" = short sizzle accent (no bell).
  Motion  whooshes / whip-pans = band-passed noise with automated ladder sweep and moving pan, energy
          building into the cut (power-in envelopes); risers = noise sweep + rising low saw cluster;
          reverse swells = reversed, filtered, growing noise.
  UI      "tok": 2.5 ms band-passed noise click + tiny 150-330 Hz thump, very quiet; "dry tok" (fixed 170 Hz
          body, mostly click); "haptic" (deeper); HUD counter = soft double tok; reel / compass ratchets = 1 ms
          clicks; typing = 1-4 kHz noise-grain cloud.
          Never melodic, nothing above ~1.5 kHz tonal.
  Space   synthetic convolution IRs (decaying, filtered, decorrelated stereo noise): plate 1.9 s, hall 3.6 s,
          dark rumble IR.  Wet returns are fully decorrelated L/R (width); kick / bass / sub stay mono and the
          master side channel is high-passed at 140 Hz (mono low end).
  Master  side-chain envelopes (kick + big hits + hop landings), low shelf -3 dB @ 60 Hz, -1.5 dB @ 220 Hz,
          +1.5 dB @ 3 kHz, glue compressor, mono low end (side HP 140 Hz), 4x-oversampled look-ahead limiter,
          LUFS normalisation to -14, true peak -1.7 dBTP (so the 320k MP3 decodes under -1.0), one 0.3 s end fade.

HARMONY  F minor.  Hook Fm -> Gb (phrygian b2) | Rejouer Db -> C (dominant "power-up") | Niveau 1 Fm Db C |
  power-ups Fm Fm Db Eb | Fm Fm Db C | Fm Db Bbm C | Fm Db Eb | breakdown Dbmaj7 Bbm Gb | build Fm Db Eb C |
  drop Fm Db Bbm C (1 chord per 2 beats) | end card Fm Db Eb -> final Fm.

ARRANGEMENT
  0-4   HOOK: lava bed + dark Fm pad; GAME / OVER = impact + braam (F, then Gb); card flip whoosh; "denied"
        distorted low stutter at 2.5; tape-stop of the whole mix 2.78-3.0; tape rewind of 1.0-3.0
        (reversed, accelerating, VHS-filtered) 3.0-3.75; CRT power-off (noise collapse + hum drop) 3.75.
  4-6   REJOUER: CRT-on slam; Db pad; muffled kick 4.5; PRESS = haptic + impact + swell (C-G-C-Db cluster);
        dive: snare roll + reverse swell 5.5 -> 6.0.
  6-10  NIVEAU 1: kick in, filtered arp starts, eight molten eruptions on 8ths (rising, panned to the
        word positions), overheat: snare roll 16ths -> 32nds + noise riser + sub tremor into 10.0.
  10-40 FULL GROOVE: kick, rumble, rolling bass, hats, clap, arp growing every power-up; open hats from 18,
        3-against-4 arp accents from 20, shaker + rim + arp 2 from 26, brighter bass from 26, new arp contour
        + low lead motif from 30; crash on 10 / 20 / 30.
  40-45 BREAKDOWN: no kick, heartbeat (lub-dub), huge choir pad, delay-washed arp.
  45-50 BUILD: thinner kick to 48.5, snare roll 8ths -> 16ths -> 32nds, 5 s noise riser peaking AT 50.0,
        pad filter sweep, sub tremor + reverse crash 49 -> 50, pre-drop vacuum (-12 dB) 49.78 -> 50.0.
  50-54 DROP: hardest kick, crash, sub boom, F braam, wide supersaw chords, lead, everything.
  54-60 END CARD: sunrise pad swell, groove continues to 58.0, short riser 58.5 -> 59, FINAL HIT 59.0
        (kick with F tail + crash + sub boom + braam + decaying final chord), natural ring-out (about -14 dB by
        59.7, reverb returns decaying), single 0.3 s fade.

CUE -> SOUND (weight 3 and 2)
  0.000 opening sub swell + lava bed + low hit       0.500 swallow: sub gulp 90->35 Hz + muffled thump + sizzle
  0.775 / 1.275 pre-slam suck: reverse swell (with a breath transient)  1.000 GAME: impact + braam F
  1.500 OVER: impact + braam Gb                      2.000 card flip: fast swish + tok
  2.250 subline: soft tok                            2.500 DEAD: distorted low "denied" stutter (2.5/.543/.584/.625)
  3.000 rewind: tape jolt + rewind                   3.750 CRT power-off
  4.000 CRT on: thump + static crack + hum           4.500 reveal: tok + muffled kick + chevron swish
  5.000 PRESS: haptic + big impact + power-up swell  5.500 dive: muffled kick + snare roll + reverse swell
  5.750 orange flash: low whoomph                    6.000 hard cut: kick + crash + cut noise
  6.150 NIVEAU 1 slam: impact + braam-lite           6.375 logo lands: low metal clank
  7.000-8.750 eruptions 1-8 (rising, panned)          7.225 logo goes under: lava splash
  9.000 overheat: roll + riser + tremor              9.500 white-out: roll goes 32nds + accent
  P = 10,15,20,25,30,35 (power-ups):
    P     eruption + impact (+ crash at 10/20/30)
    P+0.5 fall whoosh (10, 15, 35); rise whoosh + rock grind (20, 25); tile toks (30)
    P+1.0 land: heavy thud + splash + steam (10, 15, 35); settle thud (20); truck-card slams 31.0-31.75
    P+1.14 sizzle accent (cooling sheen, no bell)    P+1.5 answer stamp (heavy, plate)
    P+2.12 HUD counter: soft double tok              showcase beats: toks / swishes / kick
    hops / landings: air puff + haptic               P+4.5 whip-pan whoosh peaking at the cut
  25.25 collision: metal impact + crackle  28.5 VALIDER: press impact   17.063 zoom whoosh
  40.0 soft eruption (breakdown)  40.5 warm fall  41.0 soft land + toggle haptic  41.5 stamp + compass clunk
  42.0 tap, 42.5 / 42.75 / 43.0 avatar toks, 43.0 SOS whomp, 43.5 chat tok, 44.5 whip
  45.0 eruption + impact (build)  45.5 swipe  45.75 typing run  46.5 stamp + send suck  47.0 bubble haptic
  47.5-48.25 chip toks  48.5 tap  49.0 tremor accent  49.5 reverse crash start + roll accent
  50.0 DROP  50.075 ember crackle  50.125 title slam impact  50.5 reel ratchets (decelerating)
  50.875 8/8 impact  51.5 pull-back whoosh  51.770 goal pop + hop 1  hop landings haptics  52.813 goal impact
  53.0 / 53.5 tagline slams (with fly-in swoosh)  54.0 sunrise swell + soft boom  55.25 tab-bar whoosh
  55.5 spinning fall whoosh  56.0 magnetic snap + title slam  56.5 date swish  57.0 / 57.25 store toks
  57.75 stamp (medium)  58.0 button haptic  59.0 FINAL HIT.
"""
import os
import time
from functools import lru_cache

import numpy as np
import soundfile as sf
import pyloudnorm as pyln
from scipy.signal import butter, sosfilt, oaconvolve, resample_poly
from pedalboard import LadderFilter, PeakFilter, Compressor, Pedalboard, HighShelfFilter, LowShelfFilter

T_START = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
SR = 48000
NOUT = 60 * SR
N = NOUT + 5 * SR
R = np.random.default_rng(20260605)


# ============================================================ basic helpers
def T(d):
    return np.arange(int(round(d * SR))) / SR


def mtof(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def nz(d):
    return R.standard_normal(int(round(d * SR)))


@lru_cache(None)
def _sos(kind, f, order):
    return butter(order, f, btype=kind, fs=SR, output='sos')


def lp(x, f, o=2):
    return sosfilt(_sos('low', float(min(f, SR * 0.45)), o), x)


def hp(x, f, o=2):
    return sosfilt(_sos('high', float(f), o), x)


def bp(x, lo, hi, o=2):
    return sosfilt(_sos('band', (float(lo), float(min(hi, SR * 0.45))), o), x)


def fadeout(x, ms=5.0):
    n = max(2, int(ms * SR / 1000))
    x[..., -n:] *= np.linspace(1, 0, n)
    return x


def fadein(x, ms=0.6):
    n = max(2, int(ms * SR / 1000))
    x[..., :n] *= np.linspace(0, 1, n)
    return x


def sat(x, d):
    return np.tanh(x * d) / np.tanh(d)


def pan2(sig, pan=0.0):
    pan = np.clip(pan, -1, 1)
    l = np.cos((pan + 1) * np.pi / 4) * 1.4142
    r = np.sin((pan + 1) * np.pi / 4) * 1.4142
    return np.vstack([sig * l, sig * r])


def _blep(ph, dt):
    out = np.zeros_like(ph)
    m = ph < dt
    x = ph[m] / dt[m]
    out[m] = x + x - x * x - 1
    m2 = ph > 1 - dt
    x2 = (ph[m2] - 1) / dt[m2]
    out[m2] = x2 * x2 + x2 + x2 + 1
    return out


def saw_f(f, ph0=0.0, n=None):
    """Band-limited (polyBLEP) saw; f is a scalar (needs n) or a per-sample frequency array."""
    if np.isscalar(f):
        f = np.full(n, float(f))
    dt = np.clip(f / SR, 1e-7, 0.49)
    ph = (ph0 + np.cumsum(dt)) % 1.0
    return 2 * ph - 1 - _blep(ph, dt)


def sweep_filter(x, fcurve, mode='LPF24', res=0.15, block=64, drive=1.0):
    """Time-varying pedalboard ladder filter (block automation). x: (ch, n). fcurve: per-sample Hz."""
    x2 = np.atleast_2d(x).astype(np.float32)
    plug = LadderFilter(mode=getattr(LadderFilter.Mode, mode), cutoff_hz=float(fcurve[0]),
                        resonance=res, drive=drive)
    out = np.zeros_like(x2)
    n = x2.shape[1]
    for i in range(0, n, block):
        plug.cutoff_hz = float(np.clip(fcurve[min(i + block // 2, len(fcurve) - 1)], 20, 20000))
        out[:, i:i + block] = plug.process(x2[:, i:i + block], SR, reset=False)
    return out.astype(np.float64) if np.ndim(x) == 2 else out[0].astype(np.float64)


# ============================================================ buses + placement
BUS = {k: np.zeros((2, N)) for k in ['kick', 'bass', 'drums', 'pad', 'arp', 'lead', 'fx', 'pre', 'ui', 'plate', 'hall']}


MUTE = set(filter(None, os.environ.get('MUTE', '').split(',')))    # debug only: e.g. MUTE=arp,pad


def put(bus, sig, at, g=1.0, pan=0.0, plate=0.0, hall=0.0):
    if bus in MUTE:
        return
    sig = np.asarray(sig, dtype=np.float64)
    if sig.ndim == 1:
        sig = pan2(sig, pan)
    sig = fadein(sig.copy(), 1.0)
    i = int(round(at * SR))
    if i < 0:
        sig = sig[:, -i:]
        i = 0
    n = min(sig.shape[1], N - i)
    if n <= 0:
        return
    s = sig[:, :n] * g
    BUS[bus][:, i:i + n] += s
    if plate:
        BUS['plate'][:, i:i + n] += s * plate
    if hall:
        BUS['hall'][:, i:i + n] += s * hall


# ============================================================ harmony
CH = {'Fm': [5, 8, 0], 'Db': [1, 5, 8], 'Bbm': [10, 1, 5], 'C': [0, 4, 7], 'Gb': [6, 10, 1],
      'Eb': [3, 7, 10], 'Dbmaj7': [1, 5, 8, 0]}
ROOT = {'Fm': 5, 'Db': 1, 'Bbm': 10, 'C': 0, 'Gb': 6, 'Eb': 3, 'Dbmaj7': 1}
TL = [(0, 'Fm'), (1.5, 'Gb'), (4.0, 'Db'), (5.0, 'C'), (6.0, 'Fm'), (8.0, 'Db'), (9.0, 'C'),
      (10, 'Fm'), (14, 'Db'), (16, 'Eb'), (18, 'Fm'), (22, 'Db'), (24, 'C'), (26, 'Fm'), (28, 'Db'),
      (30, 'Bbm'), (32, 'C'), (34, 'Fm'), (36, 'Db'), (38, 'Eb'),
      (40, 'Dbmaj7'), (42, 'Bbm'), (44, 'Gb'), (45, 'Fm'), (47, 'Db'), (48, 'Eb'), (49, 'C'),
      (50, 'Fm'), (51, 'Db'), (52, 'Bbm'), (53, 'C'), (54, 'Fm'), (56, 'Db'), (58, 'Eb'), (59, 'Fm'), (61, 'Fm')]


def chord_at(t):
    c = TL[0][1]
    for t0, name in TL:
        if t + 1e-6 >= t0:
            c = name
    return c


def voicing(name, lo, hi):
    return [m for m in range(lo, hi + 1) if m % 12 in CH[name]]


def bass_midi(name):
    return 36 + ROOT[name]


# ============================================================ instruments
def kick(d=0.36, tail=0.12, drive=2.3, f_end=45.0, muffle=None, thin=False):
    t = T(d)
    f = f_end + 105 * np.exp(-t * 24) + 330 * np.exp(-t * 190)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.where(t < 0.045, 1.0, np.exp(-(t - 0.045) / tail))
    click = bp(nz(d), 1200, 5200) * np.exp(-t / 0.0022) * 0.42
    knock = bp(nz(d), 150, 900) * np.exp(-t / 0.014) * 0.7      # mid knock: the kick on a phone speaker
    beater = bp(nz(d), 1000, 3500) * np.exp(-t / 0.005) * 0.3    # beater: phone-speaker definition
    k = sat(body + click + knock + beater, drive)
    if muffle:
        k = lp(k, muffle, 2) * 1.5
    if thin:
        k = hp(k, 110, 2) * 1.2
    return fadeout(k, 8)


def clap():
    d = 0.4
    t = T(d)
    x = np.zeros(len(t))
    for off, g in [(0, 1.0), (0.007, 0.55), (0.014, 0.45)]:
        i = int(off * SR)
        b = bp(nz(0.03), 900, 7000) * np.exp(-T(0.03) / 0.0045) * g
        x[i:i + len(b)] += b
    i = int(0.004 * SR)
    tn = nz(d - 0.004)
    x[i:] += (bp(tn, 800, 3000) + hp(tn, 4000) * 0.6) * np.clip(T(d - 0.004) / 0.003, 0, 1) * np.exp(-T(d - 0.004) / 0.06) * 0.5
    x += lp(nz(d), 450) * np.exp(-t / 0.02) * 0.5
    return fadeout(x)


def rim():
    d = 0.08
    t = T(d)
    x = bp(nz(d), 700, 2600) * np.exp(-t / 0.005) + np.sin(2 * np.pi * 410 * t) * np.exp(-t / 0.014) * 0.7
    return fadeout(x)


def chat(dec=0.018):
    d = 0.07
    n = nz(d)
    x = hp(n, 4800, 4) * 0.8 + bp(n, 6500, 11000) * 0.45 + bp(n, 3000, 6000) * 0.25
    x = lp(x, 11000, 2)
    return fadeout(x * np.exp(-T(d) / dec))


def ohat():
    d = 0.32
    n = nz(d)
    x = lp(hp(n, 4500, 4) * 0.7 + bp(n, 6000, 11000) * 0.5 + bp(n, 2500, 5000) * 0.2, 11000, 2)
    t = T(d)
    return fadeout(x * np.clip(t / 0.002, 0, 1) * np.exp(-t / 0.085))


def shaker():
    d = 0.09
    t = T(d)
    x = bp(nz(d), 4000, 10000) * np.clip(t / 0.008, 0, 1) * np.exp(-np.maximum(t - 0.008, 0) / 0.022)
    return fadeout(x)


def snare(d=0.16, lo=900, hi=6000, body=1.0):
    t = T(d)
    x = bp(nz(d), lo, hi) * np.exp(-t / 0.045) + np.sin(2 * np.pi * 185 * t) * np.exp(-t / 0.03) * 0.5 * body
    return fadeout(x)


def bass_note(m, d=0.105, bright=0.4, subg=0.62, midg=1.0):
    f = mtof(m)
    fs = f
    while fs >= 72:
        fs /= 2
    while fs < 36:
        fs *= 2
    t = T(d + 0.03)
    amp = np.clip(t / 0.003, 0, 1) * np.exp(-t / 0.085)
    sub = np.sin(2 * np.pi * fs * t)
    mid = saw_f(f, R.random(), len(t)) + 0.7 * saw_f(f * 1.004, R.random(), len(t))
    fe = np.exp(-t / 0.035)
    mid = lp(mid, 300 + 1200 * bright, 2) * fe + lp(mid, 230, 2) * (1 - fe)
    mid = hp(mid, 90, 2)
    # asymmetric drive -> 2nd (and 3rd) harmonics so the line reads on small speakers
    mid = np.tanh(mid * 1.8 + 0.35) - np.tanh(0.35)
    mid = hp(mid, 120, 2)
    y = sat(sub * subg * 0.9, 1.6) + sat(mid * midg, 1.4)
    y = y * amp
    return fadeout(y, 10)


def pluck(m, d=0.3, bright=0.5, dec=0.15):
    f = mtof(m)
    t = T(d)
    n = len(t)
    x = saw_f(f, R.random(), n) + 0.7 * saw_f(f * 1.007, R.random(), n) + 0.3 * np.sin(2 * np.pi * f / 2 * t)
    fc = 330 + 3000 * bright
    fe = np.exp(-t / (0.018 + 0.05 * bright))
    y = lp(x, fc, 2) * fe + lp(x, max(fc * 0.35, 180), 2) * (1 - fe)
    y = lp(y, 4500, 2)
    amp = np.clip(t / 0.002, 0, 1) * np.exp(-t / dec)
    return fadeout(y * amp, 6)


def lead_note(m, d, bright=1.0, att=0.006):
    f = mtof(m)
    t = T(d + 0.09)
    n = len(t)
    x = (saw_f(f, R.random(), n) + saw_f(f * 1.0045, R.random(), n) + 0.9 * saw_f(f * 0.9955, R.random(), n)
         + 0.6 * np.sin(2 * np.pi * f / 2 * t))
    fe = np.exp(-t / 0.13)
    y = lp(x, 1100 + 900 * bright, 2) * fe + lp(x, 800, 2) * (1 - fe)
    y = lp(sat(y * 0.55, 2.0), 2400, 2)
    amp = np.clip(t / att, 0, 1) * np.where(t < d, 1.0, np.exp(-(t - d) / 0.03))
    return fadeout(y * amp, 6)


def pad(midis, d, att=0.4, rel=0.6, nv=5, det=0.17):
    n = int(d * SR)
    t = np.arange(n) / SR
    out = np.zeros((2, n))
    for m in midis:
        f = mtof(m)
        for v in range(nv):
            dv = (v - (nv - 1) / 2) / ((nv - 1) / 2) * det + R.normal(0, 0.012)
            fv = f * 2 ** (dv / 12) * (1 + 0.0016 * np.sin(2 * np.pi * (0.11 + 0.04 * v) * t + R.random() * 6.28))
            s = saw_f(fv, R.random())
            if v == (nv - 1) // 2:
                out += 0.6 * s
            else:
                out[v % 2] += s
    out /= np.sqrt(len(midis) * nv)
    env = np.ones(n)
    a = int(att * SR)
    r = int(rel * SR)
    if a > 0:
        env[:a] = np.sin(np.linspace(0, np.pi / 2, a)) ** 2
    if r > 0:
        env[-r:] *= np.cos(np.linspace(0, np.pi / 2, r)) ** 2
    return out * env


def braam(root, d=1.8, bright=1.0, swell=0.025, decay=0.6):
    t = T(d)
    n = len(t)
    notes = [root - 12, root, root + 7, root + 12]
    out = np.zeros((2, n))
    fe = np.clip(t / 0.05, 0, 1) * np.exp(-t / 0.35)
    for ch in range(2):
        s = np.zeros(n)
        for m in notes:
            for k in range(3):
                s += saw_f(mtof(m) * 2 ** (R.normal(0, 0.09) / 12), R.random(), n)
        y = lp(s, 1500 * bright, 2) * fe + lp(s, 330, 2) * (1 - fe)
        y = sat(y * 0.22, 3.5)
        out[ch] = lp(y, 3200, 2)
    amp = np.clip(t / swell, 0, 1) * np.exp(-t / decay)
    return fadeout(out * amp, 30)


def metal_body(d, base=110.0, decay=0.5, g=1.0):
    t = T(d)
    out = np.zeros((2, len(t)))
    ratios = [1.0, 1.593, 2.135, 2.653, 3.17, 4.07, 5.4]
    for ch in range(2):
        for k, r_ in enumerate(ratios):
            f = base * r_ * (1 + R.normal(0, 0.006))
            if f > 900:
                continue
            out[ch] += np.sin(2 * np.pi * f * t + R.random() * 6.28) * np.exp(-t / (decay / (1 + 0.35 * k))) / (1 + 0.25 * k)
    out = lp(out, 1300, 2) * g * 0.35
    return fadeout(out, 20)


def impact(size=1.0, sub0=78, sub1=32, sublen=0.9, metal=0.8, crack=1.0, base=110, body=0.8, mdecay=0.7):
    d = max(sublen, 1.0) + 0.3
    t = T(d)
    f = sub1 + (sub0 - sub1) * np.exp(-t * 7)
    sub = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / (sublen * 0.35))
    bod = lp(nz(d), 900, 2) * np.exp(-t / 0.06)
    crk = bp(nz(d), 1500, 7000) * np.exp(-t / 0.007) * crack
    mid = bp(nz(d), 250, 2500) * np.clip(t / 0.002, 0, 1) * np.exp(-t / 0.07) * 1.1   # crunch: reads on phones
    mono = sat(sub * 0.7 + bod * body + crk * 0.55 + mid, 2.4)
    st = pan2(mono, 0)
    if metal:
        st += metal_body(d, base, mdecay, metal)
    return fadeout(st * size, 30)


def stamp(size=1.0, base=170):
    d = 0.7
    t = T(d)
    f = 38 + 55 * np.exp(-t * 18)
    sub = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.13)
    thud = bp(nz(d), 120, 700) * np.exp(-t / 0.035) * 1.1
    crk = bp(nz(d), 1600, 6000) * np.exp(-t / 0.012) * 0.7
    mono = sat(sub * 0.75 + thud * 1.15 + crk, 2.6)
    st = pan2(mono, 0) + metal_body(d, base, 0.25, 0.6)
    return fadeout(st * size, 20)


def thud(size=1.0):
    d = 0.8
    t = T(d)
    f = 34 + 60 * np.exp(-t * 14)
    sub = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.18)
    bod = lp(nz(d), 500, 2) * np.exp(-t / 0.05) * 1.3
    crk = bp(nz(d), 900, 4000) * np.exp(-t / 0.006) * 0.5
    return fadeout(pan2(sat(sub * 0.7 + bod * 1.15 + crk, 2.2), 0) * size, 20)


def steam(d=0.75, g=1.0):
    t = T(d)
    out = np.zeros((2, len(t)))
    flutter = 1 + 0.35 * lp(nz(d), 25, 1) / 0.05
    env = np.clip(t / 0.01, 0, 1) * np.exp(-t / 0.2)
    for ch in range(2):
        out[ch] = lp(hp(nz(d), 2200, 2), 9000, 2) * env * np.clip(flutter, 0.3, 1.8)
    return fadeout(out * g * 0.6, 30)


def sizzle(g=1.0):
    d = 0.4
    t = T(d)
    out = np.zeros((2, len(t)))
    for ch in range(2):
        out[ch] = (bp(nz(d), 2500, 9000) * np.exp(-t / 0.035) + bp(nz(d), 3000, 8000) * np.exp(-t / 0.15) * 0.3)
    tk = bp(nz(d), 400, 1200) * np.exp(-t / 0.004) * 0.8
    return fadeout(out * 0.5 + pan2(tk, 0), 20) * g


def crackle(d=0.6, rate=120, g=1.0, tau=0.2, lo=900, hi=5000):
    n = int(d * SR)
    out = np.zeros((2, n))
    t = np.arange(n) / SR
    for ch in range(2):
        imp = np.zeros(n)
        k = R.poisson(rate * d)
        pos = R.integers(0, n, k)
        imp[pos] = R.uniform(-1, 1, k) * np.exp(-pos / SR / tau)
        out[ch] = bp(imp, lo, hi, 2) * 6
    return fadeout(out * g, 10)


def eruption(size=1.0, bright=1.0, d=1.0):
    t = T(d)
    n = nz(d)
    who = lp(n, 900 + 900 * bright, 2) * np.clip(t / 0.012, 0, 1) * np.exp(-t / 0.09) + lp(n, 300, 2) * np.exp(-t / 0.28) * 0.8
    f = 30 + 45 * np.exp(-t * 9)
    sub = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.2)
    crk = bp(nz(d), 1000, 6000) * np.exp(-t / 0.006) * 0.9
    mono = sat(who * 1.3 + sub * 0.65 + crk, 2.0)
    st = pan2(mono, 0) + crackle(d, 90, 0.5, 0.25)
    return fadeout(st * size, 25)


def splash(size=1.0):
    d = 0.6
    t = T(d)
    out = np.zeros((2, len(t)))
    for ch in range(2):
        out[ch] = bp(nz(d), 250, 2800) * np.clip(t / 0.004, 0, 1) * np.exp(-t / 0.11)
    out += crackle(d, 160, 0.4, 0.15, 700, 3500)
    out += pan2(lp(nz(d), 200) * np.exp(-t / 0.05), 0) * 0.8
    return fadeout(out * size, 20)


def tok(body=240.0, g=1.0, d=0.07, click=0.55, tau=0.018, sine=0.8):
    t = T(d)
    f = body * (1 + 0.35 * np.exp(-t * 90))
    b = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / tau)
    c = bp(nz(d), 1800, 5000) * np.exp(-t / 0.0025) * click
    return fadeout((b * sine + c) * g, 6)


def dry_tok(g=1.0):
    """unpitched premium tok: one fixed ~170 Hz body, mostly noise click (breakdown / map pins)."""
    return tok(170, g, 0.06, 1.0, 0.012, sine=0.4)


def haptic(g=1.0):
    return tok(150, g, 0.1, 0.35, 0.03)


def land_tick(g=1.0):
    d = 0.1
    t = T(d)
    c = bp(nz(d), 1800, 7000) * np.clip(t / 0.0008, 0, 1) * np.exp(-t / 0.003)
    return fadeout(haptic(1.0) + c * 0.75, 6) * g


def counter_lock(at, g=1.0):
    put('ui', land_tick(1.3 * g), at, 1.0, 0.45, plate=0.05)
    put('ui', tok(190, 0.3 * g, click=0.1), at + 0.032, 1.0, 0.45)


def ratchet(g=1.0):
    d = 0.03
    t = T(d)
    x = bp(nz(d), 1500, 6000) * np.exp(-t / 0.0012) + np.sin(2 * np.pi * 620 * t) * np.exp(-t / 0.005) * 0.35
    return fadeout(x * g, 3)


def typing(t0, t1, step, g=1.0, pan=0.0):
    """keyboard run = cloud of band-passed (1-4 kHz) noise grains at about -6 dB (no pitched body),
    framed by one soft tok at the start and one at the end."""
    n = int((t1 - t0 + 0.05) * SR)
    cloud = np.zeros((2, n))
    t = 0.0
    while t < t1 - t0 - 1e-6:
        d = 0.012
        gr = bp(nz(d), 1000, 4000) * np.clip(T(d) / 0.0006, 0, 1) * np.exp(-T(d) / 0.0022) * R.uniform(0.45, 1.0)
        gr = pan2(gr, pan + R.uniform(-0.25, 0.25))
        i = int(t * SR)
        cloud[:, i:i + gr.shape[1]] += gr[:, :n - i]
        t += step * R.uniform(0.7, 1.3)
    put('ui', fadeout(cloud, 10), t0, g * 0.5)
    put('ui', tok(220, 1.3 * g, 0.05, 0.7, 0.01, sine=0.5), t0, 1.0, pan)
    put('ui', tok(200, 0.9 * g, 0.05, 0.6, 0.01, sine=0.5), t1, 1.0, pan)


def whoosh(d, f0, f1, shape='bell', pan0=0.0, pan1=0.0, res=0.08, g=1.0, mode='BPF12', curve=1.0, peak=0.5):
    t = T(d)
    n = len(t)
    u = t / d
    base = nz(d)
    mono = base
    fc = f0 * (f1 / f0) ** (u ** curve)
    if shape == 'in':      # power-in: builds into the end (cut), tiny suck before the cut
        amp = suck(u ** 2.2, 0.018)
    elif shape == 'out':   # fast attack, decaying
        amp = np.clip(t / 0.012, 0, 1) * np.exp(-t / (d * 0.35))
    else:                  # bell, peak position adjustable
        amp = np.where(u < peak, (u / peak) ** 1.6, ((1 - u) / (1 - peak)) ** 1.4)
    y = sweep_filter(mono[None, :], fc, mode, res)[0] * amp
    p = pan0 + (pan1 - pan0) * u
    l = np.cos((p + 1) * np.pi / 4) * 1.4142
    r = np.sin((p + 1) * np.pi / 4) * 1.4142
    st = np.vstack([y * l, y * r])
    # decorrelated air layer for width
    air = sweep_filter(np.vstack([nz(d), nz(d)]), fc * 1.5, mode, 0.1) * amp * 0.35
    return fadeout((st + air) * g * 2.2, 8)


def flick(g=1.0):
    """fast-attack air transient that starts a motion (gives whooshes a clean onset)."""
    d = 0.09
    t = T(d)
    out = np.zeros((2, len(t)))
    for ch in range(2):
        out[ch] = bp(nz(d), 600, 4500) * np.clip(t / 0.002, 0, 1) * np.exp(-t / 0.02)
    out += pan2(lp(nz(d), 300) * np.exp(-t / 0.015), 0) * 0.6
    return fadeout(out * g, 6)


def reverse_swell(d, f0=500, f1=9000, g=1.0, gap=0.022):
    t = T(d)
    u = t / d
    out = np.zeros((2, len(t)))
    for ch in range(2):
        x = hp(nz(d), 300, 2)
        out[ch] = x
    fc = f0 * (f1 / f0) ** u
    out = sweep_filter(out, fc, 'LPF12', 0.0)
    amp = np.exp((u - 1) * 5.0) * u
    out *= amp
    suck(out, gap)
    return out * g


def suck(x, gap):
    """pre-hit 'suck': fade the last `gap` s out fast so the hit lands in a tiny hole."""
    n = int(gap * SR)
    f = int(0.012 * SR)
    x[..., -n - f:-n] *= np.linspace(1, 0, f) ** 2
    x[..., -n:] = 0
    return x


def riser(d, f0=250, f1=7000, g=1.0, tone_root=None, power=2.2, gap=0.022):
    t = T(d)
    u = t / d
    out = np.vstack([nz(d), nz(d)])
    fc = f0 * (f1 / f0) ** (u ** 1.3)
    out = sweep_filter(out, fc, 'BPF12', 0.04) * 2.0
    amp = u ** power
    out *= amp
    if tone_root is not None:   # rising low saw cluster (stays below 1.2 kHz)
        cl = np.zeros(len(t))
        for k, iv in enumerate([0, 7, 12]):
            fr = mtof(tone_root + iv) * 2 ** (u * 1.0)
            cl += saw_f(fr, R.random())
        cl = sweep_filter(cl[None, :], 300 * (4 ** u), 'LPF24', 0.2)[0] * amp * 0.25
        out += np.vstack([cl, cl * 0.9])
    suck(out, gap)
    return out * g


def crash(d=2.6, g=1.0, tau=0.75):
    t = T(d)
    out = np.zeros((2, len(t)))
    for ch in range(2):
        x = nz(d)
        out[ch] = (hp(x, 3200, 2) * np.exp(-t / tau) + bp(x, 5000, 11000) * np.exp(-t / (tau * 0.47)) * 0.6)
    out *= np.clip(t / 0.0015, 0, 1)
    out = lp(out, 11000, 2)
    return fadeout(out * g * 0.6, 50)


def sub_boom(d=2.0, f0=62, f1=30, g=1.0, tau=0.6):
    t = T(d)
    f = f1 + (f0 - f1) * np.exp(-t * 2.2)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.clip(t / 0.004, 0, 1) * np.exp(-t / tau)
    return fadeout(sat(x * 1.2, 1.5) * g * 0.8, 40)     # -2 dB vs v1 (phone translation)


def heartbeat(g=1.0):
    out = np.zeros(int(0.6 * SR))
    for off, a, f0 in [(0, 1.0, 68), (0.2, 0.7, 60)]:
        d = 0.32
        t = T(d)
        f = 40 + (f0 - 40) * np.exp(-t * 18)
        x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.clip(t / 0.004, 0, 1) * np.exp(-t / 0.08)
        x += lp(nz(d), 220) * np.exp(-t / 0.025) * 0.6
        x += bp(nz(d), 500, 1800) * np.exp(-t / 0.004) * 0.25
        i = int(off * SR)
        out[i:i + len(x)] += sat(x * a, 1.5)
    return fadeout(out * g, 10)


def sonar(g=1.0):
    """compass / map 'ping' without pitch: low sub thump + short band-passed noise ping."""
    d = 0.5
    t = T(d)
    x = np.sin(2 * np.pi * 55 * t) * np.clip(t / 0.004, 0, 1) * np.exp(-t / 0.09)
    x += lp(nz(d), 400) * np.exp(-t / 0.025) * 0.6
    x += bp(nz(d), 700, 2200) * np.clip(t / 0.002, 0, 1) * np.exp(-t / 0.04) * 0.35
    return fadeout(x * g, 20)


def denied(d=0.5):
    t = T(d)
    n = len(t)
    bend = 2 ** (-3 / 12 * np.clip(t / 0.12, 0, 1) ** 1.5)          # -3 semitones over 120 ms
    x = (saw_f(43.65 * bend) + 0.8 * saw_f(46.25 * bend * 1.003, 0.3) + 0.6 * saw_f(87.3 * bend, 0.6)
         + 0.4 * saw_f(130.8 * bend * 0.997, 0.2))                    # F1 / Gb1 rub + F2 / C3
    x = sat(x * 1.5, 4.0)                 # tanh drive only (no bit-crush)
    x = lp(x, 2400, 2)
    gate = np.zeros(n)
    for a_, b_, gg in [(0.0, 0.034, 1.0), (0.043, 0.074, 0.8), (0.084, 0.116, 0.9), (0.125, d, 1.0)]:
        i0, i1 = int(a_ * SR), int(b_ * SR)
        seg = np.ones(i1 - i0) * gg
        r_ = min(48, len(seg) // 3)
        seg[:r_] *= np.linspace(0, 1, r_)
        seg[-r_:] *= np.linspace(1, 0, r_)
        gate[i0:i1] = seg
    env = gate * np.where(t < 0.125, 1.0, np.exp(-(t - 0.125) / 0.12))
    y = x * env + bp(nz(d), 1000, 5000) * env * 0.15
    st = np.vstack([y, np.roll(y, 37)])
    return fadeout(st * 0.6, 15)


def crt_off(d=0.32):
    t = T(d)
    n = len(t)
    u = np.clip(t / 0.2, 0, 1)
    hum = saw_f(110 * (0.18 ** u), 0.0, n)
    hum = lp(hum, 700, 2) * (1 - u) ** 1.5 * 0.5
    nzz = sweep_filter(nz(d)[None, :], 7000 * (0.015 ** u), 'LPF12', 0.0)[0] * (1 - u) ** 1.2
    crk = bp(nz(d), 1500, 6000) * np.exp(-t / 0.006) * 0.7
    thk = np.sin(2 * np.pi * np.cumsum(70 * (0.5 ** u)) / SR) * np.exp(-t / 0.12) * 0.8
    mono = hum + nzz * 0.9 + crk + thk
    return fadeout(pan2(mono, 0), 20)


def crt_on(d=1.2):
    t = T(d)
    n = len(t)
    sub = np.sin(2 * np.pi * np.cumsum(30 + 50 * np.exp(-t * 10)) / SR) * np.exp(-t / 0.3)
    crk = bp(nz(d), 1200, 7000) * np.exp(-t / 0.01)
    stat = crackle(d, 400, 0.6, 0.12, 1500, 7000)
    hum = lp(saw_f(50 + 60 * np.clip(t / 0.15, 0, 1), 0.0, n), 500, 2) * np.exp(-t / 0.25) * 0.4
    mono = sat(sub * 0.55 + crk * 0.6 + hum, 2.0)
    return fadeout(pan2(mono, 0) + stat + metal_body(d, 95, 0.6, 0.6), 30)


def make_ir(d, rt60, lp0, lp1, pre=0.012, seed=1, hp_f=180, er=True):
    rng = np.random.default_rng(seed)
    n = int(d * SR)
    t = np.arange(n) / SR
    env = 10 ** (-3 * t / rt60)
    ir = np.zeros((2, n + int(pre * SR)))
    for ch in range(2):
        w = rng.standard_normal(n)
        mixw = np.clip(t / (rt60 * 0.5), 0, 1)
        x = (lp(w, lp0) * (1 - mixw) + lp(w, lp1) * mixw) * env
        x = hp(x, hp_f)
        x[:int(0.006 * SR)] *= np.linspace(0, 1, int(0.006 * SR))
        if er:
            for k in range(6):
                p = int(rng.uniform(0.003, 0.035) * SR)
                x[p] += rng.uniform(-1, 1) * 2.5
        ir[ch, int(pre * SR):] = x
    ir /= np.sqrt((ir ** 2).sum(1).mean())
    return ir


def convolve_wide(x_st, ir, n_out=None):
    m = x_st.mean(0)
    n_out = n_out or x_st.shape[1]
    return np.vstack([oaconvolve(m, ir[c])[:n_out] for c in range(2)])


def pingpong(x_st, delay, fb, taps=6, lo=250, hi=3500):
    out = np.zeros_like(x_st)
    d = int(delay * SR)
    y = x_st.mean(0)
    for k in range(1, taps + 1):
        y = lp(hp(y, lo, 1), hi, 1) * fb
        if k * d >= y.shape[0]:
            break
        out[(k - 1) % 2, k * d:] += y[:-k * d]
    return out


def duck_env(events):
    """events: list of (t, depth, release_s). Returns gain curve (min of all shapes)."""
    g = np.ones(N)
    att = int(0.004 * SR)
    for t0, depth, rel in events:
        i0 = int(t0 * SR) - att
        r = int(rel * SR)
        n = att + r
        c = np.empty(n)
        c[:att] = 1 - depth * np.linspace(0, 1, att)
        c[att:] = 1 - depth * (1 - np.linspace(0, 1, r)) ** 2
        a, b = max(i0, 0), min(i0 + n, N)
        if b > a:
            g[a:b] = np.minimum(g[a:b], c[a - i0:b - i0])
    return g


def curve(points, n=N):
    ts, vs = zip(*points)
    return np.interp(np.arange(n) / SR, ts, vs)


# ============================================================ MUSIC: drums
kick_times = []          # (t, kind)
for i in range(7):
    kick_times.append((6.0 + 0.5 * i, 'lvl'))
for i in range(60):
    kick_times.append((10.0 + 0.5 * i, 'full'))
for i in range(8):
    kick_times.append((45.0 + 0.5 * i, 'thin'))
for i in range(17):
    kick_times.append((50.0 + 0.5 * i, 'drop' if i < 8 else 'full'))

K_FULL = kick()
K_THIN = kick(thin=True)
K_DROP = kick(drive=2.8, tail=0.14)
for t0, kind in kick_times:
    sig = {'lvl': K_FULL, 'full': K_FULL, 'thin': K_THIN, 'drop': K_DROP}[kind]
    g = {'lvl': 0.8, 'full': 1.0, 'thin': 0.7, 'drop': 1.1}[kind]
    put('kick', sig, t0, g)
# muffled kicks in REJOUER
for t0 in (4.5, 5.5):
    put('kick', kick(muffle=260), t0, 0.6)
put('kick', K_FULL, 5.0, 0.8)
# final kick with long F tail
put('kick', kick(d=1.0, tail=0.18, drive=2.6, f_end=43.65), 59.0, 1.15)


def in_ranges(t, ranges):
    return any(a - 1e-6 <= t < b - 1e-6 for a, b in ranges)


GROOVE = [(10, 40), (50, 58.5)]
for b in range(int(6 / 0.5), int(60 / 0.5)):
    beat = b * 0.5
    bar_pos = (b % 4)
    # closed hats on the 3 sixteenths after each beat (swing on e / a)
    if in_ranges(beat, [(8, 40), (45, 49.5), (50.5, 51.5), (52.75, 58.5)]):
        lvl = 0.5 if beat < 10 else (0.7 if beat < 45 or beat >= 50 else 0.45 + 0.1 * (beat - 45))
        for s, v in [(1, 0.4), (2, 0.85), (3, 0.5)]:
            tt = beat + s * 0.125 + (0.011 if s != 2 else 0)
            if s == 2 and in_ranges(beat, [(18, 40), (50, 58.5)]):
                put('drums', ohat(), tt, 0.55 * lvl, -0.25, plate=0.1)
                v = 0.3
            put('drums', chat(0.014 + 0.01 * (s == 2)), tt, v * lvl * R.uniform(0.85, 1.05), 0.38)
    # shaker
    if in_ranges(beat, [(26, 40), (50, 51.5), (52.75, 58.5)]):     # (out during the hop landings, like the hats)
        for s in range(4):
            put('drums', shaker(), beat + s * 0.125 + (0.008 if s % 2 else 0), 0.22 * (1.3 if s == 2 else 1.0), -0.55)
    # clap on 2 & 4
    if bar_pos in (1, 3) and in_ranges(beat, GROOVE):
        put('drums', clap(), beat, 0.55, 0.0, plate=0.55)
    # rim ghosts
    if in_ranges(beat, [(26, 40), (50, 58.5)]) and bar_pos == 2:
        put('drums', rim(), beat + 0.375, 0.28, 0.35, plate=0.4)
    if in_ranges(beat, [(34, 40)]) and bar_pos == 3:
        put('drums', rim(), beat + 0.125 + 0.011, 0.2, -0.3, plate=0.4)
# drum fill before the breakdown
for k, tt in enumerate(np.arange(39.0, 39.5, 0.0625)):
    put('drums', snare(0.12, 900, 5000), tt, 0.12 + 0.05 * k, 0.15 * np.sin(k), plate=0.2)

# ============================================================ MUSIC: bass
for b in range(int(10 / 0.5), int(58.5 / 0.5)):
    beat = b * 0.5
    if not in_ranges(beat, GROOVE):
        continue
    name = chord_at(beat)
    root = bass_midi(name)
    bright = float(np.interp(beat, [10, 18, 26, 40, 50, 54, 58], [0.22, 0.32, 0.5, 0.6, 0.75, 0.55, 0.5]))
    if 51.5 <= beat < 52.75:
        # hop landings (off the 16th grid): the roll stops, one held note per beat so the ticks read
        if beat < 52.5:
            put('bass', bass_note(root, 0.3, bright * 0.6), beat + 0.125, 0.8)
        continue
    for s, v in [(1, 0.8), (2, 1.0), (3, 0.85)]:
        m = root + (12 if (s == 3 and beat >= 26 and (b % 8) in (3, 7)) else 0)
        put('bass', bass_note(m, 0.105, bright), beat + s * 0.125, v)

# ============================================================ MUSIC: arp
ARP_PAT = [0, 2, 4, 1, 3, 5, 2, 4, 0, 2, 4, 1, 5, 3, 2, 1]
ARP_PAT2 = [0, 3, 5, 2, 4, 1, 3, 5, 0, 3, 5, 2, 1, 4, 3, 2]    # 30-40 and drop: new contour, same cell length
arp_bright_pts = [(6, 0.08), (10, 0.28), (15, 0.33), (20, 0.42), (25, 0.5), (30, 0.6), (35, 0.7), (40, 0.42),
                  (45, 0.15), (49.9, 0.95), (50, 0.85), (54, 0.65), (58.5, 0.6)]
arp_gain_pts = [(6, 0.35), (10, 0.5), (20, 0.55), (30, 0.62), (39.9, 0.68), (40, 0.42), (44.9, 0.38), (45, 0.3),
                (49.9, 0.75), (50, 0.72), (54, 0.62), (58.5, 0.55)]
step = 0
for k in range(int(6 / 0.125), int(58.5 / 0.125)):
    tt = k * 0.125
    if 9.94 < tt < 10.0 or 51.45 < tt < 52.9 or 50.0 < tt < 50.25:
        continue
    name = chord_at(tt)
    vo = voicing(name, 53, 72)
    pat = ARP_PAT2 if (30 <= tt < 40 or tt >= 50) else ARP_PAT
    m = vo[pat[k % 16] % len(vo)]
    br = float(np.interp(tt, *zip(*arp_bright_pts)))
    gn = float(np.interp(tt, *zip(*arp_gain_pts)))
    if 20 <= tt < 40:      # 3-against-4 accent cycle: the arp phrase rotates against the bar
        acc = 1.12 if k % 3 == 0 else 0.74
    else:
        acc = 1.0 if k % 4 == 2 else (0.8 if k % 2 else 0.9)
    pan = 0.35 * np.sin(k * 0.7)
    put('arp', pluck(m, 0.32, br, 0.11 + 0.06 * br), tt + (0.008 if k % 2 else 0), gn * acc, pan, hall=0.18)
# arp 2: low polymetric pluck (3-step cycle)
for k in range(int(26 / 0.125), int(58.5 / 0.125)):
    tt = k * 0.125
    if not in_ranges(tt, [(26, 40), (50, 58.5)]) or k % 3:
        continue
    vo = voicing(chord_at(tt), 41, 56)
    m = vo[(k // 3) % len(vo)]
    put('arp', pluck(m, 0.28, 0.25, 0.09), tt, 0.32, -0.25, hall=0.1)

# ============================================================ MUSIC: pads
for i in range(len(TL) - 1):
    t0, name = TL[i]
    t1 = TL[i + 1][0]
    if t1 > 60.5:
        t1 = 60.5
    if 3.0 <= t0 < 4.0:
        continue
    vo = voicing(name, 55, 70)
    low = [m for m in range(43, 55) if m % 12 == ROOT[name]][:1]
    seg_end = min(t1, 3.05) if t0 < 3 else t1
    att = 0.35 if t0 not in (40, 54, 59) else (0.6 if t0 != 59 else 0.01)
    if t0 == 0:
        att = 0.02
    p = pad(low + vo, seg_end - t0 + 0.45, att=att, rel=0.45)
    if t0 == 59:           # final chord rings out (tau 0.45 s) instead of sustaining under the hit
        p *= np.exp(-np.arange(p.shape[1]) / SR / 0.3)[None, :]
    put('pad', p, t0, 1.0)

# ============================================================ MUSIC: lead (drop + end card)
MEL = [(50.0, 72, .22), (50.25, 68, .22), (50.5, 65, .22), (50.75, 67, .22),
       (51.0, 68, .35), (51.375, 65, .1), (51.5, 61, .22), (51.75, 65, .22),
       (52.0, 70, .22), (52.25, 65, .22), (52.5, 73, .22), (52.75, 72, .22),
       (53.0, 64, .35), (53.375, 67, .1), (53.5, 72, .45),
       (54.0, 72, .7), (54.75, 68, .22), (55.0, 65, .45), (55.5, 67, .45),
       (56.0, 68, .7), (56.75, 65, .22), (57.0, 65, .45), (57.5, 68, .45), (58.0, 67, .45)]
for t0, m, d in MEL:
    soft = 51.7 < t0 < 52.75          # hop landings: lead notes swell in (15 ms) so the landing ticks lead
    put('lead', lead_note(m, d, 1.0 if t0 < 54 else 0.6, 0.015 if soft else 0.006), t0, 0.5, 0.0, plate=0.25, hall=0.15)
# sparse low motif from 30 s (C4..Ab4) that pre-echoes the drop line (Ab-F-G / C)
MOTIF = [(30.0, 65, .7), (30.75, 61, .22), (31.0, 60, .9),
         (32.0, 67, .7), (32.75, 64, .22), (33.0, 60, .9),
         (34.0, 68, .7), (34.75, 65, .22), (35.0, 67, .9),
         (36.0, 68, .7), (36.75, 65, .22), (37.0, 61, .9),
         (38.0, 67, .7), (38.75, 63, .22), (39.0, 60, .7)]
for t0, m, d in MOTIF:
    put('lead', lead_note(m, d, 0.35), t0, 0.26 + 0.04 * (t0 - 30) / 9, -0.15, plate=0.3, hall=0.25)

# ============================================================ SFX / cue placement
FX = 'fx'
HITS = []   # (t, depth, rel) for the music side-chain


def big(t, depth=0.55, rel=0.5):
    HITS.append((t, depth, rel))


# ---- 0-4 HOOK
lava = np.zeros((2, int(3.1 * SR)))
tl = np.arange(lava.shape[1]) / SR
for ch in range(2):
    lava[ch] = lp(nz(3.1), 160, 2) * (0.7 + 0.3 * np.sin(2 * np.pi * (0.7 + 0.2 * ch) * tl)) * 1.6
lava += crackle(3.1, 25, 0.25, 9.0, 600, 3000)
lava *= np.clip(tl / 0.004, 0, 1)
lava[:, -int(0.3 * SR):] *= np.linspace(1, 0, int(0.3 * SR))
put(FX, lava, 0.0, 0.5)
put(FX, sub_boom(1.2, 55, 32, 1.0, 0.35), 0.0, 0.7)
put(FX, flick(1.0), 0.02, 1.0)
put(FX, tok(110, 1.2, 0.2, 0.6, 0.06), 0.02, 0.8, hall=0.3)
put(FX, tok(120, 0.6, 0.12, 0.2, 0.05), 0.163, 0.4, -0.2, hall=0.2)
put(FX, tok(110, 0.5, 0.12, 0.2, 0.05), 0.325, 0.4, 0.2, hall=0.2)
# 0.5 swallow
t_ = T(0.9)
gulp = np.sin(2 * np.pi * np.cumsum(35 + 55 * np.exp(-t_ * 9)) / SR) * np.clip(t_ / 0.003, 0, 1) * np.exp(-t_ / 0.22)
put(FX, sat(gulp * 1.3, 1.8) + 0, 0.5, 0.9)
put(FX, lp(nz(0.4), 350) * np.exp(-T(0.4) / 0.05) * 1.5, 0.5, 0.8)
put(FX, splash(0.8), 0.5, 0.6, hall=0.2)
put(FX, steam(0.6, 0.5), 0.55, 0.6)
# pre-slam sucks
for ts in (0.775, 1.275):
    put(FX, flick(1.0), ts, 1.0)
    put(FX, reverse_swell(0.225, 400, 6000, 1.0), ts, 0.8)
# GAME / OVER
# GAME braam is choked at 1.45 (30 ms suck) so OVER lands in a hole; OVER = +1.5 dB, deeper sub start,
# longer braam, more hall: the second slam is the bigger one.
bg = braam(41, 1.6)
bg[:, int(0.45 * SR) - int(0.03 * SR):int(0.45 * SR)] *= np.linspace(1, 0, int(0.03 * SR)) ** 2
bg[:, int(0.45 * SR):] = 0
put(FX, impact(1.0, 80, 30, 1.0, 0.9, 1.0, 105), 1.0, 0.95, hall=0.3)
put(FX, bg, 1.0, 0.75, hall=0.22)
put(FX, crash(1.6, 0.5), 1.0, 0.5)
big(1.0, 0.7, 0.45)
put(FX, impact(1.0, 68, 28, 1.3, 1.1, 1.2, 98), 1.5, 0.95 * 1.19, hall=0.45)
put(FX, braam(42, 2.6), 1.5, 0.75 * 1.19, hall=0.42)
put(FX, crash(2.0, 0.6), 1.5, 0.5)
big(1.5, 0.75, 0.7)
# 2.0 card flip + 2.25 subline
put(FX, flick(1.3), 2.0, 0.9, 0.5)
put(FX, whoosh(0.32, 400, 3500, 'out', 0.6, 0.3, g=0.6), 2.0, 0.8)
put('ui', tok(230, 1.3, click=0.9, sine=0.5), 2.0, 1.0, 0.5)
put('ui', tok(260, 1.6, click=0.9), 2.25, 1.0, 0.2)
for k, ts in enumerate([2.294, 2.338, 2.381, 2.425, 2.469]):
    put('ui', tok(260, 0.25), ts, 1.0, 0.2)
# 2.5 DEAD
put(FX, denied(0.55), 2.5, 0.85, hall=0.15)
put(FX, flick(0.9), 2.5, 1.0, 0.4)
put(FX, sub_boom(0.6, 50, 32, 0.6, 0.15), 2.5, 0.5)
put('ui', tok(200, 0.4, click=0.3), 2.625, 1.0, 0.4)
put('ui', tok(200, 0.35, click=0.3), 2.75, 1.0, 0.4)

# ---- 4-6 REJOUER
put(FX, crt_on(1.2), 4.0, 1.0, hall=0.25)
put(FX, impact(0.8, 70, 32, 0.7, 0.5, 0.8, 95), 4.0, 0.8, hall=0.25)
big(4.0, 0.5, 0.5)
put('ui', tok(250, 1.1), 4.5, 1.0)
put(FX, whoosh(0.25, 500, 3000, 'out', -0.5, 0.0, g=0.35), 4.5, 1.0)
put(FX, whoosh(0.25, 500, 3000, 'out', 0.5, 0.0, g=0.35), 4.5, 1.0)
# PRESS
put('ui', haptic(1.6), 5.0, 1.0)
put(FX, impact(1.0, 85, 34, 0.9, 0.8, 1.0, 130), 5.0, 0.9, hall=0.35)
put(FX, crash(1.2, 0.35), 5.0, 1.0)
big(5.0, 0.6, 0.45)
pu = pad([48, 55, 60, 61], 1.0, att=0.7, rel=0.05)          # C-G-C-Db (b9): tension, no major third
pu = sweep_filter(pu, 300 * (8 ** (T(1.0) / 1.0)), 'LPF24', 0.3)
put(FX, pu, 5.0, 0.9, hall=0.2)
# dive 5.5 -> 6.0
for k, tt in enumerate(np.arange(5.5, 5.94, 0.0625)):
    put('drums', snare(0.12, 1000 + 300 * k, 6000), tt, 0.18 + 0.05 * k, 0.0, plate=0.15)
put(FX, reverse_swell(0.5, 400, 10000, 1.2), 5.5, 1.0)
put(FX, flick(0.9), 5.5, 1.0)
put(FX, lp(nz(0.3), 400) * np.clip(T(0.3) / 0.004, 0, 1) * np.exp(-T(0.3) / 0.06) * 1.6, 5.75, 0.8, hall=0.2)
put(FX, flick(0.5), 5.75, 1.0)

# ---- 6-10 NIVEAU 1
put(FX, crash(2.4, 0.8), 6.0, 1.0)
put(FX, flick(1.0), 6.0, 1.0)
put(FX, impact(1.0, 80, 30, 1.0, 0.9, 2.0, 120), 6.15, 0.95, hall=0.35)
put(FX, flick(1.6), 6.15, 1.0)
put(FX, crash(0.3, 1.2, tau=0.03), 6.15, 1.0)
put(FX, braam(41, 1.2, 0.8), 6.15, 0.45, hall=0.25)
big(6.15, 0.55, 0.5)
put(FX, metal_body(0.6, 180, 0.3, 1.6), 6.375, 0.8, plate=0.2)
put(FX, tok(200, 1.0, 0.1, 0.8, 0.03), 6.375, 0.8, plate=0.2)
put('ui', land_tick(1.8), 6.375, 1.0)
put(FX, flick(1.8), 6.375, 1.0)
ERX = [350, 1500, 960, 445, 1460, 715, 1540, 500]
for i, x in enumerate(ERX):
    put(FX, eruption(0.75 + 0.04 * i, 0.4 + 0.08 * i, 0.8), 7.0 + 0.25 * i + (-0.013 if i == 1 else 0), 0.85, (x - 960) / 960 * 0.75, hall=0.2)
put(FX, splash(1.0), 7.237, 0.7, -0.1, hall=0.15)
put(FX, flick(0.9), 7.237, 1.0, 0.2)
# overheat 9 -> 10
for k, tt in enumerate(np.arange(9.0, 10.0, 0.0625)):
    if tt >= 9.5:
        for sub_ in (0.0, 0.03125):
            if tt + sub_ > 9.9:          # 100 ms hole before the 10.0 hit
                continue
            put('drums', snare(0.1, 1200 + 900 * (tt - 9), 7000), tt + sub_, 0.32 + 0.35 * (tt - 9.5) * 2, 0.0, plate=0.15)
    else:
        put('drums', snare(0.12, 1000 + 600 * (tt - 9), 6000), tt, (0.2 + 0.18 * (tt - 9) * 2) * (1.6 if k == 0 else 1.0), 0.0, plate=0.15)
rz = riser(1.0, 250, 8000, 0.7, tone_root=41, gap=0.035)
rz[:, int(0.47 * SR):int(0.5 * SR)] *= 0.15
put(FX, rz, 9.0, 1.0, hall=0.15)
put(FX, flick(1.4), 9.5, 1.0)
put(FX, crash(0.5, 0.6, tau=0.08), 9.5, 1.0)
put(FX, tok(120, 1.3, 0.2, 0.5, 0.05), 9.5, 1.0)
tt_ = T(1.0)
trem = np.sin(2 * np.pi * 42 * tt_) * (0.5 + 0.5 * np.sign(np.sin(2 * np.pi * 16 * tt_))) * (tt_ / 1.0) ** 1.5
put(FX, lp(trem, 120) * 0.6, 9.0, 1.0)
put(FX, reverse_swell(0.5, 500, 11000, 1.0, gap=0.035), 9.5, 1.0)

# ---- 10-40 POWER-UPS
for P in (10, 15, 20, 25, 30, 35):
    put(FX, eruption(1.1, 1.0, 1.0), P, 0.9, 0.0, hall=0.25)
    put(FX, impact(0.9, 75, 32, 0.8, 0.6, 0.9, 115 + P), P, 0.8, hall=0.3)
    big(P, 0.5, 0.45)
    if P == 10:
        put(FX, flick(2.0), P, 1.0)
        put(FX, crash(0.3, 1.8, tau=0.03), P, 1.0)
        put(FX, lp(nz(0.3), 2500) * np.exp(-T(0.3) / 0.03) * 1.0, P, 1.0)
    if P in (10, 20, 30):
        put(FX, crash(2.6, 0.8), P, 1.0)
        put(FX, sub_boom(1.6, 60, 30, 1.0, 0.45), P, 0.6)
    else:
        put(FX, crash(1.4, 0.45), P, 1.0)
    # whip-pan out at P+4.5 (builds into the cut at P+5)
    put(FX, whoosh(0.5, 300, 6500, 'in', 0.5, -0.7, g=1.0, curve=1.6), P + 4.5, 0.9, hall=0.1)
    put(FX, flick(0.9), P + 4.5, 1.0, 0.4)
    # counter increment
    counter_lock(P + 2.12)

# P = 10 navettes
for P in (10, 15, 35):
    put(FX, whoosh(0.5, 2500, 300, 'in', 0.0, 0.0, g=0.8, curve=1.0), P + 0.5, 1.0, hall=0.1)
    put(FX, flick(0.4), P + 0.5, 1.0)
    put(FX, thud(1.0), P + 1.0, 0.95, plate=0.1)
    put(FX, splash(1.0), P + 1.0, 0.7, hall=0.15)
    put(FX, steam(0.8, 1.0), P + 1.02, 0.7)
    put(FX, sizzle(1.0), P + 1.14, 0.95, plate=0.1)
    put(FX, flick(1.2), P + 1.0, 1.0)
    put(FX, crash(0.25, 0.9, tau=0.025), P + 1.0, 1.0)
    big(P + 1.0, 0.45, 0.35)
for P in (10, 15, 20, 25, 30, 35):
    put(FX, stamp(1.0, 160 + P), P + 1.5, 1.0, plate=0.35, hall=0.1)
    put(FX, crash(0.9, 0.25), P + 1.5, 1.0)
    big(P + 1.5, 0.5, 0.35)

# 10: showcase
put('ui', tok(240, 1.1, click=0.9, sine=0.5), 12.0, 1.0, 0.3)
put('ui', tok(240, 0.6), 12.5, 1.0, 0.3)
put(FX, whoosh(0.3, 600, 3000, 'out', 0.2, -0.1, g=0.35), 13.0, 1.0)
put('ui', tok(220, 0.8), 13.0, 1.0)
typing(13.5, 13.815, 0.011, 0.45, 0.1)
put(FX, whoosh(0.25, 400, 2500, 'bell', -0.6, -0.2, g=0.35, peak=0.3), 13.5, 1.0)
put('ui', haptic(1.0), 14.0, 1.0, -0.2)
# 15: objets interdits
for k, ts in enumerate([16.1, 16.163, 16.225, 16.288, 16.35, 16.413, 16.475, 16.538]):
    put(FX, sizzle(0.1 if k == 0 else 0.25), ts, 1.0, -0.6 + k * 0.17)
put('ui', tok(230, 1.4, click=0.9, sine=0.5), 17.0, 1.0)
put(FX, flick(1.0), 17.063, 1.0)
put(FX, whoosh(0.3, 500, 4500, 'out', 0.0, 0.0, g=0.5), 17.063, 1.0)
for ts, pa in ((17.5, 0.5), (18.0, -0.5)):
    put(FX, whoosh(0.3, 600, 3000, 'bell', -pa, pa, g=0.45, peak=0.35), ts, 1.0)
    put(FX, flick(0.3), ts, 1.0, pa)
put(FX, whoosh(0.3, 4000, 500, 'out', 0.0, 0.0, g=0.45), 18.5, 1.0)
put(FX, whoosh(0.25, 400, 2500, 'bell', -0.6, -0.2, g=0.3, peak=0.3), 18.5, 1.0)
put('ui', land_tick(1.5), 19.0, 1.0, -0.2)
# 20: plan
put(FX, whoosh(0.45, 300, 3500, 'bell', 0.0, 0.0, g=0.6, peak=0.4), 20.5, 1.0, hall=0.1)
put(FX, flick(1.0), 20.5, 1.0)
put(FX, crackle(0.5, 200, 0.35, 0.3, 200, 1200), 20.5, 0.7)
put(FX, lp(nz(0.5), 150) * np.exp(-T(0.5) / 0.2), 20.5, 0.7)
put(FX, thud(0.75), 21.0, 0.9, plate=0.1)
put(FX, flick(0.9), 21.0, 1.0)
for k, ts in enumerate([21.0, 21.25, 21.5, 21.75, 22.0, 22.25]):
    put('ui', dry_tok(1.5 if k == 4 else 1.0), ts, 1.0, -0.5 + 0.2 * k, plate=0.05)
put('ui', land_tick(1.5), 22.0, 1.0, -0.6)
put('ui', haptic(0.8), 22.5, 1.0, 0.1)
put('ui', land_tick(3.0), 22.56, 1.0, 0.1)
put('ui', tok(240, 1.4, click=0.9, sine=0.5), 23.0, 1.0, -0.2)
put(FX, whoosh(0.4, 500, 2000, 'bell', -0.2, 0.1, g=0.25), 23.0, 1.0)
for k, ts in enumerate([23.5, 23.75, 24.0]):
    put(FX, sonar(1.0 - 0.25 * k), ts, 0.8, -0.2, hall=0.25)
# 25: clash
put(FX, whoosh(0.25, 400, 3000, 'in', -0.9, -0.1, g=0.6), 25.0, 1.0)
put(FX, whoosh(0.25, 400, 3000, 'in', 0.9, 0.1, g=0.6), 25.0, 1.0)
put(FX, impact(1.0, 70, 32, 0.7, 1.4, 1.2, 140), 25.25, 0.95, hall=0.35)
put(FX, crackle(0.5, 300, 0.7, 0.12), 25.25, 1.0)
big(25.25, 0.55, 0.4)
put(FX, whoosh(0.36, 300, 3000, 'out', 0.0, 0.0, g=0.55), 25.5, 1.0)
put(FX, flick(1.0), 25.5, 1.0)
put(FX, pan2(lp(nz(0.6), 200) * np.exp(-T(0.6) / 0.2), 0) * 0.6, 26.0, 0.8)
for ts in (27.0, 27.5, 28.0):
    put('ui', haptic(1.0), ts, 1.0, 0.2)
    put('ui', tok(320, 0.5, 0.04, 0.6, 0.008), ts + 0.01, 1.0, 0.2)
for ts in (26.75, 27.25, 27.75):
    put('ui', tok(250, 0.25), ts, 1.0, 0.2)
put('ui', haptic(1.6), 28.5, 1.0)
put(FX, stamp(0.7, 210), 28.5, 1.0, plate=0.3)
big(28.5, 0.4, 0.3)
put(FX, whoosh(0.4, 400, 2500, 'bell', -0.7, -0.1, g=0.3, peak=0.3), 28.5, 1.0)
put('ui', haptic(1.0), 29.0, 1.0, -0.1)
# 30: food
put(FX, whoosh(0.2, 500, 2500, 'bell', 0.0, 0.0, g=0.25), 30.44, 1.0)
for k, ts in enumerate([30.5, 30.75, 31.0, 31.25]):
    put('ui', land_tick(1.4), ts, 1.0, -0.4 + 0.25 * k)
for k, ts in enumerate([31.0, 31.25, 31.5, 31.75]):
    put(FX, whoosh(0.2, 3000, 500, 'in', 0.0, 0.0, g=0.35), ts - 0.2, 1.0)
    put(FX, thud(0.65 + (0.25 if k == 3 else 0)), ts, 0.9, 0.15 * (k - 1.5), plate=0.08)
    put(FX, splash(0.4), ts, 0.6)
put(FX, whoosh(0.34, 500, 4000, 'out', 0.0, 0.0, g=0.45), 32.0, 1.0)
for ts in (32.5, 33.0, 33.5):
    put(FX, whoosh(0.3, 600, 3500, 'out', 0.4, -0.4, g=0.4), ts, 1.0)
for ts in (32.02, 32.52, 33.02, 33.52):
    put('ui', tok(270, 0.3), ts, 1.0, 0.3)
put(FX, whoosh(0.4, 400, 2500, 'bell', -0.7, -0.1, g=0.3, peak=0.3), 33.5, 1.0)
put('ui', haptic(1.1), 34.0, 1.0)
# 35: cashless
put(FX, crackle(0.5, 200, 0.6, 0.2, 1500, 6000), 36.5, 1.0)
for ts in (37.0, 37.5, 38.0):
    put('ui', tok(235, 1.0), ts, 1.0, -0.1)
put(FX, whoosh(0.3, 500, 3000, 'out', -0.3, 0.3, g=0.4), 38.5, 1.0)
for ts in (38.56, 38.62, 38.68):
    put('ui', tok(260, 0.35), ts, 1.0, 0.2)
put('ui', haptic(1.1), 39.0, 1.0)

# ---- 40-45 BREAKDOWN
put(FX, eruption(0.7, 0.4, 1.2), 40.0, 0.8, hall=0.4)
put(FX, sub_boom(2.0, 55, 30, 0.8, 0.6), 40.0, 1.0)
put(FX, reverse_swell(0.5, 300, 6000, 0.6, gap=0.035), 39.5, 1.0)
put(FX, flick(1.0), 40.0, 1.0)
for ts in np.arange(40.0, 45.0, 1.0):
    put(FX, heartbeat(1.0), ts, 0.85, hall=0.15)
put(FX, whoosh(0.5, 2000, 300, 'in', 0.0, 0.0, g=0.5), 40.5, 1.0, hall=0.2)
put(FX, flick(0.45), 40.5, 1.0)
put(FX, thud(0.6), 41.0, 0.8, hall=0.25)
put(FX, steam(0.6, 0.5), 41.0, 0.6)
put('ui', haptic(1.0), 41.0, 1.0, 0.3)
for k, ts in enumerate([41.012, 41.025, 41.038, 41.054, 41.07, 41.089, 41.111, 41.138, 41.174, 41.234]):
    put('ui', ratchet(0.5 - 0.03 * k), ts, 1.0, 0.25)
put(FX, stamp(1.0, 150), 41.5, 1.0, plate=0.4, hall=0.3)
put('ui', tok(170, 0.9, 0.12, 0.3, 0.04), 41.5, 1.0, 0.25, hall=0.2)
big(41.5, 0.45, 0.5)
put('ui', land_tick(1.3), 42.0, 1.0, -0.1)
for k, ts in enumerate([42.5, 42.75, 43.0]):
    put('ui', dry_tok(0.7), ts, 1.0, -0.3 + 0.3 * k)           # about -4 dB vs v1, one fixed body, no hall
put(FX, pan2(lp(nz(0.4), 350) * np.clip(T(0.4) / 0.003, 0, 1) * np.exp(-T(0.4) / 0.05), 0), 43.0, 0.8, hall=0.3)
put(FX, sonar(0.5), 43.0, 0.6, hall=0.25)
put('ui', dry_tok(0.75), 43.5, 1.0, 0.2)
put(FX, flick(0.6), 44.5, 1.0, 0.3)
put(FX, whoosh(0.42, 300, 7000, 'in', 0.6, -0.8, g=1.0, curve=1.6), 44.58, 0.9, hall=0.1)

# ---- 45-50 BUILD
put(FX, eruption(1.1, 1.0, 1.0), 45.0, 0.9, hall=0.25)
put(FX, impact(0.9, 75, 32, 0.8, 0.6, 1.0, 125), 45.0, 0.8, hall=0.3)
put(FX, crash(2.0, 0.6), 45.0, 1.0)
big(45.0, 0.5, 0.4)
for k in range(40):
    put('ui', ratchet(0.25), 45.0 + (k // 5) * 0.0625 + R.uniform(0, 0.03), 1.0, R.uniform(-0.8, 0.8))
put(FX, whoosh(0.26, 300, 2500, 'out', 0.0, 0.0, g=0.45), 45.5, 1.0)
put(FX, flick(1.0), 45.5, 1.0)
typing(45.75, 46.45, 0.02, 0.5, 0.0)
put(FX, stamp(1.0, 175), 46.5, 1.0, plate=0.35, hall=0.1)
put(FX, whoosh(0.2, 3000, 600, 'out', 0.0, 0.0, g=0.4), 46.5, 1.0)
big(46.5, 0.5, 0.35)
put('ui', haptic(1.1), 47.0, 1.0, -0.1)
counter_lock(47.12)
counter_lock(42.12, 1.0)
for k, ts in enumerate([47.5, 47.75, 48.0, 48.25]):
    put('ui', tok(240, 1.0), ts, 1.0, -0.45 + 0.3 * k)
put('ui', haptic(1.3), 48.5, 1.0, -0.1)
rz = riser(5.0, 200, 9000, 0.9, tone_root=41, power=3.0, gap=0.035)
for gt in (4.0, 4.5):
    rz[:, int((gt - 0.03) * SR):int(gt * SR)] *= 0.15
put('pre', rz, 45.0, 1.0, hall=0.15)
# snare roll: 8ths 45-47, 16ths 47-49, 32nds 49-50 (louder accents at 49.0 / 49.5)
rt = list(np.arange(45.0, 47.0, 0.25)) + list(np.arange(47.0, 49.0, 0.125)) + list(np.arange(49.0, 49.94, 0.0625))
for tt in rt:
    u = (tt - 45) / 5
    accent = 1.6 if abs(tt - 49.0) < 1e-6 or abs(tt - 49.5) < 1e-6 else 1.0
    put('drums', snare(0.12, 900 + 2000 * u, 7000), tt, (0.12 + 0.35 * u ** 1.5) * accent, 0.0, plate=0.15 + 0.2 * u)
tt_ = T(1.0)
trem = np.sin(2 * np.pi * 40 * tt_) * (0.5 + 0.5 * np.sign(np.sin(2 * np.pi * 20 * tt_))) * (0.3 + 0.7 * tt_ ** 1.2)
put(FX, lp(trem, 120) * 0.7, 49.0, 1.0)
put(FX, flick(0.7), 49.0, 1.0)
put(FX, flick(1.8), 49.5, 1.0)
put(FX, tok(120, 1.5, 0.2, 0.5, 0.05), 49.5, 1.0, hall=0.3)
put('pre', reverse_swell(0.5, 500, 12000, 1.6, gap=0.035), 49.5, 1.0)

# ---- 50-54 DROP
put(FX, crash(0.3, 1.6, tau=0.022), 50.0, 1.0)
put(FX, lp(nz(0.3), 2500) * np.exp(-T(0.3) / 0.03) * 1.2, 50.0, 1.0)
put(FX, flick(2.0), 50.0, 1.0)
put(FX, crash(3.0, 1.0), 50.0, 1.0)                       # long crash + sub on the bar-1 downbeat
put(FX, sub_boom(2.0, 62, 30, 1.2, 0.6), 50.0, 1.0)
put(FX, braam(41, 1.9, 1.0, swell=0.025), 50.0, 0.7, hall=0.3)   # blooms from the downbeat into the 50.125 slam
put(FX, crackle(0.7, 600, 1.0, 0.25, 1500, 7000), 50.075, 1.0)
put(FX, flick(2.5), 50.075, 1.0)
put(FX, crash(0.2, 1.8, tau=0.02), 50.075, 1.0)
big(50.075, 0.6, 0.06)
put(FX, impact(1.1, 85, 32, 1.0, 1.0, 2.2, 120), 50.125, 1.0, hall=0.3)
put(FX, flick(2.0), 50.125, 1.0)
put(FX, stamp(1.0, 140), 50.125, 1.0, plate=0.2)
put(FX, crash(0.3, 1.5, tau=0.025), 50.125, 1.0)
big(50.0, 0.3, 0.3)
big(50.125, 0.45, 0.4)
for k, ts in enumerate([50.507, 50.522, 50.539, 50.559, 50.582, 50.612, 50.656]):
    put('ui', ratchet(0.9 if k == 0 else 0.6), ts, 1.0, 0.0)
put('ui', land_tick(1.6), 50.5, 1.0)
put(FX, flick(0.8), 50.5, 1.0)
put(FX, impact(1.0, 80, 32, 0.8, 1.0, 1.2, 150), 50.875, 1.0, plate=0.2, hall=0.3)
big(50.875, 0.45, 0.4)
put(FX, whoosh(0.7, 6000, 200, 'out', 0.0, 0.0, g=0.9, curve=0.8), 51.5, 1.0, hall=0.2)
put(FX, flick(0.6), 51.5, 1.0)
for k, ts in enumerate([51.5, 51.55, 51.6, 51.65, 51.7, 51.75, 51.8, 51.85]):
    put(FX, sizzle(0.08 if 51.7 < ts < 51.85 else 0.18), ts, 1.0, -0.7 + 0.2 * k)
# hop 1 lands at 51.775 and the goal photo pops at 51.75: one tick at 51.770 serves both (5 ms early / 20 ms late)
LAND = [51.770, 51.925, 52.075, 52.225, 52.375, 52.525, 52.675]
for k, ts in enumerate(LAND):
    put('ui', land_tick({0: 2.8, 3: 3.0}.get(k, 2.6)), ts, 1.0, -0.6 + 0.18 * k)
    big(ts, 0.45, 0.12)            # music / bass dip under each landing (side-chain from the UI)
put(FX, impact(0.7, 75, 34, 0.6, 0.8, 1.0, 170), 52.8125, 0.9, 0.5, hall=0.25)
put(FX, crackle(0.5, 250, 0.6, 0.2), 52.8125, 1.0, 0.5)
put(FX, flick(1.3), 52.8125, 1.0, 0.4)
put('ui', land_tick(2.5), 52.8125, 1.0, 0.4)
for ts in (53.0, 53.5):
    put(FX, whoosh(0.1, 600, 5000, 'in', 0.0, 0.0, g=0.6), ts - 0.1, 1.0)
    put(FX, stamp(1.2, 140), ts, 1.0, plate=0.35, hall=0.15)
    put(FX, impact(0.7, 70, 32, 0.5, 0.6, 1.0, 130), ts, 0.8, hall=0.2)
    put(FX, crash(1.2, 0.45), ts, 1.0)
    big(ts, 0.5, 0.35)

# ---- 54-60 END CARD
put(FX, sub_boom(2.0, 50, 30, 0.8, 0.7), 54.0, 1.0)
put(FX, reverse_swell(0.45, 300, 6000, 0.6), 53.55, 1.0)
put(FX, crash(3.0, 0.6), 54.0, 1.0)
put(FX, flick(0.5), 54.0, 1.0)
put(FX, whoosh(0.5, 300, 5000, 'out', 0.0, 0.0, g=0.55), 55.25, 1.0, hall=0.1)
put(FX, flick(0.5), 55.25, 1.0)
for k, ts in enumerate([55.35, 55.4, 55.45, 55.5, 55.55]):
    put('ui', tok(250, 0.3), ts, 1.0, -0.6 + 0.3 * k)
sp = whoosh(0.5, 400, 5000, 'in', 0.0, 0.0, g=0.8, curve=1.4)
sp *= (0.6 + 0.4 * np.sin(2 * np.pi * np.cumsum(6 + 26 * (T(0.5) / 0.5) ** 2) / SR))
put(FX, sp, 55.5, 1.0)
put(FX, flick(0.4), 55.5, 1.0)
put(FX, impact(1.1, 85, 32, 1.0, 1.1, 1.2, 100), 56.0, 1.0, hall=0.35)
put(FX, braam(37, 1.4, 0.8), 56.0, 0.45, hall=0.3)
put('ui', haptic(1.6), 56.0, 1.0)
put(FX, crash(2.0, 0.6), 56.0, 1.0)
big(56.0, 0.55, 0.45)
put(FX, whoosh(0.35, 700, 4000, 'out', -0.4, 0.4, g=0.4), 56.5, 1.0)
put('ui', land_tick(1.5), 56.5, 1.0)
put(FX, flick(0.9), 56.5, 1.0)
put('ui', tok(170, 1.4, 0.1, 0.9, 0.02, sine=0.5), 57.0, 1.0, -0.25)
put('ui', tok(170, 1.4, 0.1, 0.9, 0.02, sine=0.5), 57.25, 1.0, 0.25)
put(FX, stamp(0.75, 190), 57.75, 1.0, plate=0.3)
big(57.75, 0.35, 0.3)
put('ui', haptic(1.4), 58.0, 1.0)
put(FX, whoosh(0.25, 400, 2500, 'out', 0.0, 0.0, g=0.35), 58.0, 1.0)
put(FX, riser(0.5, 400, 9000, 0.7), 58.5, 1.0)
put(FX, reverse_swell(0.5, 400, 12000, 1.2), 58.5, 1.0)
put('ui', tok(200, 0.5, 0.08, 0.3, 0.02), 58.925, 1.0)
# FINAL HIT
# the ring-out is carried by the braam / crash / hall tails; every layer decays (about -20 dB by 59.7)
put(FX, impact(1.25, 90, 30, 0.7, 1.2, 1.4, 105, mdecay=0.3), 59.0, 1.0, hall=0.45)
put(FX, braam(41, 1.0, 1.0, decay=0.25), 59.0, 0.8, hall=0.4)
put(FX, crash(1.0, 1.1, tau=0.3), 59.0, 1.0)
put(FX, sub_boom(1.0, 60, 29, 1.2, 0.25), 59.0, 1.0)
put('ui', haptic(1.8), 59.0, 1.0)
put(FX, crackle(0.8, 400, 0.7, 0.2, 1500, 7000), 59.02, 1.0)
big(59.0, 0.35, 0.5)

# 'air' bed: very quiet, wide 9-19 kHz hiss (heat shimmer) so the top octave is never an empty hole
# (added after the hook tape FX so it runs continuously; dips for the CRT power-off)
air = np.vstack([hp(lp(nz(60.5), 19000, 4), 9000, 4) for _ in range(2)])
ta = np.arange(air.shape[1]) / SR
air *= (0.75 + 0.25 * np.sin(2 * np.pi * 0.17 * ta))[None, :]
air *= np.interp(ta, [0, 3, 3.7, 3.8, 3.98, 4.05, 6, 10, 40, 45, 50, 54, 59.0, 59.9, 60.5],
                 [0.4, 0.45, 0.45, 0.15, 0.15, 0.45, 0.5, 0.45, 0.45, 0.55, 0.45, 0.5, 0.5, 0.1, 0.1])[None, :]
air[:, :int(0.01 * SR)] *= np.linspace(0, 1, int(0.01 * SR))
AIR = air[:, :N] * 0.15 * 0.55
print(f'[{time.time() - T_START:5.1f}s] sources placed')

# ============================================================ processing + mix
t_all = np.arange(N) / SR
# pad: choir formants + automated ladder low-pass + level automation
pad_cut = curve([(0, 900), (3, 1000), (4, 900), (5, 1200), (6, 1100), (9.9, 1700), (10, 1800), (20, 2100), (30, 2400),
                 (39.9, 2600), (40, 1300), (42, 1500), (44.9, 1600), (45, 500), (49.9, 2000), (50, 2400), (51.4, 2200), (51.5, 1700), (54, 1700),
                 (56, 1800), (60, 1600)])
pad_lvl = curve([(0, 0.45), (3, 0.5), (4, 0.4), (5, 0.6), (6, 0.45), (10, 0.5), (26, 0.6), (39.9, 0.7), (40, 0.75), (44.9, 0.8),
                 (45, 0.45), (49.9, 0.9), (50, 0.95), (54, 1.0), (58.9, 0.95), (59, 1.1), (60, 1.1)])
P = BUS['pad']
P = Pedalboard([PeakFilter(650, 4.0, 1.1), PeakFilter(1100, 3.0, 1.4), PeakFilter(2600, -3.0, 1.0)])(P.astype(np.float32), SR).astype(np.float64)
P = sweep_filter(P, pad_cut, 'LPF24', 0.12, block=256)
P = hp(P, 170, 2) * pad_lvl
BUS['pad'] = P
BUS['hall'] += P * 0.35
# bass: +3 dB around 700 Hz so the saturated mid layer carries the line on phones
BUS['bass'] = Pedalboard([PeakFilter(700, 4.0, 0.9)])(BUS['bass'].astype(np.float32), SR).astype(np.float64)
# arp delay
A = BUS['arp']
fb = 0.38
A = A + pingpong(A, 0.375, fb, taps=7, lo=300, hi=2800) * 0.9
BUS['arp'] = A
L_ = BUS['lead']
# lead delay steps back under the hop landings (51.7-52.75) so its repeats don't blur the ticks
BUS['lead'] = L_ + pingpong(L_, 0.375, 0.32, taps=5, lo=300, hi=2600) * 0.7 * curve(
    [(0, 1), (51.65, 1), (51.75, 0.35), (52.7, 0.35), (52.85, 1), (61, 1)])[None, :]
print(f'[{time.time() - T_START:5.1f}s] pads / arp processed')

# reverbs
IR_PLATE = make_ir(1.9, 1.6, 7000, 2500, 0.01, 11)
IR_HALL = make_ir(3.6, 3.0, 5000, 1500, 0.025, 12)
IR_DARK = make_ir(1.2, 0.9, 400, 150, 0.0, 13, hp_f=30, er=False)
plate_ret = convolve_wide(BUS['plate'], IR_PLATE, N)
hall_ret = convolve_wide(BUS['hall'], IR_HALL, N)
# rumble (melodic-techno kick reverb, mono, low-passed)
rum = oaconvolve(BUS['kick'][0], IR_DARK[0])[:N]
rum = lp(sat(lp(rum, 140, 4) * 3.0, 1.8), 120, 2)
rum = hp(rum, 30, 2)
print(f'[{time.time() - T_START:5.1f}s] reverbs done')

# side-chain envelopes
duck_kick_bass = duck_env([(t, 0.85, 0.11) for t, _ in kick_times])
duck_kick_music = duck_env([(t, 0.45, 0.32) for t, _ in kick_times])
duck_kick_rumble = duck_env([(t, 0.97, 0.22) for t, _ in kick_times])
duck_kick_ret = duck_env([(t, 0.35, 0.3) for t, _ in kick_times])
duck_hits = duck_env(HITS)
groove_mask = curve([(0, 0), (9.9, 0), (10, 1), (39.9, 1), (40, 0), (49.9, 0), (50, 1), (58.4, 1), (58.6, 0), (60, 0)])
rum = rum * duck_kick_rumble * groove_mask * 0.12
endcard = curve([(0, 1), (53.9, 1), (54.2, 0.84), (58.9, 0.84), (59.0, 1), (61, 1)])
# power-up trim so the drop has headroom above the groove: low end (kick / rumble / bass) -2 dB,
# music -0.5 dB (the low end is trimmed harder so the power-ups also translate on phones)
pu_trim = curve([(0, 1), (9.99, 1), (10.0, 0.97), (39.99, 0.97), (40.0, 1), (61, 1)])
drop_boost = curve([(0, 1), (49.99, 1), (50.0, 1.12), (53.9, 1.12), (54.0, 1), (61, 1)])   # +1 dB drop
pu_low = curve([(0, 1), (9.99, 1), (10.0, 0.8), (39.99, 0.8), (40.0, 1), (61, 1)])
# final ring-out: the reverb returns decay faster after the last hit (tau 0.3 s) so the 0.3 s fade is inaudible
ring = np.ones(N)
ring[int(59.05 * SR):] = np.exp(-np.arange(N - int(59.05 * SR)) / SR / 0.3)
# pre-drop vacuum: everything except the riser top / reverse swell ('pre' bus) at -12 dB for the last 8th
vacuum = curve([(0, 1), (49.70, 1), (49.78, 0.25), (49.997, 0.25), (50.0, 1), (61, 1)])

GAIN = {'kick': 0.47, 'bass': 0.62, 'drums': 1.1, 'pad': 0.62, 'arp': 0.78, 'lead': 0.55, 'fx': 0.55, 'ui': 0.42}
music = BUS['pad'] * GAIN['pad'] + BUS['arp'] * GAIN['arp'] + BUS['lead'] * GAIN['lead']
# presence bell on the music bus only (pad / arp / lead), not on the master; narrow dip at 2 kHz (saw harshness)
music = Pedalboard([PeakFilter(3300, 2.5, 1.0), PeakFilter(2000, -2.0, 1.5)])(music.astype(np.float32), SR).astype(np.float64)
music = music * duck_kick_music * duck_hits * endcard * pu_trim * drop_boost
bass = BUS['bass'] * GAIN['bass'] * duck_kick_bass * np.minimum(1, duck_hits + 0.3) * pu_low * drop_boost
rets = (plate_ret * 0.6 + hall_ret * 0.7) * duck_kick_ret * ring
mix = ((BUS['kick'] * GAIN['kick'] * pu_low * pu_low ** 0.5 + np.vstack([rum, rum]) * pu_low + bass + BUS['drums'] * GAIN['drums'] * np.minimum(1, duck_hits + 0.4)) * endcard
       + music + rets + BUS['fx'] * GAIN['fx'] + BUS['ui'] * GAIN['ui']) * vacuum + BUS['pre'] * GAIN['fx']

if os.environ.get('DEBUG'):
    def _db(x, a, b):
        seg = np.atleast_2d(x)[:, int(a * SR):int(b * SR)]
        return 10 * np.log10(np.mean(seg ** 2) + 1e-12)
    comps = {'kick': BUS['kick'] * GAIN['kick'], 'rumble': np.vstack([rum, rum]), 'bass': bass,
             'drums': BUS['drums'] * GAIN['drums'], 'pad': BUS['pad'] * GAIN['pad'] * duck_kick_music,
             'arp': BUS['arp'] * GAIN['arp'] * duck_kick_music, 'lead': BUS['lead'] * GAIN['lead'], 'rets': rets,
             'fx': BUS['fx'] * GAIN['fx'], 'ui': BUS['ui'] * GAIN['ui']}
    for a, b in [(0, 4), (12, 38), (40, 45), (45, 50), (50, 54), (54, 59), (59.0, 59.1), (59.6, 59.7)]:
        print(f'{a}-{b}', '  '.join(f'{k} {_db(v, a, b):6.1f}' for k, v in comps.items()))
    _m = pyln.Meter(SR)
    for a, b in [(0, 4), (12, 38), (50, 54)]:
        row = []
        for k, v in comps.items():
            seg = np.atleast_2d(v)[:, int(a * SR):int(b * SR)]
            if np.abs(seg).max() < 1e-6:
                continue
            ph = lp(hp(seg, 250, 4), 8000, 4)
            row.append(f'{k} {_m.integrated_loudness(seg.T):5.1f}/{_m.integrated_loudness(ph.T):5.1f}')
        print('phone', a, b, '  '.join(row))

# ---- hook: tape-stop 2.78-3.0, rewind 3.0-3.75, CRT power-off 3.75
src = mix.copy()
i0, i1 = int(2.78 * SR), int(3.0 * SR)
u = np.linspace(0, 1, i1 - i0)
pos = i0 + np.cumsum((1 - u) ** 1.6)
for c in range(2):
    mix[c, i0:i1] = np.interp(pos, np.arange(N), src[c]) * (1 - u ** 3)
gate = np.ones(N)
gate[int(3.0 * SR):int(4.0 * SR) - int(0.002 * SR)] = 0.0
mix *= gate
# rewind: reversed 1.0-3.0, accelerating read
rsrc = src[:, int(1.0 * SR):int(3.0 * SR)][:, ::-1]
rsrc = lp(rsrc, 5000, 2)
nr = int(0.75 * SR)
uu = np.linspace(0, 1, nr)
rate = 1.2 + 3.5 * uu ** 1.4
rate *= (rsrc.shape[1] - 2) / rate.sum()
rp = np.cumsum(rate)
rew = np.vstack([np.interp(rp, np.arange(rsrc.shape[1]), rsrc[c]) for c in range(2)])
rew *= (1 + 0.25 * np.sin(2 * np.pi * 9 * uu))[None, :]
rew = hp(rew, 180, 2)
rew *= np.clip(uu / 0.01, 0, 1) * (1 - 0.3 * uu)
rew[:, -int(0.01 * SR):] *= np.linspace(1, 0, int(0.01 * SR))
post = np.zeros((2, int(1.2 * SR)))
post[:, :nr] += rew * 0.75
# tape jolt
jt = T(0.2)
jolt = np.sin(2 * np.pi * np.cumsum(40 + 80 * np.exp(-jt * 20)) / SR) * np.exp(-jt / 0.05) + bp(nz(0.2), 800, 5000) * np.exp(-jt / 0.01) * 0.6
post[:, :len(jt)] += pan2(jolt * 0.7, 0)
# VHS tracking hiss bands
for ts in (0.0, 0.05, 0.225):
    hb = bp(nz(0.12), 2000, 9000) * np.sin(np.pi * T(0.12) / 0.12) * 0.12
    j = int(ts * SR)
    post[:, j:j + len(hb)] += pan2(hb, 0.3)
co = crt_off(0.32) * 0.9
j = int(0.75 * SR)
post[:, j:j + co.shape[1]] += co
mix[:, int(3.0 * SR):int(3.0 * SR) + post.shape[1]] += post * 0.9 * np.ones((1, 1))
mix[:, :AIR.shape[1]] += AIR
print(f'[{time.time() - T_START:5.1f}s] hook FX done')

# ============================================================ master
mix = Pedalboard([LowShelfFilter(60, -3.0, 0.7), PeakFilter(220, -1.5, 0.8), PeakFilter(3000, 1.5, 0.7), HighShelfFilter(9000, 1.0, 0.7),
                  Compressor(threshold_db=-16, ratio=2.0, attack_ms=12, release_ms=140)])(mix.astype(np.float32), SR).astype(np.float64)
# mono low end: high-pass the side channel
M_ = (mix[0] + mix[1]) / 2
S_ = hp((mix[0] - mix[1]) / 2, 140, 2)
mix = np.vstack([M_ + S_, M_ - S_])
mix = hp(mix, 22, 2)
mix = mix[:, :NOUT]


def limiter(x, ceil_db=-1.7, look=0.002, rel=0.09):
    ceil = 10 ** (ceil_db / 20)
    n = x.shape[1]
    up = resample_poly(x, 4, 1, axis=1)
    pk = np.abs(up).max(0)[:4 * n].reshape(n, 4).max(1)
    g = np.minimum(1.0, ceil / np.maximum(pk, 1e-9))
    L = int(look * SR)
    from scipy.ndimage import minimum_filter1d
    gm = minimum_filter1d(g, size=2 * L + 1, mode='nearest')
    B = 16
    nb = -(-n // B)
    gp = np.concatenate([gm, np.ones(nb * B - n)])
    gb = gp.reshape(nb, B).min(1)
    a = np.exp(-B / (rel * SR))
    out = np.empty(nb)
    prev = 1.0
    for k in range(nb):
        v = prev * a + (1 - a) * 1.0 if gb[k] >= prev else gb[k]
        v = min(v, gb[k])
        out[k] = v
        prev = v
    gs = np.repeat(out, B)[:n]
    ker = np.ones(L) / L
    gs = np.convolve(gs, ker, mode='same')
    gs = np.minimum(gs, gm)
    return x * gs[None, :]


meter = pyln.Meter(SR)
fade_n = int(0.3 * SR)
fade = np.ones(NOUT)
fade[-fade_n:] = np.cos(np.linspace(0, np.pi / 2, fade_n)) ** 2
gain = 10 ** ((-14 - meter.integrated_loudness((mix * fade).T)) / 20)
for it in range(4):
    y = limiter(mix * gain) * fade
    lu = meter.integrated_loudness(y.T)
    gain *= 10 ** ((-14.0 - lu) / 20)
    if abs(lu + 14.0) < 0.05:
        break
y = limiter(mix * gain)
y -= y.mean(1, keepdims=True)
y *= fade                      # the 0.3 s end fade is applied exactly once
tp = max(np.abs(resample_poly(c, 4, 1)).max() for c in y)
if tp > 10 ** (-1.6 / 20):
    y *= 10 ** (-1.6 / 20) / tp
out_path = os.environ.get('OUT') or os.path.join(HERE, 'mix.wav')
sf.write(out_path, y.T.astype(np.float32), SR, subtype='PCM_16')
print(f'[{time.time() - T_START:5.1f}s] wrote {out_path}: {y.shape}, LUFS {meter.integrated_loudness(y.T):.2f}, '
      f'TP {20 * np.log10(max(np.abs(resample_poly(c, 4, 1)).max() for c in y)):.2f} dBTP, gain {20 * np.log10(gain):.1f} dB')
