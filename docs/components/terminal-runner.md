# TerminalRunner — Persistent Console Host

**Executable:** `NovaBrowser.TerminalRunner.exe`.

TerminalRunner hosts Windows pseudo consoles (ConPTY) and the programs attached to them. Nova's terminal dock displays a console through xterm.js; agent-owned terminal sessions have a separate registry. Shells and their child programs run alongside the helper, not inside the browser's UI process.

## When It Runs

The helper is started when terminal work needs it. It can remain after Nova closes or crashes, preserving hosted processes for reconnection. With no attached Nova and no sessions it exits after a grace period. With sessions but no attached Nova for a whole day, it ends those orphaned sessions.

## Why It Is Separate

Restarting the browser should not automatically kill a development server or long-running shell command. TerminalRunner separates console lifetime from window lifetime. That is different from Outrider, whose native work is supervised and disposable.

Closing TerminalRunner ends its sessions. A terminal command timeout, by contrast, can simply end the waiting tool call while the command keeps running. Inspect the session before resubmitting work.

The starting-directory rules do not make a terminal an operating-system sandbox. Its programs run with the user's Windows permissions.

## Console Capabilities

| Capability | Purpose |
| :--- | :--- |
| Create a session | Start a program in a Windows pseudo console with a working directory, dimensions and optional environment values. |
| Send input | Forward terminal bytes to the running console program. |
| Stream output | Carry console output back to Nova for display or tool consumption. |
| Resize | Update the pseudo console's dimensions when its view changes. |
| List and attach | Find live runner sessions and attach a Nova connection. |
| Detach and reconnect | Disconnect a view without ending the hosted shell. |
| Terminate | Explicitly end a session, all sessions or the runner. |

TerminalRunner transports console input and output. It does not interpret shell commands as business tasks or decide that a deployment succeeded. Nova's terminal tools add command waiting and result handling above this layer.

## Example: A Development Server Survives a Restart

You start a development server in Nova's terminal dock. TerminalRunner owns the pseudo console and the shell process. If Nova restarts, its display connection goes away while the console can remain alive. A returning Nova can reconnect to the runner and attach to the surviving session.

That continuity depends on the runner and shell still being alive. It does not survive a Windows reboot or termination of TerminalRunner. It also does not promise that an agent's old MCP session identifier or complete command history will be restored; the agent-session registry has a separate lifecycle.

## Output and Reconnection Limits

The runner keeps a bounded in-memory output ring and uses offsets to resume a view. This supports reconnection without making terminal output a permanent archive. Older output can fall outside the retained range. A slow consumer can lose its view attachment while the shell continues producing output.

A silent terminal display therefore does not by itself prove the program stopped. Check the session and connection state. Likewise, a waiting tool call reaching its deadline does not necessarily terminate the command.

## Lifetime and Access

With an attached Nova or live sessions, the runner stays available. With neither, it exits after an approximately ten-second idle grace. With sessions but no attached Nova, a 24-hour orphan grace limits how long abandoned shells remain alive.

Nova uses one runner for a given profile, Windows logon session and integrity level. A second launch for the same identity does not create another independent console host. The pipe connection is authenticated and scoped to that identity. That protects access to the console host; it does not restrict the shell's filesystem or network access. Programs still run with the user's Windows permissions. Ending a session closes its hosted process job, so use the terminal's explicit termination controls when the intention is to stop work.

## Learn More

* [Terminal workspaces](../core-features/terminal-workspaces.md)
* [Scheduled tasks](../core-features/scheduled-tasks.md) — Uses workspaces, but has its own execution lifecycle.
* [All components](README.md)
