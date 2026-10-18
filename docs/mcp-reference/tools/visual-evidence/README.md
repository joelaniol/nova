# Visual Evidence, Screenshots & Archiving

Lossless cropped screenshots, pixel-by-pixel diffing, persistent baselines, and print-to-PDF generation.

* **Core Architecture Guide:** [Evidence Verification Mode (EVM) & Visual Evidence](../../../research/evidence-verification-mode-evm/README.md)
* **Clips from recordings:** [Video Editing](../video-editing/README.md) (`nova.video_render`)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

<!-- generated:tool-list (from the tool pages in this folder; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
## Tool Inventory (12 Tools)

Capability bundles of these tools: `app_shell_recovery`, `browser_automation`, `device_emulation`, `form_submission`, `page_read_debug`, `system_tools`, `visual_evidence`.

| Tool | What it does |
| :--- | :--- |
| **[`nova.capture_app_screenshot`](nova-capture-app-screenshot.md)** | Captures the Nova app window (tabs, topbar, WebView content) — or, if another agent holds the active tab's claim, a read-only redacted shell view with page content masked out. |
| **[`nova.capture_screenshot`](nova-capture-screenshot.md)** | Captures visual screenshot evidence of the active page, a specific DOM element, or a bounded pixel region, with support for cryptographic SHA-256 hashing, visual callout highlights, and token-saving delivery modes. |
| **[`nova.responsive_screenshots`](nova-responsive-screenshots.md)** | Sweeps multiple viewport widths one at a time, capturing a screenshot at each and restoring the tab's original viewport afterwards. |
| **[`nova.save_pdf`](nova-save-pdf.md)** | Renders the active web page to a vector PDF document on disk via Chrome DevTools Protocol (`Page.printToPDF`), providing zero-token document archiving and export capabilities. |
| **[`nova.screen_record_assert`](nova-screen-record-assert.md)** | Checks a claim during your running screen recording and marks the answer on its timeline with a picture. |
| **[`nova.screen_record_inspect`](nova-screen-record-inspect.md)** | Reads the evidence of a finished screen recording: summary, timeline, contact sheet and pictures. |
| **[`nova.screen_record_mark`](nova-screen-record-mark.md)** | Marks a moment of your running screen recording, with a lossless picture of it. |
| **[`nova.screen_record_start`](nova-screen-record-start.md)** | Starts a video of the Nova window, so your agent can show a feature or a bug as it happens. |
| **[`nova.screen_record_status`](nova-screen-record-status.md)** | Shows whether a recording of the Nova window is running, paused or already finished. |
| **[`nova.screen_record_stop`](nova-screen-record-stop.md)** | Stops the recording of the Nova window and returns the video, checked for correctness. |
| **[`nova.screenshot_baseline`](nova-screenshot-baseline.md)** | Manages named, persistent visual baselines on disk and automates snapshot comparison, providing the equivalent of Playwright's `toHaveScreenshot()` for autonomous browser testing. |
| **[`nova.screenshot_diff`](nova-screenshot-diff.md)** | Performs pixel-by-pixel visual comparison between two screenshot images or resource URIs, returning changed pixel percentages, cluster bounding boxes, and visual diff overlays. |
<!-- /generated:tool-list -->

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
