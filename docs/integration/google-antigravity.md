# Connect Antigravity to Nova

Connect Antigravity through Nova's wizard, restart it, and give it your first task. The wizard lists this connection as **Antigravity**.

## Antigravity

Follow [Your first five minutes](../getting-started/quickstart.md), choosing **Antigravity** in Nova's program list. Click **Connect** if offered, then restart Antigravity and try the first task.

Nova supplies the Antigravity-specific connection entry, including the compatibility settings needed by its bridge. You do not need to tune output sizes or configure result processing.

For manual setup, choose **Set up manually** in Nova's wizard. You can give Antigravity the generated setup text, or use **Copy entry for Google Antigravity** if you manage the file yourself. Restart Antigravity afterwards.

If tools are missing or the agent cannot read their data, use [Antigravity compatibility troubleshooting](../troubleshooting/antigravity.md).

## Which file changes, and what should it look like?

The current configuration is **`%USERPROFILE%\.gemini\config\mcp_config.json`**. Press **Win+R**, enter `%USERPROFILE%\.gemini\config`, and open `mcp_config.json` in a text editor such as Notepad. Look for `mcpServers.nova`.

Nova also updates these older files **if they already exist**:

- `%USERPROFILE%\.gemini\antigravity-cli\mcp_config.json`
- `%USERPROFILE%\.gemini\antigravity-cli\mcp.json`

If only the legacy configuration exists and the new `config` folder does not, Nova updates the existing legacy file(s). It does not create legacy files for a new installation. Use the configuration path reported by the wizard to inspect your installation.

Before changing an existing configuration, Nova creates or retains a backup beside it with the suffix `.nova.bak` (for example, `mcp_config.json.nova.bak`). This is a backup, not the file your client loads.

The entry Nova generates looks like this:

```json
{
  "mcpServers": {
    "nova": {
      "command": "C:\\Users\\YourName\\AppData\\Local\\nova-cognitive\\Nova\\bin\\NovaBrowser.McpProxy.exe",
      "args": ["--antigravity-tool-names"]
    }
  }
}
```

`YourName` is an example username. Use the actual path supplied by Nova's wizard. Older installations may use `AppData\Local\NovaBrowser\bin`. In JSON, `\\` represents one Windows path backslash. This example shows only the Nova connection; keep other settings and servers. The bridge manages Nova's local authentication, so this standard entry contains no access token.

## Why Antigravity needs compatibility mode

Antigravity needs two adaptations: compatible tool names and readable copies of structured results. In Nova's current bridge, **`--antigravity-tool-names` enables both**:

| Adaptation | What you can recognize |
|---|---|
| Names with underscores instead of dots | Nova's reference uses `nova.tabs`; Antigravity discovers `nova_tabs`. The bridge translates calls back to Nova. |
| Structured data also supplied as text | The agent receives a text copy of `structuredContent`, rather than only a summary referring to data it cannot see. |

You do not need to add `--mirror-structured-content` separately for Antigravity. It is the standalone option for other clients that lose structured results but accept dotted names; see the [custom-client examples and compatibility table](custom-agents.md#client-compatibility).

For a manually managed entry, explicitly listing both switches is also accepted:

```json
{
  "args": ["--antigravity-tool-names", "--mirror-structured-content"]
}
```

This last example shows the arguments property inside the `nova` entry, not a complete connection file. The second switch is redundant in the current Antigravity mode; the full example above matches Nova's generated configuration. These are connection compatibility options, not controls for how the agent plans or presents its work.

Restart Antigravity, including previously running CLI sessions or shells, after changing the entry. Check its MCP/tool list; where `/mcp` is available, use it. A saved entry alone does not prove the running session loaded it.

## Coming from Gemini CLI?

For individual accounts, Google's terminal offering is now Antigravity CLI. Gemini CLI stopped serving free individual accounts and Google AI Pro/Ultra on **June 18, 2026**. Enterprise and API-key access remain exceptions; see [Google's transition notice](https://github.com/google-gemini/gemini-cli/discussions/28017).

For the normal Nova setup, use Antigravity and the connection steps above. For migration, follow [Google's Antigravity CLI guide](https://antigravity.google/blog/introducing-google-antigravity-cli).

## After connecting

Optional [project onboarding and Learn Mode](../getting-started/whats-next.md#use-nova-with-agents-regularly) are available after your first successful task. For connection failures, use [Connection troubleshooting](../troubleshooting/agent-connection-issues.md).
