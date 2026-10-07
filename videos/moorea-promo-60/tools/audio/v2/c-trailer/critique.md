# Critique, round 2: direction C "trailer hybrid" (revision 2 of mix.wav / mix.mp3)

Reviewer: senior music supervisor / mix engineer. I judged this from the code and from measurements, without listening. I re-rendered a scratch copy of compose.py with STEMS_OUT set, and it is bit-identical to the delivered mix.wav.

## Measurements
- analyze.py: -14.03 LUFS, -1.05 dBTP, 2,880,000 samples, DC about 0, no click candidates.
- 3 high tonal "beeps" (1.91 / 3.86 / 55.83 s). All are braam / pad harmonics, so the toy markers are gone (the old mix had 332).
- MP3: 320 kbps, -14.2 LUFS (ffmpeg), -1.3 dBTP.
- Sync: 280 cues, median offset 4 ms. All 32 weight-3 cues are within -8.0..+1.3 ms.
  - Weight-2 cues: 0.000 is weak, as the analyser expects. 6.0 is at -21 ms and 41.0 at -24 ms; both are whoosh peaks arriving slightly early, still inside ±40 ms.
- Sections:

| section | LUFS | LUFS after 180 Hz HP (phone) | mono fold | crest | corr |
|---|---|---|---|---|---|
| hook | -14.7 | -16.8 | -1.8 | 14.6 | 0.53 |
| level | -15.2 | -18.8 | -1.2 | 13.8 | 0.65 |
| power-ups | -13.9 | -16.4 | -1.4 | 13.7 | 0.59 |
| breakdown | -19.2 | -21.6 | -1.8 | 18.8 | 0.47 |
| build | -14.7 | -17.4 | -1.4 | 13.8 | 0.70 |
| drop | -10.8 | -12.9 | -2.0 | 10.5 | 0.46 |
| end | -14.4 | -16.6 | -1.5 | 14.0 | 0.57 |

  The round-1 fix worked: the drop now reads on small speakers, 4.5 dB above the build after the HP. Mono compatibility is fine.

- **Big-moment contrast** (peak 400 ms momentary loudness at the hit minus the median of the 2 s before it):

| cue | contrast |
|---|---|
| GAME (1.0) | +5.2 LU |
| OVER (1.5) | +3.2 LU |
| CRT-ON (4.0) | **-0.6** |
| PRESS (5.0) | +3.2 |
| NIVEAU (6.15) | **+0.3** |
| stamps 11.5 / 16.5 / 21.5 / 26.5 / 31.5 / 36.5 | +0.9 / +1.2 / +1.5 / **+0.4** / +1.4 / +1.4 |
| 45.0 | +7.6 |
| 46.5 | **+0.6** |
| drop 50.0 | +4.2 |
| 50.875 | **-0.5** |
| taglines 53.0 / 53.5 | **+0.6 / +0.6** |
| 56.0 | +3.2 |
| FINAL HIT 59.0 | **+0.3** |

  - The loudest momentary window of the film is at **49.525** (-9.1 LUFS, the end of the build). The drop at 50.0 peaks at -10.0.
- **Music stem right at the hits** (RMS 0-50 ms after the hit vs 150-300 ms after):
  - 50.0: -7.2 vs -0.4
  - 53.0: -9.3 vs -0.5 (it was -2.9 just *before* the slam)
  - 53.5: -9.7 vs -1.9 (it was -1.3 before)
  - 56.0: -12.3 vs -3.9
  - 59.0: -8.4, against -4.3 before the hit

  So the music bus, which carries the braams, *drops* at the slam and swells in about 150 ms late.
- **Drop micro-structure** (10 ms RMS):
  - The riser runs at -10..-12 dB from 49.6 to 49.93, then silence from 49.94 (good).
  - 50.00: -12; 50.02-50.06: -16; **50.09-50.11: -19**; 50.13: -10.
  - So the drop hit lasts about 20 ms and is chopped by two holes before the 50.125 slam.
- **Final ring-out**: 59.0 at -12.5 dB, 59.7 at -24.1 (-11.6 dB), 59.95 at -58. It decays now. But after the 180 Hz HP the hit is -18.0 against -19.0 for the snare pickup before it: only 1 dB of hit.
- **UI**: 104 UI events, median 10.4 dB under the music + drums + bass bed. These are the loud exceptions:

| time | cue / sound | vs bed |
|---|---|---|
| 40.517 | swish | **+3.1 dB** (breakdown) |
| 18.50 | | -0.9 |
| 55.51 | | -1.4 |
| 48.50 | tok g 1.8 | -2.1 |
| 42.12 | | -3.0 |
| 51.76 | | -4.5 |

- Low end, per stem: in the power-ups the SFX bus (sub drops / impacts / eruptions) carries as much <60 Hz as the drums (-12.3 / -12.4). The pitched bass stem is 5 dB lower (-17.4), so the low end is mostly unpitched hit energy. The music stem is as loud at 60-250 Hz as at 250 Hz-2 kHz (-11.9 / -11.4), so the low-mids are thick.

## What is now right (keep it)
- There is nothing childish left: no square or pulse waves, no coins, bells, boings, plops or sparkles, and no major jingle.
- The UI sounds are noise "toks" with a low body. The game feel comes from braams, impacts, the tape rewind built from the real mix, and the CRT off/on.
- The harmony is consistently F minor: Gb phrygian colour, C as the harmonic-minor dominant, and a modal end (Fsus2-Fm / Db add9 / Ebsus4-Eb / Fm).
- Low end is mono, the stereo is wide but folds to mono well, the drop now lands on phones, and the final hit decays.
- Sync is excellent.

## BLOCKING

1. **The hit layers duck themselves, so every big moment loses its slam.**
   - Cause:
     - Line 1501 multiplies the whole music bus *and its hall return* by `dh` (and `dk`).
     - Line 1508 does the same to bass, and line 1517 to drums (`0.6+0.4*dh`).
     - But every hit braam is placed on `'music'`: lines 820, 821, 832, 843, 1057, 1150, 1206 (stamp), 1363, 1433 and 1446. The hit taikos and the drop kick are on `'drums'`.
     - The DH duck that should make room for these layers (attack 3 ms, depth 0.4-0.6) therefore cuts them by 4-10 dB at their own onset. They swell back in 150-300 ms later as a reverse-envelope "whoomp".
     - The final braam's hall tail (mhall) is held down by the 1.5 s duck (line 1454).
   - Fix:
     - Add a `'hits'` bus that is not multiplied by dk, dh or sgm. Give it its own hall send to `v_hall` (not `v_mhall`) and add it to `pre`.
     - Move every braam above to it, plus the hit taikos (1114, 1130, 1137, 1151, 1452) and the 59.0 drop_kick (1450).
     - Apply dh only to the bed: music minus hits, bass and drums. Take the mhall return out of the dh multiply, or give it only half the depth.
   - Targets:
     - Momentary contrast of at least +3 LU on every weight-3 slam, and at least +2 LU on the stamps.
     - The music stem in the 0-50 ms after each hit must be **at least** its pre-hit level.

2. **The final hit at 59.0 is not massive** (contrast +0.3 LU, about 1 dB above the snare pickup once the low end is filtered out).
   - Round 1 asked for a decaying tail. The response over-shortened the hit itself and left it self-ducked.
   - Fix, besides #1:
     - Line 1446: braam gain 0.7 → 1.0, edec 0.4 → 0.6, with the tail carried by a `v_hall` send of 0.6 that is not ducked.
     - Line 1447: impact size 0.75 → 1.2, d 1.0 → 2.0, subdec 0.28 → 0.4.
     - Line 1083: pickup roll gain `0.12+0.35*i/15` → `0.08+0.18*i/15`.
     - Line 1444: reverse_swell 0.7 → 0.45.
     - Keep the 58.93 suck.
   - Targets: 59.0 momentary at least +4 LU over the 2 s before it, and in the same range as the 50.0 drop. The tail should still be about -12 dB by 59.7, achieved through the hall decay, not by ducking.

3. **The drop at 50.0 is chopped and peaks lower than the build.**
   - Line 1399: the PD dips `(50.052, 50.073, 0.5)` and `(50.088, 50.123, 0.15)` cut the drop kick, the impact, the crash and the braam to -16 / -19 dB 50 ms after the downbeat. On the biggest moment of the film that reads as a dropout or glitch.
   - The build climax (lines 1008-1009 risers, 1381-1386 taiko 1.0 + impact + reverse swell, the 32nd rolls at 983-990, sg 1.25 at line 1526) is the loudest moment of the film: 49.525 at -9.1 LUFS momentary, against the drop's -10.0.
   - Fix:
     - Delete both PD entries at line 1399. Layer 50.075 / 50.125 on top: the post-bus slam already has its own crack.
     - Riser at 49.0: 0.32 → 0.22. Riser at 45.0: 0.4 → 0.3. Taiko at 49.5: 1.0 → 0.7. reverse_swell at 49.5: 0.8 → 0.55. sg at 49.9: 1.25 → 1.1.
   - Target: 50.0-50.4 momentary at least 2 LU above the max of 49.0-49.94, with no hole in the first 150 ms after 50.0.

4. **The tagline slams 53.0 / 53.5 (weight 3) and 8/8 at 50.875 do not stand out** (+0.6 / +0.6 / -0.5 LU).
   - Most of this is #1: the braam stabs are on the music bus, under DH 0.5.
   - The rest is the 4/4 bed at full drop gain.
   - Fix: after #1, give the 53.0 / 53.5 impacts (line 1418) a 20 ms pre-suck on the bed only. Drop the 16th ride and air bed by 4 dB for 120 ms after each tagline.

## Improvements
- **The weight-3 cues at 4.0 (CRT-ON / REJOUER, -0.6 LU) and 6.15 (NIVEAU, +0.3) are weaker than what precedes them.**
  - Before 4.0, the rewind (line 1556, gain 0.85) and the CRT zap (line 1572, 0.8) are as loud as the slam. Lower the rewind to 0.6 and the zap to 0.55.
  - At 6.15 the slam lands 150 ms after the 6.0 kick + crash + swish (lines 1147-1148). Make the 6.0 cut lighter (crash 0.35 → 0.2, no kick at 6.0) so the slam is the hit.
- **The answer stamps sit only +0.4 to +1.5 LU above the groove.** After #1, lower the groove bed by 2 dB for 250 ms (DH depth 0.55 → 0.7 on the bed only) and add a 20 ms bed pre-suck before each stamp.
- **The pre-hit "micro-sucks" are 26 ms dropouts of the whole groove (-10 dB)** at 10.972, 15.972 and 35.972 (lines 1224, 1245, 1327). They read as gating. Shorten them to 12 ms at ×0.5, or apply them to the bed only (not the sfx).
- **Register / mud:**
  - The low ostinato is transposed down an octave (line 936: `-12`), which puts 16th plucks at F1-Ab2 (43-104 Hz). That is in the same space as the kick (50 Hz end), the sub sine (43.6 Hz) and the taikos.
  - Remove the `-12`, so the staccato sits at F2-Ab3 as a low-mid lead.
  - Cut the drums bus 2-3 dB at 200-300 Hz (taiko on 1 and 3 plus tom 120 on 2 and 4 from 20 s on, lines 908 and 913).
  - Mids are -9 to -12 dB vs total in the groove and build.
- **Choir static formants** (line 757; on continuously 20-40 s at line 951 and through the drop at 1047): fixed 750 / 1180 / 2650 Hz bands show as steady horizontal lines in the spectrogram, which is the "preset aah" signature.
  - Slowly morph F1/F2 by ±8 % over each bar (ah → oh), or use tvf band-passes.
  - Lower the choir in 20-30 s to 0.2, and give it the string-pad role only from 30 s on.
- **UI level and clutter:**
  - Lower the swish at 40.5 (line 1344, g 1.2 → 0.5; it is +3 dB over the breakdown bed).
  - Lower 18.5 (line 1255, 0.9 → 0.5), 55.5 (line 1430, 1.3 → 0.6), the 48.5 tok (line 1378, 1.8 → 0.9), 51.7625 (lines 1406-1407, thump/tok 2.0 → 1.2) and the first tok of the 45.75 typing burst (line 1370, 1.4 → 0.7).
  - Drop the tok layered under thumps/toms where a drum already hits the beat: 21.0-22.25 (line 1268), 27.0-28.0 (line 1295), 41.012-41.234 (line 1350).
  - Target: no UI event louder than -6 dB vs the bed.
- **Pitch-up glides:**
  - The 0.5 s riser at 5.5 (line 844, `riser(0.5, 35, 41, 53)`) glides an octave in half a second, which is the closest thing left to a "power-up vwoop". Use m1 = 46 (a 5th) or a noise-only riser there.
  - The CRT-on hum (line 1126) is a 50→120 Hz saw glide. Drop the saw component.
- **The power-ups are half-time trailer** (kick on 1 and 3 only, lines 904-906) for 30 s.
  - For an electronic festival (Klaan / Sound of Legend / Mattn), add a quiet four-on-the-floor kick or offbeat bass in the power-ups at 30-40 s, so the drop is foreshadowed and the festival DNA is audible before 50 s.
  - The braam / taiko language reads more AAA-game than festival.
- **Side-channel HP** (line 1589) is 2nd order at 140 Hz. Side <120 Hz is still -13.5 to -15 dB vs mid in the breakdown and drop. Use 4th order.

## Scores
Maturity 7, brand fit 6, technical 6, sync 9.
