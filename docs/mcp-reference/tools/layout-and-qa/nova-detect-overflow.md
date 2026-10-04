# `nova.detect_overflow`

Scans the page or a scoped subtree for layout defects, clipped text, overflowing containers, and elements bleeding past the viewport edge.

---

## 1. Overview

Layout overflow issues—such as unintentional horizontal scrollbars, clipped text labels, or table columns breaking through container boundaries—are among the most common visual defects in web development. `nova.detect_overflow` runs an automated Quality Assurance scan over the DOM to pinpoint every overflowing element and return actionable coordinates and CSS selectors.

* **Three Issue Types Plus a Page-Level Flag:** `clipped-text`, `overflow`, and `viewport-bleed` per element, plus a separate `pageHorizontalScroll` boolean for the document as a whole.
* **Component Scoping (`selector`):** Audit a specific component or modal subtree instead of the entire document.
* **Read-Only:** Runs without mutating stylesheets, scrolling viewports, or altering DOM state.

---

## 2. Detected Issue Types

Each scanned element can report at most one issue; `x`-axis overflow is split into "clipped" (hidden/ellipsis — a real defect) vs. plain `overflow` (scrollable on purpose in most designs), while any `y`-axis overflow is only reported when it is actually hidden/clipped — a scrollable container's normal vertical scrollbar is not flagged.

| `type` | Cause / Detection Rule | `details` fields |
| :--- | :--- | :--- |
| **`clipped-text`** | `scrollWidth > clientWidth` (or `scrollHeight > clientHeight` on the y-axis) **and** the overflow is hidden/clipped (`text-overflow: ellipsis`, `overflow: hidden`/`clip`). | `scrollWidth`/`clientWidth`/`textOverflow`/`overflowX` (x-axis), or `axis:"y"`, `scrollHeight`/`clientHeight`/`overflowY` (y-axis). |
| **`overflow`** | `scrollWidth > clientWidth` on the x-axis without hidden/ellipsis styling — content spills rather than being clipped. | `axis:"x"`, `scrollWidth`, `clientWidth`, `overflowX`. |
| **`viewport-bleed`** | A non-fixed/non-sticky element's right edge sits past the viewport width while its left edge is still inside it. | `right`, `viewportWidth`, `overhangPx`. |

Separately, the top-level `pageHorizontalScroll` boolean reports whether the document's scrolling element itself has `scrollWidth > clientWidth` (a global horizontal scrollbar), independent of the per-element issue list.

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `selector` | `string` | No | `"body"` | — | CSS selector for the root element to scan. Defaults to 'body' (whole page). |
| `maxIssues` | `integer` | No | `200` | 1–2000 | Maximum number of issues to return; the scan stops early and sets truncated=true when reached. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
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

`structuredContent` wraps the in-page probe's own result under `result` (`targetId` and `ok` are lifted to the top level):

```json
{
  "targetId": "tab-101",
  "ok": true,
  "result": {
    "ok": true,
    "selectorMatched": true,
    "selector": "body",
    "url": "https://example.com/account",
    "scanned": 412,
    "pageHorizontalScroll": true,
    "summary": { "clippedText": 1, "overflow": 0, "viewportBleed": 1, "total": 2 },
    "issues": [
      {
        "type": "viewport-bleed",
        "selector": "table.user-data-table",
        "tag": "table",
        "text": "Name Email Plan ...",
        "details": { "right": 1492, "viewportWidth": 1440, "overhangPx": 52 }
      },
      {
        "type": "clipped-text",
        "selector": "span.account-email-label",
        "tag": "span",
        "text": "jane.doe@example",
        "details": { "scrollWidth": 168, "clientWidth": 120, "textOverflow": "ellipsis", "overflowX": "hidden" }
      }
    ],
    "truncated": false
  }
}
```

The scan examines at most 8000 elements; a larger subtree sets `truncated: true`.

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `-32004: No element matched selector '...'` | Provided root `selector` does not exist in the DOM. | Check selector spelling or verify that the component is loaded. |
| `-32002: Overflow probe failed: ...` | The in-page probe threw. | Check the selector syntax and retry. |
| `result.pageHorizontalScroll: true` | The document itself has a global horizontal scrollbar. | Filter `issues` for `type: "viewport-bleed"` to find the elements forcing it. |

---

## 7. Related Tools & Documentation

* [`nova.measure_elements`](nova-measure-elements.md) — Measure constraining ancestor widths and `usedWidthRatio`.
* [`nova.get_computed_style`](nova-get-computed-style.md) — Inspect CSS `overflow`, `white-space`, and `max-width` rules.
* [`nova.audit_accessibility`](nova-audit-accessibility.md) — Check for touch-target sizes and contrast issues.
