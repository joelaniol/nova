# `nova.detect_overflow`

Scans the page or a scoped subtree for layout defects, clipped text, overflowing containers, and elements bleeding past the viewport edge.

---

## 1. Overview

Layout overflow issues—such as unintentional horizontal scrollbars, clipped text labels, or table columns breaking through container boundaries—are among the most common visual defects in web development. `nova.detect_overflow` runs an automated Quality Assurance scan over the DOM to pinpoint every overflowing element and return actionable coordinates and CSS selectors.

* **Capability Bundle:** `layout_and_qa`, `quality_inspection`
* **Four Issue Classes:** Detects container scroll overflows, viewport boundary bleeding, clipped text nodes, and page-level horizontal scroll.
* **Component Scoping (`selector`):** Audit a specific component or modal subtree instead of the entire document.
* **Read-Only:** Runs without mutating stylesheets, scrolling viewports, or altering DOM state.

---

## 2. Detected Issue Classes

| Issue Type | Cause / Detection Rule | Visual Symptom |
| :--- | :--- | :--- |
| **`container_overflow`** | `scrollWidth > clientWidth` or `scrollHeight > clientHeight` without intended scrollbars. | Content spills out or creates unexpected scrollbars within card containers. |
| **`viewport_bleeding`** | Element's right or bottom boundary exceeds the document window width (`rect.x + rect.width > window.innerWidth`). | Causes annoying horizontal scrolling on mobile or desktop viewports. |
| **`clipped_text`** | Text is truncated via `text-overflow: ellipsis` or `overflow: hidden` when content exceeds visible dimensions. | Truncated product titles, cut-off price tags, or clipped buttons. |
| **`document_horizontal_scroll`** | The root document element has `scrollWidth > innerWidth`. | Indicates an uncontained element is forcing a global horizontal scrollbar. |

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `selector` | `string` | No | `"body"` | — | CSS selector for the root element to scan. Defaults to 'body' (whole page). |
| `maxIssues` | `integer` | No | `200` | 1–2000 | Maximum number of issues to return; the scan stops early and sets truncated=true when reached. |
<!-- /generated:parameters -->

---

## 4. Example Calls

### Full Page Overflow Audit
```json
{}
```

### Audit Specific Navigation Header
```json
{
  "selector": "header.navbar-container",
  "maxIssues": 50
}
```

### Audit Dialog Panel for Clipped Content
```json
{
  "selector": "div.modal-dialog"
}
```

---

## 5. Return Value Structure

```json
{
  "targetId": "tab-101",
  "scannedRoot": "body",
  "hasDocumentHorizontalScroll": true,
  "documentScrollWidth": 1492,
  "windowWidth": 1440,
  "issueCount": 2,
  "truncated": false,
  "issues": [
    {
      "type": "viewport_bleeding",
      "selector": "table.user-data-table",
      "rect": { "x": 300, "y": 420, "width": 1192, "height": 380 },
      "overflowPx": 52,
      "message": "Element bleeds 52px past the right window boundary."
    },
    {
      "type": "clipped_text",
      "selector": "span.account-email-label",
      "rect": { "x": 1240, "y": 18, "width": 120, "height": 24 },
      "message": "Text is truncated by text-overflow: ellipsis (scrollWidth: 168px, clientWidth: 120px)."
    }
  ]
}
```

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `Selector matched nothing: ...` | Provided root `selector` does not exist in the DOM. | Check selector spelling or verify that the component is loaded. |
| `hasDocumentHorizontalScroll: true` | One or more elements exceed window boundaries. | Filter issues for `type: "viewport_bleeding"` to locate offending elements. |

---

## 7. Related Tools & Documentation

* [`nova.measure_elements`](nova-measure-elements.md) — Measure constraining ancestor widths and `usedWidthRatio`.
* [`nova.get_computed_style`](nova-get-computed-style.md) — Inspect CSS `overflow`, `white-space`, and `max-width` rules.
* [`nova.audit_accessibility`](nova-audit-accessibility.md) — Check for touch-target sizes and contrast issues.
