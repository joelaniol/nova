# `nova.navigate`

Navigates an existing browser tab to a specified absolute URL with optional load synchronization, SPA settlement, and screenshot delivery.

---

## 1. Overview

`nova.navigate` is the primary tool for directing browser tabs to web destinations. Beyond traditional browser navigation, Nova integrates **SPA Settlement Detection**, **Session-Preservation Guards**, and **Integrated Visual Proof Sidecars**.

* **Target Scope:** Tab-specific (defaults to the currently active tab).
* **Guards Enforced:** Agent Awareness Gates (AAG) prevent accidental destruction of `sessionStorage`-backed logins unless explicitly confirmed.

---

## 2. Key Capabilities & Features

### A. SPA Settlement Detection (`waitForSettlement`)
Modern Single Page Applications (React, Vue, Angular) complete their HTTP document load (`document.readyState === 'complete'`) long before client-side hydration finishes.
* Setting `waitForSettlement: true` instructs Nova to observe DOM mutation quietness plus network idle states before returning.
* Optional `settlementReadiness`: Pass `{ selector: ".dashboard-container", minMatches: 1, stableForMs: 750 }` to require that a specific UI container is present and stable, preventing long timeouts caused by unrelated background timers or looping animations.

### B. Session-Preservation Protection
If the active page contains authenticated session state in memory or `sessionStorage` (e.g. an active checkout or single-sign-on portal), attempting a hard cross-origin navigation will be blocked by Nova with an **AAG Session Destruction Warning**:
* To navigate within the SPA cleanly without reloading, use `nova.route` instead.
* To open a new destination without losing your current session, use `nova.tab_new`.
* To intentionally proceed with session destruction, pass `force: true` and `confirmSessionDestruction: true`.

### C. Screenshot Sidecar (`includeScreenshot`)
Allows capturing a visual proof crop in the exact same round-trip. If screenshot capture fails (for instance, if the window was minimized), the navigation itself still succeeds, and `structuredContent.screenshotStatus` reports the capture failure reason code without aborting the workflow.

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `url` | `string` | Yes | — | — | Absolute URL to navigate to. Browser targets support allowed schemes such as https:// and trusted local file:// review pages. |
| `waitForLoad` | `boolean` | No | `false` | — | If true, wait for page load before returning. |
| `waitForLoadTimeoutMs` | `integer` | No | `10000` | 0–30000 | Max ms to wait for load (0-30000). Only used when waitForLoad=true. Default 10000 fits typical static pages; SPA-heavy domains (LinkedIn, X, Reddit, large dashboards) often need 15000-20000 — bump explicitly on retry after navigation.wait_for_load_timeout if structuredContent.pageUrl matches the request (URL committed, DOM still settling). |
| `waitForSettlement` | `boolean` | No | `false` | — | If true, observe SPA DOM quiet plus network idle after readyState=complete. Implies waitForLoad=true. Without settlementReadiness this is a heuristic and cannot prove that future timer-scheduled hydration has started. |
| `settlementTimeoutMs` | `integer` | No | `5000` | 1000–15000 | Max ms to wait for settlement (1000-15000). Only used when waitForSettlement=true. |
| `settlementReadiness` | `object` | No | — | — | Optional app-specific postcondition for delayed SPA hydration. Requires waitForSettlement=true. settled=true is withheld until selector reaches minMatches continuously for stableForMs and the page is network-idle. This explicit readiness proof replaces global DOM quiet so unrelated permanent mutations do not veto success. A timeout or invalid selector returns a non-success status with an explicit reasonCode. Use a profile-ready or empty-state container when zero content items is a valid outcome. |
| `settlementReadiness.selector` | `string` | Yes | — | 1–2048 characters | CSS selector for the expected ready surface in the top document. |
| `settlementReadiness.minMatches` | `integer` | No | `1` | 1–10000 | Minimum matching elements required for readiness. |
| `settlementReadiness.stableForMs` | `integer` | No | `750` | 0–5000 | Milliseconds the required match count must remain satisfied before readiness is accepted. |
| `includeScreenshot` | `boolean` | No | `false` | — | If true, attempt a screenshot after navigation. Capture failure does not change the navigation ok/status; inspect screenshotStatus, screenshotReasonCode, screenshotRetryable, and screenshotError. |
| `screenshotMaxWidth` | `integer` | No | — | — | Max screenshot width in pixels. |
| `screenshotMaxHeight` | `integer` | No | — | — | Max screenshot height in pixels. |
| `screenshotFormat` | `string` | No | `"png"` | `png`, `jpeg`, `auto` | Screenshot format; 'auto' picks PNG or JPEG per region. |
| `screenshotQuality` | `integer` | No | `80` | 1–100 | JPEG quality (1-100). Only used when screenshotFormat is 'jpeg'. |
| `outputDetail` | `string` | No | `"full"` | `full`, `compact`, `minimal` | Response verbosity. 'full' (default) is the unchanged payload. 'compact' drops the advisory blocks you did not ask for (pks/pksMeta, discoverySignals, routingHint, taskDiscoveryWarning, byte accounting) and keeps everything you did - state, screenshot, settlement. 'minimal' is the lean envelope: core contract (ok/status/reasonCode/stage/retryable), the navigation proof (url/requestedUrl/loadCompleted/navigationFailed/webErrorStatus/settlement), target and page info, claim/private state, screenshot sidecar status, and the never-suppressible safety warnings. No setting can hide a warning. |
| `pksInclude` | `string` | No | `"auto"` | `auto`, `off`, `summary`, `full` | PKS payload detail level in structuredContent.pks. Default is server setting (initial: auto). |
| `force` | `boolean` | No | `false` | — | When true, bypass the SPA session-preservation gate and force a full top-level document navigation even if the session is likely to be destroyed. Use only when you intentionally want a hard reload on an SPA with memory-only auth. If the target has an authenticated session, you must also pass confirmSessionDestruction=true. |
| `confirmSessionDestruction` | `boolean` | No | `false` | — | Required alongside force=true when navigating away from an authenticated session. Acknowledges that the auth session will be destroyed. Without this flag, force=true on an auth-detected tab is blocked with a recovery hint. |
| `forceAuthProbe` | `boolean` | No | `false` | — | When true, invalidate the current target-scoped auth persistence cache entry and run a fresh live probe on the current page. Use after login/logout or when you suspect the cached auth classification is stale. The response includes authPersistenceCached=false to confirm a live probe was used. |

**`_meta.intent` is required for certain arguments.** Passing a short reason in `_meta.intent` is always safe; a rejected call names the argument that made it required.

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 4. Example Calls

### Basic Navigation with Page Load
```json
{
  "name": "nova.navigate",
  "arguments": {
    "targetId": "tab-1",
    "url": "https://example.com/products",
    "waitForLoad": true
  }
}
```

### SPA Navigation with Explicit Readiness Proof
```json
{
  "name": "nova.navigate",
  "arguments": {
    "targetId": "tab-1",
    "url": "https://app.example.com/dashboard",
    "waitForSettlement": true,
    "settlementReadiness": {
      "selector": ".dashboard-grid",
      "minMatches": 1,
      "stableForMs": 500
    },
    "outputDetail": "minimal"
  }
}
```

---

## 5. Best Practices & Common Traps

* **Creating and Navigating at Once:** If you need a brand-new tab, do not call `nova.tab_new` followed by `nova.navigate`. `nova.tab_new` accepts a `url` parameter directly to create and load the tab in a single call.
* **Domain Notes in Response:** `nova.navigate` checks Nova's Operational Knowledge base. If operator notes exist for the target domain, the response returns `domainNotesAvailable { count, keys }`. Always inspect these notes to learn about site quirks before clicking.

---

## See Also

* [`nova.route`](nova-route.md) — Client-side SPA navigation without document reload.
* [`nova.tab_new`](nova-tab-new.md) — Create a new browser tab.
* [`nova.scroll_smart`](nova-scroll-smart.md) — Scroll the most relevant container after landing, with lazy-load saturation detection.
* [Core Feature: Agent Awareness Gates (AAG)](../../../core-features/aag.md)
