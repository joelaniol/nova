# `nova.get_layout_metrics`

> **Retrieves layout viewport dimensions, visual viewport offset/scale, and the full scrollable content size.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.get_layout_metrics` wraps the Chrome DevTools Protocol `Page.getLayoutMetrics` call and reports
its `layoutViewport`, `visualViewport` (including its pinch-zoom `scale`), and `contentSize`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |

Capability bundles: `browser_automation`, `page_read_debug`.
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova.get_layout_metrics",
  "arguments": {
    "targetId": "tab-1"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "{\"layoutViewport\":{...},\"visualViewport\":{...},\"contentSize\":{...}}"
    }
  ],
  "structuredContent": {
    "profileId": "tab-1",
    "layoutViewport": { "pageX": 0, "pageY": 0, "clientWidth": 1920, "clientHeight": 931 },
    "visualViewport": { "offsetX": 0, "offsetY": 0, "pageX": 0, "pageY": 0, "clientWidth": 1920, "clientHeight": 931, "scale": 1, "zoom": 1 },
    "contentSize": { "x": 0, "y": 0, "width": 1920, "height": 4200 }
  }
}
```

This is the raw Chrome DevTools Protocol `Page.getLayoutMetrics` result, passed through largely
unchanged. `layoutViewport`/`visualViewport` give the current viewport in CSS pixels;
`contentSize` is the full scrollable document size (its `height` is what a scroll-exhaustion check
compares against). The top-level key is `profileId`, not `targetId`.

---

## 4. Operational Best Practices

* **End-of-Page Detection:** Compare the visual viewport's position and size against `contentSize.height` to detect scroll exhaustion.

---

## 5. Related Tools

* [`nova.get_element_rect`](nova-get-element-rect.md)
* [`nova.page_info`](nova-page-info.md)
