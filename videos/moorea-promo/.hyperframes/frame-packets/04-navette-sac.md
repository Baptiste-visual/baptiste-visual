# Frame packet: 04-navette-sac

## Project inputs

- Project: /home/user/baptiste-visual/videos/moorea-promo
- Design tokens: /home/user/baptiste-visual/videos/moorea-promo/frame.md
- RULES_DIR: /home/user/baptiste-visual/.claude/skills/hyperframes-animation/rules

## Assigned storyboard block

## Frame 4 — Bonus 1 & 2 : NAVETTE · SAC

- status: outline
- src: compositions/frames/04-navette-sac.html
- duration: 4.8s
- transition_in: cut
- scene: NAVETTE ? → the app's Navettes card falls red-hot, cools, NAVETTE CALÉE. ; SAC RECALÉ ? → the Objets interdits card lands, its signs brand one by one, TU SAIS AVANT.
- voiceover: (beat cues) P1=0.0 · land 0.8 · answer 1.2 · hop 1.6 · pan 2.0 · P2=2.4 · land 3.2 · branding 3.3–3.9 · answer 3.6 · hop 4.0 · pan 4.4
- blueprint: compose
- focal: the app cards (Navettes route card, then Objets interdits card)
- roles: assets/img/interdits-festival.jpg — the real forbidden-items grid inside the .mui-ban card · lava (tilt 0.55, horizon 0.16) — background
- asset_candidates: assets/img/interdits-festival.jpg
- sfx: 0.0 geyser whoosh · 0.4 falling whistle · 0.8 landing thud + lava splash · 0.8 pssht-TING quench · 1.2 answer stamp + coin · 1.6 jump boing · 2.0 whip-pan swoosh · 2.4 geyser · 2.8 fall · 3.2 thud + pssht-TING · 3.3–3.9 eight branding "tsk" stamps on 32nds · 3.6 stamp + coin · 4.0 jump · 4.4 whip

Standard power-up layout (see Video direction). Lava: tilt 0.55, horizon 0.16, heat 1.0, slow panX drift; L.panX +2.5
during each whip-pan.

- Scene 1 (0.00–0.40): "NAVETTE ?" erupts (`.fx-molten`, 150 px, centre (960, 250)).
- Scene 2 (0.40–0.80): the Navettes card falls red-hot from y −700 (rotation −8°→0): `.mui-card.r-lg` (source width
  831) holding a header row — `.mui-tile.navy` with MUI.icon('mdiBusSide') + "Navettes officielles" (Montserrat 700,
  40 px) — then `.mui-route`: head "Gare de Tours → Moorea Festival · 12 €", lines "Ven. 5 juin | 14h · 16h · 18h",
  "Sam. 6 juin | 15h · 17h", "Dim. 7 juin | 15h · 17h". Wrapper scale 1.15, centred x 960, card centre y≈640.
  `.fx-hot-overlay` + `.fx-hot-rim` children at opacity 1.
- Scene 3 (0.80–1.20): LAND on 0.80: squash (scaleY 0.94→1), shake ±10 px, lava erupt at (0.5, 0.93); QUENCH: hot
  overlay + rim 1→0 (0.4 s), lava coolR 0→0.45 at (0.5, 0.6); the problem word turns `.fx-stone` and sinks 30 px to
  0.35 opacity.
- Scene 4 (1.20–1.60): answer "NAVETTE CALÉE." (display 110 px, `.fx-hot-white`) stamps at y≈250 where the word was;
  "12 €" pulses (scale 1.25→1, orange glow) at 1.30; the three Friday times light up white→orange→white on 8ths
  1.30/1.40/1.50.
- Scene 5 (1.60–2.00): the orange "toi" dot (`.mui-you`, scale 1.6) hops in from (−60, 560) and lands on the card's top
  edge at (700, 300) — parabolic arc, squash on landing.
- Scene 6 (2.00–2.40): WHIP-PAN: card, answer and dot translate x −1800 with blur 0→16 px (power2.in); lava panX +2.5.
- Scene 7 (2.40–2.80): "SAC RECALÉ ?" erupts at (960, 250).
- Scene 8 (2.80–3.20): the Objets interdits card falls red-hot: `.mui-ban` with header `.mui-dot-title` +
  `.mui-display` "FESTIVAL" and ".z" "Appuyer pour zoomer", image assets/img/interdits-festival.jpg. Wrapper scale
  1.05, centre (960, 640).
- Scene 9 (3.20–3.60): LAND + QUENCH (as Scene 3, coolR at (0.5, 0.62)). 3.30–3.90: BRANDING — the 8 sign columns
  flash one per 32nd note (0.075 s apart): over each sign a white-orange radial glow (r 46 px) blinks 0→1→0 in 0.12 s
  plus a tiny smoke puff (grey circle scale 0.5→1.6, opacity 0.5→0). Sign centres in the image: x 102, 183, 263, 344,
  424, 504, 585, 666 · y 92, 202, 313 (image is 766×431 inside the card).
- Scene 10 (3.60–4.00): answer "TU SAIS AVANT." stamps at y≈250.
- Scene 11 (4.00–4.40): dot hops in from the left onto the card's top edge.
- Scene 12 (4.40–4.80): WHIP-PAN out (as Scene 6).
