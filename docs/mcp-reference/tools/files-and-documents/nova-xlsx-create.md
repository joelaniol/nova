# `nova.xlsx_create`

> **Writes an Excel workbook from data or from a CSV file, without Microsoft Office.**

* **Core Feature Guide:** [Document Conversion](../../../core-features/media-intelligence/document-conversion/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with 1.0.0-alpha.21, which is not published yet.

`nova.xlsx_create` builds a real Excel file (`.xlsx`). Your agent either passes the data directly - one or more sheets with column names and rows - or points at a CSV, TSV or Excel file, which becomes one sheet. Columns can carry a format: whole numbers, decimals, currency, percent, date or date and time.

Numbers stay numbers and dates become real Excel dates, so they can be sorted, filtered and summed in Excel straight away. From a CSV file, German and English number formats are both understood, as with [`nova.data_inspect`](nova-data-inspect.md). Text always stays text: a value that starts with `=` is never turned into a formula. A formula is only written when the agent asks for one explicitly, and Excel calculates it when the file opens.

With `autoFormat` (on by default) the header row is bold and stays visible while scrolling, every column gets filter buttons, and column widths fit their content. Large CSV files are written piece by piece; Excel's own limits apply (about one million rows per sheet).

Without `outputPath` the workbook goes into Nova's Exports folder; a path of your own choice needs "Allow local files (file://)". An existing file is never overwritten, and Nova reads the workbook back once before it gets its name.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `sheets` | `array` of `object` | No | — | — | The workbook's sheets with their data. |
| `sourcePath` | `string` | No | — | — | Absolute path to a .csv, .tsv, .xlsx or .xlsm file, instead of sheets. |
| `sheet` | `string` | No | — | — | With an Excel sourcePath: the input sheet; default the first visible one. |
| `sheetName` | `string` | No | — | — | With sourcePath: the name of the output sheet; default the file name. |
| `autoFormat` | `boolean` | No | `true` | — | — |
| `currencySymbol` | `string` | No | `"\u20AC"` | — | — |
| `openInTab` | `boolean` | No | `false` | — | After writing, show the workbook in Nova's read-only table view in a new active tab; the result gains openedInTab {opened, targetId, reasonCode}. |
| `fitToData` | `boolean` | No | `false` | — | With openInTab: once loaded, zoom the tab (Nova's own page zoom, session only, 100 % to 200 %) so the used cells fill the window, keeping two empty columns and rows of grid around them - for screenshots and recordings of small tables. |
| `outputPath` | `string` | No | — | — | Absolute path of the new .xlsx; must not exist. Needs the user's 'Allow local files' setting. Omit for Nova's Exports folder. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_xlsx_create",
  "arguments": {
    "sheets": [
      {
        "name": "Revenue",
        "columns": ["Product", { "name": "Amount", "format": "currency" }, { "name": "Date", "format": "date" }],
        "rows": [
          ["Desk", 1200.5, "2026-09-30"],
          ["Chair", 99.5, "2026-09-30"],
          ["Total", { "formula": "SUM(B2:B3)" }, null]
        ]
      }
    ]
  }
}
```

### JSON-RPC Response

```json
{
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "outputPath": "C:\\Users\\me\\AppData\\Local\\NovaBrowser\\Exports\\Office\\Revenue-20261016-101500.xlsx",
    "size": 3870,
    "details": { "sheets": [ { "name": "Revenue", "rows": 3, "columns": 3 } ] },
    "warnings": []
  }
}
```

---

## 4. Related Tools

* [`nova.data_query`](nova-data-query.md) to compute the numbers first.
* [`nova.docx_create`](nova-docx-create.md) for a written report.
