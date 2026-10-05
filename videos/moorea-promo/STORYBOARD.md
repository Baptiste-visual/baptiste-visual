---
format: 1920x1080
duration: 35.2s
message: "Au Moorea, sans l'appli c'est GAME OVER — avec elle, chaque galère devient un bonus : tout le festival dans une seule appli."
arc: Hook (GAME OVER) → Rejouer → Obstacles (8 galères) → 8 bonus = 8 vraies fonctions de l'appli → Niveau terminé → Marque + CTA
audience: Festivaliers 18-30 ans du Moorea Festival
mode: autonomous
tempo: 150 BPM — beat 0.4 s, bar 1.6 s, 22 bars = 35.2 s
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
- duration: 3.2s
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
- duration: 1.6s
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

## Frame 4 — Bonus 1 & 2 : NAVETTE · SAC

- status: animated
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

## Frame 5 — Bonus 3 & 4 : PERDU · ÇA CLASHE

- status: animated
- src: compositions/frames/05-plan-planning.html
- duration: 4.8s
- transition_in: cut
- scene: PERDU ? → the festival map rises out of the lava, pins drop, the toi dot pings: TU TE REPÈRES. ; ÇA CLASHE ! → HALO and MAINSTAGE pills collide, Mon planning rises, 3 sets ticked, VALIDER: TU RATES RIEN.
- voiceover: (beat cues) P3=0.0 · map rises 0.4 · pins 0.8–1.8 · answer 1.2 · ping 1.4 · pan 2.0 · P4=2.4 · collision 2.6 · sheet 2.8 · ticks 3.2/3.4/3.6 · answer 3.6 · VALIDER 3.8 · hop 4.0 · pan 4.4
- blueprint: compose
- focal: the map island, then the Mon planning sheet
- roles: assets/img/map-island.png — the real isometric site map (hero) · assets/img/thumb-0.jpg (Klaan), thumb-2.jpg (Sound of Legend), thumb-4.jpg (Mattn) — planning thumbnails · lava — background
- asset_candidates: assets/img/map-island.png, assets/img/thumb-0.jpg, assets/img/thumb-2.jpg, assets/img/thumb-4.jpg
- sfx: 0.0 geyser · 0.4 deep rumble + rock grind + drips · 0.8–1.8 six pin-drop blips (pitched) · 1.0 weather chip blip · 1.2 stamp + coin · 1.4 sonar ping · 2.0 whip · 2.4 geyser · 2.6 metallic CLASH + sparks · 2.8 sheet swoosh · 3.2/3.4/3.6 checkbox clicks rising · 3.6 stamp + coin · 3.8 VALIDER thunk + flare · 4.0 jump · 4.4 whip

- Scene 1 (0.00–0.40): "PERDU ?" erupts at (960, 215), 130 px.
- Scene 2 (0.40–0.80): the map RISES out of the lava: assets/img/map-island.png (909×758) in a wrapper at scale 0.92,
  centred (960, 620); from y +520, rotationX 55°→0 (perspective 1600 px), red-hot tint (filter sepia/brightness or a
  `.fx-hot-overlay` masked to the image alpha via mask-image) cooling to the real green by 0.9; lava erupt along its
  base (eruptY 0.95). The problem word turns to stone at 0.8.
- Scene 3 (0.80–1.80): PINS drop one per 8th from 0.80 (y −140→0, bounce): place `.mui-pin` at the map's anchor
  centres (image px, scale them with the wrapper): navy "9" (169,233), orange "6" (373,239), orange "11" (484,176),
  red "4" (556,306), navy "9" (668,363), cyan "4" (829,374). 1.00: the `.mui-weather` chip (cloud icon
  MUI.icon('mdiWeatherCloudy') + "18°") pops at the map's top-left (≈ x 520, y 260).
- Scene 4 (1.20–1.60): answer "TU TE REPÈRES." stamps at y≈215. 1.40: the orange `.mui-you` dot appears on the map
  at image px (520, 300) with two sonar rings (scale 1→4, opacity 0.7→0).
- Scene 5 (2.00–2.40): WHIP-PAN out.
- Scene 6 (2.40–2.80): left half becomes the word zone (text centred at x 520): "ÇA CLASHE !" erupts at (520, 300),
  130 px. 2.40–2.60: a HALO pill (`.mui-stage.halo.mui-display`, wrapper scale 2.4) flies in from the left and a
  MAINSTAGE pill (scale 2.4) from the right; they COLLIDE at (520, 520) at 2.60 — spark burst (12 short orange lines
  radiating, 0.25 s), shake; both pills ricochet down and out of frame.
- Scene 7 (2.80–3.20): right half: the Mon planning sheet (`.mui-sheet`, wrapper scale 0.84, left edge x≈1010,
  top y≈200) rises from y +900: grab bar, head "MON PLANNING" + count "0/12", dayline "VENDREDI", 3 rows — Klaan /
  HALO / "18:00 → 19:00" (thumb-0) · Sound of Legend / MAINSTAGE / "19:30 → 20:30" (thumb-2) · Mattn / MAINSTAGE /
  "21:00 → 22:00" (thumb-4) — then the orange VALIDER button (`.mui-btn-orange`).
- Scene 8 (3.20–3.80): the checkboxes TICK one per 8th: 3.20, 3.40, 3.60 (orange fill + white check pop), the count
  rolls 0/12 → 1/12 → 2/12 → 3/12. 3.60: answer "TU RATES RIEN." stamps in the left zone (y≈300, problem word
  stoned). 3.80: VALIDER pressed (scale 0.94 → 1.04 → 1, orange flare ring).
- Scene 9 (4.00–4.40): dot hops in from the left onto the sheet's top edge (x≈1200, y 200).
- Scene 10 (4.40–4.80): WHIP-PAN out.

## Frame 6 — Bonus 5 & 6 : J'AI FAIM · BRACELET À SEC

- status: animated
- src: compositions/frames/06-food-cash.html
- duration: 4.8s
- transition_in: cut
- scene: J'AI FAIM → the app's food category tiles pop and four food-truck cards slam in a stack: À DEUX PAS. ; BRACELET À SEC → RECHARGER MON CASHLESS falls and cools, steps 1·2·3 pop: RECHARGÉ.
- voiceover: (beat cues) P5=0.0 · tiles 0.4–1.0 · cards 0.8/1.0/1.2/1.4 · answer 1.2 · hop 1.6 · pan 2.0 · P6=2.4 · button lands 3.2 · steps 3.2/3.4/3.6 · answer 3.6 · hop 4.0 · pan 4.4
- blueprint: compose
- focal: the food-truck card stack, then the cashless glow button + steps
- roles: assets/img/cat-restaurants.png, cat-bars.png, cat-pizza.png, cat-glaces.png — real category tiles · assets/img/food-sto-dimos.jpg, food-bali-napoli.jpg, food-pasta.jpg, food-cabane-burger.jpg — real food-truck photos in .mui-food cards · lava — background
- asset_candidates: assets/img/cat-restaurants.png, assets/img/cat-bars.png, assets/img/cat-pizza.png, assets/img/cat-glaces.png, assets/img/food-sto-dimos.jpg, assets/img/food-bali-napoli.jpg, assets/img/food-pasta.jpg, assets/img/food-cabane-burger.jpg
- sfx: 0.0 geyser · 0.4–1.0 four bubbly pops · 0.8–1.4 four card slaps (whoosh+thud) · 1.2 stamp + coin · 1.6 jump · 2.0 whip · 2.4 geyser · 2.8 fall · 3.2 thud + pssht-TING · 3.2/3.4/3.6 three numbered pings rising · 3.6 stamp + cash-register coin · 4.0 jump · 4.4 whip

- Scene 1 (0.00–0.40): "J'AI FAIM" erupts at (960, 230), 140 px.
- Scene 2 (0.40–1.00): a row of the 4 real category tiles (img assets/img/cat-*.png at 166×166 + labels
  "Restaurants", "Bars", "Pizza", "Glaces" in Montserrat 31 px under each — the `.mui-cat` structure) — row wrapper
  scale 1.0, centred, y≈330–520 — pops tile by tile on 8ths (0.40, 0.60, 0.80, 1.00), scale 0→1.12→1.
- Scene 3 (0.80–1.60): food-truck cards (`.mui-food`: photo with `.mui-sign` round signpost button, name + description;
  wrapper scale 0.72, centre (960, 790)) SLAM onto a stack on 8ths, each from y +600 with alternating rotation
  (−4°, +3°, −2°, 0°): 0.80 "Sto Dimos" / "Viens manger des spécialités Grecques" (food-sto-dimos.jpg) · 1.00
  "Bali Napoli" / "Des pizzas au feu de bois" + green `.mui-local` "Local" tag (food-bali-napoli.jpg) · 1.20
  "Pasta é Basta" / "Des pâtes préparées dans la meule du Parmesan" (food-pasta.jpg) · 1.40 "La Cabane à Burger" /
  "Viens manger des burgers gourmands" + "Local" tag (food-cabane-burger.jpg). Note: the tiles row moves up to
  y≈300 and scales to 0.85 at 0.80 to make room.
- Scene 4 (1.20–1.60): answer "À DEUX PAS." stamps at y≈230 (problem word stoned); 1.40 the top card's signpost
  button pulses orange (it opens the map in the app).
- Scene 5 (1.60–2.00): dot hops onto the top card. Scene 6 (2.00–2.40): WHIP-PAN out.
- Scene 7 (2.40–2.80): "BRACELET À SEC" erupts at (960, 230), 130 px.
- Scene 8 (2.80–3.20): the app's glow button `.mui-btn-glow` "RECHARGER MON CASHLESS" (source 830×157, wrapper
  scale 1.1, centre (960, 470)) falls red-hot; 4 ember dots glow inside it (as in the app).
- Scene 9 (3.20–3.60): LAND + QUENCH. The `.mui-steps` row ("1 Choisis ton montant", "2 Paie en sécurité",
  "3 Profite du festival"; wrapper scale 1.05, centre (960, 770)) — each step card pops on 8ths 3.20, 3.40, 3.60,
  its number circle flashing orange then settling to the app's dark circle.
- Scene 10 (3.60–4.00): answer "RECHARGÉ." stamps at y≈230.
- Scene 11 (4.00–4.40): dot hops onto the button. Scene 12 (4.40–4.80): WHIP-PAN out.

## Frame 7 — Bonus 7 & 8 : T'ES OÙ ?! · 1000 QUESTIONS

- status: animated
- src: compositions/frames/07-safety-mana.html
- duration: 4.8s
- transition_in: cut
- scene: (breakdown) T'ES OÙ ?! → Safety Mode: position sharing on, compass locks on your group, SOS & CHAT: RETROUVE TA BANDE. ; (build) 1000 QUESTIONS → M.A.N.A: a question typed, sent, answered with chips: M.A.N.A RÉPOND.
- voiceover: (beat cues) P7=0.0 · card lands 0.8 · toggle 0.8 · compass lock 1.2 · answer 1.2 · SOS 1.4 · CHAT 1.6 · pan 2.0 · P8=2.4 · input 2.6 · typing 2.8–3.4 · send 3.4 · bubble 3.6 · chips 3.8–4.2 · white-out 4.6
- blueprint: compose
- focal: the Safety Mode card + SOS/CHAT buttons, then the M.A.N.A chat
- roles: assets/img/tab-mana.png — M.A.N.A icon · kit components only otherwise · lava (dimmer, heat 0.55 in the breakdown) — background
- asset_candidates: assets/img/tab-mana.png
- sfx: (kick out) 0.0 heartbeat + geyser · 0.8 thud + toggle click · 0.8–1.2 compass spin tick-tick + lock ping · 1.2 stamp + coin · 1.4 glossy SOS glint · 1.6 CHAT bloop · 2.0 whip · 2.4 geyser + snare roll starts · 2.8–3.4 keyboard clicks on 16ths · 3.4 send swoosh · 3.6 message pop + coin · 3.8–4.2 chip blips · 4.2–4.8 riser to the drop

Breakdown mood for 0–2.4: lava heat 0.55, embers boost 0.5 and slower; the build 2.4–4.8 heats back up (heat 0.6→1.6).

- Scene 1 (0.00–0.40): "T'ES OÙ ?!" erupts at (960, 230), 140 px.
- Scene 2 (0.40–0.80): Safety Mode card falls (cooler — hot overlay at 0.6): `.mui-card` (source width 831, wrapper
  scale 1.0, left x≈220, top y≈330) containing: header "SAFETY MODE" (display 44 px) + `.mui-badge` "bêta"; row
  "Partage de position" (Montserrat 700, 36 px) with `.mui-toggle` (off); then `.mui-compass` (280 px) with a white
  navigation arrow (MUI.icon('mdiNavigation'), 90 px) in its centre and the label "Boussole" (Montserrat 700 34 px,
  #69707a) above it.
- Scene 3 (0.80–1.20): LAND (soft) + QUENCH; 0.80 the toggle flips ON (knob slides right, track turns orange); the
  compass arrow spins (rotation 0→520°, power3.out) and LOCKS at 1.20 pointing up-right (40°) with a white ping ring;
  three small orange avatar dots appear on the compass rim at 40° ("ta bande").
- Scene 4 (1.20–1.60): answer "RETROUVE TA BANDE." stamps at y≈230 (110 px).
- Scene 5 (1.40–2.00): right side: the glossy red `.mui-sos` button (icon mdiAlert + "SOS", wrapper scale 0.95, centre
  (1420, 560)) pops at 1.40 with a glint sweep; the gold `.mui-chatbtn` (icon mdiMessage + "CHAT", scale 0.95, centre
  (1680, 640)) pops at 1.60; under them the app's real line "Maintenez SOS pour alerter · CHAT pour le groupe."
  (Montserrat 400, 30 px, #b4bcc6, centred x 1550, y≈840) at 1.70. Respectful: no alarm flashing.
- Scene 6 (2.00–2.40): WHIP-PAN out.
- Scene 7 (2.40–2.80): "1000 QUESTIONS" erupts at (960, 215), 120 px; a swarm of 40 small "?" in the display font
  (orange, 30–60 px, seeded positions) pops around it on 32nds and orbits.
- Scene 8 (2.60–3.40): the M.A.N.A input bar `.mui-input` (wrapper scale 1.12, centred, y≈880) slides up at 2.60;
  2.80–3.40 the question types in, one character per 0.017 s: "Les douches ouvrent à quelle heure ?" (`.ph.typed`);
  3.40 the orange send button is pressed (scale 0.85→1).
- Scene 9 (3.40–4.20): header row "M.A.N.A" (display 46 px) with the tab-mana icon (52 px) at y≈330, centred; the
  answer bubble `.mui-bubble` (wrapper scale 1.0, centred, top y≈380) pops at 3.60 (scale 0.6→1.04→1, origin
  bottom-left): "Dimanche, les douches sont ouvertes de 8h à 20h." + `.hr` + chips "Programme", "Où manger ?",
  "Navettes", "Artistes ce soir" popping one per 16th (3.80–4.10); the red `.mui-warn` line "Attention, M.A.N.A
  peut faire des erreurs." under the bubble at 3.90. The "?" swarm is sucked into the send button 3.40–3.60.
- Scene 10 (3.60–4.20): answer "M.A.N.A RÉPOND." stamps at y≈215 (stone word sinks).
- Scene 11 (4.20–4.80): riser — everything vibrates (x ±4 px on 32nds), lava heat →1.8, L.flash 0→1 from 4.55 to
  4.80 (white-out) → cut to the drop.

## Frame 8 — NIVEAU TERMINÉ (drop)

- status: animated
- src: compositions/frames/08-niveau-termine.html
- duration: 3.2s
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
- duration: 4.8s
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
