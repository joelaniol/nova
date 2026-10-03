# `nova.perceive`

Fusion multi-modal perception engine: captures visual screenshot evidence and extracts structured semantic DOM data in a single coordinated atomic operation.

---

## 1. Overview

`nova.perceive` is Nova's flagship inspection and perception tool. Instead of requiring separate round-trips for screenshots, accessibility trees, and DOM text dumps, `nova.perceive` coordinates visual pixels and semantic structure simultaneously. It provides specialized perception modes tailored to the agent's immediate operational goal.

* **Capability Bundle:** `dom_reading`, `visual_evidence`, `quality_inspection`
* **Multi-Modal Fusion:** Returns a lightweight visual thumbnail (JPEG 1280px by default) together with structured JSON page semantics.
* **Six Specialized Modes:** `summary`, `state`, `form_analysis`, `cta_detection_v3`, `modals`, and `full`.
* **Fold Completeness Accounting:** Discloses both `belowFoldPx` and `aboveFoldPx` so agents know if lazy feeds, reverse-scroll chat histories, or hidden content exist.
* **Skew Detection:** Monitors the time gap between screenshot capture and DOM extraction (`skewStatus`) to prevent operating on stale state during high-frequency page mutations.

---

## 2. Perception Modes

| Mode | Target Use Case | Returned Content |
| :--- | :--- | :--- |
| **`summary`** *(default)* | General orientation after navigation. | Viewport, title, primary headings, landmarks, text sample, top Call-to-Actions (CTAs). |
| **`state`** | Fast bounded polling / status checks. | Selected status families (`url`, `title`, `activeElement`, `dialogs`, `frames`, `completeness`, `trustedState`). No large text dumps. |
| **`form_analysis`** | Preparing form entry or checkout. | All `<input>`, `<select>`, `<textarea>`, ARIA textboxes, comboboxes, and contenteditable fields with interaction hints. |
| **`cta_detection_v3`** | Interactive decision-making. | Scored and ranked clickable elements with stable handle references (`ctaRef`) and delta sync (`sinceRev`). |
| **`modals`** | Inspecting popups & dialogs. | All active dialogs, cookie banners, modal backdrops, and drawer overlays with their action buttons. |
| **`full`** | Deep diagnostic audits. | Truncated outerHTML, active element, scroll position, and full document structure. |

---

## 3. Key Capabilities & Features

### A. Completeness & Virtualization Awareness
Traditional scrapers measure only distance from the page bottom. `nova.perceive` returns bidirectional fold metrics in `structuredContent.completeness`:
* `belowFoldPx`: Unrendered content beneath the visible window.
* `aboveFoldPx`: Virtualized content above the viewport (critical for reverse-scroll chat windows like ChatGPT, Claude, or Slack).
* `mechanismHint`: Identifies whether more content requires `"scrollable"`, `"loadMoreControl"`, `"pagination"`, or `"bidirectionalVirtualization"`.

### B. Form Analysis with Semantic Interaction Hints
In `mode: "form_analysis"`, Nova analyzes interactive controls beyond basic HTML attributes:
* Returns `controlKind` (e.g. `masked_pin`, `combobox_autocomplete`, `currency_input`).
* Recommends `preferredInteraction` (e.g. `type_selector`, `select_option`, `paste`).
* Detects hidden browser autofill overlays (`autofillWarning`).

### C. CTA Detection v3 with Stable Handles & Delta Sync
In `mode: "cta_detection_v3"`:
* Clickable elements are scored by prominence, visibility, and semantic intent.
* Assigns short numeric handle IDs (`ctaRef`).
* **Delta Mode (`sinceRev`):** When monitoring a live page across steps, pass `sinceRev: <lastRev>` to receive only added, removed, or changed CTAs, saving up to 80% of tokens.

### D. Skew & Capture Synchronization (`perceiveTiming`)
When rendering dynamic SPAs, DOM changes may occur between visual pixel capture and DOM tree extraction:
* `perceiveTiming` reports the millisecond delta between pixels and DOM.
* `skewStatus` flags `'within_threshold'` or `'possible_skew'`, notifying the agent if the screenshot and DOM describe differing mutation phases.

---

## 4. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `mode` | `string` | No | `"summary"` | `summary`, `state`, `full`, `form_analysis`, `cta_detection_v3`, `modals` | Perception mode. 'summary': headings/landmarks/CTAs/text. 'state': bounded caller-selected state fields with no general page-text inventory (requested dialogs may include a <=120-character label; trustedState evaluates configured PKS positive/negative/exclusion evidence); requires responseDetail='essential' and does not clear perceive-first. 'full': truncated outerHTML + scroll + active element. 'form_analysis': form elements + contenteditable + ARIA input/choice roles (textbox/searchbox/combobox/listbox/radiogroup/radio) plus semantic interaction hints. 'cta_detection_v3': scored CTAs with handles. 'modals': open dialogs/overlays. |
| `fields` | `array` of `string` | No | — | 1–9 items | mode='state' only: exact state families to return. Default: url, title, activeElement, dialogs, frames. trustedState is opt-in and returns compact PKS detector values, confidence, exclusion state, and matched evidence. Selecting frames makes deep=true the runtime default unless deep is explicitly supplied. |
| `pksInclude` | `string` | No | `"auto"` | `auto`, `off`, `summary`, `full` | PKS payload detail level in structuredContent.pks. Default is server setting (initial: auto). |
| `maxWidth` | `integer` | No | — | 1–10000 | Max screenshot width (px). JPEG default: 1280. Set higher for detail analysis. Omit or 0 for source resolution (PNG). |
| `maxHeight` | `integer` | No | — | 1–10000 | Max screenshot height (px). JPEG default: 1280. Set higher for detail analysis. Omit or 0 for source resolution (PNG). |
| `maxDomChars` | `integer` | No | `200000` | 1000–5000000 | Maximum DOM characters to extract (full mode outerHTML). Larger values = more detail but slower and more tokens. |
| `maxResults` | `integer` | No | `25` | 1–200 | Maximum headings in summary, elements in form_analysis/cta_detection_v3, or returned dialog entries in state/modals. State dialog entries are additionally capped at 10. Default 25. |
| `omitCtas` | `boolean` | No | `false` | — | summary mode only: if true, drops the CTA list (buttons/links with rect/selector/href) from the response. Use when you only need the screenshot + page state and not the nav/CTA dump. |
| `ctaLimit` | `integer` | No | — | 0–40 | summary mode only: explicit cap on the number of CTAs returned. May go below the default floor of 8 (down to 0). Omit for the maxResults-derived default. omitCtas=true overrides this to 0. |
| `visibleOnly` | `boolean` | No | `true` | — | Only return visible elements in form_analysis/cta_detection_v3 modes. Default true. |
| `ctaColumnDetail` | `string` | No | `"compact"` | `full`, `compact`, `minimal` | CTA v3 column detail: 'minimal' (ref+label+score+rect+src), 'compact' (+href+sel), 'full' (+tag+role+labelSource+sid for cross-rev remap). |
| `topK` | `integer` | No | `20` | 1–100 | CTA v3 only: How many top-scored elements get detailed columns. Rest gets minimal columns. |
| `resolveRefs` | `array` of `integer` | No | — | ≤ 20 items | CTA v3 only: Resolve specific ctaRef handles without full DOM scan. Returns per-ref details (label, rect, tag, selector, connected). Requires existing CTA map from prior perceive. |
| `sinceRev` | `integer` | No | — | ≥ 1 | CTA v3 only: Delta mode. Only returns added/changed items since the given rev. Removed refs listed separately. Same-fingerprint items omitted (~80% token savings on stable pages). |
| `deep` | `boolean` | No | — | — | If true, includes same-origin iframe and open shadow-root traversal in summary/form_analysis/full/modals modes. Runtime default is false except mode='state' with fields containing frames, where it is true. cta_detection_v3 keeps its top-document CTA scan and additionally populates structuredContent.frames: actionable same-origin frames carry CDP frameId plus bounded interactive elements; opaque owners are metadata-only with classification/supportStatus and sanitized URL, never child-DOM execution. |
| `includeScreenshot` | `boolean` | No | — | — | If false, skip screenshot capture/artifact creation and return DOM/extraction-only perceive output with screenshotStatus='skipped'. Runtime default is false for mode='state' and true for other modes. |
| `screenshotFormat` | `string` | No | `"jpeg"` | `png`, `jpeg`, `auto` | Image format. Default 'jpeg' for lightweight thumbnails; use 'png' for detail or 'auto' for the tool-intent default. |
| `screenshotQuality` | `integer` | No | `55` | 1–100 | JPEG quality (1-100). Only used when screenshotFormat is 'jpeg'. |
| `knownDomainNotesHash` | `string` | No | — | — | The domainNotes hash you already hold, from the 'hash' field of an earlier perceive response on this domain. When it matches the current notes you get the compact stub instead of the full text (the largest single item in a perceive response), no matter how long ago you last received it. Any edit to a note changes the hash, so a stale value simply returns the full text - this can never leave you without a note you have not seen. |
| `responseDetail` | `string` | No | — | `full`, `essential` | Overall response metadata level. 'full' (default outside state): all metadata (PKS, OK hints, goals, framework, autofill, trusted state). 'essential': reduced metadata. mode='state' requires essential and returns only its requested status families plus the standard tool envelope. Oversized mode='full' responses may still emit overflow safety fields (`responseSizeWarning`, `overflowFallbackHint`, `snapshot`) so the bounded follow-up path stays available. |
<!-- /generated:parameters -->

---

## 5. Example Calls

### General Orientation after Page Navigation
```json
{
  "mode": "summary",
  "deep": true
}
```

### Lightweight State Check (No Vision Tokens)
```json
{
  "mode": "state",
  "fields": ["url", "title", "dialogs", "completeness"],
  "includeScreenshot": false
}
```

### Deep Form Audit Before Submission
```json
{
  "mode": "form_analysis",
  "deep": true,
  "maxResults": 50
}
```

### Incremental CTA Monitoring with Delta Sync
```json
{
  "mode": "cta_detection_v3",
  "sinceRev": 14
}
```

---

## 6. Return Value Structure (Summary Mode)

```json
{
  "targetId": "tab-101",
  "mode": "summary",
  "url": "https://example.com/checkout",
  "title": "Nova Checkout",
  "viewport": { "width": 1280, "height": 800 },
  "headings": [
    { "level": 1, "text": "Shipping & Payment Details" },
    { "level": 2, "text": "Order Summary" }
  ],
  "landmarks": ["header", "main", "footer"],
  "ctas": [
    { "ctaRef": 1, "label": "Place Order", "selector": "button#submit-order", "score": 98 },
    { "ctaRef": 2, "label": "Apply Coupon", "selector": "button.apply-promo", "score": 75 }
  ],
  "completeness": {
    "aboveFoldPx": 0,
    "belowFoldPx": 450,
    "continuationRisk": "low",
    "mechanismHint": "scrollable"
  },
  "perceiveTiming": {
    "captureGapMs": 14,
    "skewStatus": "within_threshold"
  },
  "screenshotStatus": "ok"
}
```

---

## 7. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `screenshotStatus: "failed"` | Tab is minimized or covered by native OS window. | Call `nova.set_active_tab` followed by `nova.window_set_state` to restore focus, then retry. |
| `possible_skew detected` | Heavy animations or layout re-renders occurred during capture. | Settle page with a brief pause or verify elements with [`nova.wait_for_selector`](../browser-automation/nova-wait-for-selector.md). |
| `bidirectionalVirtualization reported` | Content above the viewport has not been rendered into DOM yet. | Scroll upward using [`nova.scroll_smart`](../browser-automation/nova-scroll-smart.md) with negative `deltaY`. |

---

## 8. Related Tools & Documentation

* [`nova.read_text_structured`](nova-read-text-structured.md) ? Extract text grouped by semantic landmarks.
* [`nova.click_selector`](../browser-automation/nova-click-selector.md) ? Click CTAs discovered by `perceive`.
* [`nova.capture_screenshot`](../visual-evidence/nova-capture-screenshot.md) ? Standalone full-resolution or cropped screenshot captures.
* [Automated Actions Guide (AAG)](../../../core-features/aag.md) ? In-depth guide to perception and settlement cycles.
