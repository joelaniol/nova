# `nova.pdf_split`

> **Splits a local PDF into several new PDFs, one per page range.**

* **Core Feature Guide:** [PDF Reading, Export & Page Operations](../../../core-features/media-intelligence/pdf/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with 1.0.0-alpha.21, which is not published yet.

`nova.pdf_split` cuts a PDF on disk into several new files. `ranges` lists one page selection per new file, for example `["1-3", "4-8", "9-12"]`, or `["1", "2", "3"]` for one file per page. The files are numbered in that order: `<name>_part01.pdf`, `<name>_part02.pdf`, and so on.

Without `outputDir` they go into a new folder in Nova's Exports folder; a folder of your own choice needs the setting "Allow local files (file://)". If any of the target files already exists, nothing is written at all, and the source file is never changed. If something fails halfway, the files this call had already written are removed again.

As with [`nova.pdf_compose`](nova-pdf-compose.md), page content, images, fonts and links come along, while bookmarks, form fields and digital signatures do not; the answer says when the source had any.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `path` | `string` | Yes | — | — | Absolute path to the PDF, e.g. the filePath from nova.downloads_list. |
| `ranges` | `array` of `string` | Yes | — | 1–500 items | One page selection per new PDF, e.g. ['1-3', '4-8']. |
| `outputDir` | `string` | No | — | — | Absolute folder for the new PDFs. Needs the user's 'Allow local files' setting. Omit for a new folder in Nova's Exports folder. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_pdf_split",
  "arguments": {
    "path": "C:\\Users\\me\\Downloads\\report.pdf",
    "ranges": ["1-3", "4-8"]
  }
}
```

### JSON-RPC Response

```json
{
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "outputs": [
      { "path": "C:\\Users\\me\\AppData\\Local\\NovaBrowser\\Exports\\Pdf\\report-split-20261016-101500\\report_part01.pdf", "pageCount": 3, "size": 61840 },
      { "path": "C:\\Users\\me\\AppData\\Local\\NovaBrowser\\Exports\\Pdf\\report-split-20261016-101500\\report_part02.pdf", "pageCount": 5, "size": 90122 }
    ],
    "sources": [
      { "path": "C:\\Users\\me\\Downloads\\report.pdf", "pageCount": 8 }
    ],
    "warnings": [
      { "code": "bookmarks_not_kept", "source": "report.pdf", "detail": "The source has bookmarks (an outline); the new PDF has none." }
    ]
  }
}
```

---

## 4. Related Tools

* [`nova.pdf_compose`](nova-pdf-compose.md) to merge or reorder pages.
* [`nova.convert_to_markdown`](nova-convert-to-markdown.md) to read one of the parts.
