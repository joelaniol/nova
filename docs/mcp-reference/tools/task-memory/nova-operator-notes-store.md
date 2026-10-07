# `nova.operator_notes_store`

Stores or updates a persistent operator note with search tags and category.

---

## 1. Overview

`nova.operator_notes_store` saves human-authored operating instructions that are automatically indexed and surfaced to agents working in matching domains or tasks.

* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/episodic-task-memory-etm/README.md)

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

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
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
      "text": "Operator note created."
    }
  ],
  "structuredContent": {
    "action": "created",
    "noteCount": 1,
    "noteId": "a3f1c9e2b4d6487f9a21e0d4f1a2b3c4",
    "missedId": null,
    "sandboxRef": null
  }
}
```

`action` is one of `created`, `updated`, or `created_id_not_found` (the supplied `id` did not match an existing note, so a new one was created instead — `missedId` then carries the unmatched ID).

---

## 4. Operational Best Practices

* **Tag Quality:** Supply distinct, lowercase tags to ensure accurate keyword matching.

---

## 5. Related Tools

* [`nova.operator_notes_query`](nova-operator-notes-query.md)
* [`nova.domain_note`](nova-domain-note.md)
