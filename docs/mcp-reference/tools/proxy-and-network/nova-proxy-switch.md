# `nova.proxy_switch`

Dynamically switches the active proxy for global tabs or a specific sandbox without restarting Nova.

---

## 1. Overview

`nova.proxy_switch` reconfigures routing for a target sandbox or global tabs. Nova seamlessly recreates affected WebView2 instances so new proxy startup arguments take effect immediately.

* **Capability Bundle:** `proxy_management`
* **Security Tier:** Tier 2 (Routing Control)
* **Core Architecture Guide:** [Proxy Routing & Stealth Network Engine](../../../core-features/proxy-and-network.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`profileId`** | `string` | No | `null` | Profile ID to activate. Pass `null` to disable proxy. |
| **`sandboxId`** | `string` | No | `global` | Sandbox ID (e.g. `"A"`, `"B"`) to switch. |
| **`mode`** | `string` | No | `derived` | Scope mode: `"global"`, `"none"`, or `"profile"`. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.proxy_switch",
  "arguments": {
    "sandboxId": "B",
    "profileId": "prx-us-east"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Sandbox B proxy switched to 'prx-us-east'."
    }
  ],
  "structuredContent": {
    "ok": true,
    "sandboxId": "B",
    "profileId": "prx-us-east",
    "recreated": true
  }
}
```

---

## 4. Operational Best Practices

* **Sandbox Isolation:** Assigning Sandbox B to a US proxy while keeping Sandbox A direct allows concurrent multi-regional testing side-by-side.

---

## See Also

* [`nova.proxy_status`](nova-proxy-status.md) - Check proxy health.
* [`nova.proxy_disconnect`](nova-proxy-disconnect.md) - Temporarily disconnect.
* [Proxy Routing Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
