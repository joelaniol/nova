# `nova.scroll_element`

> **Shifts a specific DOM element's internal scroll offset (scrollTop) by a pixel delta.**

* **Core Feature Guide:** [Input Dispatch & Shadow DOM Traversal](../../../core-features/humanized-input-engine/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.scroll_element` finds the element matched by `selector` and sets its `scrollTop` (and `scrollLeft` where relevant) directly by `deltaY` — an immediate jump, not an animated scroll. Use it for internal scrollable containers (e.g. `overflow: auto` divs, terms-of-service boxes) rather than the main document body.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `selector` | `string` | Yes | — | — | CSS selector. Supports ' >>> ' combinator to pierce Shadow DOM boundaries (e.g. 'my-component >>> .inner-button'). |
| `deltaY` | `number` | Yes | — | — | Vertical scroll delta in pixels. Positive = down, negative = up. |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "{\"ok\":true,\"moved\":true,\"before\":{\"top\":0,\"left\":0},\"after\":{\"top\":300,\"left\":0}, ...}"
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "ok": true,
    "status": "ok",
    "reasonCode": null,
    "message": null,
    "selector": ".terms-container",
    "deltaY": 300,
    "changed": true,
    "warnings": [],
    "result": {
      "ok": true,
      "moved": true,
      "before": { "top": 0, "left": 0 },
      "after": { "top": 300, "left": 0 }
    }
  }
}
```

The `content` text is the raw scroll-probe result serialized as JSON (shown truncated above). There is no top-level `scrollTop` field — read the new offset from `result.after.top`. If the element matched by `selector` is already at the edge, `status` is `"noop"` with `reasonCode: "scroll_element.at_boundary"` (success). If the element has no scrollable overflow at all (a wrapper rather than the real scroll container was matched), `reasonCode` is `"scroll_element.not_scrollable"` instead.

---

## 4. Operational Best Practices

* **Agreements & Disclaimers:** Scroll internal agreement containers to bottom to enable greyed-out Accept buttons.
* **Wrong Selector vs. Boundary:** `reasonCode: "scroll_element.not_scrollable"` means the selector likely points at a wrapper, not the scroll container — try `nova.scroll_smart` to detect the real one instead of adjusting `deltaY`.

---

## 5. Related Tools

* [`nova.scroll_by`](nova-scroll-by.md)
* [`nova.scroll_to`](nova-scroll-to.md)
