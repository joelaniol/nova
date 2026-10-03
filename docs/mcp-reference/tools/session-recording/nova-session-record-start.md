# `nova.session_record_start`

Initiates encrypted background recording of CDP network, DOM mutations, console logs, and user interactions on a tab.

---

## 1. Overview

`nova.session_record_start` attaches Nova's asynchronous recording pipeline to an active browser tab. It streams CDP network events, console messages, JavaScript runtime errors, DOM mutations, IndexedDB operations, and user/agent inputs into local encrypted JSONL chunks.

All sensitive data (passwords, auth tokens, session cookies, DPAPI vault secrets) is automatically redacted at ingestion time prior to disk serialization. Recordings are protected with an ephemeral AES-GCM Data Encryption Key (DEK).

* **Capability Bundle:** `session_recording`
* **Security Tier:** Tier 2 (Session Capture & Tracing)
* **Core Architecture Guide:** [Session Recording & Time-Travel Debugging](../../../core-features/session-recording.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`tabId`** | `string` | Yes | `none` | Browser tab target ID from `nova.tabs`. |
| **`ttlMs`** | `integer` | No | `300000` | Recording time-to-live in ms (default 5 min; max 60 min). |
| **`permissionClasses`** | `array of strings` | No | `["metadata", "interactions"]` | Capture permission classes: `"metadata"`, `"interactions"`, `"console"`, `"network_bodies"`, `"dom_mutations"`. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.session_record_start",
  "arguments": {
    "tabId": "tab-1",
    "ttlMs": 600000,
    "permissionClasses": [
      "metadata",
      "interactions",
      "console",
      "dom_mutations"
    ]
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Started session recording 'rec-9b21f04a' on tab-1 (TTL: 10m)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "recordingId": "rec-9b21f04a",
    "tabId": "tab-1",
    "state": "running",
    "startedAtUtc": "2026-10-02T20:15:00Z",
    "expiresAtUtc": "2026-10-02T20:25:00Z",
    "permissionClasses": [
      "metadata",
      "interactions",
      "console",
      "dom_mutations"
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Pre-Flight Tab Attachment:** Ensure the tab is fully initialized and not in an unattached detached state before starting.
* **Permission Class Minimization:** Only request `network_bodies` when inspecting raw HTTP payloads to reduce disk footprint and avoid payload buffer overhead.
* **Lifecycle Pairing:** Always call [`nova.session_record_stop`](nova-session-record-stop.md) when testing or workflow completes to finalize artifacts cleanly.

---

## 5. Related Tools

* [`nova.session_record_stop`](nova-session-record-stop.md) — Finalize and seal the recording.
* [`nova.session_record_status`](nova-session-record-status.md) — Check live recording health and remaining TTL.
