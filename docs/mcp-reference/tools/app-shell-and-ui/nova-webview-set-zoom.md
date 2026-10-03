# `nova.webview_set_zoom`

> **Sets the zoom factor for a target tab's WebView2 instance.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 2 (Viewport Configuration)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.webview_set_zoom` adjusts page magnification (e.g. 0.75 for 75%, 1.5 for 150%) to inspect responsive scaling or fit wide tables.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `persistForSite` | `boolean` | No | Store the level for this host so future visits reopen at it (same effect as Ctrl+Plus). Default false keeps the zoom to the current session, which is usually what a temporary screenshot or layout check wants. Ignored on private tabs, which never persist. |
| `targetId` | `string` | No | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `zoomFactor` | `number` | **Yes** | Zoom level: 1.0 = 100%, 0.5 = 50%, 2.0 = 200%. Valid range is 0.25-5.0. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_webview_set_zoom",
  "arguments": {
    "targetId": "tab-1",
    "zoomFactor": 1.25
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Set zoom factor for tab-1 to 1.25 (125%)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "zoomFactor": 1.25
  }
}
```

---

## 4. Operational Best Practices

* **Responsive Inspection:** Zoom out (0.8) to fit high-resolution dashboards on smaller displays.

---

## 5. Related Tools

* [`nova.webview_get_zoom`](nova-webview-get-zoom.md)
* [`nova.webview_reset_zoom`](nova-webview-reset-zoom.md)
