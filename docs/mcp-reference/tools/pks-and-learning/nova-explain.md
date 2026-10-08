# `nova.explain`

Explains why a PKS phenomenon resides at its current learning level, returning a detailed per-gate breakdown of promotion requirements, failure reasons, and remediation hints.

---

## 1. Overview

Nova's Phenomenological Knowledge Store (PKS) uses empirical quality gates to govern whether a playbook is executed automatically (`Active`), evaluated passively (`Shadow`), or blocked from running (`Deprecated`). 

`nova.explain` provides transparent visibility into these internal decisions. If an agent wonders: *"Why is this playbook not running automatically?"* or *"What evidence is missing to promote this candidate?"*, `nova.explain` answers with exact mathematical deltas, gate evaluations, and actionable instructions.

* **Per-Gate Breakdown:** The gate set depends on the phenomenon's current level — promotion gates for `Candidate`/`Shadow`, demotion/deprecation triggers for `Active`, and revive gates for `Deprecated`.
* **Delta to Pass:** Identifies exactly how many additional successful runs are required to graduate.
* **Fingerprint Breakdown:** When `observedSignals` are supplied and the phenomenon has fingerprint signals, returns a scored per-signal match breakdown.

---

## 2. PKS Learning Levels & Promotion Gates

Candidate (L0) → Shadow (L1) → Active (L2). Each transition requires appropriate supporting evidence. Failures and drift can lower trust or deprecate knowledge; revival requires fresh evidence and does not immediately restore active status.

The tool explains the decision for the requested phenomenon. Active status is separate from runtime permission and ambient-application eligibility. See [PKS learning levels](../../../core-features/learning/phenomenological-knowledge-store-pks/README.md#5-why-knowledge-needs-trust-levels).

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
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
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

`currentLevel` is the raw numeric learning level (`0` = Candidate, `1` = Shadow, `2` = Active). `match` is `null` unless `observedSignals` was supplied and the phenomenon has fingerprint signals to score against.

```json
{
  "ok": true,
  "scope": "spiegel.de",
  "phenomenon": {
    "stableId": "spiegel-cmp-reject",
    "type": "consent_cmp",
    "currentLevel": 1,
    "deprecated": false
  },
  "explain": {
    "summary": "L1->L2: 3/4 gates passed",
    "kind": "promotion",
    "gates": [
      { "name": "max_drift_7d", "required": 0, "observed": 0, "passed": true, "deltaToPass": 0 },
      { "name": "min_success", "required": 3, "observed": 2, "passed": false, "deltaToPass": 1 },
      { "name": "min_distinct_sessions", "required": 2, "observed": 2, "passed": true, "deltaToPass": 0 },
      { "name": "max_failure", "required": 1, "observed": 0, "passed": true, "deltaToPass": 0 }
    ],
    "remediation": [
      "Need 1 more successful execution(s)."
    ]
  },
  "match": null
}
```

---

## 6. Related Tools & Documentation

* [`nova.telemetry_report`](nova-telemetry-report.md) — Record execution attempts to fulfill gate requirements.
* [`nova.pks_get`](nova-pks-get.md) — Retrieve phenomenon definitions.
* [Phenomenological Knowledge Store (PKS)](../../../core-features/learning/phenomenological-knowledge-store-pks/README.md) — Complete specification of PKS promotion criteria.
