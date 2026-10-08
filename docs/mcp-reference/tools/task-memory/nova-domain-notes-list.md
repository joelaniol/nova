# `nova.domain_notes_list`

Lists all stored procedural notes and operator instructions for a specific domain.

---

## 1. Overview

`nova.domain_notes_list` returns all notes registered for a target web domain, indicating keys, values, source, enforcement level, and sandbox scope.

* **Core Architecture Guide:** [Operational Knowledge](../../../core-features/learning/operational-knowledge-ok/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `domain` | `string` | Yes | — | — | The domain to list notes for (e.g. 'vxlive.net'). |
| `scope` | `string` | No | `"current_sandbox"` | `current_sandbox`, `global`, `all`, `orphaned` | Filter scope: 'current_sandbox' (default) = active sandbox + global; 'global' = only global notes; 'all' = no filter; 'orphaned' = notes anchored to deleted sandboxes (cleanup view). |
| `sandboxId` | `string` | No | — | — | Optional explicit sandbox letter-id to override the active-target resolution. Requires sandboxRef. On list this is additive (global + that sandbox); on domain_note_delete, sandboxId without scope is sandbox-only. |
| `sandboxRef` | `string` | No | — | — | Opaque PersistentUid token from nova.tabs / nova.sandbox_context. Mandatory when sandboxId is set. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
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
      "text": "1 note(s) for internal.corp (scope=current_sandbox)."
    }
  ],
  "structuredContent": {
    "domain": "internal.corp",
    "scope": "current_sandbox",
    "resolvedSandboxRef": null,
    "notes": [
      {
        "id": "note-7f2a1",
        "key": "auth_hint",
        "value": "Use SAML single sign-on button; avoid username/password form.",
        "createdUtc": "2026-08-15T09:30:00Z",
        "updatedUtc": "2026-08-15T09:30:00Z",
        "source": "agent",
        "enforcement": "none",
        "repeatMinutes": null,
        "repeatToolCalls": null,
        "sandboxId": null,
        "sandboxName": null,
        "sandboxRef": null,
        "sandboxStatus": null
      }
    ],
    "hint": "Domain notes are snapshots. source=user notes are user instructions to follow; source=agent notes are your own past observations."
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
