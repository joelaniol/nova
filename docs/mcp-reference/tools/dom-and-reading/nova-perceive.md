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

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`mode`** | `string` | No | `"summary"` | Perception mode: `"summary"`, `"state"`, `"form_analysis"`, `"cta_detection_v3"`, `"modals"`, or `"full"`. |
| **`includeScreenshot`**| `boolean` | No | `true` | When `false`, suppresses screenshot capture and returns pure structured DOM data. Default `false` for `mode: "state"`. |
| **`deep`** | `boolean` | No | `false` | When `true`, pierces same-origin iframes and open Shadow DOM trees. |
| **`fields`** | `array<string>` | No | `null` | `state` mode only: status families to include (`url`, `title`, `viewport`, `scroll`, `activeElement`, `dialogs`, `frames`, `completeness`, `trustedState`). |
| **`screenshotFormat`** | `string` | No | `"jpeg"` | Image format: `"jpeg"`, `"png"`, or `"auto"`. |
| **`screenshotQuality`**| `integer` | No | `55` | JPEG quality (1?100). Default `55` balances readability with minimal payload size. |
| **`maxWidth` / `maxHeight`** | `integer` | No | `1280` | Max image dimension bounds in pixels. |
| **`sinceRev`** | `integer` | No | `null` | `cta_detection_v3` only: Return only CTA deltas since the specified revision. |
| **`maxResults`** | `integer` | No | `25` | Maximum headings, form fields, or dialog entries returned. |
| **`omitCtas`** | `boolean` | No | `false` | `summary` mode only: drops CTA list when only state + screenshot are needed. |
| **`targetId`** | `string` | No | `"active"` | Target tab ID from `nova.tabs`, or `"active"`. |
| **`agentId`** | `string` | No | `"default"` | Agent identity for claim lease verification. |

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
