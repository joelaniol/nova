# `nova.route`

Performs Single Page Application (SPA) client-side routing within the same document, preserving in-memory JavaScript frameworks, Vue/React component states, and ephemeral authentication tokens.

---

## 1. Overview

Standard browser navigation (`window.location.href = ...` or [`nova.navigate`](nova-navigate.md)) triggers a hard document unload. On complex modern web applications (ChatGPT, LinkedIn, Jira, Slack, Figma), a hard reload destroys in-memory state machines, clears Vuex/Redux stores, and often forces the user back to the login screen.

`nova.route` performs **same-document SPA transitions**. It supports two distinct routing strategies:
1. **DOM-Click Mode (`selector`):** Clicks a sidebar menu or navigation link using CDP pointer physics and waits for a `pushState`/`replaceState` event.
2. **PushState Mode (`url`):** Dispatches a client-side `history.pushState()` call and asserts that the UI surface actually renders new content (`route.surface_not_changed` check).

* **Capability Bundle:** `browser_automation`
* **Session Preservation:** In-memory auth tokens and active WebSocket connections remain alive.
* **Hard Navigation Guard:** If a clicked link attempts a full-page document reload, Nova automatically intercepts and cancels the navigation, returning `route.hard_navigate_intercepted`.
* **Surface Change Verification:** In pushState mode, Nova verifies that the primary page container updated visually before declaring success.

---

## 2. Operation Modes

| Mode | Provided Arguments | Mechanism | Best Used For |
| :--- | :--- | :--- | :--- |
| **DOM-Click Mode** | `selector` (optional `url` expectation hint) | Clicks the UI navigation element via CDP, verifies clickability, and awaits SPA URL update. | Dashboard sidebars, tab switchers, and SPA menu buttons with an `<a>` or `<button>` element. |
| **PushState Mode** | `url` only (no selector) | Invokes `history.pushState` and verifies main-content signature mutation. | Direct routing when valid internal paths are known and no physical button exists. |

---

## 3. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`selector`** | `string` | **Conditional**| `null` | CSS selector of link/button to click. Supports ` >>> `. |
| **`url`** | `string` | **Conditional**| `null` | Target path or URL. Required for pushState mode; optional expectation hint for DOM-click mode. |
| **`targetId`** | `string` | No | `"active"` | Target tab ID from `nova.tabs`, or `"active"`. |
| **`waitForRoute`** | `boolean` | No | `true` | Wait for `pushState`/`replaceState`/`popstate` signal. |
| **`waitForRouteTimeoutMs`**| `integer`| No | `3000` | Max ms to wait for route transition (500–10,000 ms). |
| **`includeScreenshot`**| `boolean`| No | `false` | Include screenshot sidecar upon route completion. |
| **`agentId`** | `string` | No | `"default"` | Agent identity for claim lease verification. |

---

## 4. Example Calls

### Navigate via SPA Sidebar Link
```json
{
  "selector": "nav.sidebar >>> a[href='/billing']",
  "url": "/billing",
  "waitForRoute": true
}
```

### Direct PushState Transition
```json
{
  "url": "/app/projects/nova-workspace/settings",
  "waitForRoute": true,
  "waitForRouteTimeoutMs": 4000
}
```

---

## 5. Return Value Structure

```json
{
  "success": true,
  "targetId": "tab-101",
  "previousUrl": "https://example.com/app/dashboard",
  "currentUrl": "https://example.com/app/billing",
  "routeCommitted": true,
  "surfaceChanged": true,
  "pageTitle": "Billing & Subscriptions - Example SPA"
}
```

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `route.hard_navigate_intercepted` | The clicked selector was a regular anchor `<a href="...">` that triggered a full document reload. | Use [`nova.navigate`](nova-navigate.md) if a full reload is acceptable, or verify SPA selector. |
| `route.surface_not_changed` | PushState updated the browser address bar, but the SPA framework failed to render new UI content. | Use DOM-click mode instead, or check if the SPA router requires hash navigation (`/#/billing`). |
| `route.unexpected_final_url` | Final observed URL did not match the expected `url` hint. | Omit the `url` hint or verify SPA redirection logic. |

---

## 7. Related Tools & Documentation

* [`nova.navigate`](nova-navigate.md) — For full document-level HTTP navigations.
* [`nova.click_selector`](nova-click-selector.md) — Standard button and element clicks.
* [`nova.back`](nova-back.md) — Guarded history traversal.
* [Agent Awareness Gates (AAG)](../../../core-features/aag.md) — Session-preservation gates during navigation.
