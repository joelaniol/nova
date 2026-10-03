# `nova.operator_notes_delete`

Deletes an operator note by unique ID.

---

## 1. Overview

`nova.operator_notes_delete` removes an operator note from the persistent database.

* **Security Tier:** Tier 2 (Note Deletion)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `id` | `string` | Yes | — | — | Note ID from nova.operator_notes_list. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.operator_notes_delete",
  "arguments": {
    "id": "op-note-101"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Deleted operator note op-note-101."
    }
  ],
  "structuredContent": {
    "ok": true,
    "id": "op-note-101",
    "status": "Deleted"
  }
}
```

---

## 4. Operational Best Practices

* **Clean Stale Instructions:** Remove temporary guidance once automated workflows have been updated.

---

## 5. Related Tools

* [`nova.operator_notes_list`](nova-operator-notes-list.md)
* [`nova.operator_notes_store`](nova-operator-notes-store.md)
