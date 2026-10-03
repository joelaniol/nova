# `nova.pks_match`

Matches live page observations against registered Phenomenological Knowledge Store (PKS) fingerprints and global platform templates to identify active UI phenomena.

---

## 1. Overview

When an agent lands on a complex web page and detects an unfamiliar modal, login gate, or consent banner, it uses `nova.pks_match` to check whether this pattern has been previously solved and cataloged. Nova scores the observed signals against domain-specific phenomena first, and falls back to universal platform templates (e.g. standard OneTrust or Didomi cookie templates) if needed.

* **Capability Bundle:** `pks_and_learning`, `domain_knowledge`
* **Typed Signal Matching:** Compares DOM selectors, visible text fragments, vendor API markers, and layout metrics.
* **Ranked Results (`topK`):** Returns the top candidate along with confidence scores and evidence breakdowns.
* **Near-Miss Diagnostics:** When confidence falls just below the threshold, near-miss diagnostics help the agent determine whether a slight site redesign has occurred.

---

## 2. Signal Types

The `observation.signals` array accepts structured evidence items:

| Signal Kind | Matching Strategy | Example |
| :--- | :--- | :--- |
| **`dom`** | Presence of specific CSS selectors or DOM attributes. | `{ "kind": "dom", "match": "#user-consent-dialog" }` |
| **`text`** | Presence of literal UI text or button strings. | `{ "kind": "text", "match": "Accept All Cookies" }` |
| **`vendor`** | Presence of JavaScript vendor window objects or APIs. | `{ "kind": "vendor", "match": "__tcfapi" }` |
| **`layout`** | Geometry indicators (e.g. full-screen backdrop overlay). | `{ "kind": "layout", "match": "fixed_full_screen_backdrop" }` |
| **`interaction`** | Behavioral indicators (e.g. scroll wheel locked). | `{ "kind": "interaction", "match": "body_scroll_locked" }` |

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `scope` | `string` | Yes | — | — | Domain scope. |
| `observation` | `object` | Yes | — | — | What was observed: signals present on the page. |
| `observation.signals` | `array` of `object` | No | — | — | Observed signals used for matching. Each signal provides kind, match, and optional locale. |
| `observation.type` | `string` | No | — | `consent_cmp`, `modal`, `paywall`, `login_wall`, `layout_shift`, `native_dialog`, `popover_open`, `custom` | Optional type filter for candidate ranking. Phenomenon type. 'consent_cmp' = cookie/consent manager surface, 'modal' = generic blocking overlay or dialog, 'paywall' = subscription/payment gate, 'login_wall' = sign-in gate, 'layout_shift' = disruptive UI shift without a classic overlay, 'native_dialog' = browser/native prompt such as permission or file picker, 'popover_open' = anchored popover/dropdown surface, 'custom' = uncategorized site-specific phenomenon. |
| `topK` | `integer` | No | `1` | 1–10 | Optional number of ranked matches to return (1-10). Default 1. |
| `context` | `object` | No | — | — | Optional context filter. Mismatch against each phenomenon's effective context (phenomenon override with domain fallback) excludes that candidate. |
| `context.device` | `any` | No | — | — | Device type filter for phenomenon matching. Use null or omit to leave the device filter unset. |
| `context.locale` | `string or null` | No | — | ≥ 1 characters | Optional locale filter such as 'de-DE'. Use null or omit to leave the locale filter unset. |
| `context.auth` | `any` | No | — | — | Authentication state. 'anonymous' = not signed in, 'logged_in' = signed in, 'unknown' = not enough evidence to classify. Use null or omit to leave the auth filter unset. |
| `context.route` | `string or null` | No | — | ≥ 1 characters | Optional route segment filter. Examples: '_root', 'feed', '/jobs/list'. Use null or omit to leave the route filter unset. |
<!-- /generated:parameters -->

---

## 4. Example Call

```json
{
  "scope": "spiegel.de",
  "observation": {
    "type": "consent_cmp",
    "signals": [
      { "kind": "dom", "match": "#sp-consent-container" },
      { "kind": "text", "match": "Zustimmen und weiterlesen" },
      { "kind": "vendor", "match": "sourcepoint" }
    ]
  },
  "topK": 3
}
```

---

## 5. Return Value Structure

```json
{
  "matched": true,
  "scope": "spiegel.de",
  "bestMatch": {
    "phenomenonId": "spiegel-cmp-reject",
    "type": "consent_cmp",
    "confidence": 0.98,
    "learningLevel": "Active",
    "playbook": {
      "policy": "reject_preferred",
      "actions": [
        { "type": "click", "selector": "button#btn-reject-all" }
      ]
    }
  },
  "matches": [
    {
      "phenomenonId": "spiegel-cmp-reject",
      "confidence": 0.98,
      "matchedSignals": 3,
      "totalSignals": 3
    }
  ]
}
```

---

## 6. Related Tools & Documentation

* [`nova.pks_get`](nova-pks-get.md) — Retrieve all phenomena registered for a domain.
* [`nova.pks_upsert`](nova-pks-upsert.md) — Save new phenomenon fingerprints after successful resolution.
* [`nova.telemetry_report`](nova-telemetry-report.md) — Report whether executing the playbook succeeded.
