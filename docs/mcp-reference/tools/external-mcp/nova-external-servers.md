# `nova.external_servers`

Lists all configured external MCP servers with runtime status, health, and tool count.

---

## 1. Overview

`nova.external_servers` returns an inventory of all secondary MCP servers registered in Nova. It reports transport types (`stdio`, `http`, `sse`), connection states, health indicators, last error messages, and registered tool counts.

* **Capability Bundle:** `external_mcp`
* **Security Tier:** Tier 1 (Safe)
* **Core Architecture Guide:** [Plugins & External Extensions](../../../core-features/plugins.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.external_servers",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "1 external MCP server(s) configured."
    }
  ],
  "structuredContent": {
    "ok": true,
    "serverCount": 1,
    "servers": [
      {
        "serverKey": "a1b2c3d4",
        "displayName": "Postgres Gateway",
        "transport": "stdio",
        "status": "Connected",
        "running": true,
        "healthy": true,
        "toolCount": 5,
        "endpoint": null,
        "command": "npx",
        "arguments": "-y @modelcontextprotocol/server-postgres postgresql://localhost/mydb",
        "lastError": null,
        "autoStart": true,
        "autoConnect": false,
        "restartOnCrash": true,
        "enabled": true
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Server Key Reference:** Use the returned 8-character `serverKey` in subsequent calls to `start`, `stop`, `external_tools`, or `external_tool_call`.

---

## See Also

* [`nova.external_server_start`](nova-external-server-start.md) - Start server.
* [`nova.external_tools`](nova-external-tools.md) - Discover external tools.
* [External MCP Servers Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
