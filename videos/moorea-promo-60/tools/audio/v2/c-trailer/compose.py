#!/usr/bin/env python3
"""Moorea promo 60 s -- direction C "trailer hybrid" (AAA game / blockbuster trailer x festival electro).

CONCEPT
  "GAME OVER : rejoue le Moorea" scored like a AAA game launch trailer. The hook is a cinematic cold open
  (lava rumble, sub drops, two distorted braams on GAME / OVER, a tape rewind and a CRT power-off). The level
  intro is pure trailer: taiko-like low drums, a tense spiccato string-synth ostinato, a ticking-clock pulse
  and an overheat riser. The six power-ups ride a hybrid trailer groove (kick + huge toms + backbeat snare,
  a modern gated 16th electronic pulse, a staccato low synth ostinato in F minor). The breakdown is the only
  breath: heartbeat, choir-like pad, sparse low felt-piano notes. The build tightens (snare roll 8th->16th->32nd,
  rising ostinato, riser) into a dead-silent 60 ms suck, then the drop at 50.0 turns into a heavy
  four-on-the-floor techno / electro drop with braam stabs and a rolling reese bass. The end card resolves
  modally (Fsus2-Fm / Db(add9) / Ebsus4-Eb / Fm), never a major jingle, and ends on a massive final hit at 59.0
  that rings out in a hall (the hit layers are never ducked; the tail decays through braam/impact envelopes and
  the FX hall: about -11 dB by 59.7).

REVISION 3 (music-supervisor critique round 2: "the big moments do not slam")
  - Hit buses: every braam is on 'hits' (LP 1.5 kHz 4th order, hall send to the undamped v_hall) and the hit taikos,
    the stamp snare and the 59.0 drop kick are on 'hitd' (own parallel comp + tanh). Neither is multiplied by the kick
    side-chain, the big-hit duck or the section gain. The duck (dh) now only acts on the bed (music / bass / drums),
    and the music-hall return gets half its depth. Duck events take an optional hold (stop-time under the taglines).
  - Bed-only pre-sucks (BPD): 20 ms x0.5 before every stamp, 53.0 / 53.5, 40 ms x0.4 before 50.875, and 12 ms x0.5
    before the 11 / 16 / 36 quench lands (replacing the 26 ms whole-mix dropouts). The fall whooshes end 15 ms before
    the land so the quench stays a clean onset. The drop's two whole-mix dips at 50.05 / 50.09 are gone.
  - Master: stereo-linked, 2x-oversampled soft-knee clipper ahead of the look-ahead limiter (the limiter used to pull
    2-3 dB off the drop, the taglines and the final hit); glue compressor attack 30 ms / ratio 1.6 so hit onsets pass;
    side 4th-order HP at 130 Hz moved after the glue.
  - Final hit: braam 1.25 (edec 0.6, v_hall 0.6, lighter sub), impact size 1.2 / 2.0 s / subdec 0.4, crash 0.85 +
    crack, taikos 0.7, sub drop 0.35; pickup roll 0.08-0.26, reverse swell 0.45, 58.5 choir 0.45.
  - Build vs drop: risers 0.3 / 0.22, 49.5 taiko 0.7, reverse swell 0.55, section gain build 1.05 -> 1.0, drop 1.22
    (bed), drop pad 0.42 / 0.52, drop choir 0.18. Taglines: braams 0.8 s, impacts 1.35 + crash, bed out for 180 ms,
    ride / air -4 dB for 120 ms. 50.875: braam 1.0 s + crash + impact 1.3.
  - Hook / level: rewind 0.6, CRT zap 0.55, CRT hum is a sine thump (no saw glide), 4.0 braam + impact bigger; 6.0 cut
    has no kick (crash 0.2), 6.15 slam bigger + crash; 5.5 riser glides a 5th; dive lighter.
  - Stamps: braam 0.78, impact 1.15, short dark crash, bed duck 0.75 with 100 ms hold; quench lands 0.75-0.8.
  - Register / mud: power-up ostinato up an octave (F2-Ab3, gain 0.5); drums bus -2.5 dB at 250 Hz; room sends HP 80 Hz.
  - Choir: formants are time-varying band-passes, F1 / F2 morph +-8 % per bar (ah <-> oh), F3 drifts; 0.2 in 20-30 s,
    slow-attack pad role from 30 s.
  - Festival DNA: quiet four-on-the-floor kick under the backbeat from 30 to 40 s.
  - UI: swishes 40.5 0.3 / 18.5 0.5 / 54.0 0.5 / 55.25 0.7 / 55.5 0.6, toks 48.5 0.9 / 51.7625 1.2 / typing 1.0 /
    breakdown taps 0.65; doubled toks at 21-22.25, 27-28, 41.01-41.23 removed; the goal-photo and pin-pop cues get a
    short broadband crack (SFX) instead of louder UI. Every UI event is >= 6.9 dB under the bed (median -16 dB).

REVISION 2 (music-supervisor critique)
  - Drop rebuilt for small speakers: section gain build 1.15-1.25 / drop 1.45; drop sub sine 0.45, 50.0 sub drop 0.45,
    drop kick shorter (adec 0.18), low-passed body + separate click + 160 Hz knock; reese gets a driven mono mid layer
    (BP 200-1.8k -> tanh 3x -> LP 1.4k); drop pad LP 4.5 kHz, gain 0.5-0.66; clap/snare +3 dB at 2-5 kHz; 16th ride
    layer; gated wide noise air bed. Measured after a 180 Hz HP: drop is 2.6 / 2.7 dB louder than the end of the build.
  - Final hit rings out: choir with exponential decay (0.35 s), braam env 0.4 s, short final sub, duck held to 60.0.
  - Game-show residue removed: the 'denied' stutter is now made of the OVER braam tail (8 kHz crush, LP 1.2 kHz, in
    key); the 36.5 saw 'vwoop' is a 300->1200 Hz band-passed noise charge; the 9.0 overheat is a C7b9 repeated-note
    tremolo (C+G low, Db/E on top, opening filter) instead of a C major arpeggio.
  - Drop hops: one thump at 51.7625 + the 52.8125 impact; the other hops are quiet rim/tok accents, no steam.
    HUD counter clack gain 2.8 -> 1.6 (brighter, shorter click so it still marks the cue).
  - Power-up layers follow the picture (per power-up / 10 s phases at 10/20/30), two alternating ostinato
    patterns, rotating stamp-braam voicings, a tom fill into every whip-pan cut, a crack transient on every eruption.
  - Low end: sub roots folded into 34-68 Hz, taikos / eruptions high-passed at 40 Hz, power-up kick hold 10 ms,
    lighter power-up sub; bass bus low-passed at 2.2 kHz (no harmonic 'beeps').
  - Section-gain and width steps are 25 ms ramps ending on the downbeat; side gain 1.0 in the hook and end card.
  - Choir: 8 voices per note with random onsets and slow vibrato, LP'd source, 3 narrow formants (Q 6) + ensemble chorus.
  Key: F minor with phrygian colour (Gb). 120 BPM, beat 0.5 s, bar 2 s; everything sits on film time.

PALETTE (all synthesized, deterministic seeds, no samples)
  Music
  - kick: sine with exponential pitch drop (230 -> 46 Hz), held body, 1-6 kHz noise click, tanh drive. Drop kick:
    longer, tuned to F1, harder drive.
  - snare: two damped body modes (185 / 330 Hz) + band-passed noise wires + crack, saturated; layered clap;
    plate reverb send.
  - hats / shaker: high-passed noise, short; panned, never tonal.
  - taiko / toms: sine with pitch envelope + two inharmonic membrane modes + skin noise, saturated, room+hall.
  - braam: 3 detuned polyBLEP saws per note on low power chords (F1..F3), pitch bends up into the note,
    time-varying 2-stage resonant low-pass (opens in ~120 ms, closes over 1 s), 30 Hz growl, tanh, + sine sub.
  - spiccato strings: per-note detuned saw stack, 3 ms attack, short decay, note-wise low-pass, bow noise.
  - low synth ostinato: saw pair + sine sub, per-note filter envelope (300 Hz -> 1.4 kHz -> 400 Hz), mono, ducked.
  - electronic pulse: wide detuned saw chord, gated on 16ths (trance-gate), low-passed, automated per section.
  - sub bass: sine on the chord roots (40-80 Hz), mono, side-chained to the kick.
  - reese bass (drop): two detuned saws + sine sub, rolling 16ths, low-passed + driven, + driven mid layer, mono.
  - choir pad: 8-voice-per-note saw ensemble (random onsets, slow vibrato), LP 2.5 kHz, 3 narrow "ah" formants
    (750 / 1180 / 2650 Hz, Q 6) + chest body + breath, ensemble chorus, wide.
  - string pad: detuned saw stack, low-passed 1.5-3 kHz, slow attack, wide.
  - felt piano: additive inharmonic partials (B = 3.5e-4), double-string beating, hammer noise, low register only.
  - heartbeat: two low pitch-dropping sine thumps + muffled noise.
  - ticking clock: 5 ms band-passed noise tick + 800 Hz damped body (short, quiet).
  SFX (trailer grade, they live inside the music)
  - impact: sine sub drop + saturated noise crack + low thud + metallic modal body (inharmonic partials < 1.5 kHz)
    + grit; hall tail. stamp: tighter impact + snare crack + short braam stab on the current chord.
  - whoosh / whip-pan: stereo noise through a swept band-pass, power-curve swell that peaks AT the cut,
    pan sweep, low air layer, a small onset transient where the motion starts.
  - reverse swell: reversed noise-cymbal + reversed hall into a cut. Riser: swept noise + gliding low saw cluster
    + accelerating tremolo. Sub drop: sine 110 -> 30 Hz.
  - lava: low rumble bed + sparse crackle (filtered impulse trains); eruption = taiko + distorted fire burst +
    low whoomp + crackle; quench = heavy thud + splash noise + steam hiss + crackle; cooling "sheen" = crackle
    burst + soft hiss (no bell).
  - tape rewind: the actual hook mix read backwards with accelerating speed (pitch rises), tape-filtered,
    with a transport clunk; CRT power-off: noise sweep down + sub thunk + static; CRT power-on: thump + static
    burst + rising low hum.
  - UI (quiet, tactile, never melodic): "tok" = 2.5 ms band-passed noise click + 150-450 Hz damped body + tiny
    110 Hz haptic bump; "clack" (HUD counter) = two toks 14 ms apart; small swish for reveals/slides.
  Mix: buses drums / bass / music / sfx / ui + undamped hit buses hits / hitd; four synthetic convolution reverbs (decorrelated stereo noise IRs:
  music hall 2.8 s, FX hall 3.4 s, plate 1.3 s, room 0.6 s); side-chain pump on music + bass from every kick
  and deeper ducks under every big hit; parallel-compressed drums; section filter automation on the music bus;
  glue compression, low end mono (side 4th-order high-pass at 130 Hz), linked oversampled soft clipper, two-stage
  look-ahead limiter, true-peak and LUFS loop to -14 LUFS / <= -1.0 dBTP.

ARRANGEMENT
  0-4   HOOK: lava bed, ring pulses (sub whums), swallow (sub drop + thud + sizzle), suck-ins, GAME braam (Fm) /
        OVER braam (Gb over F, phrygian; ~1 dB bigger than GAME), dark string cluster, ostinato + ticking clock enter
        at 2.0, "denied" stutter of the OVER braam tail at 2.5, tape rewind 3.0-3.75 built from the real hook audio, CRT power-off 3.75, silence.
  4-6   REJOUER: CRT on slam + short dark braam, low 8th pulse + clock, PRESS = big stamp + bright braam, 16th pulse,
        dive 5.5-6.0 (whoosh + riser + reverse swell + snare roll).
  6-10  NIVEAU 1: kick + taiko groove, spiccato 16ths, clock 16ths; NIVEAU slam 6.15; eight eruptions on 8ths;
        overheat 9.0 (riser + 16th snare/tom roll + C7b9 repeated-note tremolo), white-out reverse swell, 40 ms suck.
  10-40 POWER-UPS: hybrid groove that grows on the picture cuts: 10 kick/snare/8th hats/taiko/ostinato A;
        15 + 16th hats, spiccato, ostinato B; 20 + toms, taiko on 3, pickup kick, shaker, open hats, choir;
        30 + string pad, brighter pulse, choir as pad, quiet four-on-the-floor kick. Tom fill into every whip (P+4.5). Chords Fm Fm Db Eb | Fm Gb Db C ...
  40-45 BREAKDOWN: no kick; heartbeat, choir pad Fm -> Db -> Eb, low felt piano, soft lava.
  45-50 BUILD: Db -> Eb -> C, kicks on beats, snare roll 8ths->16ths->32nds, ostinato rising, riser into 49.94 (kept
        about 3 LU under the drop),
        then 60 ms of silence.
  50-54 DROP: four-on-the-floor drop kick, bright clap/snare backbeat, offbeat open hats + 16th ride, rolling reese
        with driven mids, wide gated pulse (LP 4.5 kHz), gated noise air, braam stabs on 50.0 / 50.875 / 52.0 / 53.0 / 53.5, impacts on every slam.
  54-60 END: Fsus2->Fm swell (choir + strings + taiko), Db(add9), Ebsus4->Eb, final Fm hit at 59.0, hall ring-out.

CUE -> SOUND (every weight-3 and weight-2 cue)
  0.000 w2 first ring pulse ............ sub "whum" + soft low swish + lava bed start
  0.500 w2 PLOP swallow .................. sub drop 120->30 + muffled thud + crackle; sizzle hiss 0.55
  0.775 w2 / 1.275 w2 pre-slam suck ...... reverse suck-in whoosh with onset, swelling into the slam
  1.000 w3 GAME / 1.500 w3 OVER .......... impact + braam (Fm / Gb-over-F) + taiko + dark crash; music ducks
  2.000 w2 card flips in ................. short flip swish + low tom; ostinato + clock start
  2.250 w2 subline words ................. soft tok + ostinato 16th
  2.500 w2 card DEAD ..................... "denied": stutters of the OVER braam tail (2.543/2.584/2.625/2.75), crushed + thud
  3.000 w2 REWIND ........................ transport clunk + reversed accelerating hook audio (to 3.75)
  3.750 w2 CRT power-off ................. noise sweep down + sub thunk + static
  4.000 w3 CRT on / REJOUER .............. thump + static burst + impact + short dark braam + taiko
  4.500 w2 subline + JOUER button ........ low tom + swish + tok
  5.000 w3 PRESS ......................... stamp + bright braam + crash + taiko
  5.500 w2 dive / 5.750 w2 orange flash .. whoosh into 6.0 (onset 5.5), riser, snare roll, low tom at 5.75
  6.000 w2 hard cut ...................... kick + cut swish + crash-lite
  6.150 w3 NIVEAU 1 slam ................. impact + braam Fm + taiko
  6.375 w2 logo lands .................... taiko + metallic tok
  7.000..8.750 w2 eruptions 1-8 .......... eruption (taiko + fire burst + crackle), panned to each word
  7.225 w2 / 7.250 w2 logo under + erupt 2  one merged splash-eruption at 7.2375 (+-12.5 ms to both)
  9.000 w2 overheat / 9.500 w2 white-out . riser + 16th snare/tom roll + C7b9 tremolo / second pulse hit + reverse swell
  P = 10,15,20,25,30,35 (power-ups):
    P     w3 erupt ....................... eruption + crack transient + kick (whip-pan whoosh + tom fill peak into it)
    P+0.5 w2 card falls .................. sizzling fall whoosh (20.5: rock grind rise; 25.5: rise swish)
    P+1.0 w3 land + quench ............... heavy thud + splash + steam + crackle (21.0: settle thud; 31.0: card slam)
    P+1.14 w2 cooling sheen .............. crackle burst + soft hiss (11.14, 16.14, 36.12)
    P+1.5 w3 answer stamp ................ stamp + braam stab on the current chord; music ducks
    P+2.12 w2 HUD counter ................ counter clack
    showcase w2 (rows, pins, ticks, tiles, chips, steps) ... toks / small swishes, drums on the beats
    17.063 zoom / 17.5, 18.0 pans / 18.5 zoom-out ............ small swishes (onset on the cue)
    25.25 w3 HALO x MAINSTAGE collide .... metallic impact + crash; 28.5 w3 VALIDER .. stamp-lite
    31.0-31.75 w2 food-truck slams ....... slam thuds on 8ths; 32.0-33.5 carousel .. swishes + toks
    P+3.5 w2 hop / P+4.0 w2 land ......... soft air swish / soft haptic thump; P+4.5 w2 whip-pan whoosh into P+5
  40.000 w2 erupt (breakdown) ............ soft eruption + heartbeat + piano
  40.5 w2 fall / 41.0 w2 soft land + toggle ... soft fall whoosh / thud + tok
  41.500 w3 RETROUVE TA BANDE ............ stamp (with deep hall) + compass lock tok
  42.0 / 42.12 / 42.5 / 42.75 / 43.0 / 43.5 w2 ... tap tok / clack / avatar toks / SOS tok + low thump / chat tok
  44.500 w2 whip-pan ..................... whoosh into 45.0
  45.000 w3 1000 QUESTIONS ............... impact + braam Db + crash; build starts
  45.5 w2 input bar / 45.75 w2 typing .... swish / quiet key-click texture
  46.500 w3 M.A.N.A REPOND (+ w2 send) ... stamp + send suck whoosh
  47.0 / 47.12 / 47.5-48.25 / 48.5 w2 .... bubble tok / clack / chip toks / tap tok
  49.000 w2 riser / 49.500 w2 white-out .. riser stage 2 + 32nd snare roll / reverse swell to 49.94, silence
  50.000 w3 DROP ......................... drop kick + sub boom + impact + crash + braam Fm
  50.075 w2 ember explosion .............. fire burst + crackle
  50.125 w3 NIVEAU TERMINE slam .......... impact (metal + crack + sub)
  50.500 w2 slot reel .................... decelerating mechanical ticks on the real digit flips
  50.875 w3 8/8 lands .................... impact + braam stab
  51.500 w2 pull-back .................... big whoosh down
  51.75 w2 goal photo + 51.775 w2 hop 1 .. merged landing thump at 51.7625
  51.925..52.675 w2 hop landings ......... quiet rim / tok accents (no steam)
  52.813 w2 dot lands in goal ............ medium impact + crack + crackle, small duck
  53.000 w3 / 53.500 w3 taglines ......... impact + braam (Eb / C)
  54.000 w2 sunrise ...................... taiko + low piano + soft crash + Fsus2 swell
  55.25 w2 tab bar / 55.5 w2 logo fall ... whoosh up / spinning fall whoosh into 56.0
  56.000 w3 snap + title slam ............ impact + braam Db + crash
  56.5 / 57.0 / 57.25 w2 ................. swish + toks
  57.750 w2 PRET A JOUER ................. stamp-lite
  58.000 w2 download button .............. medium hit + Ebsus4 chord
  59.000 w3 FINAL HIT .................... braam Fm (biggest) + impact + sub drop + taiko ensemble + crash +
                                           drop kick + crack; nothing on the hit buses is ducked; everything decays
                                           (choir 0.35 s, braam 0.6 s) into the FX hall, bed duck held to 60.0,
                                           fade only the last 0.3 s
"""
import json
import os
import time

import numpy as np
import pyloudnorm as pyln
import soundfile as sf
from pedalboard import Chorus, Compressor, PeakFilter
from scipy.ndimage import maximum_filter1d, uniform_filter1d
from scipy.signal import butter, lfilter, oaconvolve, resample_poly, sosfilt

T_START = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
SR = 48000
NOUT = 60 * SR
N = NOUT + 2 * SR


# ===================================================================================== basics
def R(seed):
    return np.random.default_rng(seed)


def ns(d):
    return int(round(d * SR))


def tax(n):
    return np.arange(n) / SR


def mtof(m):
    return 440.0 * 2 ** ((np.asarray(m, float) - 69) / 12)


def noise(n, seed):
    return R(seed).standard_normal(n)


def lp(x, f, o=2):
    return sosfilt(butter(o, f, 'lowpass', fs=SR, output='sos'), x, axis=-1)


def hp(x, f, o=2):
    return sosfilt(butter(o, f, 'highpass', fs=SR, output='sos'), x, axis=-1)


def bp(x, lo, hi, o=2):
    return sosfilt(butter(o, [lo, hi], 'bandpass', fs=SR, output='sos'), x, axis=-1)


def ar(n, a=0.002, dec=0.2, hold=0.0):
    """attack (sine-shaped) / hold / exponential decay with time constant dec."""
    t = tax(n)
    e = np.exp(-np.maximum(t - a - hold, 0) / dec)
    if a > 0:
        e = e * np.sin(0.5 * np.pi * np.clip(t / a, 0, 1))
    return e


def fin(x, ms=6.0):
    """short fade at the end so nothing ends on a step."""
    x = np.array(x, dtype=np.float64)
    k = min(x.shape[-1], max(2, ns(ms / 1000)))
    x[..., -k:] *= np.linspace(1, 0, k)
    return x


def stereo(x, pan=0.0):
    if x.ndim == 2:
        return x
    l = np.cos((pan + 1) * np.pi / 4) * np.sqrt(2)
    r = np.sin((pan + 1) * np.pi / 4) * np.sqrt(2)
    return np.vstack([x * l, x * r])


# ------------------------------------------------------------------- oscillators
def _blep(p, dt):
    out = np.zeros_like(p)
    m = p < dt
    x = p[m] / dt[m]
    out[m] = x + x - x * x - 1
    m2 = p > 1 - dt
    x2 = (p[m2] - 1) / dt[m2]
    out[m2] = x2 * x2 + x2 + x2 + 1
    return out


def _ph(f, n, ph0):
    f = np.full(n, float(f)) if np.ndim(f) == 0 else np.asarray(f, float)[:n]
    return f, ph0 + np.cumsum(f) / SR


def sine(f, n, ph0=0.0):
    _, ph = _ph(f, n, ph0)
    return np.sin(2 * np.pi * ph)


def saw(f, n, ph0=0.0):
    f, ph = _ph(f, n, ph0)
    p = ph % 1.0
    dt = np.clip(f / SR, 1e-7, 0.5)
    return 2 * p - 1 - _blep(p, dt)


def sawstack(midis, n, voices=5, spread=0.22, seed=0, drift=0.0015, vib=0.0, bend=None):
    """Detuned saw stack, independent detune/phase per channel -> genuinely wide."""
    rng = R(seed)
    t = tax(n)
    out = np.zeros((2, n))
    midis = list(np.atleast_1d(midis))
    for m in midis:
        f0 = float(mtof(m))
        for ch in range(2):
            for v in range(voices):
                c = ((v / (voices - 1) - 0.5) * spread) if voices > 1 else 0.0
                c += rng.normal(0, 0.02) + (0.015 if ch else -0.015) * (1 if v % 2 else -1)
                f = f0 * 2 ** (c / 12) * (1 + drift * np.sin(2 * np.pi * rng.uniform(0.1, 0.4) * t + rng.uniform(0, 6.28)))
                if vib:
                    f = f * (1 + vib * np.sin(2 * np.pi * rng.uniform(4.6, 5.6) * t + rng.uniform(0, 6.28)) * np.clip(t / 0.5, 0, 1))
                if bend is not None:
                    f = f * 2 ** (bend / 12)
                out[ch] += saw(f, n, rng.random())
    return out / np.sqrt(len(midis) * voices)


# ------------------------------------------------------------------- time-varying biquad (block-wise)
def tvf(x, fc, q=0.707, kind='low', blk=64):
    x = np.asarray(x, float)
    if x.ndim == 2:
        return np.vstack([tvf(c, fc, q, kind, blk) for c in x])
    n = len(x)
    nb = (n + blk - 1) // blk
    fc = np.broadcast_to(np.asarray(fc, float), (n,)) if np.ndim(fc) else np.full(n, float(fc))
    fcb = np.clip(fc[::blk][:nb], 18, SR * 0.45)
    qb = np.full(nb, float(q))
    w = 2 * np.pi * fcb / SR
    cw, al = np.cos(w), np.sin(w) / (2 * qb)
    if kind == 'low':
        b0 = (1 - cw) / 2; b1 = 1 - cw; b2 = b0
    elif kind == 'high':
        b0 = (1 + cw) / 2; b1 = -(1 + cw); b2 = b0
    else:  # band, 0 dB peak
        b0 = al; b1 = 0 * al; b2 = -al
    a0 = 1 + al; a1 = -2 * cw; a2 = 1 - al
    B = np.stack([b0, b1, b2], 1) / a0[:, None]
    A = np.stack([np.ones(nb), a1 / a0, a2 / a0], 1)
    y = np.empty(n)
    z = np.zeros(2)
    for i in range(nb):
        s = i * blk
        e = min(n, s + blk)
        y[s:e], z = lfilter(B[i], A[i], x[s:e], zi=z)
    return y


# ===================================================================================== buses
BUS = {k: np.zeros((2, N)) for k in ['drums', 'bass', 'music', 'sfx', 'ui', 'post', 'hits', 'hitd',
                                      'v_mhall', 'v_hall', 'v_plate', 'v_room']}
# 'hits' (braams) and 'hitd' (hit taikos / hit kick / stamp snare) are the big-moment layers: they are NOT
# multiplied by the kick side-chain, the big-hit duck or the section gain (the duck exists to make room for them).
DK = []   # kick side-chain events (t, depth, release)
DH = []   # big-hit duck events
PD = []   # pre-hit micro-sucks on the whole pre-mix (start, end, gain)
BPD = []  # pre-hit micro-sucks on the bed only (music / bass / drums; not sfx, ui or hits)


def place(bus, sig, at, g=1.0, pan=0.0, hall=0.0, plate=0.0, room=0.0, mhall=0.0):
    if bus in ('hits', 'hitd') and mhall:     # hit layers send to the undamped FX hall, never the ducked music hall
        hall, mhall = hall + mhall * 1.4, 0.0
    s = stereo(np.asarray(sig, float), pan) * g
    i = int(round(at * SR))
    j0 = max(0, -i)
    n = min(s.shape[1], N - i)
    if n <= j0:
        return
    BUS[bus][:, i + j0:i + n] += s[:, j0:n]
    for name, amt in (('v_hall', hall), ('v_plate', plate), ('v_room', room), ('v_mhall', mhall)):
        if amt:
            BUS[name][:, i + j0:i + n] += s[:, j0:n] * amt


CUES = json.load(open(os.path.join(HERE, 'cues.json')))
CUES = CUES['cues'] if isinstance(CUES, dict) else CUES
CUE_T2 = np.array([float(c['t']) for c in CUES if c['weight'] >= 2])


def clear(t, lo=0.008, hi=0.046):
    """True if a rhythmic hit at t will not steal the onset window of a nearby weight>=2 cue."""
    d = np.abs(CUE_T2 - t)
    return not np.any((d > lo) & (d < hi))


# ===================================================================================== harmony
CH = {
    'Fm': [41, 48, 53, 56, 60], 'Fsus2': [41, 48, 53, 55, 60], 'Db': [37, 44, 49, 53, 56],
    'Dbadd9': [37, 44, 49, 51, 53, 56], 'Eb': [39, 46, 51, 55, 58], 'Ebsus4': [39, 46, 51, 56, 58],
    'Gb': [42, 49, 54, 58, 61], 'C': [36, 43, 48, 52, 55], 'Bbm': [34, 41, 46, 49, 53],
}
ROOT = {'Fm': 29, 'Fsus2': 29, 'Db': 37, 'Dbadd9': 37, 'Eb': 39, 'Ebsus4': 39, 'Gb': 30, 'C': 36, 'Bbm': 34}
TIMELINE = [(0, 4, 'Fm'), (4, 6, 'Fm'), (6, 8, 'Fm'), (8, 9, 'Db'), (9, 10, 'C'),
            (10, 12, 'Fm'), (12, 14, 'Fm'), (14, 16, 'Db'), (16, 18, 'Eb'),
            (18, 20, 'Fm'), (20, 22, 'Gb'), (22, 24, 'Db'), (24, 26, 'C'),
            (26, 28, 'Fm'), (28, 30, 'Fm'), (30, 32, 'Db'), (32, 34, 'Eb'),
            (34, 36, 'Fm'), (36, 38, 'Gb'), (38, 40, 'C'),
            (40, 42, 'Fm'), (42, 44, 'Db'), (44, 45, 'Eb'),
            (45, 47, 'Db'), (47, 49, 'Eb'), (49, 50, 'C'),
            (50, 52, 'Fm'), (52, 53, 'Db'), (53, 54, 'Eb'),
            (54, 55, 'Fsus2'), (55, 56, 'Fm'), (56, 58, 'Dbadd9'), (58, 58.5, 'Ebsus4'), (58.5, 59, 'Eb'),
            (59, 62, 'Fm')]


def subf(m):
    """sub frequency for a root: folded into one octave [34, 68) Hz so the sub register stays put
    (F 43.6, Gb 46.2, Db 34.6, Eb 38.9, C 65.4)."""
    f = float(mtof(m))
    while f >= 68:
        f /= 2
    while f < 34:
        f *= 2
    return f


def chord_at(t):
    for a, b, c in TIMELINE:
        if a <= t + 1e-6 < b:
            return c
    return 'Fm'


# ===================================================================================== instruments
def kick(seed=0, d=0.42, f_end=46.0, f_top=230.0, pdec=0.028, adec=0.16, drive=2.2, click=0.35, hold=0.025):
    n = ns(d); t = tax(n)
    f = f_end + (f_top - f_end) * np.exp(-t / pdec)
    body = sine(f, n) * ar(n, 0.0012, adec, hold=hold)
    cl = bp(noise(n, seed), 1200, 6500) * ar(n, 0.001, 0.004) * click
    y = np.tanh(drive * (body + cl)) / np.tanh(drive)
    return fin(y)


def drop_kick(seed=0):
    """tuned to F1, shorter sub tail than before, plus a driven 150-500 Hz knock so it reads on small speakers."""
    k = kick(seed, d=0.6, f_end=43.65, f_top=260, pdec=0.03, adec=0.18, drive=3.6, click=0.0)
    k = lp(k, 1200, 4)        # the driven F1 body keeps its weight but no harmonic comb above 1.2 kHz
    n = len(k); t = tax(n)
    k += bp(noise(n, seed + 51), 1200, 6500) * ar(n, 0.001, 0.004) * 0.6
    knock = sine(160 * (1 + 0.5 * np.exp(-t / 0.006)), n) * ar(n, 0.0008, 0.022)
    knock += bp(noise(n, seed + 50), 300, 2500) * ar(n, 0.0005, 0.008) * 0.5
    return fin(k + np.tanh(2.0 * knock) * 0.45)


def snare(seed=0, d=0.38, tone=185.0, bright=1.0, pres=0.0):
    n = ns(d); t = tax(n); nz = noise(n, seed)
    body = (sine(tone * (1 + 0.3 * np.exp(-t / 0.012)), n) * 0.7 + sine(tone * 1.78, n) * 0.3) * ar(n, 0.001, 0.05)
    wires = bp(nz, 1800, 9500) * ar(n, 0.001, 0.10) * bright
    crack = bp(nz, 600, 3500) * ar(n, 0.001, 0.013) * 1.3
    y = np.tanh(1.8 * (body * 0.8 + wires * 0.75 + crack)) / np.tanh(1.8)
    if pres:
        y = y + bp(y, 2000, 5000) * pres      # 2-5 kHz presence lift (pres 0.41 ~ +3 dB)
    return fin(y)


def clap(seed=0, pres=0.0):
    n = ns(0.3); y = np.zeros(n)
    for k, off in enumerate([0, 0.009, 0.019, 0.031]):
        m = n - ns(off)
        b = bp(noise(m, seed + k), 800, 4200) * ar(m, 0.0006, 0.012 if k < 3 else 0.09)
        y[ns(off):] += b
    y = np.tanh(1.5 * y)
    if pres:
        y = y + bp(y, 2000, 5000) * pres
    return fin(y)


def hat(seed=0, open_=False):
    d = 0.22 if open_ else 0.05
    n = ns(d)
    x = hp(noise(n, seed), 7200, 4) * ar(n, 0.0005, 0.06 if open_ else 0.012)
    return fin(x * (0.6 if open_ else 0.5))


def shaker(seed=0):
    n = ns(0.09)
    return fin(bp(noise(n, seed), 4500, 12000) * ar(n, 0.012, 0.025) * 0.5)


def taiko(f0=62.0, d=1.5, seed=0, drive=1.6, skin=0.8):
    n = ns(d); t = tax(n)
    f = f0 * (1 + 0.45 * np.exp(-t / 0.03))
    body = sine(f, n) * ar(n, 0.002, 0.32)
    m2 = sine(f * 1.52, n, 0.3) * ar(n, 0.001, 0.11) * 0.35
    m3 = sine(f * 2.31, n, 0.6) * ar(n, 0.001, 0.06) * 0.22
    sk = lp(bp(noise(n, seed), 100, 1600), 1400) * ar(n, 0.001, 0.045) * skin
    y = np.tanh(drive * (body + m2 + m3 + sk)) / np.tanh(drive)
    return fin(hp(y, 40))                     # keep the taikos out of the sub (the kick / sub own < 40 Hz)


def tom(f0=110.0, seed=0):
    return taiko(f0, d=0.6, seed=seed, drive=1.4, skin=0.6)


def tick_clock(seed=0, acc=1.0):
    n = ns(0.04); t = tax(n)
    nz = bp(noise(n, seed), 2200, 7000) * ar(n, 0.0003, 0.003)
    body = sine(820 * (1 + 0.05 * np.exp(-t / 0.003)), n) * ar(n, 0.0005, 0.006) * 0.5
    return fin((nz + body) * 0.5 * acc)


def braam(midis, d=2.2, bright=1.0, seed=0, growl=0.14, bend=0.6, voices=3, edec=None, sub_amt=0.45):
    n = ns(d); t = tax(n)
    bc = -bend * np.exp(-t / 0.07)
    rng = R(seed)
    out = np.zeros((2, n))
    for m in midis:
        f0 = float(mtof(m))
        for ch in range(2):
            for v in range(voices):
                det = (v - (voices - 1) / 2) * 0.09 + rng.normal(0, 0.02) + (0.02 if ch else -0.02)
                out[ch] += saw(f0 * 2 ** ((bc + det) / 12), n, rng.random())
    out /= np.sqrt(len(midis) * voices)
    rise = 1 - np.exp(-t / 0.06)
    fc = 110 + (300 + 2300 * bright) * rise * np.exp(-t / 0.95) + 260 * bright
    out = tvf(out, fc, q=1.3)
    out = tvf(out, fc * 1.2, q=0.6)
    out *= 1 + growl * np.sin(2 * np.pi * 31 * t)
    out = np.tanh(2.6 * out) / np.tanh(2.6)
    env = ar(n, 0.014, edec if edec else d * 0.42)
    sub = sine(mtof(min(midis)), n) * ar(n, 0.01, edec if edec else d * 0.35)
    y = out * env + stereo(np.tanh(1.5 * sub) * sub_amt)
    return fin(y, 30)


def impact(seed=0, size=1.0, sub=(120, 34), metal=100.0, d=2.4, bright=1.0, metal_amt=0.35, subdec=None):
    n = ns(d); t = tax(n); rng = R(seed)
    s = sine(sub[1] + (sub[0] - sub[1]) * np.exp(-t / 0.11), n) * ar(n, 0.002, subdec if subdec else 0.5 * size)
    s = np.tanh(2.2 * s)
    thud = lp(noise(n, seed + 1), 260) * ar(n, 0.001, 0.09) * 3.0
    crack = bp(noise(n, seed + 2), 350, 7000) * ar(n, 0.0007, 0.02) * bright
    crack = np.tanh(5 * crack) / 1.6
    grit = bp(noise(n, seed + 3), 150, 2400) * ar(n, 0.001, 0.22 * size) * 0.4
    mono = s + thud * 0.5 + crack * 0.55 + grit
    met = np.zeros((2, n))
    for k, (r, dec, a) in enumerate([(1, 1.4, 1.0), (2.32, 1.0, 0.7), (3.86, 0.75, 0.55), (5.41, 0.5, 0.4),
                                     (7.27, 0.35, 0.3), (9.63, 0.25, 0.22), (12.4, 0.18, 0.15)]):
        fk = metal * r
        if fk > 1450:
            continue
        for ch in range(2):
            met[ch] += sine(fk * (1 + rng.normal(0, 0.004)), n, rng.random()) * ar(n, 0.0008, dec * size) * a
    met = np.tanh(1.3 * met) * metal_amt
    return fin(stereo(mono) + met, 20)


def sub_drop(f0=110.0, f1=30.0, d=1.4, tau=0.25):
    n = ns(d); t = tax(n)
    f = f1 + (f0 - f1) * np.exp(-t / tau)
    return fin(np.tanh(1.8 * sine(f, n) * ar(n, 0.004, d * 0.45)), 20)


def crash(d=2.6, seed=0, dark=1.0):
    n = ns(d); t = tax(n)
    x = np.vstack([noise(n, seed), noise(n, seed + 7)])
    x = hp(x, 2800, 2) + 0.4 * bp(x, 900, 2800)
    fc = 4500 + 9000 * dark * np.exp(-t / 0.5)
    x = tvf(x, fc, q=0.6, blk=128)
    env = ar(n, 0.001, 0.75 * d / 2.6) * (1 + 0.6 * np.exp(-t / 0.05))
    return fin(x * env * 0.45, 40)


def whoosh(d, peak, lo=250, hi=4000, pan0=-0.7, pan1=0.7, onset=0.25, seed=0, low=0.5, after=0.10, q=1.1):
    n = ns(d); t = tax(n)
    pos = np.clip(t / peak, 0, 1)
    amp = onset + (1 - onset) * pos ** 2.6
    amp = np.where(t > peak, np.exp(-(t - peak) / after), amp)
    amp *= np.clip(t / 0.004, 0, 1)
    fc = lo * (hi / lo) ** (pos ** 1.4)
    fc = np.where(t > peak, hi * np.exp(-(t - peak) / 0.25) + lo, fc)
    x = np.vstack([noise(n, seed), noise(n, seed + 1)])
    y = tvf(x, fc, q=q, kind='band', blk=64) * 2.2
    y += stereo(lp(noise(n, seed + 2), 220) * low * 2.0)
    y *= amp
    pan = pan0 + (pan1 - pan0) * pos
    y[0] *= np.cos((pan + 1) * np.pi / 4) * np.sqrt(2)
    y[1] *= np.sin((pan + 1) * np.pi / 4) * np.sqrt(2)
    return fin(y, 8)


def swish(d=0.16, lo=600, hi=3200, seed=0, g=1.0, pan=0.0):
    """small UI reveal swish: fast onset, airy, short."""
    n = ns(d); t = tax(n)
    fc = lo * (hi / lo) ** np.clip(t / d, 0, 1)
    x = tvf(noise(n, seed), fc, q=0.9, kind='band') * ar(n, 0.003, d * 0.3) * 1.6
    return fin(stereo(x * g, pan))


def reverse_swell(d=0.5, seed=0, bright=1.0):
    n = ns(d)
    c = crash(d + 0.2, seed, dark=bright)[:, :n]
    r = c[:, ::-1] * 1.3
    t = tax(n)
    low = lp(noise(n, seed + 3), 300) * (t / d) ** 3 * 1.5
    y = r + stereo(low)
    y[:, -ns(0.003):] *= np.linspace(1, 0, ns(0.003))
    return y


def riser(d, seed=0, m0=41, m1=53, lo=200, hi=7000, trem=True):
    n = ns(d); t = tax(n); pos = t / d
    x = np.vstack([noise(n, seed), noise(n, seed + 1)])
    fc = lo * (hi / lo) ** (pos ** 1.6)
    y = tvf(x, fc, q=1.4, kind='band', blk=64) * 1.8
    m = m0 + (m1 - m0) * pos ** 1.5
    cl = np.zeros((2, n))
    rng = R(seed + 5)
    for iv in (0, 7, 12):
        for ch in range(2):
            cl[ch] += saw(mtof(m + iv + rng.normal(0, 0.05)), n, rng.random())
    cl = tvf(cl, 300 + 2200 * pos ** 2, q=0.9) * 0.35
    y = (y + cl) * pos ** 2.2
    if trem:
        rate = 8 + 16 * pos ** 2
        y *= 0.65 + 0.35 * np.cos(2 * np.pi * np.cumsum(rate) / SR)
    y[:, :ns(0.01)] *= np.linspace(0, 1, ns(0.01))
    return fin(y, 4)


def crackle(d, rate=60, seed=0, lo=900, hi=6500, decay=None, g=1.0):
    n = ns(d); rng = R(seed)
    k = max(1, int(rate * d))
    imp = np.zeros((2, n))
    for ch in range(2):
        idx = rng.integers(0, n, k)
        imp[ch, idx] = rng.exponential(1.0, k) * rng.choice([-1, 1], k)
    y = bp(imp, lo, hi) * 3.0 + 0.5 * bp(imp, 300, 900)
    if decay:
        y *= np.exp(-tax(n) / decay)
    return fin(y * g)


def fire_burst(d=0.6, seed=0, g=1.0):
    n = ns(d); t = tax(n)
    x = np.vstack([noise(n, seed), noise(n, seed + 1)])
    fc = 1800 * np.exp(-t / 0.18) + 250
    y = tvf(x, fc, q=0.7, blk=64) * ar(n, 0.003, 0.16)
    y = np.tanh(2.5 * y) * 0.8
    wh = sine(40 + 50 * np.exp(-t / 0.06), n) * ar(n, 0.004, 0.18)
    y += stereo(wh * 0.8)
    y += crackle(d, 90, seed + 2, decay=0.25) * 0.5
    return fin(y * g, 20)


def steam(d=0.9, seed=0, g=1.0, att=0.012):
    n = ns(d); t = tax(n)
    x = np.vstack([noise(n, seed), noise(n, seed + 1)])
    y = hp(x, 2600, 2) * 0.5 + bp(x, 4000, 9000) * 0.6
    y *= ar(n, att, 0.28) * (1 + 0.25 * np.sin(2 * np.pi * 23 * t))
    return fin(y * g * 0.5, 30)


def eruption(seed=0, g=1.0, pan=0.0, f0=58.0):
    tk = stereo(taiko(f0, 1.2, seed, drive=1.8), 0)
    fb = fire_burst(0.7, seed + 10)
    y = np.zeros((2, ns(1.2)))
    y += tk * 0.9
    y[:, :fb.shape[1]] += fb * 0.75
    y = hp(y, 40)
    y[0] *= 1 - 0.35 * max(pan, 0)
    y[1] *= 1 + 0.35 * min(pan, 0)
    return y * g


def crack_hit(seed, d=0.12):
    """distorted broadband transient (the 'snap' on top of a trailer hit)."""
    n = ns(d)
    x = np.vstack([noise(n, seed), noise(n, seed + 1)])
    x = np.tanh(4 * bp(x, 700, 9000) * ar(n, 0.0005, 0.012)) * 0.6 + bp(x, 250, 1200) * ar(n, 0.0008, 0.025) * 0.6
    return fin(x, 10)


def quench(seed=0, g=1.0):
    n = ns(1.4)
    y = impact(seed, size=0.8, sub=(95, 36), metal=85, d=1.4, bright=0.8, metal_amt=0.25)
    sp = bp(np.vstack([noise(n, seed + 4), noise(n, seed + 5)]), 250, 2200) * ar(n, 0.002, 0.12) * 0.9
    y = y + sp
    st = steam(1.1, seed + 6, 1.4, att=0.18)
    y[:, :st.shape[1]] += st[:, :n]
    y += crackle(1.4, 40, seed + 7, decay=0.5) * 0.35
    return y * g


def sheen(seed=0, g=1.0):
    """cooling crackle 'tsk-sss' (replaces the old bell ting)."""
    n = ns(0.5)
    c = crackle(0.5, 260, seed, 1200, 7500, decay=0.06) * 1.2
    c[:, :ns(0.004)] += hp(noise(ns(0.004), seed + 1), 3000) * 0.6
    s = steam(0.5, seed + 2, 0.9) * np.exp(-tax(n) / 0.12)
    return fin((c + s) * g)


def tok(seed=0, body=260.0, g=1.0, bright=1.0, pan=0.0):
    n = ns(0.07); t = tax(n)
    cl = bp(noise(n, seed), 1500, 6000) * ar(n, 0.0008, 0.0022) * bright * 1.6
    bd = sine(body * (1 + 0.35 * np.exp(-t / 0.004)), n) * ar(n, 0.0006, 0.016)
    hp_ = sine(110, n) * ar(n, 0.001, 0.012) * 0.6
    return fin(stereo((cl + bd + hp_) * 0.5 * g, pan))


def clack(seed=0, g=1.0):
    a = tok(seed, 330, 1.0, 0.9)
    b = tok(seed + 1, 210, 0.8, 0.6)
    y = np.zeros((2, ns(0.1)))
    y[:, :a.shape[1]] += a
    o = ns(0.014)
    y[:, o:o + b.shape[1]] += b
    return y * g


def thump(seed=0, g=1.0, f0=95.0):
    """soft haptic landing."""
    n = ns(0.25); t = tax(n)
    s = sine(f0 * (1 + 0.6 * np.exp(-t / 0.01)), n) * ar(n, 0.001, 0.05)
    nz = lp(noise(n, seed), 900) * ar(n, 0.0008, 0.012) * 1.2
    cl = bp(noise(n, seed + 1), 1500, 5000) * ar(n, 0.0003, 0.002) * 0.6
    return fin(stereo((s + nz + cl) * 0.6 * g))


def heartbeat(seed=0, g=1.0):
    n = ns(0.6)
    y = np.zeros(n)
    for off, a in ((0.0, 1.0), (0.21, 0.7)):
        m = ns(0.3); t = tax(m)
        s = sine(42 + 35 * np.exp(-t / 0.03), m) * ar(m, 0.004, 0.07)
        s += lp(noise(m, seed), 180) * ar(m, 0.002, 0.03) * 1.5
        y[ns(off):ns(off) + m] += np.tanh(1.5 * s) * a
    return fin(stereo(y * g))


def denied(seed=0, gates=(0.0, 0.043, 0.084, 0.125, 0.25)):
    """'denied' stutter built from the OVER braam itself (same synth, same seed, Gb over F): 30-40 ms slices of its
    tail re-triggered on the stutter grid, decimated to 8 kHz (sample-and-hold), low-passed at 1.2 kHz. In key."""
    src = braam([29, 42, 49, 54], 2.4, 0.75, 32)
    tail = src[:, ns(0.30):ns(0.30) + ns(0.16)]
    n = ns(0.45)
    y = np.zeros((2, n))
    for k, o in enumerate(gates):
        L = ns(0.036 if k < len(gates) - 1 else 0.13)
        sl = tail[:, ns(0.012 * k):ns(0.012 * k) + L].copy()
        L = sl.shape[1]
        w = np.ones(L); f = ns(0.002)
        w[:f] = np.linspace(0, 1, f); w[-f:] = np.linspace(1, 0, f)
        if k == len(gates) - 1:
            w *= np.exp(-tax(L) / 0.05)
        y[:, ns(o):ns(o) + L] += sl * w * (1.0 if k == 0 else 0.8)
    y = np.repeat(y[:, ::6], 6, axis=1)[:, :n]          # 8 kHz sample-and-hold crush
    y = np.round(y * 24) / 24
    y = lp(y, 1200, 4)
    return fin(np.tanh(1.8 * y), 10)


def piano(m, d=3.5, vel=0.8, seed=0):
    n = ns(d); t = tax(n); rng = R(seed)
    f0 = float(mtof(m)); B = 0.00035
    y = np.zeros((2, n))
    for k in range(1, 16):
        fk = f0 * k * np.sqrt(1 + B * k * k)
        if fk > 3500:
            break
        a = vel * (1.3 if k == 1 else 1.0) / k ** 1.15 * (0.55 + 0.45 * vel) ** (k / 3)
        dec = 2.6 / (1 + 0.4 * k)
        for ch in range(2):
            det = 1 + (0.0006 if ch else -0.0006) + rng.normal(0, 0.0002)
            y[ch] += (sine(fk * det, n, rng.random()) + sine(fk / det, n, rng.random())) * 0.5 * a * ar(n, 0.002, dec)
    ham = lp(noise(n, seed + 1), 1100) * ar(n, 0.0005, 0.01) * 0.3
    y += stereo(ham)
    y = lp(y, 2600)
    return fin(y * 0.6, 40)


def string_pad(midis, d, seed=0, cutoff=1600, att=0.5, rel=0.8, voices=5):
    n = ns(d); t = tax(n)
    x = sawstack(midis, n, voices, 0.24, seed, drift=0.002, vib=0.0018)
    x = lp(x, cutoff, 2)
    x = hp(x, 90)
    env = np.clip(t / att, 0, 1) ** 1.5 * np.clip((d - t) / rel, 0, 1)
    return x * env


def choir(midis, d, seed=0, att=0.6, rel=1.0, bright=1.0, dec=None, voices=8, t0=0.0):
    """ensemble 'ah': 8 voices per note and per channel, each with its own detune, slow vibrato and a random
    onset (0-45 ms), soft source (saws low-passed at 2.5 kHz), three narrow vowel formants (Q ~6) + chest body,
    then a slow ensemble chorus. dec -> exponential decay instead of sustain + release."""
    n = ns(d); t = tax(n); rng = R(seed)
    x = np.zeros((2, n))
    for m in np.atleast_1d(midis):
        f0 = float(mtof(m))
        for ch in range(2):
            for v in range(voices):
                c = (v / (voices - 1) - 0.5) * 0.24 + rng.normal(0, 0.03)
                vr = rng.uniform(3.6, 4.6)
                vd = rng.uniform(0.0015, 0.003)
                f = f0 * 2 ** (c / 12) * (1 + vd * np.sin(2 * np.pi * vr * t + rng.uniform(0, 6.28)) * np.clip(t / 0.6, 0, 1)
                                          + 0.0012 * np.sin(2 * np.pi * rng.uniform(0.1, 0.3) * t + rng.uniform(0, 6.28)))
                on = rng.uniform(0, 0.045)
                ve = np.clip((t - on) / 0.04, 0, 1) * rng.uniform(0.7, 1.0)
                x[ch] += saw(f, n, rng.random()) * ve
    x /= np.sqrt(len(np.atleast_1d(midis)) * voices)
    x = lp(x, 2500, 2)
    br = lp(np.vstack([noise(n, seed + 1), noise(n, seed + 2)]), 5000) * 0.05
    src = x + br

    # moving vowel: F1 / F2 morph 'ah' <-> 'oh' over each bar on film time (t0 = placement time), +-8 %,
    # F3 drifts +-4 % on a slower cycle -> no static formant lines in the spectrogram
    tf = t0 + t
    mv = np.sin(2 * np.pi * tf / 2.0 + 0.7)          # one cycle per bar
    mv2 = np.sin(2 * np.pi * tf / 5.3 + 1.9)
    y = (tvf(src, 750 * (1 - 0.08 * mv), q=5.0, kind='band', blk=128) * 1.6
         + tvf(src, 1180 * (1 - 0.08 * mv + 0.03 * mv2), q=5.0, kind='band', blk=128) * 1.0 * bright
         + tvf(src, 2650 * (1 + 0.04 * mv2), q=5.0, kind='band', blk=128) * 0.35 * bright
         + bp(src, 220, 420, 1) * 0.5)
    y = Chorus(rate_hz=0.35, depth=0.18, centre_delay_ms=9.0, feedback=0.0, mix=0.45)(y.astype(np.float32), SR).astype(float)
    if dec:
        env = np.clip(t / max(att, 1e-3), 0, 1) ** 1.6 * np.exp(-np.maximum(t - att, 0) / dec)
    else:
        env = np.clip(t / att, 0, 1) ** 1.6 * np.clip((d - t) / rel, 0, 1)
    return y * env * 2.2


def spiccato(m, d=0.14, vel=1.0, seed=0, cutoff=2200):
    n = ns(d)
    x = sawstack([m, m + 12], n, 3, 0.14, seed, drift=0.0)
    x = lp(x, cutoff * (0.6 + 0.4 * vel), 2)
    bow = bp(np.vstack([noise(n, seed + 3), noise(n, seed + 4)]), 2000, 5000) * 0.05
    env = ar(n, 0.003, 0.05)
    return fin((x + bow) * env * vel, 8)


def low_pluck(m, d=0.16, vel=1.0, seed=0, open_=1.0):
    n = ns(d); t = tax(n); f = float(mtof(m)); rng = R(seed)
    x = saw(f * 1.003, n, rng.random()) + saw(f * 0.997, n, rng.random())
    fc = 280 + 1300 * open_ * vel * np.exp(-t / 0.045)
    x = tvf(x, fc, q=1.5)
    x = np.tanh(1.6 * x) + 0.6 * sine(f, n)
    return fin(x * ar(n, 0.002, 0.07, hold=0.02) * vel * 0.6, 8)


def reese_note(m, d, seed=0, cutoff=700):
    n = ns(d); f = float(mtof(m)); rng = R(seed)
    x = saw(f * 1.006, n, rng.random()) + saw(f * 0.994, n, rng.random()) + 0.5 * saw(f * 2.004, n, rng.random())
    raw = x
    x = lp(x, cutoff, 2)
    x = np.tanh(2.2 * x) * 0.55 + 0.6 * sine(f, n)
    # driven mid layer (what a phone hears): band-pass 200 Hz-1.8 kHz -> tanh(3x) -> LP 1.4 kHz, ~-6 dB, mono
    md = lp(np.tanh(3 * bp(raw, 200, 1800)), 1400, 4) * 0.8
    return fin((x + md) * ar(n, 0.003, 0.09, hold=0.03), 6)


def gate16(n, t0, depth=0.8, dec=0.05, phase_on=None):
    t = t0 + tax(n)
    ph = (t / 0.125) % 1.0
    g = (1 - depth) + depth * np.exp(-ph * 0.125 / dec) * np.sin(0.5 * np.pi * np.clip(ph * 0.125 / 0.009, 0, 1))
    return g


# ===================================================================================== MUSIC
print('music...')
# ---------------- lava bed for the whole film (low rumble + crackle), automated level
n = N
lav = lp(np.vstack([noise(n, 11), noise(n, 12)]), 110, 2) * 2.2
boil = bp(np.vstack([noise(n, 13), noise(n, 14)]), 180, 600) * (0.5 + 0.5 * np.sin(2 * np.pi * 0.7 * tax(n)))[None] * 0.4
lav += boil
lvl = np.interp(tax(n), [0, 0.4, 3.0, 4.0, 6, 10, 10.1, 40, 40.2, 45, 50, 54, 59, 59.5, 62],
                [0.7, 1.0, 1.0, 0.0, 0.6, 0.6, 0.35, 0.35, 0.8, 0.6, 0.3, 0.35, 0.3, 0.0, 0.0])
BUS['sfx'] += hp(lav, 32, 2) * lvl * 0.12
crk = np.zeros((2, N))
for i in range(60):
    c = crackle(1.0, 14, 100 + i, 700, 5000)
    crk[:, i * SR:i * SR + c.shape[1]] += c
BUS['sfx'] += crk * lvl * 0.10

# ---------------- HOOK 0-4
place('music', string_pad([29, 41, 42, 48], 1.0, 21, cutoff=500, att=0.6, rel=0.2), 0.0, 0.35, mhall=0.3)
place('hits', braam([29, 36, 41, 44, 48], 2.0, 1.0, 31), 1.0, 0.62, mhall=0.35)
place('hits', braam([29, 42, 49, 54], 2.4, 0.75, 32), 1.5, 0.66, mhall=0.4)
place('music', string_pad([41, 42, 48, 53], 1.5, 22, cutoff=1300, att=0.35, rel=0.3), 1.5, 0.35, mhall=0.4)
# ostinato + clock 2.0-3.0
for i in range(8):
    t = 2.0 + i * 0.125
    m = [41, 41, 48, 41, 44, 41, 48, 42][i]
    place('music', spiccato(m, 0.14, 0.75 + 0.25 * (i % 4 == 0), 200 + i), t, 0.32, mhall=0.2)
for i in range(4):
    place('drums', tick_clock(300 + i, 1.0), 2.0 + i * 0.25, 0.8, room=0.2)

# ---------------- REJOUER 4-6
place('hits', braam([29, 36, 41, 48], 1.0, 0.8, 33), 4.0, 0.7, mhall=0.3)
place('music', string_pad([41, 48, 53, 56], 2.0, 23, cutoff=1100, att=0.4, rel=0.3), 4.0, 0.3, mhall=0.4)
for i in range(4):
    place('bass', low_pluck(29 if i % 2 == 0 else 41, 0.2, 0.9, 400 + i, 0.6), 4.0 + i * 0.25, 0.9)
for i in range(8):
    t = 5.0 + i * 0.0625 * 2
    place('bass', low_pluck([29, 29, 41, 29, 32, 29, 41, 36][i], 0.15, 0.95, 410 + i, 1.0), t, 0.9)
for i in range(16):
    t = 4.0 + i * 0.125
    if clear(t):
        place('drums', tick_clock(310 + i, 0.6 + 0.4 * (i % 2 == 0)), t, 0.6, room=0.15)
place('hits', braam([29, 41, 48, 53, 56], 1.6, 1.4, 34), 5.0, 0.55, mhall=0.4)
place('music', riser(0.5, 35, 41, 46), 5.5, 0.5, mhall=0.2)
for i in range(8):
    t = 5.5 + i * 0.0625
    place('drums', snare(500 + i, 0.2, bright=0.8), t, 0.25 + 0.4 * i / 7, plate=0.25)

# ---------------- LEVEL 1 6-10
for b in range(8):            # beats 6.0 .. 9.5
    t = 6.0 + b * 0.5
    if t < 9.0:
        if b > 0:     # no kick on the 6.0 cut: the NIVEAU slam 150 ms later is the hit
            place('drums', kick(600 + b, drive=2.0), t, 0.75); DK.append((t, 0.35, 0.18))
        place('drums', taiko(64 if b % 2 == 0 else 82, 1.0, 610 + b), t, 0.55 if b else 0.35, room=0.3, hall=0.15)
for i in range(24):           # spiccato 16ths 6.0-9.0
    t = 6.0 + i * 0.125
    ch = chord_at(t)
    pat = [0, 0, 2, 0, 1, 0, 3, 2]
    tones = [CH[ch][0], CH[ch][2], CH[ch][1] + 12 if False else CH[ch][1], CH[ch][3]]
    m = sorted(CH[ch][:4])[pat[i % 8] % 4]
    place('music', spiccato(m, 0.14, 0.7 + 0.3 * (i % 4 == 0), 700 + i, cutoff=min(2200, 1800 + 60 * i)), t, 0.3, mhall=0.2)
    if clear(t):
        place('drums', tick_clock(720 + i, 0.5 + 0.5 * (i % 2 == 0)), t, 0.5, room=0.1)
place('music', string_pad([41, 48, 53, 56], 3.0, 24, cutoff=1200, att=0.8, rel=0.4), 6.0, 0.28, mhall=0.4)
place('music', string_pad([37, 44, 49, 53], 1.0, 25, cutoff=1500, att=0.2, rel=0.2), 8.0, 0.28, mhall=0.4)
place('music', string_pad([36, 43, 49, 52], 1.0, 26, cutoff=1800, att=0.2, rel=0.05), 9.0, 0.3, mhall=0.4)
for i in range(16):           # overheat: 16th tremolo (repeated notes, C7b9 phrygian dominant) + snare/tom roll 9.0-10.0
    t = 9.0 + i * 0.0625
    v = 0.4 + 0.6 * i / 15
    cf = 1100 + 1900 * i / 15  # filter opens as it builds
    place('music', spiccato(36, 0.08, v, 750 + i, cutoff=cf), t, 0.2, mhall=0.2, pan=-0.25)
    place('music', spiccato(43, 0.08, v, 790 + i, cutoff=cf), t, 0.16, mhall=0.2, pan=0.25)
    place('music', spiccato(49, 0.07, v, 810 + i, cutoff=cf), t, 0.11, mhall=0.25, pan=-0.4)
    place('music', spiccato(52, 0.07, v, 830 + i, cutoff=cf), t, 0.11, mhall=0.25, pan=0.4)
    place('drums', snare(760 + i, 0.18, bright=0.7), t, 0.15 + 0.35 * v, plate=0.25)
    if i % 2 == 0:
        place('drums', tom(90 + 3 * i, 770 + i), t, 0.25 + 0.3 * v, room=0.3)
place('music', riser(1.0, 36, 36, 48), 9.0, 0.55, mhall=0.2)
for b in range(9, 10):
    place('bass', low_pluck(36, 0.3, 1.0, 780), 9.0, 0.6)

# ---------------- POWER-UPS 10-40 hybrid groove
# layers follow the picture: power-up index pu(t) = 0..5 (one per 5 s). Per-hit layers switch exactly on the
# whip-pan cuts (15/20/25/30/35); per-bar layers (choir, pad) switch on the 10 s phase cuts 20.0 and 30.0.
#   pu 0 (10-15): kick/snare/8th hats/taiko on 1/low ostinato A (kick hold 10 ms)
#   pu 1 (15-20): + 16th hats, spiccato strings, ostinato B
#   pu 2-3 (20-30): + backbeat toms, taiko on 3, pickup kick, shaker, open hats, choir
#   pu 4-5 (30-40): + string pad, brighter pulse
# A tom fill rolls into every whip-pan cut (P+4.5 -> P+5).
def pu(t):
    return int(np.clip((t + 1e-6 - 10.0) // 5, 0, 5))


OST = [[0, 0, 2, 0, 1, 0, 2, 3, 0, 0, 2, 0, 1, 2, 3, 2],
       [0, 2, 0, 3, 0, 2, 1, 0, 0, 2, 0, 3, 2, 1, 0, 1]]
SPC = [[0, 2, 1, 3], [0, 3, 2, 1]]
for bar in range(5, 20):
    t0 = bar * 2.0
    phb = (bar - 5) // 5          # 0..2, 10 s phases starting at 10 / 20 / 30
    ch = chord_at(t0 + 0.01)
    for beat in range(4):
        tb = t0 + beat * 0.5
        lv = pu(tb)
        if beat in (0, 2):
            place('drums', kick(800 + bar * 4 + beat, drive=2.4, hold=0.010, adec=0.13, f_end=50.0), tb, 0.95)
            DK.append((tb, 0.55, 0.22))
            if beat == 0 or lv >= 2:
                place('drums', taiko(68, 1.0, 820 + bar * 4 + beat, drive=1.7), tb, 0.45, room=0.3, hall=0.12)
        else:
            place('drums', snare(840 + bar * 4 + beat), tb, 0.6, plate=0.35)
            place('drums', clap(860 + bar * 4 + beat), tb + 0.004, 0.35, plate=0.3)
            if lv >= 2:
                place('drums', tom(120, 880 + bar * 4 + beat), tb, 0.3, room=0.3)
            if lv >= 4:   # 30-40: quiet four-on-the-floor under the backbeat (foreshadows the drop, festival DNA)
                place('drums', kick(940 + bar * 4 + beat, drive=2.2, hold=0.010, adec=0.12, f_end=50.0), tb, 0.6)
                DK.append((tb, 0.4, 0.2))
        if lv >= 2 and beat == 1 and clear(tb + 0.375):
            place('drums', kick(900 + bar * 4, drive=2.0, hold=0.010), tb + 0.375, 0.6)
            DK.append((tb + 0.375, 0.35, 0.16))
    # hats (8ths in power-up 1, 16ths from power-up 2 on)
    k = 0
    tt_ = t0
    while tt_ < t0 + 2.0 - 1e-6:
        lv = pu(tt_)
        on8 = abs(((tt_ - t0) / 0.125) % 2) < 1e-6
        if (lv >= 1 or on8) and clear(tt_):
            acc = 1.0 if abs((tt_ - t0) % 0.5 - 0.25) < 1e-6 else 0.55
            place('drums', hat(1000 + bar * 20 + k, open_=(lv >= 2 and abs((tt_ - t0) % 0.5 - 0.25) < 1e-6)), tt_,
                  0.32 * acc, pan=0.25 if k % 2 else -0.15)
        if lv >= 2 and on8 and clear(tt_ + 0.0625):
            place('drums', shaker(1100 + bar * 20 + k), tt_ + 0.0625, 0.25, pan=-0.4)
        tt_ += 0.125
        k += 1
    # low synth ostinato 16ths (pattern alternates per power-up) + spiccato from power-up 2
    tones = sorted(CH[ch][:4])
    for i in range(16):
        ts = t0 + i * 0.125
        lv = pu(ts)
        m = tones[OST[lv % 2][i]]
        vel = 1.0 if i % 4 == 0 else (0.75 if i % 2 == 0 else 0.6)
        place('bass', low_pluck(m, 0.15, vel, 1300 + bar * 16 + i, open_=0.55 + 0.07 * lv), ts, 0.5)
        if lv >= 1:
            ms = tones[SPC[lv % 2][i % 4]] + 12 + (12 if (lv >= 4 and i % 8 == 6) else 0)
            place('music', spiccato(ms, 0.13, 0.65 + 0.35 * (i % 4 == 0), 1500 + bar * 16 + i, cutoff=1700 + 150 * lv),
                  ts, 0.17 + 0.015 * lv, mhall=0.22, pan=0.3 if i % 2 else -0.3)
    # sub on the root, pumped by the side-chain
    nn = ns(2.0)
    place('bass', fin(sine(subf(ROOT[ch]), nn) * np.clip(tax(nn) / 0.01, 0, 1), 10) * 0.26, t0, 1.0)
    # wide gated electronic pulse on the chord
    pad = sawstack(CH[ch][1:], nn, 4, 0.22, 1600 + bar, drift=0.002)
    pad = lp(pad, 1000 + 800 * phb, 2) * gate16(nn, t0, 0.85, 0.045)
    place('music', pad, t0, 0.22 + 0.05 * phb, mhall=0.25)
    if phb == 1:
        place('music', choir(CH[ch][1:4], 2.1, 1700 + bar, att=0.4, rel=0.3, t0=t0), t0, 0.20, mhall=0.4)
    elif phb == 2:        # pad role: slow swell under the string pad, no attack of its own
        place('music', choir(CH[ch][1:4], 2.15, 1700 + bar, att=0.9, rel=0.5, bright=0.8, t0=t0), t0, 0.24, mhall=0.45)
    if phb == 2:
        place('music', string_pad(CH[ch][:4], 2.05, 1750 + bar, cutoff=2000, att=0.2, rel=0.2), t0, 0.22, mhall=0.35)
# tom fill into every whip-pan cut (P+4.5 .. P+4.875), lighter into the breakdown
for P in (10, 15, 20, 25, 30, 35):
    gf = 0.3 if P == 35 else 0.45
    for i in range(4):
        tf = P + 4.5 + i * 0.125
        if i == 0 or clear(tf):
            place('drums', tom(150 - 16 * i, 1200 + P * 4 + i), tf, gf * (0.8 + 0.1 * i), room=0.35)
    if P < 35 and clear(P + 4.875):
        place('drums', snare(1260 + P, 0.25, bright=0.8), P + 4.875, 0.3, plate=0.3)


# ---------------- BREAKDOWN 40-45
for i, tb in enumerate([40.0, 41.0, 42.0, 43.0, 44.0]):
    place('drums', heartbeat(1900 + i), tb, 0.9, room=0.2)
place('music', choir([41, 48, 53, 56], 2.3, 1910, att=0.5, rel=0.4, t0=40.0), 40.0, 0.55, mhall=0.6)
place('music', choir([37, 44, 49, 53], 2.3, 1911, att=0.3, rel=0.4, t0=42.0), 42.0, 0.55, mhall=0.6)
place('music', choir([39, 46, 51, 55], 1.2, 1912, att=0.3, rel=0.2, t0=44.0), 44.0, 0.5, mhall=0.6)
place('music', string_pad([29, 41], 5.0, 1913, cutoff=400, att=0.8, rel=0.3), 40.0, 0.35)
for t, m, v in [(40.0, 41, 0.9), (41.0, 48, 0.6), (41.5, 44, 0.7), (42.0, 37, 0.9), (42.5, 44, 0.55),
                (43.0, 49, 0.6), (43.5, 48, 0.55), (44.0, 39, 0.85), (44.5, 46, 0.5)]:
    place('music', piano(m, 2.5, v, 1920 + int(t * 10)), t, 0.6, mhall=0.5)

# ---------------- BUILD 45-50
for b in range(10):
    tb = 45.0 + b * 0.5
    place('drums', kick(2000 + b, drive=2.2), tb, 0.8 if b < 8 else 0.9)
    DK.append((tb, 0.5, 0.2))
    if b % 2 == 1:
        place('drums', tom(110, 2020 + b), tb, 0.35, room=0.3)
rolls = [(47.0, 48.0, 0.25), (48.0, 49.0, 0.125), (49.0, 49.94, 0.0625), (49.5, 49.94, 0.03125)]
for a, b_, st in rolls:
    tr = a
    while tr < b_ - 1e-6:
        prog = (tr - 47.0) / 2.94
        if clear(tr) or st >= 0.0625:
            place('drums', snare(2100 + int(tr * 100), 0.2, bright=0.8), tr, 0.16 + 0.3 * prog, plate=0.3)
        tr += st
for i in range(40):
    ts = 45.0 + i * 0.125
    ch = chord_at(ts)
    tones = sorted(CH[ch][:4])
    octv = 0 if ts < 47 else (12 if ts < 49 else 12)
    m = tones[[0, 2, 1, 3][i % 4]] + octv
    place('music', spiccato(m, 0.13, 0.7 + 0.3 * (i % 4 == 0), 2200 + i, cutoff=1800 + 40 * i), ts, 0.22, mhall=0.25,
          pan=0.3 if i % 2 else -0.3)
    place('bass', low_pluck(tones[0] - 12, 0.14, 0.9 if i % 2 == 0 else 0.6, 2300 + i, open_=0.6 + i / 60), ts, 0.6)
for a, b_, ch in [(45.0, 47.0, 'Db'), (47.0, 49.0, 'Eb'), (49.0, 49.94, 'C')]:
    nn = ns(b_ - a)
    pad = sawstack(CH[ch][1:], nn, 4, 0.22, 2400 + int(a), drift=0.002)
    fc = np.linspace(700 + (a - 45) * 400, 1200 + (b_ - 45) * 450, nn)
    pad = tvf(pad, fc, q=0.8, blk=128) * gate16(nn, a, 0.85, 0.04)
    place('music', fin(pad, 4), a, 0.28, mhall=0.25)
    rootf = subf(ROOT[ch])
    place('bass', fin(sine(float(rootf), nn) * np.clip(tax(nn) / 0.01, 0, 1), 6) * 0.5, a, 1.0)
place('music', riser(4.94, 2500, 41, 60, 150, 9000), 45.0, 0.3, mhall=0.25)
place('music', riser(0.94, 2501, 48, 60, 400, 10000), 49.0, 0.22, mhall=0.2)

# ---------------- DROP 50-54
for b in range(8):
    tb = 50.0 + b * 0.5
    place('drums', drop_kick(2600 + b), tb, 0.85)
    DK.append((tb, 0.55, 0.24))
    if b % 2 == 1:
        tsn = tb + (0.015 if abs(tb - 52.5) < 1e-6 else 0.0)
        place('drums', snare(2620 + b, 0.35, pres=0.41), tsn, 0.9, plate=0.35)
        place('drums', clap(2640 + b, pres=0.41), tsn + 0.004, 0.8, plate=0.35)
    to = tb + 0.25
    if clear(to):
        place('drums', hat(2660 + b, open_=True), to, 0.5, pan=0.2)
    for s in (0.125, 0.375):
        if clear(tb + s):
            place('drums', hat(2680 + b * 2 + int(s * 8), False), tb + s, 0.22, pan=-0.25)
    for j in range(4):        # 16th closed-hat / ride layer (top end for small speakers)
        th = tb + j * 0.125
        if clear(th):
            rd = hp(noise(ns(0.09), 2900 + b * 4 + j), 5000, 2) * ar(ns(0.09), 0.0006, 0.03 if j % 2 else 0.02)
            tag = any(0 <= th - tg < 0.12 for tg in (53.0, 53.5))
            place('drums', fin(rd), th, (0.26 if j % 2 else 0.36) * (0.63 if tag else 1.0), pan=0.35)
for i in range(32):           # rolling reese, 16ths 2-4 of every beat
    ts = 50.0 + i * 0.125
    if i % 4 == 0:
        continue
    ch = chord_at(ts)
    root = ROOT[ch] if ROOT[ch] < 36 else ROOT[ch] - 12
    m = root + (12 if i % 4 == 2 else 0) + 12
    if not clear(ts):
        continue
    place('bass', reese_note(m, 0.12, 2700 + i, cutoff=500 + 300 * (i % 4 == 3)), ts, 0.5)
for a, b_ in [(50.0, 52.0), (52.0, 53.0), (53.0, 54.0)]:
    ch = chord_at(a)
    nn = ns(b_ - a)
    pad = sawstack(CH[ch][1:], nn, 5, 0.26, 2800 + int(a), drift=0.002)
    pad = lp(pad, 4500, 2) * gate16(nn, a, 0.5, 0.06)
    place('music', fin(pad, 4), a, 0.42 if a < 52 else 0.52, mhall=0.3)
    place('music', choir(CH[ch][1:4], b_ - a, 2810 + int(a), att=0.05, rel=0.1, t0=a), a, 0.18, mhall=0.35)
    rootf = subf(ROOT[ch])
    place('bass', fin(sine(float(rootf), nn) * np.clip(tax(nn) / 0.005, 0, 1), 6) * 0.45, a, 1.0)
nn = ns(4.0)                  # wide noise 'air' bed gated on 16ths (electro drop texture, fills the top end)
air = bp(np.vstack([noise(nn, 2950), noise(nn, 2951)]), 2500, 12000, 2) * gate16(nn, 50.0, 0.7, 0.05)
air *= np.interp(tax(nn), [0, 0.05, 3.9, 4.0], [0, 1, 1.25, 0])[None]
for tg in (3.0, 3.5):         # taglines 53.0 / 53.5: air -4 dB for 120 ms
    air *= np.interp(tax(nn), [tg - 0.02, tg, tg + 0.12, tg + 0.16], [1, 0.63, 0.63, 1], left=1, right=1)[None]
place('music', air, 50.0, 0.12, mhall=0.1)
for t, chd, d, br, g in [(50.0, [29, 36, 41, 44, 48, 53], 1.0, 1.4, 0.6), (50.875, [29, 41, 48, 53, 56], 1.0, 1.2, 0.45),
                         (52.0, [25, 37, 44, 49, 53], 0.9, 0.85, 0.5), (53.0, [27, 39, 46, 51, 55], 0.8, 1.3, 0.5),
                         (53.5, [24, 36, 43, 48, 52], 0.8, 1.4, 0.52)]:
    place('hits', braam(chd, d, br, int(t * 100), sub_amt=0.45 if t < 50.5 else 0.15), t, g * {50.0: 1.45, 50.875: 2.7, 52.0: 1.2, 53.0: 3.15, 53.5: 2.6}[t], mhall=0.35)

# ---------------- END 54-60
place('music', choir([41, 48, 53, 55, 60], 1.15, 3000, att=0.7, rel=0.2, t0=54.0), 54.0, 0.55, mhall=0.45)
place('music', choir([41, 48, 53, 56, 60], 1.15, 3001, att=0.15, rel=0.2, t0=55.0), 55.0, 0.55, mhall=0.45)
place('music', choir([37, 44, 49, 51, 56], 2.1, 3002, att=0.08, rel=0.2, t0=56.0), 56.0, 0.55, mhall=0.45)
place('music', choir([39, 46, 51, 56, 58], 0.6, 3003, att=0.06, rel=0.1, t0=58.0), 58.0, 0.55, mhall=0.45)
place('music', choir([39, 46, 51, 55, 58], 0.55, 3004, att=0.03, rel=0.1, t0=58.5), 58.5, 0.45, mhall=0.45)
place('music', choir([41, 48, 53, 56, 60, 65], 1.0, 3005, att=0.01, dec=0.35, t0=59.0), 59.0, 0.5, mhall=0.5)
for a, b_, chd in [(54.0, 55.0, [29, 41, 48, 55]), (55.0, 56.0, [29, 41, 48, 56]), (56.0, 58.0, [25, 37, 44, 51]),
                   (58.0, 58.5, [27, 39, 46, 56]), (58.5, 59.0, [27, 39, 46, 55])]:
    place('music', string_pad(chd, b_ - a + 0.05, 3010 + int(a * 10), cutoff=1400, att=0.12, rel=0.08), a, 0.35, mhall=0.4)
    rootf = subf(chd[0])
    nn = ns(b_ - a)
    place('bass', fin(sine(float(rootf), nn) * np.clip(tax(nn) / 0.01, 0, 1), 8) * 0.5, a, 1.0)
for t, m, v in [(54.0, 41, 0.9), (55.0, 48, 0.6), (56.0, 37, 0.9), (57.0, 44, 0.6), (58.0, 39, 0.85)]:
    place('music', piano(m, 2.5 if t < 58 else 1.3, v, 3100 + int(t)), t, 0.55, mhall=0.5)
for i, tb in enumerate([54.0, 55.0, 55.5, 56.0, 57.0, 57.5, 58.0]):
    place('drums', taiko(58 if i % 2 == 0 else 72, 1.3, 3200 + i, drive=1.7), tb, 0.55, room=0.3, hall=0.2)
for i, tb in enumerate([56.0, 56.5, 57.0, 57.5, 58.0, 58.5]):
    place('drums', kick(3250 + i, drive=2.2), tb, 0.65)
    DK.append((tb, 0.4, 0.2))
for i, tb in enumerate([55.0, 57.0]):
    place('drums', snare(3270 + i, 0.4), tb, 0.45, plate=0.45)
for i in range(13):           # pickup 58.5-58.9 snare 32nds
    t = 58.5 + i * 0.03125
    place('drums', snare(3300 + i, 0.15, bright=0.7), t, 0.08 + 0.18 * i / 15, plate=0.3)
for i in range(16):           # end ostinato 56-58
    ts = 56.0 + i * 0.125
    tones = sorted(CH['Db'][:4])
    place('music', spiccato(tones[[0, 2, 1, 3][i % 4]] + 12, 0.13, 0.7 + 0.3 * (i % 4 == 0), 3400 + i, cutoff=2200), ts,
          0.18, mhall=0.3, pan=0.3 if i % 2 else -0.3)

# ===================================================================================== SFX on the cue sheet
print('sfx...')
S = 'sfx'
# --- HOOK
nn = ns(0.9); t = tax(nn)
whum = sine(38 + 30 * np.exp(-t / 0.08), nn) * ar(nn, 0.006, 0.18)
place(S, whum, 0.0, 0.7)
place(S, swish(0.35, 300, 1400, 5000, 0.8), 0.0, 0.8)
for k, t0 in enumerate([0.163, 0.325]):
    place(S, swish(0.3, 300, 1200, 5010 + k, 0.5), t0, 0.7)
    place(S, sine(45, ns(0.4)) * ar(ns(0.4), 0.005, 0.1), t0, 0.35)
place(S, thump(5020, 0.6, 70), 0.25, 0.6)
for k, tb in enumerate([0.217, 0.353, 0.45, 0.579]):
    place(S, crackle(0.12, 120, 5030 + k, 600, 4000, decay=0.03), tb, 0.6)
place(S, sub_drop(120, 30, 1.2, 0.18), 0.5, 0.9)
place(S, thump(5040, 1.2, 60), 0.5, 1.0, room=0.3)
place(S, fire_burst(0.5, 5041, 0.6), 0.5, 0.8)
place(S, steam(0.7, 5042, 1.0), 0.55, 0.6)
for k, (a, b_) in enumerate([(0.775, 1.0), (1.275, 1.5)]):
    place(S, whoosh(b_ - a + 0.02, b_ - a, 200, 3000, -0.5 + k, 0.0, onset=0.35, seed=5050 + k, low=0.6), a, 0.75)
    place(S, swish(0.12, 3500, 900, 5055 + k, 1.2), a, 1.0)
    place('drums', tom(80, 5057 + k), a, 0.4, room=0.3)
for k, t0 in enumerate([1.0, 1.5]):
    place(S, impact(5060 + k, 1.2, (130, 33), 92 + 10 * k, 2.6, bright=1.3 if k == 0 else 1.0), t0, 1.0, hall=0.35)
    place('hitd', taiko(55, 1.6, 5070 + k, drive=2.0), t0, 0.8, hall=0.3)
    place(S, crash(2.4, 5080 + k, dark=0.6), t0, 0.5, hall=0.3)
    DH.append((t0, 0.6, 0.45))
place(S, swish(0.22, 500, 3500, 5090), 2.0, 0.9, pan=0.4)
place('drums', tom(90, 5091), 2.0, 0.45, room=0.3)
place('ui', tok(5092, 240, 0.9), 2.25, 1.0)
place(S, denied(5100), 2.5, 1.1, room=0.2)
place(S, thump(5101, 1.0, 60), 2.5, 0.9)
place('ui', tok(5102, 200, 0.5), 2.75, 1.0)

# --- REJOUER
nn = ns(0.6); t = tax(nn)
hum = sine(55 + 40 * np.exp(-t / 0.03), nn) * ar(nn, 0.003, 0.12)     # CRT-on: low sine thump, no glide
place(S, hum, 4.0, 0.45)
place(S, impact(5200, 1.1, (110, 36), 105, 1.8, bright=1.2), 4.0, 1.1, hall=0.3)
place(S, hp(noise(ns(0.25), 5201), 2000) * ar(ns(0.25), 0.001, 0.05) * 0.4, 4.0, 1.0)
place('hitd', taiko(60, 1.4, 5202, drive=1.8), 4.0, 0.7, hall=0.2)
DH.append((4.0, 0.6, 0.35))
place(S, swish(0.3, 400, 2500, 5210), 4.5, 0.8)
place('drums', tom(100, 5211), 4.5, 0.45, room=0.3)
place('ui', tok(5212, 280, 0.8), 4.5, 1.0)
place(S, impact(5220, 1.2, (120, 34), 120, 2.4, bright=1.2), 5.0, 1.0, hall=0.4)
place(S, crash(2.2, 5221, 1.0), 5.0, 0.55, hall=0.3)
place('hitd', taiko(56, 1.5, 5222, drive=2.0), 5.0, 0.7, hall=0.3)
DH.append((5.0, 0.6, 0.4))
place(S, whoosh(0.52, 0.5, 200, 6000, -0.3, 0.3, onset=0.3, seed=5230, low=0.7), 5.5, 0.65)
place(S, reverse_swell(0.5, 5231), 5.5, 0.45)
place('drums', tom(85, 5232), 5.75, 0.6, room=0.3)
place(S, swish(0.12, 3000, 800, 5235, 1.0), 5.75, 1.0)
place('drums', taiko(66, 1.0, 5233), 5.5, 0.6, room=0.3)
place(S, swish(0.12, 3500, 900, 5234, 1.2), 5.5, 1.0)

# --- LEVEL 1
place(S, crash(1.6, 5300, 0.7), 6.0, 0.2, hall=0.2)
place(S, swish(0.2, 2500, 600, 5301, 1.0), 6.0, 0.6)
place(S, impact(5310, 1.2, (125, 34), 98, 2.4, bright=1.2), 6.15, 1.35, hall=0.35)
place('hits', braam([29, 36, 41, 48, 53], 1.4, 1.1, 5311), 6.15, 0.95, mhall=0.35)
place('hitd', taiko(55, 1.5, 5312, drive=2.0), 6.15, 0.8, hall=0.3)
DH.append((6.15, 0.7, 0.35, 0.08))
place(S, crash(2.0, 5313, 0.8), 6.15, 0.4, hall=0.25)
place('hitd', taiko(78, 1.0, 5320), 6.375, 0.6, room=0.3)
place(S, crack_hit(5322, 0.08), 6.375, 0.5)
place('ui', tok(5321, 330, 0.4), 6.375, 1.0)
ER = [(7.0, 350), (7.2375, 1500), (7.5, 960), (7.75, 445), (8.0, 1460), (8.25, 715), (8.5, 1540), (8.75, 500)]
for k, (t0, x) in enumerate(ER):
    pan = (x - 960) / 960 * 0.9
    g = 0.65 + 0.05 * k
    place(S, eruption(5400 + k * 10, g, pan, 58 + 1.5 * k), t0, 0.9, room=0.2, hall=0.1)
    place(S, swish(0.1, 3500, 1000, 5480 + k, 1.0, pan), t0, 1.0)
    if k == 1:
        place(S, quench(5490, 0.5), t0, 0.8)
place(S, reverse_swell(0.5, 5500, 1.2), 9.5, 0.7)
place('drums', taiko(60, 1.2, 5501, drive=1.9), 9.5, 0.6, hall=0.2)
place(S, sub_drop(80, 40, 0.5, 0.2), 9.5, 0.4)
place(S, impact(5502, 0.8, (110, 40), 120, 1.0, bright=1.3, metal_amt=0.3), 9.5, 0.8, hall=0.2)


# --- POWER-UPS
def whip(P, seed, pan0=0.8, pan1=-0.8):
    place(S, whoosh(0.53, 0.5, 300, 5500, pan0, pan1, onset=0.3, seed=seed, low=0.6), P - 0.5, 0.85)


def erupt(P, seed, g=1.0):
    place(S, eruption(seed, 1.0 * g, 0.0, 56), P, 1.0, room=0.2, hall=0.2)
    place(S, crack_hit(seed + 7), P, 0.55 * g, room=0.15)
    place(S, sub_drop(100, 32, 0.9, 0.12), P, 0.5 * g)
    DH.append((P, 0.4 * g, 0.3))


def fall(t0, seed, g=1.0):
    # the fall ends 15 ms before the land, so the quench is a clean onset (replaces the old whole-mix pre-suck)
    place(S, whoosh(0.485, 0.47, 400, 3500, 0.0, 0.0, onset=0.35, seed=seed, low=0.5, after=0.012), t0, 0.7 * g)
    place(S, fin(crackle(0.48, 120, seed + 1, 1500, 6000) * np.linspace(0.3, 1, ns(0.48)), 10), t0, 0.5 * g)


STAMP_N = [0]


def stamp(t0, seed, g=1.0, verb=0.35):
    place(S, impact(seed, 0.9, (105, 38), 140, 1.8, bright=1.1, metal_amt=0.3), t0, 1.15 * g, hall=verb)
    place('hitd', snare(seed + 1, 0.4), t0, 0.45 * g, plate=0.4)
    place(S, crash(1.4, seed + 5, dark=0.7), t0, 0.28 * g, hall=0.2)
    ch = chord_at(t0)
    root = ROOT[ch] if ROOT[ch] < 36 else ROOT[ch] - 12
    tn = sorted(CH[ch][:4])
    v = STAMP_N[0] % 3          # rotate the voicing: root position / 1st inversion / open (octave on top)
    STAMP_N[0] += 1
    voic = [tn[0], tn[1], tn[2]] if v == 0 else ([tn[1], tn[2], tn[3]] if v == 1 else [tn[0], tn[3], tn[1] + 12])
    place('hits', braam([root] + voic, 0.8, 1.1, seed + 2), t0, 0.78 * g, mhall=0.35)
    DH.append((t0, 0.75 * g, 0.3, 0.1))
    BPD.append((t0 - 0.02, t0 - 0.001, 0.5))


def counter(t0, seed, g=1.6):
    place('ui', clack(seed, g), t0, 1.0, plate=0.08)


def hop(P, seed):
    place('ui', swish(0.3, 300, 1500, seed, 0.8), P + 3.5, 1.0)
    place('ui', thump(seed + 1, 0.9), P + 4.0, 1.0)


# power-up 1 (10)
place(S, impact(6000, 1.3, (130, 33), 95, 2.4), 10.0, 1.0, hall=0.35)
place(S, crash(2.4, 6001, 1.0), 10.0, 0.55, hall=0.3)
erupt(10.0, 6002)
fall(10.5, 6010)
BPD.append((10.986, 10.998, 0.5)); place(S, quench(6020), 11.0, 0.8, hall=0.2); DH.append((11.0, 0.45, 0.3))
place(S, sheen(6030), 11.14, 0.9)
stamp(11.5, 6040)
place('ui', tok(6050, 300, 0.6), 11.55, 1.0)
for t0 in (12.0, 12.5):
    place('ui', tok(int(t0 * 100), 250, 0.9), t0, 1.0)
counter(12.12, 6060)
place('ui', swish(0.25, 500, 2500, 6070, 0.9), 13.0, 1.0)
place('ui', tok(6071, 280, 0.7), 13.0, 1.0)
nn = ns(0.32)
typ = np.zeros(nn)
for i in range(0, 56, 3):
    o = ns(i * 0.0055)
    typ[o:o + ns(0.004)] += bp(noise(ns(0.004), 6080 + i), 1800, 6000) * np.hanning(ns(0.004)) * 0.25
place('ui', typ, 13.5, 0.8)
hop(10.0, 6090)
whip(15.0, 6095)

# power-up 2 (15)
erupt(15.0, 6100)
fall(15.5, 6110)
BPD.append((15.986, 15.998, 0.5)); place(S, quench(6120), 16.0, 0.8, hall=0.2); DH.append((16.0, 0.45, 0.3))
for i, tb in enumerate([16.1, 16.163, 16.225, 16.288, 16.35, 16.413, 16.475, 16.538]):
    place('ui', hp(noise(ns(0.03), 6130 + i), 2500) * ar(ns(0.03), 0.004, 0.008) * 0.08, tb, 1.0, pan=-0.6 + 0.17 * i)
place(S, sheen(6140), 16.14, 1.0)
stamp(16.5, 6150)
place('ui', tok(6160, 260, 1.0), 17.0, 1.0)
place('ui', swish(0.3, 500, 3000, 6161, 0.9), 17.063, 1.0)
counter(17.12, 6170)
place('ui', swish(0.28, 700, 2200, 6180, 0.8, 0.4), 17.5, 1.0)
place('ui', swish(0.28, 700, 2200, 6181, 0.8, -0.4), 18.0, 1.0)
place('ui', swish(0.3, 2600, 700, 6182, 0.5), 18.5, 1.0)
hop(15.0, 6190)
whip(20.0, 6195)

# power-up 3 (20) map
erupt(20.0, 6200)
nn = ns(0.5); t = tax(nn)
grind = bp(noise(nn, 6210), 120, 900) * (1 + 0.8 * np.sign(np.sin(2 * np.pi * 37 * t))) * 0.5
grind = grind * ar(nn, 0.004, 0.25)
place(S, stereo(grind) + whoosh(0.5, 0.45, 200, 1500, 0, 0, 0.4, 6211, 0.7) * 0.6, 20.5, 0.8)
place(S, impact(6220, 0.7, (90, 38), 90, 1.2, bright=0.6, metal_amt=0.2), 21.0, 0.7, hall=0.15)
for i, t0 in enumerate([21.0, 21.25, 21.5, 21.75, 22.0, 22.25]):
    place('ui', thump(6230 + i, 0.55, 120), t0, 1.0)
stamp(21.5, 6250)
place('ui', tok(6260, 320, 0.7), 22.0, 1.0)
counter(22.12, 6270)
place('ui', tok(6280, 260, 1.0), 22.5, 1.0)
place('ui', swish(0.18, 600, 2400, 6281, 0.9), 22.56, 1.0)
place('ui', tok(6282, 340, 1.2), 22.56, 1.0)
place(S, crack_hit(6283, 0.06), 22.56, 0.4)       # pin pop: short broadband snap clear of the 22.5 backbeat
place('ui', swish(0.4, 400, 1800, 6290, 0.7), 23.0, 1.0)
place('ui', tok(6291, 240, 0.8), 23.0, 1.0)
for i, t0 in enumerate([23.5, 23.75, 24.0]):
    nn = ns(0.5); t = tax(nn)
    son = sine(70 + 20 * np.exp(-t / 0.05), nn) * ar(nn, 0.003, 0.12) + bp(noise(nn, 6300 + i), 300, 1500) * ar(nn, 0.002, 0.03) * 0.5
    place('ui', son, t0, 0.45 - 0.12 * i, room=0.4)
whip(25.0, 6310)

# power-up 4 (25) planning
erupt(25.0, 6400)
place(S, whoosh(0.26, 0.25, 400, 3000, -0.9, 0.0, 0.2, 6401, 0.3), 25.0, 0.6)
place(S, whoosh(0.26, 0.25, 400, 3000, 0.9, 0.0, 0.2, 6402, 0.3), 25.0, 0.6)
place(S, impact(6410, 1.0, (120, 40), 160, 1.8, bright=1.3, metal_amt=0.6), 25.25, 1.0, hall=0.3)
place(S, crash(1.6, 6411, 0.9), 25.25, 0.4, hall=0.2)
DH.append((25.25, 0.5, 0.3))
place('ui', swish(0.36, 300, 2600, 6420, 1.0), 25.5, 1.0)
place('ui', tok(6421, 250, 0.7), 25.5, 1.0)
place(S, sub_drop(70, 35, 0.6, 0.2), 26.0, 0.3)
stamp(26.5, 6430)
for i, t0 in enumerate([27.0, 27.5, 28.0]):
    place('ui', thump(6445 + i, 0.5, 140), t0, 1.0)
counter(27.12, 6450)
place(S, impact(6460, 0.8, (110, 40), 150, 1.4, bright=1.0, metal_amt=0.3), 28.5, 0.85, hall=0.25)
place('ui', tok(6461, 300, 1.0), 28.5, 1.0)
DH.append((28.5, 0.45, 0.25))
place('ui', swish(0.4, 300, 1400, 6462, 0.6), 28.5, 1.0)
place('ui', thump(6463, 1.0), 29.0, 1.0)
whip(30.0, 6470)

# power-up 5 (30) food
erupt(30.0, 6500)
for i, t0 in enumerate([30.5, 30.75, 31.0, 31.25]):
    place('ui', tok(6510 + i, 260 + 20 * i, 0.9), t0, 1.0)
for i, t0 in enumerate([31.0, 31.25, 31.5, 31.75]):
    place(S, whoosh(0.07, 0.06, 800, 3000, 0, 0, 0.5, 6520 + i, 0.3), t0 - 0.06, 0.35)
    place(S, impact(6530 + i, 0.6, (100, 42), 110, 0.8, bright=0.7, metal_amt=0.15), t0, 0.55 + 0.1 * (i == 3), hall=0.1)
stamp(31.5, 6540)
place('ui', swish(0.34, 2400, 500, 6550, 1.0), 32.0, 1.0)
counter(32.12, 6560)
for i, t0 in enumerate([32.5, 33.0, 33.5]):
    place('ui', swish(0.25, 500, 2200, 6570 + i, 0.8, 0.3), t0, 1.0)
    place('ui', tok(6575 + i, 280, 0.8), t0, 1.0)
for i, t0 in enumerate([32.02, 32.52, 33.02, 33.52]):
    place('ui', tok(6580 + i, 380, 0.35, 0.5), t0, 1.0)
place('ui', thump(6590, 1.0), 34.0, 1.0)
place('ui', tok(6591, 300, 0.6), 34.0, 1.0)
whip(35.0, 6595)

# power-up 6 (35) cashless
erupt(35.0, 6600)
fall(35.5, 6610)
BPD.append((35.986, 35.998, 0.5)); place(S, quench(6620, 1.05), 36.0, 0.75, hall=0.2); place(S, crack_hit(6625), 36.0, 0.45, room=0.15); DH.append((36.0, 0.5, 0.3))
place(S, sheen(6630), 36.12, 1.0)
stamp(36.5, 6640, 1.15)
nn = ns(0.4); t = tax(nn)        # RECHARGE: band-passed noise swept 300 -> 1200 Hz, no pitched oscillator
chg = tvf(np.vstack([noise(nn, 6645), noise(nn, 6646)]), 300 * 4 ** (t / 0.4), q=1.2, kind='band')
place(S, fin(chg * ar(nn, 0.01, 0.15) * 1.2, 20), 36.5, 0.5)
for i, t0 in enumerate([37.0, 37.5, 38.0]):
    place('ui', tok(6650 + i, 300, 1.0), t0, 1.0)
counter(37.12, 6660)
place('ui', swish(0.3, 600, 2000, 6670, 0.8), 38.5, 1.0)
place('ui', thump(6680, 1.0), 39.0, 1.0)
place('ui', tok(6681, 320, 0.7), 39.0, 1.0)
place(S, whoosh(0.54, 0.5, 300, 5500, 0.8, -0.8, onset=0.3, seed=6690, low=0.6), 39.5, 0.8)

# breakdown (40)
place(S, eruption(6700, 0.6, 0.0, 52), 40.0, 0.8, hall=0.35)
place(S, whoosh(0.5, 0.49, 300, 2200, 0, 0, 0.3, 6710, 0.5), 40.5, 0.5)
place('ui', swish(0.15, 3000, 800, 6711, 0.3), 40.5, 1.0)
place(S, crackle(0.3, 200, 6712, 1200, 6000, decay=0.08), 40.5, 0.7)
place(S, thump(6720, 1.2, 70), 41.0, 1.0, room=0.3)
place(S, steam(0.6, 6721, 0.6), 41.0, 0.6)
place('ui', tok(6722, 300, 1.0), 41.0, 1.0)
stamp(41.5, 6740, 0.9, verb=0.6)
place('ui', tok(6745, 260, 0.4), 41.5, 1.0)
place('ui', tok(6750, 280, 1.0), 42.0, 1.0)
counter(42.12, 6760, 0.9)
for i, t0 in enumerate([42.5, 42.75, 43.0, 43.5]):
    place('ui', tok(6770 + i, 300 + 20 * i, 0.65), t0, 1.0)
place('ui', thump(6780, 0.8, 110), 43.0, 1.0)
place('ui', swish(0.08, 1500, 600, 6781, 0.6), 44.5, 1.0)
place(S, whoosh(0.52, 0.5, 300, 6000, 0.8, -0.8, onset=0.3, seed=6790, low=0.7), 44.5, 0.8)

# build (45)
place(S, impact(6800, 1.2, (120, 34), 100, 2.4), 45.0, 1.0, hall=0.35)
place('hits', braam([25, 37, 44, 49, 53], 1.6, 1.0, 6801), 45.0, 0.5, mhall=0.35)
place(S, crash(2.0, 6802, 0.8), 45.0, 0.45, hall=0.3)
DH.append((45.0, 0.55, 0.35))
place('ui', swish(0.26, 400, 2200, 6810, 0.9), 45.5, 1.0)
place('ui', tok(6811, 260, 0.6), 45.5, 1.0)
for i in range(18):
    tb = 45.75 + i * 0.04
    place('ui', tok(6820 + i, 400 + 30 * (i % 3), 0.28 if i else 1.0, 0.6), tb, 1.0)
stamp(46.5, 6840)
place(S, whoosh(0.2, 0.05, 3000, 600, 0.0, 0.0, 0.6, 6841, 0.2, after=0.12), 46.5, 0.5)
place('ui', tok(6850, 260, 1.0), 47.0, 1.0)
place('ui', swish(0.15, 600, 2000, 6851, 0.6), 47.0, 1.0)
counter(47.12, 6860)
for i, t0 in enumerate([47.5, 47.75, 48.0, 48.25]):
    place('ui', tok(6870 + i, 290 + 15 * i, 0.9), t0, 1.0)
place('ui', tok(6880, 250, 0.9), 48.5, 1.0)
place('ui', swish(0.1, 3000, 900, 6881, 0.5), 48.5, 1.0)
place(S, sub_drop(60, 30, 1.0, 0.6), 49.0, 0.4)
place('drums', taiko(56, 1.0, 6890, drive=1.8), 49.0, 0.9, room=0.3)
place(S, impact(6892, 0.7, (100, 40), 130, 1.0, bright=1.3, metal_amt=0.3), 49.0, 0.8, hall=0.2)
place('drums', taiko(70, 1.0, 6893, drive=1.8), 49.5, 0.7, room=0.3)
PD.append((49.475, 49.498, 0.4))
place(S, impact(6894, 0.6, (90, 40), 150, 0.8, bright=1.4, metal_amt=0.25), 49.5, 0.7, hall=0.2)
place(S, reverse_swell(0.44, 6891, 1.3), 49.5, 0.55)

# DROP
place(S, impact(7000, 1.5, (140, 40), 90, 2.8, bright=1.5, metal_amt=0.45, subdec=0.4), 50.0, 1.0, hall=0.4)
place(S, crash(3.0, 7001, 1.0), 50.0, 0.7, hall=0.3)
place(S, sub_drop(110, 30, 1.8, 0.3), 50.0, 0.45)
DH.append((50.0, 0.4, 0.3))
place('post', fire_burst(0.6, 7010, 1.0), 50.075, 0.6)
place('post', crackle(0.6, 300, 7011, 800, 6000, decay=0.18), 50.075, 0.9)
place('post', swish(0.1, 4000, 1500, 7012, 1.5), 50.075, 0.6)
place('post', impact(7020, 1.0, (120, 38), 130, 1.6, bright=1.8, metal_amt=0.45), 50.125, 0.75)
place('post', snare(7021, 0.4), 50.125, 0.5)
place('post', swish(0.1, 4500, 1500, 7022, 1.5), 50.125, 0.6)
for i, tb in enumerate([50.507, 50.522, 50.539, 50.559, 50.582, 50.612, 50.656]):
    place('ui', tok(7030 + i, 350, (1.6 if i == 0 else 0.5 + 0.08 * i), 0.7), tb, 1.0)
place(S, impact(7040, 1.0, (120, 45), 120, 1.8, bright=1.2, metal_amt=0.45, subdec=0.14), 50.875, 1.3, hall=0.3)
place(S, crash(1.6, 7042, 0.9), 50.875, 0.45, hall=0.25)
place(S, crackle(0.5, 200, 7041, 900, 6000, decay=0.15), 50.875, 0.5)
DH.append((50.875, 0.8, 0.3, 0.15))
BPD.append((50.835, 50.874, 0.4))
place(S, whoosh(0.5, 0.1, 6000, 250, 0.0, 0.0, onset=0.6, seed=7050, low=0.9, after=0.12), 51.5, 0.6)
place('ui', thump(7060, 1.2, 100), 51.7625, 1.0)
place('ui', tok(7061, 320, 1.2, 1.2), 51.7625, 1.0)
place(S, crack_hit(7062, 0.1), 51.7625, 0.55, room=0.15)     # lava pops at the goal: short broadband crack, not a UI sound
for i, tb in enumerate([51.925, 52.075, 52.225, 52.375, 52.525, 52.675]):   # hops: rimshot-like accents only
    rim = hp(noise(ns(0.05), 7080 + i), 3000, 2) * ar(ns(0.05), 0.0004, 0.006)
    place('ui', fin(rim), tb, 0.6, pan=0.3 * (1 if i % 2 else -1))
    place('ui', tok(7070 + i, 360, 0.6, 1.0), tb, 1.0)
place(S, impact(7090, 0.7, (110, 40), 140, 1.2, bright=1.4, metal_amt=0.3), 52.8125, 0.7, hall=0.25)
place(S, crackle(0.4, 220, 7091, 900, 6000, decay=0.12), 52.8125, 0.5)
place(S, crack_hit(7092), 52.8125, 0.6, room=0.2)
DH.append((52.8125, 0.35, 0.18))
for k, t0 in enumerate([53.0, 53.5]):
    place(S, whoosh(0.11, 0.1, 600, 4000, 0.6 - 1.2 * k, 0, 0.3, 7100 + k, 0.3), t0 - 0.1, 0.5)
    place(S, impact(7110 + k, 1.1, (125, 45), 110 + 15 * k, 1.8, bright=1.3, metal_amt=0.45, subdec=0.14), t0, 1.35, hall=0.3)
    place(S, crash(1.6, 7115 + k, 0.9), t0, 0.45, hall=0.25)
    DH.append((t0, 0.82, 0.3, 0.18))     # stop-time: the bed drops out under each tagline slam
    BPD.append((t0 - 0.02, t0 - 0.001, 0.5))

# END
place(S, crash(2.4, 7200, 0.5), 54.0, 0.35, hall=0.4)
place(S, impact(7201, 0.6, (90, 36), 110, 1.2, bright=0.9, metal_amt=0.2), 54.0, 0.6, hall=0.4)
place('ui', swish(0.2, 3500, 900, 7202, 0.5), 54.0, 1.0)
place(S, sub_drop(70, 34, 1.4, 0.4), 54.0, 0.45)
place('ui', whoosh(0.4, 0.35, 300, 3500, -0.4, 0.4, 0.3, 7210, 0.4), 55.25, 0.6)
place('ui', swish(0.2, 600, 3000, 7211, 0.7), 55.25, 1.0)
place('ui', tok(7212, 280, 0.7), 55.25, 1.0)
place(S, crack_hit(7213, 0.06), 55.25, 0.3)
place(S, whoosh(0.52, 0.5, 400, 5000, 0.6, -0.2, 0.3, 7220, 0.6), 55.5, 0.8)
place('ui', swish(0.14, 3500, 900, 7221, 0.6), 55.5, 1.0)
place('ui', tok(7222, 240, 1.0), 55.5, 1.0)
place(S, impact(7230, 1.2, (125, 34), 100, 2.4, bright=1.2), 56.0, 1.0, hall=0.4)
place('hits', braam([25, 37, 44, 49, 51, 56], 1.6, 1.0, 7231), 56.0, 0.7, mhall=0.4)
place(S, crash(2.2, 7232, 0.8), 56.0, 0.45, hall=0.3)
DH.append((56.0, 0.5, 0.35))
place('ui', swish(0.3, 500, 2600, 7240, 0.9), 56.5, 1.0)
place('ui', tok(7241, 260, 0.6), 56.5, 1.0)
place('ui', tok(7250, 300, 1.0), 57.0, 1.0)
place('ui', tok(7251, 320, 1.0), 57.25, 1.0)
place(S, impact(7260, 0.7, (100, 40), 150, 1.2, bright=1.0, metal_amt=0.25), 57.75, 0.5, hall=0.25)
place(S, impact(7270, 0.8, (110, 38), 120, 1.4, bright=1.0, metal_amt=0.3), 58.0, 0.55, hall=0.3)
place('ui', tok(7271, 280, 0.8), 58.0, 1.0)
place('ui', swish(0.2, 800, 2000, 7272, 0.4), 58.725, 1.0)
place(S, reverse_swell(0.5, 7280, 1.2), 58.5, 0.45)
# FINAL HIT 59.0
place('hits', braam([29, 36, 41, 44, 48, 53, 56], 1.0, 1.6, 7300, growl=0.18, edec=0.6, sub_amt=0.25), 59.0, 1.25, hall=0.6)
place(S, impact(7301, 1.2, (140, 32), 88, 2.0, bright=1.5, metal_amt=0.4, subdec=0.4), 59.0, 1.0, hall=0.5)
place(S, crash(2.4, 7302, 1.0), 59.0, 0.85, hall=0.4)
place(S, crack_hit(7304, 0.15), 59.0, 0.7, room=0.2, hall=0.3)
place(S, sub_drop(120, 29, 0.7, 0.25), 59.0, 0.35)    # fewer stacked subs: headroom goes to the braam
place('hitd', drop_kick(7303), 59.0, 1.0)
for k, f0 in enumerate([52, 66, 84]):
    place('hitd', taiko(f0, 1.0, 7310 + k, drive=2.0), 59.0 + 0.004 * k, 0.7, hall=0.3, pan=(k - 1) * 0.5)
place('ui', tok(7320, 260, 0.8), 59.0, 1.0)
DH.append((59.0, 0.75, 1.5, 0.1))     # duck never recovers before 60.0: the hit decays
PD.append((58.93, 58.998, 0.12))

# ===================================================================================== MIX
print('mix...  %.1fs' % (time.time() - T_START))


def duck_env(events, n):
    e = np.ones(n)
    for ev in events:
        t0, depth, rel = ev[:3]
        hold = ev[3] if len(ev) > 3 else 0.012
        i = ns(t0)
        L = ns(rel + hold + 0.01)
        tt = tax(L)
        a = np.clip(tt / 0.003, 0, 1)
        r = np.clip((tt - hold) / rel, 0, 1)
        g = depth * a * (1 - r * r * (3 - 2 * r))
        j = min(N, i + L)
        e[i:j] = np.minimum(e[i:j], 1 - g[:j - i])
    return e


def make_ir(dur, t60, f0, f1, seed, pre=0.02):
    n = ns(dur); t = tax(n)
    x = np.vstack([noise(n, seed), noise(n, seed + 1)])
    x = tvf(x, f1 + (f0 - f1) * np.exp(-t / (t60 / 4)), q=0.5, blk=256)
    x *= 10 ** (-3 * t / t60) * np.clip(t / 0.01, 0, 1)
    x = hp(x, 140)
    x /= np.sqrt((x ** 2).sum(1, keepdims=True))
    return np.hstack([np.zeros((2, ns(pre))), x])


def conv(x, ir):
    return np.vstack([oaconvolve(x[c], ir[c])[:N] for c in range(2)])


IR = {'v_mhall': make_ir(3.2, 2.8, 7000, 1800, 9001, 0.03), 'v_hall': make_ir(3.8, 3.4, 9000, 2000, 9003, 0.025),
      'v_plate': make_ir(1.6, 1.3, 11000, 4000, 9005, 0.01), 'v_room': make_ir(0.8, 0.6, 8000, 2500, 9007, 0.005)}
BUS['v_room'] = hp(BUS['v_room'], 80, 2)     # keep taiko / tom room sends out of the low end
RET = {k: conv(BUS[k], IR[k]) for k in IR}

dk = duck_env(DK, N)
dh = duck_env(DH, N)

# section filter automation on the music bus (evolving filters)
fc_pts = [(0, 1800), (1.0, 6000), (2.0, 3000), (4, 1500), (5.0, 5000), (6, 3500), (9, 3000), (10, 3000), (10.1, 4500),
          (18, 7000), (26, 9000), (34, 12000), (40, 3000), (45, 2500), (49.9, 14000), (50, 16000), (54, 16000), (60, 16000)]
fcm = np.interp(tax(N), [p[0] for p in fc_pts], [p[1] for p in fc_pts])
music = tvf(BUS['music'], fcm, q=0.7, blk=128)
# the big-hit duck applies to the BED only; the music hall return gets half its depth (tails are not pumped shut)
music = (music * dh[None] + RET['v_mhall'] * 0.9 * (0.5 + 0.5 * dh)[None]) * (dk * 0.85 + 0.15 * 1.0)[None]
TS = tax(N)
# width automation: 1.0 in the hook and on the end card (mono-safe), 1.05 in the breakdown, 1.15 in the grooves
wid = np.interp(TS, [0, 3.98, 4.0, 39.97, 40.0, 44.97, 45.0, 53.97, 54.0, 62],
                [1.0, 1.0, 1.15, 1.15, 1.05, 1.05, 1.15, 1.15, 1.0, 1.0])
mm, sd = (music[0] + music[1]) / 2, (music[0] - music[1]) / 2
music = np.vstack([mm + wid * sd, mm - wid * sd])
bass = BUS['bass'] * (1 - (1 - dk) * 1.25).clip(0.1, 1)[None] * dh[None]
bass = lp(bass, 2200, 4)    # no bass harmonics poking out above 2 kHz
bass = np.vstack([bass.mean(0)] * 2)  # mono low end

drums = BUS['drums']
comp = Compressor(threshold_db=-22, ratio=6, attack_ms=2, release_ms=90)
dpar = comp(drums.astype(np.float32), SR).astype(float)
drums = drums + 0.45 * dpar
drums = np.tanh(drums * 1.1) / 1.1
drums = drums * (0.4 + 0.6 * dh)[None]       # bed drums only now (hit taikos / kick live on 'hitd')
drums = PeakFilter(250, -2.5, 0.9)(drums.astype(np.float32), SR).astype(float)    # de-mud the taiko / tom low-mids

# hit layers: never side-chained, never ducked, no section gain
hits = lp(BUS['hits'], 1500, 4)     # braam saw harmonics above ~2 kHz read as tonal 'beeps': the crash / crack carry the top
hitd = BUS['hitd']
hcomp = Compressor(threshold_db=-20, ratio=4, attack_ms=4, release_ms=120)
hitd = hitd + 0.35 * hcomp(hitd.astype(np.float32), SR).astype(float)
hitd = np.tanh(hitd * 1.1) / 1.1

sfx = BUS['sfx']
ui = BUS['ui']

G = {'drums': 0.85, 'bass': 0.5, 'music': 1.5, 'sfx': 0.75, 'ui': 0.75, 'hall': 0.55, 'plate': 0.36, 'room': 0.35,
     'hits': 1.5, 'hitd': 1.0}
# section gain on the groove (music / bass / drums): the power-ups and the build must not sag under the hits
# every step is a 25 ms ramp that ends on the downbeat. The drop gets the most section gain of the film.
sg = np.interp(TS, [0, 9.975, 10.0, 39.975, 40.0, 44.975, 45.0, 49.9, 49.975, 50.0, 53.975, 54.0, 62],
               [1.0, 1.0, 1.55, 1.55, 1.0, 1.0, 1.05, 1.0, 1.0, 1.22, 1.22, 1.05, 1.05])
sgm = sg * np.interp(TS, [0, 39.975, 40.0, 44.975, 45.0, 62], [1, 1, 0.55, 0.55, 1, 1])
drums = drums * sg[None]
bass = bass * sg[None]
music = music * sgm[None]
# bed-only pre-hit micro-sucks (stamps, quench lands, taglines): short dips of the groove, never of the SFX / hits
bpd = np.ones(N)
for a, b_, dep in BPD:
    i0, i1 = ns(a), ns(b_)
    f = ns(0.003)
    bpd[i0:i1] = np.minimum(bpd[i0:i1], dep)
    bpd[i0 - f:i0] = np.minimum(bpd[i0 - f:i0], np.linspace(1, dep, f))
    bpd[i1:i1 + f] = np.minimum(bpd[i1:i1 + f], np.linspace(dep, 1, f))
drums, bass, music = drums * bpd[None], bass * bpd[None], music * bpd[None]


def softclip(x, thr):
    """2x-oversampled tanh clipper (linear-phase resampling: no latency). Trailer-style hit bus clipping:
    shaves the crack transients so the master limiter does not pull the whole hit down."""
    up = resample_poly(x, 2, 1, axis=1)
    return resample_poly(thr * np.tanh(up / thr), 1, 2, axis=1)


hitgrp = softclip(sfx * G['sfx'] + hits * G['hits'] + hitd * G['hitd'], 100.0)
pre = (drums * G['drums'] + bass * G['bass'] + music * G['music'] + hitgrp + ui * G['ui']
       + RET['v_hall'] * G['hall'] + RET['v_plate'] * G['plate'] + RET['v_room'] * G['room'])

if os.environ.get('STEMS_OUT'):      # debug: dump the gained stems for measurement
    np.savez(os.environ['STEMS_OUT'], drums=(drums * G['drums']).astype(np.float32), bass=(bass * G['bass']).astype(np.float32),
             music=(music * G['music']).astype(np.float32), sfx=(sfx * G['sfx']).astype(np.float32),
             ui=(ui * G['ui']).astype(np.float32), hits=(hits * G['hits'] + hitd * G['hitd']).astype(np.float32),
             rev=(RET['v_hall'] * G['hall'] + RET['v_plate'] * G['plate'] + RET['v_room'] * G['room']).astype(np.float32))
for a, b_, dep in PD:
    g = np.ones(N)
    i0, i1 = ns(a), ns(b_)
    g[i0:i1] = dep
    f = ns(0.004)
    g[i0 - f:i0] = np.linspace(1, dep, f)
    g[i1:i1 + f] = np.linspace(dep, 1, f)
    pre *= g[None]

# ---- tape rewind 3.0-3.75 built from the hook mix (1.0 -> 3.0 read backwards, accelerating), then CRT off
seg = pre[:, ns(1.0):ns(3.0)].copy()
nr = ns(0.75); tr = tax(nr)
k_ = (2.0 - 0.75) / (0.75 / 2.5)
rate = 1 + k_ * (tr / 0.75) ** 1.5
pos = 2.0 - np.cumsum(rate) / SR
pos = np.clip(pos, 0, 2.0 - 1 / SR) * SR
rew = np.vstack([np.interp(pos, np.arange(seg.shape[1]), seg[c]) for c in range(2)])
rew = lp(hp(rew, 160), 1500, 4) * 0.6
rew += np.vstack([hp(noise(nr, 9103), 2500, 2), hp(noise(nr, 9104), 2500, 2)]) * 0.05 * np.clip(tr / 0.02, 0, 1)
rew *= np.clip(tr / 0.01, 0, 1)
rew += np.vstack([bp(noise(nr, 9101), 300, 2200), bp(noise(nr, 9102), 300, 2200)]) * 0.05 * (tr / 0.75)
gate = np.ones(N)
a, b_ = ns(3.0), ns(4.0)
gate[a:b_] = 0.0
gate[a - ns(0.01):a] = np.linspace(1, 0, ns(0.01))
pre *= gate[None]
place('post', rew, 3.0, 1.0)
place('post', tok(9110, 160, 1.4), 3.0, 1.0)
place('post', thump(9111, 1.4, 70), 3.0, 0.9)
nn = ns(0.35); t = tax(nn)
zap = tvf(np.vstack([noise(nn, 9120), noise(nn, 9121)]), 6000 * np.exp(-t / 0.05) + 80, q=1.2, kind='band') * 2.5
zap *= ar(nn, 0.002, 0.08)
zap += stereo(sine(30 + 90 * np.exp(-t / 0.04), nn) * ar(nn, 0.002, 0.12) * 0.9)
place('post', zap, 3.75, 0.55)
place('post', crackle(0.25, 200, 9122, 1500, 7000, decay=0.05), 3.75, 0.4)
place('post', crackle(0.1, 150, 9123, 2000, 7000, decay=0.02), 3.888, 0.25)
post = BUS['post'] + conv(BUS['post'], IR['v_room']) * 0.25 + conv(BUS['post'], IR['v_hall']) * 0.3
mix = pre + post

# drop/suck: 60 ms silence before the drop and a 40 ms suck before 10.0 (music only, the reverse swells end there)
for t0, t1 in [(49.94, 50.0), (9.965, 10.0)]:
    g = np.ones(N)
    i0, i1 = ns(t0), ns(t1)
    g[i0:i1] = 0.03
    g[i0 - ns(0.006):i0] = np.linspace(1, 0.03, ns(0.006))
    mix *= g[None]

mix = hp(mix, 22, 2)

# glue
mix = mix / (np.abs(mix).max() + 1e-9) * 0.5
glue = Compressor(threshold_db=-16, ratio=1.6, attack_ms=30, release_ms=160)   # slow attack: hit onsets pass
mix = glue(mix.astype(np.float32), SR).astype(float)

# M/S after the glue (so nothing downstream re-creates low side): low end mono (side 4th-order HP 130 Hz), width
mid = (mix[0] + mix[1]) / 2
side = (mix[0] - mix[1]) / 2
side = hp(side, 130, 4) * wid[:N]
mix = np.vstack([mid + side, mid - side])
mix = mix[:, :NOUT]


def limiter(x, ceil):
    out = x
    for la in (0.02, 0.0015):
        L = max(1, ns(la))
        pk = np.abs(out).max(0)
        gr = np.maximum(0, 1 - ceil / np.maximum(pk, 1e-12))      # needed reduction (fraction)
        gr = maximum_filter1d(gr, 2 * L + 1)
        gr = uniform_filter1d(gr, 2 * L + 1)
        out = out * (1 - gr)[None]
    return out


def master_clip(x, thr, knee=0.8):
    """2x-oversampled soft-knee clipper ahead of the limiter: shaves the few-ms crack / kick transients so the
    look-ahead limiter does not pull 40-80 ms of every slam down (hits keep their loudness)."""
    up = resample_poly(x, 2, 1, axis=1)
    a = knee * thr
    m = np.abs(up).max(0)              # stereo-linked: same gain on L and R, so no new (low-frequency) side content
    g = np.ones_like(m)
    over = m > a
    g[over] = (a + (thr - a) * np.tanh((m[over] - a) / (thr - a))) / m[over]
    return resample_poly(up * g[None], 1, 2, axis=1)


def true_peak(x):
    return max(np.abs(resample_poly(c, 4, 1)).max() for c in x)


meter = pyln.Meter(SR)
gain = 1.0
fade = np.ones(NOUT)
fade[-ns(0.3):] = np.cos(np.linspace(0, np.pi / 2, ns(0.3))) ** 2
for it in range(5):
    y = limiter(master_clip(mix * gain, 10 ** (-1.0 / 20)), 10 ** (-1.35 / 20))
    y = y * fade[None]
    tp = true_peak(y)
    if tp > 10 ** (-1.05 / 20):
        y *= 10 ** (-1.05 / 20) / tp
    L = meter.integrated_loudness(y.T)
    print(f'  loudness pass {it}: gain {gain:.3f}  LUFS {L:.2f}  TP {20 * np.log10(true_peak(y)):.2f}')
    if abs(L + 14.0) < 0.15:
        break
    gain *= 10 ** ((-14.0 - L) / 20)

if os.environ.get('STEMS_OUT'):      # debug: limiter gain reduction
    np.save(os.environ['STEMS_OUT'] + '_prelim.npy', (mix * gain).astype(np.float32))
y = y - y.mean(1, keepdims=True)
y = np.clip(y, -1, 1)
assert y.shape == (2, NOUT)
out = os.path.join(HERE, 'mix.wav')
sf.write(out, y.T.astype(np.float32), SR, subtype='PCM_16')
print('wrote', out, y.shape, 'render %.1f s' % (time.time() - T_START))
