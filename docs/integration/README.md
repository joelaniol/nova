# Connect Your AI Program

Your AI program runs the agent; Nova gives it a browser workspace. To get started, follow [Your first five minutes](../getting-started/quickstart.md).

## Two ways to connect

### Let Nova set up the connection

Open **Settings → AI & agents → Connection & setup → Set up**. Choose **Easy setup (recommended)**, continue to **How the connection is saved**, and click **Connect** beside your program if offered. Restart the AI program afterwards.

The wizard shows the programs it found and the files it will update. Opening the wizard or reading its pages does not save a connection. Restart previously open shells and agent sessions, then check Nova in the client's MCP list (`/mcp` where supported).

### Ask your agent to set it up

In the wizard, choose **Set up manually → Let an AI program do it → Copy text for an AI program**. Paste that text into the AI program you want to connect, such as Claude Code, and ask it to carry out the setup. Review any proposed configuration changes, then restart that program.

Use Nova's generated text: it contains the current connection details for your installation. It can include the access key, so do not post it in a public issue or shared document.

## Details for your program

| Program | Guide |
|---|---|
| Claude Code | [Connect Claude Code](claude-code.md) |
| Claude Desktop | [Connect Claude Desktop](claude-desktop.md) |
| OpenAI Codex CLI | [Connect Codex](openai-codex.md) |
| Antigravity | [Connect Antigravity](google-antigravity.md) |

If your program is missing, install it and choose **Search again**. For another MCP-compatible program, use **Connect another program** in the wizard.

## Once connected

Tell your agent what you want to accomplish and ask it to use Nova. The agent handles tool discovery, calls and task results. You do not need to select an output format or prescribe a tool sequence.

Nova keeps its own connection entry current when automatic sync is enabled. Tool approvals in the AI program remain your decision. Page data the agent reads may be sent to its AI provider; see the [privacy notice](../../PRIVACY.md).

After your first task, see [What's next?](../getting-started/whats-next.md) for optional project onboarding and Learn Mode. If the connection fails, start at [Connection troubleshooting](../troubleshooting/agent-connection-issues.md).

## For developers

Building your own agent runner or MCP client? Use [Custom integrations](custom-agents.md) for developer guidance.
