# `nova.learn_feedback`

> **Submits reinforcement feedback (positive or negative) on a learned phenomenon pattern.**

* **Capability Bundle:** `pks_learning`
* **Security Tier:** Tier 2 (Reinforcement Telemetry)
* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.learn_feedback` adjusts confidence scores for learned UI patterns based on whether they succeeded or failed in production automation.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `limit` | `integer` | No | Maximum number of events to return (1-100). Default 20. |
| `scope` | `string` | No | Optional domain scope filter. |
| `since` | `integer` | No | Optional Unix timestamp in milliseconds. Returns events since this time. Default: last 7 days. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_learn_feedback",
  "arguments": {
    "phenomenonId": "phenom-checkout-v2",
    "success": true,
    "latencyMs": 210
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Reinforcement feedback applied: confidence updated to 0.94."
    }
  ],
  "structuredContent": {
    "ok": true,
    "phenomenonId": "phenom-checkout-v2",
    "newConfidence": 0.94
  }
}
```

---

## 4. Operational Best Practices

* **Autonomous Tuning:** Call after executing learned playbooks to maintain high-accuracy PKS memory.

---

## 5. Related Tools

* [`nova.pks_upsert`](nova-pks-upsert.md)
* [`nova.telemetry_report`](nova-telemetry-report.md)
