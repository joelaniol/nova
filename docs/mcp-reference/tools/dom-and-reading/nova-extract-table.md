# `nova.extract_table`

Extracts HTML `<table>` elements into structured JSON objects containing column headers (`headers[]`) and data rows (`rows[][]`), eliminating manual DOM looping and complex JavaScript evaluation.

---

## 1. Overview

Parsing tabular data using general-purpose DOM dumps or `eval` scripts is slow, brittle, and token-expensive. `nova.extract_table` is a dedicated tabular extraction engine that parses `<thead>`, `<tbody>`, `<th>`, and `<td>` elements directly into typed JSON rows with configurable cell length and row limits.

* **Structured Output:** Clean `{ headers: [...], rows: [[...]] }` representation per table.
* **Header Auto-Detection:** Automatically extracts column names from `<thead>` or leading `<th>` row cells.
* **Scoped or Multi-Table:** Extract all tables on the page, or target a specific table or container via `selector`.
* **Bounded Output:** Hard limits on tables (`maxTables`), rows (`maxRows`), columns (`maxCols`), and cell length (`maxCellChars`).

---

## 2. Key Capabilities & Features

### A. All-Table Auto-Extraction
When invoked with no selector, Nova locates every `<table>` in the document:
```json
{
  "maxTables": 5
}
```

### B. Container and Subtree Scoping (`selector`)
If a page contains multiple tables or embeds a table inside a specific dashboard card:
* Pass `selector: "section.financial-reports"` or `selector: "table#pricing-grid"`.
* If the selector matches a container (e.g. `div.data-wrapper`), Nova extracts all tables nested inside that container.
* If the selector matches nothing, Nova fails-fast with a descriptive error instead of guessing.

### C. Cell Cleaning & Normalization
* Cell content is trimmed of excess whitespace and line breaks.
* Cells exceeding `maxCellChars` (default `500`) are truncated with an ellipsis.
* Empty cells are represented as empty strings (`""`) rather than `null` or missing entries, maintaining column alignment across all rows.

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `selector` | `string` | No | — | — | Optional CSS selector. Scopes extraction to the matched table(s), or to <table> elements inside the matched container(s). Omit to extract all tables on the page. Errors if it matches nothing. |
| `maxTables` | `integer` | No | `20` | 1–200 | Maximum number of tables to return. Excess tables are dropped and the top-level 'truncated' flag is set. |
| `maxRows` | `integer` | No | `500` | 1–10000 | Maximum body rows per table. Excess rows are dropped and that table's 'truncated' flag is set. |
| `maxCols` | `integer` | No | `100` | 1–1000 | Maximum cells per row (and header columns) to return. |
| `maxCellChars` | `integer` | No | `500` | 1–20000 | Maximum characters of trimmed text per cell; longer cell text is truncated. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 4. Example Calls

### Extract All Tables on Current Page
```json
{
  "maxRows": 100
}
```

### Extract a Specific Pricing Comparison Table
```json
{
  "selector": "table.pricing-matrix",
  "maxRows": 25,
  "maxCellChars": 200
}
```

### Extract Tabular Reports from a Dashboard Widget
```json
{
  "selector": "div.analytics-widget#revenue-breakdown",
  "maxTables": 1,
  "maxRows": 50
}
```

---

## 5. Return Value Structure

```json
{
  "targetId": "tab-101",
  "selector": "table.pricing-matrix",
  "result": {
    "ok": true,
    "matchedSelectorCount": 1,
    "tableCount": 1,
    "truncated": false,
    "tables": [
      {
        "index": 0,
        "caption": null,
        "headers": ["Plan", "Monthly Price", "Concurrent Sandboxes", "API Calls / Day", "Support"],
        "rowCount": 3,
        "colCount": 5,
        "colTruncated": false,
        "truncated": false,
        "rows": [
          ["Starter", "$29", "2", "10,000", "Community"],
          ["Professional", "$99", "10", "100,000", "Priority Email"],
          ["Enterprise", "Custom", "Unlimited", "Unlimited", "Dedicated 24/7 SLA"]
        ]
      }
    ]
  }
}
```

`matchedSelectorCount` is only set when `selector` was passed (it is `null` for a full-page scan).
`caption` is the table's `<caption>` text, or `null` when it has none. Per-table `truncated` means
rows were dropped (`maxRows`); the outer `result.truncated` means whole tables were dropped
(`maxTables`); `colTruncated` means more columns exist than `maxCols` returned.

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `No element matched selector '...'.` | The provided CSS `selector` does not match any node. | Verify the container or table selector with `nova.read_dom`. |
| `nova.extract_table failed: ...` | Script execution in the page failed. | Retry, or narrow `selector` to a smaller subtree. |

A page with zero `<table>` elements (e.g. CSS grids or flexboxes instead of HTML tables) is not an
error: the call returns `ok: true` with `tableCount: 0` and an empty `tables` array. Use
[`nova.dom_extract`](nova-dom-extract.md) or [`nova.read_text_structured`](nova-read-text-structured.md)
to inspect grid-based layouts instead. A table that exceeds `maxRows` is likewise not an error — its
`truncated` flag is set and the extra rows are dropped; increase `maxRows` or paginate the page.

---

## 7. Related Tools & Documentation

* [`nova.dom_extract`](nova-dom-extract.md) — Extract arbitrary grid elements and custom list items.
* [`nova.read_text_structured`](nova-read-text-structured.md) — Extract page text grouped by landmarks.
* [`nova.search_text`](nova-search-text.md) — Find specific text entries within tables.
