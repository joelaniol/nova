# `nova.notifications_permission_set`

Configures notification permission (Ask, Allow, or Deny) for a specific website origin.

---

## 1. Overview

`nova.notifications_permission_set` overrides the global notification policy for a specific origin. Setting an origin to `allow` lets the website dispatch notifications without user consent prompts.

* **Capability Bundle:** `notifications`
* **Security Tier:** Tier 2 (Configuration)
* **Core Architecture Guide:** [Closed-Loop System & Event Propagation](../../../core-features/closed-loop-system.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`origin`** | `string` | Yes | `none` | Website origin (e.g. `"https://chat.com"`). Normalized to standard web scheme and host. |
| **`mode`** | `string` | Yes | `none` | Permission mode: `"ask"`, `"allow"`, or `"deny"`. |
| **`_meta`** | `object` | No | `null` | Optional metadata with configuration intent. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.notifications_permission_set",
  "arguments": {
    "origin": "https://calendar.google.com",
    "mode": "allow",
    "_meta": {
      "intent": "Allow calendar notifications for scheduled reminders"
    }
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Permission set: https://calendar.google.com = allow."
    }
  ],
  "structuredContent": {
    "status": "ok",
    "origin": "https://calendar.google.com",
    "mode": "allow"
  }
}
```

---

## 4. Operational Best Practices

* **Normalized Origin:** Always provide clean origin strings (scheme + hostname). Path components are automatically stripped.

---

## See Also

* [`nova.notifications_permissions_list`](nova-notifications-permissions-list.md) - List configured permissions.
* [`nova.notifications_permission_default_set`](nova-notifications-permission-default-set.md) - Set global default.
* [Desktop Notifications Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
