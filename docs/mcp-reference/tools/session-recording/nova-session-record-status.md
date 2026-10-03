# `nova.session_record_status`

Returns the live state, expiry timestamp, active permission classes, and byte counts of a recording.

---

## 1. Overview

`nova.session_record_status` reports the current lifecycle phase (`running`, `finalised`, `expired`), storage usage, and configuration of a session recording. It is used to monitor recording health and detect approaching TTL expiration.

* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Session Recording & Time-Travel Debugging](../../../core-features/session-recording.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `recordingId` | `string` | Yes | — | — | Recording ID returned from session_record_start. |

Capability bundle: `session_recording` (load it with `nova.tools_bundle(bundle='session_recording')`).
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
      "text": "Recording rec-9b21f04a is running: expires in 8m 20s (total bytes: 342 KB)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "recordingId": "rec-9b21f04a",
    "state": "running",
    "expiresAtUtc": "2026-10-02T20:25:00Z",
    "remainingMs": 500000,
    "totalBytesWritten": 350208,
    "eventCount": 312,
    "activeStreams": [
      "network",
      "console",
      "interactions"
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Proactive Extension:** Check `remainingMs`; if a long test scenario is still executing, use [`nova.session_record_extend`](nova-session-record-extend.md) before expiration.
* **Buffer Monitoring:** If `totalBytesWritten` grows unexpectedly fast, verify whether unnecessary permission classes like `network_bodies` were enabled on heavy asset-streaming sites.

---

## 5. Related Tools

* [`nova.session_record_extend`](nova-session-record-extend.md) — Extend TTL before expiration.
* [`nova.session_record_stop`](nova-session-record-stop.md) — Halt recording.
