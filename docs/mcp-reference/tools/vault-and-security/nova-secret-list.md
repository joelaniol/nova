# `nova.secret_list`

Lists registered secret names, scopes, and association identifiers from Nova's user-managed keystore without disclosing secret values.

---

## 1. Overview

`nova.secret_list` provides inventory visibility into environment variables and secrets configured globally and per workspace. In accordance with zero-trust architectural design, secret values are omitted entirely from response payloads, guaranteeing that no LLM or prompt inspection can leak credentials.

* **Zero Value Disclosures:** Only names, scopes, and creation metadata are returned.
* **Granular Filtering:** Filter by `scope` (`global` or `workspace`), or restrict to a specific `workspaceId`.
* **Paginated Output:** Supports `limit` and `offset` for large corporate deployments.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `scope` | `string` | No | — | `global`, `workspace` | Optional scope filter. |
| `workspaceId` | `string` | No | — | — | Optional: only secrets scoped or granted to this workspace. |
| `limit` | `integer` | No | `100` | 1–500 | Maximum entries to return (1-500). Default: 100. |
| `offset` | `integer` | No | `0` | ≥ 0 | Number of entries to skip before returning this page. Default: 0. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `secret_store` (load it with `nova.tools_bundle(bundle='secret_store')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Example Calls

### List All Secrets Configured for a Workspace
```json
{
  "_meta": { "intent": "Verifying required environment variables are set before starting build" },
  "workspaceId": "ws-backend-deploy"
}
```

---

## 4. Return Value Structure

```json
{
  "secrets": [
    {
      "name": "DEPLOY_API_TOKEN",
      "scope": "workspace",
      "workspaceId": "ws-backend-deploy",
      "grantedWorkspaceIds": null,
      "updatedUtc": "2026-10-02T19:55:00Z"
    },
    {
      "name": "NPM_AUTH_TOKEN",
      "scope": "workspace",
      "workspaceId": "ws-backend-deploy",
      "grantedWorkspaceIds": null,
      "updatedUtc": "2026-09-28T11:20:00Z"
    },
    {
      "name": "COMPANY_MAILING_API_KEY",
      "scope": "global",
      "workspaceId": null,
      "grantedWorkspaceIds": ["ws-backend-deploy"],
      "updatedUtc": "2026-09-15T08:00:00Z"
    }
  ],
  "returnedCount": 3,
  "totalCount": 3,
  "limit": 100,
  "offset": 0,
  "truncated": false,
  "nextOffset": null
}
```

---

## 5. Operational Best Practices

* **Zero-Knowledge Token Boundary:** `secret_list` never reveals secret values. Use it solely to audit inventory, check variable availability, and verify scope associations before invoking commands or background jobs.
* **Scope Hierarchy Awareness:** Understand that `global` secrets are accessible workspace-wide, and `workspace` secrets are bound to a specific terminal workspace ID (`workspaceId`).
* **Pagination on Corporate Deployments:** When listing extensive secret stores, respect the default `limit: 100` (max 500) and check `truncated: true` and `nextOffset` to iterate through pages.
* **Auditing Before Execution:** Run `secret_list` with `workspaceId` prior to running terminal builds or deploy scripts to ensure all required API keys and deployment tokens are provisioned.

---

## 6. Related Tools & Documentation

* [`nova.secret_set`](nova-secret-set.md) — Store a new DPAPI-encrypted secret.
* [`nova.vault_list`](nova-vault-list.md) — List web browser login credentials.
* [Vault & Secret Architecture](../../../core-features/privacy/vault-and-secrets/README.md) — Architectural overview of Nova secret isolation.
