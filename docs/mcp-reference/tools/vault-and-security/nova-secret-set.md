# `nova.secret_set`

Stores an encrypted secret (such as API keys, tokens, or private credentials) into Nova's user-managed secure store with Windows DPAPI encryption.

---

## 1. Overview

Autonomous agents executing terminal commands, shell scripts, or scheduled tasks frequently require API keys (e.g. `OPENAI_API_KEY`, `AWS_SECRET_ACCESS_KEY`, `GITHUB_TOKEN`). Hardcoding these secrets into scripts, bash history, or LLM chat logs is unsafe.

`nova.secret_set` stores credentials directly into Nova's encrypted keystore. Secrets are encrypted at rest using Windows Data Protection API (DPAPI) tied to the current OS user. Once stored, **the secret value is never returned by any MCP tool**. Instead, Nova injects the secret directly as an environment variable into authorized terminal sessions and background task executions.

* **DPAPI Encryption at Rest:** Protected by the operating system's cryptographic infrastructure.
* **Write-Only Security Guarantee:** No tool, log, or MCP RPC can read back the plaintext value.
* **Three Strict Injection Scopes:** `workspace`, `task`, and `global`.
* **System Variable Protection:** Automatically rejects overwrites to critical OS variables (`PATH`, `TEMP`, `NOVA_*`).

---

## 2. Storage Scopes

| Scope | Injection Target | Activation Rule |
| :--- | :--- | :--- |
| **`workspace`** | Injected into terminal sessions & tasks within a specific workspace ID. | Immediate availability for sessions in `workspaceId`. |
| **`task`** | Injected only during execution of a specific scheduled task. | Bound strictly to `taskId`. |
| **`global`** | Stored in the central user vault. | Requires explicit user approval in Nova Settings before granting to a workspace. |

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `name` | `string` | Yes | — | — | Secret name = environment variable name (letters/digits/underscore, 1-64 chars; reserved system names like PATH/TEMP/NOVA_* rejected). |
| `value` | `string` | Yes | — | — | Secret value (DPAPI-encrypted at rest, never returned). |
| `scope` | `string` | Yes | — | `global`, `workspace`, `task` | Where the secret lives and injects. |
| `workspaceId` | `string` | No | — | — | Terminal workspace id (required for scope='workspace'). |
| `taskId` | `string` | No | — | — | Task id (required for scope='task'). |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `secret_store` (load it with `nova.tools_bundle(bundle='secret_store')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 4. Example Calls

### Store API Key for a Terminal Workspace
```json
{
  "_meta": { "intent": "Provisioning API token for automated deployment runner" },
  "name": "DEPLOY_API_TOKEN",
  "value": "sec_prod_991823719283719283",
  "scope": "workspace",
  "workspaceId": "ws-backend-deploy"
}
```

### Store Dedicated Secret for a Scheduled Backup Task
```json
{
  "_meta": { "intent": "Setting S3 bucket secret for scheduled database backup" },
  "name": "S3_BACKUP_SECRET_KEY",
  "value": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
  "scope": "task",
  "taskId": "task-nightly-backup"
}
```

---

## 5. Return Value Structure

```json
{
  "name": "DEPLOY_API_TOKEN",
  "scope": "workspace",
  "workspaceId": "ws-backend-deploy",
  "stored": true,
  "replaced": false
}
```

`replaced` is `true` when the call overwrote an existing secret of the same name/scope.

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `name must be letters/digits/underscore (1-64 chars) and not a reserved system variable name (PATH, TEMP, NOVA_*, ...)` | Name failed validation or is a protected OS variable. | Choose a valid, application-specific environment variable name. |
| `workspaceId is required` / `terminal workspace '...' not found` | Scope was set to `"workspace"` without a valid, existing `workspaceId`. | Provide the ID of an existing terminal workspace. |
| `Task-scoped secrets require the Scheduled tasks feature to be enabled in Nova settings` | Scope was set to `"task"` while the Scheduled Tasks feature is disabled. | Enable Scheduled Tasks, or use `scope='global'`/`'workspace'` instead. |

---

## 7. Related Tools & Documentation

* [`nova.secret_list`](nova-secret-list.md) — List configured secret names and scopes without reading values.
* [`nova.vault_prepare_fill`](nova-vault-prepare-fill.md) — Web browser password filling via `SecretRef`.
* [Vault & Secret Architecture](../../../core-features/vault-and-secrets.md) — Deep dive into Nova's encryption boundary.
