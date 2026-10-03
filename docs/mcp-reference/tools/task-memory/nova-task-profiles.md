# `nova.task_profiles`

Lists known task profiles, optionally filtered by taskType, domain, or platform.

---

## 1. Overview

`nova.task_profiles` returns an inventory of registered task profiles with summaries of goals and verification criteria.

* **Capability Bundle:** `task_memory`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`domain`** | `string` | No | `null` | Filter by domain (exact match), e.g. 'content_qa', 'web_content'. |
| **`includeArchived`** | `boolean` | No | `false` | Include archived profiles. Default: false. |
| **`limit`** | `integer` | No | `100` | Maximum number of profiles to return. Default: 100. |
| **`platform`** | `string` | No | `null` | Filter by platform (exact match), e.g. 'vxmodels', 'chatgpt.com'. |
| **`taskType`** | `string` | No | `null` | Filter by task type (exact match). |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.task_profiles",
  "arguments": {
    "domain": "support.example.com"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Loaded 1 task profile for support.example.com."
    }
  ],
  "structuredContent": {
    "ok": true,
    "total": 1,
    "profiles": [
      {
        "profileId": "tp-support-audit",
        "displayName": "Support Portal Link Audit",
        "taskType": "audit"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Filter by Domain:** Narrow profiles by web domain to find relevant site workflows.

---

## 5. Related Tools

* [`nova.task_search`](nova-task-search.md)
* [`nova.task_match`](nova-task-match.md)
