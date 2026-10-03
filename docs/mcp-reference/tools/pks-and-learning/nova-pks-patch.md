# `nova.pks_patch`

> **Applies partial updates or selector refinements to an existing PKS phenomenon playbook.**

* **Security Tier:** Tier 2 (Knowledge Refinement)
* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.pks_patch` updates specific properties (selectors, timeout values, assertion rules) of a phenomenon without rebuilding the entire playbook.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `scope` | `string` | Yes | — | — | Domain scope. |
| `phenomenonId` | `string` | Yes | — | — | Phenomenon ID to patch. |
| `patch` | `object` | Yes | — | — | Fields to merge. Only provided fields are updated. |
| `patch.type` | `string` | No | — | `consent_cmp`, `modal`, `paywall`, `login_wall`, `layout_shift`, `native_dialog`, `popover_open`, `custom` | Updated phenomenon type. |
| `patch.fingerprint` | `object` | No | — | — | Fingerprint signals to merge. When provided, the full fingerprint payload replaces the existing fingerprint. |
| `patch.playbook` | `object` | No | — | — | Playbook to merge. When provided, the full playbook payload replaces the existing playbook. |
| `patch.context` | `any` | No | — | — | Optional phenomenon-level context override. Set null to clear and fallback to domain context keys. |
| `patch.deprecated` | `boolean` | No | — | — | Set to false to reactivate a deprecated phenomenon. |

Capability bundle: `pks_learning` (load it with `nova.tools_bundle(bundle='pks_learning')`).
<!-- /generated:parameters -->

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
