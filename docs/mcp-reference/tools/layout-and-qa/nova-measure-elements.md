# `nova.measure_elements`

Measures geometric dimensions, client/scroll metrics, overflow flags, and constraining ancestor boundaries across multiple CSS selectors in a single round-trip.

---

## 1. Overview

Diagnosing responsive layout bugs, clipped text, or unexpected wrapping usually requires dozens of `getBoundingClientRect()` calls. `nova.measure_elements` measures up to 25 selectors simultaneously. Crucially, it calculates the **three critical layout widths**:
1. The **Window Width**.
2. The **Constraining Ancestor Offered Width** (the innermost ancestor narrower than the viewport).
3. The **Element Rendered Width**.

This reveals `usedWidthRatio`—a metric that CSS media queries cannot detect and screenshots cannot explain.

* **Capability Bundle:** `layout_and_qa`, `element_inspection`
* **Zero Scrolling:** Measuring never shifts or scrolls the page viewport.
* **Batch Execution:** Evaluates up to 25 distinct selectors in one call.
* **Partial Match Resilience:** If one selector misses or is unparseable, valid selectors are still measured with individual `found: false` reporting.

---

## 2. Key Capabilities & Features

### A. The Three-Width Constraint Metric
A UI element frequently breaks not because the screen is too narrow, but because a parent container (such as a sidebar or modal column) offers restricted width:
* A button inside a 220px sidebar within a 1920px window will report:
  * `windowWidth`: 1920
  * `availableWidth`: 220
  * `renderedWidth`: 245
  * `usedWidthRatio`: 1.11 (Flagged: element overflows its container by 11%).

### B. Overflow and Clipping Flags
For each matched element, Nova evaluates:
* `hasHorizontalOverflow`: `scrollWidth > clientWidth`.
* `hasVerticalOverflow`: `scrollHeight > clientHeight`.
* `isClipped`: Whether content is clipped by `overflow: hidden` or `text-overflow: ellipsis`.

### C. Optional Computed Styles (`properties`)
Pass up to 20 specific CSS property names (e.g. `max-width`, `min-width`, `box-sizing`, `flex-shrink`) to return resolved styles alongside bounding rects.

---

## 3. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`selectors`** | `array<string>` | **Yes** | — | Array of 1–25 CSS selectors to measure in the top document. |
| **`properties`** | `array<string>` | No | `null` | Optional CSS property names to read per element (up to 20 properties). |
| **`matchMode`** | `string` | No | `"first"` | `"first"` measures the first match per selector; `"all"` measures multiple elements. |
| **`maxMatchesPerSelector`**| `integer` | No | `5` | Upper bound of measured elements per selector when `matchMode: "all"` (1–25). |
| **`targetId`** | `string` | No | `"active"` | Target tab ID from `nova.tabs`, or `"active"`. |
| **`agentId`** | `string` | No | `"default"` | Agent identity for claim lease verification. |

---

## 4. Example Calls

### Measure Key Layout Containers
```json
{
  "selectors": [
    "header.main-header",
    "aside.sidebar",
    "main.content-area",
    "button.cta-primary"
  ],
  "properties": ["max-width", "box-sizing", "overflow-x"]
}
```

### Measure All Cards in a Grid
```json
{
  "selectors": [".pricing-card"],
  "matchMode": "all",
  "maxMatchesPerSelector": 6
}
```

---

## 5. Return Value Structure

```json
{
  "targetId": "tab-101",
  "windowWidth": 1440,
  "windowHeight": 900,
  "results": [
    {
      "selector": "aside.sidebar",
      "found": true,
      "rect": { "x": 0, "y": 64, "width": 280, "height": 836 },
      "availableWidth": 280,
      "usedWidthRatio": 1.0,
      "overflow": { "horizontal": false, "vertical": false },
      "properties": {
        "max-width": "300px",
        "box-sizing": "border-box"
      }
    },
    {
      "selector": "button.cta-primary",
      "found": true,
      "rect": { "x": 310, "y": 120, "width": 210, "height": 44 },
      "availableWidth": 800,
      "usedWidthRatio": 0.26,
      "overflow": { "horizontal": false, "vertical": false }
    }
  ]
}
```

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `measure.no_matches` | None of the provided selectors matched any elements. | Verify selector spelling or check if elements require dynamic rendering. |
| `found: false (reasonCode: "not_in_dom")` | Individual selector was not found, but other selectors succeeded. | Check if that specific component is hidden or conditionally rendered. |
| `usedWidthRatio > 1.0` | Element is physically wider than the container providing its space. | Inspect CSS margins, padding, or flex settings using [`nova.get_computed_style`](nova-get-computed-style.md). |

---

## 7. Related Tools & Documentation

* [`nova.detect_overflow`](nova-detect-overflow.md) — Scan the whole page for clipped text and bleeding containers.
* [`nova.get_computed_style`](nova-get-computed-style.md) — Inspect full CSS styling and box models.
* [`nova.audit_accessibility`](nova-audit-accessibility.md) — Validate touch target sizes and visual contrast.
