# `nova.external_server_stop`

Stops a running external MCP server gracefully with force-kill fallback.

---

## 1. Overview

`nova.external_server_stop` shuts down an active server. For `stdio`, it closes stdin, waits 5 seconds for a graceful exit, then terminates the process. It refuses to stop if other agents have active calls unless `force: true` is set.

* **Capability Bundle:** `external_mcp`
* **Security Tier:** Tier 2 (Server Lifecycle)
* **Core Architecture Guide:** [Plugins & External Extensions](../../../core-features/plugins.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`serverKey`** | `string` | Yes | `none` | 8-character hex server key. |
| **`force`** | `boolean` | No | `false` | If `true`, interrupts in-flight tool calls from other agents. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

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
