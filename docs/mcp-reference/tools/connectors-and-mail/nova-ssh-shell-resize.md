# `nova.ssh_shell_resize`

Resizes an interactive terminal's window and sends an SSH window-change request (requested, not confirmed as redrawn).

---

## 1. Overview

`nova.ssh_shell_resize` changes the window size of a terminal opened with [`nova.ssh_shell_open`](nova-ssh-shell-open.md). Nova updates its local screen model and sends an SSH window-change request to the server. This is **requested**, not confirmed: `resizeRequestSent:true` means the request went out, not that the remote TUI has finished repainting at the new size.

* **Resize before running a TUI** if you need a specific geometry, or any time the view should change.
* **Honest semantics.** A window-change request is fire-and-forget at the SSH layer; the remote program redraws on its own schedule. Read the screen afterwards to see the result.

* **Core Architecture Guide:** [Secure Shell (SSH)](../../../core-features/connectors/ssh/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `execId` | `string` | Yes | — | — | Terminal id from nova.ssh_shell_open. |
| `columns` | `integer` | Yes | — | 1–1000 | New terminal width in columns. |
| `rows` | `integer` | Yes | — | 1–1000 | New terminal height in rows. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.ssh_shell_resize",
  "arguments": {
    "execId": "ssh_3f9a1c22",
    "columns": 132,
    "rows": 50
  }
}
```

### Response (shortened)
```json
{
  "structuredContent": {
    "schemaVersion": 1,
    "ok": true,
    "execId": "ssh_3f9a1c22",
    "columns": 132,
    "rows": 50,
    "resizeRequestSent": true
  }
}
```

---

## 4. Operational Best Practices

* **Match the program.** Size the terminal to what the TUI expects before launching it; a mismatch misrenders columns and status bars.
* **Read after resizing.** The repaint is asynchronous; poll `nova.ssh_shell_read` to confirm the new geometry took effect.
