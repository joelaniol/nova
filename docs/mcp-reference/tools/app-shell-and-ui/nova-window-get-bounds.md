# `nova.window_get_bounds`

> **Returns host application window boundaries (position, size) and monitor inventory metadata.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 1 (Read-Only Window Geometry)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.window_get_bounds` provides screen geometry: window X/Y coordinates, width, height, current display monitor work area, and connected monitor dimensions.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_window_get_bounds",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Window bounds: 1920x1080 at (100, 100) on Primary Monitor."
    }
  ],
  "structuredContent": {
    "ok": true,
    "x": 100,
    "y": 100,
    "width": 1920,
    "height": 1080,
    "monitor": {
      "index": 0,
      "isPrimary": true,
      "workArea": {
        "width": 2560,
        "height": 1440
      }
    }
  }
}
```

---

## 4. Operational Best Practices

* **Multi-Monitor Automation:** Inspect available monitor bounds before calling `nova.window_move`.

---

## 5. Related Tools

* [`nova.window_set_size`](nova-window-set-size.md)
* [`nova.window_move`](nova-window-move.md)
