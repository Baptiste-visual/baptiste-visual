export const meta = {
  name: 'moorea-soundtrack-v2',
  description: 'Recompose the 60 s Moorea promo soundtrack in 3 adult directions, critique, revise and judge',
  phases: [
    { title: 'Cues', detail: 'exact film-time cue sheet from the animation code' },
    { title: 'Compose', detail: 'three directions, each a full synthesized score + SFX' },
    { title: 'Critique', detail: 'music supervisor + mix engineer review per variant' },
    { title: 'Revise', detail: 'composer applies the critique, re-renders, re-measures' },
    { title: 'Judge', detail: 'rank the finished variants for the client' },
    { title: 'Polish', detail: 'apply the judge polish to the winner, export the MP3' },
    { title: 'Verify', detail: 'adversarial final check of the MP3' },
  ],
}

const ROOT = '/home/user/baptiste-visual/videos/moorea-promo-60'
const V2 = ROOT + '/tools/audio/v2'

const CUE_SCHEMA = {
  type: 'object',
  properties: {
    cues: { type: 'array', items: { type: 'object', properties: {
      t: { type: 'number' }, frame: { type: 'string' }, event: { type: 'string' },
      kind: { type: 'string', enum: ['slam', 'transition', 'ui', 'reveal', 'texture', 'music'] },
      weight: { type: 'integer', minimum: 1, maximum: 3 }, old_sound: { type: 'string' } },
      required: ['t', 'frame', 'event', 'kind', 'weight', 'old_sound'] } },
    mismatches: { type: 'array', items: { type: 'object', properties: {
      event: { type: 'string' }, visual_t: { type: 'number' }, old_audio_t: { type: 'number' }, note: { type: 'string' } },
      required: ['event', 'visual_t', 'old_audio_t', 'note'] } },
    file: { type: 'string' },
  },
  required: ['cues', 'mismatches', 'file'],
}

const COMPOSE_SCHEMA = {
  type: 'object',
  properties: {
    key: { type: 'string' }, script: { type: 'string' }, wav: { type: 'string' },
    lufs_integrated: { type: 'number' }, true_peak_dbtp: { type: 'number' }, length_ok: { type: 'boolean' },
    high_tonal_beeps: { type: 'integer' }, cue_sync_weak: { type: 'integer' }, render_seconds: { type: 'number' },
    concept: { type: 'string' }, palette: { type: 'string' }, changes: { type: 'string' }, known_weaknesses: { type: 'string' },
  },
  required: ['key', 'script', 'wav', 'lufs_integrated', 'true_peak_dbtp', 'length_ok', 'high_tonal_beeps', 'cue_sync_weak', 'render_seconds', 'concept', 'palette', 'known_weaknesses'],
}

const CRIT_SCHEMA = {
  type: 'object',
  properties: {
    overall: { type: 'string' },
    maturity_score: { type: 'integer', minimum: 1, maximum: 10 },
    brand_fit_score: { type: 'integer', minimum: 1, maximum: 10 },
    technical_score: { type: 'integer', minimum: 1, maximum: 10 },
    sync_score: { type: 'integer', minimum: 1, maximum: 10 },
    blocking: { type: 'array', items: { type: 'object', properties: { issue: { type: 'string' }, where: { type: 'string' }, fix: { type: 'string' } }, required: ['issue', 'where', 'fix'] } },
    improvements: { type: 'array', items: { type: 'object', properties: { issue: { type: 'string' }, where: { type: 'string' }, fix: { type: 'string' } }, required: ['issue', 'where', 'fix'] } },
  },
  required: ['overall', 'maturity_score', 'brand_fit_score', 'technical_score', 'sync_score', 'blocking', 'improvements'],
}

const JUDGE_SCHEMA = {
  type: 'object',
  properties: {
    ranking: { type: 'array', items: { type: 'object', properties: {
      key: { type: 'string' }, maturity: { type: 'integer' }, brand_fit: { type: 'integer' }, technical: { type: 'integer' },
      sync: { type: 'integer' }, overall: { type: 'integer' }, rationale: { type: 'string' } },
      required: ['key', 'maturity', 'brand_fit', 'technical', 'sync', 'overall', 'rationale'] } },
    winner: { type: 'string' },
    polish: { type: 'array', items: { type: 'string' } },
  },
  required: ['ranking', 'winner', 'polish'],
}

const CONTEXT = `
PROJECT: ${ROOT} — a 60 s, 1920x1080 promo video (already rendered; it will NOT be re-rendered) for the official app of the
Moorea Festival (electronic music festival, 5-6-7 June 2026, Chateau de Grillemont, Touraine; line-up includes Klaan,
Sound of Legend, Mattn). Concept "GAME OVER : rejoue le Moorea": a lava-world platformer. The festival's 8 "galeres"
(problems) erupt from the lava as molten words, the matching real app screen falls red-hot, lands, cools into the real navy
UI card; a HUD counts "GALERES EVITEES n/8". It ends on an "L'APPLI OFFICIELLE" end card with App Store / Google Play buttons.
The client will only receive an audio file (MP3) and lay it under the existing video, so picture sync is essential.

CLIENT FEEDBACK on the current soundtrack (tools/audio/compose60.py -> assets/audio/mix.wav, synthesized in numpy):
"elle fait trop enfantine" (it sounds too childish). Measured/read causes: square-wave 8-bit blips everywhere (~330 isolated
high tonal beeps > 1.8 kHz), coin "bling" pickups, cartoon boing / slide whistle / bubbly plops, glitter sparkles and bell
"ting"s, a toy-like 8-bit game-over arpeggio, a thin acid-stab lead, thin high supersaws, an almost-mono mix (L/R correlation
0.97-0.99), weak sub in the drop (sub<60 Hz at -15 dB vs total), and every micro-cue gets its own beep (SFX clutter sitting
on top of the music). The new soundtrack must sound like a premium adult production: what a top agency would put on a
festival / app-launch trailer.

HARD RULES (anti-childish):
1. BANNED: square/pulse-wave blips, chiptune arpeggios, coin/pickup chimes, boing, slide whistle, bubbly plops, cartoon
   pitch-up "bloops", glitter/sparkle tinkles, bell/ding "ting"s, music-box / xylophone / glockenspiel timbres, major-key
   jingles or fanfares, "win" jingles, any melodic beep above ~1.5 kHz used as a UI sound. high_tonal_beeps in the analysis
   should be close to zero (a few from metallic hits are fine).
2. The game feel comes from cinematic / technical sound design, never from retro-game cliches. e.g. GAME OVER = sub drop +
   distorted braam + tape-stop / power-down, not a sad 8-bit melody.
3. UI sounds (taps, ticks, toggles, checkboxes, row reveals, typing) = premium, tactile, QUIET: short filtered-noise
   transients with a tiny low-mid body (150-600 Hz thump), soft "tok" / haptic clicks; very short, low in level, never
   melodic. Many micro-cues can share one soft click or be carried by the music's own drum hits. Prioritise weight-3 and
   weight-2 cues; weight-1 cues are optional (skip them when the music already marks the beat).
4. Big moments (GAME / OVER slams, PRESS, every answer stamp, the drop, the final hit) = heavy, layered, cinematic: sub
   thump + distorted transient + metallic/noise body + reverb tail; the music ducks under them (side-chain).
5. Music: dark minor / phrygian harmony (F minor by default; another minor key is allowed if consistent), leads in the low-mid
   register, real low end (sub + saturated kick), side-chain pumping, WIDE stereo (pads / FX / reverbs wide; kick, bass,
   sub mono), evolving filters, tension and release that follow the picture's sections.

PICTURE STRUCTURE (film time; 120 BPM grid: beat 0.5 s, bar 2 s; sections start on bars):
- 0-4 HOOK "GAME OVER": lava bubbling 0.0, deep plop 0.5, GAME slam 1.0, OVER slam 1.5, "denied" subline + artist card 2.0,
  tape-rewind 3.0-3.75, CRT power-off 3.75.
- 4-6 "REJOUER ?": CRT power-on 4.0, UI tick 4.5, BIG button PRESS 5.0 (power-up moment), reverse-swell dive 5.5 -> 6.0.
- 6-10 "NIVEAU 1": level-start impact 6.0, lava splash 7.0, eight problem words erupt one per 8th 7.0-8.75 (rising),
  overheat riser 9.0-10.0, hit at 10.0.
- 10-40 six POWER-UPS of 5 s (P = 10,15,20,25,30,35): problem erupts P, card falls P+0.5, lands + quench P+1.0, answer word
  stamps P+1.5 (HUD +1 pill flies; counter increments ~P+2.1), showcase beats P+2.0..P+3.5 (UI details, one per beat),
  hop P+3.5-4.0, land P+4.0, whip-pan transition P+4.5. Full groove.
- 40-45 BREAKDOWN (no kick, the only breath): power-up 7 "T'ES OU ?!" (Safety mode, heartbeat feel); land 41.0, answer 41.5,
  showcase 42-43.5, whip 44.5.
- 45-50 BUILD: power-up 8 "1000 QUESTIONS" (M.A.N.A chat assistant): erupt 45.0, typing 45.75-46.5, send + answer 46.5,
  bubble 47.0, chips 47.5-48.25, tap 48.5, riser 49.0-50.0 into the drop.
- 50-54 DROP "NIVEAU TERMINE 8/8": the biggest moment at 50.0, score spin 50.5, pull-back whoosh 51.5, eight hops
  51.5-52.75, two tagline slams (exact times in the cue sheet).
- 54-60 END CARD "L'APPLI OFFICIELLE": sunrise swell 54.0, tab bar 55.25, logo snap 56.0, date 56.5, store buttons
  57.0 / 57.25, "pret a jouer" 57.75, button 58.0, FINAL HIT 59.0 (kick + crash + press), ring-out to 60.0.
The exact cue sheet extracted from the animation code (below) overrides this summary.

TECHNICAL SPEC:
- Python 3.11 with numpy, scipy, soundfile, pedalboard 0.9.25 (Reverb, Convolution, Compressor, Limiter, Distortion,
  Clipping, LadderFilter, Chorus, Phaser, Delay, PitchShift, filters...), pyloudnorm, dawdreamer 0.9 (Faust DSP: high-quality
  VA oscillators / moog filters / zita reverb, optional), ffmpeg. No downloaded samples: everything synthesized and
  deterministic (fixed seeds). You may reuse helpers from tools/audio/compose60.py (place(), polyBLEP saw, filters, the
  true-peak normaliser) but none of its childish instruments. Lush reverb tip: pedalboard Convolution with a synthetic IR
  (decaying, filtered stereo noise) sounds far better than plain Reverb.
- Output: 48 kHz, 16-bit PCM WAV, stereo, EXACTLY 2,880,000 samples (60.000 s), sound starts at t=0 with no latency offset
  (compensate filter/plugin latency), integrated loudness -14 LUFS +/-0.7, true peak <= -1.0 dBTP, no clicks, DC ~ 0. The
  final hit at 59.0 rings out naturally; fade only the last ~0.3 s.
- Render time under ~6 minutes (vectorise; per-sample Python loops only on short sounds).
- Measure with: python3 tools/audio/v2/analyze.py <wav> --cues <dir>/cues.json --out <dir>/analysis
  It prints LUFS / true peak, loudness per bar, band balance + stereo correlation per section, cue sync (onset within
  +/-40 ms of each cue; lists weak/late weight>=2 cues), click candidates (heuristic: check them) and high tonal beeps (the
  "toy" marker), and writes analysis.json, spectrogram.png, waveform.png (look at the PNGs with the Read tool).
  Baseline of the OLD childish mix for comparison: -14.7 LUFS, stereo corr 0.93-0.99, 332 high tonal beeps.
- Work only inside your own variant folder. Do NOT modify tools/audio/compose60.py, assets/audio/mix.wav, compositions/,
  index.html or another variant's folder. Do not git commit. Run commands from ${ROOT}.`

const DIRECTIONS = [
  { key: 'a-melodic', spec: `DIRECTION A "melodic techno": dark cinematic melodic techno in the Afterlife / Tale Of Us / Anyma school,
120 BPM. Deep round kick with a short tail, rolling 16th off-beat bassline (sub + mid layer), shuffled closed hats + open hats,
rim / clap on 2 and 4 in a big plate; a hypnotic minor arpeggio (mid register, filter + delay automation) that grows across the
power-ups; huge dark pads / choir-like supersaw layers for the breakdown and the end card; risers and noise sweeps. SFX are
cinematic and tactile, mixed INTO the music.` },
  { key: 'b-techno', spec: `DIRECTION B "festival techno": peak-time / big-room festival techno with an industrial edge (Charlotte de Witte,
Amelie Lens, Mattn's big-room techno), on the 120 BPM grid (half-time / double-time accents allowed). Rumble kick (kick + a
reverb-fed, low-passed, side-chained rumble), driving 16th bass, metallic industrial percussion, a gritty serious acid line
(303-style resonant LadderFilter, not cute), a dark stab / hoover-like lead for the drop; tasteful heavy distortion. SFX:
industrial, metallic, aggressive but controlled.` },
  { key: 'c-trailer', spec: `DIRECTION C "trailer hybrid": AAA game / blockbuster trailer hybrid. Hook and level intro are cinematic
(braams, sub drops, taiko-like low toms, a tense strings-like synth ostinato, ticking-clock pulse, risers); the power-ups ride
a hybrid trailer groove (big toms + modern electronic pulse + staccato low synth ostinato in minor); breakdown = heartbeat +
choir-like pad + sparse low piano-like notes; the drop at 50 becomes a heavy four-on-the-floor techno / electro drop with
braams; end card = an epic modal resolution (e.g. Fm - Db - Eb - Fm with suspensions, never a happy major jingle) and a massive
final hit. SFX: trailer-grade whooshes, impacts, metallic hits, reverses.` },
]

// ---------------------------------------------------------------- Cues
phase('Cues')
const CUE_TASK = (part, frames, file) => `You extract an exact sound-sync cue sheet for a HyperFrames video. Project: ${ROOT}.
Read index.html (frame clip data-start / data-duration), STORYBOARD.md (the "sfx:" and "voiceover: beat cues" lines),
the frame compositions ${frames} in compositions/frames/, ${part === 2 ? 'compositions/hud.html (HUD clip starts at film 6.0; its local times + 6.0), ' : ''}and tools/audio/compose60.py (the OLD audio, for reference).
Timing rules: frames 01, 02, 03, 08, 09 end with a wrapper script (an outer GSAP timeline tweening the inner timeline's time with
S = 1.25), so film time = frame data-start + inner GSAP position x 1.25. Frames 04-07 are native: film time = data-start + local
GSAP position. Read the actual GSAP code (tl positions, helper calls like slamIn/hit/LK/LT, loops with offsets) to get the exact
time of every visual event a sound designer would hit: slams, impacts, lands, stamps, eruptions, whips/transitions, reveals,
UI taps/ticks/toggles, typing, pops, risers/white-outs, the drop, the final hit.
For each cue give: t (film seconds, 3 decimals), frame id, event (short, concrete: what is seen), kind, weight (3 = must hit
hard: slams/press/answer stamps/drop/final hit; 2 = clear visible accent that should be audible; 1 = micro detail, optional),
old_sound (what compose60.py plays there, or "none"). List mismatches where compose60.py's sound time differs from the real
visual time by more than 20 ms (e.g. check the frame 08 tagline slams). Be exhaustive and precise; do not invent events.
Write the cue list as a JSON array (same fields as the cues) to ${file}, and return it.`
const parts = await parallel([
  () => agent(CUE_TASK(1, '01-game-over, 02-rejouer, 03-niveau, 04-navette-sac', V2 + '/cues_part1.json'), { label: 'cues:01-04', phase: 'Cues', schema: CUE_SCHEMA }),
  () => agent(CUE_TASK(2, '05-plan-planning, 06-food-cash, 07-safety-mana, 08-niveau-termine, 09-end', V2 + '/cues_part2.json'), { label: 'cues:05-09+hud', phase: 'Cues', schema: CUE_SCHEMA }),
])
const okParts = parts.filter(Boolean)
const cues = okParts.flatMap(p => p.cues).sort((a, b) => a.t - b.t)
const mismatches = okParts.flatMap(p => p.mismatches)
log(`cue sheet: ${cues.length} cues (${cues.filter(c => c.weight === 3).length} weight-3), ${mismatches.length} old-audio mismatches`)
const CUE_TEXT = cues.map(c => `${c.t.toFixed(3)}  w${c.weight}  ${c.kind.padEnd(10)} ${c.frame}: ${c.event}   [old: ${c.old_sound}]`).join('\n')
const MIS_TEXT = mismatches.map(m => `- ${m.event}: visual ${m.visual_t} vs old audio ${m.old_audio_t} (${m.note})`).join('\n') || '- none'
const CUE_FILE_CMD = (dir) => `python3 -c "import json;a=json.load(open('${V2}/cues_part1.json'));b=json.load(open('${V2}/cues_part2.json'));a=a.get('cues',a) if isinstance(a,dict) else a;b=b.get('cues',b) if isinstance(b,dict) else b;json.dump(sorted(a+b,key=lambda c:c['t']),open('${dir}/cues.json','w'),indent=1)"`

// ---------------------------------------------------------------- Compose -> Critique -> Revise
const composePrompt = (d) => {
  const dir = `${V2}/${d.key}`
  return `You are an award-level electronic music producer and trailer sound designer. Write, from scratch, a complete new
60 s soundtrack (music + sound design, one mixed stereo file) for the video below, in the direction assigned to you.
${CONTEXT}

${d.spec}

YOUR FOLDER: ${dir} (create it). Steps:
1. mkdir -p ${dir} && ${CUE_FILE_CMD(dir)}   (creates ${dir}/cues.json, the cue sheet the analyser checks)
2. Write ${dir}/compose.py. Start it with a docstring plan: concept, palette (each instrument and SFX family, how it is
   synthesized), arrangement per section, and the mapping cue -> sound for every weight-3 and weight-2 cue. It must write
   ${dir}/mix.wav when run as: cd ${ROOT} && python3 ${dir}/compose.py
3. Render, analyse (python3 tools/audio/v2/analyze.py ${dir}/mix.wav --cues ${dir}/cues.json --out ${dir}/analysis), look at
   spectrogram.png and waveform.png, and iterate until the spec is met: exact length, -14 LUFS +/-0.7, TP <= -1.0 dBTP, zero
   weak/late weight-3 cues, high tonal beeps ~0, stereo correlation clearly below the old 0.97 on music sections (pads/FX
   wide) while the low end stays mono, solid sub in the drop, no clicks. Then do a self-critique pass as a strict music
   supervisor who hates anything childish, and fix what you find.
Craft notes: layer every important sound (transient + body + tail), use saturation and parallel compression, side-chain the
music to the kick and to big hits, automate filters across sections, use reverb/delay sends for depth, keep the SFX inside
the mix (they support the music, not a separate layer of beeps), make the arrangement evolve every 4-8 bars so 60 s never
feels like a loop, and make the drop (50.0) and the final hit (59.0) the two loudest, widest moments.

CUE SHEET (film seconds, weight, kind, frame: event [old sound]):
${CUE_TEXT}

Known timing mismatches of the OLD audio (follow the visual time):
${MIS_TEXT}

Return the structured result (key = "${d.key}", script/wav = absolute paths, metrics from the final analysis, render_seconds,
a concept + palette summary, known_weaknesses honestly).`
}

const critiquePrompt = (d, r) => `You are a strict senior music supervisor and mixing/mastering engineer reviewing a candidate soundtrack for
a client who rejected the previous one as "trop enfantine" (too childish). You cannot listen, so you judge from the code (every
synthesis and arrangement decision is in it) and from measurements.
${CONTEXT}

${d.spec}

Candidate: ${r ? r.script : V2 + '/' + d.key + '/compose.py'} -> ${r ? r.wav : V2 + '/' + d.key + '/mix.wav'} (folder ${V2}/${d.key}).
Composer's own summary: ${r ? JSON.stringify({ concept: r.concept, palette: r.palette, known_weaknesses: r.known_weaknesses }) : 'n/a'}
Do NOT edit any file except writing your notes to ${V2}/${d.key}/critique.md.
1. Run python3 tools/audio/v2/analyze.py ${V2}/${d.key}/mix.wav --cues ${V2}/${d.key}/cues.json --out ${V2}/${d.key}/analysis_review
   and look at spectrogram.png / waveform.png there. Do your own extra measurements if useful (e.g. pitch content of leads:
   are all notes in key? register of the leads; level of UI sounds vs music; side-chain depth; crest factor per section;
   low-end mono check; how long reverb tails run; abrupt cut-offs at section boundaries).
2. Read compose.py fully. Hunt for anything childish or cheap: banned timbres (square blips, coins, bells, sparkles, boings,
   whistles, plops, cute arps, major jingles), leads too high or too bright, toy-like envelopes, SFX clutter (too many
   micro-sounds), cartoon pitch sweeps, thin synths, weak drums, static loops, mono mix, harshness, mud, weak drop.
3. Check sync against the cue sheet (weight-3 cues must have a strong onset within +/-20 ms).
4. Check brand fit: credible for an electronic music festival's official app trailer, adult, premium.
Return scores and concrete fixes (where = line numbers / timestamps; fix = specific synthesis or mix change). Blocking = must
fix before the client hears it.`

const revisePrompt = (d, r, c) => `You are the producer of soundtrack variant "${d.key}". A strict music supervisor reviewed your
render; apply the critique and deliver the final version.
${CONTEXT}

${d.spec}

Your files: ${V2}/${d.key}/compose.py -> ${V2}/${d.key}/mix.wav (cue sheet ${V2}/${d.key}/cues.json). Previous metrics:
${r ? JSON.stringify({ lufs: r.lufs_integrated, tp: r.true_peak_dbtp, beeps: r.high_tonal_beeps, weak: r.cue_sync_weak, weaknesses: r.known_weaknesses }) : 'n/a'}
CRITIQUE (scores maturity ${c ? c.maturity_score : '?'}/10, brand ${c ? c.brand_fit_score : '?'}/10, technical ${c ? c.technical_score : '?'}/10, sync ${c ? c.sync_score : '?'}/10):
${c ? c.overall : '(critique missing: do your own strict review instead)'}
BLOCKING:
${c ? c.blocking.map(b => `- ${b.issue} @ ${b.where} -> ${b.fix}`).join('\n') : ''}
IMPROVEMENTS:
${c ? c.improvements.map(b => `- ${b.issue} @ ${b.where} -> ${b.fix}`).join('\n') : ''}

Fix every blocking item and every improvement you agree with (say why if you skip one). Keep what works. Re-render, re-run
python3 tools/audio/v2/analyze.py ${V2}/${d.key}/mix.wav --cues ${V2}/${d.key}/cues.json --out ${V2}/${d.key}/analysis, look at
the PNGs, and make sure the spec still holds (exact length, -14 LUFS +/-0.7, TP <= -1.0 dBTP, no weak weight-3 cues, high
tonal beeps ~0, no clicks). Update the docstring plan. Return the structured result with "changes" listing what you changed.`

phase('Compose')
const finals = await pipeline(
  DIRECTIONS,
  d => agent(composePrompt(d), { label: `compose:${d.key}`, phase: 'Compose', schema: COMPOSE_SCHEMA, effort: 'high' }),
  (r, d) => agent(critiquePrompt(d, r), { label: `critique:${d.key}`, phase: 'Critique', schema: CRIT_SCHEMA, effort: 'high' })
    .then(c => ({ r, c })),
  ({ r, c }, d) => agent(revisePrompt(d, r, c), { label: `revise:${d.key}`, phase: 'Revise', schema: COMPOSE_SCHEMA, effort: 'high' })
    .then(f => ({ key: d.key, first: r, critique: c, final: f })),
)
const done = finals.filter(Boolean).filter(x => x.final)
log(`finished variants: ${done.map(x => x.key).join(', ') || 'none'}`)

// ---------------------------------------------------------------- Judge
phase('Judge')
let verdict = null
if (done.length) {
  verdict = await agent(`You are the creative director choosing the soundtrack the client will receive (as an MP3 laid under the existing
60 s video). The client rejected the previous soundtrack as "trop enfantine". Compare the finished variants and rank them.
${CONTEXT}

Variants (folder ${V2}/<key>/: compose.py, mix.wav, cues.json, analysis/):
${done.map(x => `- ${x.key}: ${DIRECTIONS.find(d => d.key === x.key).spec.split('\n')[0]}
  final metrics ${JSON.stringify({ lufs: x.final.lufs_integrated, tp: x.final.true_peak_dbtp, beeps: x.final.high_tonal_beeps, weak: x.final.cue_sync_weak, len: x.final.length_ok })}
  concept: ${x.final.concept}
  critique scores before revision: ${x.critique ? `maturity ${x.critique.maturity_score}, brand ${x.critique.brand_fit_score}, tech ${x.critique.technical_score}, sync ${x.critique.sync_score}` : 'n/a'}
  revision changes: ${x.final.changes || ''}
  remaining weaknesses: ${x.final.known_weaknesses}`).join('\n')}

For each variant: read compose.py, run python3 tools/audio/v2/analyze.py <folder>/mix.wav --cues <folder>/cues.json --out <folder>/analysis_judge
and look at its spectrogram/waveform. Score 1-10: maturity (nothing childish, adult premium feel), brand_fit (official app trailer
of an electronic music festival; lava GAME OVER concept), technical (mix, low end, stereo, loudness, no clicks/harshness),
sync (weight-3 cues hit), overall. Pick the winner. Then list "polish": small, safe, concrete last tweaks for the winner
(each one line, with line numbers / timestamps) that would raise it further without risking the spec. Do not edit files.`,
    { label: 'judge', phase: 'Judge', schema: JUDGE_SCHEMA, effort: 'high' })
}

// ---------------------------------------------------------------- Polish + Verify (winner only)
const FIN = V2 + '/final'
const MP3 = FIN + '/Moorea-Festival-bande-son-60s.mp3'
const FINAL_SCHEMA = {
  type: 'object',
  properties: {
    wav: { type: 'string' }, mp3: { type: 'string' }, source_key: { type: 'string' },
    wav_lufs: { type: 'number' }, wav_tp: { type: 'number' }, mp3_lufs: { type: 'number' }, mp3_tp: { type: 'number' },
    mp3_decoded_samples: { type: 'integer' }, mp3_lag_samples: { type: 'integer' }, weak_weight3: { type: 'integer' },
    high_tonal_beeps: { type: 'integer' }, applied: { type: 'string' }, skipped: { type: 'string' },
  },
  required: ['wav', 'mp3', 'source_key', 'wav_lufs', 'wav_tp', 'mp3_lufs', 'mp3_tp', 'mp3_decoded_samples', 'mp3_lag_samples', 'weak_weight3', 'high_tonal_beeps', 'applied', 'skipped'],
}
const VERIFY_SCHEMA = {
  type: 'object',
  properties: {
    pass: { type: 'boolean' },
    blocking: { type: 'array', items: { type: 'object', properties: { issue: { type: 'string' }, evidence: { type: 'string' }, fix: { type: 'string' } }, required: ['issue', 'evidence', 'fix'] } },
    notes: { type: 'string' },
  },
  required: ['pass', 'blocking', 'notes'],
}
const MP3_STEPS = `Export: ffmpeg -y -i ${FIN}/mix.wav -c:a libmp3lame -b:a 320k -ar 48000 ${MP3}
Check the MP3: decode it with ffmpeg to WAV, confirm 2,880,000 samples (+/- the encoder padding handled by the LAME gapless
header; report what ffmpeg decodes), lag 0 vs the WAV by cross-correlation on the first 5 s, integrated LUFS about -14 and
true peak <= -1.0 dBTP measured on the DECODED MP3 (lower the WAV master by 0.3-0.5 dB and re-export if the MP3 overshoots).`
let fin = null, check = null
const win = verdict && done.find(x => x.key === verdict.winner)
if (win) {
  phase('Polish')
  fin = await agent(`You finalise the winning soundtrack "${win.key}" for the Moorea Festival 60 s promo. The client gets ONLY an MP3 to lay
under the existing video (no video re-render).
${CONTEXT}

1. rm -rf ${FIN} && cp -r ${V2}/${win.key} ${FIN} (then delete the copied analysis_* folders and old mix.mp3 inside ${FIN}).
   Edit ${FIN}/compose.py so it writes ${FIN}/mix.wav (fix any path pointing to the ${win.key} folder). Never edit
   ${V2}/${win.key} itself.
2. Apply the creative director's polish list below, one item at a time: render, run
   python3 tools/audio/v2/analyze.py ${FIN}/mix.wav --cues ${FIN}/cues.json --out ${FIN}/analysis, and keep an item only if
   it does what it says without breaking the spec (exact 2,880,000 samples, -14 LUFS +/-0.7, TP <= -1.0 dBTP on the WAV,
   no weak weight-3 cue, high tonal beeps ~0, no clicks). Revert items that hurt; say why.
POLISH LIST:
${verdict.polish.map(p => '- ' + p).join('\n')}
3. ${MP3_STEPS}
Return the structured result (applied / skipped = what you did and why).`,
    { label: 'polish:' + win.key, phase: 'Polish', schema: FINAL_SCHEMA, effort: 'high' })

  if (fin) {
    phase('Verify')
    check = await agent(`Adversarial final check before an MP3 goes to a client who rejected the previous soundtrack as "trop enfantine".
Try hard to find a reason NOT to ship it. Default to pass=false if a hard requirement is unproven.
${CONTEXT}

Files: ${FIN}/compose.py, ${FIN}/mix.wav, ${MP3}, cue sheet ${FIN}/cues.json. Do not edit anything.
Prove each of these with your own commands: (a) the decoded MP3 is 60.0 s, 48 kHz stereo, aligned with the WAV (lag 0 within
1 ms) so it syncs with the video from t=0; (b) LUFS about -14 and TP <= -1.0 dBTP on the decoded MP3; (c) every weight-3 cue
has a strong onset within +/-20 ms (decode the MP3 to a WAV in ${FIN}/verify/ and run python3 tools/audio/v2/analyze.py on it
with --cues ${FIN}/cues.json --out ${FIN}/verify); (d) nothing childish survives: read compose.py for banned timbres
(square/pulse blips, coins, bells, sparkles, boings, whistles, plops, major jingles, chiptune arps) and check the high tonal
beep list; (e) no clicks, no digital clipping, no silence gaps or abrupt cut-offs at section boundaries (look at the
waveform/spectrogram PNGs); (f) the drop at 50.0 and the final hit at 59.0 are the strongest moments.
Blocking = would embarrass us in front of the client. Return pass + blocking issues (evidence + fix) + notes.`,
      { label: 'verify:mp3', phase: 'Verify', schema: VERIFY_SCHEMA, effort: 'high' })

    if (check && !check.pass && check.blocking.length) {
      fin = await agent(`Fix the blocking issues found by the final check of ${FIN} (soundtrack "${win.key}" for the Moorea 60 s promo).
${CONTEXT}

Work only in ${FIN}. BLOCKING:
${check.blocking.map(b => `- ${b.issue} | evidence: ${b.evidence} | fix: ${b.fix}`).join('\n')}
Fix them in ${FIN}/compose.py, re-render, re-analyse (python3 tools/audio/v2/analyze.py ${FIN}/mix.wav --cues ${FIN}/cues.json --out ${FIN}/analysis), keep the spec.
${MP3_STEPS}
Return the structured result.`,
        { label: 'fix:final', phase: 'Verify', schema: FINAL_SCHEMA, effort: 'high' }) || fin
    }
  }
}

return {
  cues: cues.length, mismatches,
  variants: done.map(x => ({ key: x.key, final: x.final, critique: x.critique ? { m: x.critique.maturity_score, b: x.critique.brand_fit_score, t: x.critique.technical_score, s: x.critique.sync_score, blocking: x.critique.blocking.length } : null })),
  verdict, fin, check,
}
