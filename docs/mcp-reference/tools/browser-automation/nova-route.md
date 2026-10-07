# `nova.route`

Performs Single Page Application (SPA) client-side routing within the same document, preserving in-memory JavaScript frameworks, Vue/React component states, and ephemeral authentication tokens.

---

## 1. Overview

Standard browser navigation (`window.location.href = ...` or [`nova.navigate`](nova-navigate.md)) triggers a hard document unload. On complex modern web applications (ChatGPT, LinkedIn, Jira, Slack, Figma), a hard reload destroys in-memory state machines, clears Vuex/Redux stores, and often forces the user back to the login screen.

`nova.route` performs **same-document SPA transitions**. It supports two distinct routing strategies:
1. **DOM-Click Mode (`selector`):** Clicks a sidebar menu or navigation link through the same CDP mouse-event pipeline as `nova.click_selector`, then waits for a `pushState`/`replaceState` event.
2. **PushState Mode (`url`):** Dispatches a client-side `history.pushState()` call and checks that the page's main content container actually changed (`route.surface_not_changed` check).

* **Session Preservation:** In-memory auth tokens and active WebSocket connections remain alive.
* **Hard Navigation Guard:** If a clicked link attempts a full-page document reload, Nova automatically intercepts and cancels the navigation, returning `route.hard_navigate_intercepted`.
* **Surface Change Verification:** In pushState mode, Nova compares a before/after DOM signature (tag, id, class, and text shape) of the page's detected main container to confirm new content actually rendered, rather than trusting the URL change alone.

---

## 2. Operation Modes

| Mode | Provided Arguments | Mechanism | Best Used For |
| :--- | :--- | :--- | :--- |
| **DOM-Click Mode** | `selector` (optional `url` expectation hint) | Clicks the UI navigation element via CDP, verifies clickability, and awaits SPA URL update. | Dashboard sidebars, tab switchers, and SPA menu buttons with an `<a>` or `<button>` element. |
| **PushState Mode** | `url` only (no selector) | Invokes `history.pushState` and verifies main-content signature mutation. | Direct routing when valid internal paths are known and no physical button exists. |

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `url` | `string` | No | — | — | Target URL or path to route to. Required for URL-only pushState mode. Optional when selector is provided; in that case it is treated as an expectation hint for the observed final URL. With waitForRoute=true the observed final URL must match it; with waitForRoute=false Nova only fail-closes on a mismatch when a different final URL was already observed before the early return. Must be same-origin as the current document. Can be absolute (https://...) or relative (/path). |
| `selector` | `string` | No | — | — | CSS selector of a link or button to click for SPA routing. Optional when url is provided, but at least one of selector or url is required. If provided, the element is resolved through the interactability/obstruction probe and then clicked via a user-like CDP mouse sequence instead of synthetic page-JS el.click(). Preferred when a matching <a> element exists. |
| `waitForRoute` | `boolean` | No | `true` | — | If true (default), wait for a pushState/replaceState/popstate signal confirming the route changed. |
| `waitForRouteTimeoutMs` | `integer` | No | `3000` | 500–10000 | Max ms to wait for route change signal (500-10000). Only used when waitForRoute=true. |
| `includeScreenshot` | `boolean` | No | `false` | — | If true and route change completes, include a screenshot in the response. Screenshot delivery is an optional sidecar: if capture fails, this result stays authoritative and structuredContent.screenshotStatus/screenshotReasonCode/screenshotRetryable/screenshotError describe the capture-only failure - do not repeat the action to get the image. |
| `screenshotMaxWidth` | `integer` | No | — | — | Max screenshot width in pixels. |
| `screenshotMaxHeight` | `integer` | No | — | — | Max screenshot height in pixels. |
| `screenshotFormat` | `string` | No | `"png"` | `png`, `jpeg`, `auto` | Screenshot format; 'auto' picks PNG or JPEG per region. |
| `screenshotQuality` | `integer` | No | `80` | 1–100 | JPEG quality (1-100). Only used when screenshotFormat is 'jpeg'. |
| `pksInclude` | `string` | No | `"auto"` | `auto`, `off`, `summary`, `full` | PKS payload detail level in structuredContent.pks. Default is server setting (initial: auto). |
| `agentId` | `string` | No | `"default"` | — | Optional agent identity for claim authorization against the target tab. Defaults to 'default'. |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
  "ok": true,
  "status": "ok",
  "targetId": "tab-101",
  "navigationMode": "same_document",
  "requestedUrl": "/app/billing",
  "resolvedUrl": "https://example.com/app/billing",
  "finalUrl": "https://example.com/app/billing",
  "previousUrl": "https://example.com/app/dashboard",
  "sameDocument": true,
  "methodUsed": "push_state",
  "routeChanged": true,
  "waitForRoute": true,
  "waitedMs": 180,
  "stage": "route_changed",
  "pageTitle": "Billing & Subscriptions - Example SPA",
  "pageUrl": "https://example.com/app/billing"
}
```

`methodUsed` is `"dom_click"` when a `selector` was clicked, or `"push_state"` when only `url` was given.

---

## 6. Common Errors & Troubleshooting

| reasonCode | Cause | Corrective Action |
| :--- | :--- | :--- |
| `route.hard_navigate_intercepted` | The clicked selector triggered a full document navigation, which Nova cancelled. Client-side click-handler side effects may already have run before the cancel. | Re-read page state before continuing. Use [`nova.navigate`](nova-navigate.md) if a full reload is intended, or verify the SPA selector. |
| `route.surface_not_changed` | PushState updated the browser address bar, but the SPA framework failed to render new UI content. | Use DOM-click mode instead, or check if the SPA router requires hash navigation (`/#/billing`). |
| `route.unexpected_final_url` | Final observed URL did not match the expected `url` hint. | Omit the `url` hint or verify SPA redirection logic. |
| `route.same_origin_required` | The target URL has a different origin (scheme, host, or port) than the current document. | `nova.route` only supports same-document navigation; use [`nova.navigate`](nova-navigate.md) for cross-origin destinations. |
| `route.concurrent_conflict` | Another `nova.route` call is already in progress on the same target. | Wait for the earlier call to complete or time out before retrying. |
| `route.signal_timeout` | No `pushState`/`replaceState` signal arrived within `waitForRouteTimeoutMs`. | Confirm the route actually changed via `nova.page_info`, or raise `waitForRouteTimeoutMs`. |

---

## 7. Related Tools & Documentation

* [`nova.navigate`](nova-navigate.md) — For full document-level HTTP navigations.
* [`nova.click_selector`](nova-click-selector.md) — Standard button and element clicks.
* [`nova.back`](nova-back.md) — Guarded history traversal.
* [Agent Awareness Gates (AAG)](../../../core-features/agent-awareness-gates-aag/README.md) — Session-preservation gates during navigation.
