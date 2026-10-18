# Document Conversion & Office Generation Architecture

Nova provides a local document transformation and generation engine. It enables autonomous AI agents to convert diverse local document formats into structured Markdown (`nova.convert_to_markdown`) and generate native Microsoft Word (`nova.docx_create`) and Excel (`nova.xlsx_create`) files directly on the operator's computer without Microsoft Office, Python runtimes, or external cloud dependencies.

> [!NOTE]
> **Upcoming.** Document conversion and Office file creation arrive with 1.0.0-alpha.21, which is not published yet. Installed versions up to 1.0.0-alpha.20 do not have them.

---

## Specialized File & Media Subsystems

Nova provides dedicated, granular subsystems for different file types and data tasks. If your task goes beyond document-to-Markdown conversion or Office creation, see:

| Task / Media Type | Specialized Subsystem Guide | MCP Tools |
| :--- | :--- | :--- |
| **Local Images** | [Local Image Intelligence & Processing](../image-processing/README.md) | `nova.image_info`<br/>`nova.image_transform` |
| **QR Codes & Barcodes** | [Local Image Intelligence & Processing](../image-processing/README.md#5-qr-codes--barcodes) | `nova.barcode_generate`<br/>`nova.barcode_decode` |
| **Scans, Receipts & Photos** | [Offline Optical Character Recognition (OCR)](../ocr/README.md) | `nova.ocr_read` |
| **Tabular Data & Queries** | [Tabular Data Analysis & Streaming Queries](../data-analysis/README.md) | `nova.data_inspect`<br/>`nova.data_query` |
| **PDF Page Manipulation** | [PDF Reading, Export & Page Operations](../pdf/README.md) | `nova.pdf_compose`<br/>`nova.pdf_split`<br/>`nova.read_pdf`<br/>`nova.save_pdf` |
| **Archives & Backups** | [Archive Inspection & Secure Extraction](../archives/README.md) | `nova.archive_inspect`<br/>`nova.archive_extract*` |

---

## 1. What You Can Ask Your Agent

* "Read the contract I just downloaded and list every clause regarding cancellation."
* "Convert the quarterly sales presentation slide by slide, including speaker notes."
* "Turn this Word document into Markdown and save it as a `.md` file in my project folder."
* "Check whether the financial PDF mentions currency adjustments. If the text layout is fragmented, inspect the rendered page image."
* "Create an executive summary Word document (`.docx`) from your analysis with styled headings and tables."
* "Export these query results into an Excel spreadsheet (`.xlsx`) with formatted headers, auto-fitting column widths, and filter buttons."

---

## 2. Supported Conversion Formats (`nova.convert_to_markdown`)

| Format | Extensions | Recognition Mechanism | Extracted Structural Traits | Format Identifier |
| :--- | :--- | :--- | :--- | :--- |
| **PDF** | `.pdf` | Magic Bytes (`%PDF-`) | Reading order reconstruction (RecursiveXYCut), document outline bookmarks as headings, AcroForm fields, Markdown tables, column alignment, page-selective rendering (`renderPages`) | `pdf` |
| **Word** | `.docx`, `.docm`, `.dotx` | Magic Bytes (ZIP + `word/`) | Semantic headings (`heading 1`–`6`, `Title`), nested numbered and bulleted lists, tables with cell spans, footnotes and endnotes, tracked revisions (`w:ins` kept, `w:del` omitted) | `docx` |
| **Excel** | `.xlsx`, `.xlsm`, `.xltx` | Magic Bytes (ZIP + `xl/`) | One Markdown table per worksheet, stored cell values, ISO-formatted dates, hidden sheets/rows/columns counted and extracted | `xlsx` |
| **PowerPoint** | `.pptx`, `.pptm`, `.ppsx` | Magic Bytes (ZIP + `ppt/`) | One section per slide (`## Slide N: <Title>`), shapes in presentation order, speaker notes as blockquotes (`**Notes:**`), tables | `pptx` |
| **HTML** | `.html`, `.htm`, `.xhtml` | Content signature or name | Headings (`h1`–`h6`), lists, tables (`colspan`), code blocks with language tags, blockquotes, inline formatting, link resolution against `<base href>` | `html` |
| **EPUB** | `.epub` | Magic Bytes (`mimetype`) | Chapters in package spine reading order, embedded XHTML chapters converted via HTML rules, Dublin Core book metadata | `epub` |
| **CSV / TSV** | `.csv`, `.tsv` | Extension & delimiter probe | Formatted Markdown table, automatic delimiter detection (comma, semicolon, tab, pipe), RFC 4180 quoting | `csv` |
| **JSON** | `.json` | Extension & syntax parser | Neatly indented and validated JSON code block | `json` |
| **Plain Text** | `.txt`, `.text`, `.log` | Extension | Verbatim text within code block with normalized line endings | `text` |
| **Image** | `.png`, `.jpg`, `.tif`, `.bmp`, `.gif`, `.webp` | File signature | Text recognised offline by OCR, each page marked as recognised | `image` |

PDF, Word, Excel, PowerPoint, HTML, and EPUB files are recognized by **content magic bytes**, ensuring files with misleading, incorrect, or omitted extensions are correctly decoded.

> [!NOTE]
> `nova.convert_to_markdown` processes digital document streams. Scanned image-only PDFs or photographs lacking a digital text layer should be routed to [Offline OCR (`nova.ocr_read`)](../ocr/README.md).

---

## 3. Structural Fidelity & Verification Features

### Truthful Document Layouts
* **No Speculative Formatting:** Headings and lists appear only where the document explicitly defines them in its style sheet or outline tree. Visual styling such as bold text is never promoted to a heading.
* **Layout Fallback Notifications:** In complex PDF layouts, if reading order heuristics require fallback, Nova emits structured warnings (`layout_fallback_used`, `table_structure_not_preserved`).
* **Visual Page Verification (`renderPages`):** For ambiguous PDF pages, agents can request up to 3 rendered JPEG page images in memory to visually verify fragmented forms or misaligned columns against what a human would see.

### Hidden Content Discovery (`hiddenText`)
Adversarial documents and prompt injection attacks often hide text from human viewers while exposing it to AI scrapers. Nova explicitly surfaces hidden content across formats:
* **Word & HTML:** Extracted from elements styled with `display: none`, `visibility: hidden`, `hidden`, or Word `w:vanish`.
* **Excel:** Identifies hidden worksheets, hidden rows, and hidden columns.
* **PowerPoint:** Identifies hidden slides and hidden shapes.
* **PDF:** Surfaces non-painting glyphs (rendering modes `Neither`/`NeitherClip`) and text placed outside page crop boxes.
* All hidden strings are returned in structured field `hiddenText` alongside standard Markdown.

### Untrusted Content Invariant
Every response carries `contentTrust: "untrusted_document"`. AI agents are instructed by schema descriptions to treat document text strictly as passive data rather than executable instructions.

---

## 4. Creating Word and Excel Documents

Nova includes built-in native writers for Microsoft Office documents:

### Word Document Creation (`nova.docx_create`)
* Generates standard `.docx` files directly from agent-generated Markdown.
* Formats native Word heading styles, bold/italic/strikethrough text, bulleted lists, numbered lists (preserving start indices), blockquotes, code blocks, and pipe tables with repeated bold header rows.
* Supports paper dimensions (`A4` or `Letter`) and metadata titles.
* Executes with zero dependency on Microsoft Office or heavy third-party SDKs.

### Excel Workbook Creation (`nova.xlsx_create`)
* Generates native `.xlsx` workbooks from structured JSON table data or from local CSV/TSV sources.
* Supports typed column formats: `general`, `text`, `integer`, `decimal`, `currency`, `percent`, `date`, `datetime`.
* Auto-formatting: Automatically configures frozen header rows, auto-filter dropdowns, and calculates proportional column widths based on cell content.
* Formula Safety Invariant: Raw text beginning with `=` is preserved as an inline string, completely preventing formula injection attacks. Formulas are only written when explicitly declared in a `{ formula: "..." }` cell descriptor.

---

## Tool Reference Matrix

| Tool | Capability Bundle | Primary Role | Key Parameters |
| :--- | :--- | :--- | :--- |
| [`nova.convert_to_markdown`](../../../mcp-reference/tools/files-and-documents/nova-convert-to-markdown.md) | `page_read_debug` | Converts local documents, spreadsheets, slides, and tables into structured Markdown | `path`, `pages?`, `outputMode?`, `outputPath?`, `maxChars?`, `renderPages?`, `includeFormValues?` |
| [`nova.docx_create`](../../../mcp-reference/tools/files-and-documents/nova-docx-create.md) | `page_read_debug` | Generates a native Microsoft Word document from Markdown | `markdown?`, `sourcePath?`, `title?`, `pageSize?`, `outputPath?` |
| [`nova.xlsx_create`](../../../mcp-reference/tools/files-and-documents/nova-xlsx-create.md) | `page_read_debug` | Generates a native Microsoft Excel workbook from tabular data or CSV | `sheets?`, `sourcePath?`, `sheet?`, `sheetName?`, `autoFormat?`, `currencySymbol?`, `outputPath?` |

---

[Media Intelligence overview](../README.md) · [Local Image Processing](../image-processing/README.md) · [Offline OCR](../ocr/README.md) · [Tabular Data Analysis](../data-analysis/README.md) · [PDF Reading, Export & Page Operations](../pdf/README.md) · [Archive Inspection & Extraction](../archives/README.md) · [All core features](../../README.md)
