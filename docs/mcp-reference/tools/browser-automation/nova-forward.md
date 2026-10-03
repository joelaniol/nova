# `nova.forward`

Navigates forward in browser history with automated SPA session preservation, DOM settlement tracking, and guarded navigation gates.

---

## 1. Overview

`nova.forward` advances the browsing context forward along the back/forward history stack. Matching the architecture of [`nova.back`](nova-back.md), Nova distinguishes between safe same-document SPA steps (`pushState`/`popstate`) and hard cross-document unloads.

* **Capability Bundle:** `browser_automation`
* **SPA Settlement Engine:** Waits for microtasks, DOM mutations, and network activity to stabilize (`waitForSettlement: true`).
* **Session Preservation Gate:** Prevents accidental session destruction unless explicitly bypassed via `force: true`.
* **Output Tiers:** Supports `"full"`, `"compact"`, or `"minimal"` response envelopes.

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`targetId`** | `string` | No | `"active"` | Target tab ID from `nova.tabs`, or `"active"`. |
| **`waitForLoad`** | `boolean` | No | `false` | Wait for `document.readyState === 'complete'`. |
| **`waitForSettlement`**| `boolean`| No | `false` | For SPAs: wait for post-load DOM settlement. Implies `waitForLoad: true`. |
| **`waitForLoadTimeoutMs`**| `integer`| No | `10000` | Max milliseconds to wait for page load (0–30,000 ms). |
| **`settlementTimeoutMs`** | `integer`| No | `5000` | Max milliseconds to wait for SPA DOM settlement (1,000–15,000 ms). |
| **`force`** | `boolean` | No | `false` | Bypass session preservation gates and allow hard document leave. |
| **`includeScreenshot`**| `boolean`| No | `false` | Include screenshot sidecar upon load completion. |
| **`outputDetail`** | `string` | No | `"full"` | Envelope verbosity: `"full"`, `"compact"`, or `"minimal"`. |
| **`agentId`** | `string` | No | `"default"` | Agent identity for claim lease verification. |

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
  "targetId": "tab-101",
  "url": "https://example.com/checkout/step2",
  "loadCompleted": true,
  "settlement": {
    "settled": true,
    "elapsedMs": 420
  }
}
```

---

## 5. Related Tools & Documentation

* [`nova.back`](nova-back.md) — Navigate backward in history.
* [`nova.route`](nova-route.md) — Single Page Application client-side routing.
* [`nova.navigate`](nova-navigate.md) — Navigate to an absolute or relative URL.
