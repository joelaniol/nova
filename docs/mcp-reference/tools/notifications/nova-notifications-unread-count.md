# `nova.notifications_unread_count`

Returns the count of unread, non-dismissed notifications currently in the inbox.

---

## 1. Overview

`nova.notifications_unread_count` provides an ultra-lightweight check for pending alerts without downloading notification bodies or lists, ideal for periodic polling loops.


---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

Capability bundle: `notifications` (load it with `nova.tools_bundle(bundle='notifications')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
