# `nova.cmp_apply`

Applies a typed privacy consent policy directly through recognized Consent Management Platform (CMP) vendor JavaScript APIs (OneTrust, Sourcepoint, Cookiebot, Usercentrics v3), verifying consent vector state before and after execution.

---

## 1. Overview

Dismissing cookie consent dialogs through naive UI clicking is fragile: consent banners frequently embed cross-origin iframes (e.g. Sourcepoint TCF v2), employ multi-step accordion settings, or render non-standard custom checkboxes.

`nova.cmp_apply` interfaces directly with the CMP's programmatic JavaScript APIs:
* **Supported CMP Vendors:** OneTrust, Sourcepoint (TCF v2), Cookiebot (`window.Cookiebot.submitCustomConsent`) and the Usercentrics Browser CMP v3 (`window.__ucCmp`; the reject also closes the banner). Usercentrics v2 (`#usercentrics-root` only) answers `no_adapter`.
* **ConsentStateVector Verification:** Reads the vendor's consent state before and after the call (framework, CMP id/version, TCF purpose flags, OneTrust group states, Cookiebot category flags, or the Usercentrics consent type and category states, depending on the detected vendor) and compares them to decide whether the intent was actually applied.
* **Autonomous-Safe Default (`RejectOptional`):** Rejects advertising, analytics, and marketing cookies while preserving strictly necessary operational cookies.
* **AcceptAll Currently Blocked:** `intent.mode: "AcceptAll"` is rejected outright for every automated call (JSON-RPC error `-32035`, `failureCode: "accept_all_blocked"`) because the verification needed to trust a per-site accept claim is not wired up yet. Use `RejectOptional`, or let the human user accept all cookies manually in the banner.
* **User Choice Preservation:** For OneTrust, Cookiebot and Usercentrics, if the pre-state already shows an explicit prior user accept of an optional category, Nova preserves it (`user_choice_preserved`) instead of overriding it with `RejectOptional`. TCF/Sourcepoint state cannot currently be decoded well enough to detect this, so that vendor always applies the requested intent.

* **Cross-Origin Iframe Awareness:** For Sourcepoint, the `__tcfapi` function it relies on commonly lives in the top frame even when the consent UI itself renders inside a cross-origin iframe.
* **Automatic Fallback:** If no recognized CMP adapter is detected (`failureCode: "no_adapter"`), agents fall back to visual blocker dismissal via [`nova.dismiss_blockers`](nova-dismiss-blockers.md).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | Yes | — | — | Target tab or sandbox id from nova.tabs. |
| `agentId` | `string` | No | — | — | Agent identifier (used for audit trail; optional). |
| `intent` | `object` | No | — | — | Typed consent intent. Omit to use the default cookie choice from Nova's settings. |
| `intent.mode` | `string` | No | — | `RejectOptional`, `AcceptAll`, `OpenManage`, `PreserveExisting`, `Revoke` | Consent mode. RejectOptional = strict-necessary only (autonomous-safe default). AcceptAll is always refused (the user accepts manually). PreserveExisting = no-op verify (returns the current ConsentStateVector without mutating). OpenManage/Revoke are reserved values and rejected. |
| `intent.allowStrictNecessary` | `boolean` | No | — | — | Whether strictly necessary cookies are allowed (always true). |
| `intent.allowPreferences` | `boolean` | No | — | — | Whether preference / personalization cookies are allowed. |
| `intent.allowStatistics` | `boolean` | No | — | — | Whether analytics and performance cookies are allowed. |
| `intent.allowMarketing` | `boolean` | No | — | — | Whether advertising and tracking cookies are allowed. |
| `intent.objectToLegitimateInterest` | `boolean` | No | — | — | Whether to object to legitimate interest data processing. |
| `intent.doNotSellOrShare` | `boolean` | No | — | — | Assert US privacy rights (CCPA/CPRA) against selling or sharing personal data. |
| `intent.personalizedAds` | `boolean` | No | — | — | Whether personalized advertising is permitted. |
| `intent.frameworkHint` | `string` | No | — | `Unknown`, `TcfEu`, `GppUs`, `VendorCustom` | CMP standard framework: Unknown, TcfEu, GppUs, or VendorCustom. |
| `intent.userPolicyOrigin` | `string` | No | — | `user_per_site`, `user_global`, `agent_task`, `learned_default` | Provenance of the policy decision (recorded in the audit log). |
| `mode` | `string` | No | — | `auto`, `dry_run` | Tool execution mode. 'auto' = run apply immediately. 'dry_run' = read ConsentStateVector and surface preState only, no mutation. Reserved value 'ask' returns -32002. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
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
  "status": "ok",
  "mode": "auto",
  "vendor": "onetrust",
  "route": "top_frame",
  "verified": true,
  "verifyMethod": "group_state_diff",
  "failureCode": "ok",
  "retryable": false,
  "nextAction": "none",
  "userChoicePresent": false,
  "auditLogged": true,
  "preState": {
    "framework": "Unknown",
    "cmpVendor": "onetrust",
    "oneTrustGroups": { "C0001": true, "C0002": true, "C0003": true, "C0004": true },
    "source": "OneTrust.GetDomainData"
  },
  "postState": {
    "framework": "Unknown",
    "cmpVendor": "onetrust",
    "oneTrustGroups": { "C0001": true, "C0002": false, "C0003": false, "C0004": false },
    "source": "OneTrust.GetDomainData"
  }
}
```
`preState`/`postState` are shortened above; the full `ConsentStateVector` projection also carries `cmpId`, `cmpVersion`, `tcfPolicyVersion`, `gdprApplies`, `eventStatus`, the Cookiebot category flags, `tcStringHash`, and `capturedUtc`.

If the site does not use a supported CMP vendor:
```json
{
  "ok": false,
  "status": "failed",
  "reasonCode": "cmp.no_adapter",
  "vendor": "unknown",
  "verified": false,
  "failureCode": "no_adapter",
  "failureReason": "No registered CMP adapter detected in top frame. Fall back to nova.dismiss_blockers or pixel-click.",
  "retryable": false,
  "nextAction": "fallback_dismiss_blockers"
}
```

A call with `intent.mode: "AcceptAll"` does not return a tool result at all; it is rejected as a JSON-RPC error (`-32035`) with `data.failureCode: "accept_all_blocked"` and `data.nextAction: "escalate_to_user"`.

---

## 5. Operational Best Practices

* **Vendor API First, Visual Fallback Second:** Always invoke `nova.cmp_apply` as the primary defense against cookie consent barriers. By communicating directly with underlying CMP JavaScript SDKs (OneTrust, Cookiebot, TCF v2, Usercentrics), it avoids fragile DOM selectors and dark pattern traps. If the response reports `failureCode: "no_adapter"`, cleanly transition to [`nova.dismiss_blockers`](nova-dismiss-blockers.md).
* **Strict Privacy Policy Enforcement:** Nova's consent pipeline strictly blocks automated `AcceptAll` directives (triggering error code `-32035`). Agents must specify privacy-preserving intents such as `intent.mode: "RejectAll"` or configure explicit granular categories (`necessary: true`, `analytics: false`, `marketing: false`).
* **Audit State Vector Diffs:** Review `preState` and `postState` in the response to verify that non-essential tracking categories were verifiably toggled off in the vendor's internal consent ledger.

---

## 6. Related Tools & Documentation

* [`nova.dismiss_blockers`](nova-dismiss-blockers.md) — Visual fallback for closing arbitrary overlay dialogs.
* [Consent Management Architecture Overview](../../../core-features/consent-management/README.md) — Core architecture overview of Nova's privacy and blocker subsystem.
* [Programmatic CMP Vendor API Engine](../../../core-features/consent-management/cmp-engine/README.md) — Deep dive into the 8-step pipeline, vendor protocols, and state vector verification.
* [3-Stage Hijack & Dark Pattern Defense](../../../core-features/consent-management/hijack-protection/README.md) — Polarity scoring, sibling contrast, and cross-origin iframe boundaries.
* [`nova.tab_claim`](../browser-automation/nova-tab-claim.md) — Lease a tab before applying consent mutations.
* [Closed-Loop Systems Architecture](../../../core-features/closed-loop-system-cls/README.md) — Verification contracts and consent policy enforcement.
