# `nova.vault_set`

> **Stores or updates a username and password login credential in the encrypted vault.**

* **Security Tier:** Tier 2 (Credential Storage)
* **Core Feature Guide:** [Vault & Secret Keystore](../../../core-features/vault-and-secrets.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.vault_set` encrypts and persists credentials bound to a web domain scope using Windows DPAPI encryption.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `site` | `string` | Yes | — | — | Domain (e.g. 'github.com'). |
| `username` | `string` | Yes | — | — | Username or email for this credential. |
| `password` | `string` | Yes | — | — | Password to store. Encrypted at rest via DPAPI. |
| `createdBy` | `string` | No | `"agent"` | — | Client/agent name. Defaults to 'agent'. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `vault_auth` (load it with `nova.tools_bundle(bundle='vault_auth')`).
<!-- /generated:parameters -->

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
