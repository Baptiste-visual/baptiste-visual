# Frame packet: 09-end

## Project inputs

- Project: /home/user/baptiste-visual/videos/moorea-promo
- Design tokens: /home/user/baptiste-visual/videos/moorea-promo/frame.md
- RULES_DIR: /home/user/baptiste-visual/.claude/skills/hyperframes-animation/rules

## Assigned storyboard block

## Frame 9 — L'appli officielle (end card)

- status: outline
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
