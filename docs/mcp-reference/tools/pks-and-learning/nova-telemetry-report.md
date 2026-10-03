# `nova.telemetry_report`

Reports empirical execution outcomes (`success`, `failure`, or `not_applicable`) for a PKS phenomenon interaction, updating health scores and driving automatic promotion and deprecation gates.

---

## 1. Overview

The Phenomenological Knowledge Store (PKS) is a living, self-healing memory store. To prevent stale, broken selectors from lingering when websites change, Nova calculates rolling health scores for every stored playbook.

`nova.telemetry_report` is the feedback channel. Whenever an agent attempts to execute a playbook?or verifies an action sequence?it reports the outcome. High success rates promote playbooks from `Shadow` to `Active` status; repeated failures trigger automated demotion and deprecation warnings.

* **Three Interaction Outcomes:**
  * `success`: Action sequence executed and verified correctly.
  * `failure`: Action timed out, selector missing, or postcondition check failed.
  * `not_applicable`: Element legitimately does not exist on this page variant (does *not* penalize health scores).
* **Automated Promotion Engine:** Consecutive verified successes automatically graduate candidate playbooks to active status.
* **Deprecation Safeguard:** High failure rates automatically flag playbooks as deprecated to prevent other agents from looping on broken actions.

---

## 2. Interaction Outcomes

| Outcome | Health Score Impact | Definition & Common Scenarios |
| :--- | :---: | :--- |
| **`success`** | **Positive (+)** | Action executed and postcondition verification succeeded (e.g. banner dismissed, page unlocked). |
| **`failure`** | **Negative (-)** | Selector was not clickable, action timed out, or postcondition check asserted the blocker was still present. |
| **`not_applicable`** | **Neutral (0)** | Feature legitimately absent on this specific page variant (e.g. no transcript button on an instrumental music video). Does not count as an attempt or failure. |

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | — | — | Optional tab target for attribution (e.g. 'active', 'A', browser tabId). |
| `scope` | `string` | Yes | — | — | Domain scope. |
| `phenomenonId` | `string` | Yes | — | — | Phenomenon ID to report on. |
| `outcome` | `string` | Yes | — | `success`, `failure`, `not_applicable` | Outcome of the interaction. Use 'not_applicable' when the element legitimately doesn't exist on this page variant. |
| `elapsedMs` | `integer` | No | — | — | Preferred elapsed time in milliseconds. Must match elapsed_ms if both are provided. |
| `elapsed_ms` | `integer` | No | — | — | Legacy alias for elapsedMs. Optional elapsed time in milliseconds. |
| `features` | `object` | No | — | — | Optional structured evidence about which phenomenon signals were present during the interaction. Known fields cover the common compact telemetry shape; additional evidence keys may be attached for forward-compatible experimentation. |
| `features.presentSignals` | `array` of `string` | No | — | — | Signal identifiers or fingerprint labels that were observed. |
| `features.absentSignals` | `array` of `string` | No | — | — | Signal identifiers that were expected but not observed. |
| `features.matchedSelectors` | `array` of `string` | No | — | — | Selectors or element handles that matched during the interaction. |
| `features.matchConfidence` | `number` | No | — | — | Aggregate confidence score for the observed signal bundle. |
| `features.notes` | `string` | No | — | — | Short human-readable evidence note. |

Capability bundle: `pks_learning` (load it with `nova.tools_bundle(bundle='pks_learning')`).
<!-- /generated:parameters -->

---

## 4. Example Calls

### Report Successful Playbook Execution
```json
{
  "scope": "spiegel.de",
  "phenomenonId": "spiegel-cmp-reject",
  "outcome": "success",
  "elapsedMs": 420,
  "features": {
    "matchedSelectors": ["button#btn-reject-all"],
    "notes": "Modal vanished cleanly within 420ms."
  }
}
```

### Report Legitimate Absence (`not_applicable`)
```json
{
  "scope": "youtube.com",
  "phenomenonId": "video-transcript-drawer",
  "outcome": "not_applicable",
  "features": {
    "notes": "Music video without speech track; transcript control not rendered."
  }
}
```

---

## 5. Return Value Structure

```json
{
  "acknowledged": true,
  "phenomenonId": "spiegel-cmp-reject",
  "scope": "spiegel.de",
  "newHealthScore": 0.99,
  "totalAttempts": 421,
  "currentLearningLevel": "Active",
  "promotionStatus": "maintained"
}
```

---

## 6. Related Tools & Documentation

* [`nova.pks_upsert`](nova-pks-upsert.md) ? Create or update phenomenon entries in PKS.
* [`nova.explain`](nova-explain.md) ? Inspect the detailed health score and promotion gate breakdown.
* [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md) ? Mathematical health scoring and gate definitions.
