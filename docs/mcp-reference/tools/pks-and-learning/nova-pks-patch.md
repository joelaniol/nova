# `nova.pks_patch`

> **Applies partial updates or selector refinements to an existing PKS phenomenon playbook.**

* **Capability Bundle:** `pks_learning`
* **Security Tier:** Tier 2 (Knowledge Refinement)
* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.pks_patch` updates specific properties (selectors, timeout values, assertion rules) of a phenomenon without rebuilding the entire playbook.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `patch` | `object` | **Yes** | Fields to merge. Only provided fields are updated. |
| `phenomenonId` | `string` | **Yes** | Phenomenon ID to patch. |
| `scope` | `string` | **Yes** | Domain scope. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_pks_patch",
  "arguments": {
    "phenomenonId": "phenom-login",
    "patch": {
      "selector": "button[type=\"submit\"].btn-primary"
    }
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Patched selector in phenom-login."
    }
  ],
  "structuredContent": {
    "ok": true,
    "phenomenonId": "phenom-login",
    "version": 2
  }
}
```

---

## 4. Operational Best Practices

* **Surgical Repairs:** Fix minor selector drifts without losing historical execution telemetry.

---

## 5. Related Tools

* [`nova.pks_upsert`](nova-pks-upsert.md)
* [`nova.revalidate`](nova-revalidate.md)
