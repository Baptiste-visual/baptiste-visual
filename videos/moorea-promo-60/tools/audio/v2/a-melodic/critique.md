# Critique: direction A "melodic techno" (compose.py -> mix.wav / mix.mp3)

Reviewer: music supervisor / mix-master review, from the code and measurements only (not heard).
Analysis re-run: `analysis_review/` (spectrogram.png, waveform.png, analysis.json).

## Scores
- Maturity (anti-childish): 7/10
- Brand fit: 7/10
- Technical: 6/10
- Sync: 9/10

## What is good
- No banned timbres. No square or pulse waves, coins, bells, boings or whistles anywhere in the code. There are 5 high tonal beeps, against 332 in the old mix.
- The harmony is consistently F minor: Gb phrygian colour, C major as the V chord, the epic i-VI-VII-V moves.
- The lead sits low-mid (MIDI 61-73, about C#4-C#5). The arp sits in F3-C5, low-passed under 2.8 kHz.
- The low end is mono: side energy under 140 Hz is -19 to -27 dB relative to mid.
- Mids and highs are wide: L/R correlation above 300 Hz is 0.44-0.54 in the groove and 0.15 in the breakdown.
- The side-chain pumps clearly in the power-ups: the 300 Hz-3 kHz band dips 9 dB after each kick.
- Specs:
  - Exactly 2,880,000 samples, -14.0 LUFS, -1.7 dBTP, DC about 0, no click candidates.
  - The MP3 decodes (ffmpeg, gapless) to 2,880,000 samples with 0 sample lag against the WAV, -14.09 LUFS and -1.45 dBTP.
- Sync: all 32 weight-3 cues are within -8 to +10.3 ms. Median offset is 5.3 ms.

## Blocking
1. **Mix does not translate to phone or laptop speakers.** This is an app promo, so it will mostly be heard on phones.
   - The 40-80 Hz octave sits at -2.6 dB relative to the total in the power-ups. 1.28-5 kHz sits at about -23 dB.
   - Phone simulation (HP 250 Hz, LP 8 kHz):
     - Power-ups 10-40 fall from -13.7 to -19.1 LUFS, a 5.4 dB loss. The old mix lost 0.9 dB.
     - The hook 0-4 plays at -21 LUFS.
     - The opening GAME / OVER, the most important 4 s for retention, is the quietest part of the film on a phone.
   - Fixes:
     - Pull the sub contributors down 2-3 dB: rumble 0.17 -> 0.12 (l.1321), sub_boom gains, the lava bed 2.5x (l.914), bass `subg`.
     - Add 2nd-harmonic saturation on the bass mid layer (HP 90 Hz, then `sat`, then a +3 dB peak around 700 Hz) so the bass line can be heard on small speakers.
     - Open the arp's top: final LP 2800 -> 4500 (l.342), `fc` up to 330+3000*bright.
     - Raise the pad ladder floor in the power-ups from 1000-1400 Hz to 1800-2600 Hz (l.1280).
     - Add a +2.5 dB, Q 0.8 bell around 2.5-3.5 kHz on the music bus (pad, arp and lead only), not on the master.
     - Give the braams more 1-2 kHz: final LP 2100 -> 3200 (l.398).
   - Targets:
     - 1.28-5 kHz at about -15 to -17 dB relative to total in the groove.
     - Phone-simulated loss no worse than about 2.5 dB in every section.

2. **The ending is chopped, not rung out.**
   - RMS from 59.0 to 59.6 stays at -11.6 to -12.8 dB, a 1.2 dB decay in 0.6 s. It then collapses to -47 dB by 59.9.
   - Cause 1: the final Fm pad (TL (59, 'Fm') -> (61, 'Fm'), att 0.01, pad_lvl 1.1) is a sustained chord.
   - Cause 2: the 0.3 s fade is applied twice (l.1427 and l.1437), which makes it cos^4, an audible ~150 ms chop.
   - Fixes:
     - Give the 59.0 pad an exponential decay of tau about 0.45 s, or start its release at 59.2. Let the braam, hall and crash tails carry the ring.
     - The goal is about -20 dB below the 59.0 peak by 59.7, so the fade is inaudible.
     - Apply the fade only once: drop the second multiply, or apply it after DC removal only.

## Improvements (priority order)
1. **Drop contrast is small.**
   - Bar LUFS: build last bar (48-50) -13.3, drop -12.2 / -12.7, power-ups -13.3 to -13.7. The biggest moment is only about 1 dB above the groove.
   - The phone sim makes it -16.1 against -19.1, but only because the power-ups are dull.
   - Fixes:
     - Trim the power-up music by 1-1.5 dB (or arp gain in arp_gain_pts) so the limiter leaves the drop room.
     - Make 49.75-50.0 a real pre-drop vacuum: everything except the reverse swell and the riser top at -12 dB for the last 8th, not just the 35 ms suck.
   - The drop's long crash and braam sit on 50.125, a 16th after the downbeat (l.1195-1197). The bar-1 downbeat at 50.0 only gets a choked crash and a flick, which reads as a flam.
     - Move crash(3.0) and the sub boom to 50.0.
     - Keep 50.125 as impact + braam (or braam on 50.0 with a 25 ms swell, so it blooms into the slam).
2. **OVER (1.5) is weaker than GAME (1.0):** local strength 2.9 against 4.8, global 2.3.
   - The GAME braam (1.6 s, decay 0.6) and its hall are still loud at 1.5.
   - Fix: choke the GAME braam at 1.45 with a 30 ms suck. Give OVER +1.5 dB, a lower sub0, and a longer braam. The second slam must be bigger than the first.
3. **"denied" (l.669-687, at 2.5) reads as a game-show wrong-answer buzzer.**
   - It uses 12-level bit-crushing (`np.round(x*12)/12`).
   - It is tuned A1 (55 Hz) + E2 + Eb2, out of key. The A clashes a semitone against the Bb of the Gb pad.
   - Fix: retune to F1 / Gb1 (43.65 / 46.25 Hz) with tanh distortion and no quantiser. Add a fast downward pitch bend (-3 semitones over 120 ms) and keep the stutter gate. That reads as "system failure", not a quiz show.
4. **PRESS "power-up swell" (l.967-969) is a pure C major triad with the third on top (C3 E3 G3 C4 E4)** under an opening ladder sweep. It is the one place that drifts toward a hopeful "level-up" chord.
   - Fix: voice it C-G-C-Db (b9) or Csus4 -> C with no E on top, or make it a rising braam cluster. The pad at 5.0 can stay C as the V chord.
5. **Exposed UI toks in the breakdown (l.1146-1150).**
   - 42.5 / 42.75 / 43.0 rise in pitch (230 / 240 / 250 Hz sine body), at gain 1.0 with hall 0.15, and there is no kick to mask them. A rising 3-note woodblock with reverb is the cutest moment in the mix.
   - The 21.0-22.25 map pins alternate 210 / 225 Hz (tick-tock).
   - Fix: use one fixed body (about 170 Hz), more noise and less sine (click 0.8, sine 0.4), -4 dB, no hall in the breakdown.
6. **Typing runs (l.1054: 11 ms steps; l.1163: 20 ms steps)** are a 50-90 Hz train of pitched 330-420 Hz sine toks, a buzzy "brrrt" rattle.
   - Fix: replace the sine body with a band-passed (1-4 kHz) noise-grain cloud at -6 dB, keeping one soft tok at the start and end.
7. **Hop 1 land tick is 12.5 ms early:** LAND[0] = 51.7625, cue = 51.775 (l.1216). Set it to 51.775.
   - Hops 2 and 6 at gain 3.6 (l.1218) are forward; even them out at about 2.6 and let the kick carry 52.5.
8. **Sonar (l.1083-1084, 1149): three 160 Hz pitched sine pings with hall 0.45** on 8ths can read as "bloop bloop".
   - Fix: make it a sub thump + filtered noise ping, with no pitch glide and hall 0.25.
9. **Repetition.** The same rolling bass and the same 16-step arp cell run from 10 to 40, and the lead only appears at 50.
   - Fix: add a low, sparse lead motif (3-4 notes, C4-Ab4) from 30 s that pre-echoes the drop melody. Or change the arp pattern / rhythm (e.g. 3-against-4 accent) at 20 and 30. Then the power-ups develop musically, not only through filter opening.
10. **MP3 delivery.** It decodes gapless in ffmpeg, but some NLEs ignore the LAME/Xing encoder-delay tag and place the audio about 23-25 ms late (start 0.023 s in ffprobe).
    - Fix: check in the client's editor, or pre-roll-compensate. That is within 1 frame, but worth noting.
11. **Minor code hygiene:**
    - `kick_ev` is unused.
    - `A *= curve(...)` with all-1 points is a no-op (l.1295).
    - `0.0625 if True else 0` (l.994).
