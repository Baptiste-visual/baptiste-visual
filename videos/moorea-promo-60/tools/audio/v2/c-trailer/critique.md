# Critique: direction C "trailer hybrid" (mix.wav / mix.mp3)

Reviewer: senior music supervisor / mix engineer. Judged from the code and from measurements, without listening.

## Measurements
- analyze.py output: -14.02 LUFS, -1.05 dBTP, length OK, DC ~0, no click candidates, 4 high tonal beeps (braam / pad / choir harmonics at 1.85-2.16 kHz; the old mix had 332).
- Cue sync: 280 cues, median offset 4 ms. All 32 weight-3 cues are within -7.3..0 ms. The only weak weight-2 cue is 0.000, which the analyser cannot pass by design; 41.0 is at -24 ms.
- MP3: -14.43 LUFS, -1.18 dBTP. Decoded with gapless info it has 2,880,000 samples at lag 0. A decoder that ignores the LAME header plays it 1105 samples (23 ms) late; that is under one frame.
- Stems were rebuilt from a scratch copy of compose.py; the scratch render is bit-identical to the delivered mix.wav.

| section | LUFS | LUFS after a 180 Hz HP (phone-like) | mono fold-down | crest |
|---|---|---|---|---|
| hook | -14.1 | -16.0 | -2.4 dB | 14.3 |
| level | -14.8 | -18.7 | -1.1 | 13.4 |
| power-ups | -14.2 | -17.2 | -1.1 | 13.7 |
| breakdown | -19.5 | -21.9 | -2.0 | 19.2 |
| build | -13.2 | -15.8 | -1.4 | 13.2 |
| **drop** | **-12.2** | **-16.0 (loses 3.8 dB, the most of any section)** | -1.2 | 11.0 |
| outro | -13.0 | -15.1 | -2.4 | 12.9 |

- RMS above 180 Hz: build 48-49.9 = -17.9 dB, drop 50-52 = -18.5, drop 52-54 = -19.5, power-ups 34-36 = -18.7. On a phone or laptop, the drop is quieter than the build before it.
- Final ring-out, total RMS per 50 ms: 59.0 +1.5, 59.4 +0.9, 59.7 +0.3, 59.8 0.0, then the fade. The music bus rises from -5.2 dB at 59.0 to -1.2 dB at 59.4 (duck release + choir with rel 1.2 s + mhall 0.8). Nothing decays, so the last-0.3 s fade does all the work.
- UI bus vs music: 14-18 dB under the music on most cues. The loud exceptions are the counter clacks (g 2.8, about -4.5 dB at 12.12), 22.56 (-4.2), 48.5 (-7.4), and the drop hops at 51.76-52.68 (-5 to -7).
- Side-chain: music pumps 3.3 dB in the power-ups and 4.7 dB in the drop; bass pumps 17.5 dB in the drop.

## Blocking issues
1. **The drop at 50.0 does not land on small speakers.** Its energy is in the sub (sub<60 -2.5 dB vs total, presence -18.3 dB, the darkest section). Section gain is *lower* in the drop (1.3) than at the end of the build (1.45), at line 1394. The reese is low-passed at 500-800 Hz (lines 713 and 935). Fixes:
   - Set sg to build 1.15-1.25 and drop 1.45.
   - Lower the drop sub sine from 0.75 to 0.45 (line 944) and the 50.0 sub_drop from 0.7 to 0.45.
   - Add a driven mid layer to the reese: band-pass 200 Hz-1.8 kHz, tanh 3, LP cutoff about 1.4 kHz, kept mono.
   - Raise the drop pad LP from 2400 to 4500 Hz and its gain from 0.3 to 0.4.
   - Add +3 dB at 2-5 kHz on the drop clap/snare, plus a 16th closed-hat or ride layer.
   - Target: drop at least 2.5 dB above the build after the 180 Hz HP.
2. **The final hit at 59.0 never rings out.** The level is flat from 59.0 to 59.8 and the music swells back up, so the end sounds like a fade or cut.
   - Line 956: choir 59.0 att 0.01 / rel 1.2 / g 0.7 / mhall 0.8. Use an exponential decay instead (ar(dec≈0.35)), with g 0.5 and mhall 0.5.
   - Line 1327: DH (59.0, 0.5, 0.6). Use depth 0.6 and release ≥1.2 s so the duck never recovers inside the film.
   - Line 1319: shorten the braam envelope (d 1.7 → env dec ≈ 0.4 s).
   - Target: tail at least 12 dB below the hit by 59.7, and about -24 dB by 59.95.

## Improvements
- **Cheap or game-cliché residue:**
  - The "denied" glitch (lines 637-649, used at 2.5) is detuned A1/Bb1/E2 saws, quantised and gated. That reads as a quiz-show "wrong answer" buzzer, and it is out of key. Rebuild it from a stutter or bit-crush of the real OVER braam tail (like the rewind), tuned to F/Gb.
  - The rising saw "charge" at 36.5 (line 1206, 55→115 Hz) is a pitch-up "vwoop". Remove it or replace it with a filtered-noise charge.
  - The overheat at 9.0 (lines 790-796) loops the C-E-G-C major triad as a 16th arpeggio. Use a tremolo on C+G with a Db (C7b9) cluster instead.
- **SFX clutter in the drop:**
  - 51.7625-52.675 (lines 1280-1286) stacks 7 thump+tok (g 2.0) + steam on a 150 ms grid against the 4/4 kick. Keep 51.7625 and 52.8125 and let the hats carry the hops; drop the steams.
  - Counter clack g 2.8 (line 1086): lower to 1.6.
- **Arrangement vs picture:** the power-up phases change at 18 / 26 / 34 (line 805), in the middle of power-ups, not on the picture transitions. Use 3 × 10 s phases (10 / 20 / 30), so layers enter on the 20.0 and 30.0 whip-pan cuts, and add a per-power-up variation (alternate ostinato pattern, tom fill into every P+4.5 whip).
- **Low-end overall:**
  - Groove sub<60 is -3.4 dB and mids -10.7 dB.
  - High-pass the taiko and eruptions at 40 Hz and shorten the kick hold (25 → 10 ms) in the power-ups.
  - The sub register jumps: F 43.6 / Gb 46 / C 65 / Db 69 / Eb 78 Hz (lines 330, 853). Keep every root at 36-52 Hz.
- **GAME (1.0) is 3 dB weaker than OVER above 180 Hz.** Fine as escalation, but bring GAME up about 1.5 dB with a brighter crack layer.
- **Section gain steps:** sg/sgm jump within one sample at 10.0, 40.0 (-9 dB on the music bus and the hall return), 45.0 and 54.0 (lines 1394-1396). They are masked now, but should get 20-30 ms ramps.
- **Width:** hook and outro fold down 2.4 dB in mono (corr 0.35-0.39). Use side ×1.0 instead of 1.15 in those sections, or narrow the choir's mhall send.
- **Choir realism** (lines 680-689): use more voices per note (8+), narrower formant Q for 3 formants plus a chorus/ensemble, and less saw edge. If it still reads as a "synth vox", replace it with a dark analog pad in the drop.
- **MP3 delivery:** tell the client the file is gapless-tagged. If their NLE ignores the tag, the audio is 23 ms late (under one frame); nudge -1 frame only if they see it.

## Scores
Maturity 7, brand fit 6, technical 6, sync 9.
