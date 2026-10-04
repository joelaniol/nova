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

When called, Nova always returns the following curated fields, grouped under `result`:

* **`box`:** bounding rect `{ width, height, x, y }` (CSS pixels, from `getBoundingClientRect`).
* **`color` / `backgroundColor`:** resolved `color` and `background-color`.
* **`font`:** `family`, `size`, `weight`, `style`, `lineHeight`, `letterSpacing`, `textAlign`, `textTransform`.
* **`spacing`:** `marginTop`/`Right`/`Bottom`/`Left`, `paddingTop`/`Right`/`Bottom`/`Left`.
* **`boxModel`:** `display`, `position`, `boxSizing`, `borderTopWidth`/`RightWidth`/`BottomWidth`/`LeftWidth`, `borderRadius`, `overflow`, `zIndex`.
* **`visibility`:** `opacity`, `visibility`.

Only per-side border widths and `borderRadius` are included — there is no combined `border-style`/`border-color` field, and `width`/`height` live only in `box`, not duplicated under `boxModel`.

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `selector` | `string` | Yes | — | — | CSS selector for the element to inspect. |
| `properties` | `array` of `string` | No | — | — | Optional extra CSS property names to return under result.requested (in addition to the curated set). |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
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
  "ok": true,
  "result": {
    "ok": true,
    "found": true,
    "selector": "button#submit-button",
    "tag": "button",
    "box": { "width": 180, "height": 44, "x": 480, "y": 620 },
    "color": "rgb(255, 255, 255)",
    "backgroundColor": "rgb(15, 98, 254)",
    "font": {
      "family": "-apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, sans-serif",
      "size": "16px",
      "weight": "600",
      "style": "normal",
      "lineHeight": "20px",
      "letterSpacing": "normal",
      "textAlign": "center",
      "textTransform": "none"
    },
    "spacing": { "marginTop": "0px", "marginRight": "0px", "marginBottom": "0px", "marginLeft": "0px", "paddingTop": "8px", "paddingRight": "16px", "paddingBottom": "8px", "paddingLeft": "16px" },
    "boxModel": { "display": "inline-flex", "position": "static", "boxSizing": "border-box", "borderTopWidth": "0px", "borderRightWidth": "0px", "borderBottomWidth": "0px", "borderLeftWidth": "0px", "borderRadius": "6px", "overflow": "visible", "zIndex": "auto" },
    "visibility": { "opacity": "1", "visibility": "visible" },
    "requested": { "grid-template-columns": "none", "grid-gap": "normal" }
  }
}
```

`requested` is present only when `properties` was passed; a custom property name that `getPropertyValue` does not recognize simply comes back as an empty string, not an error.

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `-32602: selector is required` | `selector` was omitted or blank. | Pass a non-empty CSS selector. |
| `-32004: No element matched selector '...'` | Target element does not exist in the active document. | Verify the selector against the live DOM, e.g. with [`nova.measure_elements`](nova-measure-elements.md). |
| `-32002: Computed-style probe failed: ...` | The in-page probe threw. | Check the selector syntax and retry. |

---

## 7. Related Tools & Documentation

* [`nova.measure_elements`](nova-measure-elements.md) — Batch geometry and container width measurements.
* [`nova.detect_overflow`](nova-detect-overflow.md) — Automated scan for visual clipping.
* [`nova.audit_accessibility`](nova-audit-accessibility.md) — Contrast and target size compliance.
