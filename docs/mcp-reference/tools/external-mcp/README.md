# External MCP Servers & Tool Bridging

Registering, running, and dynamically calling secondary MCP servers through Nova's unified host.

* **Core Architecture Guide:** [Core Features: plugins.md](../../../core-features/plugins/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

<!-- generated:tool-list (from the tool pages in this folder; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
## Tool Inventory (10 Tools)

Capability bundles of these tools: `external_mcp`.

| Tool | What it does |
| :--- | :--- |
| **[`nova.external_server_add`](nova-external-server-add.md)** | Registers a new external MCP server with stdio, HTTP, or SSE transport. |
| **[`nova.external_server_import`](nova-external-server-import.md)** | Imports MCP server definitions from Claude Desktop, VS Code, Claude Code, or JSON config files. |
| **[`nova.external_server_logs`](nova-external-server-logs.md)** | Reads recent stderr log lines captured from an external MCP server process. |
| **[`nova.external_server_remove`](nova-external-server-remove.md)** | Deletes an external MCP server registration, stopping it if running. |
| **[`nova.external_server_start`](nova-external-server-start.md)** | Launches an external MCP server, runs initialize handshake, and discovers available tools. |
| **[`nova.external_server_stop`](nova-external-server-stop.md)** | Stops a running external MCP server gracefully with force-kill fallback. |
| **[`nova.external_server_update`](nova-external-server-update.md)** | Updates configuration, environment variables, or transport settings of an existing server. |
| **[`nova.external_servers`](nova-external-servers.md)** | Lists all configured external MCP servers with runtime status, health, and tool count. |
| **[`nova.external_tool_call`](nova-external-tool-call.md)** | Invokes a specific tool on a connected external MCP server and returns the raw response. |
| **[`nova.external_tools`](nova-external-tools.md)** | Lists all tools available on an external MCP server, with optional full inputSchema. |
<!-- /generated:tool-list -->

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
