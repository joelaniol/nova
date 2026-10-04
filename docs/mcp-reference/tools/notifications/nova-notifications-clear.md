# `nova.notifications_clear`

Bulk-dismisses notifications matching source or age criteria.

---

## 1. Overview

`nova.notifications_clear` performs batch cleanup across notifications. Without arguments, or with `sourceKind` set (with or without `olderThanDays`), it dismisses the matching notifications — they disappear from the default list but remain recoverable via `includeDismissed: true` on `nova.notifications_list`. Passing `olderThanDays` **without** `sourceKind` takes a different, non-reversible path: it permanently deletes notifications older than that threshold from the notification store instead of dismissing them.


---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `sourceKind` | `string` | No | — | `website`, `nova`, `agent` | Only clear notifications from this source. |
| `olderThanDays` | `integer` | No | — | ≥ 0 | Only clear notifications older than N days. |

Capability bundle: `notifications` (load it with `nova.tools_bundle(bundle='notifications')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.notifications_clear",
  "arguments": {
    "sourceKind": "agent",
    "olderThanDays": 7
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Notifications cleared."
    }
  ],
  "structuredContent": {
    "status": "ok"
  }
}
```

---

## 4. Operational Best Practices

* **Routine Maintenance:** Clear stale agent-generated notifications periodically to prevent bloating local storage.
* **Deletion vs. Dismissal:** `olderThanDays` alone permanently deletes the matching rows; every other argument combination only dismisses (soft-hide) them. If you want retention cleanup without losing history, add a `sourceKind` filter alongside `olderThanDays`.

---

## See Also

* [`nova.notifications_dismiss`](nova-notifications-dismiss.md) - Dismiss a single notification.
* [Desktop Notifications Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
