# `nova.operator_notes_delete`

Deletes an operator note by unique ID.

---

## 1. Overview

`nova.operator_notes_delete` removes an operator note from the persistent database.

* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/episodic-task-memory-etm/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `id` | `string` | Yes | — | — | Note ID from nova.operator_notes_list. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.operator_notes_delete",
  "arguments": {
    "id": "a3f1c9e2b4d6487f9a21e0d4f1a2b3c4"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Deleted operator note 'a3f1c9e2b4d6487f9a21e0d4f1a2b3c4'."
    }
  ],
  "structuredContent": {
    "deleted": true,
    "id": "a3f1c9e2b4d6487f9a21e0d4f1a2b3c4"
  }
}
```

If the ID does not match any stored note, the call still succeeds (no error) with `deleted: false` and a matching text message.

---

## 4. Operational Best Practices

* **Clean Stale Instructions:** Remove temporary guidance once automated workflows have been updated.

---

## 5. Related Tools

* [`nova.operator_notes_list`](nova-operator-notes-list.md)
* [`nova.operator_notes_store`](nova-operator-notes-store.md)
