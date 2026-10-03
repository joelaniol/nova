# `nova.proxy_switch`

Dynamically switches the active proxy for global tabs or a specific sandbox without restarting Nova.

---

## 1. Overview

`nova.proxy_switch` reconfigures routing for a target sandbox or global tabs. Nova seamlessly recreates affected WebView2 instances so new proxy startup arguments take effect immediately.

* **Security Tier:** Tier 2 (Routing Control)
* **Core Architecture Guide:** [Proxy Routing & Stealth Network Engine](../../../core-features/proxy-and-network.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string or null` | No | — | — | Proxy profile ID to activate. Use null to disable proxy (direct connection). |
| `sandboxId` | `string` | No | — | — | Sandbox ID to switch proxy for. Omit for global default switch. |
| `mode` | `string` | No | — | `global`, `none`, `profile` | Sandbox proxy scope: 'global' follows the global default, 'none' requests a direct connection, 'profile' uses profileId. Requires sandboxId. Omit for the legacy behaviour where profileId alone decides between 'profile' and 'none'. |

Capability bundle: `proxy_management` (load it with `nova.tools_bundle(bundle='proxy_management')`).
<!-- /generated:parameters -->

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
