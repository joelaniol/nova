# `nova.notifications_open`

Navigates to the originating tab, website, or resource referenced by a notification.

---

## 1. Overview

`nova.notifications_open` activates the target surface associated with a notification (focusing an open tab or opening the URL in its origin sandbox). If the notification is missing, dismissed, or targetless, returns a structured no-op status.

* **Capability Bundle:** `notifications`
* **Security Tier:** Tier 2 (Navigation)
* **Core Architecture Guide:** [Closed-Loop System & Event Propagation](../../../core-features/closed-loop-system.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`notificationId`** | `string` | Yes | `none` | Notification ID whose target to open. |
| **`agentId`** | `string` | No | `"default"` | Optional agent identifier. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.notifications_open",
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
      "text": "Opened: notif-7b8c9d0e."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "notificationId": "notif-7b8c9d0e"
  }
}
```

---

## 4. Operational Best Practices

* **Structured No-Op Handling:** If a notification has no target URL or tab, returns `ok: false` with `status: "no_target"` and `reasonCode: "notification.no_target"` rather than throwing an exception.
* **Dismissed Safety:** Opening an already dismissed notification returns `status: "already_dismissed"`.

---

## See Also

* [`nova.notifications_get`](nova-notifications-get.md) - Inspect notification target before opening.
* [Desktop Notifications Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
