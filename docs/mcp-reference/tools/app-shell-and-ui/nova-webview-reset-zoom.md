# `nova.webview_reset_zoom`

> **Resets the target tab's WebView2 zoom factor back to the default 1.0 (100%).**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 2 (Viewport Configuration)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.webview_reset_zoom` restores normal 1:1 pixel scaling for a tab, clearing previous zoom adjustments.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `targetId` | `string` | No | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |

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
