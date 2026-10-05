# Connect Your AI Program

Nova detects supported AI programs on your computer and helps them connect to its browser. Most users can use the connection wizard rather than edit configuration files.

## The normal setup

1. Open Nova's connection wizard: **Settings → AI & agents → Connection & setup → Set up**. It may already be open on first start.
2. Choose **Easy setup (recommended)**. Review the programs Nova found, then continue to **How the connection is saved**.
3. Click **Connect** beside your program if offered. Already managed entries need no new connection.
4. Restart your AI program or start a new CLI session. Then ask: **“Use Nova to find cat pictures and give me three source links.”**

For the complete first task, follow [Quickstart](../getting-started/quickstart.md).

## Choose your client

Each supported client has one setup guide. Use it for manual configuration and client-specific details.

| Your AI program | Guide |
|---|---|
| Claude Code | [Claude Code](claude-code.md) |
| Claude Desktop | [Claude Desktop](claude-desktop.md) |
| OpenAI Codex CLI | [Codex](openai-codex.md) |
| Google Antigravity / Gemini CLI | [Antigravity and Gemini](google-antigravity.md) |
| Your own Python, Node.js or other MCP client | [Custom agents](custom-agents.md) |

If a program is missing, install it and choose **Search again**. For another compatible program, the wizard's **Connect another program** step offers setup text and manual connection details.

## What the connection does

Supported clients start Nova's bridge, `NovaBrowser.McpProxy.exe`. The bridge finds Nova's local MCP server and adds its access token. Nova keeps its own client entry current when automatic sync is enabled; other entries are preserved. The token is not written into those client config entries.

Nova listens on this computer by default. Access from other devices requires a separate setting. Page data your agent reads may be sent to its AI provider under that provider's terms; see the [privacy notice](../../PRIVACY.md).

## Beyond the first task

- [Advanced onboarding and bootstrap](../getting-started/advanced-onboarding.md) — optional project references and agent discovery.
- [Protocol and transport](../mcp-reference/protocol-and-transport.md) — custom integrations.
- [Troubleshooting](../troubleshooting/README.md) — missing connections, agent behavior and client-specific quirks.
