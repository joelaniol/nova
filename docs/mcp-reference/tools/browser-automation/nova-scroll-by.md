# `nova.scroll_by`

> **Scrolls the page or active container by relative pixel offsets (deltaX, deltaY).**

* **Core Feature Guide:** [Input Dispatch & Shadow DOM Traversal](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.scroll_by` applies `window.scrollBy(deltaX, deltaY)` immediately — there is no animation or easing, the scroll position jumps directly by the requested delta. If the window does not move (common on single-page apps that scroll an inner container instead of the document), Nova automatically looks for the most plausible visible scrollable container on the page and scrolls that one instead; the response tells you whether the window or a fallback container moved. Pass `containerSelector` to scroll a specific container directly instead of relying on that fallback search.

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
Tool category: `normal` (standard risk class in Nova's agent permission settings).
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
      "text": "{\"ok\":true,\"movedWindow\":true,\"beforeWindow\":{\"x\":0,\"y\":700},\"afterWindow\":{\"x\":0,\"y\":1200}, ...}"
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "ok": true,
    "status": "ok",
    "reasonCode": null,
    "message": null,
    "deltaX": 0,
    "deltaY": 500,
    "changed": true,
    "warnings": [],
    "result": {
      "ok": true,
      "movedWindow": true,
      "beforeWindow": { "x": 0, "y": 700 },
      "afterWindow": { "x": 0, "y": 1200 }
    }
  }
}
```

The `content` text is the raw scroll-probe result serialized as JSON (shown truncated above), not a prose sentence. `result` in `structuredContent` carries the same data — there is no separate `newScrollY` field; read the window position from `result.afterWindow.y`, or `result.fallback.after.top` when a fallback container was used. When nothing moved and the page was already at the requested edge, `status` is `"noop"` with `reasonCode: "scroll_by.at_boundary"` (success); when nothing moved and the page was not at the edge, `status` is `"no_effect"` with `reasonCode: "scroll_by.no_effect"`.

---

## 4. Operational Best Practices

* **Incremental Discovery:** Scroll down in fixed increments to trigger lazy-loaded image hydration.
* **Inner Containers:** If `changed` comes back `false` with `reasonCode: "scroll_by.no_effect"`, try `nova.scroll_smart` for broader container detection, or pass an explicit `containerSelector`.

---

## 5. Related Tools

* [`nova.scroll_to`](nova-scroll-to.md)
* [`nova.scroll_smart`](nova-scroll-smart.md)
