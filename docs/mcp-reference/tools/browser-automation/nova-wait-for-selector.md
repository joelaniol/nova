# `nova.wait_for_selector`

Waits for a DOM element matching a CSS selector to appear, become visible, or disappear, returning its exact bounding rectangle and settlement state.

---

## 1. Overview

`nova.wait_for_selector` provides deterministic synchronization for dynamic web pages, Single Page Applications (SPAs), streaming LLM responses, and modal workflows. Instead of fragile arbitrary delays (`sleep(3000)`), agents wait explicitly for DOM elements to exist, become visible, or disappear completely.

* **Capability Bundle:** `browser_automation`, `element_inspection`
* **Inversion Support (`absent: true`):** Wait for spinners, overlays, or modals to disappear.
* **Shadow-DOM Piercing:** Deep selector traversal across shadow boundaries using ` >>> `.
* **Blocker Dismissal:** Optional automatic dismissal of consent banners or backdrops encountered during polling.

---

## 2. Key Capabilities & Features

### A. Waiting for Appearance & Visibility
By default (`visible: true`, `absent: false`), the tool polls until the target element exists in the DOM and is physically visible (non-zero width/height, `visibility != hidden`, `display != none`, `opacity > 0`).

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

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`selector`** | `string` | **Yes** | ? | CSS selector. Supports ` >>> ` to pierce Shadow DOM boundaries. |
| **`targetId`** | `string` | No | `"active"` | Target tab ID from `nova.tabs`, or `"active"`. |
| **`absent`** | `boolean` | No | `false` | If `true`, wait for the element to disappear (removed or hidden). |
| **`visible`** | `boolean` | No | `true` | If `true`, requires element visibility. If `false`, DOM presence is sufficient. |
| **`timeoutMs`** | `integer` | No | `10000` | Maximum wait time in milliseconds (0?300,000 ms). |
| **`pollMs`** | `integer` | No | `200` | Polling interval between checks (50?2,000 ms). |
| **`scrollIntoView`** | `boolean` | No | `true` | If `true`, scrolls the element into view once found. |
| **`autoDismissBlockers`** | `boolean` | No | `false` | Automatically dismiss overlay banners during polling. |
| **`autoDismissMode`** | `string` | No | `"conservative"` | Blocker strategy: `"conservative"` or `"aggressive"`. |
| **`includeScreenshot`** | `boolean` | No | `false` | Capture visual evidence screenshot once condition is satisfied. |
| **`screenshotFormat`** | `string` | No | `"png"` | Format for screenshot: `"png"`, `"jpeg"`, or `"auto"`. |
| **`agentId`** | `string` | No | `"default"` | Agent identity for claim lease verification. |

---

## 4. Example Calls

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

When the selector condition is satisfied, Nova returns the target element's bounding rect and settlement metrics:

```json
{
  "matched": true,
  "selector": "div.search-results-grid > article.result-item",
  "targetId": "tab-104",
  "elapsedMs": 1420,
  "rect": {
    "x": 240,
    "y": 380,
    "width": 680,
    "height": 145
  },
  "inViewport": true,
  "domCount": 12
}
```

If `absent: true` was requested and the element vanished:
```json
{
  "matched": true,
  "selector": "#global-loading-overlay",
  "absent": true,
  "elapsedMs": 2840
}
```

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `Timeout waiting for selector: ...` | Element was not added to DOM or never became visible within `timeoutMs`. | Verify selector using `nova.read_dom` or increase `timeoutMs` for heavy network calls. |
| `Element blocked by overlay: ...` | A modal backdrop or cookie banner obscures the element. | Set `autoDismissBlockers: true` or call `nova.dismiss_blockers`. |
| `Shadow root not found` | The left-hand side of ` >>> ` does not host an open or accessible shadow root. | Verify parent component selector. |

---

## 7. Related Tools & Documentation

* [`nova.click_selector`](nova-click-selector.md) ? Click the element immediately after locating it.
* [`nova.type_selector`](nova-type-selector.md) ? Enter text into inputs once visible.
* [`nova.dismiss_blockers`](nova-dismiss-blockers.md) ? Explicitly remove interfering consent dialogs.
* [Automated Actions Guide (AAG)](../../../core-features/aag.md) ? Deep overview of Nova's selector engine and settlement lifecycle.
