# Connect Claude Desktop to Nova

For Claude Desktop, use Nova's connection wizard. You do not need to edit a configuration file for the normal setup.

## Connect and restart

1. Follow [Your first five minutes](../getting-started/quickstart.md), choosing **Claude Desktop** in Nova's program list.
2. Click **Connect** if offered.
3. Quit Claude Desktop completely, including its system tray icon, then reopen it.
4. Try the [first research task](../getting-started/quickstart.md#4-give-it-a-task-and-watch).

Your conversation stays in Claude Desktop. Nova is where you see the browser work. Claude Desktop handles tool use and presents the task results; there is no extra Nova output mode to configure.

## Manual connection

If you manage Claude Desktop's connection yourself, choose **Set up manually → Enter it yourself → Copy entry** in Nova's wizard. It provides the current connection entry, and lists the configuration files it found.

Add that entry to Claude Desktop's MCP configuration alongside any existing servers. Preserve those other entries and the rest of the file. If editing JSON by hand, Windows path backslashes must be escaped. Quit and restart Claude Desktop afterwards.

The [connection guide](README.md) also explains how to give the setup text to an AI program that can edit the required file.

## If Nova is missing

First check whether Claude Desktop was still running in the tray. Then reopen Nova's wizard and read its connection status. For further checks, use [Connection troubleshooting](../troubleshooting/agent-connection-issues.md#2-claude-desktop-shows-no-nova-tools).
