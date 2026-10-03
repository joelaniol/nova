# `nova.operator_notes_store`

Stores or updates a persistent operator note with search tags and priority.

---

## 1. Overview

`nova.operator_notes_store` saves human-authored operating instructions that are automatically indexed and surfaced to agents working in matching domains or tasks.

* **Capability Bundle:** `task_memory`
* **Security Tier:** Tier 2 (Note Storage)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `content` | `string` | Yes | — | — | The note content (user preference, workflow hint, environment info). |
| `tags` | `array` of `string` | Yes | — | — | Keywords for matching (e.g. ["sandbox", "gpt", "pro"]). |
| `category` | `string` | No | — | — | Optional category (e.g. 'environment', 'workflow', 'preference'). |
| `source` | `string` | No | `"agent"` | `agent`, `user` | Who created this note: 'agent' or 'user'. |
| `id` | `string` | No | — | — | Optional: existing note ID to update instead of creating new. |
| `sandboxId` | `string` | No | — | — | Optional sandbox letter-id (e.g. 'A', 'B') to bind this note to a specific sandbox. Omit for global note. Required together with sandboxRef. |
| `sandboxRef` | `string` | No | — | — | Opaque PersistentUid token from nova.tabs / nova.sandbox_context / perceive.targetContext. Mandatory when sandboxId is set; protects against letter-id recycling races. Mismatch with current sandbox UID → -32602 stale_sandbox_reference. |
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.operator_notes_store",
  "arguments": {
    "content": "Always check inventory in warehouse B first",
    "tags": [
      "inventory",
      "orders"
    ]
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Stored operator note (id: op-note-102)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "id": "op-note-102",
    "status": "Stored"
  }
}
```

---

## 4. Operational Best Practices

* **Tag Quality:** Supply distinct, lowercase tags to ensure accurate keyword matching.

---

## 5. Related Tools

* [`nova.operator_notes_query`](nova-operator-notes-query.md)
* [`nova.domain_note`](nova-domain-note.md)
