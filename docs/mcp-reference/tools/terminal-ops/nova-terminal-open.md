# `nova.terminal_open`

Opens a new agent-owned PowerShell session in an isolated working directory and returns its unique sessionId.

---

## 1. Overview

`nova.terminal_open` launches a headless Windows Pseudo Console (ConPTY) session hosted by `NovaBrowser.TerminalRunner`. The session operates in an isolated environment, separate from the user's interactive terminal dock, and persists across browser UI reloads.

* **Security Tier:** Tier 2 (Execute)
* **Architecture Guide:** [Terminal Workspaces & ConPTY Integration](../../../core-features/terminal-workspaces.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `shell` | `string` | No | — | — | Reserved for future shells; currently every session is PowerShell. |
| `cwd` | `string` | No | — | — | Working directory. Optional — defaults to an isolated per-session temp dir. If given, must be inside an allowed root (terminal workspace, runtime temp, or install dir); otherwise cwd_not_allowed. |
| `cols` | `integer` | No | — | 80–500 | Initial width in columns. Default 120; values below 80 are raised to 80 so run_command's completion marker never wraps. |
| `rows` | `integer` | No | — | 24–200 | Initial height in rows. Default 30; values below 24 are raised to 24 for a stable renderer. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `terminal_ops` (load it with `nova.tools_bundle(bundle='terminal_ops')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.terminal_open",
  "arguments": {
    "cols": 120,
    "rows": 30,
    "_meta": {
      "intent": "Compile and run integration smoke tests"
    }
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Terminal session 'term-a8f9c1d0' opened (powershell.exe)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "sessionId": "term-a8f9c1d0",
    "shell": "powershell.exe",
    "cwd": "C:\\Users\\GNetwork\\AppData\\Local\\Temp\\NovaBrowser\\term-a8f9c1d0",
    "cols": 120,
    "rows": 30
  }
}
```

---

## 4. Operational Best Practices

* **Geometry Guarding:** Always preserve at least 80 columns. Narrower viewports cause CLI tools and sentinels to wrap lines, corrupting regex parsers.
* **Session Cleanup:** Always pair `nova.terminal_open` with `nova.terminal_close` in a `finally` block to kill child processes and reclaim OS memory.
* **Command Execution:** For running one-shot commands, prefer `nova.terminal_run_command` over raw writes.

---

## See Also

* [`nova.terminal_run_command`](nova-terminal-run-command.md) - Run a command and wait for completion.
* [`nova.terminal_read`](nova-terminal-read.md) - Read scrollback output.
* [`nova.terminal_close`](nova-terminal-close.md) - Terminate session and process tree.
* [`Core Architecture: Terminal Workspaces`](../../../core-features/terminal-workspaces.md) - ConPTY runner architecture.
* [Headless Terminal Workspaces Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
