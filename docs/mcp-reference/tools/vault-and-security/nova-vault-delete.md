# `nova.vault_delete`

> **Deletes a stored website login credential entry from the encrypted vault.**

* **Capability Bundle:** `vault_auth`
* **Security Tier:** Tier 2 (Destructive Credential Management)
* **Core Feature Guide:** [Vault & Secret Keystore](../../../core-features/vault-and-secrets.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.vault_delete` removes account credentials for a domain and username pair from the local credential vault.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional metadata. Provide _meta.intent (a short reason) for high-impact tools. A tool's annotations.intentRequired in tools/list tells you up front: 'always' means intent is mandatory, 'conditional' means it becomes mandatory for certain arguments (e.g. includeValues=true), absent means never. |
| `id` | `string` | **Yes** | Entry ID from nova.vault_list. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_vault_delete",
  "arguments": {
    "site": "https://login.example.com",
    "username": "staging_user"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Removed vault entry for staging_user at login.example.com."
    }
  ],
  "structuredContent": {
    "ok": true,
    "site": "https://login.example.com",
    "username": "staging_user"
  }
}
```

---

## 4. Operational Best Practices

* **Account Cleanup:** Remove temporary test credentials upon test suite conclusion.

---

## 5. Related Tools

* [`nova.vault_set`](nova-vault-set.md)
* [`nova.vault_list`](nova-vault-list.md)
