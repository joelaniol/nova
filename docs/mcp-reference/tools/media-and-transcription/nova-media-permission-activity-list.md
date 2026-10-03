# `nova.media_permission_activity_list`

Reads the complete in-memory ring buffer audit log of camera, mic, and screen permission decisions.

---

## 1. Overview

`nova.media_permission_activity_list` retrieves historical prompt decisions, showing whether requests were allowed once, remembered, or denied.

* **Capability Bundle:** `system_tools`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`limit`** | `integer` | No | `null` | Max entries returned, newest first. Default 200. |
| **`origin`** | `string` | No | `null` | Filter by origin prefix. Note: 'https://meet' also matches 'https://meeting.evil.com'. Use full origin for exact lookups. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.media_permission_activity_list",
  "arguments": {
    "limit": 10
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Retrieved 1 permission decision from activity log."
    }
  ],
  "structuredContent": {
    "ok": true,
    "total": 1,
    "decisions": [
      {
        "origin": "https://meet.example.com",
        "axis": "microphone",
        "decision": "allow_session",
        "timestampUtc": "2026-10-02T19:00:00Z"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Trace Interactive Decisions:** Determine whether a human operator clicked "Allow" or "Block" during an automated session.

---

## 5. Related Tools

* [`nova.media_activity_delta`](nova-media-activity-delta.md)
* [`nova.media_permissions_list`](nova-media-permissions-list.md)
