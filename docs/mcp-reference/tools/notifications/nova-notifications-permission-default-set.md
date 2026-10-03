# `nova.notifications_permission_default_set`

Sets the global website notification permission default (Ask, Allow, or Deny).

---

## 1. Overview

`nova.notifications_permission_default_set` sets the baseline behavior for web origins that do not have an explicit rule in `nova.notifications_permissions_list`. Setting this to `deny` suppresses all notification prompts across the browser.

* **Capability Bundle:** `notifications`
* **Security Tier:** Tier 2 (Configuration)
* **Core Architecture Guide:** [Closed-Loop System & Event Propagation](../../../core-features/closed-loop-system.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `mode` | `string` | Yes | — | `ask`, `allow`, `deny` | Global notification permission default to set. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.notifications_permission_default_set",
  "arguments": {
    "mode": "deny",
    "_meta": {
      "intent": "Suppress all notification popups during automated crawling"
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
      "text": "Notification default set to deny."
    }
  ],
  "structuredContent": {
    "status": "ok",
    "globalDefault": "deny"
  }
}
```

---

## 4. Operational Best Practices

* **Headless / Bot Automation:** Setting `mode: "deny"` during crawling runs ensures rogue website notification permission prompts never interrupt or freeze the automation flow.

---

## See Also

* [`nova.notifications_permission_set`](nova-notifications-permission-set.md) - Set per-origin permission.
* [`nova.notifications_permissions_list`](nova-notifications-permissions-list.md) - List permissions.
* [Desktop Notifications Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
