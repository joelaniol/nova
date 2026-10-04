# `nova.external_servers`

Lists all configured external MCP servers with runtime status, health, and tool count.

---

## 1. Overview

`nova.external_servers` returns an inventory of all secondary MCP servers registered in Nova. It reports transport types (`stdio`, `http`, `sse`), connection states, health indicators, last error messages, and registered tool counts.

* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md) (section 7, "External MCP Servers")

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `external_mcp` (load it with `nova.tools_bundle(bundle='external_mcp')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
