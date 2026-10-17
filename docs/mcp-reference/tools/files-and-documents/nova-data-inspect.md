# `nova.data_inspect`

> **Shows the columns, types and value ranges of a local CSV or Excel file, before your agent queries it.**

* **Core Feature Guide:** [Tabular Data Analysis & Streaming Queries](../../../core-features/media-intelligence/data-analysis/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with 1.0.0-alpha.21, which is not published yet.

`nova.data_inspect` looks at a table on disk - a CSV or TSV export, or a sheet of an Excel workbook (`.xlsx`, `.xlsm`) - and reports what is in it: each column's name and type (number, date, yes/no, text, or mixed), how many cells are filled, empty or unreadable, and the smallest and largest value. A few first rows come along as a preview. Your agent learns the structure without the whole file ever entering its context.

Files of any length are read piece by piece, never loaded whole. Column types are decided from the first rows (1000 by default); the counts are exact when the file ended within those rows, or when you ask for a full scan. The answer always says which.

German and English number formats are both understood (`1.234,56` and `1,234.56`), as are ISO and German dates. Nova decides the format from the values themselves; when no value proves it, the answer says what was assumed instead of guessing quietly. Excel formulas are never calculated - the result Excel stored is the value - and macros never run.

Files in Nova's download folder and Exports folder can always be read; any other path needs the setting "Allow local files (file://)". Nothing is written, and nothing about the data is kept.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `path` | `string` | Yes | — | — | Absolute path to a .csv, .tsv, .xlsx or .xlsm file. |
| `sheet` | `string` | No | — | — | Excel sheet name; default the first visible sheet. |
| `sampleRows` | `integer` | No | `1000` | 10–100000 | Rows read to decide the column types. |
| `previewRows` | `integer` | No | `5` | 0–50 | First rows returned as a preview. |
| `fullScan` | `boolean` | No | `false` | — | Read the whole file for exact rowCount and statistics. |
| `timeoutSeconds` | `integer` | No | `60` | 5–300 | Time budget for a full scan. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_data_inspect",
  "arguments": {
    "path": "C:\\Users\\me\\Downloads\\sales.csv"
  }
}
```

### JSON-RPC Response

```json
{
  "structuredContent": {
    "ok": true,
    "format": "csv",
    "encoding": "utf-8",
    "delimiter": ";",
    "rowCount": 18240,
    "statisticsComplete": true,
    "columns": [
      { "name": "Product", "type": "text", "filled": 18240, "empty": 0, "invalid": 0 },
      { "name": "Month", "type": "date", "filled": 18240, "empty": 0, "invalid": 0, "min": "2026-01-01", "max": "2026-09-30" },
      { "name": "Revenue", "type": "number", "numberFormat": "1.234,56", "numberFormatBasis": "values", "filled": 18237, "empty": 3, "invalid": 0, "min": 4.5, "max": 12890 }
    ],
    "preview": { "columns": ["Product", "Month", "Revenue"], "rows": [["Desk lamp", "2026-01-01", 129.9]] },
    "warnings": []
  }
}
```

---

## 4. Related Tools

* [`nova.data_query`](nova-data-query.md) to filter, group and total the data.
* [`nova.convert_to_markdown`](nova-convert-to-markdown.md) to read a small table as text.
