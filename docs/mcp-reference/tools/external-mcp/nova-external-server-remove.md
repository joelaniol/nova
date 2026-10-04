# `nova.external_server_remove`

Deletes an external MCP server registration, stopping it if running.

---

## 1. Overview

`nova.external_server_remove` unregisters a server from Nova. If the server is currently running, it is stopped before removal.

* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md) (section 7, "External MCP Servers")

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `serverKey` | `string` | Yes | — | — | Stable server identity (8-char hex). Get from nova.external_servers(). |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `external_mcp` (load it with `nova.tools_bundle(bundle='external_mcp')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.external_server_remove",
  "arguments": {
    "serverKey": "e4f5a6b7",
    "_meta": {
      "intent": "Decommission temporary filesystem MCP server"
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
      "text": "Server 'e4f5a6b7' removed."
    }
  ],
  "structuredContent": {
    "ok": true,
    "serverKey": "e4f5a6b7",
    "removed": true
  }
}
```

---

## 4. Operational Best Practices

* **Graceful Stop:** Nova attempts a graceful stdio shutdown before purging configuration records.

---

## See Also

* [`nova.external_server_stop`](nova-external-server-stop.md) - Stop server without removing.
* [External MCP Servers Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
