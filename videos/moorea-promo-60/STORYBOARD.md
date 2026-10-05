---
format: 1920x1080
duration: 60s
message: "Au Moorea, sans l'appli c'est GAME OVER — avec elle, chaque galère devient un bonus : tout le festival dans une seule appli."
arc: Hook (GAME OVER) → Rejouer → Obstacles (8 galères) → 8 bonus = 8 vraies fonctions de l'appli → Niveau terminé → Marque + CTA
audience: Festivaliers 18-30 ans du Moorea Festival
mode: autonomous
tempo: 120 BPM — beat 0.5 s, bar 2 s, 30 bars = 60 s
music: original hard techno / hardstyle composed in-house (assets/audio), every hit on the grid
---

## Video direction

- **World**: the app's lava sea (shared WebGL engine `assets/kit/lava.js`, seed 3, GLOBAL time) + embers. Every UI element
  is a real app component from `assets/kit/moorea-ui.css` (see `frame.md`). Film typography = the app's display caps.
- **Game grammar**: a side-scrolling platformer. Each galère ERUPTS from the lava as a molten word; the matching app
  screen FALLS red-hot into the lava, lands on the beat with a splash, COOLS into the real navy card ("pssht-ting"),
  the problem word turns to stone, the answer STAMPS in white, the orange "toi" dot HOPS onto the new platform, then
  the camera WHIP-PANS left to the next obstacle.
- **Power-up rhythm** (P = power-up start): problem erupts P · card falls P+0.4 · lands P+0.8 · quench P+0.8–1.2 ·
  answer stamp P+1.2 · hop P+1.6–2.0 · whip-pan out P+2.0–2.4. The root HUD counter increments at every P+1.2.
- **Standard power-up layout**: problem / answer word centred at y≈250 (150 px display; 130 px if long); the card
  centred at x 960, y≈620; the "toi" dot enters from the left edge. Top 150 px = HUD zone from 4.8 s to 30.4 s.
- **Holds**: the film is deliberately relentless; the only breath is F07's first half (breakdown, heartbeat).
- **Cuts**: every frame boundary is a hard cut on a downbeat, prepared inside the outgoing frame (whip-pan blur,
  white-out or CRT collapse) — `transition_in: cut` everywhere.

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

## Frame 2 — REJOUER ?

- status: animated
- src: compositions/frames/02-rejouer.html
- duration: 2s (the 35 s cut, time-stretched ×1.25 = 150→120 BPM; all cue times below ×1.25)
- transition_in: cut
- scene: CRT turns back on to "REJOUER ?", "Cette fois, avec l'appli.", the app's orange button JOUER is pressed and the camera dives into it.
- voiceover: (beat cues) 0.0 REJOUER · 0.4 subline + button · 0.8 PRESS · 1.2 dive
- blueprint: compose
- focal: the app's orange button (.mui-btn-orange) labelled JOUER
- roles: app navy background #0f1722 + sparse embers — background
- asset_candidates: (none — kit components only)
- sfx: 0.0 CRT power-on thump + menu blip · 0.4 UI tick · 0.8 BIG button press: click + power-up coin chime + kick · 1.2 reverse-cymbal whoosh into the dive

- Scene 1 (0.00–0.40): app background `#0f1722` (full-bleed clip) with a sparse ember layer (count 30). CRT ON: the
  content wrapper opens from scaleY 0.008 to 1 in 0.12 s. "REJOUER ?" (display 150 px, white `.fx-hot-white`, centred,
  y≈380) slams at 0.00.
- Scene 2 (0.40–0.80): "Cette fois, avec l'appli." (Montserrat 600, 54 px, color #b4bcc6, centred y≈520) — words rise
  in on a 0.06 s stagger at 0.40. The app's orange button `.mui-btn-orange` (source width 760, label "JOUER",
  wrapper scale 1.0, centred, y≈700) pops in at 0.40 (scale 0→1.1→1).
- Scene 3 (0.80–1.20): PRESS on the downbeat 0.80: button scale 1→0.92 (0.06 s) →1.06→1 (back.out); an orange
  shockwave ring (border 6 px #e15311) expands from the button (scale 1→4, opacity 1→0, 0.4 s); the button's glow
  doubles; label flashes white.
- Scene 4 (1.20–1.60): zoom-through INTO the button: the wrapper scales 1→7 toward the button centre with blur 0→18 px;
  an orange-to-white flash fills the frame 1.40–1.60.

## Frame 3 — NIVEAU 1 · les galères jaillissent

- status: animated
- src: compositions/frames/03-niveau.html
- duration: 4s (the 35 s cut, time-stretched ×1.25 = 150→120 BPM; all cue times below ×1.25)
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

## Frame 5 — Bonus 3 & 4 : PERDU · ÇA CLASHE

- status: animated
- src: compositions/frames/05-plan-planning.html
- duration: 10s
- transition_in: cut
- scene: PERDU ? → the festival map rises out of the lava, pins drop, the Main Stage pin is tapped and a route draws from "toi": TU TE REPÈRES. ; ÇA CLASHE ! → pills collide, Mon planning rises, sets ticked one by beat, VALIDER: TU RATES RIEN.
- voiceover: (120 BPM beat cues) P3=0.0 · rise 0.5 · pins 1.0–2.25 · answer 1.5 · weather 2.0 · tap Main Stage 2.5 · route 3.0 · ping 3.5 · whip 4.5 · P4=5.0 · collision 5.25 · sheet 5.5 · answer 6.5 · ticks 7.0/7.5/8.0 · VALIDER 8.5 · hop 8.5–9.0 · whip 9.5
- blueprint: compose
- focal: the map island, then the Mon planning sheet
- roles: assets/img/map-island.png — the real isometric site map (hero) · assets/img/thumb-0.jpg (Klaan), thumb-2.jpg (Sound of Legend), thumb-4.jpg (Mattn) — planning thumbnails · lava — background
- asset_candidates: assets/img/map-island.png, assets/img/thumb-0.jpg, assets/img/thumb-2.jpg, assets/img/thumb-4.jpg
- sfx: 0.0 geyser · 0.5 rumble + rock grind · 1.0–2.25 six pin blips on 8ths · 1.5 stamp + coin · 2.0 weather blip · 2.5 tap + pop · 3.0 route draw zip · 3.5 sonar ping · 4.5 whip · 5.0 geyser · 5.25 metallic CLASH · 5.5 sheet swoosh · 6.5 stamp + coin · 7.0/7.5/8.0 checkbox clicks rising · 8.5 VALIDER thunk + flare · 9.0 land tick · 9.5 whip

REBUILD of the 35 s version on the 120 BPM grid. Keep components/look; extra time = showcase.

- Scene 1 (0.0–0.5): "PERDU ?" erupts at (960, 215), 130 px.
- Scene 2 (0.5–1.0): the map rises out of the lava hot and cools (as before), wrapper scale 0.92, centre (960, 620).
- Scene 3 (1.0–2.25): pins drop one per 8th from 1.0 (6 pins at the anchors). 1.5 answer "TU TE REPÈRES." stamps.
- Scene 4 (2.0–3.5) SHOWCASE: slow camera push on the map (×1.0→1.08 over 2.0–4.5, origin on Main Stage). 2.0 the
  `.mui-weather` chip "18°" pops (map top-left area, as before). 2.5 a white tap ripple on the red "4" Main Stage pin:
  the pin scales 1.35 and a label tag pops above it — a navy pill (#22364f, 2 px #3a4a61, r 20) with "MAIN STAGE" in the
  display font (28 px) and "Scène principale" (Montserrat 500, 20 px, #b4bcc6). 3.0 the orange `.mui-you` dot appears on
  the map (image px (500, 362)) and a dashed orange route (SVG path, stroke #e15311 5 px, dash 2 10, round caps) draws
  from it to the Main Stage pin (0.4 s). 3.5 sonar rings from the dot.
- Scene 5 (4.5–5.0): WHIP-PAN out.
- Scene 6 (5.0–5.5): left word zone: "ÇA CLASHE !" erupts at (520, 300); HALO and MAINSTAGE pills (scale 2.4) collide at
  (520, 520) at 5.25 with sparks, then ricochet out.
- Scene 7 (5.5–6.5): the Mon planning sheet (right half, wrapper scale 0.84, left x≈1010, top y≈200) rises:
  "MON PLANNING" + "0/12", "VENDREDI", rows Klaan / HALO / 18:00 → 19:00 · Sound of Legend / MAINSTAGE / 19:30 → 20:30 ·
  Mattn / MAINSTAGE / 21:00 → 22:00, then VALIDER. 6.5 answer "TU RATES RIEN." stamps in the left zone (y≈300).
- Scene 8 (7.0–8.5) SHOWCASE: one tick per BEAT — 7.0 Klaan, 7.5 Sound of Legend, 8.0 Mattn: each row first gets a soft
  highlight (#19283d), then its checkbox fills orange with the white check; the count rolls 1/12, 2/12, 3/12. Under the
  answer word (left zone, y≈420) a small app-style line appears at 7.0 and stays: "3 artistes ajoutés à ton planning"
  (Montserrat 600, 34 px, #b4bcc6) whose number counts 1→2→3 with the ticks. 8.5 VALIDER pressed (0.94→1.04→1, flare).
- Scene 9 (8.5–9.5): the dot hops onto the sheet's top edge (lands 9.0).
- Scene 10 (9.5–10.0): WHIP-PAN out.

## Frame 6 — Bonus 5 & 6 : J'AI FAIM · BRACELET À SEC

- status: animated
- src: compositions/frames/06-food-cash.html
- duration: 10s
- transition_in: cut
- scene: J'AI FAIM → category tiles + food-truck stack: À DEUX PAS., then the stack fans into a readable carousel, one truck per beat ; BRACELET À SEC → RECHARGER MON CASHLESS falls and cools: RECHARGÉ., then steps 1·2·3 one per beat.
- voiceover: (120 BPM beat cues) P5=0.0 · tiles 0.5–1.25 · stack 1.0–1.75 · answer 1.5 · carousel 2.0/2.5/3.0/3.5 · hop 3.5–4.0 · whip 4.5 · P6=5.0 · fall 5.5 · land 6.0 · answer 6.5 · steps 7.0/7.5/8.0 · security strip 8.5 · hop 8.5–9.0 · whip 9.5
- blueprint: compose
- focal: the food-truck cards, then the cashless button + steps
- roles: assets/img/cat-restaurants.png, cat-bars.png, cat-pizza.png, cat-glaces.png · assets/img/food-sto-dimos.jpg, food-bali-napoli.jpg, food-pasta.jpg, food-cabane-burger.jpg · lava — background
- asset_candidates: assets/img/cat-restaurants.png, assets/img/cat-bars.png, assets/img/cat-pizza.png, assets/img/cat-glaces.png, assets/img/food-sto-dimos.jpg, assets/img/food-bali-napoli.jpg, assets/img/food-pasta.jpg, assets/img/food-cabane-burger.jpg
- sfx: 0.0 geyser · 0.5–1.25 four pops · 1.0–1.75 four card slaps · 1.5 stamp + coin · 2.0/2.5/3.0/3.5 four carousel swishes + map-pin blip · 4.0 land tick · 4.5 whip · 5.0 geyser · 5.5 fall · 6.0 thud + pssht-TING · 6.5 stamp + cash coin · 7.0/7.5/8.0 numbered pings rising · 8.5 shield chime · 9.0 land tick · 9.5 whip

REBUILD of the 35 s version on the 120 BPM grid. Keep components/look; extra time = showcase.

- Scene 1 (0.0–0.5): "J'AI FAIM" erupts at (960, 230), 140 px.
- Scene 2 (0.5–1.25): the category tiles row pops tile by tile on 8ths (as before), with the app's line
  "Tous les restaurants proposent du végétarien" (Montserrat 400, 30 px, #b4bcc6, leaf icon mdiLeaf in green #60a23e if
  available, else no icon) under it at 1.25.
- Scene 3 (1.0–1.75): four food-truck cards slam onto a fanned stack on 8ths (as before). 1.5 answer "À DEUX PAS." stamps.
- Scene 4 (2.0–3.75) SHOWCASE: the stack spreads into a horizontal CAROUSEL: the four `.mui-food` cards (wrapper scale
  0.5 each, ≈462 px wide) line up centred at y≈700 with 24 px gaps; one card per BEAT becomes the focus (scale ×1.12,
  others dim to 0.55): 2.0 Sto Dimos, 2.5 Bali Napoli (Local), 3.0 Pasta é Basta, 3.5 La Cabane à Burger (Local); on
  each focus its round signpost button pulses orange (it opens the map in the app).
- Scene 5 (3.5–4.5): the dot hops onto the focused card (lands 4.0).
- Scene 6 (4.5–5.0): WHIP-PAN out.
- Scene 7 (5.0–5.5): "BRACELET À SEC" erupts at (960, 230), 130 px.
- Scene 8 (5.5–6.0): the `.mui-btn-glow` "RECHARGER MON CASHLESS" falls red-hot (wrapper scale 1.1, centre (960, 470)).
- Scene 9 (6.0–6.5): LAND + QUENCH. 6.5 answer "RECHARGÉ." stamps.
- Scene 10 (7.0–8.5) SHOWCASE: the `.mui-steps` row (wrapper scale 1.05, centre (960, 770)) — ONE step per BEAT: 7.0
  "1 Choisis ton montant", 7.5 "2 Paie en sécurité", 8.0 "3 Profite du festival", each number circle flashing orange then
  settling. 8.5 a slim app strip slides in under the steps (y≈960, centred, height 70): three items with dark inset tiles
  and white icons — mdiShieldCheck "3D Secure" · mdiShield "Paiement chiffré" · mdiCreditCardOutline "CB, Visa,
  Mastercard" (Montserrat 700, 26 px).
- Scene 11 (8.5–9.5): dot hops onto the button (lands 9.0). Scene 12 (9.5–10.0): WHIP-PAN out.

## Frame 7 — Bonus 7 & 8 : T'ES OÙ ?! · 1000 QUESTIONS

- status: animated
- src: compositions/frames/07-safety-mana.html
- duration: 10s
- transition_in: cut
- scene: (breakdown) T'ES OÙ ?! → Safety Mode: sharing on, compass locks on the group, Créer un groupe, SOS & CHAT: RETROUVE TA BANDE. ; (build) 1000 QUESTIONS → M.A.N.A: question typed, sent, answered, quick replies, a chip tapped: M.A.N.A RÉPOND., white-out into the drop.
- voiceover: (120 BPM beat cues) P7=0.0 · fall 0.5 · land + toggle 1.0 · lock 1.5 · answer 1.5 · group 2.0 · avatars 2.5 · SOS 3.0 · CHAT 3.5 · whip 4.5 · P8=5.0 · input 5.5 · typing 5.75–6.5 · send 6.5 · answer 6.5 · bubble 7.0 · chips 7.5–8.25 · warning 8.0 · chip tap 8.5 · riser 9.0 · white-out 9.5–10.0
- blueprint: compose
- focal: the Safety Mode card + SOS/CHAT, then the M.A.N.A chat
- roles: assets/img/tab-mana.png — M.A.N.A icon · kit components otherwise · lava (heat 0.55 in the breakdown) — background
- asset_candidates: assets/img/tab-mana.png
- sfx: (kick out until 5.0) 0.0 heartbeat + geyser · 1.0 thud + toggle click · 1.0–1.5 compass ticks + lock ping · 1.5 stamp + coin · 2.0 button press · 2.5 three soft pops · 3.0 glossy SOS glint · 3.5 CHAT bloop · 4.5 whip · 5.0 geyser + snare roll starts · 5.75–6.5 keyboard clicks · 6.5 send swoosh + stamp + coin · 7.0 message pop · 7.5–8.25 chip blips · 8.5 tap · 9.0–10.0 riser to the drop

REBUILD of the 35 s version on the 120 BPM grid. Keep components/look; extra time = showcase.

- Scene 1 (0.0–0.5): "T'ES OÙ ?!" erupts at (960, 230), 140 px. Breakdown mood: lava heat 0.55, embers slow.
- Scene 2 (0.5–1.0): the Safety Mode card falls (as before: header "SAFETY MODE" + "bêta", "Partage de position" +
  toggle, "Boussole" + compass). ADD under the toggle row the app's "Mon groupe" row: "Mon groupe" (Montserrat 700,
  34 px) + "Rejoignez pour les alertes SMS & la boussole" (Montserrat 400, 26 px, #69707a) + two buttons
  `.mui-grpbtn.fill` "Créer un groupe" and `.mui-grpbtn.line` "Rejoindre" side by side. Keep the card's top y≈300 and
  scale it so it ends above y 960.
- Scene 3 (1.0–1.5): LAND + QUENCH; 1.0 the toggle flips ON; the compass arrow spins and LOCKS at 1.5 (40°) with a ping.
- Scene 4 (1.5–2.0): answer "RETROUVE TA BANDE." stamps at y≈230.
- Scene 5 (2.0–3.5) SHOWCASE: 2.0 "Créer un groupe" is pressed (tap ripple, scale 0.95→1); 2.5 three small orange avatar
  dots pop one per 8th on the compass rim around 40°; 3.0 the glossy red `.mui-sos` pops on the right (centre (1420, 560))
  with a glint sweep; 3.5 the gold `.mui-chatbtn` pops (centre (1680, 640)), then the app's two-line hint "Maintenez SOS
  pour alerter · / CHAT pour le groupe." under them. Respectful: no alarm flashing.
- Scene 6 (4.5–5.0): WHIP-PAN out.
- Scene 7 (5.0–5.5): "1000 QUESTIONS" erupts at (960, 215), 120 px, with the "?" swarm.
- Scene 8 (5.5–6.5): the M.A.N.A input bar slides up at 5.5; 5.75–6.5 the question types in: "Les douches ouvrent à
  quelle heure ?"; 6.5 send pressed; the swarm is sucked into the send button. 6.5 answer "M.A.N.A RÉPOND." stamps.
- Scene 9 (7.0–8.5) SHOWCASE: header "M.A.N.A" + icon; 7.0 the answer bubble pops: "Dimanche, les douches sont
  ouvertes de 8h à 20h." + `.hr`; chips "Programme", "Où manger ?", "Navettes", "Artistes ce soir" pop one per 8th
  7.5–8.25; 8.0 the red warning line; 8.5 a tap ripple on the "Navettes" chip which turns `.mui-chip.on` (navy).
- Scene 10 (9.0–10.0): riser — everything vibrates, lava heat →1.8, white-out L.flash 0→1 from 9.5 to 10.0 → cut.

## Frame 8 — NIVEAU TERMINÉ (drop)

- status: animated
- src: compositions/frames/08-niveau-termine.html
- duration: 4s (the 35 s cut, time-stretched ×1.25 = 150→120 BPM; all cue times below ×1.25)
- transition_in: cut
- scene: DROP — NIVEAU TERMINÉ slams with an ember explosion, 8/8 GALÈRES ÉVITÉES, the camera pulls back over the path of 8 cooled app cards to the festival, TOUT LE FESTIVAL. UNE SEULE APPLI.
- voiceover: (beat cues) 0.0 DROP slam · 0.4 8/8 · 1.2 pull-back · 1.2–2.2 eight hops · 2.4 tagline 1 · 2.8 tagline 2
- blueprint: compose
- focal: NIVEAU TERMINÉ, then the path of platforms
- roles: assets/img/photo-crowd-gate.jpg — the festival entrance (the level's goal) · lava (blazing) — background
- asset_candidates: assets/img/photo-crowd-gate.jpg
- sfx: 0.0 DROP: hardstyle kick + crash + crowd roar + ember burst · 0.4 slot-machine spin to 8/8 + win jingle · 1.2 big whoosh pull-back · 1.2–2.2 eight jump blips rising · 2.2 goal fanfare stab · 2.4 / 2.8 two slams

- Scene 1 (0.00–0.40): white flash 1→0 (0.15 s); lava top-down blazing (heat 2.0, zoom 1.2); embers boost 4 and
  rising fast. "NIVEAU" / "TERMINÉ" (display 190 px, `.fx-hot-white`, stacked, centred, y≈300 and y≈490) SLAM at 0.00
  (both together) with a big shake ±18 px.
- Scene 2 (0.40–1.20): "8/8" (display 200 px, orange #e15311 with glow, centred y≈700) spins in like a slot reel
  (digits 1…8 scroll vertically, landing at 0.70) + "GALÈRES ÉVITÉES" (Montserrat 700, 44 px, letter-spacing 0.2em,
  white, y≈830) at 0.70.
- Scene 3 (1.20–2.40): PULL-BACK: the type scales to 0.42 and moves to the top band (centre y≈220) while the lava
  zooms out (zoom 1.2→0.55). A path of 8 small cooled app platforms appears along an S-curve from bottom-left
  (180, 960) to top-right (1500, 470): each platform = a 150×96 navy card (#142030, r14, 2 px #22364f border) with
  its app icon in orange (MUI.icon names in order: mdiBusSide, mdiCancel, mdiMapMarker, mdiCalendarCheck,
  mdiSilverwareForkKnife, mdiCreditCardOutline, mdiCompassOutline, mdiMessage); they pop in quickly 1.20–1.50
  (stagger 0.04). The goal at the end: the festival entrance photo (assets/img/photo-crowd-gate.jpg, 420×236,
  r22, orange 4 px glow border) at (1640, 400). The `.mui-you` dot hops platform to platform on 16ths×2
  (1.30, 1.42, … 8 hops, ~0.12 s each) and lands in the photo at 2.25 → orange burst ring.
- Scene 4 (2.40–3.20): taglines over the path: "TOUT LE FESTIVAL." (display 96 px, white, centred, y≈780) slams at
  2.40; "UNE SEULE APPLI." (display 96 px, orange, y≈900) slams at 2.80.

## Frame 9 — L'appli officielle (end card)

- status: animated
- src: compositions/frames/09-end.html
- duration: 6s (the 35 s cut, time-stretched ×1.25 = 150→120 BPM; all cue times below ×1.25)
- transition_in: cut
- scene: The chrome MOOREA sun rises over the lava, drops into the app's tab bar, L'APPLI OFFICIELLE · 5-7 juin 2026 · App Store / Google Play, PRÊT À JOUER ? and the orange button TÉLÉCHARGE L'APPLI pressed on the last hit.
- voiceover: (beat cues) 0.0 sunrise · 1.0 tab bar · 1.6 logo lands in the centre button · 1.6 title · 2.0 date · 2.4/2.6 stores · 3.0 prêt à jouer · 3.2 button · 4.0 PRESS (last hit) · 4.4 hold
- blueprint: compose
- focal: the chrome logo, then the orange download button
- roles: assets/img/logo-chrome.png — brand mark (hero) · assets/img/sun-orange.png — the tab bar's centre sun · assets/img/tab-lineup.png, tab-plan.png, tab-mana.png, tab-infos.png — tab bar icons · lava horizon at dusk — background
- asset_candidates: assets/img/logo-chrome.png, assets/img/sun-orange.png, assets/img/tab-lineup.png, assets/img/tab-plan.png, assets/img/tab-mana.png, assets/img/tab-infos.png
- sfx: 0.0 choir-ish supersaw swell + shimmer · 1.0 tab bar slide · 1.6 magnetic snap + sparkle · 2.0 tick · 2.4/2.6 two blips · 3.0 tick · 3.2 button pop · 4.0 FINAL HIT: kick + crash + press click · 4.4 tail

The final frame: it may settle at the end (no other exits).

- Scene 1 (0.00–1.00): lava horizon view at dusk (tilt 0.9, horizon 0.58, heat 0.9); behind the horizon a huge soft
  orange sun glow (radial gradient, 1400 px). The chrome logo (assets/img/logo-chrome.png, scale 1.5 ≈ 855×495)
  RISES from behind the horizon (y +420 → centre y≈360) like a sunrise with heat shimmer (a slow skewX ±0.6° wobble on
  8ths) and its glow brightening.
- Scene 2 (1.00–1.60): the app's tab bar (`.mui-tabbar`, wrapper scale 1.5 ≈ 1385×300, centred x, bottom edge at
  y 1080; items "Line up", "Plan", centre, "M.A.N.A", "Infos" with the tab-*.png icons) slides up from y +320 at 1.00;
  the logo shrinks and FALLS into the tab bar's raised centre circle (scale 1.5→0.18, path to the circle centre) and at
  1.60 is swapped for assets/img/sun-orange.png with a white flash + orange ring; the centre label "Accueil" lights
  orange (add the label under the circle).
- Scene 3 (1.60–2.40): "L'APPLI OFFICIELLE" (display 100 px, white, centred, y≈230) slams at 1.60; "5 · 6 · 7 JUIN
  2026 · CHÂTEAU DE GRILLEMONT" (Montserrat 600, 40 px, #b4bcc6, letter-spacing 0.08em, y≈330) at 2.00.
- Scene 4 (2.40–3.20): two navy store pills (`.mui-seg.on` style: navy fill, #3a4a61 border, 90 px tall, white
  Montserrat 700 34 px) side by side, centred at y≈450, gap 36 px: [MUI.icon('mdiApple') 44 px] "App Store" pops at
  2.40, [MUI.icon('mdiGooglePlay') 44 px] "Google Play" at 2.60. 3.00: "PRÊT À JOUER ?" (display 48 px, orange,
  y≈560).
- Scene 5 (3.20–4.00): the app's orange button `.mui-btn-orange` labelled "TÉLÉCHARGE L'APPLI" (source width 760,
  wrapper scale 1.2, centred, y≈660) pops at 3.20 and breathes (scale 1↔1.03 on beats 3.6).
- Scene 6 (4.00–4.80): FINAL HIT at 4.00: button pressed (0.92 → 1.06 → 1), orange shockwave ring, white flash 0.5→0,
  embers burst upward (boost 4 → 1); 4.40–4.80 hold (subtle ember drift only).
