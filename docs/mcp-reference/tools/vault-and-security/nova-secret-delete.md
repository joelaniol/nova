# `nova.secret_delete`

> **Deletes an encrypted environment variable or API key secret from the DPAPI store.**

* **Capability Bundle:** `secret_store`
* **Security Tier:** Tier 2 (Destructive Secret Management)
* **Core Feature Guide:** [Vault & Secret Keystore](../../../core-features/vault-and-secrets.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.secret_delete` permanently purges an encrypted secret entry by its name and scope.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional metadata. Provide _meta.intent (a short reason) for high-impact tools. A tool's annotations.intentRequired in tools/list tells you up front: 'always' means intent is mandatory, 'conditional' means it becomes mandatory for certain arguments (e.g. includeValues=true), absent means never. |
| `name` | `string` | **Yes** | Secret name. |
| `scope` | `string` | **Yes** | Scope the secret lives in. |
| `taskId` | `string` | No | Task id (required for scope='task'). |
| `workspaceId` | `string` | No | Terminal workspace id (required for scope='workspace'). |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_secret_delete",
  "arguments": {
    "name": "PROD_DB_API_KEY",
    "scope": "global"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Deleted secret PROD_DB_API_KEY."
    }
  ],
  "structuredContent": {
    "ok": true,
    "name": "PROD_DB_API_KEY",
    "deleted": true
  }
}
```

---

## 4. Operational Best Practices

* **Key Rotation:** Purge expired credentials during key rollover workflows.

---

## 5. Related Tools

* [`nova.secret_set`](nova-secret-set.md)
* [`nova.secret_list`](nova-secret-list.md)
