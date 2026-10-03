# `nova.navigate`

Navigates an existing browser tab to a specified absolute URL with optional load synchronization, SPA settlement, and screenshot delivery.

---

## 1. Overview

`nova.navigate` is the primary tool for directing browser tabs to web destinations. Beyond traditional browser navigation, Nova integrates **SPA Settlement Detection**, **Session-Preservation Guards**, and **Integrated Visual Proof Sidecars**.

* **Capability Bundle:** `browser_automation`
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

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`url`** | `string` | **Yes** | � | Absolute URL to navigate to (`https://...` or trusted `file://...`). |
| **`targetId`** | `string` | No | `"active"` | Target tab ID from `nova.tabs` or `"active"`. |
| **`waitForLoad`** | `boolean` | No | `false` | Block until `document.readyState === 'complete'`. |
| **`waitForLoadTimeoutMs`** | `integer` | No | `10000` | Max milliseconds to wait for load completion (0�30,000 ms). Heavy SPAs often need 15,000�20,000 ms. |
| **`waitForSettlement`** | `boolean` | No | `false` | Wait for post-load DOM quietness and network idle. Implies `waitForLoad=true`. |
| **`settlementTimeoutMs`** | `integer` | No | `5000` | Max milliseconds to wait for settlement (1,000�15,000 ms). |
| **`settlementReadiness`** | `object` | No | `null` | Explicit ready postcondition: `{ selector, minMatches?, stableForMs? }`. |
| **`includeScreenshot`** | `boolean` | No | `false` | Attempt an immediate screenshot after navigation settles. |
| **`screenshotFormat`** | `string` | No | `"png"` | `"png"` or `"jpeg"`. |
| **`screenshotQuality`** | `integer` | No | `80` | JPEG quality (1�100). |
| **`outputDetail`** | `string` | No | `"full"` | `"minimal"`, `"compact"`, or `"full"`. |
| **`force`** | `boolean` | No | `false` | Bypass the SPA session-preservation gate. |
| **`confirmSessionDestruction`**| `boolean` | No | `false` | Mandatory acknowledgement when `force=true` is used on authenticated pages. |
| **`agentId`** | `string` | No | `"default"`| Agent identity for claim validation. |

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

* [`nova.route`](nova-navigate.md) � Client-side SPA navigation without document reload.
* [`nova.tab_new`](nova-tab-new.md) � Create a new browser tab.
* [`nova.scroll_smart`](nova-scroll-smart.md) � Natural wheel scrolling after landing.
* [Core Feature: Agent Awareness Gates (AAG)](../../../core-features/aag.md)
