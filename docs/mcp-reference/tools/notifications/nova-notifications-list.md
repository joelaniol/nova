# `nova.notifications_list`

Queries the Nova notification inbox with filtering by source, website origin, and read status.

---

## 1. Overview

`nova.notifications_list` retrieves notifications stored in Nova's persistent database, allowing agents to monitor background alerts from websites, system events, and peer agents.

* **Capability Bundle:** `notifications`
* **Security Tier:** Tier 1 (Safe)
* **Core Architecture Guide:** [Closed-Loop System & Event Propagation](../../../core-features/closed-loop-system.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`sourceKind`** | `string` | No | `null` | Filter by source: `"website"`, `"nova"`, or `"agent"`. |
| **`origin`** | `string` | No | `null` | Filter by website origin (e.g. `"https://chat.com"`). |
| **`unreadOnly`** | `boolean` | No | `false` | When `true`, returns only unread notifications. |
| **`includeDismissed`** | `boolean` | No | `false` | When `true`, includes dismissed notifications. |
| **`limit`** | `integer` | No | `50` | Maximum results to return (1 - 200). |
| **`offset`** | `integer` | No | `0` | Pagination offset. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

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

---

## 4. Operational Best Practices

* **Monitoring Website Alerts:** Filter by `sourceKind: "website"` and `origin` to check if a web service (e.g. Discord, GitHub, Slack) sent notifications while running in a background tab.

---

## See Also

* [`nova.notifications_get`](nova-notifications-get.md) - Get full single notification details.
* [`nova.notifications_mark_read`](nova-notifications-mark-read.md) - Mark notification as read.
* [Desktop Notifications Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
