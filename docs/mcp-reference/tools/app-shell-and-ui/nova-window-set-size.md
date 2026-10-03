# `nova.window_set_size`

> **Resizes the Nova application window to specified pixel width and height.**

* **Security Tier:** Tier 2 (Window Geometry)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.window_set_size` adjusts the host window outer bounds to simulate various standard display resolutions.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `width` | `integer` | Yes | — | 200–10000 | Target window width in logical (DPI-aware) pixels. |
| `height` | `integer` | Yes | — | 200–10000 | Target window height in logical (DPI-aware) pixels. |

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_window_set_size",
  "arguments": {
    "width": 1920,
    "height": 1080
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Resized Nova window to 1920x1080."
    }
  ],
  "structuredContent": {
    "ok": true,
    "width": 1920,
    "height": 1080
  }
}
```

---

## 4. Operational Best Practices

* **Standard Viewports:** Resize to standard dimensions (1920x1080, 1366x768) for consistent visual baselines.

---

## 5. Related Tools

* [`nova.window_get_bounds`](nova-window-get-bounds.md)
* [`nova.window_set_state`](nova-window-set-state.md)
