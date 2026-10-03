# `nova.save_pdf`

Renders the active web page to a vector PDF document on disk via Chrome DevTools Protocol (`Page.printToPDF`), providing zero-token document archiving and export capabilities.

---

## 1. Overview

Exporting contracts, receipts, articles, or multi-page documentation as visual screenshots is cumbersome and lossy. `nova.save_pdf` renders pages directly into searchable, vector PDF files. Because the generated PDF is written directly to disk, large multi-page reports consume **zero response tokens** in the agent conversation context.

* **Capability Bundle:** `visual_evidence`, `data_extraction`
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
Generating accessible tagged PDFs requires snapshotting the browser's accessibility tree, which can crash render processes on complex pages. In Nova, `generateTaggedPDF` defaults to `false` for rock-solid stability while keeping all text selectable and searchable.

---

## 3. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`savePath`** | `string` | No | `null` | Optional absolute path to write PDF to. Defaults to Nova's `Exports/` directory. |
| **`pageRanges`** | `string` | No | `null` | Pages to print (e.g. `"1-5, 8, 11-13"`). Omit to print all pages. |
| **`landscape`** | `boolean` | No | `false` | Paper orientation (`true` = landscape, `false` = portrait). |
| **`printBackground`** | `boolean` | No | `true` | Include background graphics and colors. |
| **`preferCSSPageSize`**| `boolean` | No | `true` | Prefer CSS `@page` dimensions over paper width/height. |
| **`scale`** | `number` | No | `1.0` | Content render scale factor (0.1–2.0). |
| **`displayHeaderFooter`**| `boolean`| No | `false` | Print browser header/footer (date, URL, page number). |
| **`generateTaggedPDF`**| `boolean`| No | `false` | Generate PDF/UA accessible structure tree. |
| **`timeoutMs`** | `integer` | No | `15000` | Max render timeout in milliseconds (1,000–30,000). |
| **`targetId`** | `string` | No | `"active"` | Target tab ID from `nova.tabs`, or `"active"`. |
| **`agentId`** | `string` | No | `"default"` | Agent identity for claim lease verification. |

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
  "targetId": "tab-101",
  "url": "https://example.com/reports/financials",
  "title": "Quarterly Financial Overview",
  "pageCount": 4,
  "fileSizeBytes": 184520,
  "structuredContent": {
    "filePath": "C:/Users/Agent/AppData/Local/NovaBrowser/Exports/financials_20261002_194512.pdf"
  }
}
```

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `-32035: Local file access disabled` | `savePath` was provided, but user disabled local disk writes. | Omit `savePath` to use the built-in `Exports/` folder. |
| `save_pdf.tagged_pdf_renderer_crash` | `generateTaggedPDF: true` crashed on complex nested SVG/shadow trees. | Retry with `generateTaggedPDF: false`. |
| `Print timeout exceeded` | Heavy print media stylesheets or dynamic images stalled rendering. | Increase `timeoutMs` to 30,000 ms. |

---

## 7. Related Tools & Documentation

* [`nova.capture_screenshot`](nova-capture-screenshot.md) — For raster image proof and visual cropped evidence.
* [`nova.extract_table`](../dom-and-reading/nova-extract-table.md) — For extracting raw tabular data instead of rendering documents.
