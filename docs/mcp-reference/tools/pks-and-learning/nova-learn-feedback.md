# `nova.learn_feedback`

> **Lists recent learning-level changes (promotions, demotions, deprecations, revivals, generated candidates) in the PKS.**

* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/phenomenological-knowledge-store-pks/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.learn_feedback` is read-only. It returns the recorded learning events of the Phenomenological Knowledge Store: each time a phenomenon or domain hint changed its learning level, for example `l0_to_l1`, `l1_to_l2`, `demotion`, `deprecation`, `revive`, or `learn_generate` / `learn_generate_patch` for candidates written by `nova.learn_generate`. Without `since` it covers the last 7 days; `scope` narrows the list to one domain. It does not change any confidence values.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `scope` | `string` | No | — | — | Optional domain scope filter. |
| `since` | `integer` | No | — | — | Optional Unix timestamp in milliseconds. Returns events since this time. Default: last 7 days. |
| `limit` | `integer` | No | `20` | 1–100 | Maximum number of events to return (1-100). Default 20. |

Capability bundle: `pks_learning` (load it with `nova.tools_bundle(bundle='pks_learning')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_learn_feedback",
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
      "text": "Recent learning events for 'example.com' (1):\n1. [2026-10-01 14:02] cookie-banner-accept: l0_to_l1 (L0->L1) on example.com"
    }
  ],
  "structuredContent": {
    "ok": true,
    "scope": "example.com",
    "count": 1,
    "events": [
      {
        "stableId": "cookie-banner-accept",
        "contextHost": "example.com",
        "fromLevel": 0,
        "toLevel": 1,
        "reasonKind": "l0_to_l1",
        "reason": { "support": 3, "successSupport": 3, "confidence": 0.82, "evidenceScore": 0.71 },
        "createdAtMs": 1790863320000,
        "createdAtUtc": "2026-10-01T14:02:00.0000000Z"
      }
    ]
  }
}
```

Without events in the window the result is `count: 0` with an empty `events` array and the text "No promotion events in the specified time window.". Without `scope`, `scope` is reported as `"*"`.

---

## 4. Operational Best Practices

* **Audit trail:** Use it to see why a phenomenon is (or no longer is) used as a learned pattern; `nova.explain` shows the gates for a single phenomenon.

---

## 5. Related Tools

* [`nova.pks_upsert`](nova-pks-upsert.md)
* [`nova.telemetry_report`](nova-telemetry-report.md)
