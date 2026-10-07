# `nova.terminal_write`

Writes raw characters to the session stdin without appending an implicit newline.

---

## 1. Overview

`nova.terminal_write` feeds raw bytes or strings directly into the ConPTY stdin stream. It does not wait for command completion or output generation.

* **Architecture Guide:** [Terminal Workspaces & ConPTY Integration](../../../core-features/terminal-workspaces/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `sessionId` | `string` | Yes | — | — | Session id from terminal_open. |
| `data` | `string` | Yes | — | — | Text to send to stdin verbatim. |
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
  "name": "nova.terminal_write",
  "arguments": {
    "sessionId": "term_1a2b3c4d5e6f7a8b",
    "data": "npm test\r"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Wrote 9 char(s) to 'term_1a2b3c4d5e6f7a8b'."
    }
  ],
  "structuredContent": {
    "ok": true,
    "sessionId": "term_1a2b3c4d5e6f7a8b",
    "charsWritten": 9
  }
}
```

---

## 4. Operational Best Practices

* **CRLF Submission:** Because this is a raw PTY write, a command line requires a trailing carriage return (`\r` or `\r\n`) to be executed by PowerShell.
* **Prefer `run_command`:** For linear command execution, `nova.terminal_run_command` is much safer because it waits for the exit code and sentinel.

---

## See Also

* [`nova.terminal_send_key`](nova-terminal-send-key.md) - Send control key combinations.
* [`nova.terminal_read`](nova-terminal-read.md) - Read scrollback output.
* [Headless Terminal Workspaces Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
