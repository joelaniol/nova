# `nova.domain_note_delete`

Deletes a domain note by domain name and key.

---

## 1. Overview

`nova.domain_note_delete` removes an obsolete note for a specific domain and scope.

* **Core Architecture Guide:** [Operational Knowledge](../../../core-features/learning/operational-knowledge-ok/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `domain` | `string` | Yes | — | — | The domain (e.g. 'vxlive.net'). |
| `key` | `string` | Yes | — | — | The note key to delete. |
| `scope` | `string` | No | — | `current_sandbox`, `global`, `all`, `orphaned` | Disambiguation scope. 'global' deletes only the global note; 'current_sandbox' (default) deletes global + active-sandbox match; 'all' deletes every matching note regardless of scope; 'orphaned' deletes only notes anchored to deleted sandboxes. |
| `sandboxId` | `string` | No | — | — | Optional explicit sandbox letter-id. Without explicit scope, sandboxId-only delete removes only the sandbox-specific note (not the global twin). Requires sandboxRef. |
| `sandboxRef` | `string` | No | — | — | Opaque PersistentUid token from nova.tabs / nova.sandbox_context. Mandatory when sandboxId is set. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "Deleted 1 domain note(s): internal.corp/auth_hint"
    }
  ],
  "structuredContent": {
    "deleted": true,
    "domain": "internal.corp",
    "key": "auth_hint",
    "deletedCount": 1
  }
}
```

If no note matches, the response is `deleted: false` with `deletedCount: 0`. If notes exist both globally and in a sandbox for the same domain/key and neither `scope` nor `sandboxId` disambiguates, the call fails with `ambiguous_note_target` instead of deleting both.

---

## 4. Operational Best Practices

* **Scope Awareness:** Specify `scope` (`global`, `current_sandbox`, `all`, or `orphaned`) or an explicit `sandboxId`/`sandboxRef` if notes exist both globally and in a sandbox for the same domain/key.

---

## 5. Related Tools

* [`nova.domain_note`](nova-domain-note.md)
* [`nova.domain_notes_list`](nova-domain-notes-list.md)
