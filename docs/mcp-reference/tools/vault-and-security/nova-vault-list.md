# `nova.vault_list`

Lists stored credential entries (site domain, associated usernames, and creation source) without returning passwords.

---

## 1. Overview

`nova.vault_list` enables agents to discover available stored credentials in the secure Vault. To adhere to least-privilege principles, the tool never returns secret values. Furthermore, passing an optional `site` filter restricts results to relevant domains, preventing the exposure of unrelated user accounts to the agent's context window.

* **Zero Password Exposure:** Returns only metadata (entry id, `site`, `username`, `createdBy`, `createdUtc`) — never the password.
* **Domain Substring Filtering (`site`):** Narrow search to a specific provider (e.g. `github.com`).
* **Multi-Account Discovery:** Quickly identify which accounts are configured for a given service.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `site` | `string` | No | — | — | Optional: only list entries whose site matches this fragment (e.g. 'linkedin.com'). Substring, case-insensitive. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `vault_auth` (load it with `nova.tools_bundle(bundle='vault_auth')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
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
  "entries": [
    {
      "id": "a1b2c3d4",
      "site": "github.com",
      "username": "developer@example.com",
      "createdBy": "user_import",
      "createdUtc": "2026-10-01T14:22:00Z"
    },
    {
      "id": "e5f6g7h8",
      "site": "github.com",
      "username": "ci-automation-bot",
      "createdBy": "agent",
      "createdUtc": "2026-10-02T09:15:00Z"
    }
  ],
  "matchCount": 2,
  "siteFilter": "github.com"
}
```

`siteFilter` is `null` when the call did not pass a `site` filter.

---

## 5. Related Tools & Documentation

* [`nova.vault_prepare_fill`](nova-vault-prepare-fill.md) — Request single-use fill token for a listed account.
* [`nova.vault_get`](nova-vault-get.md) — Inspect metadata for a specific entry.
* [Vault Architecture](../../../core-features/vault-and-secrets/README.md) — DPAPI encryption and security controls.
