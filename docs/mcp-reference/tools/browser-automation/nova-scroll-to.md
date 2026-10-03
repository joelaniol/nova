# `nova.scroll_to`

> **Scrolls the target tab viewport to absolute pixel coordinates (top, left).**

* **Capability Bundle:** `browser_automation`
* **Security Tier:** Tier 2 (Viewport Manipulation)
* **Core Feature Guide:** [Humanized Input & Navigation](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.scroll_to` jumps or smoothly animates the document scroll position to absolute coordinates.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `targetId` | `string` | No | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `x` | `number` | No | Target horizontal scroll position in pixels. |
| `y` | `number` | **Yes** | Target vertical scroll position in pixels (0 = top of page). |

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
