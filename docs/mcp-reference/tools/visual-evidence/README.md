# Visual Evidence, Screenshots & Archiving

Lossless cropped screenshots, pixel-by-pixel diffing, persistent baselines, and print-to-PDF generation.

* **Capability Bundle(s):** `visual_evidence`
* **Core Architecture Guide:** [Core Features: evm-and-visual-evidence.md](../../../core-features/evm-and-visual-evidence.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (7 Tools)

| Tool Name | Status | Description |
| :--- | :---: | :--- |
| **[`nova.capture_app_screenshot`](nova-capture-app-screenshot.md)** | Documented | Capture app-UI evidence. |
| **[`nova.capture_screenshot`](nova-capture-screenshot.md)** | Documented | Capture a screenshot of a tab (best-effort; CDP Page.captureScreenshot). |
| **[`nova.read_pdf`](nova-read-pdf.md)** | Documented | Read the text of a PDF on disk - the other half of nova.save_pdf. |
| **[`nova.responsive_screenshots`](nova-responsive-screenshots.md)** | Documented | Responsive-breakpoint sweep: capture one screenshot per viewport width in a single call (the 'screenshot @ [375, 768, 1280, 192... |
| **[`nova.save_pdf`](nova-save-pdf.md)** | Documented | Render the current page to a PDF and write it to disk (CDP Page.printToPDF). |
| **[`nova.screenshot_baseline`](nova-screenshot-baseline.md)** | Documented | Named, persistent visual baselines — the Playwright toHaveScreenshot() equivalent. |
| **[`nova.screenshot_diff`](nova-screenshot-diff.md)** | Documented | Compare two PNG screenshots pixel-by-pixel and return changed regions as bounding boxes. |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
