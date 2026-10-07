# `nova.reload`

Reloads the active tab with configurable cache bypassing, SPA settlement verification, session-destruction protection, and stuck-renderer recovery.

---

## 1. Overview

Reloading a tab during automated operations must be handled with extreme care: if an agent triggers a reload on an authenticated banking portal, social network feed, or checkout form, session tokens stored in memory may be wiped out.

`nova.reload` protects against unintended session destruction through **Agent Awareness Gates (AAG)**:
* **Session Destruction Confirmation (`confirmSessionDestruction`):** Because a reload keeps the same URL, cookie- and `sessionStorage`-backed auth survive it. Ephemeral (memory-only) auth does not: reloading destroys the in-memory token. When Nova's Auth Surface Detection (ASD) classifies the page's auth as ephemeral, reload is blocked and requires both `force: true` and `confirmSessionDestruction: true` to proceed.
* **Hard Reload (`hard: true`):** Bypasses browser HTTP caching to fetch fresh assets.
* **Renderer Crash Recovery (`recoverRenderer: true`):** If a heavy script or GPU deadlock freezes the WebView2 renderer process (returning `cdp.renderer_stalled`), passing `recoverRenderer: true` terminates and respawns a fresh renderer process at the same URL.

* **Safe Same-Origin Defaults:** Reload is evaluated as same-origin rather than cross-origin navigation.
* **Renderer Deadlock Self-Healing:** Seamlessly recovers tabs frozen by infinite loops or memory pressure.
* **Settlement Tracking:** Waits for DOM mutation queues to settle (`waitForSettlement: true`).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `hard` | `boolean` | No | `false` | — | If true, bypass cache (hard reload). If false, normal reload using cached resources. |
| `force` | `boolean` | No | `false` | — | If true, bypass the SPA/session-preservation AAG gate and allow a full-document reload even when the current tab is flagged as session-sensitive. If the target has an authenticated session, you must also pass confirmSessionDestruction=true. |
| `confirmSessionDestruction` | `boolean` | No | `false` | — | Required alongside force=true when reloading an authenticated session. Acknowledges that the auth session may be destroyed. Without this flag, force=true on an auth-detected tab is blocked with a recovery hint. |
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
| `recoverRenderer` | `boolean` | No | `false` | — | Recreate the tab's renderer and load the same URL in a fresh one - Chrome's 'Exit page' for an unresponsive tab. Unsaved input on the page is lost. Only on a tab you claimed, and only while the tab is known not to answer (its calls return cdp.renderer_stalled); otherwise refused with reload.recover_renderer_not_claimed / reload.recover_renderer_not_stalled. hard/force are ignored with it; waitForLoad applies. |
| `agentId` | `string` | No | `"default"` | — | Your agent identity. recoverRenderer requires that this agent holds the claim on the tab. |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Example Calls

### Standard Refresh with SPA Settlement
```json
{
  "waitForSettlement": true,
  "settlementTimeoutMs": 3000
}
```

### Hard Cache-Bypassing Reload
```json
{
  "hard": true,
  "waitForLoad": true
}
```

### Force Reload on Authenticated Tab (Explicit Session Destruction)
```json
{
  "force": true,
  "confirmSessionDestruction": true,
  "waitForLoad": true
}
```

### Recover Frozen Renderer Process
```json
{
  "recoverRenderer": true,
  "waitForLoad": true
}
```

---

## 4. Return Value Structure

```json
{
  "ok": true,
  "status": "ok",
  "stage": "load_complete",
  "targetId": "tab-101",
  "hard": false,
  "waitForLoad": true,
  "loadCompleted": true,
  "pageUrl": "https://example.com/dashboard",
  "pageTitle": "Dashboard",
  "waitForSettlement": true,
  "settlement": {
    "settled": true,
    "quietMs": 400,
    "pendingResources": 0,
    "elapsedMs": 920
  }
}
```

---

## 5. Common Errors & Troubleshooting

| reasonCode | Cause | Corrective Action |
| :--- | :--- | :--- |
| `navigate.session_destruction_requires_confirmation` | `force: true` on a tab with an active authenticated session, without `confirmSessionDestruction`. | Pass both `force: true` and `confirmSessionDestruction: true`, or reload without `force` if the session should be preserved. |
| `reload.recover_renderer_not_stalled` | `recoverRenderer: true` was called on a tab whose renderer is healthy. | Use standard `nova.reload` without `recoverRenderer`. |
| `reload.recover_renderer_not_claimed` | `recoverRenderer: true` was called on a tab not claimed by the calling `agentId`. | Claim the tab first, or call without `recoverRenderer`. |
| `reload.recover_renderer_failed` | The target was not a recreatable browser tab, or it was already closed. | Verify the `targetId` with `nova.tabs` before retrying. |

---

## 6. Related Tools & Documentation

* [`nova.navigate`](nova-navigate.md) — Navigate to a new URL.
* [`nova.route`](nova-route.md) — Same-document client-side routing.
* [Agent Awareness Gates (AAG)](../../../core-features/agent-awareness-gates-aag/README.md) — Session-preservation gates and auth surface detection.
* [Auth Surface Detection (ASD)](../../../core-features/auth-surface-detection-asd/README.md) — How Nova identifies active login sessions.
