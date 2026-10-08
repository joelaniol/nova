# `nova.operator_notes_list`

Lists all persistent operator notes with tags and sandbox scopes.

---

## 1. Overview

`nova.operator_notes_list` returns a paginated list of human operator notes, including tags, categories, and sandbox assignments.

* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/learning/episodic-task-memory-etm/README.md)

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

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
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
      "text": "1 of 1 note(s) (scope=current_sandbox)."
    }
  ],
  "structuredContent": {
    "total": 1,
    "offset": 0,
    "scope": "current_sandbox",
    "resolvedSandboxRef": null,
    "notes": [
      {
        "id": "a3f1c9e2b4d6487f9a21e0d4f1a2b3c4",
        "content": "Never delete test databases on staging",
        "tags": ["staging", "safety"],
        "category": null,
        "source": "agent",
        "createdUtc": "2026-09-30T12:00:00Z",
        "lastMatchedUtc": null,
        "matchCount": 0,
        "sandboxId": null,
        "sandboxName": null,
        "sandboxRef": null,
        "sandboxStatus": null
      }
    ],
    "hint": "These notes are snapshots from earlier sessions, not guaranteed facts. Contents may be outdated. If you find a note is no longer accurate, update it via operator_notes_store(id=...) or delete it via operator_notes_delete(id=...)."
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
