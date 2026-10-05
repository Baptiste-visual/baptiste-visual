# Frame packet: 03-niveau

## Project inputs

- Project: /home/user/baptiste-visual/videos/moorea-promo
- Design tokens: /home/user/baptiste-visual/videos/moorea-promo/frame.md
- RULES_DIR: /home/user/baptiste-visual/.claude/skills/hyperframes-animation/rules

## Assigned storyboard block

## Frame 3 — NIVEAU 1 · les galères jaillissent

- status: outline
- src: compositions/frames/03-niveau.html
- duration: 3.2s
- transition_in: cut
- scene: "NIVEAU 1" + the chrome MOOREA logo over the lava horizon, they sink, then 8 molten problem words erupt across the lava, white-out.
- voiceover: (beat cues) 0.0 NIVEAU 1 · 0.2 logo · 0.8 sink · 0.8–2.2 eight eruptions on 8ths · 2.4–3.2 overheat + white-out
- blueprint: compose
- focal: the eight problem words
- roles: assets/img/logo-chrome.png — brand mark (supporting) · lava horizon — background
- asset_candidates: assets/img/logo-chrome.png
- sfx: 0.0 impact + level-start square-wave arpeggio up · 0.8 lava splash · 0.8–2.2 eight geyser fire-whooshes + rising acid stabs (one per word, +1 semitone each) · 2.4–3.2 white-noise riser · 3.2 hit

HUD zone active from this frame on: keep everything below y 150.

- Scene 1 (0.00–0.80): lava in horizon view (tilt 0.85, horizon 0.30, heat 1.0); the camera swoops forward over it
  (L.panY 0→6 over the frame, power2.out). "NIVEAU 1" (display 120 px, orange #e15311 with orange glow, centred,
  y≈330) slams at 0.00; the chrome logo (assets/img/logo-chrome.png at 0.95 scale ≈ 540×314, centred, y≈470–785)
  drops in at 0.20 (y −200→0, back.out(2)).
- Scene 2 (0.80–1.20): both sink into the lava: y +320, scale 0.75, opacity 1→0 in 0.35 s (power2.in); lava erupt at
  (0.5, 0.75) 0→1→0.
- Scene 3 (0.80–2.40): EIGHT eruptions, one per 8th note starting 0.80 (0.80, 1.00 … 2.20), each a `.fx-molten`
  display word with the "erupt" motion + a small lava erupt at its foot. Centres / sizes: "NAVETTE ?" (330, 300) 92 px ·
  "SAC RECALÉ ?" (1500, 290) 84 px · "PERDU ?" (960, 450) 124 px · "ÇA CLASHE !" (430, 600) 108 px ·
  "J'AI FAIM" (1460, 570) 108 px · "BRACELET À SEC" (780, 760) 100 px · "T'ES OÙ ?!" (1560, 830) 116 px ·
  "1000 QUESTIONS" (380, 900) 92 px. Words stay; each wobbles (rotation ±2°, scale 1↔1.04) on every beat.
- Scene 4 (2.40–3.20): overheat — lava heat 1→1.9, embers boost 1→4, all words pulse bigger on the beats 2.4 and 2.8;
  L.flash 0→1 from 2.80 to 3.20 (white-out) → hard cut.
