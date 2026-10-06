# Critique: b-techno (festival techno), senior supervisor review

Re-analysed `mix.wav`: -13.99 LUFS, -2.40 dBTP, 2,880,000 samples, DC ~0, no clicks, 4 high tonal beeps (all noise-band peaks). Cue sync: median 5.3 ms. Every weight-3 cue lands within +/-20 ms (the worst is 56.0 at -16 ms, pulled early by the transient placed at 55.99).
A scratch re-render of a copy, with stems, matched the delivered file bit for bit, so the script is deterministic and renders in about 50 s.

## Verdict
This is a real step up from the "enfantine" version: no square blips, coins, bells or chiptune, and it has a real kick, rumble, side-chain and acid. Three things could still make the client hear "game / cheap", plus one sync hole:

1. **41.5 (weight 3): the "RETROUVE TA BANDE." answer stamp has no sound.** The power-up loop (l.1094) only covers P = 10..35. The breakdown block (l.1201-1231) puts only a 0.45 clack at 41.5, so the onset measures 0.9x global median / 2.0x local. Every other answer gets a stamp.
2. **2.5 "denied" glitch (l.993-1008).** It is a sample-and-hold decimated saw (every 14 samples, so an effective ~3.4 kHz sample rate) gated "eh-eh-eh-ehhh". That is an arcade / game-show "wrong answer" buzzer, a lo-fi 8-bit cliche, and it plays louder than the music there (SFX rms -11.5 dB vs music -15.7 dB).
3. **7.0-8.75 eruption stabs (l.1061).** Eight hoover octaves climb chromatically F to C, one per 8th, each with an upward 1.5-semitone scoop. That is the "level-up staircase" gesture. It also puts A natural and B natural against the Gbmaj7 pad (8-10 s).

## Measurements (own)
- Low end is mono: correlation below 100 Hz is 0.98-0.998 in every section. The exception is the hook at 0.945, because `lava_bed` (l.927) uses independent noise per channel below 140 Hz.
- Phone translation: integrated loudness band-limited to 400 Hz-8 kHz is -20.8 LUFS, about 6.8 dB under the full-band -14.0. In the power-ups it is -21.5 vs -14.1. Stems in 10-40: low bus -4.3 dB rms, synths -14.9, drums (hats/claps/perc) -21.8, SFX -21.0. Hats and claps sit about 17 dB under the low bus, and presence (2-6 kHz) is -19.6 dB re total. On a laptop or phone this will sound muffled and small. The analysis spectrogram shows the 2-6 kHz band thin everywhere except the build.
- Contrast: breakdown -15.8 LUFS vs power-ups -14.1, only 1.7 LU of "breath". The drop is -11.8 (+2.3, good). The 10-40 bars sit at -14.0 +/-0.4 for 30 s. Crest per section is 10.8-15 dB.
- Pre-drop: 49.9-50.0 rms -17.4 dB, 50.0-50.1 -12.0 dB. The drop lands, but its onset is only 2.7x the local median because the riser, reverse crash and snare roll run full-level right up to 49.98.
- UI levels are fine: toks peak 8-20 dB under the music. Exception: the drop hop landings at 51.775-52.675 (l.1303-1306, gain 1.0 plus a transient at 0.65) peak level with the music, as 7 toks rising 240 to 300 Hz.
- Harmony (chroma 60-1500 Hz): the F / C / Db / Eb / Gb centre is fine, and C dominates because the saturated F1 kick makes a strong 3rd harmonic. There are out-of-key slips:
  - Bass passing note `root+1` (l.778-779) gives D natural over Db at 15.75 and 47.75, E natural over Eb at 31.75, and G natural over Gb.
  - `CH['Eb']` / `VO['Eb']` (l.735, l.1291) use G natural, while the acid plays Gb. At 53.125 the acid Gb2 (pattern C, step 9) sits against the G3 of the tagline-1 hoover and pad: a minor 9th smear on a slam.
  - The 49-50 C7 (E natural) sits against acid Ab/Gb.
- Register: acid F2-F3 (l.864, hp 70 Hz at l.921) and bass 16ths on F2 share 87-175 Hz with the same 16th grid. That masking is part of why low60-250 sits at -3.6 dB re total.

## Blocking
1. **41.5 stamp missing.** Add `stamp(41.5, 4045, 0.85, 0.9)` (a slightly smaller, darker room in the breakdown is fine) and keep the clack 20 ms later at 0.3.
2. **Replace the decimated "denied" buzzer** (l.996-1003). Remove the `np.repeat(gb[::14],14)` decimation and the pitched saw buzz. Instead: a tape-stop of the OVER braam tail (varispeed 1 to 0 over 0.35 s, like the rewind code at l.1369), a gated sub stutter on F1 (sine with tanh, same 4 gate windows), and a relay "clunk" (tok 150 Hz, tau 25 ms, plus a low transient). Peak it about 4 dB under the OVER slam.
3. **De-gamify the eruption stabs** (l.1061). Drop `+i` from the pitch and use `scoop=0`. Keep every stab on the F power voicing [29, 41, 48] (or alternate F / Gb, phrygian). Carry the rise with the filter (`cut=900+180*i`) and the eruption noise only. If a pitch rise is wanted, use the scale degrees F-Gb-Ab-Bb-C-Db-Eb-F, never chromatic, and never scooped.

## Improvements (priority order)
1. **Translation / brightness.** On the master (l.1472), add a +2 dB high shelf at 2.5 kHz on DRUMS only, not the master: raise the DRUMS bus +3 dB (l.1456) and give claps a 2-4 kHz crack layer. Bring the rumble down to 0.22 (l.1406) and the low bus down -1.5 dB. Add 2nd/3rd-harmonic saturation to the bass above 150 Hz (parallel `sat(hp(bass,150),3)` at -12 dB) so the bass line exists on phones. Target: 400-8k band LUFS within about 5 dB of full band.
2. **Harmony hygiene.**
   - Make the bass passing note scale-aware: use `root+1` only on Fm. Use `root+12` or the next scale tone on Db / Gb / Eb, and never D, E or G natural.
   - Make Eb an Ebsus (Eb-Ab-Bb) or Ebm, and change VO Eb to [39, 46, 51, 54] or [39, 46, 51, 56].
   - Transpose the acid per chord (root follows `ROOT[chord_at]`), or mute the step-1 Gb on Eb and C chords.
3. **Unmask the acid.** Use `hp(...,170, 2)` at l.921 instead of 70 Hz, or keep the acid an octave higher (F3-F4, still low-mid) from 30 s on. Then the bass owns 40-170 Hz and the 303 owns the resonant 200-1500 Hz bite.
4. **Breakdown must breathe.** Set SG 40-45 to 0.72 (l.1463-1464) instead of 0.9. Remove the shaker for 40-42, and let the heartbeat plus the pad carry it. Aim for -17.5/-18 LUFS so the build and drop feel bigger.
5. **Drop impact.** Add a 90-120 ms pre-drop "vacuum" (49.88-50.0): gate SYN/SFX/DRUMS to -18 dB, end the riser at 49.88 and let only a reverse-reverb suck through. Do the same before 59.0, which already works (-18 dB pre, -11.9 post).
6. **Power-up groove variation.** Six half-bar kick and bass drop-outs at every whip (l.757, l.1080) chop the "full groove" every 2.5 bars. Keep the kick muted only on the last two 8ths (P+4.75) for 15/25/35, or replace it with a filtered kick, and keep the full mute at 20 / 30 / 40.
   Make the 10-40 energy step up in tiers: 10-20 without claps on even bars, 20-30 add perc, 30-40 ride, toms and open acid, with SG stepping 0.80 / 0.84 / 0.88. The acid cut-off saw-tooth reset every 5 s (l.857-861) can become one long ramp 10 to 40 with smaller per-power-up wiggles.
7. **cool_sheen** (l.664-672, used at l.1112). The rising 2.2 to 6.6 kHz air shimmer reads as a "magic sparkle" after each landing. Make it descend (6 kHz to 1.5 kHz, a decaying steam hiss) or drop it and keep the thermal crack plus 2-3 low metal "tick" contractions (metal() 150-700 Hz, very short).
8. **Drop hop toks** (l.1303-1306). Set the gain to 0.55 and the transient to 0.35, and hold the body pitch constant (230 Hz) instead of rising 240 to 300 Hz. Seven ascending pitched toks in a row read as a little melody.
9. **EDM snare-roll builds** appear three times (5.5, 9.0, 45-50: l.1036, l.1066, l.1248). For a de Witte / Lens register, swap at least the 45-50 one to a kick/tom roll (`kick_s` low-passed at 400 Hz plus `tom_s`) with a clap washed into the hall, and keep the snare only as a quiet top layer.
10. **Width in the drop** (corr 0.78, no wider than the groove). Use 4-5 hoover voices per side with +/-25 cent decorrelated detune, a Haas 12 ms on the hall return for claps, and send the hoover to the hall at 0.35. Keep kick, bass and rumble mono as now.
11. Hook: make `lava_bed` below 140 Hz mono (sum the lp part) to fix the 0.945 low correlation. Move the opening tok/transient from 0.035 to 0.0-0.005 (l.947-948) so the first hit is not 35 ms late.

## Brand fit
Credible as a festival-app trailer bed: dark F minor/phrygian, 120 BPM rumble techno, braams and industrial impacts suit Klaan / Mattn line-up energy. Fix the buzzer, the chromatic staircase and the sparkle, and it reads as adult and premium. The muffled top end is the main thing that would make it sound "cheap" on phone playback, which is where an app promo is mostly watched.
