# Credentials, Vault & DPAPI Secret Keystore

Password autofill via ephemeral origin-bound SecretRef tokens, credential discovery, and write-only encrypted environment variables.

* **Capability Bundle(s):** `vault_auth, secret_store`
* **Core Architecture Guide:** [Core Features: vault-and-secrets.md](../../../core-features/vault-and-secrets.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (8 Tools)

| Tool Name | Status | Description |
| :--- | :---: | :--- |
| **[`nova.secret_delete`](nova-secret-delete.md)** | Documented | Delete a secret from the user-managed store. |
| **[`nova.secret_list`](nova-secret-list.md)** | Documented | List secret names and scopes from the user-managed store (values are never returned). |
| **[`nova.secret_set`](nova-secret-set.md)** | Documented | Store an encrypted secret in the user-managed store. |
| **[`nova.vault_delete`](nova-vault-delete.md)** | Documented | Delete a vault entry by ID.. |
| **[`nova.vault_get`](nova-vault-get.md)** | Documented | Get vault entry metadata for a site. |
| **[`nova.vault_list`](nova-vault-list.md)** | Documented | List vault entries (site, username, createdBy). |
| **[`nova.vault_prepare_fill`](nova-vault-prepare-fill.md)** | Documented | Prepare vault credentials for form filling. |
| **[`nova.vault_set`](nova-vault-set.md)** | Documented | Store or update credentials. |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
