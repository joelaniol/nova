# `nova.page_info`

Retrieves essential page metadata (URL, title, DOM ready state, viewport dimensions, scroll offsets, and active focused element) with minimal token overhead.

---

## 1. Overview

`nova.page_info` is an ultra-lightweight status inspection tool. When an agent needs to verify navigation success, check if a document has settled, read current viewport coordinates, or determine which element currently holds focus, `nova.page_info` returns these essentials without extracting full DOM trees or generating screenshots.

* **Zero Visual Overhead:** Never generates image artifacts or consumes vision tokens.
* **Settlement & Focus Tracking:** Returns `document.readyState` and detailed descriptors for the currently focused active element.
* **Auto-Shrinking Under Context Pressure:** Dynamically optimizes response payload size when the conversation approaches token limits.

---

## 2. Key Capabilities & Features

### A. Navigation & Document State
Returns:
* `url` / `href`: Current resolved canonical URL.
* `title`: Document `<title>` string.
* `readyState`: `"loading"`, `"interactive"`, or `"complete"`.
* `charset`: Character encoding of the document.

### B. Viewport & Scroll Coordinates
Provides instantaneous physical geometry:
* Viewport width and height.
* Document total scrollable width and height.
* Current `scrollX` and `scrollY` positions.

### C. Active Element Inspection
Identifies the element currently holding keyboard focus:
* Tag name (e.g. `INPUT`, `BUTTON`, `BODY`).
* ID and CSS class names.
* ARIA role or input type.

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `maxChars` | `integer` | No | `20000` | 1000–5000000 | Maximum characters to return. Defaults shrink automatically under context pressure unless explicitly provided. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
<!-- /generated:parameters -->

---

## 4. Example Calls

### Standard Page Health Check
```json
{}
```

### Inspect Target Background Tab
```json
{
  "targetId": "tab-104"
}
```

---

## 5. Return Value Structure

```json
{
  "targetId": "tab-101",
  "url": "https://example.com/app/settings",
  "title": "Account Settings - Nova Workspace",
  "readyState": "complete",
  "viewport": {
    "width": 1440,
    "height": 900
  },
  "scroll": {
    "x": 0,
    "y": 320,
    "maxX": 0,
    "maxY": 1840
  },
  "activeElement": {
    "tagName": "INPUT",
    "id": "user-display-name",
    "type": "text",
    "selector": "input#user-display-name"
  }
}
```

---

## 6. Related Tools & Documentation

* [`nova.perceive`](nova-perceive.md) — For deeper visual and structural page inspection.
* [`nova.navigate`](../browser-automation/nova-navigate.md) — For navigating between URLs.
* [`nova.tabs`](../browser-automation/nova-tabs.md) — For listing all available browser tabs.
