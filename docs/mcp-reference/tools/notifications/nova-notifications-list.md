# `nova.notifications_list`

Queries the Nova notification inbox with filtering by source, website origin, and read status.

---

## 1. Overview

`nova.notifications_list` retrieves notifications stored in Nova's persistent database, allowing agents to monitor background alerts from websites, system events, and peer agents.


---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `sourceKind` | `string` | No | — | `website`, `nova`, `agent` | Filter by source: 'website', 'nova', or 'agent'. |
| `origin` | `string` | No | — | — | Filter by website origin (e.g. 'https://chat.com'). Only relevant for website notifications. |
| `unreadOnly` | `boolean` | No | — | — | If true, only return unread notifications. Default: false. |
| `includeDismissed` | `boolean` | No | — | — | If true, include dismissed notifications. Default: false. |
| `limit` | `integer` | No | — | 1–200 | Maximum number of results. Default: 50, max: 200. |
| `offset` | `integer` | No | — | ≥ 0 | Number of results to skip for pagination. Default: 0. |

Capability bundle: `notifications` (load it with `nova.tools_bundle(bundle='notifications')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.notifications_list",
  "arguments": {
    "unreadOnly": true,
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
      "text": "1 notification(s)."
    }
  ],
  "structuredContent": {
    "count": 1,
    "limit": 10,
    "offset": 0,
    "notifications": [
      {
        "notificationId": "notif-7b8c9d0e",
        "sourceKind": "agent",
        "title": "Build Verification Complete",
        "body": "All 48 integration smoke tests passed successfully in 14.2s.",
        "isRead": false,
        "isDismissed": false,
        "createdAtUtc": "2026-10-02T21:10:00.0000000Z"
      }
    ]
  }
}
```

Shortened for readability: each entry also carries `origin`, `targetId`, `sandboxId`, `profileId`, `tag`, `iconPath`, `imagePath`, `isSilent`, `requiresInteraction`, `language`, `timestampMs`, and `deliveryState` (see [`nova.notifications_get`](nova-notifications-get.md)).

---

## 4. Operational Best Practices

* **Monitoring Website Alerts:** Filter by `sourceKind: "website"` and `origin` to check if a web service (e.g. Discord, GitHub, Slack) sent notifications while running in a background tab.

---

## See Also

* [`nova.notifications_get`](nova-notifications-get.md) - Get full single notification details.
* [`nova.notifications_mark_read`](nova-notifications-mark-read.md) - Mark notification as read.
* [Desktop Notifications Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
