# `nova.data_query`

> **Filters, groups and totals a local CSV or Excel file and returns only the result rows.**

* **Core Feature Guide:** [Tabular Data Analysis & Streaming Queries](../../../core-features/media-intelligence/data-analysis/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with 1.0.0-alpha.21, which is not published yet.

`nova.data_query` answers questions like "the ten best-selling products in September" from a table on disk, and returns only the answer - not the whole file. Your agent describes the question in fixed building blocks; Nova does the arithmetic locally and exactly. There is no query language and no code to run.

The building blocks are filters (equal, not equal, greater or smaller, contains, one of a list, empty, not empty), grouping by one or more columns, totals per group (count, sum, average, smallest, largest), sorting, and a limit (50 rows by default, at most 500). Without grouping, the result is the matching rows themselves, sorted and cut to the limit. Amounts are added as exact decimal numbers, so cents do not drift.

The file is read piece by piece, so even millions of rows work without filling the memory. The answer counts how many rows were read and how many matched, and says plainly when something affects the numbers: values that could not be read as numbers or dates, a number format that had to be assumed, or a time limit that stopped the scan early (then the result is marked as partial).

As with [`nova.data_inspect`](nova-data-inspect.md), files in Nova's download and Exports folders can always be read; other paths need "Allow local files (file://)". Nothing is written or kept.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `path` | `string` | Yes | — | — | Absolute path to a .csv, .tsv, .xlsx or .xlsm file. |
| `sheet` | `string` | No | — | — | Excel sheet name; default the first visible sheet. |
| `columns` | `array` of `string` | No | — | — | Columns of plain result rows; not with groupBy or metrics. |
| `filters` | `array` of `object` | No | — | — | All must match. |
| `groupBy` | `array` of `string` | No | — | — | Columns to group by. |
| `metrics` | `array` of `object` | No | — | — | Aggregation calculations: count, countNonNull, sum, avg, min, max. |
| `orderBy` | `any` | No | — | — | {column, direction} or a list of them. |
| `limit` | `integer` | No | `50` | 1–500 | Result rows returned. |
| `timeoutSeconds` | `integer` | No | `60` | 5–300 | Time budget for the scan. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_data_query",
  "arguments": {
    "path": "C:\\Users\\me\\Downloads\\sales.csv",
    "filters": [ { "column": "Month", "op": "gte", "value": "2026-09-01" } ],
    "groupBy": ["Product"],
    "metrics": [ { "op": "sum", "column": "Revenue", "as": "revenue" } ],
    "orderBy": { "column": "revenue", "direction": "desc" },
    "limit": 3
  }
}
```

### JSON-RPC Response

```json
{
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "complete": true,
    "columns": ["Product", "revenue"],
    "rows": [["Standing desk", 48210.5], ["Office chair", 31975.0], ["Desk lamp", 9870.4]],
    "returnedRows": 3,
    "truncated": true,
    "rowsScanned": 18240,
    "rowsMatched": 2016,
    "groups": 37,
    "warnings": []
  }
}
```

---

## 4. Related Tools

* [`nova.data_inspect`](nova-data-inspect.md) for the column names and types first.
