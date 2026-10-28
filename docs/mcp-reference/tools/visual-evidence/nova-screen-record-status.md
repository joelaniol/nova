# `nova.screen_record_status`

> **Shows whether a recording of the Nova window is running, paused or already finished.**

* **Core Feature Guide:** [Visual Evidence & Auditing](../../../research/evidence-verification-mode-evm/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

`nova.screen_record_status` reports the recording started with [`nova.screen_record_start`](nova-screen-record-start.md): `state` is `recording`, `paused` while Nova is minimized (`reasonCode: "video.source_minimized"`) or another agent's tab is shown (`reasonCode: "video.foreign_claim"`), or `finishing` once the recording has ended and Nova is still writing and checking the file (`stage`; [`nova.screen_record_stop`](nova-screen-record-stop.md) waits for it). While recording it also reports how long it runs (`elapsedMs`), how many frames are written, how many of them repeat the previous picture because the window did not change (`duplicateFrames`), how many were skipped because the computer stalled (`droppedFrames`), and the file size so far.

When no recording runs, the answer is `ok: false` with `reasonCode: "not_recording"` and `lastRecording` holds the result of the most recent one - also when it ended by itself, for example at its time limit or because Nova stayed minimized.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `agentId` | `string` | No | — | — | The agentId you started the recording with. |

Capability bundle: `visual_evidence` (load it with `nova.tools_bundle(bundle='visual_evidence')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Related Tools

* [`nova.screen_record_start`](nova-screen-record-start.md) — Starts screen recordings of the Nova window or tab
* [`nova.screen_record_stop`](nova-screen-record-stop.md) — Stops active recording and returns the verified video
* [`nova.screen_record_mark`](nova-screen-record-mark.md) — Adds timeline markers during recording
* [`nova.screen_record_inspect`](nova-screen-record-inspect.md) — Inspects recorded evidence and manifests
