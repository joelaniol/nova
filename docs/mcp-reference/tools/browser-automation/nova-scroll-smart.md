# `nova.scroll_smart`

Executes natural, CDP-level mouse wheel scrolls to trigger dynamic lazy-loading and virtualized lists, reporting scroll saturation and completeness.

---

## 1. Overview

Many modern web applications (social feeds, e-commerce listings, search results) utilize **virtualized lists** or dynamic `IntersectionObserver` listeners. Calling naive scripts like `window.scrollTo(0, 5000)` fails because synthetic coordinate jumps bypass physical wheel events, leaving feeds unhydrated.

`nova.scroll_smart` emits physical wheel events directly via the Chrome DevTools Protocol (CDP). It measures the resulting scroll delta and reports **saturation metrics** (`moved: true/false`, `atEnd: true/false`), allowing agents to scroll feeds deterministically without getting stuck in infinite loops.

* **Underlying Mechanism:** CDP `Input.dispatchMouseEvent` with `type: "mouseWheel"`.
* **Directionality:** Supports downward scrolls (`deltaY > 0`) and upward scrolls (`deltaY < 0`, crucial for chat history virtualization).

---

## 2. Key Capabilities & Features

### A. Virtualized Feed Hydration
Because `scroll_smart` fires authentic hardware wheel events, web frameworks (React Virtualized, TanStack Virtual, UI virtualization in AliExpress/Twitter/Reddit) trigger their event listeners and render subsequent DOM cards immediately.

### B. Saturation & End-of-List Feedback
Every call to `nova.scroll_smart` returns a structured report:
* `moved`: Indicates whether the document or container actually shifted.
* `atEnd`: Signals that the bottom (or top) of the scrollable surface has been reached.
* `saturation`: A metric indicating whether continued scrolling produces diminishing returns.

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

### Sample Response
```json
{
  "ok": true,
  "moved": true,
  "deltaYActual": 1200,
  "scrollTop": 2400,
  "atEnd": false,
  "saturation": 0.85,
  "newDomNodesDetected": 19
}
```

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

* **Never Use `eval("window.scrollTo(...)")`:** In 9 out of 10 modern web applications, `eval(scrollTo)` does not trigger lazy loading because it does not generate user-gesture wheel events.
* **Stop on `atEnd: true` or `moved: false`:** If `scroll_smart` reports `moved: false`, do not keep scrolling with the same parameters. Check if an inner container needs to be targeted via `containerSelector`.

---

## See Also

* [`nova.perceive`](nova-navigate.md) — Inspect page completeness (`belowFoldPx`, `aboveFoldPx`).
* [`nova.click_selector`](nova-click-selector.md) — Click loaded elements.
* [Core Feature: Humanized Input Engine](../../../core-features/humanized-input-engine.md)
