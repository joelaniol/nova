# Headless Terminal Workspaces & TTY

Isolated pseudo-terminals (ConPTY), command execution streams, terminal dock control, and session persistence.

* **Capability Bundle(s):** `terminal_ops`
* **Core Architecture Guide:** [Core Features: terminal-workspaces.md](../../../core-features/terminal-workspaces.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (12 Tools)

| Tool Name | Status | Description |
| :--- | :---: | :--- |
| **[`nova.terminal_close`](nova-terminal-close.md)** | Documented | Terminate and remove an agent-owned terminal session (kills the shell tree). |
| **[`nova.terminal_dock_get_state`](nova-terminal-dock-get-state.md)** | Documented | Get the visible Nova Terminal dock state. |
| **[`nova.terminal_dock_set_state`](nova-terminal-dock-set-state.md)** | Documented | Set the visible Nova Terminal dock state to expanded, collapsed, or hidden. |
| **[`nova.terminal_get_state`](nova-terminal-get-state.md)** | Documented | Get a session's state: shell, cwd, running, exitCode (if exited), createdAtUtc. |
| **[`nova.terminal_list`](nova-terminal-list.md)** | Documented | List all open agent-owned terminal sessions (sessionId, shell, running, exitCode, createdAtUtc). |
| **[`nova.terminal_open`](nova-terminal-open.md)** | Documented | Open a new agent-owned PowerShell session in an isolated working directory and return its sessionId. |
| **[`nova.terminal_read`](nova-terminal-read.md)** | Documented | Read the recent raw output of a session (tail of the scrollback). |
| **[`nova.terminal_run_command`](nova-terminal-run-command.md)** | Documented | Run one command in an existing session and wait for it to finish. |
| **[`nova.terminal_send_key`](nova-terminal-send-key.md)** | Documented | Send a named control key to the session: Enter, Tab, Escape, Backspace, Delete, Up/Down/Left/Right, Home, End, Ctrl+C, Ctrl+D, ... |
| **[`nova.terminal_settings_get`](nova-terminal-settings-get.md)** | Documented | Read the terminal's appearance settings: theme, font size, and whether programs may use colour. |
| **[`nova.terminal_settings_set`](nova-terminal-settings-set.md)** | Documented | Change the terminal's appearance settings. |
| **[`nova.terminal_write`](nova-terminal-write.md)** | Documented | Write raw text to the session's stdin (no implicit newline — include \r to submit a line). |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
