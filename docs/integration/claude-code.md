# Connect Claude Code to Nova

Use Nova's connection wizard or give Claude Code Nova's generated setup text. After connecting, ask Claude Code for a task and let it handle Nova's tools and results.

## Connect through Nova

Follow [Your first five minutes](../getting-started/quickstart.md), choosing **Claude Code** in the program list. Click **Connect** if offered, then close the existing Claude Code session and start a new one.

If Claude Code is not listed, install it or make its installation available to Nova, then choose **Search again**.

## Which file changes, and what should it look like?

Nova's automatic setup adds or updates `mcpServers.nova` in **`%USERPROFILE%\.claude.json`**. Press **Win+R**, enter `%USERPROFILE%`, and open `.claude.json` in a text editor such as Notepad. Search for `"nova"` under `"mcpServers"`.

Before changing an existing configuration, Nova creates or retains a backup beside it with the suffix `.nova.bak` (for example, `.claude.json.nova.bak`). This is a backup, not the file your client loads.

A standard Nova connection looks like this:

```json
{
  "mcpServers": {
    "nova": {
      "command": "C:\\Users\\YourName\\AppData\\Local\\nova-cognitive\\Nova\\bin\\NovaBrowser.McpProxy.exe"
    }
  }
}
```

`YourName` is an example username. Use the actual path supplied by Nova's wizard. Older installations may use `AppData\Local\NovaBrowser\bin` instead. In JSON, `\\` represents one Windows path backslash.

This example shows only the Nova connection. Keep other server entries and settings; Nova preserves them when updating its entry. The bridge handles Nova's local authentication, so this standard entry contains no access token.

Connection setup does not write Claude Code's permission files, such as `.claude/settings.json` or `settings.local.json`. Permissions are a separate decision in Claude Code. A project `.mcp.json` is a manually managed alternative; Nova does not create it automatically. `%USERPROFILE%\.claude\.mcp.json` is a legacy location Nova can inspect, rather than its current automatic write target.

Close previously running Claude Code sessions or shells and start a new session, then use `/mcp` to check the loaded connection. A matching file entry alone does not show that an already running session has loaded it.

## Have Claude Code configure the connection

Open Nova's wizard and choose **Set up manually → Let an AI program do it → Copy text for an AI program**. Paste the generated text into Claude Code and ask it to set up Nova for this Claude Code installation.

The text tells the agent which connection to add and supplies your current Nova details. Review the proposed changes, then start a new Claude Code session. See [the connection guide](README.md#ask-your-agent-to-set-it-up) for handling the setup text.

## Try a task

Use the [first research task](../getting-started/quickstart.md#4-give-it-a-task-and-watch), or describe your own goal. Your conversation and final answer stay in Claude Code; the browser work happens in Nova.

For recurring project work, optional [project onboarding](../getting-started/whats-next.md#recommended-optional-project-onboarding) helps later sessions find Nova's instructions.

## If it does not connect

Reopen the wizard and read the Claude Code row. It distinguishes a missing registration, an outdated entry, disabled automatic setup, a missing runner, and an unreadable configuration.

Use [Connection troubleshooting](../troubleshooting/agent-connection-issues.md). For a manually managed entry, use the current details supplied by Nova instead of copying a path from another machine.
