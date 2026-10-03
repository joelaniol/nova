# `nova.operator_notes_query`

Queries operator notes by keywords with tag-intersection and TF-IDF relevance scoring.

---

## 1. Overview

`nova.operator_notes_query` performs scored text retrieval across operator notes, factoring in temporal decay and keyword relevance.

* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `keywords` | `array` of `string` | Yes | — | — | Keywords to match against note tags. |
| `minScore` | `number` | No | `0.3` | 0–1 | Minimum match score (0.0-1.0). Default: 0.3. |
| `limit` | `integer` | No | `10` | 1–50 | Maximum results. Default: 10. |
| `scope` | `string` | No | `"current_sandbox"` | `current_sandbox`, `global`, `all`, `orphaned` | Filter scope: 'current_sandbox' (default) = active sandbox + global; 'global' = only global notes; 'all' = no filter; 'orphaned' = notes anchored to deleted sandboxes (cleanup view). |
| `sandboxId` | `string` | No | — | — | Optional explicit sandbox letter-id to override the active-target resolution. Requires sandboxRef. |
| `sandboxRef` | `string` | No | — | — | Opaque PersistentUid token from nova.tabs / nova.sandbox_context. Mandatory when sandboxId is set. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.operator_notes_query",
  "arguments": {
    "keywords": [
      "staging",
      "database"
    ]
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Found 1 matching operator note."
    }
  ],
  "structuredContent": {
    "ok": true,
    "matchesCount": 1,
    "notes": [
      {
        "id": "op-note-101",
        "content": "Never delete test databases on staging",
        "score": 0.92
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Targeted Querying:** Query keywords matching current task nouns and verbs.

---

## 5. Related Tools

* [`nova.operator_notes_list`](nova-operator-notes-list.md)
* [`nova.domain_notes_list`](nova-domain-notes-list.md)
