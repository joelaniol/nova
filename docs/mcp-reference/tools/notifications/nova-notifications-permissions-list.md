# `nova.notifications_permissions_list`

Lists website origin notification permissions and reports the effective global default.

---

## 1. Overview

`nova.notifications_permissions_list` inspects which web origins have been granted or denied permission to push browser notifications, along with the global fallback default.

* **Capability Bundle:** `notifications`
* **Security Tier:** Tier 1 (Safe)
* **Core Architecture Guide:** [Closed-Loop System & Event Propagation](../../../core-features/closed-loop-system.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`origin`** | `string` | No | `null` | Filter by origin prefix (e.g. `"https://chat"`). |
| **`mode`** | `string` | No | `null` | Filter by permission mode: `"ask"`, `"allow"`, or `"deny"`. |
| **`limit`** | `integer` | No | `100` | Maximum results (1 - 500). |
| **`offset`** | `integer` | No | `0` | Pagination offset. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.notifications_permissions_list",
  "arguments": {
    "mode": "allow"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "2 permission(s)."
    }
  ],
  "structuredContent": {
    "count": 2,
    "limit": 100,
    "offset": 0,
    "globalDefault": "ask",
    "permissions": [
      {
        "origin": "https://github.com",
        "mode": "allow",
        "updatedAtUtc": "2026-10-01T14:22:00.0000000Z"
      },
      {
        "origin": "https://chat.com",
        "mode": "allow",
        "updatedAtUtc": "2026-10-01T15:00:00.0000000Z"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Global Fallback:** `globalDefault` (`ask`, `allow`, or `deny`) applies to any origin not explicitly listed in `permissions`.

---

## See Also

* [`nova.notifications_permission_set`](nova-notifications-permission-set.md) - Configure per-origin permission.
* [`nova.notifications_permission_default_set`](nova-notifications-permission-default-set.md) - Configure global default.
* [Desktop Notifications Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
