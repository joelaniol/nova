# `nova.ssh_shell_watch`

Shows the **user** a read-only live view of an interactive terminal you opened, and controls that display window.

---

## 1. Overview

`nova.ssh_shell_watch` lets you — the agent — put an interactive SSH terminal you are driving ([`nova.ssh_shell_open`](nova-ssh-shell-open.md)) **on screen for the human**, and resize, focus or close that viewer. It is Nova's "the agent can drive every surface" rule applied to the terminal: you decide when the person sees the live session.

* **Read-only display, not input.** The viewer mirrors exactly the screen you already read with [`nova.ssh_shell_read`](nova-ssh-shell-read.md) (real colours, correct Unicode). It **never** sends input and is **never** a second writer — you remain the only one driving the terminal.
* **`action`** selects what to do: `open` shows (or re-focuses) the viewer, `resize` sets the **display window** size, `focus` brings it to the front, `close` closes it.
* **Window size, not remote size.** `width`/`height` resize the *display window in pixels*. They do **not** change the remote terminal's columns/rows — that geometry belongs to the session (use [`nova.ssh_shell_resize`](nova-ssh-shell-resize.md) for the actual terminal). Resizing the viewer never disturbs what you are doing.
* **Honest result.** `watchState` is `open` or `closed`; `width`/`height` report the display window size (null when closed). In a headless or unattended context (no Nova window), the call returns `watch_ui_unavailable`.
* **The user can also open it themselves** from the connector activity indicator — this tool is the agent-driven path to the same read-only viewer.

* **Core Architecture Guide:** [Secure Shell (SSH)](../../../core-features/connectors/ssh/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `execId` | `string` | Yes | — | — | Terminal id from nova.ssh_shell_open. |
| `action` | `string` | No | `"open"` | `open`, `close`, `resize`, `focus` | open shows the read-only viewer; resize sets the display window size; focus brings it to front; close closes it. |
| `width` | `integer` | No | — | 100–10000 | Display window width in pixels (for action=resize). NOT the remote terminal width. |
| `height` | `integer` | No | — | 100–10000 | Display window height in pixels (for action=resize). NOT the remote terminal height. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.ssh_shell_watch",
  "arguments": {
    "execId": "ssh_3f9a1c22",
    "action": "open"
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
    "action": "open",
    "watchState": "open",
    "width": 900,
    "height": 560,
    "note": "read_only_display_control_not_remote_input"
  }
}
```

---

## 4. Operational Best Practices

* **Open it when the human should watch.** For anything the user asked to "see" — a long migration, a TUI, a risky step — `open` the viewer so they can follow along live, read-only.
* **Resize the window, not the terminal.** Use `resize` here only to make the viewer bigger/smaller on screen; to change what the remote program sees, use [`nova.ssh_shell_resize`](nova-ssh-shell-resize.md).
* **Close it when done.** `close` the viewer once the session ends or the user no longer needs to watch; the terminal itself keeps running until you [`nova.ssh_shell_close`](nova-ssh-shell-close.md) it.
* **Expect `watch_ui_unavailable` when headless.** Scheduled/unattended runs have no window to show; do not treat it as a failure of the session.
