# `nova.pks_deprecate`

> **Marks an obsolete or broken PKS phenomenon playbook as deprecated.**

* **Security Tier:** Tier 2 (Knowledge Deprecation)
* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.pks_deprecate` deactivates an outdated playbook after a website redesign, preventing agents from continuing to execute failing patterns.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `scope` | `string` | Yes | — | — | Domain scope. |
| `phenomenonId` | `string` | Yes | — | — | Phenomenon ID to deprecate. |
| `reason` | `string` | No | — | — | Reason for deprecation (e.g. 'selector no longer matches', '5x consecutive failure'). |

Capability bundle: `pks_learning` (load it with `nova.tools_bundle(bundle='pks_learning')`).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_pks_deprecate",
  "arguments": {
    "phenomenonId": "phenom-old-nav",
    "reason": "Website upgraded to v3 with shadow DOM nav bar."
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Deprecated phenomenon phenom-old-nav."
    }
  ],
  "structuredContent": {
    "ok": true,
    "phenomenonId": "phenom-old-nav",
    "status": "Deprecated"
  }
}
```

---

## 4. Operational Best Practices

* **Deprecate on Redesign:** Mark playbooks deprecated rather than deleting to preserve audit history.

---

## 5. Related Tools

* [`nova.pks_patch`](nova-pks-patch.md)
* [`nova.pks_list`](nova-pks-list.md)
