# `nova.operator_notes_delete`

Deletes an operator note by unique ID.

---

## 1. Overview

`nova.operator_notes_delete` removes an operator note from the persistent database.

* **Capability Bundle:** `task_memory`
* **Security Tier:** Tier 2 (Note Deletion)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`id`** | `string` | Yes | `null` | Note ID from nova.operator_notes_list. |

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
