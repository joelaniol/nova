# `nova.notifications_clear`

Bulk-dismisses notifications matching source or age criteria.

---

## 1. Overview

`nova.notifications_clear` performs batch dismissal across notifications. Without arguments, it dismisses all current notifications. Filters can restrict dismissal to a specific source or age threshold.

* **Capability Bundle:** `notifications`
* **Security Tier:** Tier 2 (Bulk State Change)
* **Core Architecture Guide:** [Closed-Loop System & Event Propagation](../../../core-features/closed-loop-system.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `sourceKind` | `string` | No | — | `website`, `nova`, `agent` | Only clear notifications from this source. |
| `olderThanDays` | `integer` | No | — | ≥ 0 | Only clear notifications older than N days. |
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

* **Routine Maintenance:** Clear stale agent-generated notifications periodically to prevent bloating local SQLite storage.

---

## See Also

* [`nova.notifications_dismiss`](nova-notifications-dismiss.md) - Dismiss a single notification.
* [Desktop Notifications Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
