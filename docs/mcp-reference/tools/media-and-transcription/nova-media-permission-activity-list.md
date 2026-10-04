# `nova.media_permission_activity_list`

Reads recent entries from the in-memory ring buffer of camera, microphone, speaker, screen-share, and geolocation permission decisions.

---

## 1. Overview

`nova.media_permission_activity_list` retrieves historical prompt decisions, showing whether requests were allowed once, remembered, or denied.

* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `limit` | `integer` | No | — | 1–500 | Max entries returned, newest first. Default 200. |
| `origin` | `string` | No | — | — | Filter by origin prefix. Note: 'https://meet' also matches 'https://meeting.evil.com'. Use full origin for exact lookups. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "1 activity entry/entries (in-memory ring buffer, cleared on app restart)."
    }
  ],
  "structuredContent": {
    "entries": [
      {
        "sequence": 1,
        "timestampUtc": "2026-10-02T19:00:00Z",
        "targetId": "tab-1",
        "origin": "https://meet.example.com",
        "kind": "Microphone",
        "state": "allow",
        "source": "SiteGrant",
        "lifetime": "session",
        "isUserInitiated": true,
        "isHiddenCrawl": false,
        "hashedDeviceIdHex": null
      }
    ],
    "count": 1,
    "limit": 10
  }
}
```

The ring buffer is in-memory only and resets when Nova restarts — it is a live trace, not a permanent audit log.

---

## 4. Operational Best Practices

* **Trace Interactive Decisions:** Determine whether a human operator clicked "Allow" or "Block" during an automated session.

---

## 5. Related Tools

* [`nova.media_activity_delta`](nova-media-activity-delta.md)
* [`nova.media_permissions_list`](nova-media-permissions-list.md)
