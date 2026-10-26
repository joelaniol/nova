# `nova.video_render`

> **Turns a screen recording into a clip: an animated GIF, a WebM or MP4 video, or a still.**

* **Core Feature Guide:** [Visual Evidence & Auditing](../../../research/evidence-verification-mode-evm/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

Nova's video editor. A video recorded with [`nova.screen_record_start`](../visual-evidence/nova-screen-record-start.md) is the evidence; a short clip is what people actually watch in a README, an issue, a chat or a feed. `nova.video_render` makes one from your most recent recording, or from the recording `filePath` names. The recording itself stays unchanged.

**Cut and tighten, never stage.** `segments` picks parts of the recording and plays them one after the other, each at its own `speed`: a waiting phase at `speed: 4` takes a quarter of the time, a detail at `speed: 0.5` runs at half speed. `idle='auto'` does that by itself from the recording's evidence timeline. Every frame in the clip is a frame that was recorded; captions and the end card are the only pictures added.

**The format for the place it goes.** `gif` plays everywhere, also inline on GitHub; it uses one palette of 255 colours and stores only what changed from frame to frame, so interface text stays sharp (8 to 12 frames per second at 800 to 1000 pixels wide is the usual range). `webm` is full-colour VP8 video at a fraction of the size, for chats and websites. `mp4` is H.264 video for LinkedIn, Reddit and YouTube. `png` is one still frame for a thumbnail. `mp4` with `lossless=true` cuts the recording itself without re-encoding, for unchanged evidence in a bug report.

**Feeds and phones.** `aspect='4:5'` or `'9:16'` reframes the clip and pans to where things change; `croppedShare` in the result says how much of each recorded frame was left out. `captions` tell the story in two to five words per step, `endCard` closes the clip, `keys=true` shows the shortcuts that were pressed (never typed text), `zoom` enlarges details.

**A finished look.** `template='nova-linkedin'` applies a complete set of values (4:5, 1080x1350, H.264, the styled look: the recording as a framed window on a dark canvas, captions beside it, an animated end card). `style` sets the look's values one by one; templates are listed and saved with [`nova.video_template_list`](nova-video-template-list.md) and [`nova.video_template_save`](nova-video-template-save.md).

The clip goes to Nova's Exports folder (`ScreenRecordings`) next to the recordings unless `saveDir` names another folder, which needs the user's "Allow local files" setting. Nothing is ever overwritten. Only the agent that made a recording can render it.

### Example

```text
nova.screen_record_start(area="tab", evidence=true, fileName="draft-review")
... the flow ...
nova.screen_record_stop()
nova.video_render(fps=10, width=900, endHoldMs=1500, segments=[
  {"startMs": 0, "endMs": 6000},
  {"startMs": 6000, "endMs": 14000, "speed": 4},
  {"startMs": 14000}
])
nova.video_render(template="nova-linkedin", captions=[{"startMs": 800, "endMs": 3500, "text": "Table from Wikipedia."}], endCard={"text": "Done in 14 s."})
```

Common refusals: `export.no_recording`, `export.still_recording` (stop the recording first), `export.too_large`, `export.too_many_frames` (shorten the segments or lower `fps`), `export.no_timeline` (`idle`, `keys` or `zoom='auto'` on a recording made without `evidence`).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `agentId` | `string` | No | — | — | The agentId you recorded with. |
| `filePath` | `string` | No | — | — | Recording to export (absolute path). Omit for your most recent recording. |
| `format` | `string` | No | `"gif"` | `gif`, `webm`, `mp4`, `png` | gif: an animated clip that plays everywhere, 255 colours (segments, speed, idle, zoom, keys, captions, endCard, maxBytes). webm: the same options as VP8 video in full colour and usually a fraction of the GIF's size - for a chat or a website. mp4: the same options as H.264 video, the safe upload for LinkedIn, Reddit and YouTube (lossless=true: a cut of the recording itself instead). png: one still frame (atMs) for a thumbnail or a README image. |
| `segments` | `array` of `object` | No | — | ≤ 20 items | Parts of the recording to use, in this order. Omit for the whole recording at normal speed. |
| `fps` | `integer` | No | `10` | 1–30 | Frames per second of the GIF. |
| `width` | `integer` | No | `0` | 0–1920 | Width in pixels (64..1920); 0 keeps the recording's width up to 960. Up to twice the recording's width enlarges it. |
| `loop` | `boolean` | No | `true` | — | Play the GIF in an endless loop. |
| `endHoldMs` | `integer` | No | `0` | 0–10000 | Keep the last frame on screen this long at the end. |
| `idle` | `string` | No | — | `auto` | GIF, WebM and MP4, instead of segments: play what happens at normal speed and speed through the stretches where the picture stood still (from the evidence timeline: observed changes and pressed keys; a still stretch of 1.5 s or more plays in about 0.6 s, speed 2..16). Needs a recording made with evidence=true; idleSegments in the result lists what was chosen. |
| `maxBytes` | `integer` | No | — | 102400–52428800 | GIF, WebM and MP4: a size target in bytes (e.g. 4194304 for a 4 MB README image). GIF: Nova exports, measures and exports again with fewer frames per second (down to 6) and then a narrower picture (down to 320 px), at most 4 tries. WebM and MP4: the bit rate is set from the clip's length so the file lands under the target in one go. sizeTarget in the result lists the tries and whether it was met. |
| `atMs` | `integer` | No | — | ≥ 0 | format='png': the moment in the recording to show; omit for the last frame. The still has the recording's own size unless width is given. |
| `aspect` | `string` | No | — | `16:9`, `4:5`, `1:1`, `9:16` | Output aspect ratio for phones and feeds: '4:5' (LinkedIn, Instagram), '9:16' (Shorts, Reels), '1:1', '16:9'. The largest area of that ratio is cut from the recording and pans smoothly to where things change (from the evidence timeline, or to your zoom areas); without a timeline it stays in the middle. Portrait clips default to 720 px wide. croppedShare in the result is the share of each recorded frame left out. Tip: size the window so the tab is about the target shape (nova.window_set_size, e.g. 900x1250 for 4:5), so nothing is cut away. |
| `includeAudio` | `boolean` | No | `true` | — | webm and mp4: carry the recorded sound (Opus in WebM, AAC in MP4). Parts played at normal speed keep their sound; parts at any other speed (faster or slower, also idle='auto'), the end hold and the end card are silent. Where parts from different places meet, the sound fades over 5 ms instead of clicking. audio in the result says whether the clip has sound; a recording without sound gives a silent clip and audioNote. |
| `lossless` | `boolean` | No | `false` | — | format='mp4' only: cut the recording itself without re-encoding instead - one segment at speed 1, every byte a recorded byte (with its sound), starting at the keyframe at or before startMs. For unchanged evidence in a bug report. |
| `captions` | `array` of `object` | No | — | ≤ 20 items | GIF, WebM and MP4: short texts shown while that part of the recording plays (recording time, so they work with idle and segments), at the top or bottom - by default on the half where nothing happens meanwhile. Two to five words read best on a phone: 'Save clicked.', 'Nothing saved.' A longer text wraps onto two lines and gets smaller rather than being cut. |
| `proofFocus` | `boolean` | No | `true` | — | Styled look: marks that measured a place (nova.screen_record_mark selector/rect) dim the recording outside that place - consecutive ones walk from place to place - and a mark whose check Nova found equal gets a green tick at the end of its place. Only measured places and Nova's own verdicts are drawn, never a guessed spot. false switches it off. |
| `dryRun` | `boolean` | No | `false` | — | Plan only, in about a second: returns what the clip would show when (plan.chapters, plan.captions, plan.proofMarks with clip and recording times), its length, the segments and every check - without decoding or writing a file. Try texts and timing with dryRun, then call again without it. |
| `fromMarks` | `boolean` | No | `false` | — | The easy way: build the clip from the recording's marks (nova.screen_record_mark role and headline) - chapters from task, step and result marks, captions from marks with a caption, the proof focus and result card from check marks, and without segments the pace of idle='auto' with the opening task fitted to 1.8 s - so the call needs no times at all. Use with a template (template='nova-linkedin') and add resultCard and endCard; chapters, captions and captionsFromMarks are left out. Reported in fromMarks {chapters, captions, skipped}. |
| `proofPace` | `boolean` | No | `true` | — | With proofFocus: every place of a run of proof marks (marks less than 15 s apart) gets about 650 ms of clip time - the still recording between them plays faster - and the last holds 1.2 s at normal speed, so checks show evenly without hand-made segments. Works over your segments or idle; parts you cut stay cut. Reported as render.proof_paced and proofPaced. false keeps your own pace. |
| `resultCard` | `object` | No | — | — | The grid (4:5 with chapters) after the checks: the recording shrinks to a picture-in-picture and a card lists every check of the recording's marks - item, both values exactly as the recording shows them, = or ≠, a tick only where Nova found them equal - row by row with a counter, before the end card (about 2.4 s). Its rows come only from the marks' checks the clip shows; more than fit are summed up in its last line. |
| `resultCard.title` | `string` | Yes | — | ≤ 40 characters | The card's title, e.g. 'Check result'. |
| `resultCard.sourceLabel` | `string` | No | — | ≤ 40 characters | Name of the expected side, e.g. 'Wikipedia'. |
| `resultCard.targetLabel` | `string` | No | — | ≤ 40 characters | Name of the actual side, e.g. 'Excel'. |
| `resultCard.subtitle` | `string` | No | — | ≤ 40 characters | One line under the title on what the numbers are, e.g. 'Area in km2'. Without it the card shows the unit all checks named (screen_record_mark check.unit). |
| `captionsFromMarks` | `boolean` | No | `false` | — | Instead of captions: one caption per mark of the recording (nova.screen_record_mark) - its caption, or its label when that is up to 40 characters - from the mark until the next one (at most 4 s). Mark the moments once with a short caption and the clip writes them. Needs evidence=true. |
| `endCard` | `object` | No | — | — | GIF, WebM and MP4: a closing card after the last frame - the last frame dimmed, text large in the middle, subtext smaller below, shown for holdMs. |
| `endCard.text` | `string` | Yes | — | ≤ 80 characters | The closing line; on the grid's card up to three lines, each started with a line break (\n) where you want it. |
| `endCard.subtext` | `string` | No | — | ≤ 80 characters | — |
| `endCard.accent` | `string` | No | — | ≤ 80 characters | The grid's card: one word or phrase of text in the accent colour, green with tone='verified' (e.g. text='Research in.\nExcel out.\nChecked.', accent='Checked.'). |
| `endCard.holdMs` | `integer` | No | `2500` | 500–10000 | — |
| `endCard.tone` | `string` | No | — | `verified` | Styled look: 'verified' turns the card's accent line green. Only when the clip shows a check that really ran (e.g. the agent read the result back), never as decoration. |
| `endCard.logo` | `string` | No | — | — | The grid's card: a logo left of the wordmark (header) - 'nova' for Nova's own symbol, or the absolute path of your PNG (transparent margins are trimmed; outside Nova's recordings folder it needs 'Allow local files'). |
| `endCard.cta` | `string` | No | — | ≤ 40 characters | The grid's end card (styled 4:5 with chapters): what to do next, drawn as a button, e.g. 'Try the free alpha →'. |
| `endCard.url` | `string` | No | — | ≤ 80 characters | The grid's end card: the address written out under the button (a video has no link), e.g. 'example.com/try'. |
| `keys` | `boolean` | No | `false` | — | GIF, WebM and MP4: show the keys you pressed as a badge at the bottom (named keys and Ctrl/Alt/Win shortcuts only, never typed text). Needs a recording made with evidence=true. |
| `zoom` | `any` | No | — | — | Zoom effects in the exported GIF, WebM or MP4 only (the recording stays unchanged). 'auto': from the recording's evidence timeline - every observed change that covered a part of the picture (a menu, a toast, a field) gets a smooth zoom onto that area from shortly before it started until shortly after it settled. Or a list of {startMs, endMs, x, y, width, height} in recording pixels (as the timeline's change boxes). The view keeps the GIF's aspect ratio, enlarges at most 3x and eases in and out over 0.4 s. |
| `saveDir` | `string` | No | — | — | Absolute folder for the clip. Omit to use Nova's Exports folder; any other folder needs 'Allow local files'. |
| `fileName` | `string` | No | — | ≤ 80 characters | File name without extension; default: the recording's name. A taken name gets -2, -3 ... |
| `chapters` | `array` of `object` | No | — | ≤ 12 items | Styled look only (style or a template with one): the clip's chapters, each a small kicker above a headline in the zone above the window, with at most one accent word that the accent colour wipes across. Times are recording time like captions; a chapter stands until endMs or until the next one begins. Keep headlines to three to seven words ('Data found.', 'Excel created.'). A chapter in a part the clip cuts away, or one the next chapter replaces before its first frame (same startMs), is not shown (droppedChapters in the result). In 4:5 chapters switch on the fixed grid: header (header text, chapter counter '01 / 03', a progress line that grows at each chapter), a one-line headline, the recording at 90 % of the width in a 1.4:1 place (record a tab of that shape: nova.get_instructions(topic='demo_clip')), the caption as a neutral pill below and the bottom 200 px free for the feed's controls; a text too long for its line is drawn smaller and named in checks. |
| `motion` | `string` | No | — | `standard`, `short`, `reduced` | Styled look only: how texts move. standard: rise and fade, the accent wipes across its word; short: the moves about a quarter faster for 15-20 s clips (reading time stays); reduced: plain fades, no rise, no wipe. Default: reduced for a GIF (its 255 colours band soft moves), standard otherwise. The result repeats the profile used. |
| `protect` | `array` of `object` | No | — | ≤ 10 items | The proof in the picture that must never be cut: areas in recording pixels (as the timeline's boxes), optionally only from startMs to endMs (recording time). If a zoom or the reframing of aspect would cut one on any frame, the render is refused with render.proof_covered and says where; nothing else changes the picture. |
| `proofLine` | `string` | No | — | ≤ 100 characters | Styled look only: one line of small monospace text at the bottom that says what the clip is, e.g. 'Real run · Claude Code + Nova'. When parts are sped up, Nova adds the speed itself (' · 3×' or ' · 1–16×'), so the clip never claims real time; the result repeats the line as shown. In the 4:5 grid it stands right on the kicker's row: keep it short there ('TIME-LAPSE'). |
| `header` | `string` | No | — | ≤ 40 characters | The 4:5 grid only (styled, with chapters): the brand text top left on every frame in monospace capitals - your product's name - and the end card's wordmark. Omit for no brand. |
| `template` | `string` | No | — | — | An export template's name (nova.video_template_list), e.g. 'nova-linkedin'. Its values stand in for the arguments you leave out; your own arguments win. The result names the template and its version, so the export can be repeated. |
| `style` | `object` | No | — | — | The styled look ('Nova Cinematic'): the recording as a rounded window with shadows on a dark canvas, captions beside the window (never over the picture) in the shipped Inter, an end card that turns into the canvas. Any style value given here - even {} - switches it on; values you leave out come from the template, then from Nova's defaults (nova.video_template_list(name=...) shows them as defaultStyle). Sizes are shares of the output: padding and radius of its width, text sizes of its height. The result repeats the style it used. |
| `style.background` | `array` of `string` | No | — | 2–2 items | Canvas gradient from top left to bottom right. |
| `style.accent` | `string` | No | — | — | Accent colour: the chapter headline's accent word, the end card's line (default Nova's violet #9270F5). |
| `style.accentLight` | `string` | No | — | — | Light accent for small text: kickers and caption accents (default #B39DFF, readable on the dark canvas). |
| `style.verified` | `string` | No | — | — | Colour of a tone='verified' chapter or end card (default #55D6A4). |
| `style.glow` | `number` | No | — | 0–0.5 | Strength of an accent glow behind the window (default 0: none). |
| `style.padding` | `number` | No | — | 0–0.2 | Space between window and the canvas edge, share of the width. |
| `style.radius` | `number` | No | — | 0–0.06 | Window corner radius, share of the width. |
| `style.border` | `number` | No | — | 0–1 | Opacity of the window's thin white outline. |
| `style.shadow` | `number` | No | — | 0–2 | Strength of the two window shadows (1 = default). |
| `style.textSize` | `number` | No | — | 0.02–0.07 | Caption size, share of the height. |
| `style.textColor` | `string` | No | — | — | Captions and the end card's headline. |
| `style.secondaryColor` | `string` | No | — | — | The end card's second line. |
| `style.textAlign` | `string` | No | — | `left`, `center` | Captions and end card: aligned with the window's left edge, or centred. |
| `style.textEnterMs` | `integer` | No | — | 0–1000 | Caption fade-in (it rises a little longer). |
| `style.textExitMs` | `integer` | No | — | 0–1000 | Caption fade-out. |
| `style.headlineSize` | `number` | No | — | 0.025–0.09 | End card headline size, share of the height. |
| `style.brandSize` | `number` | No | — | 0.015–0.05 | End card second line size, share of the height. |
| `style.cardTransitionMs` | `integer` | No | — | 0–1500 | How long the last picture takes to turn into the canvas for the end card. |

Capability bundle: `visual_evidence` (load it with `nova.tools_bundle(bundle='visual_evidence')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->
