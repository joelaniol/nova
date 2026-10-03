# `nova.vault_get`

Retrieves metadata and account identifiers for a stored vault entry, resolving username ambiguity without exposing password credentials.

---

## 1. Overview

`nova.vault_get` looks up vault metadata for a designated web service or URL. If multiple accounts exist for the requested site (e.g. a personal GitHub account and an organization service bot) and no username is provided, Nova returns the list of candidate usernames so the agent can select the correct account before form submission.

* **Capability Bundle:** `vault_and_security`
* **Zero Secret Exposure:** Passwords are never returned; use [`nova.vault_prepare_fill`](nova-vault-prepare-fill.md) to initiate fill workflows.
* **Account Disambiguation:** Returns all valid usernames associated with a site when ambiguous.
* **Metadata Insights:** Reports last updated timestamps, origin constraints, and custom metadata fields.

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`site`** | `string` | **Yes** | — | Domain or URL fragment to match (e.g. `"github.com"`). |
| **`username`** | `string` | No | `null` | Optional specific username to inspect. |
| **`_meta.intent`**| `string` | **Conditional**| — | Audit trail statement explaining the lookup. |

---

## 3. Example Calls

### Look Up Account for Known Domain
```json
{
  "_meta": { "intent": "Resolving credentials for Jira workspace" },
  "site": "company.atlassian.net"
}
```

### Disambiguate Between Multiple Usernames
```json
{
  "_meta": { "intent": "Inspecting specific developer profile" },
  "site": "github.com",
  "username": "lead-dev@company.com"
}
```

---

## 4. Return Value Structure

When multiple accounts exist:
```json
{
  "site": "github.com",
  "matchStatus": "multiple_accounts",
  "availableUsernames": [
    "personal_account",
    "lead-dev@company.com"
  ],
  "guidance": "Specify one of the available usernames in your next call to vault_get or vault_prepare_fill."
}
```

When resolved to a single entry:
```json
{
  "site": "company.atlassian.net",
  "matchStatus": "resolved",
  "username": "support-agent@company.com",
  "hasPassword": true,
  "hasTotp": false,
  "notes": "Staging Jira administrator credentials"
}
```

---

## 5. Related Tools & Documentation

* [`nova.vault_prepare_fill`](nova-vault-prepare-fill.md) — Request single-use fill token for the resolved entry.
* [`nova.vault_list`](nova-vault-list.md) — List all stored domains and accounts.
* [`nova.type_selector_secret`](nova-type-selector-secret.md) — Inject the password into the browser form.
