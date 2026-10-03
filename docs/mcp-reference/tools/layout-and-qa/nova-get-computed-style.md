# `nova.get_computed_style`

Reads the fully resolved CSS computed style and box-model geometry of a specific DOM element, providing authoritative styling data without executing arbitrary JavaScript.

---

## 1. Overview

Testing whether a button is visually disabled, checking font family hierarchy, or verifying exact margin and padding values often leads agents to write fragile `window.getComputedStyle(el)` scripts via `eval`. `nova.get_computed_style` provides a dedicated, read-only interface that returns both a curated core design set (colors, typography, dimensions, display, visibility) and any requested custom CSS properties.

* **Zero Script Execution:** Safe, read-only CSSOM extraction.
* **Curated Core Styles:** Automatically returns common design properties (colors, fonts, box model, z-index, visibility).
* **Custom Property Support (`properties`):** Request any specific CSS property (e.g. `grid-template-columns`, `flex-direction`, `backdrop-filter`).

---

## 2. Default Curated Properties

When called, Nova always returns the following primary design properties:

* **Typography:** `font-family`, `font-size`, `font-weight`, `line-height`, `letter-spacing`, `text-align`.
* **Colors & Borders:** `color`, `background-color`, `border-width`, `border-style`, `border-color`, `border-radius`.
* **Box Model:** `margin`, `padding`, `box-sizing`, `width`, `height`.
* **Layout & Visibility:** `display`, `position`, `z-index`, `opacity`, `visibility`, `overflow`.
* **Bounding Box:** Screen coordinates `{ x, y, width, height }`.

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `selector` | `string` | Yes | — | — | CSS selector for the element to inspect. |
| `properties` | `array` of `string` | No | — | — | Optional extra CSS property names to return under result.requested (in addition to the curated set). |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
<!-- /generated:parameters -->

---

## 4. Example Calls

### Inspect Primary Action Button
```json
{
  "selector": "button#submit-button"
}
```

### Inspect Grid Layout & Flexbox Configuration
```json
{
  "selector": "div.product-card-grid",
  "properties": [
    "grid-template-columns",
    "grid-gap",
    "justify-content",
    "align-items"
  ]
}
```

---

## 5. Return Value Structure

```json
{
  "targetId": "tab-101",
  "selector": "button#submit-button",
  "rect": {
    "x": 480,
    "y": 620,
    "width": 180,
    "height": 44
  },
  "styles": {
    "color": "rgb(255, 255, 255)",
    "backgroundColor": "rgb(15, 98, 254)",
    "fontFamily": "-apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, sans-serif",
    "fontSize": "16px",
    "fontWeight": "600",
    "display": "inline-flex",
    "visibility": "visible",
    "opacity": "1",
    "cursor": "pointer",
    "zIndex": "auto"
  },
  "requested": {
    "grid-template-columns": "none",
    "grid-gap": "normal"
  }
}
```

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `Selector matched nothing: ...` | Target element does not exist in the active document. | Verify selector using [`nova.dom_extract`](../dom-and-reading/nova-dom-extract.md). |
| `Unsupported property format` | CSS property name contains invalid characters. | Use standard kebab-case CSS property names (e.g. `flex-direction`). |

---

## 7. Related Tools & Documentation

* [`nova.measure_elements`](nova-measure-elements.md) — Batch geometry and container width measurements.
* [`nova.detect_overflow`](nova-detect-overflow.md) — Automated scan for visual clipping.
* [`nova.audit_accessibility`](nova-audit-accessibility.md) — Contrast and target size compliance.
