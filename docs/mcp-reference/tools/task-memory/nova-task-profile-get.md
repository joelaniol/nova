# `nova.task_profile_get`

Retrieves full details of a task profile: guidance, mandatory checks, and completion conditions.

---

## 1. Overview

`nova.task_profile_get` returns the complete specification for a task profile, including stable guidance hints, required verification assertions, and known error workarounds.

* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/learning/episodic-task-memory-etm/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | The profile ID to retrieve. |

Capability bundle: `task_memory` (load it with `nova.tools_bundle(bundle='task_memory')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.task_profile_get",
  "arguments": {
    "profileId": "tp-support-audit"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "{\"ok\":true,\"profileId\":\"tp-support-audit\", ...}"
    }
  ],
  "structuredContent": {
    "ok": true,
    "profileId": "tp-support-audit",
    "taskType": "audit",
    "displayName": "Support Portal Link Audit",
    "domain": "support.example.com",
    "platform": null,
    "goal": "Audit all links under /support",
    "stableGuidance": [
      { "guidanceId": "g1", "kind": "workflow", "text": "Pagination links use AJAX; wait 300ms" }
    ],
    "mandatoryChecks": [
      { "checkId": "chk-tuc-100", "description": "All support links return 200", "kind": "completeness", "required": true }
    ],
    "completionCondition": { "coverageMode": "exploratory", "unitKind": "page", "stopMetric": "checked_units", "stopValue": null },
    "knownExceptions": [],
    "confidence": 0.8,
    "contentRev": 2,
    "usageCount": 5,
    "createdAtUtc": "2026-09-01T10:00:00Z",
    "updatedAtUtc": "2026-09-20T12:00:00Z",
    "confidenceTuning": { "currentConfidence": 0.8, "projectedConfidence": 0.82 }
  }
}
```

If `profileId` is unknown, the call does not error — it returns `{ "ok": false, "reason": "not_found", "profileId": "..." }` with the text "Profile not found." On success there is no separate summary sentence: `content[0].text` is the same structured data serialized as plain JSON text, and `mandatoryChecks`/`stableGuidance` are objects, not plain strings. `confidenceTuning` carries more signal fields than shown here.

---

## 4. Operational Best Practices

* **Follow Stable Guidance:** Incorporate `stableGuidance` hints directly into your execution strategy.

---

## 5. Related Tools

* [`nova.task_profiles`](nova-task-profiles.md)
* [`nova.task_profile_upsert`](nova-task-profile-upsert.md)
