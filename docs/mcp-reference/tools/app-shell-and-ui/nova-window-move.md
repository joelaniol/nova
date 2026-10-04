# `nova.window_move`

> **Moves the Nova application window to a monitor, by index.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.window_move` moves the host window to the monitor identified by `monitorIndex` (see `nova.window_get_bounds`'s `availableMonitors`), placing it inside that monitor's work area centered, top-left aligned, or at the same offset it had on its previous monitor.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `monitorIndex` | `integer` | Yes | — | ≥ 0 | Target monitor index from window_get_bounds.availableMonitors (primary monitor is typically index 0). |
| `position` | `string` | No | `"center"` | `center`, `top_left`, `keep_offset` | Target placement inside the monitor work area: center the window, align to the work-area top-left corner, or keep the current offset relative to the source monitor work area. |

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_window_move",
  "arguments": {
    "monitorIndex": 1
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Window moved to monitor 1 (center)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "monitorIndex": 1,
    "position": "center",
    "bounds": {
      "x": 2880,
      "y": 140,
      "width": 1600,
      "height": 900,
      "state": "normal",
      "hasFocus": true,
      "monitor": { "index": 1, "isPrimary": false },
      "availableMonitors": "... (truncated; see nova.window_get_bounds)"
    }
  }
}
```
An unknown `monitorIndex` (not present in `availableMonitors`) is rejected as an invalid parameter rather than silently falling back to another monitor.

---

## 4. Operational Best Practices

* **Secondary Display:** Relocate Nova to a secondary monitor to preserve primary screen real estate during live development.
* **Look Up the Index First:** Call `nova.window_get_bounds` to read `availableMonitors` before picking a `monitorIndex`.

---

## 5. Related Tools

* [`nova.window_get_bounds`](nova-window-get-bounds.md)
* [`nova.window_set_size`](nova-window-set-size.md)
