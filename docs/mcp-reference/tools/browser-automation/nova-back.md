# `nova.back`

Navigates backward in browser history with automated SPA session preservation, DOM settlement tracking, and guarded navigation gates.

---

## 1. Overview

Executing a browser back action in automated workflows can easily destroy unsaved form entries or log users out of authenticated Single Page Applications. `nova.back` provides **Guarded History Traversal**:
* On SPA-aware surfaces, Nova attempts a same-document history pop (`popstate`), preserving in-memory JavaScript states and session tokens.
* If moving back would trigger a full-document unload on an authenticated or session-sensitive page, Nova's Agent Awareness Gates (AAG) intercept the leave and require explicit `force: true`.
* Supports awaiting DOM settlement (`waitForSettlement: true`) so dynamic client-side rendering settles before subsequent tool calls.

* **Capability Bundle:** `browser_automation`
* **SPA Settlement Engine:** Waits for microtasks, DOM mutations, and network activity to stabilize.
* **Session Preservation Gate:** Prevents accidental session destruction unless explicitly bypassed via `force: true`.
* **Output Tiers:** Supports `"full"`, `"compact"`, or `"minimal"` response envelopes.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `force` | `boolean` | No | `false` | — | If true, bypass the SPA/session-preservation AAG gate and allow a hard history back even when the current tab is flagged as session-sensitive. |
| `waitForLoad` | `boolean` | No | `false` | — | If true, wait for page load before returning. |
| `waitForLoadTimeoutMs` | `integer` | No | `10000` | 0–30000 | Max ms to wait for load (0-30000). Only used when waitForLoad=true. Default 10000 fits typical static pages; SPA-heavy domains (LinkedIn, X, Reddit, large dashboards) often need 15000-20000 — bump explicitly on retry after navigation.wait_for_load_timeout if structuredContent.pageUrl matches the request (URL committed, DOM still settling). |
| `waitForSettlement` | `boolean` | No | `false` | — | If true, wait for SPA DOM settlement after readyState=complete. Implies waitForLoad=true. |
| `settlementTimeoutMs` | `integer` | No | `5000` | 1000–15000 | Max ms to wait for settlement (1000-15000). Only used when waitForSettlement=true. |
| `includeScreenshot` | `boolean` | No | `false` | — | If true and load completes, include a screenshot in the response. Screenshot delivery is an optional sidecar: if capture fails, this result stays authoritative and structuredContent.screenshotStatus/screenshotReasonCode/screenshotRetryable/screenshotError describe the capture-only failure - do not repeat the action to get the image. |
| `screenshotMaxWidth` | `integer` | No | — | — | Max screenshot width in pixels. |
| `screenshotMaxHeight` | `integer` | No | — | — | Max screenshot height in pixels. |
| `screenshotFormat` | `string` | No | `"png"` | `png`, `jpeg`, `auto` | Screenshot format; 'auto' picks PNG or JPEG per region. |
| `screenshotQuality` | `integer` | No | `80` | 1–100 | JPEG quality (1-100). Only used when screenshotFormat is 'jpeg'. |
| `outputDetail` | `string` | No | `"full"` | `full`, `compact`, `minimal` | Response verbosity. 'full' (default) is the unchanged payload. 'compact' drops the advisory blocks you did not ask for (pks/pksMeta, discoverySignals, routingHint, taskDiscoveryWarning, byte accounting) and keeps everything you did - state, screenshot, settlement. 'minimal' is the lean envelope: core contract (ok/status/reasonCode/stage/retryable), the navigation proof (url/requestedUrl/loadCompleted/navigationFailed/webErrorStatus/settlement), target and page info, claim/private state, screenshot sidecar status, and the never-suppressible safety warnings. No setting can hide a warning. |
<!-- /generated:parameters -->

---

## 3. Example Calls

### Standard History Back with SPA Settlement
```json
{
  "waitForSettlement": true,
  "settlementTimeoutMs": 4000
}
```

### Force History Back Across Document Boundaries
```json
{
  "force": true,
  "waitForLoad": true
}
```

---

## 4. Return Value Structure

```json
{
  "ok": true,
  "targetId": "tab-101",
  "url": "https://example.com/products",
  "loadCompleted": true,
  "settlement": {
    "settled": true,
    "elapsedMs": 850
  }
}
```

---

## 5. Related Tools & Documentation

* [`nova.forward`](nova-forward.md) — Navigate forward in history.
* [`nova.route`](nova-route.md) — Single Page Application client-side routing.
* [`nova.navigate`](nova-navigate.md) — Navigate to an absolute or relative URL.
* [Agent Awareness Gates (AAG)](../../../core-features/aag.md) — Protection against accidental session loss.
