# `nova.external_server_start`

Launches an external MCP server, runs initialize handshake, and discovers available tools.

---

## 1. Overview

`nova.external_server_start` initiates the server process or network connection, exchanges MCP initialization capabilities, and queries tools/list. Returns PID, duration, and tool count on success.

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
      "text": "Server 'Postgres Gateway' started (PID 14820, 5 tools, 420ms)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "result": {
      "serverKey": "a1b2c3d4",
      "displayName": "Postgres Gateway",
      "status": "Connected",
      "pid": 14820,
      "toolCount": 5,
      "startupDurationMs": 420,
      "serverName": "postgres-mcp",
      "serverVersion": "0.4.1",
      "protocolVersion": "2025-03-26"
    }
  }
}
```

On failure, `ok` is `false`, `result.status` is `"Failed"`, `result.pid` is omitted, and `result` instead carries `errorPhase`, `errorMessage`, an optional `exitCode`/`stderr`, and `suggestions` (a short list of likely fixes).

---

## 4. Operational Best Practices

* **Pre-check Tool Inventory:** On start, Nova automatically populates its cached tool inventory. Call `nova.external_tools` to inspect schema details.

---

## See Also

* [`nova.external_server_stop`](nova-external-server-stop.md) - Stop server.
* [`nova.external_server_logs`](nova-external-server-logs.md) - View server stderr logs.
* [External MCP Servers Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
