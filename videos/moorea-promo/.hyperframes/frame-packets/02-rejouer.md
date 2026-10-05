# Frame packet: 02-rejouer

## Project inputs

- Project: /home/user/baptiste-visual/videos/moorea-promo
- Design tokens: /home/user/baptiste-visual/videos/moorea-promo/frame.md
- RULES_DIR: /home/user/baptiste-visual/.claude/skills/hyperframes-animation/rules

## Assigned storyboard block

## Frame 2 — REJOUER ?

- status: outline
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
