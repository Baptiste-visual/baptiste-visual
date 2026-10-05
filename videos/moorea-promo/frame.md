---
version: 1
name: Moorea Festival app — Frame (video / frame layer)
description: >
  Design truth for the "GAME OVER : rejoue le Moorea" promo. The atoms are the Moorea Festival app's
  REAL components, measured pixel by pixel on the client's screenshots and rebuilt as an HTML/CSS kit.
  Fidelity is the brief ("les mêmes formes, tout pareil"): never restyle an app component, never invent
  a generic one. The world around the UI is the app's own key art: a lava sea of black basalt plates
  and orange-to-yellow veins, floating embers, the chrome sun logo.
unit: the frame — 1920×1080
principle: the app's components are sacred · the lava world is the stage · every hit lands on the 150 BPM grid

colors:
  bg: "#0f1722"            # app page background — the film's canvas and every UI screen
  card: "#142030"          # cards / rows
  card-2: "#19283d"        # nested sub-card
  navy: "#22364f"          # primary button, active pill, navy icon tile (border #3a4a61)
  orange: "#e15311"        # THE accent: section bars, active tab, prices, times, VALIDER
  orange-hot: "#ff6a1f"
  text: "#ffffff"
  text-2: "#b4bcc6"
  text-3: "#69707a"
  teal-halo: "#039283"     # HALO stage pill
  crimson-mainstage: "#9c1736"  # MAINSTAGE stage pill
  green-local: "#2d7d32"
  sos-red: "#d81f22"
  chat-gold: "#d99a12"
  ember-core: "#ffcf2d"
  ember-halo: "#b06116"
  lava-vein: "#ff8a1f → #ffd34a → #fff6d8 (white-hot core)"
  basalt: "#121316"

typography:
  display:   { fontFamily: "Turret Road", weight: 800, upper: true, class: "mui-display", note: "the app's techno unicase caps (N/M drawn as n/m); thickened by the kit with a 0.075em same-colour stroke" }
  ui:        { fontFamily: "Montserrat", weights: [300, 400, 500, 600, 700, 800] }
  film-hero: { fontFamily: "Turret Road", weight: 800, px: "150–260", class: "mui-display", note: "problem words / GAME OVER / NIVEAU TERMINÉ; treatments .fx-molten / .fx-gameover / .fx-hot-white / .fx-stone" }
  film-answer: { fontFamily: "Turret Road", weight: 800, px: "84–120", class: "mui-display", color: "text", note: "answer stamps, white with orange glow (.fx-hot-white)" }
  film-sub:  { fontFamily: "Montserrat", weight: 600, px: "44–56", color: "text" }

fonts: |
  Paste this block INSIDE your frame's <style> (lint requires in-file @font-face; files are shipped):
  @font-face{font-family:"Montserrat";font-weight:300;font-display:block;src:url("assets/fonts/Montserrat-300.woff2") format("woff2");}
  @font-face{font-family:"Montserrat";font-weight:400;font-display:block;src:url("assets/fonts/Montserrat-400.woff2") format("woff2");}
  @font-face{font-family:"Montserrat";font-weight:500;font-display:block;src:url("assets/fonts/Montserrat-500.woff2") format("woff2");}
  @font-face{font-family:"Montserrat";font-weight:600;font-display:block;src:url("assets/fonts/Montserrat-600.woff2") format("woff2");}
  @font-face{font-family:"Montserrat";font-weight:700;font-display:block;src:url("assets/fonts/Montserrat-700.woff2") format("woff2");}
  @font-face{font-family:"Montserrat";font-weight:800;font-display:block;src:url("assets/fonts/Montserrat-800.woff2") format("woff2");}
  @font-face{font-family:"Turret Road";font-weight:800;font-display:block;src:url("assets/fonts/TurretRoad-800.woff2") format("woff2");}

kit: |
  Load these INSIDE your <template> (project-root-relative paths; no CDN is reachable):
    <link rel="stylesheet" href="assets/kit/moorea-ui.css">
    <script src="assets/vendor/gsap.min.js"></script>
    <script src="assets/kit/mui.js"></script>      (MUI.icon('mdiBus') -> inline SVG; MUI.hydrate(rootEl) fills [data-mui-icon])
    <script src="assets/kit/lava.js"></script>     (MooreaLava / MooreaEmbers — only if your frame shows lava/embers)
  Put class "mui" on your frame's content wrapper so kit typography applies.
  READ assets/kit/moorea-ui.css (it is short) before building: its class names and measured sizes ARE the components.
  Kit components are authored in the app's SOURCE pixels (a 923-px-wide phone screen). At scale 1 a full-width
  card is ~830 px wide in the 1920 frame — a good hero size. Scale a component's WRAPPER (GSAP scale), never
  edit its internal sizes, radii or colours.

components:
  card:            ".mui-card (r22, pad 37, #142030); .mui-card.r-lg for r37 parent cards"
  section-title:   ".mui-section > .t[.mui-display] — 7×42 orange bar + title"
  kv-row:          ".mui-kv > .k + .sep + .v — 'Vendredi | 17h - 02h30' rows (r22, h97)"
  navette-route:   ".mui-card.r-lg > .mui-route > .head(.from → .to .price) + .line(.d .h(14h<i></i>16h<i></i>18h))"
  primary-button:  ".mui-btn — navy full-width button (h101, r18)"
  orange-button:   ".mui-btn-orange > span.mui-display — the app's VALIDER button (gradient orange, r30, orange glow)"
  glow-button:     ".mui-btn-glow — 'RECHARGER MON CASHLESS' outlined glowing button (r37)"
  steps:           ".mui-steps > .mui-step > .n.mui-display + .l — 'Comment ça marche' 1·2·3 cards"
  stage-pills:     ".mui-stage.halo.mui-display / .mui-stage.mainstage.mui-display"
  planning-sheet:  ".mui-sheet > .grab + .head(.mui-display title + .count) + .mui-dayline.mui-display + .mui-prow…; row = img.thumb + .info(.name + .meta(pill + '18:00 → 19:00')) + .mui-check (checked: add <div class=fill> + <span data-mui-icon=mdiCheckBold>)"
  tab-bar:         ".mui-tabbar > 5×.it (img tab-*.png + label; .on = orange) + .center > img sun-orange.png"
  mana-chat:       ".mui-bubble > .txt + .hr + .mui-chips > .mui-chip; .mui-input > .mic[data-mui-icon=mdiMicrophone] + .ph(.typed) + .mui-send[data-mui-icon=mdiArrowUp]; .mui-warn"
  map:             "img assets/img/map-island.png (909×758) + .mui-pin.navy/.orange/.red/.cyan at the anchor centres listed in capture/extracted/asset-descriptions.md; .mui-you = the orange 'toi' location dot; .mui-weather chip"
  line-up:         ".mui-daytabs > .d(.on) ; .mui-fchip(.on) ; .mui-seg(.on) ; .mui-artist > img + .cap(.n + .h)"
  food:            ".mui-food > .ph(img + .mui-local 'Local' + .mui-sign[data-mui-icon=mdiSignDirection]) + .tx(.n + .d); category tiles: img assets/img/cat-*.png (166×166) with a Montserrat 31px label"
  forbidden:       ".mui-ban > .hd(.mui-dot-title > .mui-display 'FESTIVAL' + .z 'Appuyer pour zoomer') + img assets/img/interdits-festival.jpg — grid of 8 cols × 3 rows of red prohibition signs (circle r≈34); sign centres in the 766×431 image: x = 102, 183, 263, 344, 424, 504, 585, 666 · y = 92, 202, 313"
  safety-mode:     ".mui-card rows: 'Partage de position' + .mui-toggle(.on); 'Mon groupe' + .mui-grpbtn.fill 'Créer un groupe' / .mui-grpbtn.line 'Rejoindre'; .mui-compass (draw a navigation arrow inside); .mui-sos (icon mdiAlert + .lbl SOS); .mui-chatbtn (icon mdiMessage + .lbl CHAT); .mui-badge 'bêta'"
  round-buttons:   ".mui-roundbtn (home screen torch / SOS / profile / €)"
  hud:             ".hud-counter, .hud-bonus — owned by the root HUD overlay; frames never draw the HUD"
  fx:              ".fx-molten (yellow core, orange rim, glow) · .fx-gameover (red-hot) · .fx-hot-white · .fx-stone · .fx-rgb (animate --gx) · .fx-hot-overlay / .fx-hot-rim (a UI card landing red-hot then cooling: animate their opacity 1→0)"

lava-world: |
  The stage is the app's lava (Plan screen): use the shared engine, never a flat colour.
    <canvas class="clip" id="<frame_id>-lava" width="960" height="540" data-start="0" data-duration="<dur>" data-track-index="0"
            style="position:absolute;inset:0;width:100%;height:100%"></canvas>
    <canvas class="clip" id="<frame_id>-embers" width="1920" height="1080" data-start="0" data-duration="<dur>" data-track-index="1"
            style="position:absolute;inset:0;width:100%;height:100%;pointer-events:none"></canvas>
  Drive it from the timeline with a proxy object (seek-safe):
    var lava = MooreaLava.create(lavaCanvas, { seed: 3 }), emb = MooreaEmbers.create(emberCanvas, { seed: 11, count: 70 });
    var L = { t: FRAME_START, heat: 1, zoom: 1, panX: 0, panY: 0, tilt: 0, horizon: 0.3, coolR: 0, coolX: .5, coolY: .5, erupt: 0, eruptX: .5, eruptY: .5, flash: 0 };
    function draw(){ lava.render(L); emb.render(L.t, { boost: 1 }); }
    tl.to(L, { t: FRAME_START + DUR, duration: DUR, ease: 'none', onUpdate: draw }, 0);   // continuous flow across frames
    ... other tl.to(L, {...}) moves (camera pan/zoom/tilt, coolR quench, erupt blasts, flash) also with onUpdate: draw
    draw();
  ALWAYS seed 3 for the lava and pass the GLOBAL time (FRAME_START + local) so the sea flows continuously across cuts.
  Lava params: heat 0..2 · zoom · panX/panY (world units, ~1 = one plate) · tilt 0 top-down … 1 grazing horizon ·
  horizon (screen y of the horizon) · coolR/coolX/coolY quench ring in screen units (inside = cooled navy basalt + bright
  steam edge) · erupt/eruptX/eruptY white-hot blast · flash 0..1 overexposure.

composition:
  hud-zone: "From 4.8 s to 30.4 s a root HUD overlay owns the TOP 150 px of the frame (counter top-right, clock pill top-centre, lives top-left). Keep frame content out of y < 150 during that window."
  bottom: "No captions in this film. Keep primary content above y ≈ 960; only F09's tab bar may sit on the bottom edge."
  scale: "UI components are heroes: show them big (scale 1.0–1.6 of the source size) and legible for ≥ 0.6 s."
  depth: "Lava world behind, UI in front. A card that 'falls into the lava' lands with a splash (lava erupt at its foot) and cools (hot overlay fades, coolR ring opens under it)."
  copy: "Only the copy written in your Scene lines. Short French, tutoiement. Never add sentences."

motion:
  grid: "150 BPM — beat 0.4 s, bar 1.6 s. Every entrance, slam and hop lands ON a beat or an 8th (0.2 s). Times in your packet are already on the grid: hit them exactly."
  vocabulary:
    slam: "type/card arrives from scale 2.2–2.6 (or from y −700) to 1 in 0.16–0.22 s, ease 'power4.in' on the way in then a 0.25 s 'back.out(2)' settle; 1-frame white flash overlay (opacity 0.9→0 in 0.12 s) + camera shake (wrapper x/y ±10→0 over 0.3 s, 'rough' feel via a short keyframed sequence)."
    erupt: "a molten word bursts up from the lava: y +120→0, scaleY 0.3→1.15→1, blur 12px→0, with a lava erupt at its foot (L.erupt 1→0 over 0.5 s)."
    quench: "a hot card cools: .fx-hot-overlay opacity 1→0 (0.4 s, 'power2.out'), .fx-hot-rim 1→0, lava coolR 0→0.45 around it; problem word turns .fx-stone and drops 30 px with 0.4 opacity."
    hop: "the orange 'toi' dot (.mui-you) jumps between platforms on a parabolic arc (x linear, y up then down with 'power2.out'/'power2.in' halves), squash 1.25×0.8 on landing."
    stamp: "answer words appear white with a quick scale 1.4→1 'back.out(3)' + tracking 0.3em→0.035em."
    tick: "checkboxes / pins / steps pop with scale 0→1.15→1 in 0.18 s, one per 8th note."
  never: "no slow fades (film is cut on the beat), no CSS transitions, no random — seed everything; no exit tweens except in the final frame."
---

# Moorea Festival — frame design truth

The app is the hero. Every UI element in this film is one of the app's own components from `assets/kit/moorea-ui.css`,
rebuilt from measured screenshots: same navy surfaces (#0f1722 / #142030), same orange (#e15311), same radii, same
Montserrat sizes, same techno display caps. The film adds only two things around them: the lava world (from the app's
Plan screen and key art) and film typography for problems/answers in the same display face.
