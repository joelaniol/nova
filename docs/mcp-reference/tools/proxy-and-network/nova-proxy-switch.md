# `nova.proxy_switch`

Dynamically switches the active proxy for global tabs or a specific sandbox without restarting Nova.

---

## 1. Overview

`nova.proxy_switch` changes the global default proxy, or stores a sandbox's own proxy choice (`global`, `none`, or a specific profile). For a global switch, Nova recreates the open tab WebViews so the new proxy applies right away. A sandbox-scoped switch restarts that sandbox's WebView, but WebView2 does not currently give one profile its own outbound proxy — every surface still carries the single global proxy regardless of a sandbox's stored choice.

* **Core Architecture Guide:** [Proxy Routing](../../../core-features/network/proxy/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string or null` | No | — | — | Proxy profile ID to activate. Use null to disable proxy (direct connection). |
| `sandboxId` | `string` | No | — | — | Sandbox ID to switch proxy for. Omit for global default switch. |
| `mode` | `string` | No | — | `global`, `none`, `profile` | Sandbox proxy scope: 'global' follows the global default, 'none' requests a direct connection, 'profile' uses profileId. Requires sandboxId. Omit for the legacy behaviour where profileId alone decides between 'profile' and 'none'. |

Capability bundle: `proxy_management` (load it with `nova.tools_bundle(bundle='proxy_management')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.proxy_switch",
  "arguments": {
    "sandboxId": "B",
    "profileId": "proxy-2"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Sandbox 'B' proxy switched to profile 'proxy-2'."
    }
  ],
  "structuredContent": {
    "success": true,
    "scope": "sandbox",
    "sandboxId": "B",
    "profileId": "proxy-2",
    "mode": "profile"
  }
}
```
A request without `sandboxId` switches the global default instead and returns `{"success": true, "scope": "global", "profileId": ...}`. Because WebView2 currently gives no profile its own outbound proxy, the sandbox's `mode`/`profileId` choice is stored but every surface still carries the one global proxy — see the [proxy routing guide](../../../core-features/network/proxy/README.md) for the current limitation.

---

## 4. Operational Best Practices

* **Per-sandbox proxies are not routed independently today:** browser tabs and every sandbox share one browser process, so the global proxy applies to all of them. Setting one sandbox's `mode` to `profile` records that choice, but the sandbox is switched back to the global proxy the next time Nova starts.

---

## See Also

* [`nova.proxy_status`](nova-proxy-status.md) - Check proxy health.
* [`nova.proxy_disconnect`](nova-proxy-disconnect.md) - Temporarily disconnect.
* [Proxy Routing Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
