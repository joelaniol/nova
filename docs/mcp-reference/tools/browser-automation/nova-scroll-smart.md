# `nova.scroll_smart`

Detects the real scroll container on the page (not just the window) and scrolls it by the requested delta, with a real mouse-wheel event as an automatic fallback, reporting whether content kept growing (saturation) across repeated calls.

---

## 1. Overview

Many modern web applications (social feeds, e-commerce listings, search results) utilize **virtualized lists** or dynamic `IntersectionObserver` listeners. Calling `window.scrollTo(0, 5000)` on such a page often does nothing visible: the document itself does not scroll because the actual scrollable surface is an inner `div`, so the window position never changes and nothing downstream (including `IntersectionObserver`) has anything to react to.

`nova.scroll_smart` probes the page for the most plausible visible scroll container (main content area, open dialog, feed/list/grid — or the window itself), applies the requested delta to it directly (`scrollTop`/`scrollLeft`, or `window.scrollBy` for the window), and re-reads the offset to confirm movement. If that direct application reports no movement, Nova automatically retries once with a **real CDP mouse-wheel event** (`Input.dispatchMouseEvent`, `type: "mouseWheel"`) at a detected anchor point, since some custom scroll surfaces only react to genuine wheel input. The response's `changed`/`ok` field and `reasonCode` report what actually happened; `wheelFallback` is present only when that CDP retry was attempted.

* **Underlying Mechanism:** Direct DOM scroll-offset assignment first, with a one-shot CDP wheel-event retry as a fallback when nothing moved.
* **Directionality:** Supports downward scrolls (`deltaY > 0`) and upward scrolls (`deltaY < 0`, crucial for chat history virtualization).

---

## 2. Key Capabilities & Features

### A. Virtualized Feed Hydration
Where `nova.scroll_to`/`window.scrollTo` fails silently because the page scrolls an inner `div` rather than the document, `scroll_smart` detects that real scroll container (by visibility, overflow, and scroll range) and scrolls it directly, so virtualized feeds (React Virtualized, TanStack Virtual, infinite lists) still see their scroll position change and render subsequent DOM cards. If a container genuinely ignores a programmatic scroll-offset change, the automatic CDP wheel-event retry covers that case too.

### B. Movement & End-of-Range Feedback
Every call to `nova.scroll_smart` returns:
* `changed` (also mirrored as `ok`): whether the chosen target actually moved.
* `reasonCode`: set when nothing moved — e.g. `scroll.no_movement`, `scroll.no_scrollable_target`, `scroll.container_not_found`/`scroll.container_not_scrollable` (only with an explicit `containerSelector`), or `scroll.decoy_detected`.
* `saturation` (only once a scroll range has been observed for the route): `{ grewThisScroll, growthRounds, stableRounds, atEnd, hint }` — an advisory signal for whether repeated downward scrolling is still producing new content, built from the chosen container's scroll range across calls. It is not emitted on upward scrolls (negative `deltaY`).

### C. Inner Container Scrolling (`containerSelector`)
If the scrollable content resides inside a modal, side panel, or specific `div` with `overflow-y: scroll`, pass `containerSelector: ".modal-scroll-body"` to target that element directly rather than the main window.

### D. Upward Scrolling in Chat Histories
In chat apps (Slack, Discord, ChatGPT), older messages load **upwards**. Passing a negative `deltaY` (e.g. `deltaY: -800`) scrolls towards the start of the conversation, triggering upward virtualization.

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `deltaX` | `number` | No | `0` | — | Horizontal scroll delta in pixels (positive = right). |
| `deltaY` | `number` | Yes | — | — | Vertical scroll delta in pixels (positive = down). |
| `containerSelector` | `string` | No | — | — | CSS selector of the scroll container to use, overriding container detection. When set, no other container is tried and no window-scroll fallback runs: if the element is missing or cannot scroll, the call reports reasonCode scroll.container_not_found / scroll.container_not_scrollable instead of scrolling something else. |
| `useRouteCache` | `boolean` | No | `true` | — | If true, reuse and update last-known-good scroll container per host/route key. |
| `cachePriority` | `string` | No | `"normal"` | `low`, `normal`, `high` | Bias strength for cached selector candidates. |
| `suggestPksHint` | `boolean` | No | `true` | — | If true, include pksSuggestions when a stable scroll container is observed repeatedly. |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 4. Example Calls

### Scrolling Down an Infinite Search Feed
```json
{
  "name": "nova.scroll_smart",
  "arguments": {
    "targetId": "tab-1",
    "deltaY": 1200
  }
}
```

### Sample Response (truncated — real responses also carry telemetry, hint, and cache-related fields)
```json
{
  "targetId": "tab-1",
  "deltaX": 0,
  "deltaY": 1200,
  "changed": true,
  "ok": true,
  "status": "ok",
  "reasonCode": null,
  "chosenSource": "DETECTED",
  "chosenSelector": "main.feed",
  "confidence": 0.82,
  "wheelFallback": null,
  "warnings": [],
  "saturation": {
    "grewThisScroll": true,
    "growthRounds": 3,
    "stableRounds": 0,
    "atEnd": false,
    "hint": "still growing"
  },
  "result": {
    "ok": true,
    "moved": true,
    "diagnostics": { "candidateCount": 5, "attemptedCount": 1 }
  }
}
```

There is no `deltaYActual`, top-level `scrollTop`, or `newDomNodesDetected` field. `saturation` is `null` until the route has a measurable scroll range to compare across calls, and it is never emitted on an upward scroll (negative `deltaY`).

### Scrolling Up in a Virtualized Chat Thread
```json
{
  "name": "nova.scroll_smart",
  "arguments": {
    "targetId": "tab-1",
    "containerSelector": "div.chat-scroll-area",
    "deltaY": -600
  }
}
```

---

## 5. Best Practices & Common Traps

* **Avoid `eval("window.scrollTo(...)")` on SPAs:** `window.scrollTo` only moves the document. On pages where the real scroll happens inside an inner container, the window position never changes and lazy-loading never fires — `scroll_smart` detects and scrolls the actual container instead.
* **Stop on `changed: false` (status `"not_found"` or `"blocked"`):** Do not keep retrying with the same parameters. Check `reasonCode` — `scroll.no_scrollable_target`/`scroll.container_not_found` usually means the wrong `containerSelector` or a page that genuinely has no more room to scroll; `scroll.decoy_detected` means the detected container turned out not to be the right one.

---

## See Also

* [`nova.perceive`](../dom-and-reading/nova-perceive.md) — Inspect page completeness (`belowFoldPx`, `aboveFoldPx`).
* [`nova.click_selector`](nova-click-selector.md) — Click loaded elements.
* [Core Feature: Input Dispatch & Shadow DOM Traversal](../../../core-features/humanized-input-engine.md)
