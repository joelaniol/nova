# `nova.notifications_get`

Retrieves complete metadata and payload for a single notification by ID.

---

## 1. Overview

`nova.notifications_get` fetches full details of a specific notification entry, including origin, target tab, sandbox association, delivery state, and timestamps.

* **Capability Bundle:** `notifications`
* **Security Tier:** Tier 1 (Safe)
* **Core Architecture Guide:** [Closed-Loop System & Event Propagation](../../../core-features/closed-loop-system.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`notificationId`** | `string` | Yes | `none` | Notification ID to look up. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.notifications_get",
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
      "text": "Notification 'notif-7b8c9d0e'."
    }
  ],
  "structuredContent": {
    "notificationId": "notif-7b8c9d0e",
    "sourceKind": "agent",
    "title": "Build Verification Complete",
    "body": "All 48 integration smoke tests passed successfully.",
    "tag": null,
    "targetId": null,
    "sandboxId": "A",
    "isRead": false,
    "isDismissed": false,
    "createdAtUtc": "2026-10-02T21:10:00.0000000Z"
  }
}
```

---

## 4. Operational Best Practices

* **Error Handling:** If the ID does not exist in the store, returns standard invalid parameters error.

---

## See Also

* [`nova.notifications_list`](nova-notifications-list.md) - List all notifications.
* [`nova.notifications_open`](nova-notifications-open.md) - Open notification destination.
* [Desktop Notifications Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
