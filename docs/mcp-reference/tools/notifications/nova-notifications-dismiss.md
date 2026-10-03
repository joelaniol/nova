# `nova.notifications_dismiss`

Dismisses a notification, hiding it from the default inbox view.

---

## 1. Overview

`nova.notifications_dismiss` marks a notification as dismissed. Dismissed entries are excluded from standard list views and unread counts unless `includeDismissed: true` is passed.

* **Capability Bundle:** `notifications`
* **Security Tier:** Tier 2 (State Change)
* **Core Architecture Guide:** [Closed-Loop System & Event Propagation](../../../core-features/closed-loop-system.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`notificationId`** | `string` | Yes | `none` | Notification ID to dismiss. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.notifications_dismiss",
  "arguments": {
    "notificationId": "notif-7b8c9d0e"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Dismissed: notif-7b8c9d0e."
    }
  ],
  "structuredContent": {
    "status": "ok",
    "notificationId": "notif-7b8c9d0e"
  }
}
```

---

## 4. Operational Best Practices

* **Clean Inbox:** Call after resolving an alert so the user's notification drawer stays uncluttered.

---

## See Also

* [`nova.notifications_clear`](nova-notifications-clear.md) - Bulk dismiss notifications.
* [`nova.notifications_mark_read`](nova-notifications-mark-read.md) - Mark as read without dismissing.
* [Desktop Notifications Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
