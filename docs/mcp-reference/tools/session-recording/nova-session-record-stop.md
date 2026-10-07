# `nova.session_record_stop`

Stops an active session recording, flushes buffered events, and finalizes the encrypted artifact with a per-stream SHA-256 integrity manifest.

---

## 1. Overview

`nova.session_record_stop` cleanly terminates an ongoing session recording. It flushes in-memory streaming channels, finalizes encrypted chunk files on disk, computes SHA-256 checksums in `integrity.json`, and seals the recording for post-hoc forensic inspection.

* **Core Architecture Guide:** [Session Recording & Time-Travel Debugging](../../../core-features/session-recording/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `recordingId` | `string` | Yes | — | — | Recording ID returned from session_record_start. |
| `reason` | `string` | No | — | — | Optional canonical reason code (default: agent_stop). |

Capability bundle: `session_recording` (load it with `nova.tools_bundle(bundle='session_recording')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.session_record_stop",
  "arguments": {
    "recordingId": "rec-9b21f04a",
    "reason": "test_complete"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Recording rec-9b21f04a — state=completed\n  tab=tab-1  expires=2026-10-02T20:25:00.0000000Z  stopReason=test_complete"
    }
  ],
  "structuredContent": {
    "ok": true,
    "recordingId": "rec-9b21f04a",
    "targetId": "tab-1",
    "sandboxId": null,
    "state": "completed",
    "startedAtUtc": "2026-10-02T20:15:00Z",
    "expiresAtUtc": "2026-10-02T20:25:00Z",
    "stoppedAtUtc": "2026-10-02T20:18:42Z",
    "stopReason": "test_complete",
    "permissionClasses": [
      "metadata",
      "interactions_mcp",
      "dom_snapshots"
    ],
    "captureWaves": ["R1", "R2"]
  }
}
```

The per-stream SHA-256 hashes themselves are written to `integrity.json` inside the recording directory, not returned in this tool's result.

---

## 4. Operational Best Practices

* **Atomic Finalization:** The temporary directory `.tmp` is atomically renamed to its permanent recording directory upon successful stop.
* **Query Ready:** Once finalized, query tools such as [`nova.session_record_query`](nova-session-record-query.md) and [`nova.session_record_interactions`](nova-session-record-interactions.md) can be safely executed against the recording.
* **Auto-Stop on Tab Close:** If the parent tab is closed before `stop` is called, Nova automatically halts recording and preserves available chunks.

---

## 5. Related Tools

* [`nova.session_record_start`](nova-session-record-start.md) — Start recording session.
* [`nova.session_record_query`](nova-session-record-query.md) — Query network entries in finalized recordings.
