# Frame packet: 01-game-over

## Project inputs

- Project: /home/user/baptiste-visual/videos/moorea-promo-60
- Design tokens: /home/user/baptiste-visual/videos/moorea-promo-60/frame.md
- RULES_DIR: /home/user/baptiste-visual/.claude/skills/hyperframes-animation/rules

## Assigned storyboard block

## Frame 1 — GAME OVER

- status: animated
- src: compositions/frames/01-game-over.html
- duration: 4s (the 35 s cut, time-stretched ×1.25 = 150→120 BPM; all cue times below ×1.25)
- transition_in: cut
- scene: The orange "toi" dot sinks into boiling lava, GAME OVER erupts, "Tu as raté Sound of Legend.", then the tape rewinds.
- voiceover: (no voice-over — beat cues) 0.4 plop · 0.8 GAME · 1.2 OVER · 1.6 subline + artist card · 2.4 rewind
- blueprint: compose
- focal: GAME OVER display type (.fx-gameover)
- roles: assets/img/artist-sound-of-legend.jpg — the missed artist, line-up card (supporting) · lava + embers — background
- asset_candidates: assets/img/artist-sound-of-legend.jpg
- sfx: 0.0 lava bubbling + descending 3-note lose blip · 0.4 deep plop + sizzle · 0.8 SUB BOOM + distorted kick + 8-bit game-over arpeggio · 1.2 second slam · 1.6 glitch "denied" buzz · 2.4 tape-rewind squeal · 3.0 CRT power-off zap

Frame 0 is already in motion — never a black or empty first frame.

- Scene 1 (0.00–0.40): top-down lava (tilt 0.25, heat 1.0, zoom 1.25 pushing to 1.35 over the whole frame). Centre
  (960, 560): the app's orange location dot `.mui-you` at scale 2.4 is SINKING — scale 2.4→1.5, y +0→+24, its white ring
  pulsing; three ripple rings (2 px orange/white circles) expand from it (radius 40→220, opacity 0.8→0) at 0.0/0.13/0.26.
- Scene 2 (0.40–0.80): 0.40 the dot is swallowed (scale→0 in 0.12 s); lava erupt at (0.5, 0.52) 0→1→0 over 0.4 s;
  embers boost 1→2.5.
- Scene 3 (0.80–1.60): SLAM "GAME" (display 250 px, `.fx-gameover`, centred x 900, baseline row y≈430) at 0.80;
  SLAM "OVER" (same style, y≈660) at 1.20. Each slam: from scale 2.6, 0.18 s power4.in, back.out settle, 1-frame white
  flash overlay, shake ±12 px; lava heat jumps to 1.6 and L.flash 0.35→0 on each slam.
- Scene 4 (1.60–2.40): right side (x 1300–1700, y 300–670): the real line-up card `.mui-artist` (Sound of Legend
  image, caption "Sound of Legend" / "19:30-20:30") flips in (rotateY 90°→0, 0.25 s) at 1.60; under GAME OVER the
  subline "Tu as raté Sound of Legend." (Montserrat 600, 52 px, white, x-centred on GAME OVER, y≈830) slides up at 1.80;
  at 2.00 the card goes dead: grayscale 1, brightness 0.45, a 6° drop and a red 4 px border flash.
- Scene 5 (2.40–3.20): REWIND. Top-left (x 110, y 90) a white rewind glyph (MUI.icon('mdiRewind'), 90 px) blinks on
  8ths; 3 horizontal VHS tracking bands (full width, 40–90 px tall, white 8–15 % opacity) scroll up the frame;
  `.fx-rgb` split on all type (--gx 0→18); type and card jitter (x ±8 px on 16ths); the lava runs BACKWARDS
  (L.t from 2.4 back to 0.8) and embers fall (rise −3). 3.00–3.20 CRT power-off: the whole content wrapper scaleY
  1→0.008 then scaleX 1→0 with a white line — the frame ends on black + a white dot.
