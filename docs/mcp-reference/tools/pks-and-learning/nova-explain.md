# `nova.explain`

Explains why a PKS phenomenon resides at its current learning level, returning a detailed per-gate breakdown of promotion requirements, failure reasons, and remediation hints.

---

## 1. Overview

Nova's Phenomenological Knowledge Store (PKS) uses empirical quality gates to govern whether a playbook is executed automatically (`Active`), evaluated passively (`Shadow`), or blocked from running (`Deprecated`). 

`nova.explain` provides transparent visibility into these internal decisions. If an agent wonders: *"Why is this playbook not running automatically?"* or *"What evidence is missing to promote this candidate?"*, `nova.explain` answers with exact mathematical deltas, gate evaluations, and actionable instructions.

* **Per-Gate Breakdown:** Evaluates sample size, consecutive successes, failure ratios, and multi-session consistency.
* **Delta to Pass:** Identifies exactly how many additional successful runs are required to graduate.
* **Fingerprint Breakdown:** When `observedSignals` are supplied, highlights which signals matched and which failed during live page detection.

---

## 2. PKS Learning Levels & Promotion Gates

```
  [Candidate / Ingest]
           ?
           ?
    [Level: Shadow]  ?-- Passive monitoring; evaluated without modifying live page
           ?
           ? (Requires: 3 consecutive successes, 0 failures, verified verification step)
           ?
    [Level: Active]  ?-- Fully automated execution for all agents on this domain
           ?
           ? (If: 3 consecutive failures or health score < 0.60)
           ?
  [Level: Deprecated] ?-- Flagged as broken; execution blocked until refreshed
```

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `scope` | `string` | Yes | — | — | Domain scope (e.g. 'spiegel.de'). |
| `stableId` | `string` | Yes | — | — | Preferred phenomenon stable ID to explain. Must match stable_id if both are provided. |
| `stable_id` | `string` | No | — | — | Legacy alias for stableId. Phenomenon stable ID to explain. |
| `observedSignals` | `array` of `string` | No | — | — | Preferred alias for observed_signals. Must match observed_signals if both are provided. |
| `observed_signals` | `array` of `string` | No | — | — | Legacy alias for observedSignals. Optional DOM/text/vendor/layout signals to compute match breakdown against this phenomenon's fingerprint. |

Capability bundle: `pks_learning` (load it with `nova.tools_bundle(bundle='pks_learning')`).
<!-- /generated:parameters -->

---

## 4. Example Call

```json
{
  "scope": "spiegel.de",
  "stableId": "spiegel-cmp-reject"
}
```

---

## 5. Return Value Structure

```json
{
  "stableId": "spiegel-cmp-reject",
  "scope": "spiegel.de",
  "currentLevel": "Shadow",
  "targetLevel": "Active",
  "overallGatePass": false,
  "gates": [
    {
      "name": "min_sample_size",
      "status": "passed",
      "required": 5,
      "current": 6
    },
    {
      "name": "min_success_rate",
      "status": "passed",
      "required": 0.90,
      "current": 1.0
    },
    {
      "name": "min_distinct_sessions",
      "status": "failed",
      "required": 3,
      "current": 2,
      "delta": 1,
      "remediation": "Requires verification in at least 1 additional distinct browser session."
    }
  ]
}
```

---

## 6. Related Tools & Documentation

* [`nova.telemetry_report`](nova-telemetry-report.md) ? Record execution attempts to fulfill gate requirements.
* [`nova.pks_get`](nova-pks-get.md) ? Retrieve phenomenon definitions.
* [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md) ? Complete specification of PKS promotion criteria.
