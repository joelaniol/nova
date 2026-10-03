# `nova.session_record_extend`

Extends an active recording’s time-to-live (TTL) to prevent premature expiration during long workflows.

---

## 1. Overview

`nova.session_record_extend` adds additional time in milliseconds to a running session recording's expiry deadline. To prevent runaway disk consumption, extensions are strictly bounded by a 60-minute hard cap measured from the recording's original start timestamp.

* **Capability Bundle:** `session_recording`
* **Security Tier:** Tier 2 (Session Management)
* **Core Architecture Guide:** [Session Recording & Time-Travel Debugging](../../../core-features/session-recording.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`recordingId`** | `string` | Yes | `none` | Recording ID returned by `nova.session_record_start`. |
| **`additionalMs`** | `integer` | Yes | `none` | Additional milliseconds to add to current expiration deadline. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

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
      "text": "Extended recording rec-9b21f04a by 10m. New expiry: 2026-10-02T20:35:00Z."
    }
  ],
  "structuredContent": {
    "ok": true,
    "recordingId": "rec-9b21f04a",
    "newExpiresAtUtc": "2026-10-02T20:35:00Z",
    "extendedByMs": 600000
  }
}
```

---

## 4. Operational Best Practices

* **60-Minute Hard Ceiling:** Nova clamps any extension request that would exceed 60 minutes from the initial start time.
* **Active Recordings Only:** Cannot extend finalized or already expired recordings; if expired, start a new recording session.

---

## 5. Related Tools

* [`nova.session_record_status`](nova-session-record-status.md) — Check remaining time.
* [`nova.session_record_start`](nova-session-record-start.md) — Initial session recorder.
