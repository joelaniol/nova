# `nova.domain_notes_list`

Lists all stored procedural notes and operator instructions for a specific domain.

---

## 1. Overview

`nova.domain_notes_list` returns all active notes registered for a target web domain, indicating keys, values, must-read statuses, and sandbox scopes.

* **Capability Bundle:** `task_memory`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `domain` | `string` | Yes | — | — | The domain to list notes for (e.g. 'vxlive.net'). |
| `scope` | `string` | No | `"current_sandbox"` | `current_sandbox`, `global`, `all`, `orphaned` | Filter scope: 'current_sandbox' (default) = active sandbox + global; 'global' = only global notes; 'all' = no filter; 'orphaned' = notes anchored to deleted sandboxes (cleanup view). |
| `sandboxId` | `string` | No | — | — | Optional explicit sandbox letter-id to override the active-target resolution. Requires sandboxRef. On list this is additive (global + that sandbox); on domain_note_delete, sandboxId without scope is sandbox-only. |
| `sandboxRef` | `string` | No | — | — | Opaque PersistentUid token from nova.tabs / nova.sandbox_context. Mandatory when sandboxId is set. |
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.domain_notes_list",
  "arguments": {
    "domain": "internal.corp"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Found 1 note for internal.corp."
    }
  ],
  "structuredContent": {
    "ok": true,
    "domain": "internal.corp",
    "notes": [
      {
        "key": "auth_hint",
        "value": "Use SAML SSO...",
        "isMustRead": false
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Pre-Flight Inspection:** Check domain notes upon first entering an unfamiliar enterprise domain.

---

## 5. Related Tools

* [`nova.domain_note`](nova-domain-note.md)
* [`nova.operator_notes_query`](nova-operator-notes-query.md)
