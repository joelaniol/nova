# `nova.task_profile_get`

Retrieves full details of a task profile: guidance, mandatory checks, and completion conditions.

---

## 1. Overview

`nova.task_profile_get` returns the complete specification for a task profile, including stable guidance hints, required verification assertions, and known error workarounds.

* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | The profile ID to retrieve. |

Capability bundle: `task_memory` (load it with `nova.tools_bundle(bundle='task_memory')`).
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
      "text": "Loaded task profile tp-support-audit: Support Portal Link Audit."
    }
  ],
  "structuredContent": {
    "ok": true,
    "profileId": "tp-support-audit",
    "displayName": "Support Portal Link Audit",
    "goal": "Audit all links under /support",
    "mandatoryChecks": [
      "chk-tuc-100"
    ],
    "stableGuidance": [
      "Pagination links use AJAX; wait 300ms"
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Follow Stable Guidance:** Incorporate `stableGuidance` hints directly into your execution strategy.

---

## 5. Related Tools

* [`nova.task_profiles`](nova-task-profiles.md)
* [`nova.task_profile_upsert`](nova-task-profile-upsert.md)
