# PDF Composition, Splitting & Embedded Viewer

> [!NOTE]
> Autonomous document workflows often require combining multiple PDF exhibits into a single submission, or splitting a multi-invoice bundle into separate files. **Nova AI Workspace** implements programmatic composition (`nova.pdf_compose`), selective partitioning (`nova.pdf_split`), and an embedded hardware-accelerated WinUI 3 PDF viewing surface.

---

## 1. Multi-Source PDF Composition (`nova.pdf_compose`)

`nova.pdf_compose` merges selected pages from one or more local PDF documents into a newly synthesized document:

```mermaid
flowchart TD
    SourceA["Source PDF A\n(e.g. Contract.pdf, pages 1-2)"] --> Builder["PdfDocumentBuilder Engine\n(In-Memory Sequence Validation)"]
    SourceB["Source PDF B\n(e.g. Addendum.pdf, pages 4-5)"] --> Builder
    SourceC["Source PDF C\n(e.g. Signature.pdf, page 1)"] --> Builder

    Builder --> PartFile["Atomic Temporary File (.part)\n(Page Validation & Geometry Check)"]
    PartFile --> FinalPdf["Final Composed Document\n(output.pdf)"]
```

### JSON-RPC Example

```json
{
  "name": "nova_pdf_compose",
  "arguments": {
    "sources": [
      { "path": "C:\\Docs\\Executive_Summary.pdf", "pages": "1-3" },
      { "path": "C:\\Docs\\Financial_Exhibits.pdf", "pages": "12-15" },
      { "path": "C:\\Docs\\Signature_Page.pdf", "pages": "1" }
    ],
    "outputPath": "C:\\Docs\\Board_Submission.pdf"
  }
}
```

### Key Architectural Invariants

* **Lossless Vector Preservation:** Vector artwork, embedded TrueType/OpenType fonts, transparency layers, and high-resolution images are preserved without lossy rasterization.
* **Source Immutability:** Input PDF files are opened in read-only shared mode (`FileShare.Read`). Nova never modifies source files.
* **Atomic Part-File Commit:** Nova writes bytes to an ephemeral `.part` file, verifies structural integrity, and renames it to the destination path in a single atomic filesystem operation.

---

## 2. Document Partitioning (`nova.pdf_split`)

`nova.pdf_split` decomposes a single multi-page PDF into discrete documents based on page ranges:

```mermaid
flowchart LR
    Source["Multi-Page Bundle\n(Bundle_100Pages.pdf)"] --> Splitter["nova.pdf_split\nranges: ['1-10', '11-30', '31-100']"]
    Splitter --> Out1["Part_1_pages_1-10.pdf"]
    Splitter --> Out2["Part_2_pages_11-30.pdf"]
    Splitter --> Out3["Part_3_pages_31-100.pdf"]
```

### Protocol Parameters

* **`path`:** Absolute path to the source PDF document.
* **`ranges`:** Array of page range strings (e.g. `["1-5", "6-10", "11"]`).
* **`outputDir`:** Destination directory for partitioned PDF files.

---

## 3. Embedded WinUI 3 Human PDF Viewer

In addition to headless agent automation, Nova features a native WinUI 3 PDF viewer for human operators:

```mermaid
flowchart TD
    PdfFile["Local PDF Asset"] --> ViewerSurface["Hardware-Accelerated Direct2D Page Surface"]
    ViewerSurface --> Toolbar["Navigation Toolbar\n(Page Counter, Fit Width, Fit Page, Rotate)"]
    ViewerSurface --> KeyHooks["Keyboard Navigation\n(PgUp, PgDn, Home, End, Ctrl+Wheel Zoom)"]
```

### Viewer Capabilities

* **Hardware-Accelerated Direct2D Rendering:** Smooth scrolling across high-DPI displays with sub-pixel text anti-aliasing.
* **Keyboard Navigation:** Full hotkey support for rapid page navigation (`PageUp`, `PageDown`, `Home`, `End`).
* **Interactive Zoom:** Smooth continuous zoom with `Ctrl + MouseWheel` or toolbar presets (`Fit Width`, `Fit Page`, `100%`).

---

## 4. Related Documentation

* [PDF Reading, Export & Page Operations Overview](../README.md)
* [Webpage Print Pipeline & Crash Guards](../print-pipeline-and-crash-guard/README.md)
* [Digital Text Extraction & Page Range Parsing](../text-extraction-and-range-parsing/README.md)
* [PDF Compose Tool Reference](../../../../mcp-reference/tools/files-and-documents/nova-pdf-compose.md)
* [PDF Split Tool Reference](../../../../mcp-reference/tools/files-and-documents/nova-pdf-split.md)
