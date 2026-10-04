# `nova.vault_delete`

> **Deletes a stored website login credential entry from the encrypted vault.**

* **Core Feature Guide:** [Vault & Secret Keystore](../../../core-features/vault-and-secrets.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.vault_delete` removes one login entry from Nova's vault by its entry `id` (from `nova.vault_list`); site and username are not accepted as keys. If the entry was imported by password sync, Nova also remembers not to import it again. An unknown `id` returns `deleted: false`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `id` | `string` | Yes | — | — | Entry ID from nova.vault_list. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `vault_auth` (load it with `nova.tools_bundle(bundle='vault_auth')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_vault_delete",
  "arguments": {
    "_meta": { "intent": "Removing the temporary staging login after the test run" },
    "id": "3fa91c2e"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Deleted vault entry '3fa91c2e'."
    }
  ],
  "structuredContent": {
    "deleted": true,
    "id": "3fa91c2e"
  }
}
```

Not found: `{ "deleted": false, "id": "..." }` with the text "No vault entry found with id '<id>'.".

---

## 4. Operational Best Practices

* **Account cleanup:** Remove temporary test credentials when the test run is over; look up the entry `id` with `nova.vault_list` first.

---

## 5. Related Tools

* [`nova.vault_set`](nova-vault-set.md)
* [`nova.vault_list`](nova-vault-list.md)
