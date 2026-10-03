# `nova.telemetry_report`

Reports empirical execution outcomes (`success`, `failure`, or `not_applicable`) for a PKS phenomenon interaction, updating health scores and driving automatic promotion and deprecation gates.

---

## 1. Overview

The Phenomenological Knowledge Store (PKS) is a living, self-healing memory store. To prevent stale, broken selectors from lingering when websites change, Nova calculates rolling health scores for every stored playbook.

`nova.telemetry_report` is the feedback channel. Whenever an agent attempts to execute a playbook?or verifies an action sequence?it reports the outcome. High success rates promote playbooks from `Shadow` to `Active` status; repeated failures trigger automated demotion and deprecation warnings.

* **Capability Bundle:** `pks_and_learning`, `domain_knowledge`
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

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`scope`** | `string` | **Yes** | ? | Domain scope (e.g. `"nytimes.com"`). |
| **`phenomenonId`**| `string` | **Yes** | ? | Phenomenon ID being evaluated. |
| **`outcome`** | `string` | **Yes** | ? | Result: `"success"`, `"failure"`, or `"not_applicable"`. |
| **`elapsedMs`** | `integer` | No | `null` | Milliseconds taken to execute the interaction. |
| **`features`** | `object` | No | `null` | Optional structured evidence: `{ presentSignals, absentSignals, matchedSelectors, notes }`. |
| **`targetId`** | `string` | No | `"active"` | Target tab ID for session attribution. |

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
