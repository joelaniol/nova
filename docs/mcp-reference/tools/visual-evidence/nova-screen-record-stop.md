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
| `holdMs` | `integer` | No | `0` | 0–10000 | Keep recording this many ms before stopping: the last result stays in the picture (a clip needs 2-3 s after the last mark; material.end_too_soon otherwise). Use it instead of waiting in a shell. |

Capability bundle: `visual_evidence` (load it with `nova.tools_bundle(bundle='visual_evidence')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova.screen_record_stop",
  "arguments": {
    "holdMs": 2000
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Screen recording finished: C:/Workspace/Exports/ScreenRecordings/audit_run.mp4 (duration: 18.2s, 546 frames, verified: ok)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "stopped",
    "filePath": "C:/Workspace/Exports/ScreenRecordings/audit_run.mp4",
    "durationMs": 18200,
    "frames": 546,
    "bytes": 5242880,
    "container": "mp4",
    "stoppedBy": "request",
    "verified": true,
    "selfCheck": {
      "verdict": "ok",
      "failures": []
    }
  }
}
```

---

## 4. Operational Best Practices

* **Always Specify `holdMs`:** When recording UI automation, passing `holdMs: 2000` to `2500` ensures that the final state remains visible on screen for viewers to read and comprehend before the recording terminates. Without `holdMs`, stopping immediately after a final click can cause `material.end_too_soon` validation warnings in downstream rendering.
* **Inspect the Self-Check Verdict:** Nova automatically decodes sample frames of the output file to confirm color accuracy and roundtrip fidelity. Check `selfCheck.verdict`: if `ok: false` with `reasonCode: "video.not_verified"`, inspect the listed `failures` before presenting the asset in formal audit reports.
* **Transition to Editing:** Once stopped, pass the resulting `filePath` directly to [`nova.video_render`](../video-editing/nova-video-render.md) or [`nova.screen_record_inspect`](nova-screen-record-inspect.md).

---

## 5. Related Tools

* [`nova.screen_record_start`](nova-screen-record-start.md) — Starts screen recording sessions.
* [`nova.screen_record_status`](nova-screen-record-status.md) — Inspects active recording state.
* [`nova.screen_record_inspect`](nova-screen-record-inspect.md) — Inspects recording evidence and timeline.
* [`nova.video_render`](../video-editing/nova-video-render.md) — Renders the recorded video into styled clips.
