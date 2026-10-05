# TerminalRunner — Persistent Console Host

**Executable:** `NovaBrowser.TerminalRunner.exe`.

TerminalRunner hosts Windows pseudo consoles (ConPTY) and the programs attached to them. Nova's terminal dock displays a console through xterm.js; agent-owned terminal sessions have a separate registry. Shells and their child programs run alongside the helper, not inside the browser's UI process.

## When It Runs

The helper is started when terminal work needs it. It can remain after Nova closes or crashes, preserving hosted processes for reconnection. With no attached Nova and no sessions it exits after a grace period. With sessions but no attached Nova for a whole day, it ends those orphaned sessions.

## Why It Is Separate

Restarting the browser should not automatically kill a development server or long-running shell command. TerminalRunner separates console lifetime from window lifetime. That is different from Outrider, whose native work is supervised and disposable.

Closing TerminalRunner ends its sessions. A terminal command timeout, by contrast, can simply end the waiting tool call while the command keeps running. Inspect the session before resubmitting work.

The starting-directory rules do not make a terminal an operating-system sandbox. Its programs run with the user's Windows permissions.

## Learn More

* [Terminal workspaces](../core-features/terminal-workspaces.md)
* [Scheduled tasks](../core-features/scheduled-tasks.md) — Uses workspaces, but has its own execution lifecycle.
* [All components](README.md)
