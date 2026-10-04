# `nova.terminal_get_state`

Queries lifecycle status, working directory, and exit code for a specific session.

---

## 1. Overview

`nova.terminal_get_state` inspects whether a terminal session is actively running, its working directory, and its process exit code if it has terminated.

* **Architecture Guide:** [Terminal Workspaces & ConPTY Integration](../../../core-features/terminal-workspaces.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `sessionId` | `string` | Yes | — | — | Session id from terminal_open. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `terminal_ops` (load it with `nova.tools_bundle(bundle='terminal_ops')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.terminal_get_state",
  "arguments": {
    "sessionId": "term_1a2b3c4d5e6f7a8b"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "'term_1a2b3c4d5e6f7a8b': running."
    }
  ],
  "structuredContent": {
    "ok": true,
    "sessionId": "term_1a2b3c4d5e6f7a8b",
    "shell": "powershell.exe -NoProfile -NoLogo -NoExit -Command \"Remove-Module PSReadLine -Force -ErrorAction SilentlyContinue\"",
    "cwd": "%LOCALAPPDATA%\\nova-cognitive\\Nova\\Temp\\mcp-terminal\\1a2b3c4d5e6f7a8b",
    "running": true,
    "exitCode": null,
    "createdAtUtc": "2026-10-02T20:15:30.1234567Z"
  }
}
```

---

## 4. Operational Best Practices

* **State Check Before Commands:** Check session state to avoid running commands against exited or broken shells.

---

## See Also

* [`nova.terminal_list`](nova-terminal-list.md) - List all active sessions.
* [`nova.terminal_close`](nova-terminal-close.md) - Close session.
* [Headless Terminal Workspaces Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
