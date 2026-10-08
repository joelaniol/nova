# External Model Context Protocol (MCP) Servers

Nova can also register other MCP servers and call their tools (bundle `external_mcp`):

* `nova.external_server_add`, `nova.external_server_update`, `nova.external_server_remove`, `nova.external_server_import`: Register servers with `stdio`, `http` (Streamable HTTP) or `sse` transport, or import definitions from Claude Desktop, VS Code, Claude Code or JSON config files.
* `nova.external_server_start`, `nova.external_server_stop`, `nova.external_server_logs`: Start a stdio server (Nova runs the process), stop it, read its recent error output.
* `nova.external_servers`, `nova.external_tools`: List registered servers and the tools a server offers.
* `nova.external_tool_call`: Call a tool on an external server.

[Connectors overview](../README.md) · [All core features](../../README.md)
