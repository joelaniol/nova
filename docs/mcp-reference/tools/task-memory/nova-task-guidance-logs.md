# `nova.task_guidance_logs`

Lists guidance log entries filtered by profile, domain, or guidance kind.

---

## 1. Overview

`nova.task_guidance_logs` lists entries of the guidance log written by `nova.task_guidance_log_add`, filtered by profile, instance, guidance kind or status (`logged`, `proposed`, `accepted`, `rejected`, `promoted`). When `profileId` is set, the result also contains `profileLearningStats` for that profile: instance counts, completion percentage, terminal failures, match telemetry, the most frequent overrides and the confidence tuning signals.

* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/episodic-task-memory-etm/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | No | — | — | Filter by profile ID. When set, also returns profileLearningStats (instance counts, completionPercent as 0..100, terminalFailureCount, weighted avg match score, accepted/total match telemetry, top overrides). Legacy aliases like completionRate and abortedCount remain for compatibility. |
| `instanceId` | `string` | No | — | — | Filter by instance ID. |
| `guidanceKind` | `string` | No | — | — | Filter by kind: style, terminology, scope_rule, workflow, quality, match_telemetry, custom. |
| `status` | `string` | No | — | — | Filter by status: logged, proposed, accepted, rejected, promoted. |
| `limit` | `integer` | No | `50` | 1–200 | Max entries to return. Default: 50. |

Capability bundle: `task_memory` (load it with `nova.tools_bundle(bundle='task_memory')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.task_guidance_logs",
  "arguments": {
    "guidanceKind": "workflow",
    "status": "logged",
    "limit": 5
  }
}
```

### JSON-RPC Response

The text block carries the same object as `structuredContent`, serialized as JSON (shortened here).

```json
{
  "content": [
    {
      "type": "text",
      "text": "{\"logs\":[{\"guidanceLogId\":\"4d7e1a9c2b6f4e0a8c3d5b7f9e1a2c4d\", ...}],\"count\":1,\"profileLearningStats\":null}"
    }
  ],
  "structuredContent": {
    "logs": [
      {
        "guidanceLogId": "4d7e1a9c2b6f4e0a8c3d5b7f9e1a2c4d",
        "profileId": "9b2c4e7a1f3d4c6e8a0b2d4f6a8c0e1f",
        "instanceId": null,
        "normalizedHash": "e3a1f0c47b9d2e6a5c8f1b3d7e9a0c2f4b6d8e1a3c5f7b9d0e2a4c6f8b1d3e5a",
        "guidanceKind": "workflow",
        "payload": {
          "text": "Close the newsletter modal by clicking the backdrop; the close icon does not respond.",
          "url": "https://shop.example.com/checkout"
        },
        "sourceKind": "agent",
        "sourceRef": null,
        "status": "logged",
        "occurrenceCount": 2,
        "createdAtUtc": "2026-10-02T15:41:07.5120000Z",
        "updatedAtUtc": "2026-10-03T09:12:44.0310000Z",
        "promotedToContentRev": null
      }
    ],
    "count": 1,
    "profileLearningStats": null
  }
}
```

---

## 4. Operational Best Practices

* **Review before promoting:** Inspect entries and their `occurrenceCount` before promoting guidance into a profile with `nova.task_promote_guidance`.

---

## 5. Related Tools

* [`nova.task_guidance_log_add`](nova-task-guidance-log-add.md)
* [`nova.task_promotion_candidates`](nova-task-promotion-candidates.md)
