# Local Files, Documents & Archives

Reading and reshaping files that already lie on disk: PDF, Word, Excel, PowerPoint, EPUB, HTML and text as Markdown, CSV/Excel tables with exact totals, PDF page composition, and ZIP/TAR archives.

* **Core Architecture Guide:** [Document Conversion](../../../core-features/media-intelligence/document-conversion/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

<!-- generated:tool-list (from the tool pages in this folder; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
## Tool Inventory (12 Tools)

Capability bundles of these tools: `page_read_debug`, `visual_evidence`.

| Tool | What it does |
| :--- | :--- |
| **[`nova.archive_extract`](nova-archive-extract.md)** | Unpacks a local ZIP or TAR archive of any size, or chosen entries of it, into a new folder - safely, in the background. |
| **[`nova.archive_extract_status`](nova-archive-extract-status.md)** | Reports how far a background extraction of nova.archive_extract has come, or its result. |
| **[`nova.archive_extract_stop`](nova-archive-extract-stop.md)** | Stops a running extraction of nova.archive_extract and removes what it had written. |
| **[`nova.archive_inspect`](nova-archive-inspect.md)** | Lists what a local ZIP or TAR archive holds, without unpacking it. |
| **[`nova.convert_to_markdown`](nova-convert-to-markdown.md)** | Converts a local PDF, Word, Excel, PowerPoint, HTML, CSV, JSON or text file into Markdown for an agent, with an honest account of what was read. |
| **[`nova.data_inspect`](nova-data-inspect.md)** | Shows the columns, types and value ranges of a local CSV or Excel file, before your agent queries it. |
| **[`nova.data_query`](nova-data-query.md)** | Filters, groups and totals a local CSV or Excel file and returns only the result rows. |
| **[`nova.docx_create`](nova-docx-create.md)** | Writes a Word document from Markdown, without Microsoft Office. |
| **[`nova.pdf_compose`](nova-pdf-compose.md)** | Builds one new PDF from pages of local PDFs: merge files, keep or drop pages, change their order. |
| **[`nova.pdf_split`](nova-pdf-split.md)** | Splits a local PDF into several new PDFs, one per page range. |
| **[`nova.read_pdf`](nova-read-pdf.md)** | Extracts the text of a local PDF file, optionally per page and for selected pages only. |
| **[`nova.xlsx_create`](nova-xlsx-create.md)** | Writes an Excel workbook from data or from a CSV file, without Microsoft Office. |
<!-- /generated:tool-list -->

---

## Related Documentation

* [`nova.save_pdf`](../visual-evidence/nova-save-pdf.md) — prints the open page to a PDF; the file tools then read it back
* [`nova.read_text`](../dom-and-reading/nova-read-text.md) — the same Markdown conversion for the live page instead of a file
* [`nova.downloads_list`](../downloads/nova-downloads-list.md) — where downloaded files land before these tools read them
* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
