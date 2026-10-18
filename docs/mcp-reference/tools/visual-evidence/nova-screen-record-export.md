# `nova.screen_record_export`

> **Turns a screen recording into an animated GIF for a README, an issue or a chat.**

* **Core Feature Guide:** [Visual Evidence & Auditing](../../../research/evidence-verification-mode-evm/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

A video recorded with [`nova.screen_record_start`](nova-screen-record-start.md) is the evidence; a short GIF is what people actually watch in a README or an issue. `nova.screen_record_export` makes one from the most recent recording, or from the recording `filePath` names.

**Cut and tighten, never stage.** `segments` picks parts of the recording and plays them one after the other, each at its own `speed`: a waiting phase at `speed: 4` takes a quarter of the time, a detail at `speed: 0.5` runs at half speed. Every frame in the GIF is a frame that was recorded. `endHoldMs` keeps the last frame on screen at the end.

**Readable interface text.** The GIF uses one palette of 255 colours for the whole clip and stores only what changed from one frame to the next, without dithering. Text and panels stay sharp and the file stays small: for interface clips, 8 to 12 frames per second at 800 to 1000 pixels wide is the usual range. `width` also enlarges a recording of a small area, up to twice its size. The result warns (`note`) when the file is larger than the 10 MB GitHub shows inline.

The GIF goes to Nova's Exports folder (`ScreenRecordings`) next to the recordings unless `saveDir` names another folder, which needs the user's "Allow local files" setting. Nothing is ever overwritten.

### Example

```text
nova.screen_record_start(area="tab", includeCursor=false, fileName="draft-review")
... the flow ...
nova.screen_record_stop()
nova.screen_record_export(fps=10, width=900, endHoldMs=1500, segments=[
  {"startMs": 0, "endMs": 6000},
  {"startMs": 6000, "endMs": 14000, "speed": 4},
  {"startMs": 14000}
])
```

Common refusals: `export.no_recording`, `export.still_recording` (stop the recording first), `export.too_large`, `export.too_many_frames` (shorten the segments or lower `fps`).

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
| `includeAudio` | `boolean` | No | `true` | — | webm and mp4: carry the recorded sound (Opus in WebM, AAC in MP4). Parts played at normal speed keep their sound; sped-up parts (speed, idle='auto'), the end hold and the end card are silent. audio in the result says whether the clip has sound; a recording without sound gives a silent clip and audioNote. |
| `lossless` | `boolean` | No | `false` | — | format='mp4' only: cut the recording itself without re-encoding instead - one segment at speed 1, every byte a recorded byte (with its sound), starting at the keyframe at or before startMs. For unchanged evidence in a bug report. |
| `captions` | `array` of `object` | No | — | ≤ 20 items | GIF, WebM and MP4: short texts shown while that part of the recording plays (recording time, so they work with idle and segments), at the top or bottom - by default on the half where nothing happens meanwhile. Two to five words read best on a phone: 'Save clicked.', 'Nothing saved.' A longer text wraps onto two lines and gets smaller rather than being cut. |
| `endCard` | `object` | No | — | — | GIF, WebM and MP4: a closing card after the last frame - the last frame dimmed, text large in the middle, subtext smaller below, shown for holdMs. |
| `endCard.text` | `string` | Yes | — | ≤ 80 characters | — |
| `endCard.subtext` | `string` | No | — | ≤ 80 characters | — |
| `endCard.holdMs` | `integer` | No | `2500` | 500–10000 | — |
| `keys` | `boolean` | No | `false` | — | GIF, WebM and MP4: show the keys you pressed as a badge at the bottom (named keys and Ctrl/Alt/Win shortcuts only, never typed text). Needs a recording made with evidence=true. |
| `zoom` | `any` | No | — | — | Zoom effects in the exported GIF, WebM or MP4 only (the recording stays unchanged). 'auto': from the recording's evidence timeline - every observed change that covered a part of the picture (a menu, a toast, a field) gets a smooth zoom onto that area from shortly before it started until shortly after it settled. Or a list of {startMs, endMs, x, y, width, height} in recording pixels (as the timeline's change boxes). The view keeps the GIF's aspect ratio, enlarges at most 3x and eases in and out over 0.4 s. |
| `saveDir` | `string` | No | — | — | Absolute folder for the GIF. Omit to use Nova's Exports folder; any other folder needs 'Allow local files'. |
| `fileName` | `string` | No | — | ≤ 80 characters | File name without extension; default: the recording's name. A taken name gets -2, -3 ... |

Capability bundle: `visual_evidence` (load it with `nova.tools_bundle(bundle='visual_evidence')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->
