# `nova.pdf_compose`

> **Builds one new PDF from pages of local PDFs: merge files, keep or drop pages, change their order.**

* **Core Feature Guide:** [PDF Reading, Export & Page Operations](../../../core-features/media-intelligence/pdf/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with 1.0.0-alpha.21, which is not published yet.

`nova.pdf_compose` puts pages of one or more PDF files on disk into a new PDF, in exactly the order you list them. One call covers the usual jobs: merging several invoices into one file, keeping only some pages, removing a page, or moving the last page to the front. Each entry of `sources` takes all pages of its file, or only the pages named in its `pages` (for example `"3,1-2,5"`), in that order.

Without `outputPath` the new PDF goes into Nova's Exports folder; a path of your own choice needs the setting "Allow local files (file://)". An existing file is never overwritten, and the source files are never changed. Because the tool writes a file, it follows your confirmation setting for saving data permanently in Nova's agent permissions.

Page content, images, fonts and links come along. Bookmarks, fillable form fields and digital signatures do not - a signature only ever covers the original file - and the answer names each source where something was left out. Password-protected PDFs are not opened, and files over 50 MB or 2000 pages are refused. Every new PDF is opened again and checked for its page count before it gets its name.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `sources` | `array` of `object` | Yes | — | 1–100 items | The PDFs in the order their pages should appear. |
| `outputPath` | `string` | No | — | — | Absolute path of the new PDF; must not exist. Needs the user's 'Allow local files' setting. Omit for a new file in Nova's Exports folder. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_pdf_compose",
  "arguments": {
    "sources": [
      { "path": "C:\\Users\\me\\Downloads\\invoice-1042.pdf" },
      { "path": "C:\\Users\\me\\Downloads\\invoice-1043.pdf", "pages": "2,1" }
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
    "outputs": [
      { "path": "C:\\Users\\me\\AppData\\Local\\NovaBrowser\\Exports\\Pdf\\invoice-1042-composed-20261016-101500.pdf", "pageCount": 3, "size": 118204 }
    ],
    "sources": [
      { "path": "C:\\Users\\me\\Downloads\\invoice-1042.pdf", "pageCount": 1 },
      { "path": "C:\\Users\\me\\Downloads\\invoice-1043.pdf", "pageCount": 2 }
    ],
    "warnings": []
  }
}
```

---

## 4. Related Tools

* [`nova.pdf_split`](nova-pdf-split.md) to cut one PDF into several.
* [`nova.read_pdf`](nova-read-pdf.md) to check the text of the result.
