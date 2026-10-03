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

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `maxWidth` | `integer` | No | — | 1–10000 | Legacy alias for screenshotMaxWidth. Max screenshot width in pixels. Image is downscaled if wider. |
| `maxHeight` | `integer` | No | — | 1–10000 | Legacy alias for screenshotMaxHeight. Max screenshot height in pixels. Image is downscaled if taller. |
| `screenshotMaxWidth` | `integer` | No | — | 1–10000 | Preferred screenshot width limit in pixels. Must match maxWidth if both are provided. |
| `screenshotMaxHeight` | `integer` | No | — | 1–10000 | Preferred screenshot height limit in pixels. Must match maxHeight if both are provided. |
| `format` | `string` | No | — | `png`, `jpeg`, `auto` | Legacy alias for screenshotFormat. Image format: 'png' (lossless), 'jpeg' (smaller), or 'auto'. With 'auto' + region: PNG for moderate text/UI evidence crops (<= ~1 MP), JPEG q=85 for very large photo/canvas/overview regions. Without region, 'auto' falls back to the tool-intent default (jpeg q=78). |
| `screenshotFormat` | `string` | No | — | `png`, `jpeg`, `auto` | Preferred image format. Must match format if both are provided. See 'format' for 'auto' semantics. |
| `quality` | `integer` | No | — | 1–100 | Legacy alias for screenshotQuality. JPEG quality (1-100). Only used when format is 'jpeg'. |
| `screenshotQuality` | `integer` | No | — | 1–100 | Preferred JPEG quality (1-100). Must match quality if both are provided. |
| `region` | `object` | No | — | — | Optional crop bounding box in CSS pixels. CDP captures only this region (capture-time clip — single CDP call, no decode/re-encode). Use with screenshotFormat='auto' to get PNG for moderate text/UI evidence crops (<= ~1 MP) or JPEG q=85 for very large photo/canvas/overview regions. |
| `region.x` | `integer` | Yes | — | ≥ 0 | Left edge of the crop box in CSS pixels (>= 0). |
| `region.y` | `integer` | Yes | — | ≥ 0 | Top edge of the crop box in CSS pixels (>= 0). |
| `region.width` | `integer` | Yes | — | 1–10000 | Width of the crop box in CSS pixels (> 0). |
| `region.height` | `integer` | Yes | — | 1–10000 | Height of the crop box in CSS pixels (> 0). |
| `responseMode` | `string` | No | — | `inline`, `reference`, `thumbnail+reference`, `auto` | Override default delivery mode. 'inline': full image bytes in response (default for nova.capture_screenshot). 'reference': only nova://screenshot/... URI in response — read with nova.read_screenshot_resource(uri='nova://screenshot/...') or MCP resources/read on demand (saves ~2400 tokens for large screenshots). 'thumbnail+reference': small inline thumbnail (~18 KB) + URI for full image. 'auto': server picks inline for small images with budget headroom, otherwise thumbnail+reference. URIs are session-scoped and TTL-bound (default 1h). |
| `force` | `boolean` | No | `false` | — | Power-user override for the aag.screenshot_budget gate. When true, bypasses Soft-Warn and Forceable-Hard caps (inlineBytes, sourcePixels, sessionBudget). Does NOT bypass Absolute-Safety caps (decompression-bomb-guards at 50 MB encoded / 50 MP source) — those reject regardless. Default false. Use sparingly: forced inline captures cost full vision tokens (~5800 for 4K). Auto-downgrade to thumbnail+reference is usually preferable. |
| `highlightSelector` | `string` | No | — | — | Optional CSS selector. When used without selector/region, captures a readable close-up crop of the matched element. When combined with selector/region, adds a colored outline to that explicit capture. Supports ' >>> ' shadow DOM combinator. |
| `scrollToSelector` | `string` | No | — | — | Optional CSS selector. Scrolls the element into view before capturing. No visual highlight. Supports ' >>> ' shadow DOM combinator. |
| `selector` | `string` | No | — | — | Optional CSS selector for a one-shot element screenshot (Playwright locator.screenshot()). Resolves the element's bounding box (scrolled into view, shadow-DOM aware via ' >>> ') and captures only that region. Mutually exclusive with 'region'. Errors if the element is not found, not visible (display:none, visibility:hidden, zero-size), covered by another element or clipped away by an ancestor, or fully transparent (opacity 0 on it or on an ancestor) — in the transparent case a crop would show the content behind it, so no image is returned at all. |
| `cropPaddingPx` | `integer` | No | — | 0–200 | Optional CSS-pixel padding around selector/highlightSelector element crops. 0 keeps a tight crop; positive values add page context and are clamped to 200. Must match contextPaddingPx if both are provided. |
| `contextPaddingPx` | `integer` | No | — | 0–200 | Alias for cropPaddingPx. Use for QM/context proof crops when the surrounding page helps interpret the element. |
| `cropPadding` | `string` | No | — | `tight`, `comfortable`, `debug` | Preset padding for selector/highlightSelector element crops. 'tight'=0 CSS px, 'comfortable'=18 CSS px, 'debug'=32 CSS px. Numeric cropPaddingPx/contextPaddingPx wins when provided. |
| `includeContextImage` | `boolean` | No | `false` | — | When true with selector or highlightSelector-as-crop, returns the normal detail crop plus a small marked viewport overview in structuredContent.contextOverview and content[]. The context image uses thumbnail+reference JPEG defaults and is for orientation, not text proof. |
| `highlightColor` | `string` | No | `"#FF2020"` | — | Hex CSS color for highlightSelector/includeContextImage markers. Accepted forms: #RGB, #RRGGBB, #RRGGBBAA. |
| `highlightStrokePx` | `integer` | No | `3` | 1–16 | Marker stroke width in CSS pixels for highlightSelector/includeContextImage. Values are clamped to 1..16. |
| `highlightStyle` | `string` | No | `"dashed"` | `solid`, `dashed`, `dotted` | Marker line style for highlightSelector/includeContextImage. |
| `highlightPlacement` | `string` | No | `"outside"` | `outside`, `inside`, `both` | Where to draw the marker relative to the target element. 'inside' uses an inset frame so tight crops still show the marker; 'both' draws outside and inside frames. |
| `highlightLabel` | `string` | No | — | ≤ 80 characters | Optional short label rendered near the marker. Use for QM labels such as 'target' or 'expected modal'. Ignored unless highlightSelector or includeContextImage is active. |
| `highlightBackdrop` | `boolean` | No | `false` | — | When true, dims the viewport around the target marker. Useful for context overview proof; ignored unless highlightSelector or includeContextImage is active. |
| `highlightCenterMarker` | `boolean` | No | `false` | — | When true, draws a small crosshair at the target center. Useful when the target is tiny; ignored unless highlightSelector or includeContextImage is active. |
| `outputDetail` | `string` | No | `"full"` | `full`, `compact` | Response verbosity. 'compact' omits screenshotFilePath (always identical to filePath), inlinePreview when it describes the same image as evidenceImage, and the delivery telemetry: byteAccounting (byte counts of what you just received) and tokens (per-provider vision-token estimates). The image, coordinateMeta and every warning are unaffected - no setting can hide a warning. |
| `fullPage` | `boolean` | No | `false` | — | Capture the entire scrollable page instead of just the visible viewport (Playwright screenshot({fullPage:true})). Ignored when 'region' is set — a crop box already names what to capture. Very long pages are capped (~20000px tall / 20 MP); over that the capture falls back to the viewport. If full-page CDP capture times out, Nova degrades through a precomputed viewport CDP clip before CapturePreviewAsync. Combine with screenshotMaxWidth/Height to downscale the tall result. Tip: prefer responseMode='thumbnail+reference' for full-page shots — they are token-expensive inline. |

Capability bundles: `browser_automation`, `form_submission`, `page_read_debug`, `visual_evidence`.
<!-- /generated:parameters -->

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
