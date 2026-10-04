# `nova.measure_elements`

Measures geometric dimensions, client/scroll metrics, overflow flags, and constraining ancestor boundaries across multiple CSS selectors in a single round-trip.

---

## 1. Overview

Diagnosing responsive layout bugs, clipped text, or unexpected wrapping usually requires dozens of `getBoundingClientRect()` calls. `nova.measure_elements` measures up to 25 selectors in one call. Crucially, per matched element it calculates the **three widths a layout defect lives between**:
1. `viewportWidth` — the window width.
2. `availableWidth` — the client width of the innermost ancestor narrower than the window (the nearest actual constraint; `null`/equal to the viewport when no ancestor constrains it).
3. The element's own rendered `rect.width`.

This reveals `usedWidthRatio` (`width / availableWidth`) — a metric that CSS media queries cannot detect and screenshots cannot explain.

* **Zero Scrolling:** Measuring never shifts or scrolls the page viewport.
* **Batch Execution:** Evaluates up to 25 distinct selectors in one call.
* **Partial Match Resilience:** If one selector misses or is unparseable, valid selectors are still measured with individual `found: false` reporting.

---

## 2. Key Capabilities & Features

### A. The Three-Width Constraint Metric
A UI element frequently breaks not because the screen is too narrow, but because a parent container (such as a sidebar or modal column) offers restricted width. Each result's `widthContext` reports:
* `viewportWidth`: 1920
* `availableWidth`: 220 (the sidebar's client width)
* the element's own `rect.width`: 245
* `usedWidthRatio`: 1.114, plus `overflowsAvailableWidth: true` and `overhangPx: 25` — the element is 25px wider than the space it was given.
* `withinViewportX`: whether the element's horizontal bounds still fall inside the viewport at all (catches elements pushed off-screen entirely, which a ratio alone would not show).

### B. Overflow Flags
For each matched element, `overflow.x`/`overflow.y` report whether `scrollWidth > clientWidth` / `scrollHeight > clientHeight`. This tool does not classify *why* — for clipped-vs-plain overflow (ellipsis, `overflow: hidden`), use [`nova.detect_overflow`](nova-detect-overflow.md).

### C. Optional Computed Styles (`properties`)
Pass up to 20 specific CSS property names (e.g. `max-width`, `min-width`, `box-sizing`, `flex-shrink`) to return resolved styles alongside bounding rects.

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `selectors` | `array` of `string` | Yes | — | 1–25 items | CSS selectors to measure, 1-25 per call. |
| `properties` | `array` of `string` | No | — | ≤ 20 items | Optional computed-style properties to read per element; returned under each result's 'properties'. |
| `matchMode` | `string` | No | `"first"` | `first`, `all` | 'first' (default) measures only the first match per selector; 'all' measures up to maxMatchesPerSelector and reports truncated=true when a selector had more. |
| `maxMatchesPerSelector` | `integer` | No | `5` | 1–25 | Upper bound on measured matches per selector when matchMode='all'. matchCount always reports how many the selector really had, so a bound is visible rather than silent. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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

`structuredContent` carries the outcome (`ok`/`status`/`reasonCode`) alongside the probe's own `result`:

```json
{
  "targetId": "tab-101",
  "ok": true,
  "status": "ok",
  "reasonCode": null,
  "requestedSelectors": 2,
  "matchedSelectors": 2,
  "matchMode": "first",
  "maxMatchesPerSelector": 5,
  "result": {
    "ok": true,
    "url": "https://example.com/app",
    "viewport": { "width": 1440, "height": 900, "devicePixelRatio": 1 },
    "pageHorizontalScroll": false,
    "requestedSelectors": 2,
    "matchedSelectors": 2,
    "results": [
      {
        "selector": "aside.sidebar",
        "matchIndex": 0,
        "matchCount": 1,
        "found": true,
        "tag": "aside",
        "path": "aside.sidebar",
        "visible": true,
        "rect": { "x": 0, "y": 64, "width": 280, "height": 836 },
        "content": { "clientWidth": 280, "clientHeight": 836, "scrollWidth": 280, "scrollHeight": 836 },
        "overflow": { "x": false, "y": false },
        "widthContext": {
          "viewportWidth": 1440,
          "availableWidth": 1440,
          "constrainingAncestor": null,
          "usedWidthRatio": 0.194,
          "overflowsAvailableWidth": false,
          "overhangPx": 0,
          "withinViewportX": true
        },
        "properties": { "max-width": "300px", "box-sizing": "border-box" }
      },
      {
        "selector": "button.cta-primary",
        "matchIndex": 0,
        "matchCount": 1,
        "found": true,
        "tag": "button",
        "path": "aside.sidebar > button.cta-primary",
        "visible": true,
        "rect": { "x": 20, "y": 120, "width": 245, "height": 44 },
        "content": { "clientWidth": 245, "clientHeight": 44, "scrollWidth": 245, "scrollHeight": 44 },
        "overflow": { "x": false, "y": false },
        "widthContext": {
          "viewportWidth": 1440,
          "availableWidth": 220,
          "constrainingAncestor": { "path": "aside.sidebar", "tag": "aside", "clientWidth": 220, "cssWidth": "220px", "cssMaxWidth": "none", "display": "block", "overflowX": "visible" },
          "usedWidthRatio": 1.114,
          "overflowsAvailableWidth": true,
          "overhangPx": 25,
          "withinViewportX": true
        }
      }
    ],
    "truncated": false
  }
}
```

A miss or unparsable selector is reported as its own entry (`found: false`, `reasonCode: "measure.selector_not_found"` or `"measure.invalid_selector"`) rather than failing the whole call.

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `ok: false`, `reasonCode: "measure.no_matches"` | None of the provided selectors matched any elements. | Verify selector spelling or check if elements require dynamic rendering. |
| `status: "partial"`, `reasonCode: "measure.partial_matches"` | Some selectors matched, others did not; `ok` is still `true`. | Check each result's `found`/`reasonCode` to see which selectors missed. |
| `found: false`, `reasonCode: "measure.selector_not_found"` | Individual selector was valid CSS but matched nothing. | Check if that specific component is hidden or conditionally rendered. |
| `found: false`, `reasonCode: "measure.invalid_selector"` | Individual selector string is not valid CSS. | Fix the selector syntax; other selectors in the same call were still measured. |
| `widthContext.overflowsAvailableWidth: true` | Element is physically wider than the container providing its space. | Inspect CSS margins, padding, or flex settings using [`nova.get_computed_style`](nova-get-computed-style.md). |

---

## 7. Related Tools & Documentation

* [`nova.detect_overflow`](nova-detect-overflow.md) — Scan the whole page for clipped text and bleeding containers.
* [`nova.get_computed_style`](nova-get-computed-style.md) — Inspect full CSS styling and box models.
* [`nova.audit_accessibility`](nova-audit-accessibility.md) — Validate touch target sizes and visual contrast.
