# `nova.forward`

Navigates forward in browser history, with optional load/settlement waiting and a screenshot sidecar.

---

## 1. Overview

`nova.forward` moves the target tab one step forward through its WebView2 history stack. Like [`nova.back`](nova-back.md), this is a same-document history operation — it does not trigger the full-document-unload Agent Awareness Gate that [`nova.navigate`](nova-navigate.md) and [`nova.reload`](nova-reload.md) enforce.

* **Settlement Tracking (`waitForSettlement: true`):** Waits for SPA DOM mutations and network activity to quiet down after the page reports `readyState=complete`.
* **Screenshot Sidecar (`includeScreenshot`):** Optionally captures a screenshot in the same round-trip; a capture failure does not change the navigation result.
* **Output Tiers:** Supports `"full"`, `"compact"`, or `"minimal"` response envelopes.

The `force` parameter exists for parity with `nova.navigate`/`nova.reload`, but since `nova.forward` never runs their full-document-unload gate, it has no effect on this tool.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `force` | `boolean` | No | `false` | — | If true, bypass the SPA/session-preservation AAG gate and allow a hard history forward even when the current tab is flagged as session-sensitive. |
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

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Example Call

```json
{
  "waitForSettlement": true,
  "settlementTimeoutMs": 3000
}
```

---

## 4. Return Value Structure

```json
{
  "ok": true,
  "status": "ok",
  "stage": "history_forward",
  "targetId": "tab-101",
  "waitForLoad": true,
  "loadCompleted": true,
  "pageUrl": "https://example.com/checkout/step2",
  "pageTitle": "Checkout - Step 2",
  "waitForSettlement": true,
  "settlement": {
    "settled": true,
    "quietMs": 200,
    "pendingResources": 0,
    "elapsedMs": 420
  }
}
```

If there is no forward history entry, the call returns `ok: false` with `reasonCode: "navigation.cannot_go_forward"`.

---

## 5. Related Tools & Documentation

* [`nova.back`](nova-back.md) — Navigate backward in history.
* [`nova.route`](nova-route.md) — Single Page Application client-side routing.
* [`nova.navigate`](nova-navigate.md) — Navigate to an absolute or relative URL.
