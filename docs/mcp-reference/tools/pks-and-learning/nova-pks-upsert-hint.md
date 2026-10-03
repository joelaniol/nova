# `nova.pks_upsert_hint`

> **Attaches or updates a human operator guidance hint on a phenomenon pattern.**

* **Capability Bundle:** `pks_learning`
* **Security Tier:** Tier 2 (Operator Guidance)
* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.pks_upsert_hint` binds operator annotations (e.g. "Wait 2 seconds after click for React state settlement") to a phenomenon.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `domainHint` | `object` | **Yes** | Domain hint to upsert (matched by id if existing). |
| `scope` | `string` | **Yes** | Domain scope (e.g. 'youtube.com'). |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_pks_upsert_hint",
  "arguments": {
    "phenomenonId": "phenom-cart-flow-01",
    "hint": "Requires 500ms settlement after selecting shipping address."
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Attached guidance hint to phenom-cart-flow-01."
    }
  ],
  "structuredContent": {
    "ok": true,
    "phenomenonId": "phenom-cart-flow-01",
    "hintsCount": 1
  }
}
```

---

## 4. Operational Best Practices

* **Human Knowledge Injection:** Record non-obvious site quirks for future agent runs.

---

## 5. Related Tools

* [`nova.pks_patch`](nova-pks-patch.md)
