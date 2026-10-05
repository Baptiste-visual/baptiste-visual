# Frame packet: 08-niveau-termine

## Project inputs

- Project: /home/user/baptiste-visual/videos/moorea-promo-60
- Design tokens: /home/user/baptiste-visual/videos/moorea-promo-60/frame.md
- RULES_DIR: /home/user/baptiste-visual/.claude/skills/hyperframes-animation/rules

## Assigned storyboard block

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
