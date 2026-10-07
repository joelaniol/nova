# `nova.session_record_extend`

Extends an active recording’s time-to-live (TTL) to prevent premature expiration during long workflows.

---

## 1. Overview

`nova.session_record_extend` adds additional time in milliseconds to a running session recording's expiry deadline. To prevent runaway disk consumption, extensions are strictly bounded by a 60-minute hard cap measured from the recording's original start timestamp.

* **Core Architecture Guide:** [Session Recording & Time-Travel Debugging](../../../core-features/session-recording/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `recordingId` | `string` | Yes | — | — | Recording ID returned from session_record_start. |
| `additionalMs` | `integer` | Yes | — | 1000–3600000 | Additional time to add to the recording's expiry, in milliseconds. |

Capability bundle: `session_recording` (load it with `nova.tools_bundle(bundle='session_recording')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.session_record_extend",
  "arguments": {
    "recordingId": "rec-9b21f04a",
    "additionalMs": 600000
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Recording rec-9b21f04a — state=running\n  tab=tab-1  expires=2026-10-02T20:35:00.0000000Z"
    }
  ],
  "structuredContent": {
    "ok": true,
    "recordingId": "rec-9b21f04a",
    "targetId": "tab-1",
    "sandboxId": null,
    "state": "running",
    "startedAtUtc": "2026-10-02T20:15:00Z",
    "expiresAtUtc": "2026-10-02T20:35:00Z",
    "stoppedAtUtc": null,
    "stopReason": null,
    "permissionClasses": [
      "metadata",
      "interactions_mcp",
      "dom_snapshots"
    ],
    "captureWaves": ["R1", "R2"]
  }
}
```

The tool returns the same status-shaped payload as [`nova.session_record_status`](nova-session-record-status.md) — there is no separate `newExpiresAtUtc`/`extendedByMs` field; read `expiresAtUtc` for the new deadline.

---

## 4. Operational Best Practices

* **60-Minute Hard Ceiling:** Nova clamps any extension request that would exceed 60 minutes from the initial start time.
* **Active Recordings Only:** Cannot extend finalized or already expired recordings; if expired, start a new recording session.

---

## 5. Related Tools

* [`nova.session_record_status`](nova-session-record-status.md) — Check remaining time.
* [`nova.session_record_start`](nova-session-record-start.md) — Initial session recorder.
