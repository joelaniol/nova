# `nova.scheduled_task_secret_set`

Stores an encrypted secret (API key, auth token) for a task using Windows DPAPI encryption.

---

## 1. Overview

`nova.scheduled_task_secret_set` associates an encrypted credential with a task. Secrets are encrypted using Windows Data Protection API (DPAPI) tied to the current OS user and decrypted only in-memory during task execution. Secret values are write-only and cannot be retrieved via MCP tools.

* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `taskId` | `string` | Yes | — | — | The task ID. |
| `key` | `string` | Yes | — | — | Secret key name (e.g. 'api_key', 'webhook_token'). |
| `value` | `string` | Yes | — | — | Secret value (will be DPAPI-encrypted, never stored in plaintext). |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `scheduled_tasks` (load it with `nova.tools_bundle(bundle='scheduled_tasks')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_secret_set",
  "arguments": {
    "taskId": "task-7c81a2f0",
    "key": "OPENAI_API_KEY",
    "value": "sk-proj-xyz123..."
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Secret 'OPENAI_API_KEY' stored (DPAPI-encrypted) for task 'task-7c81a2f0'. Reference it in argsTemplate as {SECRET:OPENAI_API_KEY}."
    }
  ],
  "structuredContent": {
    "taskId": "task-7c81a2f0",
    "key": "OPENAI_API_KEY",
    "stored": true
  }
}
```

---

## 4. Operational Best Practices

* **Environment Injection:** For process-based executors (`ClaudeCode`, `CodexCli`, `Shell`, `CustomCommand`), Nova decrypts secrets at run start and injects them as environment variables matching their key names. For `HttpWebhook` tasks (no subprocess), `{SECRET:key}` placeholders in `argsTemplate` are substituted directly instead.
* **Zero Plaintext Exposure:** Secrets are never written to disk unencrypted and are not returned by any MCP tool.
* **Reserved Names Rejected:** A key matching a reserved system variable name (`PATH`, `TEMP`, `NOVA_*`, …) is rejected.
* **Auditing Keys:** Use [`nova.scheduled_task_secret_list`](nova-scheduled-task-secret-list.md) to verify registered secret key names.

---

## 5. Related Tools

* [`nova.scheduled_task_secret_list`](nova-scheduled-task-secret-list.md) — List registered secret key names.
* [`nova.secret_set`](../vault-and-security/nova-secret-set.md) — Global browser secret store.
