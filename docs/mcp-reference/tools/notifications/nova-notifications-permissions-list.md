# `nova.notifications_permissions_list`

Lists website origin notification permissions and reports the effective global default.

---

## 1. Overview

`nova.notifications_permissions_list` inspects which web origins have been granted or denied permission to push browser notifications, along with the global fallback default.


---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `mode` | `string` | No | — | `ask`, `allow`, `deny` | Filter by mode. |
| `origin` | `string` | No | — | — | Filter by origin prefix (e.g. 'https://chat'). |
| `limit` | `integer` | No | — | 1–500 | Max results. Default: 100. |
| `offset` | `integer` | No | — | ≥ 0 | Pagination offset. |

Capability bundle: `notifications` (load it with `nova.tools_bundle(bundle='notifications')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
