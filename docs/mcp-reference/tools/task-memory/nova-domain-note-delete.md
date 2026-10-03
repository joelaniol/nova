# `nova.domain_note_delete`

Deletes a domain note by domain name and key.

---

## 1. Overview

`nova.domain_note_delete` removes an obsolete note for a specific domain and scope.

* **Capability Bundle:** `task_memory`
* **Security Tier:** Tier 2 (Note Deletion)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`domain`** | `string` | Yes | `null` | The domain (e.g. 'vxlive.net'). |
| **`key`** | `string` | Yes | `null` | The note key to delete. |
| **`sandboxId`** | `string` | No | `null` | Optional explicit sandbox letter-id. Without explicit scope, sandboxId-only delete removes only the sandbox-specific note (not the global twin). Requires sandboxRef. |
| **`sandboxRef`** | `string` | No | `null` | Opaque PersistentUid token from nova.tabs / nova.sandbox_context. Mandatory when sandboxId is set. |
| **`scope`** | `string` | No | `null` | Disambiguation scope. 'global' deletes only the global note; 'current_sandbox' (default) deletes global + active-sandbox match; 'all' deletes every matching note regardless of scope; 'orphaned' deletes only notes anchored to deleted sandboxes. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.domain_note_delete",
  "arguments": {
    "domain": "internal.corp",
    "key": "auth_hint"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Deleted note auth_hint for internal.corp."
    }
  ],
  "structuredContent": {
    "ok": true,
    "domain": "internal.corp",
    "key": "auth_hint",
    "status": "Deleted"
  }
}
```

---

## 4. Operational Best Practices

* **Scope Awareness:** Specify `scope` (`global` or `sandbox`) if notes exist in multiple tiers.

---

## 5. Related Tools

* [`nova.domain_note`](nova-domain-note.md)
* [`nova.domain_notes_list`](nova-domain-notes-list.md)
