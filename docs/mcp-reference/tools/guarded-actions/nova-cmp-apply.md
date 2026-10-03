# `nova.cmp_apply`

Applies a typed privacy consent policy directly through recognized Consent Management Platform (CMP) vendor JavaScript APIs (OneTrust, Sourcepoint, Cookiebot), verifying consent vector state before and after execution.

---

## 1. Overview

Dismissing cookie consent dialogs through naive UI clicking is fragile: consent banners frequently embed cross-origin iframes (e.g. Sourcepoint TCF v2), employ multi-step accordion settings, or render non-standard custom checkboxes.

`nova.cmp_apply` interfaces directly with the CMP's programmatic JavaScript APIs:
* **Supported CMP Vendors:** OneTrust, Sourcepoint (TCF v2), and Cookiebot (`window.Cookiebot.submitCustomConsent`).
* **ConsentStateVector Verification:** Reads the active consent state vector before and after execution, ensuring the privacy flags were actually written into the vendor's storage and cookies.
* **Autonomous-Safe Default (`RejectOptional`):** Automatically rejects advertising, analytics, and marketing cookies while preserving strictly necessary operational cookies.
* **AcceptAll Safeguard:** Blanket acceptance of tracking cookies (`AcceptAll`) is hard-gated to prevent rogue autonomous consent inflation.
* **User Choice Preservation:** If the human user previously made an explicit consent choice on this domain, Nova preserves the user's decision (`user_choice_preserved`) and prevents autonomous overrides.

* **Cross-Origin Iframe Piercing:** Communicates with embedded iframe banners via top-frame `__tcfapi` messaging.
* **Pre-Claim Requirement:** The calling agent must hold an active tab claim via [`nova.tab_claim`](../browser-automation/nova-tab-claim.md).
* **Automatic Fallback:** If no recognized CMP adapter is detected (`failureCode: "no_adapter"`), agents fall back to visual blocker dismissal via [`nova.dismiss_blockers`](../browser-automation/nova-dismiss-blockers.md).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | Yes | — | — | Target tab or sandbox id from nova.tabs. |
| `agentId` | `string` | No | — | — | Agent identifier (used for audit trail; optional). |
| `intent` | `object` | No | — | — | Typed consent intent. Omit to use the AppSettings.DefaultConsentPolicy default. |
| `intent.mode` | `string` | No | — | `RejectOptional`, `AcceptAll`, `OpenManage`, `PreserveExisting`, `Revoke` | Consent mode. RejectOptional = strict-necessary only (autonomous-safe default). AcceptAll is hard-gated. PreserveExisting = no-op verify (returns the current ConsentStateVector without mutating). OpenManage/Revoke are reserved values and rejected. |
| `intent.allowStrictNecessary` | `boolean` | No | — | — | — |
| `intent.allowPreferences` | `boolean` | No | — | — | — |
| `intent.allowStatistics` | `boolean` | No | — | — | — |
| `intent.allowMarketing` | `boolean` | No | — | — | — |
| `intent.objectToLegitimateInterest` | `boolean` | No | — | — | — |
| `intent.doNotSellOrShare` | `boolean` | No | — | — | — |
| `intent.personalizedAds` | `boolean` | No | — | — | — |
| `intent.frameworkHint` | `string` | No | — | `Unknown`, `TcfEu`, `GppUs`, `VendorCustom` | — |
| `intent.userPolicyOrigin` | `string` | No | — | `user_per_site`, `user_global`, `agent_task`, `learned_default` | Provenance of the policy decision. Required token 'user_per_site' when calling AcceptAll. |
| `mode` | `string` | No | — | `auto`, `dry_run` | Tool execution mode. 'auto' = run apply immediately. 'dry_run' = read ConsentStateVector and surface preState only, no mutation. Reserved value 'ask' returns -32002. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
<!-- /generated:parameters -->

---

## 3. Example Calls

### Autonomous Reject-Optional Apply
```json
{
  "targetId": "tab-101",
  "mode": "auto",
  "intent": {
    "mode": "RejectOptional"
  }
}
```

### Inspect Existing Consent State Vector (Dry Run)
```json
{
  "targetId": "tab-101",
  "mode": "dry_run"
}
```

---

## 4. Return Value Structure

```json
{
  "ok": true,
  "verified": true,
  "targetId": "tab-101",
  "adapter": "OneTrust",
  "preState": {
    "strictlyNecessary": true,
    "performance": true,
    "targeting": true
  },
  "postState": {
    "strictlyNecessary": true,
    "performance": false,
    "targeting": false
  },
  "userChoicePresent": false,
  "retryable": false,
  "nextAction": "none"
}
```

If the site does not use a supported CMP vendor:
```json
{
  "ok": false,
  "verified": false,
  "targetId": "tab-101",
  "failureCode": "no_adapter",
  "retryable": false,
  "nextAction": "call_dismiss_blockers",
  "guidance": "No recognized CMP API detected. Use nova.dismiss_blockers to click visible banner dismiss buttons."
}
```

---

## 5. Related Tools & Documentation

* [`nova.dismiss_blockers`](../browser-automation/nova-dismiss-blockers.md) — Visual fallback for closing arbitrary overlay dialogs.
* [`nova.tab_claim`](../browser-automation/nova-tab-claim.md) — Lease a tab before applying consent mutations.
* [Closed-Loop Systems Architecture](../../../core-features/closed-loop-system.md) — Verification contracts and consent policy enforcement.
