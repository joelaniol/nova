# `nova.reload`

Reloads the active tab with configurable cache bypassing, SPA settlement verification, session-destruction protection, and stuck-renderer recovery.

---

## 1. Overview

Reloading a tab during automated operations must be handled with extreme care: if an agent triggers a reload on an authenticated banking portal, social network feed, or checkout form, session tokens stored in memory may be wiped out.

`nova.reload` protects against unintended session destruction through **Agent Awareness Gates (AAG)**:
* **Session Destruction Confirmation (`confirmSessionDestruction`):** If Nova's Auth Surface Detection (ASD) identifies an active authenticated session, calling reload with `force: true` is blocked unless `confirmSessionDestruction: true` is also explicitly supplied.
* **Hard Reload (`hard: true`):** Bypasses browser HTTP caching to fetch fresh assets.
* **Renderer Crash Recovery (`recoverRenderer: true`):** If a heavy script or GPU deadlock freezes the WebView2 renderer process (returning `cdp.renderer_stalled`), passing `recoverRenderer: true` terminates and respawns a fresh renderer process at the same URL.

* **Capability Bundle:** `browser_automation`, `app_shell_recovery`
* **Safe Same-Origin Defaults:** Reload is evaluated as same-origin rather than cross-origin navigation.
* **Renderer Deadlock Self-Healing:** Seamlessly recovers tabs frozen by infinite loops or memory pressure.
* **Settlement Tracking:** Waits for DOM mutation queues to settle (`waitForSettlement: true`).

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`targetId`** | `string` | No | `"active"` | Target tab ID from `nova.tabs`, or `"active"`. |
| **`hard`** | `boolean` | No | `false` | When `true`, ignores HTTP cache (hard refresh). |
| **`waitForLoad`** | `boolean` | No | `false` | Wait for `document.readyState === 'complete'`. |
| **`waitForSettlement`**| `boolean`| No | `false` | Wait for SPA post-load DOM settlement. |
| **`waitForLoadTimeoutMs`**| `integer`| No | `10000` | Max milliseconds to wait for page load (0–30,000 ms). |
| **`settlementTimeoutMs`** | `integer`| No | `5000` | Max milliseconds to wait for DOM settlement (1,000–15,000 ms). |
| **`force`** | `boolean` | No | `false` | Bypass session preservation gates on sensitive tabs. |
| **`confirmSessionDestruction`**| `boolean`| No | `false`| Required alongside `force: true` when reloading an authenticated session. |
| **`recoverRenderer`** | `boolean`| No | `false` | Recreate a frozen or stalled WebView2 renderer process. |
| **`includeScreenshot`**| `boolean`| No | `false` | Include screenshot sidecar upon load completion. |
| **`outputDetail`** | `string` | No | `"full"` | Envelope verbosity: `"full"`, `"compact"`, or `"minimal"`. |
| **`agentId`** | `string` | No | `"default"` | Agent identity for claim lease verification. |

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
  "targetId": "tab-101",
  "url": "https://example.com/dashboard",
  "loadCompleted": true,
  "hardReload": false,
  "settlement": {
    "settled": true,
    "elapsedMs": 920
  }
}
```

---

## 5. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `AAG Block: Active auth session detected` | Attempted to reload an authenticated tab without explicit confirmation. | Pass both `force: true` and `confirmSessionDestruction: true`. |
| `reload.recover_renderer_not_stalled` | `recoverRenderer: true` was called on a tab whose renderer is healthy. | Use standard `nova.reload` without `recoverRenderer`. |

---

## 6. Related Tools & Documentation

* [`nova.navigate`](nova-navigate.md) — Navigate to a new URL.
* [`nova.route`](nova-route.md) — Same-document client-side routing.
* [Agent Awareness Gates (AAG)](../../../core-features/aag.md) — Session-preservation gates and auth surface detection.
* [Auth Surface Detection (ASD)](../../../core-features/auth-surface-detection.md) — How Nova identifies active login sessions.
