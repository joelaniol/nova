# `nova.webview_reset_zoom`

> **Resets the target tab's WebView2 zoom factor back to the default 1.0 (100%).**

* **Security Tier:** Tier 2 (Viewport Configuration)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.webview_reset_zoom` restores normal 1:1 pixel scaling for a tab, clearing previous zoom adjustments.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_webview_reset_zoom",
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
      "text": "Reset zoom factor for tab-1 to 1.0."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "zoomFactor": 1
  }
}
```

---

## 4. Operational Best Practices

* **Coordinate Consistency:** Reset zoom prior to clicking dynamic canvas or SVG elements.

---

## 5. Related Tools

* [`nova.webview_get_zoom`](nova-webview-get-zoom.md)
* [`nova.webview_set_zoom`](nova-webview-set-zoom.md)
