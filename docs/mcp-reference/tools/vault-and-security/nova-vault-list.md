# `nova.vault_list`

Lists stored credential entries (site domain, associated usernames, and creation source) without returning passwords.

---

## 1. Overview

`nova.vault_list` enables agents to discover available stored credentials in the secure Vault. To adhere to least-privilege principles, the tool never returns secret values. Furthermore, passing an optional `site` filter restricts results to relevant domains, preventing the exposure of unrelated user accounts to the agent's context window.

* **Capability Bundle:** `vault_and_security`
* **Zero Password Exposure:** Returns only metadata: `site`, `username`, and `createdBy`.
* **Domain Substring Filtering (`site`):** Narrow search to a specific provider (e.g. `github.com`).
* **Multi-Account Discovery:** Quickly identify which accounts are configured for a given service.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `site` | `string` | No | — | — | Optional: only list entries whose site matches this fragment (e.g. 'linkedin.com'). Substring, case-insensitive. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).
<!-- /generated:parameters -->

---

## 3. Example Calls

### Discover Credentials for a Specific Domain
```json
{
  "_meta": { "intent": "Checking if credentials exist for staging server" },
  "site": "gitlab.example.com"
}
```

### List All Configured Sites in Vault
```json
{
  "_meta": { "intent": "Auditing configured service logins" }
}
```

---

## 4. Return Value Structure

```json
{
  "totalEntries": 2,
  "entries": [
    {
      "site": "github.com",
      "username": "developer@example.com",
      "createdBy": "user_import",
      "lastUsedUtc": "2026-10-01T14:22:00Z"
    },
    {
      "site": "github.com",
      "username": "ci-automation-bot",
      "createdBy": "agent_vault_set",
      "lastUsedUtc": "2026-10-02T09:15:00Z"
    }
  ]
}
```

---

## 5. Related Tools & Documentation

* [`nova.vault_prepare_fill`](nova-vault-prepare-fill.md) ? Request single-use fill token for a listed account.
* [`nova.vault_get`](nova-vault-get.md) ? Inspect metadata for a specific entry.
* [Vault Architecture](../../../core-features/vault-and-secrets.md) ? DPAPI encryption and security controls.
