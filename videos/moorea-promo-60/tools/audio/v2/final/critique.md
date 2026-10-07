# Critique, round 2: direction A "melodic techno" (compose.py rev 2 -> mix.wav / mix.mp3)

Reviewer: music supervisor / mix-master review. Judged from the code and measurements only, not by listening.
Analysis re-run: `analysis_review/` (spectrogram.png, waveform.png, analysis.json), plus my own measurements.
I re-rendered compose.py to the scratchpad with DEBUG=1. It is bit-identical to mix.wav (max diff 0.0) and renders in 42 s.

## Scores
- Maturity (anti-childish): 8/10
- Brand fit: 8/10
- Technical: 7/10
- Sync: 9/10

## Verified fixes from round 1
- **Phone translation.** Loss under a HP 250 / LP 8 kHz phone simulation is now 1.2-3.0 dB per section (the power-ups lost 5.4 dB before).
- **Ending.** It now decays: -11.5 dB at 59.0, -19.5 at 59.5, -25.7 at 59.7. The fade is applied once.
- **"denied".** Retuned to F1 / Gb1, with tanh drive only and a -3 st bend.
- **PRESS swell.** Voiced C-G-C-Db.
- **UI.** Breakdown toks use the fixed 170 Hz body. Typing is a noise-grain cloud. The sonar has no pitch.
- **Development.** 3:4 arp accents from 20 s, ARP_PAT2 and a low motif from 30 s.
- **Drop downbeat.** The long crash, sub and braam now hit at 50.0.
- **Specs.**
  - Exactly 2,880,000 samples, -14.0 LUFS, -1.7 dBTP, DC about 0, no click candidates.
  - High tonal beeps: 5 (old mix: 332).
  - MP3 decodes to 2,880,000 samples with lag 0 against the WAV, at -14.0 LUFS.
- **Harmony.**
  - All lead, motif, arp and pad notes are diatonic to F minor, or use the harmonic-minor E on the C chord.
  - The lead stays in C#4-Db5 and the arp in F3-C5.
- **Low end and stereo.**
  - The low end is mono: side/mid under 120 Hz is -18 to -26 dB.
  - The image is wide: side/mid above 300 Hz is -1.6 to -4.5 dB.
  - The side-chain pump on 300 Hz-3 kHz is about 5 dB deep in the power-ups and recovers in about 150 ms.
- **UI level.** UI sits about 12 dB under the music in the groove.

## Sync
- All 32 weight-3 cues land within -6.7 to +1.3 ms with strong onsets (local strength 2.5-11x). The median offset over 280 cues is 4 ms.
- The weakest weight-3 cues are 50.125 (title slam, local 2.5) and 50.875 (8/8, local 2.6). Both fall inside the drop's wall of sound.
- 52.525 (hop 6, weight 2) reads -23.7 ms because the 52.5 kick wins.
- 0.000 is an analyser edge case.
- No weight-3 problems.

## Blocking
1. **Constant white-noise hiss bed (l.1360-1368, added at l.1499).** It sounds like a noise floor, not "heat shimmer".
   - The `air` bed is decorrelated 9-19 kHz noise at about -37 dBFS for the whole 60 s.
   - In the hook and the breakdown, everything above 9 kHz is this bed alone (L/R corr 0.00):
     - 0.2-0.9 s: -19 dB under the total.
     - 40.5-44.5 s: -20 dB under the total.
   - In the breakdown the spectrum is inverted: 2-4 kHz is -22.5 dB and 4-8 kHz is -25.8 dB, but above 9 kHz is -20 dB. You can see this in the spectrogram at 40-45 s: a dark-blue hole at 3-6 kHz with a red band above it.
   - On headphones or a laptop, a dark pad with steady hiss on top sounds like a bad encode or tape noise. That is the opposite of premium.
   - Fix:
     - Lower it by 10-12 dB (`AIR = ... * 0.15 * 0.55` -> `* 0.025`).
     - Add a tilt so it falls about 6 dB/oct above 12 kHz.
     - Duck it to 0 in the breakdown (40-45) and in the hook 0-3.
     - Better still, drop the bed and let the hats, crash tails and steam carry the top octave: those exist in every groove section.

## Improvements (priority order)
1. **The drop is not clearly the biggest moment.**
   - Momentary loudness (400 ms) at 49.0 is -11.5 LUFS, the same as at 50.0 (-11.5). Build bar 24 (48-50) is -12.6 LUFS against -12.1 for the drop bar.
   - Short RMS (80 ms) of the 50.0 downbeat is -14.3 dB. A routine power-up eruption at 20.0, 25.25 or 45.0 is -13.4. The drop gets its punch almost entirely from the low end returning (+17 dB under 100 Hz).
   - The vacuum (l.1428) only reaches -17.7 dB at 49.75, because the 'pre' bus is left out of it (riser power 3 peaking at 50.0, l.1259-1262; reverse swell gain 1.6, l.1275).
   - Fixes:
     - Cap the build riser at -3 dB from 49.5. Put 'pre' through the vacuum at 0.5 (not 1.0) so 49.78-50.0 sits about 8-10 dB under the drop.
     - Trim the 32nd snare roll 49.0-49.94 by 2 dB.
     - Lower `pad_lvl` at 49.9 from 0.9 to 0.7 and arp gain at 49.9 from 0.75 to 0.6, so the drop has a step up at 50.0.
2. **The drop sags 51.5-52.75 (hop landings).**
   - Arp out (l.916), hats and shaker out (l.865, 874), bass reduced to held notes (l.897-901), and the music ducked 0.45 under each landing (l.1308).
   - M400 at 52.0 is -13.4 LUFS, quieter than the power-ups (20.0: -12.6). One second after the biggest hit, the drop sounds like a breakdown.
   - Fixes:
     - Keep the closed hats at -4 dB and the rolling bass, ducked by the ticks (big() depth 0.25, not 0.45).
     - Keep arp 2.
     - Let the lead carry the hops (accent one lead note per landing, +2 dB) instead of stripping the groove.
3. **The breakdown is barely a breath** (-15.2 LUFS against -14.0 in the power-ups; the waveform is a flat 3 dB brick from 6 to 59 s).
   - The whole film's short-term loudness sits between -12.0 and -16.5 LUFS.
   - Fix: bring 40-45 down 2.5-3 dB: `pad_lvl` 0.75/0.8 -> 0.55/0.6 (l.1377), heartbeat 0.85 -> 0.7. Then the build and drop open up from a real low point, and the -14 LUFS normalisation gives the other sections that level back.
4. **The "washed in delay" breakdown arp is not actually implemented.**
   - `pingpong` (l.1390) has a fixed send (0.9) and fixed feedback (0.38). The breakdown arp only loses gain.
   - "Evolving filters" are slow brightness ramps through a non-resonant two-LP crossfade, with no filter movement inside a section. That makes the hypnotic thread static, especially 10-30 s.
   - Fixes:
     - Automate the delay send per section: 0.6 in power-ups 1-2, 0.9 later, 1.5 with fb 0.55 and hi 2000 Hz in 40-45.
     - Run the arp bus through `sweep_filter(..., 'LPF24', res=0.35)` driven by a 2-bar or 4-bar sine LFO (±0.6 oct) on top of `arp_bright_pts`. This is the classic Afterlife arp motion.
5. **The cold open hits softer than the groove.**
   - Hook LUFS is -15.9. GAME and OVER short RMS is -14.3 / -13.6, no louder than the power-up eruptions.
   - The first 4 s are the retention moment.
   - Fixes:
     - +2 dB on the GAME / OVER impact and braam (l.1017-1023).
     - Lava bed 0.5 -> 0.35 (l.994) so the slams have contrast.
     - OVER's hall tail is fine.
6. **Pitched sine-tok trains can read as a woodblock or marimba roll.** `tok()` defaults to sine=0.8 with a 35 % pitch drop (l.550). Fast runs of identical 250-270 Hz bodies:
   - 2.294-2.469 (5 x 44 ms)
   - 26.75 / 27.25 / 27.75
   - 32.02-33.52
   - 38.56-38.68 (3 x 60 ms)
   - 55.35-55.55 (5 x 50 ms)

   Fix: use `dry_tok` (sine 0.4, fixed body) or noise grains for every run of 3 or more. Set the default `sine` to 0.5.
7. **Hop landing ticks are forward in the drop.**
   - The UI bus measures -13.7 LUFS (gated) in 50-54, against -11 to -12.6 for the music stems.
   - Gains of 2.6-3.0 (l.1307) on a 150 Hz haptic plus a 1.8-7 kHz click.
   - Fix: once item 2 restores the groove, bring them down to 1.8-2.0 and lean on the side-chain dip.
8. **The tape rewind (l.1476) runs up to 4.7x speed**, which shifts the reversed braams about +27 st. That is a chipmunk squeal, and it is where the 3.35 s beep (1.8 kHz) comes from.
   - Fix: cap the rate at about 3x (`1.0 + 2.0*uu**1.4`) and LP at 3.5 kHz.
   - Add wow (±3 % at 6-9 Hz) plus a little broadband tape hiss so it reads as a machine, not a squeal.
9. **The 55.5 "spinning fall" whoosh (l.1329-1330)** has an accelerating 6 -> 32 Hz amplitude tremolo, which edges toward a cartoon propeller.
   - Fix: replace the tremolo with a Doppler-style pan sweep plus a filter dive, or keep the tremolo depth at 0.15 or less.
10. **MP3 delivery.** The MP3 stream has a 23 ms start_time (encoder delay). It is gapless in ffmpeg, but some NLEs place it 1 frame late.
    - Fix: also send the client the WAV (or a 48 k AAC/M4A with an edit list), and confirm sync in their editor.
