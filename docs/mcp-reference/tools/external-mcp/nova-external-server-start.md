# `nova.external_server_start`

Launches an external MCP server, runs initialize handshake, and discovers available tools.

---

## 1. Overview

`nova.external_server_start` initiates the server process or network connection, exchanges MCP initialization capabilities, and queries tools/list. Returns PID, duration, and tool count on success.

* **Capability Bundle:** `external_mcp`
* **Security Tier:** Tier 2 (Server Lifecycle)
* **Core Architecture Guide:** [Plugins & External Extensions](../../../core-features/plugins.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `serverKey` | `string` | Yes | — | — | Stable server identity (8-char hex). Get from nova.external_servers(). |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.external_server_start",
  "arguments": {
    "serverKey": "a1b2c3d4"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Server 'a1b2c3d4' started (pid=14820, 5 tool(s), 420ms)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "serverKey": "a1b2c3d4",
    "processId": 14820,
    "toolCount": 5,
    "durationMs": 420,
    "status": "Connected"
  }
}
```

---

## 4. Operational Best Practices

* **Pre-check Tool Inventory:** On start, Nova automatically populates its cached tool inventory. Call `nova.external_tools` to inspect schema details.

---

## See Also

* [`nova.external_server_stop`](nova-external-server-stop.md) - Stop server.
* [`nova.external_server_logs`](nova-external-server-logs.md) - View server stderr logs.
* [External MCP Servers Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
