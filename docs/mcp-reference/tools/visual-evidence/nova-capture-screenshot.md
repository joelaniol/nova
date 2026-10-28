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
| `maxWidth` | `integer` | No | — | 1–10000 | Alias of screenshotMaxWidth. |
| `maxHeight` | `integer` | No | — | 1–10000 | Alias of screenshotMaxHeight. |
| `screenshotMaxWidth` | `integer` | No | — | 1–10000 | Downscale to at most this width px. |
| `screenshotMaxHeight` | `integer` | No | — | 1–10000 | Downscale to at most this height px. |
| `format` | `string` | No | — | `png`, `jpeg`, `auto` | Alias of screenshotFormat. |
| `screenshotFormat` | `string` | No | — | `png`, `jpeg`, `auto` | png (lossless) \| jpeg (smaller) \| auto (region: png up to ~1 MP, else jpeg q85; no region: jpeg q78). |
| `quality` | `integer` | No | — | 1–100 | Alias of screenshotQuality. |
| `screenshotQuality` | `integer` | No | — | 1–100 | JPEG quality 1-100. |
| `region` | `object` | No | — | — | Optional crop bounding box in CSS pixels. CDP captures only this region (capture-time clip — single CDP call, no decode/re-encode). Use with screenshotFormat='auto' to get PNG for moderate text/UI evidence crops (<= ~1 MP) or JPEG q=85 for very large photo/canvas/overview regions. |
| `region.x` | `integer` | Yes | — | ≥ 0 | Left edge of the crop box in CSS pixels (>= 0). |
| `region.y` | `integer` | Yes | — | ≥ 0 | Top edge of the crop box in CSS pixels (>= 0). |
| `region.width` | `integer` | Yes | — | 1–10000 | Width of the crop box in CSS pixels (> 0). |
| `region.height` | `integer` | Yes | — | 1–10000 | Height of the crop box in CSS pixels (> 0). |
| `responseMode` | `string` | No | — | `inline`, `reference`, `thumbnail+reference`, `auto` | Override default delivery mode. 'inline': full image bytes in response (default for nova.capture_screenshot). 'reference': only nova://screenshot/... URI in response — read with nova.read_screenshot_resource(uri='nova://screenshot/...') or MCP resources/read on demand (saves ~2400 tokens for large screenshots). 'thumbnail+reference': small inline thumbnail (~18 KB) + URI for full image. 'auto': server picks inline for small images with budget headroom, otherwise thumbnail+reference. URIs are session-scoped and TTL-bound (default 1h). |
| `force` | `boolean` | No | `false` | — | Power-user override for the aag.screenshot_budget gate. When true, bypasses Soft-Warn and Forceable-Hard caps (inlineBytes, sourcePixels, sessionBudget). Does NOT bypass Absolute-Safety caps (decompression-bomb-guards at 50 MB encoded / 50 MP source) — those reject regardless. Default false. Use sparingly: forced inline captures cost full vision tokens (~5800 for 4K). Auto-downgrade to thumbnail+reference is usually preferable. |
| `highlightSelector` | `string` | No | — | — | Alone: readable crop of this element with a marker. With selector/region: outline it in that capture. ' >>> ' pierces shadow DOM. |
| `scrollToSelector` | `string` | No | — | — | Scroll this element into view first (no marker); check scrollToSelectorReached in the result. |
| `selector` | `string` | No | — | — | Crop to this element (scrolled into view; ' >>> ' for shadow DOM). Not with region. Errors if not found, hidden, covered, clipped, or fully transparent (then no image at all). |
| `cropPaddingPx` | `integer` | No | — | 0–200 | Padding px around an element crop (0-200). |
| `contextPaddingPx` | `integer` | No | — | 0–200 | Alias of cropPaddingPx. |
| `cropPadding` | `string` | No | — | `tight`, `comfortable`, `debug` | Padding preset: tight 0 \| comfortable 18 \| debug 32 px. A number wins. |
| `includeContextImage` | `boolean` | No | `false` | — | With an element crop: also a small marked viewport overview (structuredContent.contextOverview), for orientation, not text. |
| `highlightColor` | `string` | No | `"#FF2020"` | — | Marker color #RGB / #RRGGBB / #RRGGBBAA. |
| `highlightStrokePx` | `integer` | No | `3` | 1–16 | Marker width 1-16 px. |
| `highlightStyle` | `string` | No | `"dashed"` | `solid`, `dashed`, `dotted` | Marker line: solid \| dashed \| dotted. |
| `highlightPlacement` | `string` | No | `"outside"` | `outside`, `inside`, `both` | Marker outside \| inside (visible in tight crops) \| both. |
| `highlightLabel` | `string` | No | — | ≤ 80 characters | Short label next to the marker. |
| `highlightBackdrop` | `boolean` | No | `false` | — | Dim everything around the marker. |
| `highlightCenterMarker` | `boolean` | No | `false` | — | Crosshair at the element center (tiny targets). |
| `outputDetail` | `string` | No | `"compact"` | `full`, `compact` | 'compact' (default) leaves out repeats (screenshotFilePath = filePath, duplicate inlinePreview) and delivery statistics (byteAccounting, tokens); the image, coordinateMeta and all warnings stay. 'full' adds them. A compact answer carries outputDetail='compact': a missing field was not sent, not absent. |
| `fullPage` | `boolean` | No | `false` | — | Capture the entire scrollable page instead of just the visible viewport (Playwright screenshot({fullPage:true})). Ignored when 'region' is set — a crop box already names what to capture. Very long pages are capped (~20000px tall / 20 MP); over that the capture falls back to the viewport. If full-page CDP capture times out, Nova degrades through a precomputed viewport CDP clip before CapturePreviewAsync. Combine with screenshotMaxWidth/Height to downscale the tall result. Tip: prefer responseMode='thumbnail+reference' for full-page shots — they are token-expensive inline. |

Capability bundles: `browser_automation`, `form_submission`, `page_read_debug`, `visual_evidence`.
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
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

`structuredContent` is flat (there is no separate top-level envelope) — a representative subset of a `selector` capture with `responseMode: "reference"`:

```json
{
  "structuredContent": {
    "profileId": "tab-101",
    "targetId": "tab-101",
    "bytes": 17408,
    "pixelWidth": 640,
    "pixelHeight": 380,
    "scaled": false,
    "sourcePixelWidth": 640,
    "sourcePixelHeight": 380,
    "mimeType": "image/png",
    "filePath": "C:\\Users\\me\\AppData\\Local\\nova-cognitive\\Nova\\Screenshots\\<id>.png",
    "resource": { "uri": "nova://screenshot/<id>", "mimeType": "image/png", "size": 17408 },
    "evidence": {
      "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "hashedFrom": "file",
      "filePath": "C:\\Users\\me\\AppData\\Local\\nova-cognitive\\Nova\\Screenshots\\<id>.png",
      "capturedAtUtc": "2026-10-02T19:30:00Z"
    },
    "selector": "div.invoice-summary-card"
  }
}
```

`evidence.sha256` is `null` with `hashedFrom: "not_available_thumbnail_only"` when only a thumbnail came back (no stored file and no full inline image to hash). Page URL/title are attached by shared response enrichment, not inside `evidence`. The full response also carries `byteAccounting`, `tokens`, `coordinateMeta`, `deliveryMode`, `inlinePreview`/`evidenceImage`, `readabilityRisk`, and `evidenceGuidance`.

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `-32004: Element for selector not capturable (not found): ...` | Target `selector` matched nothing. | Verify the selector against the live DOM. |
| `-32004: Element for selector not capturable (obstructed): ...` | Another element covers the target near its top edge (or covers it heavily). | Close/dismiss the blocker, or read the box with `nova.get_element_rect` and capture it via `region` instead, which skips this gate. |
| `-32004: Element for selector not capturable (fully-transparent): ...` | The element (or an ancestor) has `opacity: 0` — a crop would show whatever is behind it. | Make it visible first, or capture the surrounding container. |
| AAG screenshot-budget block (`isError: true`) | Consecutive large inline captures exceeded the session's safety budget. | Switch to `responseMode: "thumbnail+reference"`/`"reference"`, crop via `selector`/`region`, or pass `force: true` to override (does not bypass the absolute decompression-bomb caps). |

---

## 7. Operational Best Practices

* **Crop Elements Rather than Capturing Full Viewports:** Full-page or 4K viewport screenshots consume thousands of multimodal vision tokens and blur fine interface typography. Using `selector` or `region` with `screenshotFormat: "png"` yields pixel-perfect, lossless crops at up to 90% lower token cost.
* **Token Economy with Delivery Modes:** In long conversational sessions, avoid dumping raw base64 megabytes into model history. Specify `responseMode: "thumbnail+reference"`. Nova provides an immediate ~18 KB thumbnail preview while persisting the lossless original under a durable `nova://screenshot/...` URI that can be fetched on demand via [`nova.read_screenshot_resource`](../app-shell-and-ui/nova-read-screenshot-resource.md).
* **Handle Obstructed Elements:** If an element is occluded by a sticky navbar, modal backdrop, or cookie banner, Nova rejects the crop with `-32004 (obstructed)`. Clear the obstructing overlay via [`nova.dismiss_blockers`](../guarded-actions/nova-dismiss-blockers.md) before capturing.

---

## 8. Related Tools & Documentation

* [`nova.screenshot_diff`](nova-screenshot-diff.md) — Compare two screenshots pixel-by-pixel.
* [`nova.screenshot_baseline`](nova-screenshot-baseline.md) — Persistent visual regression testing.
* [`nova.save_pdf`](nova-save-pdf.md) — Print documents to vector PDF files on disk.
