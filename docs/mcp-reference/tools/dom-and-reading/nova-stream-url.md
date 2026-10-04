# `nova.stream_url`

> **Returns the local address of a live image stream of a tab or of the Nova window.**

* **Core Feature Guide:** [DOM Perception & Semantic Extraction](../../../core-features/tob.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.stream_url` returns the address of a live view of a tab (`kind: "tab"`, page content only) or of the whole Nova window (`kind: "app"`, including tabs and address bar). The address points to Nova's local MCP server; opening it delivers a continuous stream of PNG frames (`multipart/x-mixed-replace`) at `fps` frames per second. The call itself only builds the address; it does not capture anything.

The stream endpoint needs the same bearer token as the MCP server. Pass `includeToken: true` to embed the token in the address so a plain browser can open it; treat such an address like the token itself.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `kind` | `string` | No | `"tab"` | `tab`, `app` | Stream source. 'tab': web content only (page viewport). 'app': entire application window including browser chrome (title bar, tabs, URL bar). |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `agentId` | `string` | No | `"default"` | — | Optional agent identity for claim authorization. Defaults to 'default'. |
| `fps` | `integer` | No | `2` | 1–10 | Frames per second for the stream. |
| `includeToken` | `boolean` | No | `false` | — | If true, embed the bearer auth token in the URL for direct browser access. |
| `maxWidth` | `integer` | No | — | 1–10000 | Legacy alias for screenshotMaxWidth. Max frame width in pixels. |
| `maxHeight` | `integer` | No | — | 1–10000 | Legacy alias for screenshotMaxHeight. Max frame height in pixels. |
| `screenshotMaxWidth` | `integer` | No | — | 1–10000 | Preferred frame width limit in pixels. Must match maxWidth if both are provided. |
| `screenshotMaxHeight` | `integer` | No | — | 1–10000 | Preferred frame height limit in pixels. Must match maxHeight if both are provided. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_stream_url",
  "arguments": {
    "targetId": "tab-1",
    "kind": "tab",
    "fps": 2,
    "screenshotMaxWidth": 1280
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "http://127.0.0.1:27183/stream?kind=tab&targetId=tab-1&fps=2&agentId=default&maxWidth=1280"
    }
  ],
  "structuredContent": {
    "url": "http://127.0.0.1:27183/stream?kind=tab&targetId=tab-1&fps=2&agentId=default&maxWidth=1280",
    "kind": "tab",
    "targetId": "tab-1",
    "agentId": "default",
    "fps": 2,
    "includesToken": false,
    "maxWidth": 1280
  }
}
```

---

## 4. Operational Best Practices

* **Watch Long Runs:** Open the address in a browser or viewer to follow what an agent does in a tab without taking repeated screenshots.
* **Keep Tokens Private:** Only use `includeToken: true` when the address stays on the local machine.

---

## 5. Related Tools

* [`nova.capture_screenshot`](../visual-evidence/nova-capture-screenshot.md)
* [`nova.capture_app_screenshot`](../visual-evidence/nova-capture-app-screenshot.md)
