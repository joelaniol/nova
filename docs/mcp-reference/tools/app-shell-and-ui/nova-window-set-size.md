# `nova.window_set_size`

> **Resizes the Nova application window to specified pixel width and height.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 2 (Window Geometry)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.window_set_size` adjusts the host window outer bounds to simulate various standard display resolutions.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `height` | `integer` | **Yes** | Target window height in logical (DPI-aware) pixels. |
| `width` | `integer` | **Yes** | Target window width in logical (DPI-aware) pixels. |

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
