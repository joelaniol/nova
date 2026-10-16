# Visual Evidence, Screenshots & Archiving

Lossless cropped screenshots, pixel-by-pixel diffing, persistent baselines, and print-to-PDF generation.

* **Core Architecture Guide:** [Evidence Verification Mode (EVM) & Visual Evidence](../../../research/evidence-verification-mode-evm/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

<!-- generated:tool-list (from the tool pages in this folder; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
## Tool Inventory (16 Tools)

Capability bundles of these tools: `app_shell_recovery`, `browser_automation`, `device_emulation`, `form_submission`, `page_read_debug`, `system_tools`, `visual_evidence`.

| Tool | What it does |
| :--- | :--- |
| **[`nova.archive_extract`](nova-archive-extract.md)** | Unpacks a local ZIP or TAR archive of any size, or chosen entries of it, into a new folder - safely, in the background. |
| **[`nova.archive_extract_status`](nova-archive-extract-status.md)** | Reports how far a background extraction of nova.archive_extract has come, or its result. |
| **[`nova.archive_extract_stop`](nova-archive-extract-stop.md)** | Stops a running extraction of nova.archive_extract and removes what it had written. |
| **[`nova.archive_inspect`](nova-archive-inspect.md)** | Lists what a local ZIP or TAR archive holds, without unpacking it. |
| **[`nova.capture_app_screenshot`](nova-capture-app-screenshot.md)** | Captures the Nova app window (tabs, topbar, WebView content) — or, if another agent holds the active tab's claim, a read-only redacted shell view with page content masked out. |
| **[`nova.capture_screenshot`](nova-capture-screenshot.md)** | Captures visual screenshot evidence of the active page, a specific DOM element, or a bounded pixel region, with support for cryptographic SHA-256 hashing, visual callout highlights, and token-saving delivery modes. |
| **[`nova.convert_to_markdown`](nova-convert-to-markdown.md)** | Converts a local PDF, Word, Excel, PowerPoint, HTML, CSV, JSON or text file into Markdown for an agent, with an honest account of what was read. |
| **[`nova.data_inspect`](nova-data-inspect.md)** | Shows the columns, types and value ranges of a local CSV or Excel file, before your agent queries it. |
| **[`nova.data_query`](nova-data-query.md)** | Filters, groups and totals a local CSV or Excel file and returns only the result rows. |
| **[`nova.pdf_compose`](nova-pdf-compose.md)** | Builds one new PDF from pages of local PDFs: merge files, keep or drop pages, change their order. |
| **[`nova.pdf_split`](nova-pdf-split.md)** | Splits a local PDF into several new PDFs, one per page range. |
| **[`nova.read_pdf`](nova-read-pdf.md)** | Extracts the text of a local PDF file, optionally per page and for selected pages only. |
| **[`nova.responsive_screenshots`](nova-responsive-screenshots.md)** | Sweeps multiple viewport widths one at a time, capturing a screenshot at each and restoring the tab's original viewport afterwards. |
| **[`nova.save_pdf`](nova-save-pdf.md)** | Renders the active web page to a vector PDF document on disk via Chrome DevTools Protocol (`Page.printToPDF`), providing zero-token document archiving and export capabilities. |
| **[`nova.screenshot_baseline`](nova-screenshot-baseline.md)** | Manages named, persistent visual baselines on disk and automates snapshot comparison, providing the equivalent of Playwright's `toHaveScreenshot()` for autonomous browser testing. |
| **[`nova.screenshot_diff`](nova-screenshot-diff.md)** | Performs pixel-by-pixel visual comparison between two screenshot images or resource URIs, returning changed pixel percentages, cluster bounding boxes, and visual diff overlays. |
<!-- /generated:tool-list -->

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
