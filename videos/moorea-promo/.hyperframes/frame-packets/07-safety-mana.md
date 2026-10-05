# Frame packet: 07-safety-mana

## Project inputs

- Project: /home/user/baptiste-visual/videos/moorea-promo
- Design tokens: /home/user/baptiste-visual/videos/moorea-promo/frame.md
- RULES_DIR: /home/user/baptiste-visual/.claude/skills/hyperframes-animation/rules

## Assigned storyboard block

## Frame 7 — Bonus 7 & 8 : T'ES OÙ ?! · 1000 QUESTIONS

- status: outline
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
