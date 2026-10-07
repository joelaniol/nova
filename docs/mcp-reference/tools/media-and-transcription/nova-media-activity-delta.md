# `nova.media_activity_delta`

Performs an incremental read of the in-memory media permission activity ring buffer.

---

## 1. Overview

`nova.media_activity_delta` reads new permission events that occurred since a given sequence watermark. Designed for real-time monitoring of agent or user permission prompts.

* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `sinceSequence` | `integer` | No | — | ≥ 0 | Lower bound (exclusive) for entries returned. Default 0 (= return all). |
| `limit` | `integer` | No | — | 1–500 | Max entries returned. Default 200. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "0 new activity entry/entries since sequence 104 (latest now 104)."
    }
  ],
  "structuredContent": {
    "entries": [],
    "count": 0,
    "sinceSequence": 104,
    "latestSequence": 104,
    "lastDeliveredSequence": 104,
    "hasMore": false
  }
}
```

---

## 4. Operational Best Practices

* **Event Polling:** Save `lastDeliveredSequence` and pass it back as `sinceSequence` on the next call to incrementally stream subsequent permission decisions without re-reading past events.

---

## 5. Related Tools

* [`nova.media_activity_audit`](nova-media-activity-audit.md)
* [`nova.media_permission_activity_list`](nova-media-permission-activity-list.md)
