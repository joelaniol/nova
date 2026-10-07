# `nova.wait_for_selector`

Waits for a DOM element matching a CSS selector to appear, become visible, or disappear, returning its exact bounding rectangle and settlement state.

---

## 1. Overview

`nova.wait_for_selector` provides deterministic synchronization for dynamic web pages, Single Page Applications (SPAs), streaming LLM responses, and modal workflows. Instead of fragile arbitrary delays (`sleep(3000)`), agents wait explicitly for DOM elements to exist, become visible, or disappear completely.

* **Inversion Support (`absent: true`):** Wait for spinners, overlays, or modals to disappear.
* **Streamed content finished (`stableMs`):** Wait until text that keeps arriving (a chat reply, a log, progress output) has stopped changing, on any site and without site-specific selectors. By default the content must change at least once first, and an element inside the region marked `aria-busy="true"` (the standard "still updating" marker many sites set while a reply is written) keeps the wait open, so a model that is still thinking is not mistaken for a finished answer. A model that searches the web or runs tools can stay silent for longer stretches without that marker; use a larger `stableMs` (10000-15000) there. `result.stability` says how much it grew, how long it has been quiet and whether the busy marker was seen; `includeText: true` returns the finished text.
* **Shadow-DOM Piercing:** Deep selector traversal across shadow boundaries using ` >>> `.
* **Blocker Dismissal:** Optional automatic dismissal of consent banners or backdrops encountered during polling.

---

## 2. Key Capabilities & Features

### A. Waiting for Appearance & Visibility
By default (`visible: true`, `absent: false`), the tool polls until the target element exists in the DOM and is physically visible (non-zero width/height, `display != none`, `visibility != hidden`, `pointer-events != none`). A fully transparent element (`opacity: 0`) still counts as visible — Nova reports its effective opacity separately rather than treating it as hidden.

```json
{
  "selector": ".dashboard-analytics-card",
  "timeoutMs": 15000,
  "visible": true
}
```

### B. Waiting for Disappearance (`absent: true`)
When waiting for asynchronous background tasks, payment processing, or modal closure, agents set `absent: true`:
```json
{
  "selector": ".payment-processing-spinner",
  "absent": true,
  "timeoutMs": 20000
}
```
The call succeeds as soon as the element is removed from the DOM or becomes hidden.

### C. Shadow-DOM Traversal (` >>> `)
Like other Nova DOM tools, `nova.wait_for_selector` pierces Web Components and Shadow DOM trees:
```css
nova-chat-widget >>> .streaming-response-complete
```

### D. Scroll Into View (`scrollIntoView: true`)
Once detected, Nova can immediately scroll the resolved element into the current viewport (`scrollIntoView: true`, default `true`), preparing it for subsequent clicks, typing, or inspection.

### E. Blocker Clearance During Polling (`autoDismissBlockers: true`)
If a newly rendered consent dialog or marketing overlay blocks the view while polling:
* When `autoDismissBlockers: true` is passed, Nova automatically applies consent rules or dismisses overlays to clear the viewport for the target element.

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `selector` | `string` | Yes | — | — | CSS selector. Supports ' >>> ' combinator to pierce Shadow DOM boundaries (e.g. 'my-component >>> .inner-button'). |
| `visible` | `boolean` | No | `true` | — | If true (default), element must be visible (not just in DOM). If false, any DOM presence counts. |
| `timeoutMs` | `integer` | No | `10000` | 0–300000 | Max wait time in ms before timing out. |
| `pollMs` | `integer` | No | `200` | 50–2000 | Polling interval in ms between checks. |
| `absent` | `boolean` | No | `false` | — | If true, wait for the element to DISAPPEAR (not exist or not visible). Useful for waiting on loading spinners, streaming indicators, or modal close. |
| `stableMs` | `integer` | No | — | 250–120000 | Wait until the matched content stops changing for this many ms (streamed text finished). 2000 suits plain chat replies. A model that searches the web or runs tools can stay silent for 10+ seconds between steps without marking the page busy, so use 10000-15000 there. Counts against timeoutMs, so give timeoutMs room (e.g. 180000). Not combinable with absent. |
| `requireChange` | `boolean` | No | `true` | — | Only with stableMs. If true (default), the content must change at least once before quiet counts, so a model still thinking is not mistaken for a finished answer. Set false when the content may already be complete. |
| `includeText` | `boolean` | No | `false` | — | Only with stableMs. If true, a settled result also carries text: the text of the last matched element (the newest message when the selector matches messages), saving a separate read call. |
| `maxTextChars` | `integer` | No | `20000` | 1–200000 | Only with includeText. Keeps the END of a longer text (textTruncated=true), where a streamed answer finishes. |
| `frameId` | `string` | No | — | — | Optional same-origin frame ID from nova.perceive(deep=true).structuredContent.frames[].frameId. Waits for the selector inside that iframe; stableMs then watches content inside it as well. |
| `scrollIntoView` | `boolean` | No | `true` | — | If true, scroll the element into view once found. |
| `autoDismissBlockers` | `boolean` | No | `false` | — | If true, explicitly dismiss overlays/modals during polling that may hide the target element. Default false: use overlayDetected plus cmp_apply/dismiss_blockers for consent banners. |
| `autoDismissMode` | `string` | No | `"conservative"` | `conservative`, `aggressive` | Blocker dismissal strategy during polling. 'conservative': common banners only. 'aggressive': all overlay/fixed-position blockers. |
| `includeScreenshot` | `boolean` | No | `false` | — | If true, include a screenshot once the condition is met. |
| `screenshotMaxWidth` | `integer` | No | — | — | Max screenshot width in pixels. |
| `screenshotMaxHeight` | `integer` | No | — | — | Max screenshot height in pixels. |
| `screenshotFormat` | `string` | No | `"png"` | `png`, `jpeg`, `auto` | Screenshot format. Use 'auto' to fall back to the tool-intent default (e.g. jpeg q=72 for confirm-shots). |
| `screenshotQuality` | `integer` | No | `80` | 1–100 | JPEG quality (1-100). Only used when screenshotFormat is 'jpeg'. |
| `screenshotResponseMode` | `string` | No | — | `inline`, `reference`, `thumbnail+reference`, `auto` | Override default delivery mode for the screenshot. Default comes from the tool-intent profile (e.g. confirm-shots default 'thumbnail+reference' for token efficiency). Use 'inline' to force full image bytes, 'auto' to let the server pick based on projected token cost and session budget. |
| `outputDetail` | `string` | No | `"full"` | `full`, `compact` | 'compact' omits fields that repeat a value carried elsewhere in the same response (the duplicate file path, and inlinePreview when it describes the same image as evidenceImage) plus the delivery telemetry: byteAccounting (byte counts of what you just received) and tokens (per-provider vision-token estimates). The image, coordinateMeta and every warning are unaffected - no setting can hide a warning. |

Capability bundles: `browser_automation`, `form_submission`.
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 4. Example Calls

### Wait for a Streamed Reply to Finish
```json
{
  "selector": "main [role='log'] > *",
  "stableMs": 2000,
  "timeoutMs": 120000
}
```
Point the selector at the region the stream writes into. A timeout with `wait_for_selector.no_change` means nothing arrived yet; `wait_for_selector.still_changing` means the content never stayed quiet for `stableMs`.

### Wait for Dynamic Search Results
```json
{
  "selector": "div.search-results-grid > article.result-item",
  "timeoutMs": 8000,
  "visible": true,
  "scrollIntoView": true
}
```

### Wait for Loading Overlay to Disappear
```json
{
  "selector": "#global-loading-overlay",
  "absent": true,
  "timeoutMs": 15000,
  "pollMs": 100
}
```

### Wait for Element in Shadow DOM with Visual Evidence
```json
{
  "selector": "app-video-player >>> .playback-controls-ready",
  "timeoutMs": 12000,
  "includeScreenshot": true
}
```

---

## 5. Return Value Structure

When the selector condition is satisfied, Nova returns `ok: true`, how long it waited, and (unless `absent: true`) the element's probe result nested under `result`:

```json
{
  "structuredContent": {
    "profileId": "tab-104",
    "selector": "div.search-results-grid > article.result-item",
    "absent": false,
    "ok": true,
    "waitedMs": 1420,
    "result": {
      "ok": true,
      "visible": true,
      "attached": true,
      "enabled": true,
      "rect": { "left": 240, "top": 380, "width": 680, "height": 145, "right": 920, "bottom": 525 },
      "center": { "x": 580, "y": 404 },
      "tagName": "ARTICLE"
    }
  }
}
```
This is a trimmed excerpt; the full payload also carries `effectiveOpacity`, `visualViewport`, screenshot-sidecar fields (when `includeScreenshot: true`), and `identityOverlayWarning`.

If `absent: true` was requested and the element disappeared, `result` is `null`:
```json
{
  "structuredContent": {
    "profileId": "tab-1",
    "selector": "#global-loading-overlay",
    "absent": true,
    "ok": true,
    "waitedMs": 2840,
    "result": null
  }
}
```

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `reasonCode: "wait_for_selector.timeout"` — "Timeout waiting for selector: ..." | Element was not added to DOM or never became visible within `timeoutMs`. | Verify the selector (e.g. with `nova.read_dom`) or increase `timeoutMs` for heavy network calls. |
| Still polling past an obscuring overlay | A modal backdrop or cookie banner covers the element, so it never satisfies `visible: true`. | Set `autoDismissBlockers: true` or call `nova.dismiss_blockers` so the overlay is cleared while polling. |
| Selector never matches, no distinct error | The left-hand side of ` >>> ` does not host an open shadow root, so the combinator cannot step into it (closed shadow roots are not reachable). | Verify the parent component actually exposes an open shadow root. |

---

## 7. Related Tools & Documentation

* [`nova.click_selector`](nova-click-selector.md) — Click the element immediately after locating it.
* [`nova.type_selector`](nova-type-selector.md) — Enter text into inputs once visible.
* [`nova.dismiss_blockers`](nova-dismiss-blockers.md) — Explicitly remove interfering consent dialogs.
* [Automated Actions Guide (AAG)](../../../core-features/agent-awareness-gates-aag/README.md) — Deep overview of Nova's selector engine and settlement lifecycle.
