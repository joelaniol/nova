# `nova.notifications_unread_count`

Returns the count of unread, non-dismissed notifications currently in the inbox.

---

## 1. Overview

`nova.notifications_unread_count` provides an ultra-lightweight check for pending alerts without downloading notification bodies or lists, ideal for periodic polling loops.

* **Capability Bundle:** `notifications`
* **Security Tier:** Tier 1 (Safe)
* **Core Architecture Guide:** [Closed-Loop System & Event Propagation](../../../core-features/closed-loop-system.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.notifications_unread_count",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Unread: 3."
    }
  ],
  "structuredContent": {
    "unreadCount": 3
  }
}
```

---

## 4. Operational Best Practices

* **Token Efficient Polling:** Call this lightweight endpoint before deciding whether to invoke `nova.notifications_list`.

---

## See Also

* [`nova.notifications_list`](nova-notifications-list.md) - Read notifications list.
* [Desktop Notifications Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
