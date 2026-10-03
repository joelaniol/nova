# `nova.learn_generate`

> **Synthesizes a proposed phenomenon interaction playbook from recorded execution trajectories.**

* **Capability Bundle:** `pks_learning`
* **Security Tier:** Tier 2 (Pattern Synthesis)
* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.learn_generate` analyzes session interaction recordings to extract robust CSS/ARIA selectors and step sequences, proposing a new phenomenon candidate.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `scope` | `string` | Yes | — | — | Required domain scope (e.g. 'github.com'). |
| `limit` | `integer` | No | `5` | 1–20 | Maximum number of candidates to generate (1-20). Default 5. |
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_learn_generate",
  "arguments": {
    "recordingSessionId": "rec-8801",
    "scope": "checkout.shop.com"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Synthesized candidate phenomenon: phenom-cart-flow-01."
    }
  ],
  "structuredContent": {
    "ok": true,
    "candidateId": "phenom-cart-flow-01",
    "proposedSteps": 4
  }
}
```

---

## 4. Operational Best Practices

* **Playbook Mining:** Turn exploratory browsing trajectories into deterministic fast-path playbooks.

---

## 5. Related Tools

* [`nova.learn_promote`](nova-learn-promote.md)
* [`nova.pks_upsert`](nova-pks-upsert.md)
