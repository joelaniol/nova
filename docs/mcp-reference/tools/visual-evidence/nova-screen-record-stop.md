# `nova.screen_record_stop`

> **Stops the recording of the Nova window and returns the video, checked for correctness.**

* **Core Feature Guide:** [Visual Evidence & Auditing](../../../research/evidence-verification-mode-evm/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

`nova.screen_record_stop` ends the recording started with [`nova.screen_record_start`](nova-screen-record-start.md) and waits until the file is complete. It returns `filePath`, `durationMs`, `frames`, `bytes`, the encoder used, `stoppedBy` (`request`, `user`, `max_duration`, `max_bytes`, `user_minimized`, `source_closed`, `stalled`) and `pauses` - the moments Nova was minimized or another agent's tab was shown, each with its reason.

**File format.** By default the video is a classic MP4 (`container: "mp4"`) that every player, editor and upload form accepts. Nova records into a crash-safe fragmented file and rewrites it after the stop, without re-encoding; a long recording therefore takes a moment to finish, and [`nova.screen_record_status`](nova-screen-record-status.md) reports `state: "finishing"` meanwhile. If the rewrite is not possible, the fragmented file is kept and `finalizeNote` says why. Started with `finalize="fragmented"`, the file stays as recorded.

**Self-check.** A broken recording can still be a perfectly valid video file - full of wrong colours, stripes or a black picture. So Nova does not trust the file blindly: while recording it keeps small reference images, and after the stop it decodes the finished video the way a player would and compares. `selfCheck.verdict` is `ok`, `suspect` (a single bad moment) or `broken`, with up to three `failures` naming what went wrong and when, for example `video.color_mismatch`, `video.roundtrip_mismatch`, `video.frames_uniform` or `video.frame_count_mismatch`. Your agent gets this verdict without having to look at a single frame.

`verified: true` means the verdict was `ok`. Otherwise the answer is `ok: false` with `reasonCode: "video.not_verified"`: the file is kept for inspection but should not be presented as evidence.

When no recording runs, the answer is `ok: false` with `reasonCode: "not_recording"` and `lastRecording` holds the most recent result.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `agentId` | `string` | No | — | — | The agentId you started the recording with. |

Capability bundle: `visual_evidence` (load it with `nova.tools_bundle(bundle='visual_evidence')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->
