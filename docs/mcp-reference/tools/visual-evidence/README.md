# Visual Evidence, Screenshots & Archiving

Lossless cropped screenshots, pixel-by-pixel diffing, persistent baselines, and print-to-PDF generation.

* **Capability Bundle(s):** `visual_evidence`
* **Core Architecture Guide:** [Core Features: evm-and-visual-evidence.md](../../../core-features/evm-and-visual-evidence.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (7 Tools)

| Tool | What it does |
| :--- | :--- |
| **[`nova.capture_app_screenshot`](nova-capture-app-screenshot.md)** | Captures a screenshot of the entire Nova host application window including tabs and window chrome. |
| **[`nova.capture_screenshot`](nova-capture-screenshot.md)** | Captures visual screenshot evidence of the active page, a specific DOM element, or a bounded pixel region, with support for cryptographic SHA-256 hashing, visual callout highlights, and token-saving delivery modes. |
| **[`nova.read_pdf`](nova-read-pdf.md)** | Extracts plain text and page metadata from a locally saved PDF document. |
| **[`nova.responsive_screenshots`](nova-responsive-screenshots.md)** | Captures responsive screenshots across multiple breakpoint widths (mobile, tablet, desktop) in parallel. |
| **[`nova.save_pdf`](nova-save-pdf.md)** | Renders the active web page to a vector PDF document on disk via Chrome DevTools Protocol (`Page.printToPDF`), providing zero-token document archiving and export capabilities. |
| **[`nova.screenshot_baseline`](nova-screenshot-baseline.md)** | Manages named, persistent visual baselines on disk and automates snapshot comparison, providing the equivalent of Playwright's `toHaveScreenshot()` for autonomous browser testing. |
| **[`nova.screenshot_diff`](nova-screenshot-diff.md)** | Performs pixel-by-pixel visual comparison between two screenshot images or resource URIs, returning changed pixel percentages, cluster bounding boxes, and visual diff overlays. |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
