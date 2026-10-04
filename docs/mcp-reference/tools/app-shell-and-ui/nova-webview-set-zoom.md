# `nova.webview_set_zoom`

> **Sets the zoom factor for a target tab's WebView2 instance.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.webview_set_zoom` adjusts page magnification (e.g. 0.75 for 75%, 1.5 for 150%) to inspect responsive scaling or fit wide tables. With `persistForSite: true` the level is saved for the page's host and reapplied on future visits; this never persists on private tabs or when no host can be resolved, and the response's `persistedForSite`/`persistScope` report what actually happened. A failure (for example on a PDF viewer page that rejects zoom changes) is reported as `ok: false` with a `reasonCode` and a recovery hint rather than a generic error.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `zoomFactor` | `number` | Yes | `1` | 0.25–5 | Zoom level: 1.0 = 100%, 0.5 = 50%, 2.0 = 200%. Valid range is 0.25-5.0. |
| `persistForSite` | `boolean` | No | `false` | — | Store the level for this host so future visits reopen at it (same effect as Ctrl+Plus). Default false keeps the zoom to the current session, which is usually what a temporary screenshot or layout check wants. Ignored on private tabs, which never persist. |

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "ZoomFactor set to 1.25. This session only."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "targetId": "tab-1",
    "zoomFactor": 1.25,
    "requestedZoomFactor": 1.25,
    "requestedPersistForSite": false,
    "persistedForSite": false,
    "persistScope": "session"
  }
}
```
On failure, `ok` is `false` and the response adds `reasonCode`, `message`, `recoveryHint`, and (when relevant) `pdfViewer: true`.

---

## 4. Operational Best Practices

* **Responsive Inspection:** Zoom out (0.8) to fit high-resolution dashboards on smaller displays.
* **Session vs. Site:** Pass `persistForSite: true` to save the level for the host; otherwise it only applies to the current session.

---

## 5. Related Tools

* [`nova.webview_get_zoom`](nova-webview-get-zoom.md)
* [`nova.webview_reset_zoom`](nova-webview-reset-zoom.md)
