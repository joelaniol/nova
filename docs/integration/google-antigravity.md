# Connect Antigravity or Gemini CLI

Antigravity and Gemini CLI are separate programs. Nova's automatic connection wizard has an **Antigravity** entry; that entry does not configure Gemini CLI.

## Antigravity

Follow [Your first five minutes](../getting-started/quickstart.md), choosing **Antigravity** in Nova's program list. Click **Connect** if offered, then restart Antigravity and try the first task.

Nova supplies the Antigravity-specific connection entry, including the compatibility settings needed by its bridge. You do not need to tune output sizes or configure result processing.

For manual setup, choose **Set up manually** in Nova's wizard. You can give Antigravity the generated setup text, or use **Copy entry for Google Antigravity** if you manage the file yourself. Restart Antigravity afterwards.

If tools are missing or the agent cannot read their data, use [Antigravity compatibility troubleshooting](../troubleshooting/antigravity.md).

## Gemini CLI

Use the wizard's **Connect another program** route to obtain Nova's current connection details. Ask Gemini CLI to configure Nova for Gemini CLI using those details, or configure its MCP entry yourself following the [official Gemini CLI MCP guide](https://geminicli.com/docs/tools/mcp-server/).

Gemini CLI has its own configuration. Do not treat Antigravity's configuration file or compatibility entry as Gemini CLI's setup. For a local connection through Nova's bridge, use the runner command supplied by Nova.

Restart Gemini CLI after changing its configuration, then try the [first research task](../getting-started/quickstart.md#4-give-it-a-task-and-watch). The agent handles tool discovery and results.

## After connecting

Optional [project onboarding and Learn Mode](../getting-started/whats-next.md#use-nova-with-agents-regularly) are available after your first successful task. For connection failures, use [Connection troubleshooting](../troubleshooting/agent-connection-issues.md).
