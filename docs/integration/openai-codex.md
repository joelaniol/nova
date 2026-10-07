# Connect Codex CLI to Nova

Connect Codex through Nova's wizard, then start a new Codex session. Codex handles the task, chooses tools and processes their results.

## Connect through Nova

Follow [Your first five minutes](../getting-started/quickstart.md), choosing **Codex** in the program list. Click **Connect** if offered.

Close the existing Codex session and start a new one so it loads the connection. Then try the [first research task](../getting-started/quickstart.md#4-give-it-a-task-and-watch).

## Which file changes, and what should it look like?

Nova's automatic setup adds or updates **`[mcp_servers.nova]`** in **`%USERPROFILE%\.codex\config.toml`**. Press **Win+R**, enter `%USERPROFILE%\.codex`, and open `config.toml` in a text editor such as Notepad.

Before changing an existing configuration, Nova creates or retains a backup beside it with the suffix `.nova.bak` (for example, `config.toml.nova.bak` for Codex). This is a backup, not the file your client loads.

Nova writes a standard entry in this form:

```toml
[mcp_servers.nova]
enabled = true
command = "C:\\Users\\YourName\\AppData\\Local\\nova-cognitive\\Nova\\bin\\NovaBrowser.McpProxy.exe"
```

`YourName` is an example username. Use the actual command path supplied by Nova's wizard. Older installations may use `AppData\Local\NovaBrowser\bin`. In a TOML double-quoted string, `\\` represents one Windows path backslash.

Keep other Codex settings and server sections. Nova updates its connection without replacing the whole file. The standard bridge entry needs no arguments, URL or access token; the bridge handles Nova's local authentication.

This is Nova's automatic write location. If you deliberately use a different Codex configuration location, configure that installation with the generated setup text and verify which file it loads. See [OpenAI's MCP configuration documentation](https://developers.openai.com/codex/mcp/) for Codex's configuration options.

Close previously running Codex sessions or shells and start a new session, then use `/mcp` to check the loaded connection. The entry in the file is only the saved configuration.

## Have Codex configure the connection

In Nova's wizard, choose **Set up manually → Let an AI program do it → Copy text for an AI program**. Paste that text into Codex and ask it to configure Nova for this Codex installation.

Use the generated agent instructions for Codex: its configuration uses TOML, so the JSON entry intended for other clients is not a replacement. Review the changes and start a new Codex session afterwards. See [the connection guide](README.md#ask-your-agent-to-set-it-up) for handling the setup text.

## Regular work

Give Codex a goal and ask it to use Nova. You do not need to pick result sizes, write tool calls, or manage tab claims yourself.

If you want Nova's instructions available in later project sessions, ask for optional [project onboarding](../getting-started/whats-next.md#recommended-optional-project-onboarding). For repeated website tasks, see [Learn Mode](../getting-started/whats-next.md#learn-recurring-website-workflows).

## If it does not connect

Reopen Nova's wizard and read the Codex row. Check that you started a new session after the connection was saved. Continue with [Connection troubleshooting](../troubleshooting/agent-connection-issues.md).
