# How the Connection Works

Nova's connection wizard handles setup for supported AI programs. You do not need to configure MCP manually for your first task: follow [Your first five minutes](quickstart.md).

## Why restart the AI program?

Your AI program reads its connection settings when it starts. A session that was already open when you clicked **Connect** keeps its old settings. Close and reopen the program, or start a new CLI session. For Claude Desktop, also quit its tray icon.

## Starting and reconnecting to Nova

Once connected, supported clients can start Nova when needed and reconnect automatically. Their Nova entry starts a bridge, `NovaBrowser.McpProxy.exe`, which locates Nova and supplies its current access token. You do not need to copy a token into client configuration.

Nova keeps its own connection entry current when automatic sync is enabled. Other connection entries are preserved. Your AI program's tool approvals remain your decision; connecting Nova does not create a permission allowlist.

## What is MCP?

MCP is the protocol your AI program uses to ask Nova for browser tools and read their results. Your conversation stays in the AI program. Page data the agent reads may be sent to its AI provider under that provider's terms; see the [privacy notice](../../PRIVACY.md).

## Connection problems or custom setup

- [Connection diagnostics](../troubleshooting/agent-connection-issues.md) — missing tools, server health and bridge logs.
- [Client-specific guides](../integration/README.md) — manual setup and compatibility details.
- [Protocol and transport](../mcp-reference/protocol-and-transport.md) — custom integrations.
