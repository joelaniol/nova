# `nova.terminal_read`

Reads the recent raw output tail of a terminal session scrollback buffer.

---

## 1. Overview

`nova.terminal_read` extracts the most recent output from a running or exited session. The output may contain ANSI escape codes, progress markers, and sensitive environment data.

* **Architecture Guide:** [Terminal Workspaces & ConPTY Integration](../../../core-features/terminal-workspaces.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `sessionId` | `string` | Yes | — | — | Session id from terminal_open. |
| `maxBytes` | `integer` | No | — | 256–200000 | Max bytes from the tail to return. Default 16384. |
| `agentId` | `string` | No | — | — | Accepted for compatibility and ignored: terminal sessions are addressed by sessionId and are not bound to a tab or a tab claim. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `terminal_ops` (load it with `nova.tools_bundle(bundle='terminal_ops')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.terminal_read",
  "arguments": {
    "sessionId": "term_1a2b3c4d5e6f7a8b",
    "maxBytes": 8192
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "PS C:\\Work> git status\nOn branch main\nnothing to commit"
    }
  ],
  "structuredContent": {
    "ok": true,
    "sessionId": "term_1a2b3c4d5e6f7a8b",
    "output": "PS C:\\Work> git status\nOn branch main\nnothing to commit",
    "totalBytes": 2450,
    "truncated": false,
    "running": true,
    "exitCode": null
  }
}
```

---

## 4. Operational Best Practices

* **Understanding `truncated`:** `truncated: true` indicates that output was permanently evicted from the circular scrollback buffer due to size limits, not that `maxBytes` was reached.
* **Sensitive Content:** Output may contain credentials or sensitive system information; do not log terminal scrollbacks to public sinks.

---

## See Also

* [`nova.terminal_write`](nova-terminal-write.md) - Write raw text to stdin.
* [`nova.terminal_run_command`](nova-terminal-run-command.md) - Run a command and capture output.
* [Headless Terminal Workspaces Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
