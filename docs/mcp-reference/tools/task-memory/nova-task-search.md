# `nova.task_search`

Searches for matching task profiles by free-text query with keyword ranking.

---

## 1. Overview

`nova.task_search` performs text search across profile goals, display names, and guidance hints, returning ranked candidates.

* **Capability Bundle:** `task_memory`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`domain`** | `string` | No | `null` | Optional: filter/boost by domain (e.g. 'vxlive.net'). |
| **`limit`** | `integer` | No | `10` | Max candidates to return (default 10). |
| **`platform`** | `string` | No | `null` | Optional: filter/boost by platform. |
| **`query`** | `string` | Yes | `null` | Free-text task description in any language. The scorer ranks profiles by relevance. |
| **`taskType`** | `string` | No | `null` | Optional: filter by task type. |

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
      "text": "Found 1 task profile matching query."
    }
  ],
  "structuredContent": {
    "ok": true,
    "matches": [
      {
        "profileId": "tp-support-audit",
        "displayName": "Support Portal Link Audit",
        "rank": 1
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Interactive Discovery:** Search existing task templates when given an underspecified prompt.

---

## 5. Related Tools

* [`nova.task_match`](nova-task-match.md)
* [`nova.task_profile_get`](nova-task-profile-get.md)
