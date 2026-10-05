# MCP Proxy — Agent Connection Bridge

**Executable:** `NovaBrowser.McpProxy.exe`, installed under `tools/`.

An agent client can start this helper as its MCP server over standard input and output. The helper forwards protocol messages to Nova's local MCP endpoint and returns the responses. It can locate or start Nova when the connection needs it, and provides client-specific naming or response adaptations where configured.

## When It Runs

The agent client owns the standard-input/output connection. Different client sessions can start their own proxy processes, so multiple instances do not necessarily indicate a duplicate installation. A direct client connection to Nova does not require this bridge.

## Why It Is Separate

The client's process-launch contract differs from a running desktop app's local server. The bridge lets Nova remain the desktop application while the client has a transport process it can start and communicate with.

This is an **MCP transport proxy**, not the HTTP or SOCKS proxy used for browser traffic. Ending it interrupts that client connection; it is not a general network disconnect or Nova emergency stop.

## Learn More

* [Agent integration](../integration/README.md)
* [Protocol and transport](../mcp-reference/protocol-and-transport.md)
* [Agent-native affordances](../core-features/agent-native-affordances.md)
* [All components](README.md)
