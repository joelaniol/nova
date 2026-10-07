# MCP Proxy — Agent Connection Bridge

**Executable:** `NovaBrowser.McpProxy.exe`, installed under `tools/`.

An agent client can start this helper as its MCP server over standard input and output. The helper forwards protocol messages to Nova's local MCP endpoint and returns the responses. It can locate or start Nova when the connection needs it, and provides client-specific naming or response adaptations where configured.

## When It Runs

The agent client owns the standard-input/output connection. Different client sessions can start their own proxy processes, so multiple instances do not necessarily indicate a duplicate installation. A direct client connection to Nova does not require this bridge.

## Why It Is Separate

The client's process-launch contract differs from a running desktop app's local server. The bridge lets Nova remain the desktop application while the client has a transport process it can start and communicate with.

This is an **MCP transport proxy**, not the HTTP or SOCKS proxy used for browser traffic. Ending it interrupts that client connection; it is not a general network disconnect or Nova emergency stop.

## What the Bridge Can Do

* Accept JSON-RPC over standard input and output, using newline-delimited JSON or `Content-Length` framing.
* Discover Nova's recorded endpoint and authenticate the upstream connection.
* Establish an upstream MCP session and refresh the connection when Nova restarts.
* Start Nova when needed, unless autostart is disabled in the proxy configuration.
* Serve cached tool-discovery information while the upstream connection warms up, then refresh it from Nova.
* Handle client cancellation messages while tool work is in flight.
* Adapt tool names and result presentation for clients with different MCP conventions.

A cached tool list describes capabilities; it does not prove Nova is currently connected or that a listed action will succeed. Calls still need the live application and its normal policy checks.

## Client Compatibility

| Option | Effect |
| :--- | :--- |
| Default | Uses Nova's canonical tool names and result structure. |
| `--antigravity-tool-names` | Projects names into the client's compatible naming convention and maps incoming calls back to canonical names. Also enables structured-content mirroring. |
| `--mirror-structured-content` | Adds a text representation of structured results for clients that expose only text content to the model. |
| `--version` | Prints the proxy version and exits. |

The adaptation switches can be combined. They change this proxy connection's presentation, rather than globally renaming Nova's tool catalog. Mirroring has size limits; it is not a promise that every arbitrarily large result is duplicated in full.

## A Typical Connection

A configured agent client launches the proxy, sends its initialization request and requests tools. The proxy establishes the connection to Nova, starting the application if necessary. When the agent calls a tool, the proxy forwards the request and returns Nova's response in the configured client presentation.

The installed payload contains the proxy under `tools/`; Nova also maintains a profile-side copy used by client registration. The executable path in the client's configuration determines which copy it starts. Multiple proxy instances can belong to different client sessions.

## What a Disconnect Means

Ending the proxy breaks its client's transport. It does not switch off the browser's network connection, replace Nova's emergency stop, or prove an already-dispatched action was rolled back. Inspect Nova's state before repeating an action whose outcome was interrupted.

## Learn More

* [Agent integration](../integration/README.md)
* [Protocol and transport](../mcp-reference/protocol-and-transport.md)
* [Agent-native affordances](../core-features/agent-native-affordances/README.md)
* [All components](README.md)
