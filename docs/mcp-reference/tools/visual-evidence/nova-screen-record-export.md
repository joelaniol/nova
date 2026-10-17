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
| `filePath` | `string` | No | — | — | Recording to export (absolute path). Omit for the most recent recording. |
| `format` | `string` | No | `"gif"` | `gif` | Output format. |
| `segments` | `array` of `object` | No | — | ≤ 20 items | Parts of the recording to use, in this order. Omit for the whole recording at normal speed. |
| `fps` | `integer` | No | `10` | 1–30 | Frames per second of the GIF. |
| `width` | `integer` | No | `0` | 0–1920 | Width in pixels (64..1920); 0 keeps the recording's width up to 960. Up to twice the recording's width enlarges it. |
| `loop` | `boolean` | No | `true` | — | Play the GIF in an endless loop. |
| `endHoldMs` | `integer` | No | `0` | 0–10000 | Keep the last frame on screen this long at the end. |
| `saveDir` | `string` | No | — | — | Absolute folder for the GIF. Omit to use Nova's Exports folder; any other folder needs 'Allow local files'. |
| `fileName` | `string` | No | — | ≤ 80 characters | File name without extension; default: the recording's name. A taken name gets -2, -3 ... |

Capability bundle: `visual_evidence` (load it with `nova.tools_bundle(bundle='visual_evidence')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->
