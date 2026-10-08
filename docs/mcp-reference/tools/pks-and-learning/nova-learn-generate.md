# `nova.learn_generate`

> **Synthesizes a proposed phenomenon interaction playbook from recorded execution trajectories.**

* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/learning/phenomenological-knowledge-store-pks/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.learn_generate` turns the observations Nova has collected for one domain (repeated blocker dismissals, shared result-item selectors, selector drift) into learning candidates and writes them to the PKS at level L0 (candidate). Depending on the observation it creates a new phenomenon, a new domain hint, or a patch for an existing, similar phenomenon. It does not read session recordings. The domain must be open in a tab or sandbox; otherwise the call is rejected with `reasonCode: "pks.scope_not_open"`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `scope` | `string` | Yes | — | — | Required domain scope (e.g. 'github.com'). |
| `limit` | `integer` | No | `5` | 1–20 | Maximum number of candidates to generate (1-20). Default 5. |

Capability bundle: `pks_learning` (load it with `nova.tools_bundle(bundle='pks_learning')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_learn_generate",
  "arguments": {
    "scope": "example.com",
    "limit": 5
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Generated 1/1 candidates for 'example.com':\n1. [NewPhenomenon] Blocker dismissed 4x on example.com."
    }
  ],
  "structuredContent": {
    "ok": true,
    "scope": "example.com",
    "generated": 1,
    "proposed": 1,
    "proposals": [
      {
        "kind": "NewPhenomenon",
        "contextHost": "example.com",
        "candidateKey": "auto:modal:example.com:3f9a1c2e",
        "confidence": 0.74,
        "reason": "Blocker dismissed 4x on example.com.",
        "phenomenonType": "modal",
        "targetStableId": null,
        "hintKind": null
      }
    ]
  }
}
```

If nothing can be generated, the result has `count: 0`, an empty `proposals` array and a `skipped` array that names a `reasonCode` per observation cluster (for example `already_covered`, `blocker_dismiss_requires_success`, `result_item_requires_three_successes`).

---

## 4. Operational Best Practices

* **Check first:** `nova.learn_suggest` lists the ranked opportunities for a domain without writing anything.
* **Candidates are not active yet:** generated entries start at L0 and only become active after promotion (`nova.learn_promote` or automatic promotion).

---

## 5. Related Tools

* [`nova.learn_promote`](nova-learn-promote.md)
* [`nova.pks_upsert`](nova-pks-upsert.md)
