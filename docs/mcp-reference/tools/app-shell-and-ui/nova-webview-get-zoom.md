# `nova.webview_get_zoom`

> **Retrieves the current zoom factor of the target tab's WebView2 control.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.webview_get_zoom` returns the effective zoom multiplier (1.0 = 100%, 1.25 = 125%) for the browser page.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_webview_get_zoom",
  "arguments": {
    "targetId": "tab-1"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "ZoomFactor=1"
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "zoomFactor": 1
  }
}
```

---

## 4. Operational Best Practices

* **Visual Alignment:** Confirm zoom factor is 1.0 before performing pixel-precise element coordinate measurements.

---

## 5. Related Tools

* [`nova.webview_set_zoom`](nova-webview-set-zoom.md)
* [`nova.webview_reset_zoom`](nova-webview-reset-zoom.md)
