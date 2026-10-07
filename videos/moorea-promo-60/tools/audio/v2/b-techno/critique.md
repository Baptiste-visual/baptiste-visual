# Critique: b-techno (festival techno), second independent review

Analysed `mix.wav` again: -13.99 LUFS, -2.40 dBTP, 2,880,000 samples, DC ~0, no clicks, 4 "high tonal beeps" (noise-band peaks; the old mix had 332). Cue sync: median 5.3 ms. Every weight-3 cue has an onset within +/-20 ms. The exception is **41.5**, which has no real onset (0.9x global median). The tightest pass is 56.0 at -16 ms.

## Own measurements
| section | LUFS | phone band 400 Hz-8 kHz LUFS | crest dB | corr <100 Hz | S/M |
|---|---|---|---|---|---|
| hook 0-4 | -15.7 | -22.5 | 13.7 | 0.945 | -9.2 |
| power-ups 10-40 | -14.1 | -21.5 | 12.6 | 0.998 | -11.2 |
| breakdown 40-45 | -15.8 | -21.0 | 13.3 | 0.983 | -3.0 |
| build 45-50 | -13.9 | -19.4 | 12.9 | 0.996 | -9.7 |
| drop 50-54 | -11.8 | -18.4 | 10.3 | 0.983 | -9.1 |
| end 54-59 | -14.0 | -21.5 | 12.3 | 0.998 | -11.0 |

- Side-chain pump (300 Hz-2 kHz, averaged over 20-24 s): 11 dB. Real, clearly audible pumping. Good.
- Low end is mono everywhere except the hook (0.945, because `lava_bed` uses independent noise per channel below 140 Hz).
- **Darkest of the three v2 variants.** Presence (2-6 kHz) is -19.6 dB re total in the power-ups (a-melodic -15.3, c-trailer -14.8, old mix -8.2). Sub<60 Hz is -3.8 dB. Phone-band loudness is about 7.4 dB below full band.
- Pre-drop: 49.8-50.0 sits at -15.2 dB rms and 50.0-50.1 at -11.7. That is only a 3.5 dB step into the biggest moment, with no vacuum.
- Final hit: 59.0 is -11.3 dB, then 59.5 -13.8 and 59.6 -14.5. The tail decays only about 3 dB in 0.7 s, so the 0.3 s fade removes a sustained chord at about -15 dB. It reads as a fade-out, not a ring-out.
- Breakdown is only 1.7 LU under the groove. The waveform PNG is a sausage from 4 to 60 s, and the breakdown barely dents it.
- 2.5 "denied" buzz peaks at -6.4 dBFS (sample peak) and sits at the same level as the surrounding hook material.
- Drop hop toks (51.775-52.675) peak level with the music (-3.4 to -4.9 dBFS vs -3.3 to -5.9 just before).

## Childish / cheap hunt
- No square blips, coins, bells, music box, boing, slide whistle or chiptune arpeggios. Kick + rumble + 16th bass + ladder acid + braams is the right toolbox.
- **Still game-cliche:** the bitcrushed "eh-eh-eh-ehhh" wrong-answer buzzer (l.993-1003), and the eight chromatic, scooped pulse-wave stabs climbing F2->C3 (l.1061), a literal "level-up staircase" that also puts A and B natural over the Gbmaj7 pad. `cool_sheen` (l.664-672) is a rising 2.2->6.6 kHz noise shimmer after each landing, which reads as a "magic sparkle".
- Harmony slips: the bass `root+1` passing note (l.778-779) plays D natural over Db (15.75, 47.75) and E natural over Eb (31.75). `CH['Eb']` / `VO['Eb']` (l.735, l.1291) contain G natural while the acid plays Gb (step 1 of every pattern), which gives a b9 rub on the 53.0 tagline slam. The C7 at 49-50 has E/G against acid Gb/Ab.

## Blocking
1. **41.5 (w3) answer stamp "RETROUVE TA BANDE." is silent.** The stamp loop (l.1094-1115) covers only P=10..35, and the breakdown (l.1223) has only a 0.45 clack. Add `stamp(41.5, 4045, 0.85, 0.9)` (it may use a darker room, `rev=0.25`), move the clack to 41.52 at 0.3, and add `duck(DIPH, 41.5, 0.5, 0.2)`.
2. **Replace the decimated "denied" buzzer** (l.994-1003). Delete the `np.repeat(gb[::14],14)` sample-and-hold and the pitched saw buzz. Build it from: (a) a tape-stop of the OVER braam tail (copy SYN 1.9-2.5, `varispeed` rate 1->0 over 0.35 s); (b) a gated F1 sine sub stutter (`tanh`, same 4 gate windows, lp 120 Hz); (c) a relay clunk (`tok(150, 0.025)` + `transient` at 0.4). Peak it about 4 dB under the OVER slam.
3. **De-gamify the 7.0-8.75 eruption stabs** (l.1061). Remove `+i` and set `scoop=0`. Alternate the F power voicing [29,41,48] with Gb [30,42,49] (phrygian). Carry the rise with `cut=700+200*i` and the eruptions only. If pitch must rise, use scale degrees only (F Gb Ab Bb C Db Eb F), never chromatic. Alternatively, swap the pulse stacks for `braam`-style saws at 0.18 s.
4. **Phone translation: the mix is muffled where an app promo is watched.** Phone-band LUFS is -21.5 vs -14.1. Fixes:
   - Rumble scale 0.3 -> 0.2 (l.1406).
   - `low` bus -1.5 dB (l.1455).
   - DRUMS +3 dB (l.1456).
   - Clap: add a 2-4.5 kHz crack layer (bp noise, tau 15 ms).
   - Hats: closed-hat level 0.32 -> 0.42.
   - Parallel bass harmonics: `sat(hp(bass,150),3)` at -12 dB before the low bus, so the 16th line exists on phones.
   - Acid: raise the soft ceiling at l.916 to 2800 Hz in 30-54 and the post-LP at l.921 to 3.5 kHz.

   Target: presence 2-6 kHz at -15 dB re total and phone-band within about 5.5 dB of full band. Re-check `high_tonal_beeps`; the noise peaks are fine.

## Improvements (priority order)
1. **Pre-drop vacuum** (49.88-50.0): gate SYN/SFX/DRUMS/HITS to -18 dB (multiply `mix` before `SG`), end the riser (l.1254) and the snare roll at 49.88, and let only a reverse-reverb suck through. Aim for >= 8 dB from 49.9 to 50.0. Do the same 58.88-59.0 for the final hit.
2. **Breakdown depth**: SG 40-45 0.9 -> 0.7 (l.1463-1464), drop the shaker for 40-42, and let heartbeat + pads + delayed acid carry it. Target -17.5 LUFS, so the 45-50 build and the drop feel bigger.
3. **Final ring-out** (l.1347-1350): braam `d=1.0` and pad `d=0.35, rel=0.3`, so the tail is about -30 dB by 59.7 and the 0.3 s fade only trims reverb. Keep the hall send.
4. **Harmony hygiene**:
   - Bass passing note: use `root+1` only when `chord_at` is Fm7/Fm9. Otherwise use `root+12`.
   - Eb chords -> Ebsus4 [51,56,58,63] / VO [39,46,51,56].
   - The acid follows chord: mute the Gb step on Eb and C, or transpose the acid root to `ROOT[chord]` on Db/Gb.
   - 49-50: use Db/C (C-Db-F-Ab), not C7.
5. **cool_sheen** (l.669): invert the sweep to 6 kHz->1.5 kHz (a decaying steam hiss) and lower it to 0.12. Or replace it with 2-3 low metal contraction ticks (`metal(0.1, 150, 700)`).
6. **Drop hop toks** (l.1303-1306): gain 1.0 -> 0.5, transient 0.65 -> 0.3, and fixed body 230 Hz (the current 240->300 Hz ascending 7-step reads as a little melody). They are on a 0.15 s grid against 16th hats, so keep them quiet.
7. **EDM snare-roll builds** (l.1036, l.1066, l.1248) are more Ibiza big-room than de Witte / Lens. For 45-50, use a kick/tom roll (`kick_s` lp 400 + `tom_s`) with hall-washed claps, and keep the snare as a quiet top layer.
8. **Groove variation 10-40**: the kick and bass drop out on all six whips. Keep the full mute on 20/30/40 only, and on 15/25/35 mute only P+4.75-5.0. Step the energy in tiers: SG 0.80/0.84/0.88 per 10 s, and replace the acid cut-off saw-tooth reset every 5 s (l.857-861) with one long ramp plus per-power-up wiggles.
9. **Drop width** (S/M -9.1 dB, no wider than the groove): add more hoover voices with +/-25 c decorrelated detune per side, send it to the hall at 0.35, and put a Haas 12 ms on the clap room return. Keep kick, bass and rumble mono.
10. **Small sync and hygiene items**:
    - Move the opening tok and transient from 0.035 to 0.003 (l.947-948).
    - Move the 55.99 transient to 55.997 (l.1334).
    - Make `lava_bed` mono below 140 Hz (l.933).
    - Add a sub thump at 7.225 so the w2 logo-sink lands under +20 ms (now +23).

## Brand fit
The right genre language for a Moorea / Klaan / Mattn festival app: F-minor rumble techno, acid, braams and industrial impacts. With the buzzer, the chromatic staircase and the sparkle gone, nothing reads as a game toy. What would still make it sound "cheap" to the client is the muffled, sub-heavy balance on phone or laptop speakers and the flat dynamics (a 30 s sausage). Fix those and it is a credible premium trailer bed.
