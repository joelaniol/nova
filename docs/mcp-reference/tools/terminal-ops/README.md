# Headless Terminal Workspaces & TTY

Isolated pseudo-terminals (ConPTY), command execution streams, terminal dock control, and session persistence.

* **Capability Bundle(s):** `terminal_ops`
* **Core Architecture Guide:** [Core Features: terminal-workspaces.md](../../../core-features/terminal-workspaces.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (12 Tools)

| Tool | What it does |
| :--- | :--- |
| **[`nova.terminal_close`](nova-terminal-close.md)** | Terminates an agent-owned terminal session and cleans up its process tree and temporary directory. |
| **[`nova.terminal_dock_get_state`](nova-terminal-dock-get-state.md)** | Reads the presentation state of the visible terminal dock in the Nova application shell. |
| **[`nova.terminal_dock_set_state`](nova-terminal-dock-set-state.md)** | Sets the visual presentation of the Nova terminal dock to expanded, collapsed, or hidden. |
| **[`nova.terminal_get_state`](nova-terminal-get-state.md)** | Queries lifecycle status, working directory, and exit code for a specific session. |
| **[`nova.terminal_list`](nova-terminal-list.md)** | Lists all open agent-owned terminal sessions with status, shell type, and exit codes. |
| **[`nova.terminal_open`](nova-terminal-open.md)** | Opens a new agent-owned PowerShell session in an isolated working directory and returns its unique sessionId. |
| **[`nova.terminal_read`](nova-terminal-read.md)** | Reads the recent raw output tail of a terminal session scrollback buffer. |
| **[`nova.terminal_run_command`](nova-terminal-run-command.md)** | Executes a single command line in an existing session and waits synchronously for its completion. |
| **[`nova.terminal_send_key`](nova-terminal-send-key.md)** | Sends a named control key or key combination to the active terminal session. |
| **[`nova.terminal_settings_get`](nova-terminal-settings-get.md)** | Reads terminal appearance settings and reports why ANSI colour output is enabled or disabled. |
| **[`nova.terminal_settings_set`](nova-terminal-settings-set.md)** | Updates terminal appearance settings such as color theme, font size, and program color rules. |
| **[`nova.terminal_write`](nova-terminal-write.md)** | Writes raw characters to the session stdin without appending an implicit newline. |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
