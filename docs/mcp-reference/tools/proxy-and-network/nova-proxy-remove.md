# `nova.proxy_remove`

Deletes a proxy profile and resets any sandbox bindings back to the global default.

---

## 1. Overview

`nova.proxy_remove` deletes a proxy profile and removes its encrypted credentials. Any sandboxes assigned to the deleted profile are automatically reset to `global`.

* **Core Architecture Guide:** [Proxy Routing & Network Engine](../../../core-features/proxy-and-network.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | ID of the proxy profile to delete. |

Capability bundle: `proxy_management` (load it with `nova.tools_bundle(bundle='proxy_management')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.proxy_remove",
  "arguments": {
    "profileId": "proxy-1"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Proxy profile 'proxy-1' removed."
    }
  ],
  "structuredContent": {
    "success": true,
    "removedProfileId": "proxy-1"
  }
}
```

---

## 4. Operational Best Practices

* **Automatic Fallback:** Sandboxes never fail closed upon profile deletion; they seamlessly fall back to global proxy routing.

---

## See Also

* [`nova.proxy_list`](nova-proxy-list.md) - List profiles.
* [Proxy Routing Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
