# `nova.get_element_rect`

> **Returns the exact bounding client rectangle (x, y, width, height) of an element.**

* **Capability Bundle:** `page_read_debug`
* **Security Tier:** Tier 1 (Read-Only Geometry)
* **Core Feature Guide:** [DOM Perception & Semantic Extraction](../../../core-features/tob.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.get_element_rect` computes the viewport-relative bounding box of an element matching a CSS or Shadow-DOM selector.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `selector` | `string` | Yes | — | — | CSS selector. Supports ' >>> ' combinator to pierce Shadow DOM boundaries (e.g. 'my-component >>> .inner-button'). |
| `visible` | `boolean` | No | `true` | — | If true (default), element must be visible (not just in DOM) for the rect to be valid. |
| `scrollIntoView` | `boolean` | No | `true` | — | If true (default), scroll the element into the viewport before measuring. |
| `screenshot` | `boolean` | No | `false` | — | Legacy alias for includeScreenshot. If true, return a screenshot with the element highlighted. |
| `includeScreenshot` | `boolean` | No | `false` | — | Preferred screenshot opt-in flag. Must match screenshot if both are provided. |
| `screenshotFormat` | `string` | No | — | `png`, `jpeg`, `auto` | Optional screenshot format. Omit to use the tool-intent default; use 'auto' for region-aware PNG/JPEG selection. |
| `screenshotQuality` | `integer` | No | `80` | 1–100 | JPEG quality (1-100). |
| `screenshotMaxWidth` | `integer` | No | — | 1–10000 | Optional max screenshot width. |
| `screenshotMaxHeight` | `integer` | No | — | 1–10000 | Optional max screenshot height. |
| `screenshotResponseMode` | `string` | No | — | `inline`, `reference`, `thumbnail+reference`, `auto` | Override screenshot delivery mode. When omitted and the element is found, get_element_rect returns an inline close-up crop; use 'thumbnail+reference' or 'reference' for lower inline payloads. |
| `cropPaddingPx` | `integer` | No | — | 0–200 | CSS-pixel padding around the element crop. 0 keeps a tight crop; positive values add page context and are clamped to 200. Defaults to 24. Needs includeScreenshot=true and must match contextPaddingPx if both are provided. |
| `contextPaddingPx` | `integer` | No | — | 0–200 | Alias for cropPaddingPx. |
| `cropPadding` | `string` | No | — | `tight`, `comfortable`, `debug` | Preset padding for the element crop. 'tight'=0 CSS px, 'comfortable'=18 CSS px, 'debug'=32 CSS px. Numeric cropPaddingPx/contextPaddingPx wins when provided. |
| `outputDetail` | `string` | No | `"full"` | `full`, `compact` | 'compact' omits fields that repeat a value carried elsewhere in the same response (the duplicate file path, and inlinePreview when it describes the same image as evidenceImage) plus the delivery telemetry: byteAccounting (byte counts of what you just received) and tokens (per-provider vision-token estimates). The image, coordinateMeta and every warning are unaffected - no setting can hide a warning. |
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_get_element_rect",
  "arguments": {
    "targetId": "tab-1",
    "selector": "button.checkout"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Element bounds: 200x50 at (450, 320)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "selector": "button.checkout",
    "x": 450,
    "y": 320,
    "width": 200,
    "height": 50
  }
}
```

---

## 4. Operational Best Practices

* **Click Alignment:** Retrieve rects to feed into `nova.input_click` when interacting with custom visual elements.

---

## 5. Related Tools

* [`nova.get_layout_metrics`](nova-get-layout-metrics.md)
* [`nova.measure_elements`](../layout-and-qa/nova-measure-elements.md)
