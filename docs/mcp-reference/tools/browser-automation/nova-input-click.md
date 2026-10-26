# `nova.input_click`

> **Dispatches a physical mouse click at exact viewport X/Y coordinates.**

* **Core Feature Guide:** [Input Dispatch](../../../core-features/browser-interaction/input-dispatch/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.input_click` dispatches a mouse move, a press, and (about 16 ms later) a release through the browser's DevTools input pipeline at precise viewport coordinates. The events arrive as real browser input (`isTrusted: true`), so the click also reaches canvas widgets, WebGL surfaces, and other non-DOM targets that have no CSS selector to click by. There is no movement curve or synthetic delay beyond the fixed press/release gap — for a humanized mouse path use `nova.input_drag_humanized` (drag gestures only).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `observe` | `object` | No | — | — | See what this action set off, in the same call: requests started by page JavaScript (fetch, XHR, WebSocket, sendBeacon) with method, url, status, ok and duration, whether the page navigated, and optionally the state of an element afterwards. Waits until no request is in flight and nothing new arrived for quietMs, at most waitMs. Pass {} for the defaults. Replaces network_read before and after the action plus dom_extract. Document navigations and images are not listed. |
| `observe.waitMs` | `integer` | No | `3000` | 0–15000 | Longest wait for the traffic to settle after the action. |
| `observe.quietMs` | `integer` | No | `500` | 100–5000 | How long nothing may be in flight or arrive before the traffic counts as settled. |
| `observe.urlContains` | `string` | No | — | ≤ 500 characters | List only requests whose URL contains this text (counts still cover all). |
| `observe.maxRequests` | `integer` | No | `20` | 1–100 | Most requests listed; requestsOmitted counts the rest. |
| `observe.after` | `object` | No | — | — | Read an element once the traffic settled, like nova.dom_extract: {selector, properties}. |
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
Tool category: `normal` (standard risk class in Nova's agent permission settings).
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
      "text": "Clicked (left) at (450,320)."
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "x": 450,
    "y": 320,
    "button": "left",
    "clickCount": 1,
    "waitForNavigation": false,
    "navigationDetected": null,
    "loadCompleted": null,
    "actionDispatched": true
  }
}
```

With `waitForNavigation: true`, the response also carries `loadCompleted`, `waitedMs`, `newTabOpened`/`newTabIds` (set when the click opened a new tab instead of navigating this one), and a sanitized `pageTitle`/`pageUrl`. There is no top-level `ok` field — treat a thrown JSON-RPC error as the failure signal, and `actionDispatched: true` as confirmation the click itself was sent.

---

## 4. Operational Best Practices

* **Prefer Selectors:** Prefer `nova.click_selector` for DOM elements; reserve `nova.input_click` for canvas, WebGL, or SVG drag handles.
* **DPI Scaling:** Ensure coordinates align with WebView2 layout metrics.

---

## 5. Related Tools

* [`nova.click_selector`](nova-click-selector.md)
* [`nova.input_move`](nova-input-move.md)
