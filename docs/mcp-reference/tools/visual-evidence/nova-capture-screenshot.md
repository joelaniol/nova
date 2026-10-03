# `nova.capture_screenshot`

Captures visual screenshot evidence of the active page, a specific DOM element, or a bounded pixel region, with support for cryptographic SHA-256 hashing, visual callout highlights, and token-saving delivery modes.

---

## 1. Overview

`nova.capture_screenshot` provides deterministic visual evidence for audits, regression testing, and multimodal verification. Unlike generic screen grabbers that blindly dump entire viewports into model contexts, Nova is optimized for **Token Economics** and **Evidence Integrity**:
* **Targeted Crops:** Element crops (`selector`) and bounding regions (`region`) are up to 90% cheaper and significantly sharper than full-page images.
* **Token-Saving Delivery Modes:** Use `responseMode: "thumbnail+reference"` or `"reference"` (`nova://screenshot/...`) to avoid filling LLM context windows with multi-megabyte payloads.
* **Cryptographic Evidence:** Every capture generates a tamper-evident SHA-256 hash in `structuredContent.evidence`.
* **Visual Callouts:** Mark target elements with highlight outlines, labels, and contextual backdrops.

---

## 2. Key Capabilities & Features

### A. Element & Region Cropping (Sharper & Cheaper)
Reading 13px text from a full 4K viewport requires huge token budgets and often yields blurry JPEGs. In contrast, an element crop captures crisp, lossless PNGs at a fraction of the cost:
```json
{
  "selector": "div.invoice-summary-card",
  "screenshotFormat": "png",
  "cropPadding": "comfortable"
}
```

### B. Delivery Modes (`responseMode`)
Manage model token consumption dynamically:
* `inline` *(default)*: Returns full image base64 bytes directly in the MCP response.
* `thumbnail+reference`: Delivers a lightweight inline preview (~18 KB) plus a durable `nova://screenshot/...` URI for full-resolution inspection.
* `reference`: Emits only the resource URI. Agents can read it later on demand via MCP resources, saving ~2,400+ tokens per image.
* `auto`: The server automatically selects `inline` for small images or falls back to `thumbnail+reference` when approaching token budgets.

### C. Visual Callouts & Highlighting
Annotate screenshots for human reviewers or audit trails without editing images externally:
* `highlightSelector`: Draws a colored bounding frame around the target element.
* `highlightColor`: Hex color code (e.g. `"#FF2020"` or `"#00E676"`).
* `highlightLabel`: Short textual tag (e.g. `"Expected Button"`).
* `includeContextImage`: Attaches a miniature overview screenshot alongside the close-up crop.

### D. Full-Page Captures (`fullPage: true`)
Stitches the entire scrollable document vertically (up to 20,000px). Combine with `responseMode: "thumbnail+reference"` to avoid context token overflows.

---

## 3. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`selector`** | `string` | No | `null` | Scopes capture to a specific DOM element. Pierces Shadow DOM via ` >>> `. |
| **`region`** | `object` | No | `null` | Bounding box crop in CSS pixels: `{ x, y, width, height }`. |
| **`fullPage`** | `boolean` | No | `false` | Captures the entire scrollable page height instead of just the viewport. |
| **`screenshotFormat`**| `string` | No | `"auto"` | `"png"` (lossless, ideal for text), `"jpeg"` (smaller), or `"auto"`. |
| **`screenshotQuality`**| `integer`| No | `80` | JPEG compression quality (1–100). |
| **`responseMode`** | `string` | No | `"inline"` | `"inline"`, `"reference"`, `"thumbnail+reference"`, or `"auto"`. |
| **`cropPadding`** | `string` | No | `"comfortable"`| Preset padding around selector crops: `"tight"`, `"comfortable"`, or `"debug"`. |
| **`highlightSelector`**| `string`| No | `null` | Element selector to draw an annotation frame around. |
| **`highlightColor`** | `string` | No | `"#FF2020"`| Hex color for highlight marker. |
| **`highlightLabel`** | `string` | No | `null` | Short label rendered alongside the highlight marker (max 80 chars). |
| **`includeContextImage`**| `boolean`| No | `false` | Returns both a close-up crop and a marked full-viewport overview. |
| **`targetId`** | `string` | No | `"active"` | Target tab ID from `nova.tabs`, or `"active"`. |
| **`agentId`** | `string` | No | `"default"` | Agent identity for claim lease verification. |

---

## 4. Example Calls

### High-Resolution Element Proof with Context Padding
```json
{
  "selector": "#payment-receipt-box",
  "screenshotFormat": "png",
  "cropPadding": "comfortable"
}
```

### Full-Page Capture with Token-Saving Reference
```json
{
  "fullPage": true,
  "responseMode": "thumbnail+reference"
}
```

### Highlight Target Element with Audit Label
```json
{
  "selector": "button#delete-account-btn",
  "highlightSelector": "button#delete-account-btn",
  "highlightColor": "#FF0055",
  "highlightLabel": "Destructive Action",
  "includeContextImage": true
}
```

---

## 5. Return Value Structure

```json
{
  "targetId": "tab-101",
  "format": "png",
  "dimensions": { "width": 640, "height": 380 },
  "fileSizeBytes": 42180,
  "resourceUri": "nova://screenshot/evidence-883921.png",
  "structuredContent": {
    "evidence": {
      "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "capturedAtUtc": "2026-10-02T19:30:00Z",
      "pageUrl": "https://example.com/receipt/4810",
      "pageTitle": "Transaction Receipt"
    }
  }
}
```

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `Element is not visible` | Target `selector` has `display: none`, `opacity: 0`, or zero dimensions. | Ensure the element is rendered and visible before capturing. |
| `Screenshot budget exceeded` | Consecutive full-viewport inline captures exceeded session safety budget. | Switch to `responseMode: "thumbnail+reference"` or crop via `selector`. |
| `Dimension mismatch on diff` | Capture dimensions vary between viewports. | Standardize window bounds with `nova.window_set_size`. |

---

## 7. Related Tools & Documentation

* [`nova.screenshot_diff`](nova-screenshot-diff.md) — Compare two screenshots pixel-by-pixel.
* [`nova.screenshot_baseline`](nova-screenshot-baseline.md) — Persistent visual regression testing.
* [`nova.save_pdf`](nova-save-pdf.md) — Print documents to vector PDF files on disk.
