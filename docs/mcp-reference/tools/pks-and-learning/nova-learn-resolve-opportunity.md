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

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `opportunityId` | `string` | **Yes** | Stable ID emitted in pksSemanticLearning.opportunityId, format sem:{kind}:{origin}:{fingerprint}. |
| `reason` | `string` | No | Optional short rationale (≤500 chars) for telemetry. |
| `verdict` | `string` | **Yes** | How the agent handled the opportunity. |

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
