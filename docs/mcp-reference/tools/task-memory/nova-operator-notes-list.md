# `nova.operator_notes_list`

Lists all persistent operator notes with tags and sandbox scopes.

---

## 1. Overview

`nova.operator_notes_list` returns a paginated list of human operator notes, including tags, priorities, and sandbox assignments.

* **Capability Bundle:** `task_memory`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `offset` | `integer` | No | `0` | ≥ 0 | Skip first N entries. Default: 0. |
| `limit` | `integer` | No | `20` | 1–100 | Maximum results. Default: 20. |
| `scope` | `string` | No | `"current_sandbox"` | `current_sandbox`, `global`, `all`, `orphaned` | Filter scope: 'current_sandbox' (default) = active sandbox + global; 'global' = only global notes; 'all' = no filter; 'orphaned' = notes anchored to deleted sandboxes. |
| `sandboxId` | `string` | No | — | — | Optional explicit sandbox letter-id to override the active-target resolution. Requires sandboxRef. |
| `sandboxRef` | `string` | No | — | — | Opaque PersistentUid token from nova.tabs / nova.sandbox_context. Mandatory when sandboxId is set. |
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.operator_notes_list",
  "arguments": {
    "limit": 10
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Loaded 1 operator note."
    }
  ],
  "structuredContent": {
    "ok": true,
    "total": 1,
    "notes": [
      {
        "id": "op-note-101",
        "content": "Never delete test databases on staging",
        "tags": [
          "staging",
          "safety"
        ]
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Review Active Directives:** Review operator directives before running high-risk automation tasks.

---

## 5. Related Tools

* [`nova.operator_notes_query`](nova-operator-notes-query.md)
* [`nova.operator_notes_store`](nova-operator-notes-store.md)
