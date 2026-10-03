# `nova.task_profile_upsert`

Creates or updates a task profile with semantic content revision tracking.

---

## 1. Overview

`nova.task_profile_upsert` registers a reusable task template. Bumps `contentRev` on semantic changes, preserving proven operational guidance across runs.

* **Capability Bundle:** `task_memory`
* **Security Tier:** Tier 2 (Profile Mutation)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`completionCondition`** | `object` | No | `null` | Completion condition for this task profile. Invalid enum values and missing threshold stopValue are rejected fail-fast. |
| **`confidence`** | `number` | No | `null` | Profile confidence score 0.0-1.0. Default: 0.5. |
| **`displayName`** | `string` | Yes | `null` | Human-readable display name. |
| **`domain`** | `string` | No | `null` | Optional domain category, e.g. 'content_qa', 'site_audit'. |
| **`expectedContentRev`** | `integer` | No | `null` | Expected contentRev for optimistic concurrency on update. Optional. |
| **`goal`** | `string` | Yes | `null` | What this task type aims to achieve. |
| **`knownExceptions`** | `array` | No | `null` | Known exception rules or caveats that the agent should keep in mind for this task profile. |
| **`mandatoryChecks`** | `array` | No | `null` | Mandatory checks that later progress updates can satisfy, fail, waive, or mark as not applicable. |
| **`platform`** | `string` | No | `null` | Optional platform scope, e.g. 'vxmodels'. Null = platform-agnostic. |
| **`profileId`** | `string` | No | `null` | Profile ID. Omit for create (auto-generated). |
| **`sourceInstanceId`** | `string` | No | `null` | Optional: seed profile content from this instance's effectiveContextJson. |
| **`stableGuidance`** | `array` | No | `null` | Stable guidance entries that should travel with every future instance of this profile. |
| **`taskType`** | `string` | Yes | `null` | Normalized task type identifier, e.g. 'language_quality_review'. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.task_profile_upsert",
  "arguments": {
    "taskType": "audit",
    "displayName": "Support Portal Link Audit",
    "goal": "Audit all links under /support",
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
      "text": "Upserted task profile tp-support-audit (rev: 1)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "profileId": "tp-support-audit",
    "contentRev": 1,
    "status": "Active"
  }
}
```

---

## 4. Operational Best Practices

* **Reusable Task Profiles:** Define profiles for recurring audits and automated checks to standardize completion quality.

---

## 5. Related Tools

* [`nova.task_profile_get`](nova-task-profile-get.md)
* [`nova.task_profiles`](nova-task-profiles.md)
