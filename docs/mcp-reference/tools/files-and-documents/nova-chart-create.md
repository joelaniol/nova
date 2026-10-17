# `nova.chart_create`

> **Draws a column, bar, line, area, scatter, pie or donut chart from rows of data and saves it as a PNG or SVG file.**

* **Core Feature Guide:** [Tabular Data Analysis](../../../core-features/media-intelligence/data-analysis/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with 1.0.0-alpha.21, which is not published yet.

`nova.chart_create` turns a handful of rows into a finished chart, on your computer and without any extra program. Your agent passes the rows directly or names a CSV, Excel or JSON file. German and English number forms in files are read the same way [`nova.data_query`](nova-data-query.md) reads them.

Which type fits:

| Type | Good for |
| :--- | :--- |
| `column` | Comparing categories, e.g. sales per month |
| `bar` | Rankings and long labels (horizontal; the first row on top) |
| `line` | A development over time or along a number |
| `area` | A development with the amount below it |
| `scatter` | How two numbers relate |
| `pie` / `donut` | Shares of one whole (one series, no negative values) |

The chart shows the data exactly as given. Nothing is invented, added up or sorted:

* a value that is not a number is refused, and the answer names its row;
* an empty cell stays a gap;
* rows keep their order, and the answer warns when categories repeat or dates are out of order.

For larger tables, your agent first sums them up with [`nova.data_query`](nova-data-query.md) and charts the result.

The defaults aim at a chart you can use as it is: colours that people with colour blindness can tell apart, a legend only when there are several series, bars that start at zero, readable labels, and a light or dark theme. The picture is saved as a file in Nova's Exports folder (or a path you name) and is not sent back into the conversation. No existing file is overwritten.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `type` | `string` | Yes | — | `bar`, `column`, `line`, `area`, `scatter`, `pie`, `donut` | — |
| `data` | `array` of `object` | No | — | — | Rows as objects; not with sourcePath. |
| `sourcePath` | `string` | No | — | — | Absolute path to a .csv, .tsv, .xlsx, .xlsm or .json file; not with data. |
| `sheet` | `string` | No | — | — | Excel sheet; default the first visible one. |
| `xKey` | `string` | No | — | — | Category or x column; default the first column. |
| `yKey` | `string` | No | — | — | Value column; default the second column. |
| `series` | `array` of `string` | No | — | — | Several value columns, one series each; replaces yKey. |
| `title` | `string` | No | — | — | — |
| `xLabel` | `string` | No | — | — | Title of the category / x axis. |
| `yLabel` | `string` | No | — | — | Title of the value axis. |
| `width` | `integer` | No | `1200` | 200–4000 | — |
| `height` | `integer` | No | `675` | 150–4000 | — |
| `theme` | `string` | No | `"light"` | `light`, `dark`, `auto` | — |
| `format` | `string` | No | — | `png`, `svg` | Default: from outputPath, else png. |
| `outputPath` | `string` | No | — | — | Absolute path of the new file (.png or .svg). Default: Exports/Charts. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_chart_create",
  "arguments": {
    "type": "column",
    "data": [
      { "month": "Jan", "sales": 12.5, "costs": 9.0 },
      { "month": "Feb", "sales": 14.1, "costs": 10.5 },
      { "month": "Mar", "sales": 16.0, "costs": 11.0 }
    ],
    "xKey": "month",
    "series": ["sales", "costs"],
    "title": "Sales and costs, Q1",
    "yLabel": "thousand EUR"
  }
}
```

### JSON-RPC Response

```json
{
  "structuredContent": {
    "ok": true,
    "outputPath": "C:\\Users\\me\\AppData\\Local\\NovaBrowser\\Exports\\Charts\\Sales and costs, Q1-20261017-101500.png",
    "format": "png",
    "chartType": "column",
    "width": 1200,
    "height": 675,
    "dataPointCount": 6,
    "seriesCount": 2,
    "fileSizeBytes": 19074
  }
}
```

---

## 4. Related Tools

* [`nova.data_query`](nova-data-query.md) sums up, filters and sorts a table before charting.
* [`nova.data_inspect`](nova-data-inspect.md) shows which columns a file has.
