# `nova.media_activity_delta`

Performs an incremental read of the in-memory media permission activity ring buffer.

---

## 1. Overview

`nova.media_activity_delta` reads new permission events that occurred since a given sequence watermark. Designed for real-time monitoring of agent or user permission prompts.

* **Capability Bundle:** `system_tools`
* **Security Tier:** Tier 1 (Read-Only Stream)
* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`limit`** | `integer` | No | `null` | Max entries returned. Default 200. |
| **`sinceSequence`** | `integer` | No | `null` | Lower bound (exclusive) for entries returned. Default 0 (= return all). |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.media_activity_delta",
  "arguments": {
    "sinceSequence": 104,
    "limit": 20
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Retrieved 0 new permission activity events."
    }
  ],
  "structuredContent": {
    "ok": true,
    "highestSequence": 104,
    "events": []
  }
}
```

---

## 4. Operational Best Practices

* **Event Polling:** Save `highestSequence` to incrementally stream subsequent permission decisions without re-reading past events.

---

## 5. Related Tools

* [`nova.media_activity_audit`](nova-media-activity-audit.md)
* [`nova.media_permission_activity_list`](nova-media-permission-activity-list.md)
