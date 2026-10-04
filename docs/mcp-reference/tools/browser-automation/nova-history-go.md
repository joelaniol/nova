# `nova.history_go`

> **Navigates forward or backward in tab history by a relative delta offset.**

* **Core Feature Guide:** [Input Dispatch & Shadow DOM Traversal](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.history_go` jumps within the tab's session history, either by a relative `offset` (e.g. -1 for back, +1 for forward, -3 to skip back 3 steps) or to a stable `entryId` from `nova.history_get`. Pass exactly one of the two. The response example below is an excerpt.

An offset outside the history returns `ok: false` with `reasonCode: "navigation.history_index_out_of_range"`; an unknown `entryId` returns `navigation.history_entry_not_found`. A jump of zero steps returns `status: "noop"`. Multi-step jumps on a tab whose session Nova protects need `force: true` (`navigation.history_multi_step_requires_force` otherwise).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `entryId` | `integer` | No | — | — | Stable entryId from nova.history_get. Mutually exclusive with offset. |
| `offset` | `integer` | No | — | — | Relative step count from currentIndex. -1 = back one step, +2 = forward two steps. Mutually exclusive with entryId. |
| `force` | `boolean` | No | `false` | — | If true, bypass the SPA/session-preservation AAG gate. Required for multi-step jumps on session-flagged tabs. |
| `confirmSessionDestruction` | `boolean` | No | `false` | — | Required alongside force=true when the tab has an authenticated session. Acknowledges that the session may be destroyed by the jump. |
| `waitForLoad` | `boolean` | No | `false` | — | If true, wait for page load before returning. |
| `waitForLoadTimeoutMs` | `integer` | No | `10000` | 0–30000 | Max ms to wait for load (0-30000). Only used when waitForLoad=true. |
| `waitForSettlement` | `boolean` | No | `false` | — | If true, wait for SPA DOM settlement after readyState=complete. Implies waitForLoad=true. |
| `settlementTimeoutMs` | `integer` | No | `5000` | 1000–15000 | Max ms to wait for settlement (1000-15000). Only used when waitForSettlement=true. |
| `includeScreenshot` | `boolean` | No | `false` | — | If true and load completes, include a screenshot in the response. Screenshot delivery is an optional sidecar: if capture fails, this result stays authoritative and structuredContent.screenshotStatus/screenshotReasonCode/screenshotRetryable/screenshotError describe the capture-only failure - do not repeat the action to get the image. |
| `screenshotMaxWidth` | `integer` | No | — | — | Max screenshot width in pixels. |
| `screenshotMaxHeight` | `integer` | No | — | — | Max screenshot height in pixels. |
| `screenshotFormat` | `string` | No | `"png"` | `png`, `jpeg`, `auto` | Screenshot format; 'auto' picks PNG or JPEG per region. |
| `screenshotQuality` | `integer` | No | `80` | 1–100 | JPEG quality (1-100). Only used when screenshotFormat is 'jpeg'. |
| `outputDetail` | `string` | No | `"full"` | `full`, `compact`, `minimal` | Response verbosity. 'full' (default) is the unchanged payload. 'compact' drops the advisory blocks you did not ask for (pks/pksMeta, discoverySignals, routingHint, taskDiscoveryWarning, byte accounting) and keeps everything you did - state, screenshot, settlement. 'minimal' is the lean envelope: core contract (ok/status/reasonCode/stage/retryable), the navigation proof (url/requestedUrl/loadCompleted/navigationFailed/webErrorStatus/settlement), target and page info, claim/private state, screenshot sidecar status, and the never-suppressible safety warnings. No setting can hide a warning. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_history_go",
  "arguments": {
    "targetId": "tab-1",
    "offset": -2,
    "waitForLoad": true
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "History jumped -2 step(s) (page loaded)."
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "ok": true,
    "status": "ok",
    "stage": "load_complete",
    "retryable": false,
    "waitForLoad": true,
    "loadCompleted": true,
    "waitedMs": 412,
    "waitForSettlement": false,
    "pageTitle": "Example Domain",
    "pageUrl": "https://example.com/",
    "targetIndex": 1,
    "targetEntryId": 7,
    "movedSteps": -2
  }
}
```

---

## 4. Operational Best Practices

* **Bounds Checking:** Verify current stack boundaries with `nova.history_get` before passing large offsets.

---

## 5. Related Tools

* [`nova.history_get`](nova-history-get.md)
* [`nova.back`](nova-back.md)
* [`nova.forward`](nova-forward.md)
