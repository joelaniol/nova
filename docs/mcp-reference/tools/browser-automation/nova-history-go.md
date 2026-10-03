# `nova.history_go`

> **Navigates forward or backward in tab history by a relative delta offset.**

* **Capability Bundle:** `browser_automation`
* **Security Tier:** Tier 2 (Navigation)
* **Core Feature Guide:** [Humanized Input & Navigation](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.history_go` traverses the navigation stack by integer offset (e.g. -1 for back, +1 for forward, -3 to skip back 3 steps).

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional metadata. Provide _meta.intent (a short reason) for high-impact tools. A tool's annotations.intentRequired in tools/list tells you up front: 'always' means intent is mandatory, 'conditional' means it becomes mandatory for certain arguments (e.g. includeValues=true), absent means never. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `confirmSessionDestruction` | `boolean` | No | Required alongside force=true when the tab has an authenticated session. Acknowledges that the session may be destroyed by the jump. |
| `entryId` | `integer` | No | Stable entryId from nova.history_get. Mutually exclusive with offset. |
| `force` | `boolean` | No | If true, bypass the SPA/session-preservation AAG gate. Required for multi-step jumps on session-flagged tabs. |
| `includeScreenshot` | `boolean` | No | If true and load completes, include a screenshot in the response. Screenshot delivery is an optional sidecar: if capture fails, this result stays authoritative and structuredContent.screenshotStatus/screenshotReasonCode/screenshotRetryable/screenshotError describe the capture-only failure - do not repeat the action to get the image. |
| `offset` | `integer` | No | Relative step count from currentIndex. -1 = back one step, +2 = forward two steps. Mutually exclusive with entryId. |
| `outputDetail` | `string` | No | Response verbosity. 'full' (default) is the unchanged payload. 'compact' drops the advisory blocks you did not ask for (pks/pksMeta, discoverySignals, routingHint, taskDiscoveryWarning, byte accounting) and keeps everything you did - state, screenshot, settlement. 'minimal' is the lean envelope: core contract (ok/status/reasonCode/stage/retryable), the navigation proof (url/requestedUrl/loadCompleted/navigationFailed/webErrorStatus/settlement), target and page info, claim/private state, screenshot sidecar status, and the never-suppressible safety warnings. No setting can hide a warning. |
| `screenshotFormat` | `string` | No | Screenshot format. |
| `screenshotMaxHeight` | `integer` | No | Max screenshot height in pixels. |
| `screenshotMaxWidth` | `integer` | No | Max screenshot width in pixels. |
| `screenshotQuality` | `integer` | No | JPEG quality (1-100). Only used when screenshotFormat is 'jpeg'. |
| `settlementTimeoutMs` | `integer` | No | Max ms to wait for settlement (1000-15000). Only used when waitForSettlement=true. |
| `targetId` | `string` | No | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `waitForLoad` | `boolean` | No | If true, wait for page load before returning. |
| `waitForLoadTimeoutMs` | `integer` | No | Max ms to wait for load (0-30000). Only used when waitForLoad=true. |
| `waitForSettlement` | `boolean` | No | If true, wait for SPA DOM settlement after readyState=complete. Implies waitForLoad=true. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_history_go",
  "arguments": {
    "targetId": "tab-1",
    "delta": -2
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Navigated 2 steps backward in tab history."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "newIndex": 1,
    "url": "https://example.com"
  }
}
```

---

## 4. Operational Best Practices

* **Bounds Checking:** Verify current stack boundaries with `nova.history_get` before passing large deltas.

---

## 5. Related Tools

* [`nova.history_get`](nova-history-get.md)
* [`nova.back`](nova-back.md)
* [`nova.forward`](nova-forward.md)
