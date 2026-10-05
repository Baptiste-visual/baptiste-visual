# Frame packet: 05-plan-planning

## Project inputs

- Project: /home/user/baptiste-visual/videos/moorea-promo-60
- Design tokens: /home/user/baptiste-visual/videos/moorea-promo-60/frame.md
- RULES_DIR: /home/user/baptiste-visual/.claude/skills/hyperframes-animation/rules

## Assigned storyboard block

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
