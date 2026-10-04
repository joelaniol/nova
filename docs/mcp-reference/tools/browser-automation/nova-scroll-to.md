# `nova.scroll_to`

> **Scrolls the target tab viewport to absolute pixel coordinates (x, y).**

* **Core Feature Guide:** [Input Dispatch & Shadow DOM Traversal](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.scroll_to` sets the document scroll position to absolute coordinates (`x` defaults to 0, `y` is required). The text block carries the raw scroll measurement; `structuredContent.result` holds the same data. The response example below is an excerpt; Nova adds page and contract fields such as `pageUrl` and `stage`.

If the page is already at the requested position or at the edge, `status` is `noop` (`scroll_to.already_at_position` or `scroll_to.at_boundary`). If nothing moved because the page scrolls inside an inner container, `status` is `no_effect` with a hint to use `nova.scroll_smart`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `x` | `number` | No | `0` | — | Target horizontal scroll position in pixels. |
| `y` | `number` | Yes | — | — | Target vertical scroll position in pixels (0 = top of page). |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_scroll_to",
  "arguments": {
    "targetId": "tab-1",
    "y": 0
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "{\"ok\":true,\"before\":{\"x\":0,\"y\":1840},\"after\":{\"x\":0,\"y\":0},\"movedWindow\":true,\"reasonCode\":\"success\"}"
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "ok": true,
    "status": "ok",
    "x": 0,
    "y": 0,
    "changed": true,
    "warnings": [],
    "result": {
      "ok": true,
      "before": {
        "x": 0,
        "y": 1840
      },
      "after": {
        "x": 0,
        "y": 0
      },
      "movedWindow": true,
      "reasonCode": "success"
    }
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
