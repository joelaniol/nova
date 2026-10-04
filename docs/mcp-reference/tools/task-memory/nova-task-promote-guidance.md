# `nova.task_promote_guidance`

Explicitly promotes a guidance log entry into a profile’s stable guidance.

---

## 1. Overview

`nova.task_promote_guidance` promotes an observed workaround or tip from `task_guidance_logs` into the permanent `stableGuidance` of a task profile.

* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `guidanceLogId` | `string` | Yes | — | — | The guidance log entry to promote. |
| `profileId` | `string` | Yes | — | — | The profile to promote the guidance into. |

Capability bundle: `task_memory` (load it with `nova.tools_bundle(bundle='task_memory')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.task_promote_guidance",
  "arguments": {
    "guidanceLogId": "log-guid-401",
    "profileId": "tp-checkout-01"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "{\"ok\":true,\"profileId\":\"tp-checkout-01\",\"guidanceLogId\":\"log-guid-401\",\"promotedToContentRev\":4,\"message\":\"Guidance promoted to profile. Profile contentRev bumped.\"}"
    }
  ],
  "structuredContent": {
    "ok": true,
    "profileId": "tp-checkout-01",
    "guidanceLogId": "log-guid-401",
    "promotedToContentRev": 4,
    "message": "Guidance promoted to profile. Profile contentRev bumped."
  }
}
```

There is no separate summary sentence: `content[0].text` is the same structured data serialized as plain JSON text. Failure responses set `ok: false` with a `reason` of `not_found`, `already_promoted`, `profile_mismatch`, `profile_archived`, or `size_limit`.

---

## 4. Operational Best Practices

* **Reviewed Learning:** Promotes validated hints into the profile's stable guidance for future task instances.

---

## 5. Related Tools

* [`nova.task_promotion_candidates`](nova-task-promotion-candidates.md)
* [`nova.task_guidance_logs`](nova-task-guidance-logs.md)
