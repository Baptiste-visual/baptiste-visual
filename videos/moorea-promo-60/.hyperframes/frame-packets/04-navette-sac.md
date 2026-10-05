# Frame packet: 04-navette-sac

## Project inputs

- Project: /home/user/baptiste-visual/videos/moorea-promo-60
- Design tokens: /home/user/baptiste-visual/videos/moorea-promo-60/frame.md
- RULES_DIR: /home/user/baptiste-visual/.claude/skills/hyperframes-animation/rules

## Assigned storyboard block

## Frame 4 — Bonus 1 & 2 : NAVETTE · SAC

- status: animated
- src: compositions/frames/04-navette-sac.html
- duration: 10s
- transition_in: cut
- scene: NAVETTE ? → the Navettes card falls red-hot, cools, NAVETTE CALÉE., then the card is explored line by line ; SAC RECALÉ ? → the Objets interdits card lands, signs brand, TU SAIS AVANT., then the camera zooms into the grid like the app's "Appuyer pour zoomer".
- voiceover: (120 BPM beat cues) P1=0.0 · fall 0.5 · land 1.0 · answer 1.5 · showcase 2.0/2.5/3.0/3.5 · hop 3.5–4.0 · whip 4.5 · P2=5.0 · fall 5.5 · land 6.0 · branding 6.1–6.6 · answer 6.5 · zoom showcase 7.0/7.5/8.0/8.5 · hop 8.5–9.0 · whip 9.5
- blueprint: compose
- focal: the app cards (Navettes, then Objets interdits)
- roles: assets/img/interdits-festival.jpg — the real forbidden-items grid inside the .mui-ban card · lava (tilt 0.55, horizon 0.16) — background
- asset_candidates: assets/img/interdits-festival.jpg
- sfx: 0.0 geyser · 0.5 fall whistle · 1.0 thud + splash + pssht-TING · 1.5 stamp + coin · 2.0/2.5/3.0 three row blips (rising) · 3.5 soft notification pop · 3.5 jump · 4.0 land tick · 4.5 whip · 5.0 geyser · 5.5 fall · 6.0 thud + pssht-TING · 6.1–6.6 eight branding tsk · 6.5 stamp + coin · 7.0 zoom-in whoosh · 7.5 / 8.0 two slide swishes · 8.5 zoom-out whoosh · 8.5 jump · 9.0 land tick · 9.5 whip

REBUILD of the 35 s version on the 120 BPM grid (beat 0.5 s). Keep the existing components and look; animations stay
snappy (same speeds as before), the extra time goes into SHOWCASE beats where the app card stays big and readable.

- Scene 1 (0.0–0.5): "NAVETTE ?" erupts (`.fx-molten`, 150 px, centre (960, 250)).
- Scene 2 (0.5–1.0): the Navettes card falls red-hot (same build as before: `.mui-card.r-lg` with the navy bus tile +
  "Navettes officielles", then TWO `.mui-route` sub-cards: (a) "Gare de Tours → Moorea Festival · 12 €" with
  "Ven. 5 juin | 14h · 16h · 18h", "Sam. 6 juin | 15h · 17h", "Dim. 7 juin | 15h · 17h" and (b) "Moorea Festival → Gare de
  Tours · 12 €" with "Sam. 6 juin | 2h45", "Dim. 7 juin | 2h45", "Lun. 8 juin | 1h45 · 12h" — (b) starts hidden).
  Wrapper scale 0.95, card top at y≈330.
- Scene 3 (1.0–1.5): LAND + QUENCH (as before).
- Scene 4 (1.5–2.0): answer "NAVETTE CALÉE." stamps at y≈250; "12 €" pulses.
- Scene 5 (2.0–3.5) SHOWCASE: a slow camera push on the card (scale ×1.0→1.06 over 2.0–4.5). 2.0 the Friday line
  lights (row tint #22364f, times flash white→orange on 8ths 2.0/2.25/2.5); 2.5 Saturday line lights; 3.0 the return
  sub-card (b) slides down open under (a) (height reveal via clip-path inset, 0.25 s, back.out) and its "2h45" values
  flash; 3.5 under the routes, the app's bold line "Réservation obligatoire via la billetterie du festival." (Montserrat
  700, 35 px, white) types in quickly (0.3 s).
- Scene 6 (3.5–4.5): the "toi" dot hops in from the left and lands on the card's top edge at 4.0 (ring pulse).
- Scene 7 (4.5–5.0): WHIP-PAN out (x −1800, blur 0→16 px, lava panX +2.5).
- Scene 8 (5.0–5.5): "SAC RECALÉ ?" erupts at (960, 250).
- Scene 9 (5.5–6.0): the Objets interdits card (`.mui-ban`, FESTIVAL, "Appuyer pour zoomer", interdits-festival.jpg)
  falls red-hot; wrapper scale 1.05, centre (960, 640).
- Scene 10 (6.0–6.5): LAND + QUENCH; 6.1–6.6 BRANDING flashes column by column (0.0625 s apart).
- Scene 11 (6.5–7.0): answer "TU SAIS AVANT." stamps.
- Scene 12 (7.0–8.5) SHOWCASE "Appuyer pour zoomer": 7.0 a white tap ripple on the image, then the IMAGE zooms ×2.1
  inside its rounded frame (overflow hidden, transform-origin on the top row, left half) so the signs + captions
  "BOISSONS ET BOUTEILLES…", "ENGINS PYROTECHNIQUES", "ARMES" are readable; 7.5 it pans to the top row's right half
  ("VÉLOS ET TROTTINETTES", "MATÉRIEL DE CAMPING"); 8.0 it pans down to the middle row ("DRONES", "POINTEURS LASERS",
  "ANIMAUX"…); 8.5 it zooms back out to the full grid (0.3 s, power3.out).
- Scene 13 (8.5–9.5): dot hops onto the card (lands 9.0).
- Scene 14 (9.5–10.0): WHIP-PAN out.
