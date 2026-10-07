# `nova.task_profiles`

Lists known task profiles, optionally filtered by taskType, domain, or platform.

---

## 1. Overview

`nova.task_profiles` returns an inventory of registered task profiles with summaries of goals and verification criteria.

* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/episodic-task-memory-etm/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `taskType` | `string` | No | — | — | Filter by task type (exact match). |
| `domain` | `string` | No | — | — | Filter by domain (exact match), e.g. 'content_qa', 'web_content'. |
| `platform` | `string` | No | — | — | Filter by platform (exact match), e.g. 'vxmodels', 'chatgpt.com'. |
| `includeArchived` | `boolean` | No | `false` | — | Include archived profiles. Default: false. |
| `limit` | `integer` | No | `100` | 1–500 | Maximum number of profiles to return. Default: 100. |

Capability bundle: `task_memory` (load it with `nova.tools_bundle(bundle='task_memory')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "{\"profiles\":[{\"profileId\":\"tp-support-audit\", ...}],\"count\":1}"
    }
  ],
  "structuredContent": {
    "profiles": [
      {
        "profileId": "tp-support-audit",
        "taskType": "audit",
        "displayName": "Support Portal Link Audit",
        "domain": "support.example.com",
        "platform": null,
        "goal": "Audit all links under /support",
        "confidence": 0.8,
        "contentRev": 2,
        "usageCount": 5,
        "updatedAt": "2026-09-20T12:00:00Z"
      }
    ],
    "count": 1
  }
}
```

There is no separate summary sentence: `content[0].text` is the same structured data serialized as plain JSON text. The response field is `count`, not `total`.

---

## 4. Operational Best Practices

* **Filter by Domain:** Narrow profiles by web domain to find relevant site workflows.

---

## 5. Related Tools

* [`nova.task_search`](nova-task-search.md)
* [`nova.task_match`](nova-task-match.md)
