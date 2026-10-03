# `nova.window_move`

> **Moves the Nova application window to a specific monitor or coordinate offset.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 2 (Window Positioning)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.window_move` repositions the host window across multi-monitor setups using monitor index or X/Y offsets.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `monitorIndex` | `integer` | Yes | — | ≥ 0 | Target monitor index from window_get_bounds.availableMonitors (primary monitor is typically index 0). |
| `position` | `string` | No | `"center"` | `center`, `top_left`, `keep_offset` | Target placement inside the monitor work area: center the window, align to the work-area top-left corner, or keep the current offset relative to the source monitor work area. |
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
      "text": "Moved Nova window to Monitor 1."
    }
  ],
  "structuredContent": {
    "ok": true,
    "monitorIndex": 1,
    "x": 2560,
    "y": 0
  }
}
```

---

## 4. Operational Best Practices

* **Secondary Display:** Relocate Nova to a secondary monitor to preserve primary screen real estate during live development.

---

## 5. Related Tools

* [`nova.window_get_bounds`](nova-window-get-bounds.md)
* [`nova.window_set_size`](nova-window-set-size.md)
