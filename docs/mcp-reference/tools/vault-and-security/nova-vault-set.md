# `nova.vault_set`

> **Stores or updates a username and password login credential in the encrypted vault.**

* **Capability Bundle:** `vault_auth`
* **Security Tier:** Tier 2 (Credential Storage)
* **Core Feature Guide:** [Vault & Secret Keystore](../../../core-features/vault-and-secrets.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.vault_set` encrypts and persists credentials bound to a web domain scope using Windows DPAPI encryption.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional metadata. Provide _meta.intent (a short reason) for high-impact tools. A tool's annotations.intentRequired in tools/list tells you up front: 'always' means intent is mandatory, 'conditional' means it becomes mandatory for certain arguments (e.g. includeValues=true), absent means never. |
| `createdBy` | `string` | No | Client/agent name. Defaults to 'agent'. |
| `password` | `string` | **Yes** | Password to store. Encrypted at rest via DPAPI. |
| `site` | `string` | **Yes** | Domain (e.g. 'github.com'). |
| `username` | `string` | **Yes** | Username or email for this credential. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_vault_set",
  "arguments": {
    "site": "https://login.example.com",
    "username": "testuser@example.com",
    "password": "SuperSecretPassword123!"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Saved credentials for testuser@example.com."
    }
  ],
  "structuredContent": {
    "ok": true,
    "site": "https://login.example.com",
    "username": "testuser@example.com",
    "status": "Stored"
  }
}
```

---

## 4. Operational Best Practices

* **Zero Context Leaks:** Pass credentials directly into the vault; avoid printing them into LLM chat transcripts.

---

## 5. Related Tools

* [`nova.vault_get`](nova-vault-get.md)
* [`nova.vault_prepare_fill`](nova-vault-prepare-fill.md)
