# `nova.learn_promote`

> **Evaluates and applies learning-level transitions (promotion, demotion, deprecation, revival) for the PKS entries of one domain.**

* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/learning/phenomenological-knowledge-store-pks/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.learn_promote` checks the phenomena and domain hints of a domain against Nova's promotion gates (confidence, support count, successful uses, evidence score) and moves each entry that passes to its next level: `l0_to_l1` (candidate to shadow), `l1_to_l2` (shadow to active), or `demotion`, `deprecation` and `revive`. Nova also runs the same evaluation in the background; the tool lets an agent trigger it for one domain and see every decision. With `dryRun: true` the gates are evaluated without writing anything. Without `dryRun`, the domain must be open in a tab or sandbox, otherwise the call is rejected with `reasonCode: "pks.scope_not_open"`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `scope` | `string` | Yes | — | — | Required domain scope (e.g. 'github.com'). |
| `stableIds` | `array` of `string` | No | — | — | Stable IDs to evaluate. Pass ["all"] to evaluate all entries for the scope. If omitted, evaluates all. |
| `transition` | `string` | No | — | `l0_to_l1`, `l1_to_l2`, `demotion`, `deprecation`, `revive` | Transition type to evaluate: 'l0_to_l1', 'l1_to_l2', 'demotion', 'deprecation', 'revive'. If omitted, evaluates all applicable transitions. |
| `dryRun` | `boolean` | No | `false` | — | If true, evaluate gates without executing transitions. Default false. |

Capability bundle: `pks_learning` (load it with `nova.tools_bundle(bundle='pks_learning')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_learn_promote",
  "arguments": {
    "scope": "example.com",
    "transition": "l0_to_l1",
    "dryRun": true
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Promotion evaluation for 'example.com' (DRY RUN): 1 approved, 1 rejected, 0 applied.\n1. [APPROVED] lcj_4b1f0c9a2d7e: l0_to_l1 - L0->L1\n2. [REJECTED] lcj_9e03d5a1c6b2: l0_to_l1 - Support count 1 < 2."
    }
  ],
  "structuredContent": {
    "ok": true,
    "scope": "example.com",
    "dryRun": true,
    "approved": 1,
    "rejected": 1,
    "applied": 0,
    "writeFailed": 0,
    "total": 2,
    "decisions": [
      {
        "stableId": "lcj_4b1f0c9a2d7e",
        "approved": true,
        "applied": false,
        "skippedBecause": "dry_run",
        "writeError": null,
        "reasonKind": "l0_to_l1",
        "fromLevel": 0,
        "toLevel": 1,
        "rejectionReason": null
      },
      {
        "stableId": "lcj_9e03d5a1c6b2",
        "approved": false,
        "applied": false,
        "skippedBecause": "not_approved",
        "writeError": null,
        "reasonKind": "l0_to_l1",
        "fromLevel": 0,
        "toLevel": 1,
        "rejectionReason": "Support count 1 < 2."
      }
    ]
  }
}
```

If the domain has no PKS data, the result is `{ "ok": true, "scope": "...", "decisions": [], "count": 0 }` with the text "No PKS data for '<scope>'.". `ok` is `false` only when an approved transition could not be written (`writeFailed` > 0, `skippedBecause: "write_failed"`).

---

## 4. Operational Best Practices

* **Dry run first:** Run with `dryRun: true` to see which entries would move and why the others are rejected, then repeat without it.
* **Narrow the run:** `stableIds` and `transition` limit the evaluation to specific entries or one transition type.

---

## 5. Related Tools

* [`nova.learn_generate`](nova-learn-generate.md)
* [`nova.pks_get`](nova-pks-get.md)
