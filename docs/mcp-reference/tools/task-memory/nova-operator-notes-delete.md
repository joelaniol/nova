# `nova.operator_notes_delete`

Deletes an operator note by unique ID.

---

## 1. Overview

`nova.operator_notes_delete` removes an operator note from the persistent database after the user confirms it.

From 1.0.0-alpha.19 (upcoming, not published yet), every delete first shows the user a Nova dialog with the note's tags and content; Nova never remembers the answer. Declining returns `-32036` and the note stays; without a confirmation UI (for example an unattended run) the call fails with `-32033`. Agents should update an outdated note with `nova.operator_notes_store(id=...)` instead of deleting it.

* **Core Architecture Guide:** [Operator Notes](../../../core-features/learning/operator-notes/README.md)

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

If the ID does not match any stored note, the call still succeeds (no error, no dialog) with `deleted: false` and a matching text message.

| Code | Meaning |
| :--- | :--- |
| `-32036` | The user declined; the note stays. Do not retry without a new reason from the user. |
| `-32033` | No confirmation UI is available (for example an unattended run); the note stays. |

---

## 4. Operational Best Practices

* **Update Before Deleting:** Correct an outdated note with `nova.operator_notes_store(id=...)`; delete only when the user wants the note gone.

---

## 5. Related Tools

* [`nova.operator_notes_list`](nova-operator-notes-list.md)
* [`nova.operator_notes_store`](nova-operator-notes-store.md)
