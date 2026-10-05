# Frame packet: 05-plan-planning

## Project inputs

- Project: /home/user/baptiste-visual/videos/moorea-promo
- Design tokens: /home/user/baptiste-visual/videos/moorea-promo/frame.md
- RULES_DIR: /home/user/baptiste-visual/.claude/skills/hyperframes-animation/rules

## Assigned storyboard block

## Frame 5 — Bonus 3 & 4 : PERDU · ÇA CLASHE

- status: outline
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
