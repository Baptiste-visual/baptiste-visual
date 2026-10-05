# Frame packet: 06-food-cash

## Project inputs

- Project: /home/user/baptiste-visual/videos/moorea-promo
- Design tokens: /home/user/baptiste-visual/videos/moorea-promo/frame.md
- RULES_DIR: /home/user/baptiste-visual/.claude/skills/hyperframes-animation/rules

## Assigned storyboard block

## Frame 6 — Bonus 5 & 6 : J'AI FAIM · BRACELET À SEC

- status: outline
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
