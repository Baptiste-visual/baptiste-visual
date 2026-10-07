#!/usr/bin/env python3
"""Moorea promo 60 s - DIRECTION B "festival techno" (v2, b-techno).

CONCEPT
  "GAME OVER: rejoue le Moorea" scored as a peak-time industrial festival-techno track (Charlotte de Witte /
  Amelie Lens / Mattn big-room) that is cut to picture like a trailer. F minor with phrygian colour (Gb),
  120 BPM grid (beat 0.5 s, bar 2 s). The "game" is told with cinematic machine sound design (braams, sub
  drops, tape rewind, CRT power-down / degauss, magma bursts, steam quench, metal stamps) - never retro-game
  cliches. No square blips, no coins, no bells, no boings, no chiptune, no major-key jingle.

PALETTE (all synthesized here with numpy/scipy, deterministic seeds, no samples)
  Drums
    KICK     sine with 2-stage pitch envelope (210 Hz -> F1 43.65 Hz tail) + noise knock + HF click, tanh-saturated.
             Mono. Drives a side-chain envelope (DIPK) for everything tonal.
    RUMBLE   the kick track convolved with a dark 1 s noise IR, low-passed 110 Hz, saturated, low-passed again
             and side-chained to the kick so it swells between kicks (classic techno rumble). Mono.
    HATS     high-passed noise + ring-modulated noise (metallic), closed 16ths / open off-beats, ride (long metal
             noise) in the later sections; stereo-spread with per-hit pan.
    CLAP     4 noise bursts (900-4 kHz) spread in stereo + a 2-4.5 kHz crack layer (tau 15 ms, phone presence) +
             room send (room return Haas-widened 12 ms); layered with a short metal clank in the drop.
    PERC     industrial "clank": inharmonic modal partials (<1.6 kHz) + noise, syncopated, ping-pong delay send.
    ROLLS    industrial kick/tom rolls (low-passed kick 400 Hz + two toms) for the 9.0 overheat and the 47-49.88 build;
             the snare (noise + 185 Hz body) is only a quiet top layer (and the short 5.5 dive roll).
  Synths
    BASS     rolling 16th bass (off the kick): two detuned polyBLEP saws + fundamental sine, per-note low-pass
             (cut-off automated per section), sub sine an octave down, tanh. Mono, side-chained. A parallel
             sat(hp(bass,150)) harmonic layer at -10 dB keeps the 16th line audible on phone speakers.
    ACID     303-style line: polyBLEP saw with slides/accents through a 4-pole tanh ladder filter
             (per-sample, resonance k~3.2-3.6, filter envelope per note, one long 10->40 cut-off ramp with a small
             swell per power-up; soft ceiling 2.0 kHz, 2.8 kHz from 30 s; post-LP 2.6 -> 3.5 kHz), hard tanh.
             Low-mid register (F2-F3). Its Gb step is muted on Ebsus4 and Db/C. Dry centre + ping-pong delay + hall.
    PADS     dark wide chords (Fm7 / Dbmaj7 / Gbmaj7 / Ebsus4 / Db/C), 3 detuned saws per note per channel with
             independent detune/phase L vs R (decorrelated = wide), low-passed 0.9-3 kHz, hall send, pumping.
    HOOVER   drop lead: PWM stacks (saw - shifted saw), 5 decorrelated voices per side (+/-25 cents), LP 2.6 kHz,
             tanh, hall send 0.35. Low-mid voicing (F2/C3/F3/Ab3). Also the 8 eruption stabs (7.0-8.75): no scoop,
             no pitch climb, alternating F5 / Gb5 power voicings; the rise is carried by the filter (700->2100 Hz).
    BRAAM    detuned saw stack (root-12, root, 5th, octave, minor 3rd) through the ladder filter with a fast
             opening / slow closing envelope + sub sine, heavy saturation, decorrelated L/R.
    RISERS   noise riser (time-varying band-pass sweep, tremolo), dark saw-cluster pitch riser, reverse crashes.
  SFX (industrial, kept inside the mix: they duck the music, the music never fights them)
    IMPACT   sub boom (90->30 Hz) + low noise thump + distorted transient + noise body + inharmonic metal
             (decorrelated L/R) + hall send. Sizes 0.6-1.8.
    STAMP    shorter impact: sub knock, transient, short metal clank, gated room.
    ERUPTION magma burst: noise through a rising low-pass sweep, roar band, sub push, ember crackle.
    FALL / LAND / QUENCH  accelerating red-hot whoosh with sizzle -> heavy thud + lava splash + steam hiss.
    COOL     "thermal crack" transient + falling 6 -> 1.5 kHz steam hiss (decaying) + two low metal contraction ticks.
    WHOOSH   band-pass noise sweeps with power-curve envelopes that peak exactly on the cut; stereo travel.
    UI       premium tactile "tok" (0.5 ms noise click + 180-450 Hz body, 6-15 ms decay), mechanical
             odometer clack (double tok), soft swish. Quiet, never melodic.
    GAME FX  tape rewind (reversed hook, varispeed + wow), CRT power-off (power-down of the rewind + thunk +
             crackle + falling noise), CRT power-on (degauss hum swell + thump), "denied" power failure (tape-stop of
             the OVER braam + gated tanh F1 sub stutter + relay clunk; no buzzer).
    VACUUM   49.88-49.993 and 58.88-58.993: the whole bed drops to -18 dB; only a reverse-reverb suck is heard,
             so the drop and the final hit land 9-10 dB above what precedes them.

ARRANGEMENT
  0-4   HOOK      lava bed (wide low noise + low bubbles), drone; GAME/OVER = impact + braam (OVER slides Gb->F);
                  2.5 power failure (tape-stop); 3.0-3.75 tape rewind; 3.75 CRT power-down; near silence to 4.0.
  4-6   REJOUER   CRT degauss slam; Fm pad low; muffled kicks 4.5/5.0/5.5; PRESS = impact + power-up saw riser;
                  5.5-6.0 dive: reverse crash + short snare roll + whoosh peaking on the 6.0 cut.
  6-10  NIVEAU 1  groove starts (kick, rumble, filtered bass, hats); 6.15 slam; 7.0-8.75 eight magma
                  eruptions + F5/Gb5 hoover stabs opening in filter (panned like the words); 9.0 overheat: tom/kick
                  roll + tremor jolts + noise riser, kick stops 9.5, white-out swell into 10.0.
  10-40 POWER-UPS full groove: kick/rumble/16th bass/claps/hats; acid enters at 10 and evolves (patterns A/B/C,
                  one long cut-off ramp + per-power-up swell); perc clanks from 20, ride + toms from 30;
                  pad chords every 4 s (Fm7 Db Gb Fm7 Db Ebsus4 Gb Fm7). Energy steps per 10 s (bus 0.80/0.84/0.88).
                  Full kick/bass mute on the whips into 20/30/40; only P+4.75-5.0 on the whips into 15/25/35.
  40-45 BREAKDOWN no kick/bass, bus 0.62 (about -17.4 LUFS): heartbeat sub, wide pads, closed acid + delay;
                  shaker only from 42; 41.5 answer stamp (darker room) + ducked music.
  45-50 BUILD     kick back thinning (rising HP), hall-washed claps, bass/acid filters opening, kick/tom roll
                  47-49.88 (8ths -> 16ths -> 32nds), noise + pitch riser ending 49.88, kick stops 49.0 (tremor),
                  Db/C chord 49-50, VACUUM 49.88-50.0 (reverse-reverb suck only).
  50-54 DROP      biggest moment: impact 1.8 + braam + crash + hard kick; 50.125 title slam; hoover riff,
                  full acid, ride, claps+clank; 8/8 land; quiet fixed-230 Hz hop toks; taglines 53.0 / 53.5 slam on
                  hoover stabs (Ebsus4 on 53.0, no G natural against the acid).
  54-60 END CARD  sunrise pad swell Fm9 -> Db -> Ebsus4, lighter groove, snap/slam 56.0, quiet tactile UI;
                  groove stops 58.5, short reverse swell, VACUUM 58.88-59.0, FINAL HIT 59.0 (impact + braam 1.0 s +
                  kick + crash); dry buses release (tau 0.16 s) from 59.12 while the hall rings out; rumble dies
                  by 59.35; fade only the last 0.3 s.

CUE -> SOUND (weight 3 and weight 2)
  0.000 w2 open: wide lava bed + low pulse      | 0.500 w2 plop: magma gulp (sub swallow + low splash + sizzle)
  0.775 w2 suck: reverse air suck into GAME      | 1.000 w3 GAME: impact 1.4 + braam F + crash
  1.275 w2 suck 2 (braam gated)                  | 1.500 w3 OVER: impact 1.5 + braam Gb->F
  2.000 w2 card flip: flip swish + tok           | 2.250 w2 subline: 6 soft word toks
  2.500 w2 DEAD: tape-stop of the OVER braam + F1 sub stutter (gated 2.5/2.543/2.584/2.625) + relay clunk
  3.000 w2 rewind: tape jolt + reversed hook     | 3.750 w2 CRT off: power-down + thunk + crackle
  4.000 w3 CRT on: degauss + impact 1.1          | 4.500 w2 reveal: muffled kick + tok + chevron swish
  5.000 w3 PRESS: impact 1.2 + thock + power-up riser | 5.500 w2 dive: kick + whoosh + reverse crash + roll
  5.750 w2 flash: accented roll hit + air burst  | 6.000 w2 cut: kick + crash + release burst
  6.150 w3 NIVEAU 1 slam: impact 1.3             | 6.375 w2 logo lands: stamp (small)
  7.000-8.750 w2 eruptions: eruption + spurt crack + F5/Gb5 stab each 8th (7.225 logo sink + 7.25 eruption 2
                share one splash/thump at 7.233)
  9.000 w2 overheat: roll + riser + tremor start | 9.500 w2 white-out: accent hit + reverse crash
  P=10,15,20,25,30,35 (w3): eruption + impact + crash on 10/20/30
  P+0.5 w2: red-hot fall (10.5/15.5/35.5/40.5), map rise grind (20.5), sheet rise whoosh (25.5), tile tok (30.5)
  P+1.0 w3/w2: land = thud impact + lava splash + steam (11/16/36/41), map settle thud (21), truck slam (31)
  P+1.14 w2 cool: thermal crack + falling steam hiss + metal ticks (11.14 / 16.14 / 36.12)
  P+1.5 w3 answer stamps (11.5 16.5 21.5 26.5 31.5 36.5 41.5 46.5): stamp + duck
  P+2.12 w2 HUD counter: mechanical odometer clack (12.12 ... 47.12)
  showcase w2 (rows, pins, ticks, tiles, steps, chips, avatar dots, store pills ...): tactile toks / swishes
  dot jumps w2 (13.5 18.5 28.5 33.5 38.5): soft air swish; dot lands w2 (14.0 19.0 29.0 34.0 39.0): thock
  sonar 23.5 w2: low radar pulse (no ping)       | whips w2 (P+4.5, 44.5): whoosh peaking on the cut, kick muted
  17.063/18.5 zoom whooshes, 17.5/18.0 pan swishes, 22.56 label pop, 23.0 route draw: swish + tok
  25.250 w3 HALO x MAINSTAGE collide: metal-heavy impact 1.3 | 28.5 w3 VALIDER: thock + impact 0.9
  31.0-31.75 w2 truck card slams: thud x4       | 32.0-33.5 carousel swishes + toks
  40.0 w2 breakdown eruption (soft) + crack     | 41.0 w2 soft land + toggle double tok
  41.5 w3 answer stamp (room 0.2 / hall 0.25) + duck; 41.52 compass lock clack (quiet)
  45.0 w3 build eruption + impact + crash        | 45.75 w2 typing ticks | 46.5 w2 send suck
  49.0 w2 riser: low boom + tremor               | 49.5 w2 white-out: reverse crash + 32nd snare
  50.000 w3 DROP: impact 1.8 + braam + crash + kick | 50.075 w2 ember spray | 50.125 w3 title slam
  50.5 w2 slot reel: decelerating ratchet clicks at the digit flips | 50.875 w3 8/8 land: impact + hoover
  51.5 w2 pull-back whoosh | 51.75 goal pop + 51.775 hop 1 share one hit at 51.762 | 51.925..52.675 w2 hop
  landings: quiet 230 Hz toks (no open hat at 51.75 / 52.25) | 52.813 w2 goal impact
  53.000 / 53.500 w3 taglines: impact + kick + hoover stab
  54.0 w2 sunrise: crash + pad swell + sub | 55.25/55.5 w2 tab-bar / spin whooshes | 56.0 w3 snap + slam
  56.5 w2 date swish | 57.0/57.25 w2 store toks | 57.75 w2 small stamp | 58.0 w2 button thock
  32/33/34/37/38/39 w2 beat cues in the dense 30-40 groove: a quiet filtered-noise transient on top of the kick.
  59.000 w3 FINAL HIT: impact 1.9 + braam + kick + crash, after the vacuum and its reverse-reverb suck.
"""
import os
import time
import numpy as np
import soundfile as sf
import pyloudnorm as pyln
from scipy.signal import butter, sosfilt, oaconvolve, resample_poly
from scipy.ndimage import minimum_filter1d, uniform_filter1d
from pedalboard import Pedalboard, Compressor

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
SR = 48000
NOUT = 60 * SR
N = NOUT + 2 * SR
BEAT = 0.5
S16 = 0.125
TWO_PI = 2 * np.pi


# ======================================================================== basics
def tt(d):
    return np.arange(int(round(d * SR))) / SR


def note(m):
    return 440.0 * 2 ** ((np.asarray(m, dtype=np.float64) - 69) / 12)


_seed = [7000]


def R(seed=None):
    if seed is None:
        _seed[0] += 1
        seed = _seed[0]
    return np.random.default_rng(seed)


def noise(d, seed=None):
    return R(seed).standard_normal(int(round(d * SR)))


def _sos(btype, f, order=2):
    if btype == 'band':
        lo, hi = max(f[0], 12.0), min(f[1], SR * 0.45)
        return butter(order, [lo, max(hi, lo * 1.05)], 'band', fs=SR, output='sos')
    return butter(order, min(max(f, 12.0), SR * 0.45), btype, fs=SR, output='sos')


def lp(x, f, o=2):
    return sosfilt(_sos('low', f, o), x, axis=-1)


def hp(x, f, o=2):
    return sosfilt(_sos('high', f, o), x, axis=-1)


def bp(x, lo, hi, o=2):
    return sosfilt(_sos('band', (lo, hi), o), x, axis=-1)


def tv_filter(x, fc, btype='band', bw_oct=1.0, order=2, block=256):
    """Time-varying Butterworth (coefficients per block, state carried)."""
    x = np.asarray(x, np.float64)
    y = np.empty_like(x)
    zi = None
    for i in range(0, len(x), block):
        f = float(fc[min(i + block // 2, len(x) - 1)])
        if btype == 'band':
            sos = _sos('band', (f * 2 ** (-bw_oct / 2), f * 2 ** (bw_oct / 2)), order)
        else:
            sos = _sos(btype, f, order)
        if zi is None:
            zi = np.zeros((sos.shape[0], 2))
        y[i:i + block], zi = sosfilt(sos, x[i:i + block], zi=zi)
    return y


def fade_tail(x, d=0.02):
    n = min(int(d * SR), x.shape[-1])
    if n > 1:
        x = x.copy()
        x[..., -n:] *= np.linspace(1, 0, n) ** 2
    return x


def fade_head(x, d=0.002):
    n = min(int(d * SR), x.shape[-1])
    if n > 1:
        x = x.copy()
        x[..., :n] *= np.linspace(0, 1, n)
    return x


def sat(x, drive=2.0):
    return np.tanh(x * drive) / np.tanh(drive)


def _blep(ph, dt):
    out = np.zeros_like(ph)
    m = ph < dt
    if np.any(m):
        x = ph[m] / dt[m]
        out[m] = x + x - x * x - 1
    m2 = ph > 1 - dt
    if np.any(m2):
        x2 = (ph[m2] - 1) / dt[m2]
        out[m2] = x2 * x2 + x2 + x2 + 1
    return out


def saw_f(f, phase0=0.0):
    """Band-limited saw from a frequency array (Hz per sample)."""
    f = np.asarray(f, np.float64)
    dt = np.clip(f / SR, 1e-7, 0.45)
    ph = (phase0 + np.cumsum(dt)) % 1.0
    return 2 * ph - 1 - _blep(ph, dt), ph, dt


def saw_ph(ph, dt):
    ph = ph % 1.0
    return 2 * ph - 1 - _blep(ph, dt)


def ladder(x, fc, k=3.2, drive=1.0):
    """4-pole TPT ladder low-pass with tanh input stage (per-sample, used on synth lines only)."""
    from math import tanh
    g = np.tan(np.pi * np.clip(fc, 20, SR * 0.42) / SR)
    G = (g / (1 + g)).tolist()
    xs = (np.asarray(x, np.float64) * drive).tolist()
    ks = (np.broadcast_to(np.asarray(k, np.float64), (len(xs),))).tolist()
    out = [0.0] * len(xs)
    s1 = s2 = s3 = s4 = y4 = 0.0
    for i in range(len(xs)):
        Gi = G[i]
        u = tanh(xs[i] - ks[i] * y4)
        v = (u - s1) * Gi; y1 = v + s1; s1 = y1 + v
        v = (y1 - s2) * Gi; y2 = v + s2; s2 = y2 + v
        v = (y2 - s3) * Gi; y3 = v + s3; s3 = y3 + v
        v = (y3 - s4) * Gi; y4 = v + s4; s4 = y4 + v
        out[i] = y4
    return np.asarray(out) * (1 + 0.45 * np.asarray(ks))


def pan2(sig, pan):
    l = np.cos((pan + 1) * np.pi / 4) * np.sqrt(2)
    r = np.sin((pan + 1) * np.pi / 4) * np.sqrt(2)
    return np.vstack([sig * l, sig * r])


# ======================================================================== buses
KICK = np.zeros(N)          # mono
BASS = np.zeros(N)          # mono (bass + sub)
DRUMS = np.zeros((2, N))    # hats / claps / perc
SYN = np.zeros((2, N))      # acid / pads / hoover / braam / risers (side-chained)
SFX = np.zeros((2, N))      # sound design (lightly ducked by big hits)
HITS = np.zeros((2, N))     # impacts (never ducked)
TOP = np.zeros((2, N))      # rewind / CRT (ignores the hook mute)
REV = np.zeros((2, N))      # hall send
ROOM = np.zeros((2, N))     # short room send
DLY = np.zeros((2, N))      # ping-pong delay send
DIPK = np.zeros(N)          # kick side-chain (0..1)
DIPH = np.zeros(N)          # big-hit side-chain (0..1)
KICK_T = []


def _add(buf, sig, i0):
    n = sig.shape[-1]
    a, b = max(i0, 0), min(i0 + n, buf.shape[-1])
    if b <= a:
        return
    buf[..., a:b] += sig[..., a - i0:b - i0]


def put(buf, sig, at, g=1.0, pan=0.0, rev=0.0, room=0.0, dly=0.0):
    sig = np.asarray(sig, np.float64)
    i0 = int(round(at * SR))
    if buf.ndim == 1:
        if sig.ndim == 2:
            sig = sig.mean(0)
        _add(buf, sig * g, i0)
        st = np.vstack([sig, sig]) * g
    else:
        if sig.ndim == 1:
            st = pan2(sig, pan) * g
        else:
            st = sig * g
            if pan:
                st = st * np.array([[min(1, 1 - pan)], [min(1, 1 + pan)]])
        _add(buf, st, i0)
    for send, amt in ((REV, rev), (ROOM, room), (DLY, dly)):
        if amt:
            _add(send, st * amt, i0)


def duck(arr, at, depth, rel, att=0.003, hold=0.01):
    n = int((att + hold + rel * 6) * SR)
    t = np.arange(n) / SR
    shape = np.where(t < att, t / att, np.where(t < att + hold, 1.0, np.exp(-(t - att - hold) / rel))) * depth
    i0 = int(round((at - att * 0.6) * SR))
    a, b = max(i0, 0), min(i0 + n, len(arr))
    if b > a:
        arr[a:b] = np.maximum(arr[a:b], shape[a - i0:b - i0])


# ======================================================================== drums
_kcache = {}


def kick_s(hard=1.0, d=0.45):
    key = (round(hard, 2), round(d, 2))
    if key in _kcache:
        return _kcache[key]
    t = tt(d)
    f = 43.65 + 215 * np.exp(-t * 46) + 50 * np.exp(-t * 10)
    body = np.sin(TWO_PI * np.cumsum(f) / SR) * np.exp(-t * (5.2 - 0.8 * (hard - 1)))
    ramp = np.minimum(1, t / 0.0008)
    knock = bp(noise(d, 11), 120, 700) * np.exp(-t * 55) * 0.55 * ramp
    click = bp(noise(d, 12), 1800, 9000) * np.exp(-t * 320) * 0.45 * ramp
    drive = 1.6 + 2.2 * hard
    k = lp(sat(body + knock, drive), 3000, 2) * 0.92 + click
    k = fade_tail(k, 0.06)
    _kcache[key] = k
    return k


def kick_at(t, hard=1.0, g=1.0, lpf=None, hpf=None, d=0.45, sc=1.0):
    k = kick_s(hard, d)
    if lpf:
        k = lp(k, lpf, 2)
    if hpf:
        k = hp(k, hpf, 2)
    put(KICK, k, t, g)
    if sc > 0:
        KICK_T.append((t, sc))
        duck(DIPK, t, sc, 0.11, att=0.002, hold=0.02)


def hat(kind='c', seed=None):
    d = {'c': 0.07, 'o': 0.3, 'r': 0.9, 's': 0.09}[kind]
    t = tt(d)
    n = noise(d, seed)
    met = n * (np.sin(TWO_PI * 3170 * t) + np.sin(TWO_PI * 4890 * t) + np.sin(TWO_PI * 6930 * t) + np.sin(TWO_PI * 8460 * t))
    if kind == 'c':
        y = hp(n, 7500, 4) * np.exp(-t * 85) + 0.35 * hp(met, 6000) * np.exp(-t * 70)
    elif kind == 'o':
        y = hp(n, 6500, 4) * np.exp(-t * 14) + 0.45 * hp(met, 5000) * np.exp(-t * 11)
    elif kind == 'r':
        y = 0.5 * hp(n, 6000, 2) * np.exp(-t * 4) + 0.7 * bp(met, 3500, 11000) * np.exp(-t * 3.2)
        y += hp(n, 2500) * np.exp(-t * 60) * 0.4
    else:  # shaker
        y = bp(n, 4000, 11000) * np.minimum(1, t / 0.012) * np.exp(-t * 45)
    y = np.tanh(2.2 * y) / 2.2
    return fade_tail(fade_head(y, 0.0005), 0.01)


def clap_s(seed, metal_amt=0.0):
    d = 0.35
    t = tt(d)
    r = R(seed)
    out = np.zeros((2, len(t)))
    for k, off in enumerate([0.0, 0.009, 0.018, 0.029]):
        nz_ = r.standard_normal(len(t))
        b = (bp(nz_, 900, 4200) + 0.55 * hp(nz_, 4500)) * np.exp(-t * (110 if k < 3 else 16))
        i = int(off * SR)
        p = r.uniform(-0.5, 0.5)
        out[:, i:] += pan2(b[:len(t) - i], p)
    out += np.vstack([lp(hp(r.standard_normal(len(t)), 500), 3000), lp(hp(r.standard_normal(len(t)), 500), 3000)]) * np.exp(-t * 9) * 0.12
    # 2-4.5 kHz crack layer (phone-speaker presence), tau 15 ms, slightly wide
    out += np.vstack([bp(r.standard_normal(len(t)), 2000, 4500) for _ in range(2)]) * np.exp(-t / 0.015) * np.minimum(1, t / 0.0006) * 0.9
    if metal_amt:
        m = metal(d, 300, 1500, 12, (0.03, 0.12), seed + 1)
        out += metal_amt * m * 0.6
    return fade_tail(np.tanh(out * 1.6) * 0.7)


def snare_s(seed, d=0.2):
    t = tt(d)
    tone = np.sin(TWO_PI * 185 * t * (1 + 0.3 * np.exp(-t * 60))) * np.exp(-t * 32)
    nz = bp(noise(d, seed), 1400, 8000) * np.exp(-t * 20)
    return fade_tail(np.tanh((tone * 0.7 + nz) * 1.5) * 0.6)


def metal(d, lo=140, hi=1500, n=18, tau=(0.08, 0.6), seed=0):
    r = R(seed)
    t = tt(d)
    f = np.exp(r.uniform(np.log(lo), np.log(hi), n))
    taus = r.uniform(tau[0], tau[1], n)
    amps = r.uniform(0.4, 1.0, n) / np.sqrt(np.arange(1, n + 1))
    ph = r.uniform(0, TWO_PI, n)
    y = np.zeros(len(t))
    for i in range(n):
        y += amps[i] * np.sin(TWO_PI * f[i] * t + ph[i]) * np.exp(-t / taus[i])
    y *= np.clip(t / 0.0015, 0, 1)
    return fade_tail(y / (np.abs(y).max() + 1e-9))


def clank_s(seed):
    d = 0.35
    t = tt(d)
    m = metal(d, 280, 1600, 14, (0.02, 0.14), seed)
    tr = bp(noise(d, seed + 3), 1500, 7000) * np.exp(-t * 300)
    return fade_tail(np.tanh((m * 0.8 + tr * 0.6) * 1.8) * 0.6)


def tom_s(seed, f0=110):
    d = 0.4
    t = tt(d)
    f = f0 * (0.65 + 0.35 * np.exp(-t * 20))
    y = np.sin(TWO_PI * np.cumsum(f) / SR) * np.exp(-t * 9) + bp(noise(d, seed), 200, 1200) * np.exp(-t * 40) * 0.4
    return fade_tail(sat(y, 2.0) * 0.7)


# ======================================================================== synths
def bass_note(f, cut, d=0.118, vel=1.0, seed=0):
    t = tt(d)
    s, _, _ = saw_f(np.full(len(t), f), 0.0)
    s2, _, _ = saw_f(np.full(len(t), f * 1.006), 0.37)
    y = lp(s + 0.6 * s2, cut, 2) + 0.9 * np.sin(TWO_PI * f * t)
    env = np.minimum(1, t / 0.003) * np.exp(-t * 14)
    y = sat(y * env * vel * 1.3, 1.8)
    sub = np.sin(TWO_PI * f / 2 * t) * np.minimum(1, t / 0.004) * np.exp(-t * 8) * 0.85 * vel
    return fade_tail(y * 0.6 + sub * 0.38, 0.012)


def pad(notes, d, cut, att=0.6, rel=0.8, seed=0, bright=1.0):
    """Wide dark pad: per channel independent detune / phase."""
    total = d + rel
    t = tt(total)
    n = len(t)
    r = R(seed)
    out = np.zeros((2, n))
    for m in notes:
        f0 = float(note(m))
        for ch in range(2):
            for det in (-0.11, 0.0, 0.12):
                dd = det + r.uniform(-0.04, 0.04)
                lfo = 1 + 0.0015 * np.sin(TWO_PI * r.uniform(0.15, 0.4) * t + r.uniform(0, 6.28))
                s, _, _ = saw_f(np.full(n, f0 * 2 ** (dd / 12)) * lfo, r.uniform(0, 1))
                out[ch] += s
    out /= np.sqrt(len(notes) * 3)
    fcut = cut * (1 + 0.25 * np.sin(TWO_PI * 0.23 * t))
    out = np.vstack([tv_filter(out[0], fcut, 'low', order=2, block=1024), tv_filter(out[1], fcut * 1.03, 'low', order=2, block=1024)])
    out = hp(out, 110)
    env = np.clip(t / att, 0, 1) ** 1.5
    env *= np.where(t > d, np.exp(-(t - d) / (rel / 3.5)), 1.0)
    return fade_tail(out * env * 0.5, 0.05)


def hoover(notes, d, seed=0, scoop=4.0, cut=2600):
    total = d + 0.12
    t = tt(total)
    n = len(t)
    r = R(seed)
    bend = -scoop * np.exp(-t / 0.03) - 0.6 * np.clip((t - d) / 0.12, 0, 1) ** 2
    out = np.zeros((2, n))
    for m in notes:
        for ch in range(2):
            for det in r.uniform(-0.25, 0.25, 5):
                f = note(m + det + bend)
                dt = np.clip(f / SR, 1e-7, 0.45)
                ph = (r.uniform(0, 1) + np.cumsum(dt))
                pw = 0.5 + 0.32 * np.sin(TWO_PI * (4.3 + 0.9 * ch) * t + r.uniform(0, 6.28))
                out[ch] += saw_ph(ph, dt) - saw_ph(ph + pw, dt)
    out /= np.sqrt(len(notes) * 5)
    out = hp(lp(out, cut, 2), 70)
    env = np.minimum(1, t / 0.004) * np.where(t > d, np.exp(-(t - d) / 0.035), 1.0) * (0.75 + 0.25 * np.exp(-t * 6))
    return fade_tail(np.tanh(out * env * 2.2) * 0.45, 0.02)


def braam(root, d=2.2, seed=0, slide=0.0, peak=2400, k=1.6):
    t = tt(d)
    n = len(t)
    r = R(seed)
    bend = slide * np.exp(-t / 0.18)
    out = np.zeros((2, n))
    for m, a in ((root - 12, 1.0), (root, 0.9), (root + 7, 0.7), (root + 12, 0.55), (root + 15, 0.35)):
        for ch in range(2):
            for _ in range(4):
                det = r.uniform(-0.18, 0.18)
                s, _, _ = saw_f(note(m + det + bend) * np.ones(n), r.uniform(0, 1))
                out[ch] += a * s
    out /= 6
    fc = 110 + (peak - 110) * np.minimum(1, t / 0.05) * np.exp(-np.maximum(t - 0.05, 0) / 0.45) + 260
    y = np.vstack([ladder(out[ch], fc * (1 + 0.04 * ch), k, 1.4) for ch in range(2)])
    sub = np.sin(TWO_PI * np.cumsum(note(root - 12 + bend)) / SR) * 0.9
    y = y + sub
    env = np.minimum(1, t / 0.006) * np.exp(-t / (d * 0.42))
    y = np.tanh(y * env * 2.6) * 0.5
    return fade_tail(hp(y, 30), 0.25)


# ======================================================================== sound design
def sub_boom(d=1.4, f0=90, f1=30, tau=0.45, drive=1.6):
    t = tt(d)
    f = f1 + (f0 - f1) * np.exp(-t * 9)
    s = np.sin(TWO_PI * np.cumsum(f) / SR) * np.exp(-t / tau) * np.clip(t / 0.002, 0, 1)
    return fade_tail(sat(s, drive), 0.08)


def transient(seed, d=0.08, amt=1.0):
    t = tt(d)
    a = hp(noise(d, seed), 1200) * np.exp(-t * 230)
    b = bp(noise(d, seed + 1), 300, 2500) * np.exp(-t * 75) * 0.8
    return fade_tail(np.tanh(2.6 * (a + b) * amt) * 0.9, 0.01)


def impact(size=1.0, seed=0, metal_amt=0.6, sub=True, d=None):
    d = d or (1.0 + 0.9 * size)
    t = tt(d)
    n = len(t)
    low = np.zeros(n)
    if sub:
        low += sub_boom(d, 95, 30, 0.22 + 0.28 * size)[:n] * 0.95
    low += lp(noise(d, seed), 170, 4) * np.exp(-t * 20) * 2.6
    hi = np.zeros((2, n))
    tr = transient(seed + 2)
    hi[:, :len(tr)] += tr * 0.9
    for ch in range(2):
        body = bp(noise(d, seed + 10 + ch), 220, 1900) * np.exp(-t * (15 / size))
        hi[ch] += np.tanh(2.4 * body) * 0.55
        hi[ch] += metal(d, 110, 1450, 20, (0.07, 0.25 + 0.45 * size), seed * 7 + ch) * metal_amt * 0.42 * np.exp(-t * 1.2)
    return low, fade_tail(hi, 0.1)


def hit(at, size=1.0, seed=0, metal_amt=0.6, sub=True, g=1.0, rev=0.35, crash_d=0.0, duck_depth=None):
    low, hi = impact(size, seed, metal_amt, sub)
    put(HITS, low, at, g)
    put(HITS, hi, at, g * 0.85, rev=rev, room=0.15)
    if crash_d:
        put(HITS, crash(crash_d, seed + 50), at, g * 0.45, rev=0.25)
    dd = duck_depth if duck_depth is not None else min(0.85, 0.4 + 0.3 * size)
    duck(DIPH, at, dd, 0.12 + 0.15 * size)


def stamp(at, seed, g=1.0, size=1.0, rev=0.12, room=0.35):
    d = 0.9
    t = tt(d)
    low = sub_boom(d, 85, 38, 0.12 * size + 0.08) * 0.9 + lp(noise(d, seed), 220, 4) * np.exp(-t * 30) * 2.0
    hi = np.zeros((2, len(t)))
    tr = transient(seed + 1, amt=1.2)
    hi[:, :len(tr)] += tr
    for ch in range(2):
        hi[ch] += metal(d, 160, 1500, 16, (0.03, 0.22), seed * 3 + ch) * 0.5 * np.exp(-t * 3)
        hi[ch] += np.tanh(2 * bp(noise(d, seed + 5 + ch), 300, 1600) * np.exp(-t * 35)) * 0.5
    put(HITS, low, at, g)
    put(HITS, fade_tail(hi, 0.1), at, g * 0.8, room=room, rev=rev)
    duck(DIPH, at, 0.55 * min(size, 1.2), 0.14)


def crash(d=2.0, seed=0, tau=None):
    tau = tau or d * 0.35
    t = tt(d)
    out = []
    for ch in range(2):
        r = R(seed + ch)
        nz = r.standard_normal(len(t))
        met = nz * (np.sin(TWO_PI * 3150 * t) + np.sin(TWO_PI * 4870 * t) + np.sin(TWO_PI * 6930 * t) + np.sin(TWO_PI * 8410 * t))
        y = hp(nz, 3500) * 0.7 + hp(met, 4000) * 0.22
        y = y * np.exp(-t / tau) * np.clip(t / 0.002, 0, 1) + hp(nz, 1200) * np.exp(-t * 35) * 0.5
        out.append(lp(y, 13500))
    return fade_tail(np.vstack(out) * 0.6, 0.2)


def rev_crash(d=1.0, seed=0):
    c = crash(d * 1.6, seed, tau=d * 0.5)[:, ::-1]
    c = c[:, -int(d * SR):]
    return fade_head(c, 0.02)


def whoosh(d, f0, f1, curve=2.0, tail=0.12, pan0=-0.5, pan1=0.5, bw=1.3, seed=0, onset=0.12, low=0.6):
    """Noise sweep whose energy peaks exactly at d (the cut)."""
    tot = d + tail
    t = tt(tot)
    p = np.clip(t / d, 0, 1)
    fc = f0 * (f1 / f0) ** (p ** curve)
    amp = np.maximum(p ** curve, onset * np.minimum(1, t / 0.006) * np.exp(-t / 0.08))
    amp = np.where(t > d, np.exp(-(t - d) / 0.045), amp)
    n1, n2 = noise(tot, seed), noise(tot, seed + 1)
    out = []
    for ch, nz in enumerate((n1, 0.6 * n1 + 0.8 * n2)):
        y = tv_filter(nz, fc * (1 + 0.06 * ch), 'band', bw) + low * tv_filter(nz, fc / 5, 'low')
        out.append(y)
    out = np.vstack(out) * amp
    pan = pan0 + (pan1 - pan0) * p
    out[0] *= np.sqrt(np.clip(1 - pan, 0, 2) / 2) * 1.414
    out[1] *= np.sqrt(np.clip(1 + pan, 0, 2) / 2) * 1.414
    return fade_tail(fade_head(out, 0.001), 0.02) * 0.5


def swish(d=0.18, f0=700, f1=3500, seed=0, pan=0.0):
    t = tt(d)
    fc = f0 * (f1 / f0) ** (t / d)
    y = tv_filter(noise(d, seed), fc, 'band', 1.0) * np.minimum(1, t / 0.004) * np.exp(-t / (d * 0.35))
    return pan2(fade_tail(y, 0.02) * 0.6, pan)


def tok(body=300, tau=0.012, click=1.0, seed=0, d=0.07, bright=5000):
    t = tt(d)
    b = np.sin(TWO_PI * body * t * (1 + 0.22 * np.exp(-t * 150))) * np.exp(-t / tau)
    c = bp(noise(d, seed), 900, bright) * np.exp(-t * 1100) * click
    return fade_tail((b * 0.8 + c * 0.7) * np.minimum(1, t / 0.0004), 0.01)


def clack(seed):
    a = tok(430, 0.006, 1.0, seed, 0.06)
    b = tok(290, 0.010, 0.7, seed + 1, 0.06)
    y = np.zeros(int(0.08 * SR))
    y[:len(a)] += a
    i = int(0.013 * SR)
    y[i:i + len(b)] += b[:len(y) - i] * 0.8
    return y


def crackle(d, rate=120, seed=0, lo=900, hi=6000):
    r = R(seed)
    n = int(d * SR)
    y = np.zeros(n)
    k = r.poisson(rate * d)
    idx = r.integers(0, n, k)
    y[idx] = r.uniform(-1, 1, k) * r.uniform(0.2, 1, k)
    y = bp(y, lo, hi)
    return y * np.exp(-np.arange(n) / SR / (d * 0.4))


def eruption(seed, size=1.0, d=1.2):
    t = tt(d)
    n = len(t)
    fc = 180 + 2600 * size * np.minimum(1, t / 0.2) ** 0.7 * np.exp(-np.maximum(t - 0.2, 0) / 0.35)
    out = np.zeros((2, n))
    for ch in range(2):
        nz = noise(d, seed + ch)
        burst = tv_filter(nz, fc, 'low', order=2) * np.minimum(1, t / 0.006) * np.exp(-t / 0.32)
        roar = bp(nz, 110, 600) * np.minimum(1, t / 0.01) * np.exp(-t / 0.45)
        out[ch] = np.tanh(2.2 * (burst * 1.3 + roar * 0.9)) * 0.55
        out[ch] += crackle(d, 160, seed + 5 + ch) * 2.5
    push = np.sin(TWO_PI * np.cumsum(40 + 35 * np.minimum(1, t / 0.15)) / SR) * np.exp(-t / 0.18) * np.minimum(1, t / 0.003)
    out += push * 0.6
    return fade_tail(out, 0.15)


def splash(seed, d=0.7):
    t = tt(d)
    out = np.zeros((2, len(t)))
    for ch in range(2):
        nz = noise(d, seed + ch)
        a = bp(nz, 280, 2600) * np.minimum(1, t / 0.003) * np.exp(-t / 0.09)
        g = tv_filter(nz, 1400 * np.exp(-t * 5) + 180, 'low') * np.exp(-t / 0.22) * 0.9
        out[ch] = np.tanh(1.8 * (a + g)) * 0.5 + crackle(d, 90, seed + 9 + ch, 600, 4000) * 1.5
    thump = np.sin(TWO_PI * 85 * t * (1 + 0.3 * np.exp(-t * 30))) * np.exp(-t * 18)
    return fade_tail(out + thump * 0.4, 0.1)


def steam(seed, d=0.7, g=1.0):
    t = tt(d)
    fc = 2600 + 5200 * np.exp(-t * 4)
    out = np.vstack([tv_filter(noise(d, seed + ch), fc, 'high', order=2) for ch in range(2)])
    env = np.minimum(1, t / 0.018) * np.exp(-t / (d * 0.32))
    return fade_tail(out * env * 0.32 * g, 0.08)


def cool_sheen(seed):
    d = 0.45
    t = tt(d)
    crack_ = bp(noise(d, seed), 700, 5200) * np.exp(-t * 600) * 0.9
    crack_ += np.sin(TWO_PI * 520 * t) * np.exp(-t * 90) * 0.35
    # steam hiss falling 6 kHz -> 1.5 kHz, decaying (no rising shimmer)
    fc = 6000 * (0.25 ** (t / d))
    sh = np.vstack([tv_filter(noise(d, seed + 1 + ch), fc, 'high', order=2) for ch in range(2)])
    sh *= np.minimum(1, t / 0.01) * np.exp(-t / 0.12) * 0.12
    # two low metal contraction ticks
    tick = np.zeros(len(t))
    for k, (t0, a) in enumerate(((0.06, 0.18), (0.19, 0.11))):
        m_ = metal(0.1, 150, 700, 8, (0.01, 0.04), seed + 30 + k)
        i0 = int(t0 * SR)
        tick[i0:i0 + len(m_)] += m_[:len(t) - i0] * a
    return fade_tail(sh + crack_ + np.vstack([tick, np.roll(tick, 24)]), 0.05)


def fall_sfx(seed, d=0.5, rise=False):
    """Red-hot object accelerating toward the lava (or rising out of it)."""
    w = whoosh(d, 300 if not rise else 1600, 2600 if not rise else 260, curve=2.4 if not rise else 0.6,
               tail=0.05, pan0=0.0, pan1=0.0, seed=seed, onset=0.25, low=0.9)
    t = tt(d + 0.05)
    s = np.vstack([hp(noise(d + 0.05, seed + 7 + ch), 3500) for ch in range(2)]) * (0.1 + 0.25 * np.clip(t / d, 0, 1) ** 2) * (np.abs(np.sin(TWO_PI * 13 * t)) ** 3)
    return w + s * 0.35


def heartbeat():
    d = 0.6
    t = tt(d)
    def one(t0, a):
        tt_ = np.clip(t - t0, 0, None)
        on = (t >= t0)
        f = 48 + 22 * np.exp(-tt_ * 25)
        return on * np.sin(TWO_PI * np.cumsum(f * on) / SR) * np.exp(-tt_ * 13) * np.minimum(1, tt_ / 0.004) * a
    y = one(0, 1.0) + one(0.22, 0.65)
    y += lp(noise(d, 77), 160, 4) * (np.exp(-t * 30) + 0.6 * (t > 0.22) * np.exp(-np.clip(t - 0.22, 0, None) * 30)) * 1.2
    return fade_tail(sat(y, 1.5), 0.05)


def riser(d, f0=250, f1=9000, seed=0, trem=True, bw=1.4):
    t = tt(d)
    p = t / d
    fc = f0 * (f1 / f0) ** (p ** 1.4)
    out = np.vstack([tv_filter(noise(d, seed + ch), fc, 'band', bw) for ch in range(2)])
    amp = p ** 2.2
    if trem:
        rate = 4 + 12 * p ** 1.5
        amp = amp * (0.6 + 0.4 * np.sin(TWO_PI * np.cumsum(rate) / SR) ** 2)
    return fade_tail(out * amp * 0.5, 0.01)


def pitch_riser(d, root=41, semis=12, cut0=300, cut1=2200, seed=0):
    t = tt(d)
    p = t / d
    r = R(seed)
    out = np.zeros((2, len(t)))
    for m in (root, root + 7, root + 12):
        for ch in range(2):
            for _ in range(3):
                s, _, _ = saw_f(note(m + semis * p ** 1.6 + r.uniform(-0.2, 0.2)), r.uniform(0, 1))
                out[ch] += s
    out /= 5
    fc = cut0 * (cut1 / cut0) ** p
    out = np.vstack([tv_filter(out[ch], fc, 'low', order=2, block=512) for ch in range(2)])
    return fade_tail(np.tanh(out * (p ** 1.5) * 2.0) * 0.4, 0.01)


def varispeed(x, rate):
    pos = np.cumsum(rate)
    pos = np.clip(pos, 0, x.shape[-1] - 2)
    i = pos.astype(int)
    fr = pos - i
    return x[..., i] * (1 - fr) + x[..., i + 1] * fr


# ======================================================================== harmony
CH = {'Fm7': [53, 56, 60, 63], 'Fm9': [53, 56, 60, 67], 'Db': [49, 53, 56, 60], 'Gb': [54, 58, 61, 65],
      'Eb': [51, 56, 58, 63], 'DbC': [48, 53, 56, 61]}   # Eb = Ebsus4 (no G natural), DbC = Db/C (C-F-Ab-Db)
ROOT = {'Fm7': 41, 'Fm9': 41, 'Db': 37, 'Gb': 42, 'Eb': 39, 'DbC': 36}
SCHED = [(4, 6, 'Fm7'), (6, 8, 'Fm7'), (8, 10, 'Gb'),
         (10, 14, 'Fm7'), (14, 18, 'Db'), (18, 22, 'Gb'), (22, 26, 'Fm7'), (26, 30, 'Db'), (30, 34, 'Eb'),
         (34, 38, 'Gb'), (38, 40, 'Fm7'),
         (40, 42, 'Fm9'), (42, 44, 'Db'), (44, 45, 'Eb'),
         (45, 46.5, 'Fm7'), (46.5, 48, 'Db'), (48, 49, 'Gb'), (49, 50, 'DbC'),
         (50, 52, 'Fm7'), (52, 53, 'Db'), (53, 54, 'Eb'),
         (54, 56, 'Fm9'), (56, 58, 'Db'), (58, 59, 'Eb'), (59, 61, 'Fm9')]


def chord_at(t):
    for a, b, c in SCHED:
        if a <= t + 1e-6 < b:
            return c
    return 'Fm7'


PS = [10, 15, 20, 25, 30, 35]
WHIPS = [p + 4.5 for p in PS]


def in_whip(t):
    for w in WHIPS:
        a = w if int(round(w + 0.5)) % 10 == 0 else w + 0.25
        if a - 1e-6 <= t < w + 0.5 - 1e-6:
            return True
    return False


# ======================================================================== groove
def bass_cut(t):
    keys = [(4, 180), (6, 260), (9.5, 700), (10, 480), (15, 560), (20, 650), (25, 720), (30, 820), (35, 900), (40, 900),
            (45, 260), (49, 1500), (50, 1300), (54, 800), (60, 800)]
    return float(np.interp(t, [k[0] for k in keys], [k[1] for k in keys]))


def bass_line(t0, t1, gain=1.0):
    s = t0
    while s < t1 - 1e-6:
        step = int(round((s % 2.0) / S16))
        if step % 4 != 0 and not in_whip(s):
            root = ROOT[chord_at(s)]
            m = root
            bar = int(s // 2)
            if step in (7, 15) and bar % 2 == 1:
                m = root + 12
            if step == 14 and bar % 4 == 3:
                m = root + 1 if chord_at(s) in ('Fm7', 'Fm9') else root + 12
            vel = 1.0 if step % 4 == 2 else 0.78
            f = float(note(m))
            put(BASS, bass_note(f, bass_cut(s) * (1.25 if step % 4 == 2 else 1.0), vel=vel, seed=step), s, gain)
        s += S16


# leave room for the goal pop / hop 1 (51.75: no open hat, ride swells in softly) and hop 4 (52.25: nothing)
HAT_SKIP = {51.75: 'soft', 52.25: 'all'}


def hats_line(t0, t1, mode, g=1.0):
    s = t0
    i = 0
    while s < t1 - 1e-6:
        step = int(round((s % 2.0) / S16))
        skip = next((v for h, v in HAT_SKIP.items() if abs(s - h) < 1e-6), None)
        if not in_whip(s) and skip != 'all':
            pan = 0.6 * np.sin(i * 0.9)
            if mode in ('full', 'drop', 'build', 'lite', 'intro') and skip is None:
                if step % 4 == 2:
                    put(DRUMS, hat('o', 300 + i % 7), s, 0.42 * g, pan=-0.15, room=0.1)
                elif mode != 'intro' or step % 2 == 1:
                    v = 0.42 if step % 2 == 1 else 0.24
                    if mode == 'lite' and step % 2 == 0:
                        v = 0
                    if v:
                        put(DRUMS, hat('c', 400 + i % 11), s, v * g, pan=pan)
            if mode == 'shaker':
                put(DRUMS, hat('s', 500 + i % 9), s, (0.18 if step % 2 else 0.1) * g, pan=0.5 * np.sin(i * 1.3), dly=0.2)
            if mode in ('drop', 'ride') and step % 4 == 2:
                rd = hat('r', 600 + i % 5)
                if skip == 'soft':
                    rd = rd * np.minimum(1, np.arange(len(rd)) / (0.03 * SR))
                put(DRUMS, rd, s, 0.22 * g, pan=0.3, rev=0.1)
        s += S16
        i += 1


def claps_line(t0, t1, g=1.0, metal_amt=0.0):
    b = t0
    while b < t1 - 1e-6:
        beat = int(round((b % 2.0) / BEAT))
        if beat in (1, 3) and not in_whip(b):
            put(DRUMS, clap_s(800 + int(b * 2) % 6, metal_amt), b, 0.6 * g, room=0.3, rev=0.08)
        b += BEAT


def perc_line(t0, t1, g=1.0, toms=False):
    s = t0
    i = 0
    while s < t1 - 1e-6:
        step = int(round((s % 2.0) / S16))
        bar = int(s // 2)
        if not in_whip(s):
            if step in (3, 11) or (step == 6 and bar % 2 == 1) or (step == 13 and bar % 4 == 2):
                put(DRUMS, clank_s(900 + i % 8), s, 0.3 * g, pan=(-0.55 if i % 2 else 0.55), dly=0.35)
            if toms and step in (14, 15) and bar % 4 == 3:
                put(DRUMS, tom_s(950 + step, 120 if step == 14 else 95), s, 0.5 * g, pan=(0.3 if step == 14 else -0.3), room=0.2)
        s += S16
        i += 1


# ---------- acid
ACID_PAT = {
    'A': [(0, 1, 0), None, (0, 0, 0), (12, 0, 1), (0, 0, 0), None, (3, 1, 0), (0, 0, 0),
          None, (0, 0, 0), (1, 1, 1), (0, 0, 0), (12, 0, 0), None, (7, 1, 0), (0, 0, 1)],
    'B': [(0, 1, 0), (0, 0, 0), (12, 0, 1), (0, 0, 0), None, (3, 0, 0), (0, 1, 0), None,
          (0, 0, 0), (10, 0, 1), (12, 1, 0), None, (0, 0, 0), (1, 0, 1), (0, 1, 0), None],
    'C': [(0, 1, 0), (12, 0, 1), (0, 0, 0), (3, 1, 0), (0, 0, 0), (12, 0, 1), (10, 1, 0), (0, 0, 0),
          (0, 1, 0), (1, 0, 1), (0, 0, 0), (12, 1, 0), (0, 0, 1), (3, 0, 0), (7, 1, 1), (0, 0, 0)],
}


def acid_pattern_at(t):
    if t < 20:
        return 'A'
    if t < 30:
        return 'B' if int(t // 2) % 4 != 3 else 'A'
    if t < 40:
        return 'B' if int(t // 2) % 2 == 0 else 'C'
    if t < 45:
        return 'A'
    return 'C'


def acid_cut(t):
    t = np.asarray(t, np.float64)
    keys = [(10, 220), (39.9, 1350), (40, 260), (44.9, 380), (45, 300), (49.9, 2700), (50, 1100), (54, 1500)]
    base = np.interp(t, [k[0] for k in keys], [k[1] for k in keys])
    # one long 10->40 ramp; each power-up adds a small swell (opens through the showcase, eases into the whip)
    ph = np.clip((t - 10) % 5 / 5, 0, 1)
    wig = np.where((t >= 10) & (t < 40), 1 + 0.16 * np.sin(np.pi * ph) ** 2, 1.0)
    return base * wig


def acid_render(t0, t1, root=29):
    """F1-rooted 303 line (sounds in F2-F3 because steps add 12)."""
    n = int(round((t1 - t0) * SR))
    t = t0 + np.arange(n) / SR
    semis = np.zeros(n)
    gate = np.zeros(n)
    fenv = np.zeros(n)
    accent = np.zeros(n)
    nsteps = int(round((t1 - t0) / S16))
    prev = None
    prev_slide = False
    for k in range(nsteps):
        st = t0 + k * S16
        a, b = int(round(k * S16 * SR)), min(n, int(round((k + 1) * S16 * SR)))
        pat = ACID_PAT[acid_pattern_at(st)]
        ev = pat[int(round((st % 2.0) / S16)) % 16]
        if ev is not None and ev[0] == 1 and chord_at(st) in ('Eb', 'DbC'):
            ev = None   # no Gb against Ebsus4 / Db/C
        if ev is None or in_whip(st):
            prev_slide = False
            continue
        m = root + 12 + ev[0]
        semis[a:b] = m
        if prev_slide and prev is not None:
            g = min(b - a, int(0.055 * SR))
            semis[a:a + g] = np.linspace(prev, m, g)
        glen = (b - a) if ev[2] else int((b - a) * 0.6)
        gate[a:a + glen] = 1.0
        if not prev_slide:
            tl = np.arange(n - a) / SR
            dec = 0.11 if ev[1] else 0.2
            seg = np.exp(-tl / dec) * (1.0 + 0.6 * ev[1])
            fenv[a:] = np.maximum(fenv[a:] * (tl > 0.0005), seg) if False else seg
            accent[a:b] = ev[1]
        else:
            accent[a:b] = accent[a - 1] if a > 0 else 0
        prev = m
        prev_slide = bool(ev[2])
    # fill semis holes with last value to avoid pitch jumps to 0
    last = root + 12
    idx = np.where(semis == 0)[0]
    if len(idx):
        filled = semis.copy()
        nz = semis != 0
        ii = np.where(nz, np.arange(n), 0)
        np.maximum.accumulate(ii, out=ii)
        filled = semis[ii]
        filled[filled == 0] = last
        semis = filled
    g = lp(gate, 160, 1)
    f = note(semis)
    s, _, _ = saw_f(f, 0.0)
    base = acid_cut(t) * (1 + 0.18 * np.sin(TWO_PI * 0.11 * t))
    fc = base * 0.55 * 2 ** (1.8 * fenv)
    ceil = np.interp(t, [10, 29.9, 30.5, 61], [2000, 2000, 2800, 2800])
    fc = ceil * np.tanh(fc / ceil)   # soft ceiling, never pinned (resonance keeps moving)
    kk = np.where(t < 45, 3.15, np.where(t < 50, 3.15 + 0.25 * (t - 45) / 5, 3.4))
    kk = kk * np.clip(1 - (fc - 800) / 2400, 0.7, 1.0)
    y = ladder(s * g * (0.8 + 0.4 * accent), fc, kk, 1.3)
    y = np.tanh(y * 3.2) * 0.5
    y_d = hp(lp(y, 2600, 2), 70)
    y_b = hp(lp(y, 3500, 2), 70)
    xf = np.clip((t - 29.5) / 1.0, 0, 1)
    return y_d * (1 - xf) + y_b * xf


# ======================================================================== ARRANGEMENT
# ---------------- 0-4 HOOK
def lava_bed(d, seed):
    t = tt(d)
    out = []
    low_ = lp(noise(d, seed + 50), 140, 4) * 3.0          # mono below 140 Hz
    for ch in range(2):
        nz = noise(d, seed + ch)
        lfo = 0.6 + 0.4 * lp(R(seed + 10 + ch).standard_normal(len(t)), 3, 1) * 30
        y = low_ + lp(hp(nz, 140), 420, 2) * 0.5 * np.clip(lfo, 0.1, 1.5)
        out.append(y)
    return np.vstack(out)


bed = lava_bed(3.2, 100)
bed *= np.minimum(1, tt(3.2) / 0.02)
put(SFX, fade_tail(bed, 0.4), 0.0, 0.5)
# drone: dark low saw cluster, swells to the GAME slam
dr = pad([29, 36, 41], 2.6, 260, att=0.9, rel=1.0, seed=3)
put(SYN, dr, 0.0, 0.9, rev=0.2)
# opening low pulse (ring pulse 1) and ring 2 pulse
pulse0 = sub_boom(0.6, 70, 40, 0.12, 1.3) * 0.7
put(HITS, pulse0, 0.0, 0.8)
put(SFX, tok(160, 0.03, 1.2, 21, 0.12), 0.003, 0.9, rev=0.3)
put(SFX, transient(22, amt=0.8), 0.003, 0.6, rev=0.2)
put(HITS, sub_boom(0.5, 60, 40, 0.09, 1.2), 0.25, 0.35)


def bubble(seed, f=150):
    d = 0.12
    t = tt(d)
    y = bp(noise(d, seed), f * 0.7, f * 1.5, 2) * np.minimum(1, t / 0.004) * np.exp(-t * 35)
    y += np.sin(TWO_PI * f * 0.6 * t) * np.exp(-t * 40) * 0.3
    return fade_tail(y * 2.0)


for i, tb in enumerate([0.217, 0.223, 0.353, 0.357, 0.373, 0.45, 0.489, 0.499, 0.579]):
    put(SFX, bubble(200 + i, 120 + 25 * (i % 4)), tb, 0.35, pan=0.4 * np.sin(i * 2.1))
# 0.5 PLOP: magma gulp
d = 0.9
t = tt(d)
gulp = np.sin(TWO_PI * np.cumsum(32 + 110 * np.exp(-t * 14)) / SR) * np.exp(-t * 5) * np.minimum(1, t / 0.003)
put(HITS, sat(gulp, 1.8), 0.5, 0.9)
put(SFX, lp(splash(230, 0.8), 1700, 2), 0.5, 0.8, rev=0.2)
put(SFX, steam(240, 0.6, 0.7), 0.55, 0.6)
duck(DIPH, 0.5, 0.4, 0.15)
# 0.775 suck into GAME / 1.275 suck into OVER
for ts, sd in ((0.775, 250), (1.275, 260)):
    put(SFX, whoosh(0.225, 600, 5000, curve=2.2, tail=0.0, pan0=0.0, pan1=0.0, seed=sd, onset=0.35, low=0.4), ts, 0.85)
    put(SFX, rev_crash(0.225, sd + 5), ts, 0.4)
    inh = hp(noise(0.2, sd + 6), 3500) * np.minimum(1, tt(0.2) / 0.002) * np.exp(-tt(0.2) * 25)
    put(SFX, np.vstack([inh, inh[::-1] * 0 + hp(noise(0.2, sd + 7), 3500) * np.minimum(1, tt(0.2) / 0.002) * np.exp(-tt(0.2) * 25)]), ts, 0.45)
# 1.0 GAME / 1.5 OVER
put(SYN, braam(41, 2.2, seed=31, peak=2200), 1.0, 0.95, rev=0.3)
hit(1.0, 1.4, 270, 0.7, crash_d=1.6)
put(SYN, braam(41, 2.6, seed=37, slide=1.0, peak=2600), 1.5, 1.0, rev=0.35)
hit(1.5, 1.5, 280, 0.75, crash_d=1.8)
# gate the GAME braam so OVER's suck reads
gate = np.ones(N)
a_, b_ = int(1.27 * SR), int(1.5 * SR)
gate[a_:b_] = np.linspace(1, 0.25, b_ - a_)
SYN[:, :int(1.5 * SR)] *= gate[:int(1.5 * SR)]
# 2.0 card flip
put(SFX, swish(0.2, 500, 4000, 290, 0.4), 2.0, 0.8, room=0.2)
put(SFX, tok(240, 0.015, 1.5, 291), 2.0, 0.9, pan=0.4)
put(SFX, transient(292, amt=0.5), 2.0, 0.3, pan=0.4)
for i, tw in enumerate([2.25, 2.294, 2.338, 2.381, 2.425, 2.469]):
    put(SFX, tok(330, 0.006, 1.2, 300 + i, 0.04), tw, 0.35 if i else 1.0, pan=-0.2 + 0.08 * i)
put(SFX, transient(309, amt=0.5), 2.25, 0.35)
# 2.5 DEAD: power failure (no buzzer): (a) tape-stop of the OVER braam, (b) gated F1 sub stutter, (c) relay clunk
i25 = int(2.5 * SR)
src = SYN[:, i25:i25 + int(0.6 * SR)].copy()
d = 0.42
t = tt(d)
rate = np.clip(1 - t / 0.35, 0, 1) ** 1.4
ts_ = varispeed(src, rate) * np.minimum(1, t / 0.002)
fts = 250 + 3800 * np.clip(1 - t / 0.35, 0, 1) ** 1.5
ts_ = np.vstack([tv_filter(ts_[ch], fts, 'low', order=2, block=256) for ch in range(2)])
put(SFX, fade_tail(ts_, 0.06), 2.5, 0.9)
# the live braam / drone collapse under the tape-stop (keeps the low drone faintly until the rewind)
gsyn = np.ones(int(0.5 * SR))
gsyn[:int(0.012 * SR)] = np.linspace(1, 0.18, int(0.012 * SR))
gsyn[int(0.012 * SR):] = 0.18
SYN[:, i25:i25 + len(gsyn)] *= gsyn
gatev = np.zeros(len(t))
for a0, a1 in ((0.0, 0.03), (0.043, 0.075), (0.084, 0.115), (0.125, 0.4)):
    gatev[int(a0 * SR):int(a1 * SR)] = 1
gatev = lp(gatev, 300, 1)
subst = lp(np.tanh(2.5 * np.sin(TWO_PI * float(note(29)) * t)) * gatev * np.exp(-t * 4), 120, 4)
put(HITS, fade_tail(subst, 0.04), 2.5, 0.75)
put(SFX, tok(150, 0.025, 1.0, 312, 0.12), 2.5, 0.8, room=0.25)
put(SFX, transient(310, amt=0.4), 2.5, 0.5, pan=0.2)
put(SFX, tok(160, 0.012, 0.5, 313), 2.625, 0.22, pan=0.25)
put(SFX, transient(311, amt=0.35), 2.75, 0.2, pan=0.3)
duck(DIPH, 2.5, 0.45, 0.2)

# ---------------- 4-6 REJOUER (music built before the rewind is taken from 1.0-3.0)
# 4.0 CRT ON: degauss + slam
d = 0.9
t = tt(d)
hum = (np.sin(TWO_PI * 50 * t) + 0.6 * np.sin(TWO_PI * 100 * t) + 0.3 * np.sin(TWO_PI * 150 * t)) * np.minimum(1, t / 0.004) * np.exp(-t / 0.22)
put(HITS, sat(hum, 2.5) * 0.6, 4.0, 1.0)
put(SFX, crackle(0.25, 900, 320, 1500, 9000) * 3.0, 4.0, 0.6, pan=-0.2)
hit(4.0, 1.1, 330, 0.55)
put(SYN, pad(CH['Fm7'], 2.0, 700, att=0.25, rel=0.4, seed=40), 4.0, 0.55, rev=0.35)
put(BASS, np.sin(TWO_PI * float(note(29)) * tt(2.0)) * np.minimum(1, tt(2.0) / 0.2) * 0.35, 4.0, 1.0)
put(SFX, tok(260, 0.01, 0.5, 333), 4.25, 0.3)
# 4.5 reveal
put(SFX, tok(300, 0.012, 0.8, 340), 4.5, 0.45)
put(SFX, swish(0.25, 400, 2500, 341, -0.5), 4.5, 0.5)
put(SFX, swish(0.25, 400, 2500, 342, 0.5), 4.5, 0.5)
for tk in (4.5, 5.0, 5.5):
    kick_at(tk, 0.8, 0.8, lpf=500 if tk < 5.5 else 1200)
hats_line(4.5, 5.5, 'intro', 0.5)
# 5.0 PRESS
put(SFX, tok(170, 0.02, 1.2, 350, 0.1), 5.0, 0.9)
hit(5.0, 1.2, 360, 0.6, crash_d=1.0)
put(SYN, pitch_riser(1.0, 29, 12, 200, 2200, 361), 5.0, 1.0, rev=0.2)
# 5.5 dive
put(SFX, whoosh(0.5, 300, 7000, curve=2.0, tail=0.05, pan0=0.0, pan1=0.0, seed=370, onset=0.3), 5.5, 1.0)
put(SFX, rev_crash(0.5, 371), 5.5, 0.55)
put(SFX, transient(372, amt=0.7), 5.5, 0.5)
for i in range(4):
    put(DRUMS, snare_s(380 + i), 5.5 + i * S16, 0.25 + 0.15 * i + (0.25 if i == 2 else 0), room=0.2)
put(SFX, hp(noise(0.08, 385), 2500) * np.exp(-tt(0.08) * 40) * 0.5, 5.75, 0.6)

# ---------------- 6-10 NIVEAU 1
put(SFX, crash(1.4, 400), 6.0, 0.35)
put(SFX, hp(noise(0.15, 401), 800) * np.exp(-tt(0.15) * 25) * 0.6, 6.0, 0.7)
hit(6.15, 1.3, 410, 0.7)
stamp(6.375, 420, 0.6, 0.7)
for i, th in enumerate([6.05, 6.2, 6.3, 6.4]):
    put(SFX, tok(380, 0.005, 0.5, 430 + i, 0.04), th, 0.18, pan=0.6)
b = 6.0
while b < 9.49:
    kick_at(b, 1.0, 1.0)
    b += BEAT
bass_line(6.0, 9.5, 0.85)
hats_line(6.0, 9.5, 'intro', 0.8)
claps_line(6.0, 9.5, 0.8)
put(SYN, pad(CH['Fm7'], 2.0, 900, att=0.1, rel=0.3, seed=44), 6.0, 0.45, rev=0.35)
put(SYN, pad(CH['Gb'], 2.0, 1100, att=0.1, rel=0.3, seed=45), 8.0, 0.45, rev=0.35)
XS = [350, 1500, 960, 445, 1460, 715, 1540, 500]
for i in range(8):
    te = 7.0 + i * 0.25
    pn = (XS[i] - 960) / 960 * 0.85
    put(SFX, eruption(440 + i * 3, 0.7 + 0.05 * i, 0.9), te, 0.6, pan=pn, rev=0.15)
    if i != 1:
        put(SFX, transient(448 + i * 3, amt=0.7), te, 0.4, pan=pn)       # spurt crack on the burst frame
    vo_ = [29, 41, 48] if i % 2 == 0 else [30, 42, 49]     # F5 / Gb5 power voicings (phrygian), never chromatic
    put(SYN, hoover(vo_, 0.2, seed=460 + i, scoop=0.0, cut=700 + 200 * i), te, 0.6 + 0.04 * i, pan=pn * 0.6, dly=0.15)
    duck(DIPH, te, 0.3, 0.08)
# logo sink (7.225) and eruption 2 (7.25) are 25 ms apart: one shared splash/thump at 7.233 marks both
put(SFX, splash(470, 0.7), 7.233, 0.7, pan=0.1)
put(HITS, sub_boom(0.4, 80, 40, 0.1), 7.233, 0.4)
put(HITS, sub_boom(0.25, 95, 45, 0.05, 2.0), 7.233, 0.55)
put(SFX, transient(471, amt=0.9), 7.233, 0.55, pan=0.1)
# 9.0 overheat
for i in range(16):
    tr_ = 9.0 + i * 0.0625
    put(DRUMS, tom_s(480 + i % 5, 105 if i % 2 == 0 else 82), tr_, 0.12 + 0.3 * (i / 15) ** 1.3, room=0.2)
    put(DRUMS, snare_s(480 + i % 5, 0.1), tr_, 0.04 + 0.08 * (i / 15), room=0.15)
    put(HITS, sub_boom(0.12, 70, 45, 0.04, 1.2), tr_, 0.08 + 0.25 * (i / 15))
put(SFX, riser(1.0, 300, 9000, 490), 9.0, 0.8)
put(SYN, pitch_riser(1.0, 41, 12, 300, 2500, 491), 9.0, 0.7, rev=0.2)
put(SFX, transient(492, amt=0.7), 9.0, 0.4)
put(SFX, transient(493, amt=0.9), 9.5, 0.6, room=0.2)
put(SFX, rev_crash(0.5, 494), 9.5, 0.6)
put(HITS, sub_boom(0.5, 70, 40, 0.12), 9.5, 0.5)

# ---------------- 10-40 POWER-UPS
b = 10.0
while b < 39.99:
    if not in_whip(b):
        kick_at(b, 1.0, 1.0)
    b += BEAT
bass_line(10.0, 40.0, 1.0)
hats_line(10.0, 20.0, 'full', 0.9)
hats_line(20.0, 30.0, 'full', 1.0)
hats_line(30.0, 40.0, 'drop', 1.0)
claps_line(10.0, 40.0, 1.0)
perc_line(20.0, 30.0, 0.9)
perc_line(30.0, 40.0, 1.0, toms=True)
for a, b_, c in SCHED:
    if 10 <= a < 40:
        put(SYN, pad(CH[c], b_ - a, 1100 + 30 * (a - 10), att=0.4, rel=0.6, seed=int(a * 10)), a, 0.62, rev=0.55)

for i, P in enumerate(PS):
    sd = 1000 + i * 100
    put(SFX, eruption(sd, 1.1, 1.3), P, 0.8, pan=0.0, rev=0.2)
    hit(P, 0.95, sd + 1, 0.55, crash_d=(1.6 if P in (10, 20, 30) else 0.9))
    # P+0.5
    if P in (10, 15, 35):
        put(SFX, fall_sfx(sd + 10, 0.5), P + 0.5, 0.75)
    elif P == 20:
        put(SFX, fall_sfx(sd + 10, 0.45, rise=True), P + 0.5, 0.65)
        put(SFX, lp(noise(0.5, sd + 11), 300, 2) * np.exp(-tt(0.5) * 5) * 1.5 + crackle(0.5, 200, sd + 12, 300, 2500) * 1.5, P + 0.5, 0.6)
        put(SFX, transient(sd + 13, amt=0.5), P + 0.5, 0.3)
    elif P == 25:
        put(SFX, whoosh(0.36, 2500, 300, curve=0.7, tail=0.05, pan0=0, pan1=0, seed=sd + 10, onset=0.6), P + 0.5, 0.6)
    # P+1.0 landings
    if P in (10, 15, 35):
        hit(P + 1.0, 1.0 if P != 35 else 1.15, sd + 20, 0.5, rev=0.25)
        put(SFX, splash(sd + 21), P + 1.0, 0.7)
        put(SFX, steam(sd + 22, 0.8 if P != 35 else 1.0, 1.0), P + 1.02, 0.9)
        put(SFX, cool_sheen(sd + 23), P + (1.14 if P != 35 else 1.12), 1.0)
        put(SFX, transient(sd + 24, amt=0.8), P + (1.14 if P != 35 else 1.12), 0.55, pan=0.3)
    # P+1.5 answer stamp
    stamp(P + 1.5, sd + 30, 1.0, 1.0)
    # counter clack
    put(SFX, clack(sd + 40), P + 2.12, 0.8, pan=0.6)
    put(SFX, transient(sd + 41, amt=0.4), P + 2.12, 0.25, pan=0.6)

# per power-up showcases
# P=10 Navettes
for tt_, g_ in ((12.0, 0.45), (12.25, 0.25), (12.5, 0.45), (12.625, 0.2), (12.75, 0.2), (13.125, 0.18), (13.25, 0.18)):
    put(SFX, tok(320, 0.008, 0.8, int(tt_ * 100)), tt_, g_, pan=-0.2)
put(SFX, swish(0.25, 600, 2800, 1300, 0.0), 13.0, 0.55)
put(SFX, tok(260, 0.01, 0.8, 1301), 13.0, 0.4)
for i in range(14):
    put(SFX, tok(520, 0.003, 0.5, 1310 + i, 0.03), 13.5 + i * 0.0225, 0.12, pan=0.1)
# P=15 Objets interdits: branding sear
for i, tb in enumerate([16.1, 16.163, 16.225, 16.288, 16.35, 16.413, 16.475, 16.538]):
    put(SFX, steam(1600 + i, 0.12, 0.6), tb, 0.45, pan=-0.6 + 0.17 * i)
put(SFX, tok(300, 0.01, 0.9, 1700), 17.0, 0.5)
put(SFX, whoosh(0.3, 500, 3500, curve=0.8, tail=0.06, pan0=0, pan1=0, seed=1701, onset=0.7), 17.063, 0.5)
put(SFX, transient(1705, amt=0.5), 17.063, 0.4)
put(SFX, swish(0.3, 600, 2400, 1702, 0.4), 17.5, 0.6)
put(SFX, swish(0.3, 600, 2400, 1703, -0.4), 18.0, 0.6)
put(SFX, whoosh(0.3, 3500, 500, curve=0.8, tail=0.06, pan0=0, pan1=0, seed=1704, onset=0.7), 18.5, 0.45)
# P=20 map
put(SFX, transient(2000, amt=0.6), 21.0, 0.4)
hit(21.0, 0.7, 2001, 0.4, sub=True, g=0.7, rev=0.15)
for i, tp in enumerate([21.0, 21.25, 21.5, 21.75, 22.0, 22.25]):
    put(SFX, tok(280 + 20 * (i % 3), 0.01, 0.9, 2010 + i), tp, 0.45, pan=-0.4 + 0.16 * i, room=0.15)
put(SFX, tok(420, 0.005, 0.7, 2020), 22.0, 0.3, pan=-0.6)
put(SFX, tok(220, 0.012, 1.0, 2021), 22.5, 0.5)
put(SFX, tok(360, 0.008, 1.6, 2022), 22.56, 1.0, pan=0.1)
put(SFX, transient(2025, amt=0.6), 22.56, 0.45, pan=0.1)
put(SFX, tok(300, 0.01, 0.8, 2023), 23.0, 0.4)
put(SFX, swish(0.4, 900, 2200, 2024, 0.2), 23.0, 0.35)


def sonar(seed, g=1.0):
    d = 0.9
    t = tt(d)
    y = sub_boom(d, 75, 50, 0.15, 1.2) * 0.7
    ring = bp(noise(d, seed), 500, 900, 2) * np.minimum(1, t / 0.004) * np.exp(-t / 0.18) * 1.5
    return fade_tail(y + ring) * g


put(SFX, sonar(2030), 23.5, 0.55, rev=0.35)
put(SFX, sonar(2031), 23.75, 0.3, rev=0.35)
put(SFX, sonar(2032), 24.0, 0.25, rev=0.35)
# P=25 clash
put(SFX, whoosh(0.25, 400, 4000, curve=2.0, tail=0.0, pan0=-0.8, pan1=0, seed=2500, onset=0.2), 25.0, 0.4)
put(SFX, whoosh(0.25, 400, 4000, curve=2.0, tail=0.0, pan0=0.8, pan1=0, seed=2501, onset=0.2), 25.0, 0.4)
hit(25.25, 1.3, 2502, 1.3, crash_d=1.2)
put(SFX, crackle(0.6, 300, 2503, 1000, 7000) * 3, 25.25, 0.6)
put(SFX, lp(noise(0.8, 2504), 260) * np.exp(-tt(0.8) * 4) * 1.2, 26.0, 0.5)
for i, tk in enumerate([27.0, 27.5, 28.0]):
    put(SFX, tok(250, 0.012, 1.0, 2510 + i), tk, 0.5, pan=0.15)
    put(SFX, tok(420, 0.004, 0.5, 2515 + i), tk + 0.03, 0.2, pan=0.15)
put(SFX, tok(170, 0.02, 1.2, 2520, 0.1), 28.5, 0.8)
hit(28.5, 0.85, 2521, 0.45, g=0.85)
# P=30 food
for i, tp in enumerate([30.5, 30.75, 31.0, 31.25]):
    put(SFX, tok(300 + 30 * i, 0.009, 0.9, 3000 + i), tp, 0.45, pan=-0.5 + 0.3 * i)
for i, tc in enumerate([31.0, 31.25, 31.5, 31.75]):
    put(SFX, swish(0.06, 2000, 600, 3010 + i, 0.2), tc - 0.06, 0.4)
    hit(tc, 0.6 + (0.2 if i == 3 else 0), 3020 + i, 0.35, sub=(i in (0, 3)), g=0.7, rev=0.12, duck_depth=0.35)
put(SFX, swish(0.3, 500, 4000, 3030, 0.0), 32.0, 0.8)
put(SFX, tok(260, 0.01, 1.2, 3031), 32.0, 0.5)
for i, tc in enumerate([32.5, 33.0, 33.5]):
    put(SFX, swish(0.2, 700, 3000, 3040 + i, 0.4), tc, 0.45)
    put(SFX, tok(300, 0.009, 0.8, 3045 + i), tc, 0.35)
for i, tc in enumerate([32.02, 32.52, 33.02, 33.52]):
    put(SFX, tok(400, 0.004, 0.5, 3050 + i, 0.04), tc, 0.15, pan=0.3)
# P=35 cashless
put(SFX, sat(saw_f(np.full(int(0.3 * SR), float(note(29))))[0] * np.exp(-tt(0.3) * 10), 3) * 0.2, 36.5, 0.6)
for i, ts_ in enumerate([37.0, 37.5, 38.0]):
    put(SFX, tok(280, 0.01, 1.0, 3500 + i), ts_, 0.5, pan=-0.2)
put(SFX, swish(0.3, 500, 2500, 3510, 0.0), 38.5, 0.5)
for ta_ in (32.0, 33.0, 34.0, 37.0, 38.0, 39.0):
    put(SFX, transient(int(ta_ * 10) + 7, amt=0.5), ta_, 0.32, pan=0.15)
# dot hops (jump swish / land thock)
for tj in (13.5, 18.5, 28.5, 33.5, 38.5):
    put(SFX, swish(0.3, 400, 1800, int(tj * 10), -0.4), tj, 0.45)
for tl in (14.0, 19.0, 29.0, 34.0, 39.0):
    put(SFX, tok(190, 0.018, 1.4, int(tl * 10) + 1, 0.1), tl, 0.8, room=0.2)
# whips: build into the cut
for w in WHIPS:
    put(SFX, whoosh(0.5, 350, 6500, curve=2.2, tail=0.12, pan0=0.7, pan1=-0.7, seed=int(w * 10), onset=0.3), w, 1.0)
    put(SYN, rev_crash(0.5, int(w * 10) + 1), w, 0.25)
    put(SFX, transient(int(w * 10) + 2, amt=0.6), w, 0.5, pan=0.5, room=0.2)

# ---------------- 40-45 BREAKDOWN
put(SFX, eruption(4000, 0.7, 1.4), 40.0, 0.55, rev=0.4)
put(SFX, transient(4003, amt=0.8), 40.0, 0.55, rev=0.2)
put(HITS, sub_boom(1.0, 70, 32, 0.4), 40.0, 0.6)
duck(DIPH, 40.0, 0.4, 0.3)
for hb in (40.0, 41.0, 42.0, 43.0, 44.0):
    put(BASS, heartbeat(), hb, 0.75)
put(SYN, pad(CH['Fm9'], 2.0, 1100, att=0.5, rel=0.8, seed=401), 40.0, 0.65, rev=0.6)
put(SYN, pad(CH['Db'], 2.0, 1200, att=0.4, rel=0.8, seed=402), 42.0, 0.65, rev=0.6)
put(SYN, pad(CH['Eb'], 1.0, 1400, att=0.3, rel=0.5, seed=403), 44.0, 0.65, rev=0.6)
air = np.vstack([hp(noise(5.0, 4090 + ch), 2500, 2) for ch in range(2)]) * (0.5 + 0.5 * np.sin(TWO_PI * 0.2 * tt(5.0)) ** 2)
air *= np.minimum(1, tt(5.0) / 0.3) * np.minimum(1, (5.0 - tt(5.0)) / 0.3)
put(SFX, lp(air, 9000, 2), 40.0, 0.035)
hats_line(42.0, 44.5, 'shaker', 0.8)
put(SFX, fall_sfx(4010, 0.5), 40.5, 0.5)
put(SFX, transient(4011, amt=0.5), 40.5, 0.4, rev=0.2)
put(SFX, splash(4020), 41.0, 0.5)
put(SFX, transient(4024, amt=0.6), 41.0, 0.5)
put(SFX, tok(200, 0.02, 0.8, 4021, 0.1), 41.0, 0.55)
put(SFX, tok(380, 0.006, 0.8, 4022), 41.0, 0.35, pan=0.3)
put(SFX, tok(300, 0.006, 0.6, 4023), 41.16, 0.3, pan=0.3)
for i, tcm in enumerate([41.012, 41.025, 41.038, 41.054, 41.070, 41.089, 41.111, 41.138, 41.174, 41.234]):
    put(SFX, tok(600, 0.003, 0.6, 4030 + i, 0.03), tcm, 0.1, pan=0.2)
stamp(41.5, 4045, 0.85, 0.9, rev=0.25, room=0.2)      # w3 answer stamp 'RETROUVE TA BANDE.' (darker room)
duck(DIPH, 41.5, 0.5, 0.2)
put(SFX, clack(4040), 41.52, 0.3, pan=0.2)
put(SFX, tok(220, 0.012, 1.0, 4041), 42.0, 0.5)
for i, ta in enumerate([42.5, 42.75, 43.0]):
    put(SFX, tok(300 + 25 * i, 0.01, 1.4, 4050 + i), ta, 0.65, pan=0.3, rev=0.2)
put(SFX, tok(170, 0.02, 1.0, 4055, 0.1), 43.0, 0.5)
put(SFX, tok(260, 0.012, 0.9, 4056), 43.5, 0.45)
put(SFX, whoosh(0.5, 300, 6500, curve=2.4, tail=0.12, pan0=0.7, pan1=-0.7, seed=4060, onset=0.4), 44.5, 1.0)
put(SYN, rev_crash(0.5, 4061), 44.5, 0.35)
put(SFX, transient(4062, amt=0.6), 44.5, 0.5, pan=0.5, room=0.2)

# ---------------- 45-50 BUILD
hit(45.0, 1.1, 4500, 0.55, crash_d=1.2)
put(SFX, eruption(4501, 1.1, 1.2), 45.0, 0.7)
for i in range(14):
    put(SFX, tok(500, 0.003, 0.6, 4510 + i, 0.03), 45.0 + i * 0.03125, 0.08, pan=0.7 * np.sin(i * 1.7))
b = 45.0
while b < 48.99:
    kick_at(b, 1.0, 0.95, hpf=30 + 140 * ((b - 45) / 4) ** 1.5, sc=0.9)
    b += BEAT
bass_line(45.0, 49.0, 0.9)
hats_line(45.0, 49.0, 'build', 0.9)
for a, b_, c in SCHED:
    if 45 <= a < 50:
        put(SYN, pad(CH[c], b_ - a, 1000 + 400 * (a - 45), att=0.3, rel=0.4, seed=int(a * 10)), a, 0.45 + 0.04 * (a - 45), rev=0.45)
# industrial build: hall-washed claps + kick/tom roll (low-passed kick + toms), snare only as a quiet top layer;
# everything ends at 49.88 (vacuum before the drop)
claps_line(45.0, 49.0, 0.7)
for b in (45.5, 46.5, 47.5, 48.5):
    put(DRUMS, clap_s(4590 + int(b * 2) % 5), b, 0.25, rev=0.6)
KR = lp(kick_s(1.0, 0.25), 400, 2)
tr_ = 47.0
k_ = 0
while tr_ < 49.87:
    p = (tr_ - 47.0) / 2.88
    step = 0.25 if tr_ < 48 else (0.125 if tr_ < 49.25 else 0.0625)
    if not (tr_ < 49.0 and abs((tr_ / 0.5) - round(tr_ / 0.5)) < 1e-6):   # leave the main kicks alone
        put(DRUMS, KR, tr_, (0.12 + 0.16 * p ** 1.3) * (0.6 if step < 0.1 else 1.0))
    put(DRUMS, tom_s(4600 + k_ % 7, 110 if k_ % 2 == 0 else 86), tr_, (0.1 + 0.16 * p ** 1.3) * (0.7 if step < 0.1 else 1.0), pan=(0.25 if k_ % 2 else -0.25), room=0.15, rev=0.1)
    if tr_ >= 48.0:
        put(DRUMS, snare_s(4620 + k_ % 5, 0.1), tr_, 0.03 + 0.06 * p, room=0.2)
    tr_ += step
    k_ += 1
put(SFX, riser(4.88, 200, 10000, 4700, bw=2.2), 45.0, 1.0)
put(SYN, pitch_riser(2.88, 41, 12, 300, 2600, 4701), 47.0, 0.8, rev=0.3)
put(SFX, swish(0.26, 400, 2000, 4710, 0.0), 45.5, 0.45)
for i in range(18):
    put(SFX, tok(450 + 30 * (i % 3), 0.003, 0.7, 4720 + i, 0.03), 45.75 + i * 0.04, 0.16 if i else 0.3, pan=0.15)
put(SFX, whoosh(0.19, 4000, 500, curve=0.5, tail=0.0, pan0=0.5, pan1=0, seed=4740, onset=0.5), 46.5, 0.5)
stamp(46.5, 4741, 1.0)
for i, tc in enumerate([47.0, 47.5, 47.75, 48.0, 48.25]):
    put(SFX, tok(300 + 20 * (i % 2), 0.009, 0.9, 4750 + i), tc, 0.45, pan=-0.3 + 0.15 * i)
put(SFX, tok(220, 0.012, 1.6, 4760), 48.5, 0.95)
put(SFX, transient(4761, amt=0.4), 48.5, 0.3)
# 49.0 tremor + 49.5 white-out
put(HITS, sub_boom(1.0, 70, 35, 0.5), 49.0, 0.5)
put(SFX, transient(4770, amt=0.6), 49.0, 0.4)
tv_ = tt(1.0)
trem = lp(noise(1.0, 4771), 120, 4) * (0.5 + 0.5 * np.sign(np.sin(TWO_PI * 20 * tv_))) * (0.3 + 0.7 * tv_) * 2.0
put(SFX, trem, 49.0, 0.6)
put(SFX, rev_crash(0.5, 4772), 49.5, 0.8)
put(SFX, transient(4773, amt=0.7), 49.5, 0.45)

# ---------------- 50-54 DROP
hit(50.0, 1.8, 5000, 0.9, crash_d=2.6)
put(SYN, braam(41, 2.4, seed=5001, peak=3000), 50.0, 0.85, rev=0.3)
put(SFX, crackle(0.8, 700, 5002, 1500, 9000) * 3.5, 50.075, 0.6)
put(SFX, hp(noise(0.3, 5003), 2000) * np.exp(-tt(0.3) * 15) * 0.6, 50.075, 0.6)
hit(50.125, 1.2, 5004, 0.9, sub=False, g=0.9)
b = 50.0
while b < 53.99:
    kick_at(b, 1.4, 1.05)
    b += BEAT
bass_line(50.0, 54.0, 1.05)
hats_line(50.0, 54.0, 'drop', 1.05)
claps_line(50.0, 54.0, 1.1, metal_amt=0.6)
perc_line(50.0, 54.0, 1.0)
for a, b_, c in SCHED:
    if 50 <= a < 54:
        put(SYN, pad(CH[c], b_ - a, 2400, att=0.05, rel=0.4, seed=int(a * 10)), a, 0.75, rev=0.65)
VO = {'Fm7': [41, 48, 53, 56], 'Db': [37, 44, 49, 53], 'Eb': [39, 46, 51, 56]}   # Eb = Ebsus4
for st_, dd_, c in ((50.0, 0.45, 'Fm7'), (50.75, 0.12, 'Fm7'), (50.875, 0.4, 'Fm7'), (51.5, 0.18, 'Fm7'),
                    (52.0, 0.45, 'Db'), (52.75, 0.2, 'Db'), (53.0, 0.4, 'Eb'), (53.5, 0.45, 'Fm7')):
    put(SYN, hoover(VO[c], dd_, seed=int(st_ * 100)), st_, 0.9, rev=0.35, dly=0.12)
# slot reel
put(SFX, swish(0.16, 900, 2400, 5010, 0.0), 50.5, 0.4)
for i, tf in enumerate([50.507, 50.522, 50.539, 50.559, 50.582, 50.612, 50.656]):
    put(SFX, tok(420, 0.004, 0.9, 5020 + i, 0.04), tf, 0.3 + (0.15 if i == 6 else 0), pan=0.1)
hit(50.875, 1.0, 5030, 0.7)
put(SFX, whoosh(0.7, 6000, 250, curve=0.45, tail=0.1, pan0=-0.3, pan1=0.3, seed=5040, onset=0.8), 51.5, 0.8)
# goal pop (51.75) and hop-1 landing (51.775) share one hit at 51.762 (12 ms from each)
put(SFX, tok(260, 0.01, 0.9, 5050), 51.762, 0.2, pan=0.5)
put(SFX, crackle(0.3, 300, 5051), 51.762, 0.6, pan=0.5)
put(SFX, transient(5052, amt=0.8), 51.762, 0.4, pan=0.3)
for i in range(7):
    tl = 51.775 + 0.15 * i if i else 51.762
    put(SFX, tok(230, 0.01, 1.2, 5060 + i, 0.07), tl, 0.7, pan=-0.6 + 0.18 * i)
    put(SFX, transient(5065 + i, amt=0.8), tl, 0.42, pan=-0.6 + 0.18 * i)
hit(52.8125, 0.8, 5070, 0.6, g=0.8, rev=0.2)
put(SFX, crackle(0.5, 600, 5071, 1500, 9000) * 3, 52.8125, 0.5, pan=0.5)
hit(53.0, 1.2, 5080, 0.75)
hit(53.5, 1.3, 5090, 0.8, crash_d=1.0)

# ---------------- 54-60 END CARD
put(SFX, crash(2.2, 5400), 54.0, 0.4, rev=0.3)
put(HITS, sub_boom(1.5, 70, 32, 0.5), 54.0, 0.75)
put(SFX, transient(5401, amt=0.6), 54.0, 0.4)
duck(DIPH, 54.0, 0.5, 0.3)
b = 54.0
while b < 58.49:
    kick_at(b, 1.1, 0.95)
    b += BEAT
bass_line(54.0, 58.5, 0.85)
hats_line(54.0, 58.5, 'full', 0.9)
claps_line(54.0, 58.5, 0.9)
put(SYN, pad(CH['Fm9'], 2.0, 2600, att=0.5, rel=0.5, seed=541), 54.0, 0.6, rev=0.6)
put(SYN, pad(CH['Db'], 2.0, 2800, att=0.1, rel=0.4, seed=561), 56.0, 0.55, rev=0.6)
put(SYN, pad(CH['Eb'], 0.88, 1800, att=0.1, rel=0.1, seed=581), 58.0, 0.55, rev=0.4)
put(SFX, whoosh(0.375, 300, 4000, curve=0.6, tail=0.08, pan0=0, pan1=0, seed=5500, onset=0.6), 55.25, 0.6)
for i, ti in enumerate([55.35, 55.40, 55.45, 55.50, 55.55]):
    put(SFX, tok(380, 0.004, 0.5, 5510 + i, 0.03), ti, 0.12, pan=-0.6 + 0.3 * i)
w_ = whoosh(0.5, 500, 5000, curve=2.0, tail=0.0, pan0=0.6, pan1=0.0, seed=5520, onset=0.4)
w_ *= 0.6 + 0.4 * np.sin(TWO_PI * np.cumsum(6 + 18 * tt(0.5) / 0.5) / SR) ** 2
put(SFX, w_, 55.5, 0.8)
hit(56.0, 1.3, 5600, 0.8, crash_d=1.2)
put(SFX, transient(5601, amt=1.4), 55.997, 0.6)
put(SFX, swish(0.3, 600, 3000, 5650, 0.0), 56.5, 0.45)
put(SFX, tok(300, 0.01, 0.8, 5651), 56.5, 0.4)
put(SFX, tok(280, 0.01, 1.0, 5700), 57.0, 0.5, pan=-0.3)
put(SFX, tok(280, 0.01, 1.0, 5701), 57.25, 0.5, pan=0.3)
stamp(57.75, 5750, 0.55, 0.6)
put(SFX, tok(180, 0.02, 1.2, 5800, 0.1), 58.0, 0.7)
put(HITS, sub_boom(0.4, 80, 40, 0.1), 58.0, 0.4)
put(SFX, tok(350, 0.004, 0.4, 5850, 0.03), 58.725, 0.12)
# tension 58.5 -> 59.0
put(SFX, rev_crash(0.38, 5900), 58.5, 0.7)
put(SFX, riser(0.38, 400, 8000, 5901), 58.5, 0.5)
# FINAL HIT
hit(59.0, 1.9, 5950, 0.9, crash_d=2.2)
kick_at(59.0, 1.6, 1.1, d=0.9)
put(SYN, braam(41, 1.0, seed=5951, peak=3200), 59.0, 0.85, rev=0.28)
put(SYN, pad(CH['Fm9'], 0.35, 1800, att=0.01, rel=0.3, seed=5952), 59.0, 0.6, rev=0.4)
put(SFX, crackle(0.8, 500, 5953, 1500, 9000) * 3, 59.0, 0.5)

# ---------------- ACID
acid = acid_render(10.0, 54.0)
ta = 10.0 + np.arange(len(acid)) / SR
ag = np.interp(ta, [10, 12, 39.9, 40.0, 44.9, 45.0, 49.9, 50.0, 53.6, 54.0], [0.55, 0.8, 0.85, 0.5, 0.5, 0.45, 0.9, 0.9, 0.9, 0.0])
acid = acid * ag
put(SYN, acid, 10.0, 0.75, rev=0.15, dly=0.35)

print('arrangement done %.1fs' % (time.time() - T0))

# ======================================================================== REWIND + CRT
pre = KICK + BASS
premix = np.vstack([pre, pre]) + DRUMS + SYN + SFX + HITS
seg = premix[:, int(1.0 * SR):int(3.0 * SR)][:, ::-1]
seg = lp(seg, 6000, 2)
d_rw = 0.88
t = tt(d_rw)
rate = np.where(t < 0.75, 1.6 + 2.0 * (t / 0.75), 3.6 * np.clip(1 - (t - 0.75) / 0.13, 0, 1) ** 1.5)
rate = rate * (1 + 0.04 * np.sin(TWO_PI * 7 * t))
rw = varispeed(seg, rate) * np.minimum(1, t / 0.01)
rw += np.vstack([hp(noise(d_rw, 3001 + ch), 3000) for ch in range(2)]) * 0.02
put(TOP, fade_tail(rw, 0.02), 3.0, 0.55)
put(TOP, tok(120, 0.03, 0.8, 3002, 0.12), 3.0, 0.8)
put(TOP, transient(3003, amt=0.5), 3.0, 0.35)
# CRT power-off
put(TOP, sub_boom(0.35, 70, 28, 0.08, 1.5), 3.75, 0.8)
put(TOP, np.vstack([tv_filter(noise(0.2, 3010 + ch), 7000 * np.exp(-tt(0.2) * 22) + 150, 'low') for ch in range(2)]) * np.exp(-tt(0.2) * 12) * 0.5, 3.75, 0.8)
put(TOP, crackle(0.15, 1200, 3011, 1500, 9000) * 2.5, 3.75, 0.5)
put(TOP, tok(500, 0.004, 0.5, 3012, 0.04), 3.888, 0.15)
# hook mute: everything except TOP collapses into the rewind / power-off
HG = np.ones(N)
a_, b_, c_, d_ = int(3.0 * SR), int(3.08 * SR), int(3.75 * SR), int(3.85 * SR)
HG[a_:b_] = np.linspace(1, 0.12, b_ - a_)
HG[b_:c_] = 0.12
HG[c_:d_] = np.linspace(0.12, 0.0, d_ - c_)
HG[d_:int(3.998 * SR)] = 0.0
HG[int(3.998 * SR):int(4.0 * SR)] = np.linspace(0, 1, int(4.0 * SR) - int(3.998 * SR))

# ======================================================================== MIX
print('rumble / sends %.1fs' % (time.time() - T0))
DIPK = np.clip(DIPK, 0, 1)
DIPH = np.clip(DIPH, 0, 1)
# rumble
r_ir = noise(1.1, 9001) * np.exp(-tt(1.1) / 0.28)
r_ir = lp(r_ir, 300, 2)
r_ir /= np.sqrt((r_ir ** 2).sum())
rum = oaconvolve(KICK, r_ir)[:N]
rum = lp(rum, 110, 4)
rum = sat(rum * 2.2, 2.0)
rum = hp(lp(rum, 95, 4), 28, 2)
rduck = np.zeros(N)
for tk, scv in KICK_T:
    duck(rduck, tk, 1.0 * scv, 0.16, att=0.002, hold=0.05)
rum *= (1 - np.clip(rduck, 0, 1)) ** 1.5
rum *= np.interp(np.arange(N) / SR, [0, 59.05, 59.35, 61], [1, 1, 0, 0])
rum *= np.sqrt(np.mean(KICK[int(10 * SR):int(40 * SR)] ** 2)) / (np.sqrt(np.mean(rum[int(10 * SR):int(40 * SR)] ** 2)) + 1e-9) * 0.2

bass_g = 1 - np.clip(0.9 * DIPK + 0.6 * DIPH, 0, 0.95)
syn_g = 1 - np.clip(0.55 * DIPK + 0.75 * DIPH, 0, 0.9)
drm_g = 1 - np.clip(0.15 * DIPK + 0.5 * DIPH, 0, 0.8)
sfx_g = 1 - np.clip(0.35 * DIPH, 0, 0.5)
low = KICK * (1 - 0.5 * np.clip(DIPH - 0.3, 0, 1)) + BASS * bass_g + rum
low = hp(low, 24, 2)
low = sat(low * 1.1, 1.2) / 1.1 * 10 ** (-3.0 / 20)
# parallel bass harmonics (-12 dB): the 16th line survives on phone / laptop speakers (still mono)
bass_h = sat(hp(BASS * bass_g, 150, 2), 3.0)
bass_h = lp(bass_h, 5000, 2) * 10 ** (-10 / 20)


def make_ir(d, t60, seed, bright=6500, dark=1400, pre=0.015):
    t = tt(d)
    out = []
    for ch in range(2):
        r = R(seed + ch)
        nz = r.standard_normal(len(t))
        a = np.exp(-t / (d * 0.25))
        y = (a * lp(nz, bright) + (1 - a) * lp(nz, dark)) * 10 ** (-3 * t / t60)
        y = hp(y, 150)
        sh = int((pre + 0.005 * ch) * SR)
        y = np.concatenate([np.zeros(sh), y])[:len(t)]
        for k in range(6):
            p_ = int(r.uniform(0.004, 0.04) * SR)
            y[p_] += r.uniform(-0.6, 0.6) * np.sqrt(np.mean(y[sh:sh + 2000] ** 2)) * 20
        out.append(y)
    ir = np.vstack(out)
    return ir / np.sqrt((ir ** 2).sum(1)).max()


hall = make_ir(3.4, 3.0, 9100)
room = make_ir(0.8, 0.6, 9200, bright=8000, dark=3000, pre=0.005)
REV_in = REV * (1 - 0.3 * DIPK)
rev_out = np.vstack([oaconvolve(REV_in[ch], hall[ch])[:N] for ch in range(2)])
room_out = np.vstack([oaconvolve(ROOM[ch], room[ch])[:N] for ch in range(2)])
HAAS = int(0.012 * SR)            # 12 ms Haas on the right room return (clap / stamp rooms widen)
room_out[1, HAAS:] = room_out[1, :-HAAS].copy()
room_out[1, :HAAS] = 0
# reverse-reverb sucks: the only thing heard in the pre-drop / pre-final-hit vacuum
VAC = np.zeros((2, N))
for t_end, sd_, g_ in ((49.995, 9300, 0.3), (58.995, 9310, 0.35)):
    src_ = np.vstack([transient(sd_ + ch, d=0.08, amt=1.2) for ch in range(2)]) + crash(0.3, sd_ + 4)[:, :int(0.08 * SR)] * 0.6
    wet = np.vstack([oaconvolve(src_[ch], hall[ch])[:int(0.6 * SR)] for ch in range(2)])
    wet = hp(wet, 300, 2)[:, ::-1]
    wet = wet / (np.abs(wet).max() + 1e-9)
    wet = fade_head(wet, 0.05)
    wet[:, -int(0.002 * SR):] *= np.linspace(1, 0, int(0.002 * SR))
    put(VAC, wet, t_end - wet.shape[1] / SR, g_)

# ping-pong delay 3/16
D = int(0.1875 * SR)
dsum = DLY.mean(0)
dly_out = np.zeros((2, N))
tap = dsum
for k in range(1, 7):
    tap = lp(tap, 3800, 1) * 0.5
    tap = hp(tap, 250, 1)
    ch = (k + 1) % 2
    dly_out[ch, k * D:] += tap[:N - k * D]
dly_out *= (1 - 0.4 * DIPK)

if os.environ.get('STEMS'):
    np.savez(os.path.join(os.environ['STEMS'], 'stems.npz'), low=low[:NOUT].astype(np.float32), drums=(DRUMS*drm_g)[:, :NOUT].astype(np.float32), syn=(SYN*syn_g)[:, :NOUT].astype(np.float32), sfx=(SFX*sfx_g)[:, :NOUT].astype(np.float32), hits=HITS[:, :NOUT].astype(np.float32), rev=rev_out[:, :NOUT].astype(np.float32))
mix = np.vstack([low, low])
mix += DRUMS * drm_g * 10 ** (3 / 20)
mix += np.vstack([bass_h, bass_h])
mix += SYN * syn_g
mix += SFX * sfx_g
mix += HITS
mix += rev_out * 0.8 * (1 - 0.4 * DIPK)
mix += room_out * 0.5
mix += dly_out * 0.6
SG = np.interp(np.arange(N) / SR,
               [0, 9.99, 10.0, 19.99, 20.0, 29.99, 30.0, 39.99, 40.0, 44.99, 45.0, 49.99, 50.0, 53.99, 54.0, 58.99, 59.0, 61],
               [1.0, 1.0, 0.80, 0.80, 0.84, 0.84, 0.88, 0.88, 0.62, 0.62, 0.84, 0.98, 1.15, 1.15, 0.95, 0.95, 1.3, 1.3])
# vacuum: the whole music + SFX bed drops to -18 dB just before the two biggest hits
VG = np.ones(N)
for a0, a1 in ((49.88, 49.993), (58.88, 58.993)):
    i0, i1, r_ = int(a0 * SR), int(a1 * SR), int(0.008 * SR)
    VG[i0:i0 + r_] = np.linspace(1, 10 ** (-18 / 20), r_)
    VG[i0 + r_:i1] = 10 ** (-18 / 20)
    VG[i1:i1 + int(0.004 * SR)] = np.linspace(10 ** (-18 / 20), 1, int(0.004 * SR))
mix *= HG * SG * VG
tt_all = np.arange(N) / SR
DRYREL = np.where(tt_all > 59.12, np.exp(-np.clip(tt_all - 59.12, 0, None) / 0.16), 1.0)
mix -= (rev_out * 0.8 * (1 - 0.4 * DIPK)) * HG * SG * VG     # take the hall return out ...
mix *= DRYREL                                               # ... release the dry buses ...
mix += (rev_out * 0.8 * (1 - 0.4 * DIPK)) * HG * SG * VG     # ... and put the hall back untouched
mix += VAC
mix += TOP
mix = hp(mix, 20, 2)

print('master %.1fs' % (time.time() - T0))
mix = mix[:, :NOUT].astype(np.float32)
from pedalboard import LowShelfFilter, PeakFilter, HighShelfFilter
mix = Pedalboard([LowShelfFilter(cutoff_frequency_hz=80, gain_db=-3.0), PeakFilter(cutoff_frequency_hz=3200, gain_db=4.5, q=0.5), HighShelfFilter(cutoff_frequency_hz=8000, gain_db=1.5)])(mix, SR)
glue = Pedalboard([Compressor(threshold_db=-14, ratio=2.0, attack_ms=12, release_ms=140)])
mix = glue(mix, SR)
par = Pedalboard([Compressor(threshold_db=-28, ratio=6.0, attack_ms=1.0, release_ms=70)])(mix, SR)
mix = (mix + 0.3 * par).astype(np.float64)


def limiter(x, ceil_db=-2.4, win=0.006):  # -2 dBTP leaves room for MP3 encoding overshoot
    c = 10 ** (ceil_db / 20)
    up = resample_poly(x, 4, 1, axis=1)
    pk = np.abs(up).max(0)
    pk = pk[:x.shape[1] * 4].reshape(-1, 4).max(1)
    g = np.minimum(1.0, c / np.maximum(pk, 1e-9))
    W = int(win * SR)
    g = minimum_filter1d(g, 2 * W + 1)
    g = uniform_filter1d(g, W + 1)
    return x * g


def soft_clip(x, thr=0.7):
    a = np.abs(x)
    over = a > thr
    y = x.copy()
    y[over] = np.sign(x[over]) * (thr + (1 - thr) * np.tanh((a[over] - thr) / (1 - thr)))
    return y


meter = pyln.Meter(SR)
target = -14.0
gain = 1.0
for it in range(4):
    y = soft_clip(mix * gain, 0.75)
    y = limiter(y)
    l = meter.integrated_loudness(y.T)
    gain *= 10 ** ((target - l) / 20)
    if abs(l - target) < 0.1:
        break
fade = int(0.3 * SR)
y[:, -fade:] *= np.linspace(1, 0, fade) ** 1.5
for _ in range(3):
    tp = max(np.abs(resample_poly(c, 4, 1)).max() for c in y)
    if 20 * np.log10(tp) <= -2.3:
        break
    y *= 10 ** (-2.35 / 20) / tp
y -= y.mean(1, keepdims=True)
y = np.clip(y, -1, 1)
out = os.path.join(HERE, 'mix.wav')
sf.write(out, y.T.astype(np.float32), SR, subtype='PCM_16')
print('LUFS %.2f  TP %.2f dBTP  samples %d  render %.1fs' % (meter.integrated_loudness(y.T), 20 * np.log10(max(np.abs(resample_poly(c, 4, 1)).max() for c in y)), y.shape[1], time.time() - T0))

# delivery copy: 320 kbps MP3 of the same master (the client lays it under the existing video)
import subprocess
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', out, '-c:a', 'libmp3lame', '-b:a', '320k', os.path.join(HERE, 'mix.mp3')], check=False)
