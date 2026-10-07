# `nova.secret_delete`

> **Deletes an encrypted environment variable or API key secret from the DPAPI store.**

* **Core Feature Guide:** [Vault & Secret Keystore](../../../core-features/vault-and-secrets/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.secret_delete` permanently purges an encrypted secret entry by its name and scope.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `name` | `string` | Yes | — | — | Secret name. |
| `scope` | `string` | Yes | — | `global`, `workspace`, `task` | Scope the secret lives in. |
| `workspaceId` | `string` | No | — | — | Terminal workspace id (required for scope='workspace'). |
| `taskId` | `string` | No | — | — | Task id (required for scope='task'). |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `secret_store` (load it with `nova.tools_bundle(bundle='secret_store')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova.secret_delete",
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
      "text": "Secret 'PROD_DB_API_KEY' deleted (global scope)."
    }
  ],
  "structuredContent": {
    "name": "PROD_DB_API_KEY",
    "scope": "global",
    "workspaceId": null,
    "taskId": null,
    "deleted": true,
    "found": true
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
