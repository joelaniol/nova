# `nova.task_match`

Finds the best matching task profiles for a task description with score breakdowns.

---

## 1. Overview

`nova.task_match` evaluates a user prompt or task description against existing task profiles, returning the top candidates with confidence scores and guidance previews.

* **Capability Bundle:** `task_memory`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`currentScope`** | `object` | No | `null` | Optional structured scope used for context and matching query-term enrichment. Common keys include route, locale/languages, section/sections, authState, tags, entities, and variables; additional scope keys are allowed. Legacy currentScope.targetUrl is still tolerated as an alias when top-level targetUrl is omitted. |
| **`domain`** | `string` | No | `null` | Optional: narrow search to a specific domain. |
| **`platform`** | `string` | No | `null` | Optional: platform for matching. If omitted, platform weight is redistributed to other signals. |
| **`targetUrl`** | `string` | No | `null` | Optional canonical target URL for context and matching. Prefer this top-level field over currentScope.targetUrl. |
| **`taskDescription`** | `string` | Yes | `null` | Free-text description of the task to match against known profiles. |
| **`taskType`** | `string` | No | `null` | Optional: narrow search to a specific task type. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.task_match",
  "arguments": {
    "taskDescription": "Audit broken links on the support portal"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Found 1 matching task profile: Support Portal Link Audit (score: 0.94)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "matches": [
      {
        "profileId": "tp-support-audit",
        "displayName": "Support Portal Link Audit",
        "score": 0.94,
        "goal": "Audit all links under /support"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Early Profile Discovery:** Match task descriptions before creating ad-hoc instances to reuse existing completion criteria.

---

## 5. Related Tools

* [`nova.task_search`](nova-task-search.md)
* [`nova.task_profile_get`](nova-task-profile-get.md)
