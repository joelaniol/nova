# `nova.scroll_to`

> **Scrolls the target tab viewport to absolute pixel coordinates (top, left).**

* **Security Tier:** Tier 2 (Viewport Manipulation)
* **Core Feature Guide:** [Humanized Input & Navigation](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.scroll_to` jumps or smoothly animates the document scroll position to absolute coordinates.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `x` | `number` | No | `0` | — | Target horizontal scroll position in pixels. |
| `y` | `number` | Yes | — | — | Target vertical scroll position in pixels (0 = top of page). |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_scroll_to",
  "arguments": {
    "targetId": "tab-1",
    "top": 0,
    "left": 0
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Scrolled to top of page (0, 0)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "scrollX": 0,
    "scrollY": 0
  }
}
```

---

## 4. Operational Best Practices

* **Back to Top:** Quick one-shot method to reset viewport to page header after deep scrolling.

---

## 5. Related Tools

* [`nova.scroll_by`](nova-scroll-by.md)
* [`nova.scroll_smart`](nova-scroll-smart.md)
