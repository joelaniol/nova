# `nova.extract_table`

Extracts HTML `<table>` elements into structured JSON objects containing column headers (`headers[]`) and data rows (`rows[][]`), eliminating manual DOM looping and complex JavaScript evaluation.

---

## 1. Overview

Parsing tabular data using general-purpose DOM dumps or `eval` scripts is slow, brittle, and token-expensive. `nova.extract_table` is a dedicated tabular extraction engine that parses `<thead>`, `<tbody>`, `<th>`, and `<td>` elements directly into typed JSON rows with configurable cell length and row limits.

* **Capability Bundle:** `dom_reading`, `data_extraction`
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

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`selector`** | `string` | No | `null` | Optional CSS selector targeting a table or container element. |
| **`maxTables`** | `integer` | No | `20` | Maximum number of tables to extract (1–200). Excess tables set `truncated: true`. |
| **`maxRows`** | `integer` | No | `500` | Maximum body rows per table (1–10,000). Excess rows are dropped. |
| **`maxCols`** | `integer` | No | `100` | Maximum cells per row (1–1,000). |
| **`maxCellChars`** | `integer` | No | `500` | Maximum character length per cell (1–20,000 chars). |
| **`targetId`** | `string` | No | `"active"` | Target tab ID from `nova.tabs`, or `"active"`. |
| **`agentId`** | `string` | No | `"default"` | Agent identity for claim lease verification. |

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
  "tableCount": 1,
  "tables": [
    {
      "index": 0,
      "selector": "table.pricing-matrix",
      "headers": ["Plan", "Monthly Price", "Concurrent Sandboxes", "API Calls / Day", "Support"],
      "rowCount": 3,
      "colCount": 5,
      "truncated": false,
      "rows": [
        ["Starter", "$29", "2", "10,000", "Community"],
        ["Professional", "$99", "10", "100,000", "Priority Email"],
        ["Enterprise", "Custom", "Unlimited", "Unlimited", "Dedicated 24/7 SLA"]
      ]
    }
  ],
  "truncated": false
}
```

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `Selector matched nothing: ...` | Provided CSS selector does not match any node. | Verify container or table selector with `nova.read_dom`. |
| `No <table> elements found` | The page uses CSS grids (`display: grid`) or flexboxes instead of HTML `<table>` elements. | Use [`nova.dom_extract`](nova-dom-extract.md) or [`nova.read_text_structured`](nova-read-text-structured.md) to inspect grid items. |
| `Table rows truncated` | The table exceeds `maxRows` (e.g. large 5,000-row datasets). | Increase `maxRows` or paginate the target web page. |

---

## 7. Related Tools & Documentation

* [`nova.dom_extract`](nova-dom-extract.md) — Extract arbitrary grid elements and custom list items.
* [`nova.read_text_structured`](nova-read-text-structured.md) — Extract page text grouped by landmarks.
* [`nova.search_text`](nova-search-text.md) — Find specific text entries within tables.
