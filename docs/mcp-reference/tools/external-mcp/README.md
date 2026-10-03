# External MCP Servers & Tool Bridging

Registering, running, and dynamically calling secondary MCP servers through Nova's unified host.

* **Capability Bundle(s):** `external_mcp`
* **Core Architecture Guide:** [Core Features: plugins.md](../../../core-features/plugins.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (10 Tools)

| Tool Name | Status | Description |
| :--- | :---: | :--- |
| **[`nova.external_server_add`](nova-external-server-add.md)** | Documented | Register a new external MCP server. |
| **[`nova.external_server_import`](nova-external-server-import.md)** | Documented | Import MCP server configurations from Claude Desktop, VS Code, Claude Code, or a JSON file. |
| **[`nova.external_server_logs`](nova-external-server-logs.md)** | Documented | Read recent stderr log lines from an external MCP server process. |
| **[`nova.external_server_remove`](nova-external-server-remove.md)** | Documented | Remove an external MCP server from the configuration. |
| **[`nova.external_server_start`](nova-external-server-start.md)** | Documented | Start an external MCP server. |
| **[`nova.external_server_stop`](nova-external-server-stop.md)** | Documented | Stop a running external MCP server. |
| **[`nova.external_server_update`](nova-external-server-update.md)** | Documented | Update configuration of an existing external MCP server. |
| **[`nova.external_servers`](nova-external-servers.md)** | Documented | List all configured external MCP servers with their current runtime status, health, and tool count. |
| **[`nova.external_tool_call`](nova-external-tool-call.md)** | Documented | Call a tool on an external MCP server. |
| **[`nova.external_tools`](nova-external-tools.md)** | Documented | List all tools available on an external MCP server. |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
