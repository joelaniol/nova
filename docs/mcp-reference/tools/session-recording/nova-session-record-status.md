# `nova.session_record_status`

Returns the live state, start/expiry timestamps, tab/sandbox binding, and granted permission classes of a recording.

---

## 1. Overview

`nova.session_record_status` reports the current lifecycle state (`recording`, exposed as `running`; or `completed`, `aborted`, `stopped_revoked`, `aborted_crash`, `aborted_crash_dek_lost`), the bound tab/sandbox, start/expiry/stop timestamps, and the granted permission classes and capture waves of a session recording. It is used to monitor recording health and detect approaching TTL expiration.

* **Core Architecture Guide:** [Session Recording & Time-Travel Debugging](../../../core-features/session-recording.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `recordingId` | `string` | Yes | — | — | Recording ID returned from session_record_start. |

Capability bundle: `session_recording` (load it with `nova.tools_bundle(bundle='session_recording')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.session_record_status",
  "arguments": {
    "recordingId": "rec-9b21f04a"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Recording rec-9b21f04a — state=running\n  tab=tab-1  expires=2026-10-02T20:25:00.0000000Z"
    }
  ],
  "structuredContent": {
    "ok": true,
    "recordingId": "rec-9b21f04a",
    "targetId": "tab-1",
    "sandboxId": null,
    "state": "running",
    "startedAtUtc": "2026-10-02T20:15:00Z",
    "expiresAtUtc": "2026-10-02T20:25:00Z",
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

---

## 4. Operational Best Practices

* **Proactive Extension:** Check `expiresAtUtc` against the current time; if a long test scenario is still executing, use [`nova.session_record_extend`](nova-session-record-extend.md) before expiration.
* **Permission Audit:** Check `permissionClasses` to confirm which capture classes (e.g. `request_bodies`/`response_bodies`) are actually active before assuming a stream was captured.

---

## 5. Related Tools

* [`nova.session_record_extend`](nova-session-record-extend.md) — Extend TTL before expiration.
* [`nova.session_record_stop`](nova-session-record-stop.md) — Halt recording.
