# `nova.save_pdf`

Renders the active web page to a vector PDF document on disk via Chrome DevTools Protocol (`Page.printToPDF`), providing zero-token document archiving and export capabilities.

---

## 1. Overview

Exporting contracts, receipts, articles, or multi-page documentation as visual screenshots is cumbersome and lossy. `nova.save_pdf` renders pages directly into searchable, vector PDF files. Because the generated PDF is written directly to disk, large multi-page reports consume **zero response tokens** in the agent conversation context.

* **Zero Response Tokens:** Returns the on-disk file path in `structuredContent.filePath` rather than base64 bytes.
* **Background Tab Execution:** Unlike screenshots, PDF generation does not require the tab to be focused or visible on screen.
* **Print Styling & CSS Page Rules:** Honors `@media print` stylesheets and `@page` size rules (`preferCSSPageSize: true`).
* **Flexible Page Range:** Print specific pages (e.g. `"1-3, 5"`) or complete documents.

---

## 2. Key Capabilities & Features

### A. Automatic Exports Directory Storage
By default, Nova stores PDFs in its secure, persistent `Exports/` folder:
* Requires no filesystem permissions.
* The absolute file path is returned in `structuredContent.filePath`.

### B. Custom Save Paths (`savePath`)
Agents can specify custom export paths (e.g. `C:/workspace/invoices/2026-10-receipt.pdf`):
* Requires the user to enable "Allow local files" in Nova settings.
* Returns error `-32035` if local file access is restricted by policy.

### C. Clean Archival Defaults
Out of the box, `nova.save_pdf` configures optimal print parameters:
* `printBackground: true` preserves brand colors, graphs, and table backgrounds.
* `displayHeaderFooter: false` removes messy browser print headers (URLs, timestamps, page counts).
* `preferCSSPageSize: true` automatically sizes paper to match layout specifications.

### D. Tagged PDF Safety (`generateTaggedPDF`)
Generating accessible tagged PDFs requires snapshotting the browser's accessibility tree, and that snapshot step can crash the render process on some pages (seen in practice on at least one real-world page). `generateTaggedPDF` defaults to `false` so the common case stays stable; untagged output still contains selectable, searchable text, it just has no PDF/UA structure tree. If a tagged render does crash the renderer, the tool reports `reasonCode: "save_pdf.tagged_pdf_renderer_crash"` and the fix is to retry without the flag.

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `savePath` | `string` | No | — | — | Optional absolute file path to write the PDF to (e.g. C:\Users\me\archive\page.pdf). Requires the user's 'Allow local files' setting; returns -32035 when disabled. Omit to write into Nova's Exports folder and read the path from structuredContent.filePath. |
| `timeoutMs` | `integer` | No | `15000` | 1000–30000 | Maximum time in milliseconds for Page.printToPDF. Increase for long messages or complex pages. A timeout occurs before file writing and reports operationOutcome='not_committed'. |
| `landscape` | `boolean` | No | `false` | — | Paper orientation. false = portrait, true = landscape. |
| `printBackground` | `boolean` | No | `true` | — | Print background graphics/colors. Default true so archived pages look like the rendered page. |
| `displayHeaderFooter` | `boolean` | No | `false` | — | Print the default browser header/footer (date, URL, page numbers). Default false for clean output. |
| `preferCSSPageSize` | `boolean` | No | `true` | — | Prefer any page size declared in the page's CSS @page rules over paperWidth/paperHeight. |
| `generateTaggedPDF` | `boolean` | No | `false` | — | Emit a tagged (accessible) PDF with a structure tree. Off by default because building the tags makes the renderer snapshot the accessibility tree, which crashes the render process on some pages — the tab then has to be rebuilt and no PDF is produced. Untagged output still contains selectable text. Turn it on only when a downstream consumer needs PDF/UA structure tags; on a renderer crash the tool returns reasonCode='save_pdf.tagged_pdf_renderer_crash' and retrying without this flag is the fix. |
| `scale` | `number` | No | `1` | 0.1–2 | Render scale of the page content (0.1–2.0). |
| `pageRanges` | `string` | No | — | — | Paper ranges to print, e.g. '1-5, 8, 11-13'. Empty/omitted prints all pages. |
| `paperWidth` | `number` | No | — | ≥ 0 | Paper width in inches. Ignored when preferCSSPageSize applies a CSS page size. |
| `paperHeight` | `number` | No | — | ≥ 0 | Paper height in inches. Ignored when preferCSSPageSize applies a CSS page size. |
| `marginTop` | `number` | No | — | ≥ 0 | Top margin in inches. |
| `marginBottom` | `number` | No | — | ≥ 0 | Bottom margin in inches. |
| `marginLeft` | `number` | No | — | ≥ 0 | Left margin in inches. |
| `marginRight` | `number` | No | — | ≥ 0 | Right margin in inches. |

Capability bundles: `page_read_debug`, `visual_evidence`.
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 4. Example Calls

### Standard Page Export to Exports Directory
```json
{
  "printBackground": true
}
```

### Landscape Export of Specific Pages to Custom Location
```json
{
  "savePath": "C:/Reports/Q3_Executive_Summary.pdf",
  "landscape": true,
  "pageRanges": "1-3",
  "scale": 0.9
}
```

---

## 5. Return Value Structure

```json
{
  "content": [
    { "type": "text", "text": "Saved PDF (184520 bytes) to C:\\Users\\user\\AppData\\Local\\NovaBrowser\\Exports\\page_20261002_194512_a1b2c3d4.pdf" }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-101",
    "filePath": "C:\\Users\\user\\AppData\\Local\\NovaBrowser\\Exports\\page_20261002_194512_a1b2c3d4.pdf",
    "savePath": null,
    "bytes": 184520,
    "deliveryMode": "file",
    "generateTaggedPDF": false
  }
}
```

`savePath` is `null` when the default Exports folder was used, and echoes the resolved absolute path when the caller passed `savePath`. There is no page URL/title, page count, or file-size field beyond `bytes` in this response — read the page's own title/URL separately (e.g. `nova.page_info`) if you need it alongside the archive.

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `-32035: ... writing to a custom savePath requires local file access` | `savePath` was provided, but the user has not enabled "Allow local files". | Omit `savePath` to use the built-in `Exports/` folder, or enable the setting. |
| `reasonCode: "save_pdf.tagged_pdf_renderer_crash"` (`-32002`) | `generateTaggedPDF: true` made the renderer snapshot the accessibility tree, which crashed the render process on this page. No PDF was written. | Retry the same call without `generateTaggedPDF` (the untagged path still keeps selectable text). |
| `reasonCode: "save_pdf.renderer_unavailable"` (`-32002`, `retryable: true`) | The target renderer exited or is being recreated (not from `generateTaggedPDF`). No PDF was written. | Wait for the tab to reload, confirm with `nova.tabs`/`nova.page_info`, then retry once; stop retrying if it recurs. | 
| Timeout before `Page.printToPDF` completes | Heavy print stylesheets or slow rendering exceeded `timeoutMs`. Reports `operationOutcome: "not_committed"`; no file was written. | Increase `timeoutMs` (max 30000). |

---

## 7. Related Tools & Documentation

* [`nova.capture_screenshot`](nova-capture-screenshot.md) — For raster image proof and visual cropped evidence.
* [`nova.extract_table`](../dom-and-reading/nova-extract-table.md) — For extracting raw tabular data instead of rendering documents.
