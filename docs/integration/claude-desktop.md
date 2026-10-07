# Connect Claude Desktop to Nova

For Claude Desktop, use Nova's connection wizard. You do not need to edit a configuration file for the normal setup.

## Connect and restart

1. Follow [Your first five minutes](../getting-started/quickstart.md), choosing **Claude Desktop** in Nova's program list.
2. Click **Connect** if offered.
3. Quit Claude Desktop completely, including its system tray icon, then reopen it.
4. Try the [first research task](../getting-started/quickstart.md#4-give-it-a-task-and-watch).

Your conversation stays in Claude Desktop. Nova is where you see the browser work. Claude Desktop handles tool use and presents the task results; there is no extra Nova output mode to configure.

## Which file changes, and what should it look like?

Nova adds or updates `mcpServers.nova` in **`%APPDATA%\Claude\claude_desktop_config.json`**. Press **Win+R**, enter `%APPDATA%\Claude`, and open `claude_desktop_config.json` in a text editor such as Notepad.

For a Microsoft Store/MSIX installation, an existing configuration may be under `%LOCALAPPDATA%\Packages\<Claude package>\LocalCache\Roaming\Claude\claude_desktop_config.json` instead. Use the configuration path reported by Nova's wizard if it differs from the standard location.

Before changing an existing configuration, Nova creates or retains a backup beside it with the suffix `.nova.bak` (for example, `claude_desktop_config.json.nova.bak`). This is a backup, not the file your client loads.

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

`YourName` is an example username. Use the actual path supplied by Nova's wizard. Older installations may use `AppData\Local\NovaBrowser\bin`. In JSON, `\\` represents one Windows path backslash.

This example shows only the Nova connection. Preserve other settings and servers; Nova preserves them when updating its entry. The bridge handles Nova's local authentication, so this standard entry contains no access token.

Quit Claude Desktop completely, including its tray icon, and reopen it before checking its Nova tools. Saving this file does not reconnect a session that is already running.

## Manual connection

If you manage Claude Desktop's connection yourself, choose **Set up manually → Enter it yourself → Copy entry** in Nova's wizard. It provides the current connection entry, and lists the configuration files it found.

Add that entry to Claude Desktop's MCP configuration alongside any existing servers. Preserve those other entries and the rest of the file. If editing JSON by hand, Windows path backslashes must be escaped. Quit and restart Claude Desktop afterwards.

The [connection guide](README.md) also explains how to give the setup text to an AI program that can edit the required file.

## If Nova is missing

First check whether Claude Desktop was still running in the tray. Then reopen Nova's wizard and read its connection status. For further checks, use [Connection troubleshooting](../troubleshooting/agent-connection-issues.md#2-claude-desktop-shows-no-nova-tools).
