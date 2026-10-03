# `nova.notifications_mark_read`

Marks a notification as read without dismissing it from the inbox.

---

## 1. Overview

`nova.notifications_mark_read` flags an unread notification as processed, decrementing the unread counter while keeping the entry visible in the inbox history.

* **Capability Bundle:** `notifications`
* **Security Tier:** Tier 2 (State Change)
* **Core Architecture Guide:** [Closed-Loop System & Event Propagation](../../../core-features/closed-loop-system.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`notificationId`** | `string` | Yes | `none` | Notification ID to mark as read. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.notifications_mark_read",
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
      "text": "Marked read: notif-7b8c9d0e."
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

* **Idempotency:** Calling mark read on an already read notification is a safe no-op.

---

## See Also

* [`nova.notifications_dismiss`](nova-notifications-dismiss.md) - Dismiss notification.
* [`nova.notifications_clear`](nova-notifications-clear.md) - Clear multiple notifications.
* [Desktop Notifications Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
