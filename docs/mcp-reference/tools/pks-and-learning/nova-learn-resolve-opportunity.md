# `nova.learn_resolve_opportunity`

> **Resolves or closes a learning opportunity opportunity flagged during autonomous browsing.**

* **Capability Bundle:** `pks_learning`
* **Security Tier:** Tier 2 (Learning Maintenance)
* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.learn_resolve_opportunity` marks an identified optimization opportunity as resolved, dismissed, or converted to a playbook.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `opportunityId` | `string` | Yes | — | — | Stable ID emitted in pksSemanticLearning.opportunityId, format sem:{kind}:{origin}:{fingerprint}. |
| `verdict` | `string` | Yes | — | `upsert`, `not_applicable`, `unsafe`, `already_known`, `defer` | How the agent handled the opportunity. |
| `reason` | `string` | No | — | ≤ 500 characters | Optional short rationale (≤500 chars) for telemetry. |
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_learn_resolve_opportunity",
  "arguments": {
    "opportunityId": "opp-992",
    "resolution": "ConvertedToPhenomenon"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Resolved opportunity opp-992."
    }
  ],
  "structuredContent": {
    "ok": true,
    "opportunityId": "opp-992",
    "status": "Resolved"
  }
}
```

---

## 4. Operational Best Practices

* **Queue Hygiene:** Keep learning queues clean by resolving obsolete opportunities.

---

## 5. Related Tools

* [`nova.learn_suggest`](nova-learn-suggest.md)
