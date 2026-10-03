# `nova.scroll_element`

> **Scrolls a specific DOM element container into view or shifts its internal scroll offset.**

* **Capability Bundle:** `browser_automation`
* **Security Tier:** Tier 2 (DOM Manipulation)
* **Core Feature Guide:** [Humanized Input & Navigation](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.scroll_element` targets internal scrollable containers (e.g. overflow: auto divs, terms of service boxes) rather than the main document body.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `deltaY` | `number` | **Yes** | Vertical scroll delta in pixels. Positive = down, negative = up. |
| `selector` | `string` | **Yes** | CSS selector. Supports ' >>> ' combinator to pierce Shadow DOM boundaries (e.g. 'my-component >>> .inner-button'). |
| `targetId` | `string` | No | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_scroll_element",
  "arguments": {
    "targetId": "tab-1",
    "selector": ".terms-container",
    "deltaY": 300
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Scrolled .terms-container by 300px."
    }
  ],
  "structuredContent": {
    "ok": true,
    "selector": ".terms-container",
    "scrollTop": 300
  }
}
```

---

## 4. Operational Best Practices

* **Agreements & Disclaimers:** Scroll internal agreement containers to bottom to enable greyed-out Accept buttons.

---

## 5. Related Tools

* [`nova.scroll_by`](nova-scroll-by.md)
* [`nova.scroll_to`](nova-scroll-to.md)
