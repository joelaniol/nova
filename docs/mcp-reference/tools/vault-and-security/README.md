# Credentials, Vault & DPAPI Secret Keystore

Password autofill via ephemeral origin-bound SecretRef tokens, credential discovery, and write-only encrypted environment variables.

* **Core Architecture Guide:** [Core Features: vault-and-secrets.md](../../../core-features/vault-and-secrets/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

<!-- generated:tool-list (from the tool pages in this folder; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
## Tool Inventory (9 Tools)

Capability bundles of these tools: `secret_store`, `vault_auth`.

| Tool | What it does |
| :--- | :--- |
| **[`nova.secret_delete`](nova-secret-delete.md)** | Deletes an encrypted environment variable or API key secret from the DPAPI store. |
| **[`nova.secret_list`](nova-secret-list.md)** | Lists registered secret names, scopes, and association identifiers from Nova's user-managed keystore without disclosing secret values. |
| **[`nova.secret_set`](nova-secret-set.md)** | Stores an encrypted secret (such as API keys, tokens, or private credentials) into Nova's user-managed secure store with Windows DPAPI encryption. |
| **[`nova.type_selector_secret`](nova-type-selector-secret.md)** | Types a vault password into a target form field using an ephemeral `SecretRef` token, setting the value through the field's native value setter and dispatching input/change events, without exposing plaintext secrets to the agent. |
| **[`nova.vault_delete`](nova-vault-delete.md)** | Deletes a stored website login credential entry from the encrypted vault. |
| **[`nova.vault_get`](nova-vault-get.md)** | Retrieves metadata and account identifiers for a stored vault entry, resolving username ambiguity without exposing password credentials. |
| **[`nova.vault_list`](nova-vault-list.md)** | Lists stored credential entries (site domain, associated usernames, and creation source) without returning passwords. |
| **[`nova.vault_prepare_fill`](nova-vault-prepare-fill.md)** | Prepares stored credentials from the secure Vault for automated form-filling, returning an ephemeral, origin-bound, and single-use `SecretRef` token instead of the raw password string. |
| **[`nova.vault_set`](nova-vault-set.md)** | Stores or updates a username and password login credential in the encrypted vault. |
<!-- /generated:tool-list -->

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
