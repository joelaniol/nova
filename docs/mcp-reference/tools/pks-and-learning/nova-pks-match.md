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

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`scope`** | `string` | **Yes** | — | Domain scope to search (e.g. `"nytimes.com"`). |
| **`observation`** | `object` | **Yes** | — | Observed signals: `{ signals: [...], type?: string }`. |
| **`context`** | `object` | No | `null` | Context filters: `{ auth, device, locale, route }`. |
| **`topK`** | `integer` | No | `1` | Number of ranked candidates to return (1–10). |

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
