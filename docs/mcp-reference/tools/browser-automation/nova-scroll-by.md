# `nova.scroll_by`

> **Scrolls the page or active container by relative pixel offsets (deltaX, deltaY).**

* **Security Tier:** Tier 2 (Viewport Manipulation)
* **Core Feature Guide:** [Humanized Input & Navigation](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.scroll_by` shifts viewport or element offsets by relative pixel values.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `deltaX` | `number` | No | `0` | — | Horizontal scroll distance in pixels. Positive = right, negative = left. |
| `deltaY` | `number` | Yes | — | — | Vertical scroll distance in pixels. Positive = down, negative = up. Typical page scroll: 500-800. |
| `containerSelector` | `string` | No | — | — | Optional CSS selector for the scroll container. When provided, skips window.scrollBy and scrolls this container directly. |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_scroll_by",
  "arguments": {
    "targetId": "tab-1",
    "deltaX": 0,
    "deltaY": 500
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Scrolled page by 500px vertically."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "newScrollY": 1200
  }
}
```

---

## 4. Operational Best Practices

* **Incremental Discovery:** Scroll down in fixed increments to trigger lazy-loaded image hydration.

---

## 5. Related Tools

* [`nova.scroll_to`](nova-scroll-to.md)
* [`nova.scroll_smart`](nova-scroll-smart.md)
