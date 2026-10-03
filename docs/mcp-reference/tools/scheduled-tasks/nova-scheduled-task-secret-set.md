# `nova.scheduled_task_secret_set`

Stores an encrypted secret (API key, auth token) for a task using Windows DPAPI encryption.

---

## 1. Overview

`nova.scheduled_task_secret_set` associates an encrypted credential with a task. Secrets are encrypted using Windows Data Protection API (DPAPI) tied to the current OS user and decrypted only in-memory during task execution. Secret values are write-only and cannot be retrieved via MCP tools.

* **Capability Bundle:** `scheduled_tasks`
* **Security Tier:** Tier 2 (Encrypted Secret Storage)
* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `taskId` | `string` | Yes | — | — | The task ID. |
| `key` | `string` | Yes | — | — | Secret key name (e.g. 'api_key', 'webhook_token'). |
| `value` | `string` | Yes | — | — | Secret value (will be DPAPI-encrypted, never stored in plaintext). |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).
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
      "text": "Secret 'OPENAI_API_KEY' stored and DPAPI-encrypted for task-7c81a2f0."
    }
  ],
  "structuredContent": {
    "ok": true,
    "taskId": "task-7c81a2f0",
    "key": "OPENAI_API_KEY",
    "status": "EncryptedAndStored"
  }
}
```

---

## 4. Operational Best Practices

* **Environment Injection:** During execution, Nova decrypts secrets and injects them as environment variables matching their key names.
* **Zero Plaintext Exposure:** Secrets are never written to disk unencrypted, logged in stdout/stderr streams, or returned in query tools.
* **Auditing Keys:** Use [`nova.scheduled_task_secret_list`](nova-scheduled-task-secret-list.md) to verify registered secret key names.

---

## 5. Related Tools

* [`nova.scheduled_task_secret_list`](nova-scheduled-task-secret-list.md) — List registered secret key names.
* [`nova.secret_set`](../vault-and-security/nova-secret-set.md) — Global browser secret store.
