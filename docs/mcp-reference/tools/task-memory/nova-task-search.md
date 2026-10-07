# `nova.task_search`

Searches for matching task profiles by free-text query with keyword ranking.

---

## 1. Overview

`nova.task_search` performs text search across profile goals, display names, and guidance hints, returning ranked candidates.

* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/episodic-task-memory-etm/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `query` | `string` | Yes | — | — | Free-text task description in any language. The scorer ranks profiles by relevance. |
| `domain` | `string` | No | — | — | Optional: filter/boost by domain (e.g. 'vxlive.net'). |
| `platform` | `string` | No | — | — | Optional: filter/boost by platform. |
| `taskType` | `string` | No | — | — | Optional: filter by task type. |
| `limit` | `integer` | No | `10` | 1–50 | Max candidates to return (default 10). |

Capability bundle: `task_memory` (load it with `nova.tools_bundle(bundle='task_memory')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.task_search",
  "arguments": {
    "query": "link audit support"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "{\"candidates\":[{\"profileId\":\"tp-support-audit\",\"displayName\":\"Support Portal Link Audit\", ...}], ...}"
    }
  ],
  "structuredContent": {
    "candidates": [
      {
        "profileId": "tp-support-audit",
        "displayName": "Support Portal Link Audit",
        "goal": "Audit all links under /support",
        "taskType": "audit",
        "domain": "support.example.com",
        "score": 0.94,
        "accepted": true,
        "hasGuidance": true,
        "usageCount": 3
      }
    ],
    "count": 1,
    "minScore": 0.3,
    "omittedWeakMatches": 0,
    "hint": "Choose the best matching profile and call task_instance_create(profileId=...). accepted=true means the score clears the match threshold; others are near misses. If none match your task, create a new profile via task_profile_upsert."
  }
}
```

There is no separate summary sentence: `content[0].text` is the same structured data serialized as plain JSON text.

---

## 4. Operational Best Practices

* **Interactive Discovery:** Search existing task templates when given an underspecified prompt.

---

## 5. Related Tools

* [`nova.task_match`](nova-task-match.md)
* [`nova.task_profile_get`](nova-task-profile-get.md)
