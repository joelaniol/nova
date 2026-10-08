# `nova.learn_resolve_opportunity`

> **Closes a semantic learning opportunity that Nova raised in a tool result (`pksSemanticLearning`).**

* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/learning/phenomenological-knowledge-store-pks/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

When Nova notices a page situation that is worth storing in the PKS (a cookie-consent banner, a login wall, a risky repeated action), it adds a `pksSemanticLearning` block with an `opportunityId` (format `sem:{kind}:{origin}:{fingerprint}`) to tool results. `nova.learn_resolve_opportunity` tells Nova how the agent handled it. Verdict `upsert` marks the opportunity as `Resolved` (the agent stored the knowledge, for example with `nova.pks_upsert`) and marks older selector-only candidates for the same origin as superseded. The verdicts `not_applicable`, `unsafe`, `already_known` and `defer` mark it as `Dismissed`. An opportunity that is unknown or already closed is not changed and the result has `ok: false`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `opportunityId` | `string` | Yes | — | — | Stable ID emitted in pksSemanticLearning.opportunityId, format sem:{kind}:{origin}:{fingerprint}. |
| `verdict` | `string` | Yes | — | `upsert`, `not_applicable`, `unsafe`, `already_known`, `defer` | How the agent handled the opportunity. |
| `reason` | `string` | No | — | ≤ 500 characters | Optional short rationale (≤500 chars) for telemetry. |

Capability bundle: `pks_learning` (load it with `nova.tools_bundle(bundle='pks_learning')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_learn_resolve_opportunity",
  "arguments": {
    "opportunityId": "sem:consent_cmp:https://example.com:6c0e2f91",
    "verdict": "already_known",
    "reason": "Consent banner is already covered by an existing PKS phenomenon."
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Opportunity sem:consent_cmp:https://example.com:6c0e2f91 resolved with verdict 'already_known'."
    }
  ],
  "structuredContent": {
    "ok": true,
    "opportunityId": "sem:consent_cmp:https://example.com:6c0e2f91",
    "verdict": "already_known",
    "reason": "Consent banner is already covered by an existing PKS phenomenon.",
    "priorState": "Prompted",
    "resolvedState": "Dismissed",
    "resolvedAtUtc": "2026-10-03T09:20:11.4410000+00:00",
    "fr1CandidatesSuperseded": 0
  }
}
```

---

## 4. Operational Best Practices

* **Copy the ID exactly:** Use the `opportunityId` from the `pksSemanticLearning` block of the tool result; it is not listed by `nova.learn_suggest`.
* **Answer prompted opportunities:** A prompt that stays unresolved over further calls on the same origin moves to a warning digest; resolving it, even with `defer`, closes it.

---

## 5. Related Tools

* [`nova.learn_suggest`](nova-learn-suggest.md)
