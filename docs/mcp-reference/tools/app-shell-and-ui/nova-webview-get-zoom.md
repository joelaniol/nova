# `nova.webview_get_zoom`

> **Retrieves the current zoom factor of the target tab's WebView2 control.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 1 (Read-Only Zoom State)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
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
      "text": "Zoom factor for tab-1: 1.0 (100%)."
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

* **Visual Alignment:** Confirm zoom factor is 1.0 before performing pixel-precise element coordinate measurements.

---

## 5. Related Tools

* [`nova.webview_set_zoom`](nova-webview-set-zoom.md)
* [`nova.webview_reset_zoom`](nova-webview-reset-zoom.md)
