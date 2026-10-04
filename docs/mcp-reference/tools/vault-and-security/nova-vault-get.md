# `nova.vault_get`

Retrieves metadata and account identifiers for a stored vault entry, resolving username ambiguity without exposing password credentials.

---

## 1. Overview

`nova.vault_get` looks up vault metadata for a designated web service or URL. If multiple accounts exist for the requested site (e.g. a personal GitHub account and an organization service bot) and no username is provided, Nova returns the list of candidate usernames so the agent can select the correct account before form submission.

* **Zero Secret Exposure:** Passwords are never returned; use [`nova.vault_prepare_fill`](nova-vault-prepare-fill.md) to initiate fill workflows.
* **Account Disambiguation:** Returns all valid usernames associated with a site when ambiguous.
* **Metadata Insights:** Reports who created the entry and when, plus whether a password is stored.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `site` | `string` | Yes | — | — | Domain or URL fragment to match (e.g. 'github.com'). |
| `username` | `string` | No | — | — | Optional specific username. Required after selecting one when multiple accounts remain for the site. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `vault_auth` (load it with `nova.tools_bundle(bundle='vault_auth')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

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

When multiple accounts exist and no `username` was given:
```json
{
  "found": true,
  "site": "github.com",
  "matchCount": 2,
  "ambiguous": true,
  "accounts": [
    { "username": "personal_account", "createdBy": null },
    { "username": "lead-dev@company.com", "createdBy": "agent" }
  ]
}
```

When resolved to a single entry:
```json
{
  "found": true,
  "entryId": "a1b2c3d4",
  "site": "company.atlassian.net",
  "username": "support-agent@company.com",
  "createdBy": "agent",
  "createdUtc": "2026-09-15T08:00:00Z",
  "passwordAvailable": true,
  "passwordRedacted": true,
  "retrievalMode": "secretref_required",
  "nextTool": "nova.vault_prepare_fill",
  "matchCount": 1
}
```

Nova never returns the password itself; `passwordAvailable`/`passwordRedacted` only report whether a password is stored. There is no stored notes or one-time-password field.

---

## 5. Related Tools & Documentation

* [`nova.vault_prepare_fill`](nova-vault-prepare-fill.md) — Request single-use fill token for the resolved entry.
* [`nova.vault_list`](nova-vault-list.md) — List all stored domains and accounts.
* [`nova.type_selector_secret`](nova-type-selector-secret.md) — Set the password into the browser form.
