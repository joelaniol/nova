# `nova.task_guidance_log_add`

Logs a guidance observation or proposal without directly mutating task profiles.

---

## 1. Overview

`nova.task_guidance_log_add` records one piece of guidance (style, terminology, scope rule, workflow, quality, match telemetry or custom) in the guidance log. With `profileId` the entry is stored as `logged` for that task profile; without it, it is stored as a `proposed` entry. Identical entries (same profile, kind and payload) are not duplicated: the existing entry's `occurrenceCount` goes up instead. Entries that recur often enough show up in `nova.task_promotion_candidates` and can be promoted into the profile with `nova.task_promote_guidance`.

* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/episodic-task-memory-etm/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | No | — | — | Optional: associate with a profile. When omitted, the entry is stored as a proposal (`status=proposed`) instead of a profile-scoped log. |
| `instanceId` | `string` | No | — | — | Optional: associate with an instance. |
| `guidanceKind` | `string` | Yes | — | — | Kind of guidance. Canonical MCP kinds are style, terminology, scope_rule, workflow, quality, match_telemetry, and custom. match_telemetry is the system telemetry kind used for match acceptance/rejection observations and imports. |
| `payload` | `object` | No | — | — | Structured payload with guidance details. Common fields include text, appliesTo, rationale, notes, telemetry scores, evidenceRefs, and optional observed overrides; additional keys stay allowed for guidance-kind-specific metadata. |
| `payload.text` | `string` | No | — | — | Primary guidance text, recommendation, or learning statement. |
| `payload.appliesTo` | `string` | No | — | — | Optional scope hint such as locale, route, section, or unit kind. |
| `payload.rationale` | `string` | No | — | — | Optional explanation for why this guidance exists. |
| `payload.notes` | `string` | No | — | — | Optional extra note or reviewer comment. |
| `payload.decision` | `string` | No | — | — | Optional decision marker such as accept, reject, prefer, avoid, or escalate. |
| `payload.severity` | `string` | No | — | — | Optional severity or confidence bucket for the observation. |
| `payload.selector` | `string` | No | — | — | Optional DOM selector related to the observation. |
| `payload.url` | `string` | No | — | — | Optional URL or route where the guidance was observed. |
| `payload.matchScore` | `number` | No | — | — | Optional normalized score, commonly used for match telemetry. |
| `payload.accepted` | `boolean` | No | — | — | Optional match/review acceptance flag. |
| `payload.rejected` | `boolean` | No | — | — | Optional explicit rejection flag. |
| `payload.tags` | `array` of `string` | No | — | — | Optional free-form tags for grouping or later promotion review. |
| `payload.evidenceRefs` | `array` of `string` | No | — | — | Optional evidence references such as screenshots, URLs, trace IDs, or note IDs. |
| `payload.overrides` | `object` | No | — | — | Optional override payload observed together with the guidance entry. |
| `sourceKind` | `string` | Yes | — | `user`, `agent`, `reviewer`, `migration`, `system` | Who created this guidance entry. 'user' = direct operator input, 'agent' = autonomous or assistant-generated guidance, 'reviewer' = human review decision, 'migration' = imported historical data, 'system' = runtime-generated guidance or telemetry. |
| `sourceRef` | `string` | No | — | — | Optional reference to the source (e.g. conversation ID, user name). |

Capability bundle: `task_memory` (load it with `nova.tools_bundle(bundle='task_memory')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.task_guidance_log_add",
  "arguments": {
    "profileId": "9b2c4e7a1f3d4c6e8a0b2d4f6a8c0e1f",
    "guidanceKind": "workflow",
    "sourceKind": "agent",
    "payload": {
      "text": "Close the newsletter modal by clicking the backdrop; the close icon does not respond.",
      "url": "https://shop.example.com/checkout"
    }
  }
}
```

### JSON-RPC Response

The text block carries the same object as `structuredContent`, serialized as JSON.

```json
{
  "content": [
    {
      "type": "text",
      "text": "{\"guidanceLogId\":\"4d7e1a9c2b6f4e0a8c3d5b7f9e1a2c4d\",\"normalizedHash\":\"e3a1f0c47b9d2e6a5c8f1b3d7e9a0c2f4b6d8e1a3c5f7b9d0e2a4c6f8b1d3e5a\",\"occurrenceCount\":1,\"status\":\"logged\"}"
    }
  ],
  "structuredContent": {
    "guidanceLogId": "4d7e1a9c2b6f4e0a8c3d5b7f9e1a2c4d",
    "normalizedHash": "e3a1f0c47b9d2e6a5c8f1b3d7e9a0c2f4b6d8e1a3c5f7b9d0e2a4c6f8b1d3e5a",
    "occurrenceCount": 1,
    "status": "logged"
  }
}
```

---

## 4. Operational Best Practices

* **Non-destructive:** Log entries do not change the task profile until they are promoted with `nova.task_promote_guidance`.
* **Repeat instead of rephrasing:** Logging the same payload again raises `occurrenceCount`, which is what promotion looks at; a reworded payload starts a new entry.

---

## 5. Related Tools

* [`nova.task_guidance_logs`](nova-task-guidance-logs.md)
* [`nova.task_promote_guidance`](nova-task-promote-guidance.md)
