# `nova.docx_create`

> **Writes a Word document from Markdown, without Microsoft Office.**

* **Core Feature Guide:** [Document Conversion](../../../core-features/media-intelligence/document-conversion/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with 1.0.0-alpha.21, which is not published yet.

`nova.docx_create` turns Markdown - the format agents write anyway - into a real Word file (`.docx`). Headings become Word heading styles, so the navigation pane and a table of contents work; bold, italic, strikethrough and code are kept; links become clickable Word links; bullet and numbered lists keep their nesting; quotes, code blocks and tables (with a header row that repeats on every page) are laid out as Word expects. An optional `title` sets the document title, `pageSize` chooses A4 or Letter.

Nova writes the file itself, so nothing else needs to be installed. Images in the Markdown, such as a chart from [`nova.chart_create`](nova-chart-create.md), are embedded when they are local PNG, JPEG, GIF or BMP files. They keep their proportions and are scaled down to fit the page. Images from the web are not downloaded. An image that cannot be embedded keeps its description in the text, and the answer names it with the reason. Raw HTML is kept as plain text.

Without `outputPath` the document goes into Nova's Exports folder; a path of your own choice needs the setting "Allow local files (file://)". An existing file is never overwritten. Before the file gets its name, Nova reads it back once to make sure it opens. Because the tool writes a file, it follows your confirmation setting for saving data permanently.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `markdown` | `string` | No | — | — | The document as Markdown. |
| `sourcePath` | `string` | No | — | — | Absolute path to a Markdown file, instead of markdown. |
| `title` | `string` | No | — | — | Optional document title, shown as the first paragraph. |
| `pageSize` | `string` | No | `"A4"` | `A4`, `Letter` | Page paper size: A4 (default) or Letter. |
| `outputPath` | `string` | No | — | — | Absolute path of the new .docx; must not exist. Needs the user's 'Allow local files' setting. Omit for Nova's Exports folder. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_docx_create",
  "arguments": {
    "title": "Quarterly report",
    "markdown": "## Summary\n\nRevenue rose by **12 %**.\n\n| Product | Revenue |\n|---|---:|\n| Desk | 1,200 |"
  }
}
```

### JSON-RPC Response

```json
{
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "outputPath": "C:\\Users\\me\\AppData\\Local\\NovaBrowser\\Exports\\Office\\Quarterly report-20261016-101500.docx",
    "size": 6214,
    "details": { "headings": 1, "paragraphs": 1, "listItems": 0, "tables": 1, "links": 0 },
    "warnings": []
  }
}
```

---

## 4. Related Tools

* [`nova.xlsx_create`](nova-xlsx-create.md) for spreadsheets.
* [`nova.convert_to_markdown`](nova-convert-to-markdown.md) for the opposite direction.
