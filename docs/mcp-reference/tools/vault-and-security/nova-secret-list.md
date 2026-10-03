# `nova.secret_list`

Lists registered secret names, scopes, and association identifiers from Nova's user-managed keystore without disclosing secret values.

---

## 1. Overview

`nova.secret_list` provides inventory visibility into environment variables and secrets configured across workspaces and scheduled tasks. In accordance with zero-trust architectural design, secret values are omitted entirely from response payloads, guaranteeing that no LLM or prompt inspection can leak credentials.

* **Capability Bundle:** `vault_and_security`, `system_and_recovery`
* **Zero Value Disclosures:** Only names, scopes, and creation metadata are returned.
* **Granular Filtering:** Filter by `scope` (`global`, `workspace`, or `task`), or restrict to a specific `workspaceId` or `taskId`.
* **Paginated Output:** Supports `limit` and `offset` for large corporate deployments.

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`scope`** | `string` | No | `null` | Optional scope filter: `"global"`, `"workspace"`, or `"task"`. Omit for global + workspace. |
| **`workspaceId`**| `string` | No | `null` | Return only secrets scoped or granted to this workspace. |
| **`taskId`** | `string` | **Conditional**| `null` | Required when `scope: "task"`. |
| **`limit`** | `integer` | No | `100` | Maximum number of secret records to return (1?500). |
| **`offset`** | `integer` | No | `0` | Number of records to skip for pagination. |
| **`_meta.intent`**| `string` | **Conditional**| ? | Audit trail statement explaining why secrets are being audited. |

---

## 3. Example Calls

### List All Secrets Configured for a Workspace
```json
{
  "_meta": { "intent": "Verifying required environment variables are set before starting build" },
  "workspaceId": "ws-backend-deploy"
}
```

### Inspect Secrets Dedicated to a Scheduled Task
```json
{
  "_meta": { "intent": "Checking backup runner credentials" },
  "scope": "task",
  "taskId": "task-nightly-backup"
}
```

---

## 4. Return Value Structure

```json
{
  "total": 3,
  "limit": 100,
  "offset": 0,
  "secrets": [
    {
      "name": "DEPLOY_API_TOKEN",
      "scope": "workspace",
      "workspaceId": "ws-backend-deploy",
      "createdAtUtc": "2026-10-02T19:55:00Z"
    },
    {
      "name": "NPM_AUTH_TOKEN",
      "scope": "workspace",
      "workspaceId": "ws-backend-deploy",
      "createdAtUtc": "2026-09-28T11:20:00Z"
    },
    {
      "name": "COMPANY_MAILING_API_KEY",
      "scope": "global",
      "grantedWorkspaces": ["ws-backend-deploy"],
      "createdAtUtc": "2026-09-15T08:00:00Z"
    }
  ]
}
```

---

## 5. Related Tools & Documentation

* [`nova.secret_set`](nova-secret-set.md) ? Store a new DPAPI-encrypted secret.
* [`nova.vault_list`](nova-vault-list.md) ? List web browser login credentials.
* [Vault & Secret Architecture](../../../core-features/vault-and-secrets.md) ? Architectural overview of Nova secret isolation.
