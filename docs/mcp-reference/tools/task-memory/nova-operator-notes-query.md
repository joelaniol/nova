# `nova.operator_notes_query`

Queries operator notes by keywords with tag-intersection and TF-IDF relevance scoring.

---

## 1. Overview

`nova.operator_notes_query` performs scored text retrieval across operator notes, factoring in temporal decay and keyword relevance.

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
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
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
      "text": "1 matching note(s) (scope=current_sandbox)."
    }
  ],
  "structuredContent": {
    "scope": "current_sandbox",
    "resolvedSandboxRef": null,
    "notes": [
      {
        "id": "a3f1c9e2b4d6487f9a21e0d4f1a2b3c4",
        "content": "Never delete test databases on staging",
        "tags": ["staging", "safety"],
        "category": null,
        "source": "agent",
        "score": 0.92,
        "scoreBreakdown": {
          "tagScore": 1.0,
          "contentScore": 0.84,
          "decayFactor": 0.97
        },
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

* **Targeted Querying:** Query keywords matching current task nouns and verbs.

---

## 5. Related Tools

* [`nova.operator_notes_list`](nova-operator-notes-list.md)
* [`nova.domain_notes_list`](nova-domain-notes-list.md)
