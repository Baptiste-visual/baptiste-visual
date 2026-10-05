# Frame packet: 07-safety-mana

## Project inputs

- Project: /home/user/baptiste-visual/videos/moorea-promo-60
- Design tokens: /home/user/baptiste-visual/videos/moorea-promo-60/frame.md
- RULES_DIR: /home/user/baptiste-visual/.claude/skills/hyperframes-animation/rules

## Assigned storyboard block

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
