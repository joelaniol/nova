# `nova.input_click`

> **Dispatches a physical mouse click at exact viewport X/Y coordinates.**

* **Security Tier:** Tier 2 (Physical Input)
* **Core Feature Guide:** [Humanized Input & Navigation](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.input_click` simulates native hardware mouse events (mousedown, mouseup, click) at precise screen coordinates, triggering canvas widgets and non-DOM targets.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `activateIfNeeded` | `boolean` | No | `true` | — | For an explicit concrete inactive targetId, temporarily activate that Nova target before physical pointer dispatch. Defaults true. Omitted/'active' targets are never auto-retargeted, and Nova never foregrounds the app window. |
| `restoreActiveTarget` | `boolean` | No | `true` | — | After automatic activation and an unambiguous non-navigation success, restore the previously active Nova target if no user or competing target switch occurred. Ignored when no automatic activation happened. |
| `x` | `number` | Yes | — | — | X coordinate in CSS pixels relative to viewport left edge. |
| `y` | `number` | Yes | — | — | Y coordinate in CSS pixels relative to viewport top edge. |
| `button` | `string` | No | `"left"` | `left`, `middle`, `right` | Mouse button to click. |
| `clickCount` | `integer` | No | `1` | 1–3 | Click count: 1=single, 2=double, 3=triple click. |
| `waitForNavigation` | `boolean` | No | `false` | — | If true, wait for URL change + page load after clicking. |
| `waitForNavigationTimeoutMs` | `integer` | No | `5000` | 0–30000 | Max ms to wait for navigation (0-30000). Only used when waitForNavigation=true. |
| `includeScreenshot` | `boolean` | No | `false` | — | If true and navigation completes, include a screenshot in the response. |
| `screenshotMaxWidth` | `integer` | No | — | — | Max screenshot width in pixels. |
| `screenshotMaxHeight` | `integer` | No | — | — | Max screenshot height in pixels. |
| `screenshotFormat` | `string` | No | `"png"` | `png`, `jpeg`, `auto` | Screenshot format. Use 'auto' to fall back to the tool-intent default (e.g. jpeg q=72 for confirm-shots). |
| `screenshotQuality` | `integer` | No | `80` | 1–100 | JPEG quality (1-100). Only used when screenshotFormat is 'jpeg'. |
| `screenshotResponseMode` | `string` | No | — | `inline`, `reference`, `thumbnail+reference`, `auto` | Override default delivery mode for the screenshot. Default comes from the tool-intent profile (e.g. confirm-shots default 'thumbnail+reference' for token efficiency). Use 'inline' to force full image bytes, 'auto' to let the server pick based on projected token cost and session budget. |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_input_click",
  "arguments": {
    "targetId": "tab-1",
    "x": 450,
    "y": 320,
    "button": "left",
    "clickCount": 1
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Clicked at coordinates (450, 320)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "x": 450,
    "y": 320
  }
}
```

---

## 4. Operational Best Practices

* **Prefer Selectors:** Prefer `nova.click_selector` for DOM elements; reserve `nova.input_click` for canvas, WebGL, or SVG drag handles.
* **DPI Scaling:** Ensure coordinates align with WebView2 layout metrics.

---

## 5. Related Tools

* [`nova.click_selector`](nova-click-selector.md)
* [`nova.input_move`](nova-input-move.md)
