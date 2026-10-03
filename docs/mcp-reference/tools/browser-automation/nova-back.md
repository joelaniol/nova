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
