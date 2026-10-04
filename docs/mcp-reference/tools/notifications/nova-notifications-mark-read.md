# `nova.notifications_mark_read`

Marks a notification as read without dismissing it from the inbox.

---

## 1. Overview

`nova.notifications_mark_read` flags an unread notification as processed, decrementing the unread counter while keeping the entry visible in the inbox history.


---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `notificationId` | `string` | Yes | — | — | The notification ID to mark as read. |

Capability bundle: `notifications` (load it with `nova.tools_bundle(bundle='notifications')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
* **Unknown IDs:** the call does not verify that `notificationId` exists before writing; passing an ID that does not exist still returns `status: "ok"`.

---

## See Also

* [`nova.notifications_dismiss`](nova-notifications-dismiss.md) - Dismiss notification.
* [`nova.notifications_clear`](nova-notifications-clear.md) - Clear multiple notifications.
* [Desktop Notifications Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
