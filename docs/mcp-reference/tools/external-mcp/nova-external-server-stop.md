# `nova.external_server_stop`

Stops a running external MCP server gracefully with force-kill fallback.

---

## 1. Overview

`nova.external_server_stop` shuts down an active server. For `stdio`, it closes stdin, waits 5 seconds for a graceful exit, then terminates the process. It refuses to stop if other agents have active calls unless `force: true` is set.

* **Security Tier:** Tier 2 (Server Lifecycle)
* **Core Architecture Guide:** [Plugins & External Extensions](../../../core-features/plugins.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `serverKey` | `string` | Yes | — | — | Stable server identity (8-char hex). Get from nova.external_servers(). |
| `force` | `boolean` | No | — | — | If true, interrupt in-flight tool calls from other agents. Default: false (refuse if active calls exist). |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `external_mcp` (load it with `nova.tools_bundle(bundle='external_mcp')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.external_server_stop",
  "arguments": {
    "serverKey": "a1b2c3d4",
    "force": false
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Server 'a1b2c3d4' stopped."
    }
  ],
  "structuredContent": {
    "ok": true,
    "serverKey": "a1b2c3d4",
    "stopped": true
  }
}
```

---

## 4. Operational Best Practices

* **Multi-Agent Coordination:** Without `force: true`, Nova protects peer agents against abrupt process termination while tool calls are in flight.

---

## See Also

* [`nova.external_server_start`](nova-external-server-start.md) - Start server.
* [External MCP Servers Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
