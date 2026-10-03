# `nova.network_intercept_clear`

Disarms network interception rules: by rule ID, by tab ID, or globally across the entire browser.

---

## 1. Overview

`nova.network_intercept_clear` removes active network interception rules. Called with no arguments, it acts as an emergency stop disarming every interception rule across all tabs.

* **Capability Bundle:** `proxy_management`
* **Security Tier:** Tier 2 (Control)
* **Core Architecture Guide:** [Proxy Routing & Stealth Network Engine](../../../core-features/proxy-and-network.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`ruleId`** | `string` | No | `null` | Specific rule ID to disarm. |
| **`targetId`** | `string` | No | `null` | Clear all rules assigned to this tab. |
| **`agentId`** | `string` | No | `"default"` | Optional agent identifier. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.network_intercept_clear",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "All network interception rules disarmed (2 rule(s) cleared)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "clearedCount": 2,
    "scope": "global"
  }
}
```

---

## 4. Operational Best Practices

* **Emergency Stop:** Run `nova.network_intercept_clear()` without arguments if automated tests fail unexpectedly to restore normal network traffic.

---

## See Also

* [`nova.network_intercept_add`](nova-network-intercept-add.md) - Add interception rule.
* [`nova.network_intercept_list`](nova-network-intercept-list.md) - List active rules.
* [Proxy Routing Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
