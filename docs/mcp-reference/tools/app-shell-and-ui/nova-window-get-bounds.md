# `nova.window_get_bounds`

> **Returns host application window boundaries (position, size) and monitor inventory metadata.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.window_get_bounds` returns the host window's position, size, window state, and focus flag, the monitor it currently sits on, and the full inventory of available monitors (each with its index, name, scale factor, resolution, bounds, and work area). Use `availableMonitors` to look up a valid `monitorIndex` before calling `nova.window_move`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "{ ... same JSON as structuredContent, pretty-printed ... }"
    }
  ],
  "structuredContent": {
    "x": 100,
    "y": 100,
    "width": 1920,
    "height": 1080,
    "presenterKind": "native",
    "state": "normal",
    "hasFocus": true,
    "monitor": {
      "index": 0,
      "name": "\\\\.\\DISPLAY1",
      "isPrimary": true,
      "scaleFactor": 1.0,
      "containsWindowCenter": true,
      "resolution": { "width": 2560, "height": 1440 },
      "bounds": { "x": 0, "y": 0, "width": 2560, "height": 1440 },
      "workArea": { "x": 0, "y": 0, "width": 2560, "height": 1400 }
    },
    "availableMonitors": [
      {
        "index": 0,
        "name": "\\\\.\\DISPLAY1",
        "isPrimary": true,
        "scaleFactor": 1.0,
        "containsWindowCenter": true,
        "resolution": { "width": 2560, "height": 1440 },
        "bounds": { "x": 0, "y": 0, "width": 2560, "height": 1440 },
        "workArea": { "x": 0, "y": 0, "width": 2560, "height": 1400 }
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Multi-Monitor Automation:** Inspect `availableMonitors` before calling `nova.window_move` to confirm a valid `monitorIndex`.

---

## 5. Related Tools

* [`nova.window_set_size`](nova-window-set-size.md)
* [`nova.window_move`](nova-window-move.md)
