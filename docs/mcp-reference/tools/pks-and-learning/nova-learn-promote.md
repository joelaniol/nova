# `nova.learn_promote`

> **Promotes a candidate phenomenon playbook from staging into active production PKS memory.**

* **Security Tier:** Tier 2 (Knowledge Promotion)
* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.learn_promote` transitions a validated learning candidate to active status once confidence and safety verification gates pass.

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
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_learn_promote",
  "arguments": {
    "candidateId": "phenom-cart-flow-01",
    "justification": "Verified across 5 consecutive successful checkout runs."
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Promoted phenom-cart-flow-01 to active PKS memory."
    }
  ],
  "structuredContent": {
    "ok": true,
    "phenomenonId": "phenom-cart-flow-01",
    "status": "Active"
  }
}
```

---

## 4. Operational Best Practices

* **Rigorous Gate:** Only promote candidates that satisfy pre-verification polarity checks.

---

## 5. Related Tools

* [`nova.learn_generate`](nova-learn-generate.md)
* [`nova.pks_get`](nova-pks-get.md)
