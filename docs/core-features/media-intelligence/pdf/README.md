# PDF Reading, Export & Page Operations Architecture

Nova provides comprehensive PDF document intelligence through four complementary operations: extracting structured digital text from existing PDF files on disk (`nova.read_pdf`), generating pixel-accurate vector PDF documents from active web pages using Chromium's DevTools print engine (`nova.save_pdf`), assembling custom documents from page subsets (`nova.pdf_compose`), and partitioning documents into separate files (`nova.pdf_split`).

It bridges automated document processing for AI agents with a native, hardware-accelerated WinUI 3 PDF viewing surface for human operators.

> [!TIP]
> To read a PDF as structured Markdown - with page markers, headings from its bookmarks, links, and page images for checking - and to read Word, Excel, PowerPoint, and other files the same way, see [Document Conversion](../document-conversion/README.md). `nova.read_pdf` stays the tool for the exact continuous text of a PDF. For scanned bitmaps without a digital text layer, see [Offline OCR](../ocr/README.md).

```mermaid
flowchart TD
    subgraph ReadPath["1. Digital PDF Text Extraction (nova.read_pdf)"]
        LocalFile["PDF File on Disk\n(Downloads, Exports, or Permitted Path)"]
        RangeFilter["Page Range Parser\n(e.g. '1', '2-5', '1,3-6,9', 'all')"]
        PdfPigParser["UglyToad.PdfPig Managed Parser\n(Glyph & Document Layout Extraction)"]
        TokenBudget["Token Budget Guard\n(maxChars Clamping: 1,000 - 2,000,000)"]
        StructuredText["Structured Extraction Output\n(pageCount, pagesRead, text, truncated)"]
    end

    subgraph SavePath["2. Webpage Print-to-PDF Export (nova.save_pdf)"]
        ActiveDOM["Active Webpage DOM & Styles\n(@media print Stylesheets)"]
        CrashGuard["Renderer Crash Guard\n(generateTaggedPDF: false Pinned Default)"]
        CDPPrint["DevTools Page.printToPDF Pipeline\n(Margins, Paper Format, Scale, Backgrounds)"]
        DiskWriter["Reference-Based Disk Writer\n(Writes to Exports or Gated savePath)"]
        PathResult["Verified Disk Path Return\n(Zero Base64 Context Bloat)"]
    end

    subgraph PageOpsPath["3. PDF Composition & Splitting (nova.pdf_compose & nova.pdf_split)"]
        SourcePdfs["One or More Source PDFs\n(sources: [{path, pages}])"]
        DocBuilder["PdfDocumentBuilder Engine\n(AddPage Sequencing & In-Memory Verification)"]
        PartCommit["Atomic Part-File Commit\n(Zero Overwrites, Source Files Immutable)"]
        NewPdfs["Composed or Partitioned PDF Assets\n(Preserves Vector Paths, Fonts, Images)"]
    end

    subgraph ViewerPath["4. Embedded WinUI 3 Human Viewer"]
        NativeViewer["Native WinUI 3 PDF Viewer Toolbar"]
        RenderSurface["Hardware-Accelerated PDF Page Surface"]
        KeyHook["Keyboard & Zoom Hooks (PgUp, PgDn, Ctrl+Wheel)"]
    end

    LocalFile --> RangeFilter --> PdfPigParser --> TokenBudget --> StructuredText
    ActiveDOM --> CrashGuard --> CDPPrint --> DiskWriter --> PathResult
    SourcePdfs --> DocBuilder --> PartCommit --> NewPdfs
    LocalFile -.-> NativeViewer --> RenderSurface --> KeyHook
```

---

## 1. Webpage PDF Export (`nova.save_pdf`)

`nova.save_pdf` renders the active web tab into an archival vector PDF document on disk using Chromium's `Page.printToPDF` protocol. It provides granular typographic, page dimension, and styling controls:

```mermaid
sequenceDiagram
    participant Agent as Autonomous Agent
    participant Nova as Nova MCP Document Handler
    participant Chromium as Chromium DevTools Pipeline
    participant Disk as Local Storage (StoragePaths.ExportsDir)

    Agent->>Nova: nova.save_pdf(targetId="active", printBackground=true, preferCSSPageSize=true)
    Note over Nova: Pre-flight validation & path gating
    Nova->>Chromium: Page.printToPDF(generateTaggedPDF=false, ...)
    Chromium->>Chromium: Renders @media print CSS layout
    Chromium-->>Nova: Binary PDF stream
    Nova->>Disk: Writes "Export_20261010_123456.pdf"
    Nova-->>Agent: { savedPath: "C:/.../Export_20261010_123456.pdf", pages: 3, bytes: 245100 }
```

### The `generateTaggedPDF: false` Renderer Crash Guard

A critical architectural invariant in Nova's PDF printing pipeline is the explicit deactivation of tagged PDF generation:

```json
{
  "generateTaggedPDF": false
}
```

* **The Underlying Chromium Bug:** In Chromium and WebView2, generating an accessible, tagged PDF forces the renderer to take an internal accessibility snapshot:
  $$\text{PrintWithParams} \longrightarrow \text{PrintPagesNative} \longrightarrow \text{SnapshotAccessibilityTree} \longrightarrow \text{SerializeEntireTreeAndDispose}$$
  On complex webpages containing deeply nested dynamic DOM structures or malformed ARIA trees (first observed on Roundcube webmail, WebView2 151.0.4129.101), this code path triggers an unrecoverable internal Chromium `CHECK` assertion failure (`int 3`).
* **The Failure Mode:** When the assertion fails, the entire WebView render process crashes mid-call. The browser tab goes blank, Nova must rebuild the tab's WebView controller, and no PDF file is generated.
* **The Safe Invariant:** Untagged PDF export takes the exact same typographic layout, font embedding, and vector rendering path while bypassing the accessibility tree snapshot. By pinning `generateTaggedPDF: false` by default, Nova eliminates the renderer crash risk entirely while preserving 100% visual fidelity and selectable text.

### Layout & Page Parameters

* **`printBackground` (Default: `true`):** Renders CSS background colors, gradients, and images. Essential for generating authentic receipts, invoices, data dashboards, and charts.
* **`preferCSSPageSize` (Default: `true`):** Prioritizes `@page` rules declared within the website's print stylesheet over tool parameters, ensuring layouts intended for specific book or invoice dimensions render as designed.
* **`landscape` (Default: `false`):** Toggles orientation between portrait (`false`) and landscape (`true`).
* **`scale` (Range: `0.1` to `2.0`, Default: `1.0`):** Scales page content uniformly, preventing wide tables or fixed layouts from truncating.
* **Paper Sizing (`paperWidth` & `paperHeight`):** Explicit paper dimensions in inches (e.g. `8.27` $\times$ `11.69` for A4, `8.5` $\times$ `11.0` for US Letter).
* **Granular Margins (`marginTop`, `marginBottom`, `marginLeft`, `marginRight`):** Independent margin offsets in inches.
* **`pageRanges`:** Selective printing of specific pages (e.g. `'1-3'`, `'1,5'`).
* **`displayHeaderFooter` (Default: `false`):** Injects standard browser headers (current date, page title) and footers (page number, source URL). Kept disabled by default for clean archival exports.

### Reference-Based Delivery Invariant

A single rendered PDF frequently exceeds several megabytes in size. Encoding this binary stream into a JSON-RPC response via base64 would immediately consume hundreds of thousands of context tokens and risk blowing MCP client message limits.

Nova strictly enforces **reference-based delivery**:
1. The rendered PDF is written directly to disk.
2. Nova writes by default to `StoragePaths.ExportsDir`, requiring no elevated permissions.
3. The MCP tool returns a compact JSON envelope containing the verified absolute path (`savedPath`), total page count (`pages`), and file size (`bytes`).

---

## 2. Digital PDF Text Extraction (`nova.read_pdf`)

`nova.read_pdf` extracts selectable digital text from PDF documents stored locally on disk. It closes the verification loop for agents: an agent can save a webpage to PDF or download an invoice, and immediately read back its contents to confirm that key data (such as invoice numbers, dollar amounts, or cancellation notices) are present.

### Managed Parsing Engine (`UglyToad.PdfPig`)

Nova utilizes the managed, high-performance `UglyToad.PdfPig` engine for digital PDF parsing:
* **Zero External Dependencies:** Executes entirely within Nova's managed process without requiring external command-line utilities (such as `pdftotext` or Poppler).
* **Glyph & Layout Analysis:** Reconstructs natural reading order across multi-column text layouts, tables, and headers.
* **Page-Selective Parsing:** When specific page ranges are requested, only the target pages are loaded and tokenized, minimizing CPU and memory consumption on large documents.

### Page Selection Syntax

Agents can target specific sections of a document to conserve context tokens:
* Single page: `"1"`
* Disjoint pages: `"1,4,8"`
* Continuous range: `"2-5"`
* Mixed selection: `"1,3-6,9"`
* All pages: Omit the argument or pass `"all"`.

### Token Budget Guard (`maxChars`)

To protect LLM context windows from overflowing when processing large legal filings or technical manuals:
* **Default Budget:** 50,000 characters.
* **Configurable Range:** Clamped between `1,000` and `2,000,000` characters.
* **Truncation Flag:** If the extracted text reaches the limit, Nova halts further extraction and sets `truncated: true` alongside structured decision metadata (`McpOutputBudget`), alerting the agent to narrow its query with specific `pageRanges`.

### Diagnostic Codes & Outcomes

| Result Code | Status | Meaning & Recommended Agent Action |
| :--- | :--- | :--- |
| **`ok`** | `"ok"` | Extraction succeeded. Returns `text`, `pageCount`, and `pagesRead` array. |
| **`read_pdf.not_found`** | `"not_found"` | File does not exist at the specified path. Check download progress via `nova.downloads_wait` before reading. |
| **`read_pdf.encrypted`** | `"blocked"` | The document is protected by an owner or user password. Nova does not store or prompt for PDF passwords. |
| **`read_pdf.no_extractable_text`** | `"empty"` | The document parsed successfully, but contains zero digital text streams. The document is a rasterized scan or flattened bitmap. Use [Offline OCR (`nova.ocr_read`)](../ocr/README.md) to read it. |
| **`read_pdf.unreadable`** | `"error"` | File header or structure is corrupted, incomplete, or not a valid PDF. |

> [!NOTE]
> `nova.read_pdf` is a pure digital text extractor. It does not perform Optical Character Recognition (OCR) on scanned bitmaps. For scanned PDFs or photographic documents without a text layer, use [Offline OCR (`nova.ocr_read`)](../ocr/README.md).

---

## 3. PDF Page Composition & Splitting (`nova.pdf_compose` & `nova.pdf_split`)

> [!NOTE]
> **Upcoming.** Native PDF composition and splitting arrive with 1.0.0-alpha.21, which is not published yet. Installed versions up to 1.0.0-alpha.20 do not have them.

Agents frequently need to reorganize PDF files: combine multiple monthly invoices into a single report, remove unnecessary cover pages, or extract specific page ranges for external submission. Nova handles these operations locally using its integrated PDF page engine:

### Composing Documents (`nova.pdf_compose`)
* **Flexible Page Sequencing:** Assembles a new PDF from pages of one or more source files in exact requested sequence:
  ```json
  {
    "name": "nova_pdf_compose",
    "arguments": {
      "sources": [
        { "path": "C:\\Docs\\Cover.pdf", "pages": "1" },
        { "path": "C:\\Docs\\Report.pdf", "pages": "2-5" },
        { "path": "C:\\Docs\\Appendix.pdf" }
      ]
    }
  }
  ```
* Pages can be reordered, repeated, or omitted.
* High fidelity: Preserves original font programs, vector paths, high-resolution bitmap assets, and interactive link annotations.
* Transparency on dynamic elements: Bookmarks, fillable AcroForm fields, and digital signatures are not carried into merged files; Nova issues structured warnings (`bookmarks_not_kept`, `form_fields_not_kept`, `signatures_not_kept`) so agents understand the outcome.

### Splitting Documents (`nova.pdf_split`)
* Partitions a multi-page PDF into discrete files based on specified page ranges:
  ```json
  {
    "name": "nova_pdf_split",
    "arguments": {
      "path": "C:\\Docs\\QuarterlyBilling.pdf",
      "ranges": ["1-3", "4-7", "8-12"]
    }
  }
  ```
* Generates sequentially numbered files (`QuarterlyBilling_part01.pdf`, `QuarterlyBilling_part02.pdf`, etc.) in the destination directory.

### Atomic Verification & Integrity Guarantees
1. Nova builds the new document entirely in memory via `PdfDocumentBuilder`.
2. It writes to a temporary `.part` file in the destination folder.
3. It re-opens the generated file from disk and verifies that the written page count matches the requested page count.
4. Only upon successful verification is the file atomically committed to its final name.
5. If an error occurs, all partial files generated during that call are removed immediately.
6. Existing files are never overwritten (`output_exists`). Source files remain strictly read-only and immutable.

---

## 4. Filesystem Sandboxing & Policy Gating

Access to local PDF files is governed by Nova's path security policy:

* **Automatic Consent:** PDF files residing in Nova's default `Downloads` and `Exports` directories are accessible immediately without friction.
* **Custom Paths & Hard Drive Access:** Reading files from arbitrary local paths or exporting to a custom `savePath` or `outputPath` requires the user setting **"Allow local files (file://)"**. If disabled, requests fail immediately with:
  ```json
  {
    "code": -32035,
    "message": "Tool blocked by policy: accessing a custom path requires local file access.",
    "data": { "reasonCode": "mcp.file_access_disabled" }
  }
  ```
* **Early Path Validation:** Tools validate destination paths before executing render or composition pipelines, ensuring invalid paths fail fast before consuming CPU and layout compute.

---

## 5. Embedded WinUI 3 PDF Viewer

For human operators, Nova embeds a native WinUI 3 PDF viewing surface directly inside browser tabs:
* **Hardware-Accelerated Zooming:** Smooth page zooming managed via `PdfViewerZoom`.
* **Keyboard Navigation:** Full support for `Page Up`, `Page Down`, `Home`, `End`, and `Ctrl + Wheel` zooming hooks (`PdfZoomKeyboardHook`).
* **Interactive PDF Toolbar:** Built-in WinUI 3 toolbar (`PdfToolbar`) providing single-click page navigation, zoom presets (fit-to-width, fit-to-page), and native printing.

---

## Tool Reference Matrix

| Tool | Capability Bundle | Primary Role | Key Parameters |
| :--- | :--- | :--- | :--- |
| [`nova.save_pdf`](../../../mcp-reference/tools/visual-evidence/nova-save-pdf.md) | `visual_evidence` | Vector PDF print export from active browser tabs | `targetId?`, `savePath?`, `printBackground?`, `preferCSSPageSize?`, `landscape?`, `scale?`, `pageRanges?` |
| [`nova.read_pdf`](../../../mcp-reference/tools/files-and-documents/nova-read-pdf.md) | `page_read_debug`, `visual_evidence` | Exact digital text extraction and token-bounded reading | `path`, `pages?`, `maxChars?`, `includePages?` |
| [`nova.pdf_compose`](../../../mcp-reference/tools/files-and-documents/nova-pdf-compose.md) | `page_read_debug` | Assembles a new PDF from page subsets of one or more local PDFs | `sources`, `outputPath?` |
| [`nova.pdf_split`](../../../mcp-reference/tools/files-and-documents/nova-pdf-split.md) | `page_read_debug` | Partitions a PDF into multiple documents by page ranges | `path`, `ranges`, `outputDir?` |

---

[Media Intelligence overview](../README.md) · [WinUI 3 Image Viewer](../image-viewer/README.md) · [Offline OCR](../ocr/README.md) · [Local Image Processing](../image-processing/README.md) · [Document Conversion](../document-conversion/README.md) · [All core features](../../README.md)
