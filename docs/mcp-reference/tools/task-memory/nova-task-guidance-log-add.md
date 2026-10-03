# `nova.task_guidance_log_add`

Logs a guidance observation or proposal without directly mutating task profiles.

---

## 1. Overview

`nova.task_guidance_log_add` records procedural findings, unexpected DOM drift, or failure workarounds into the guidance audit log. Entries are reviewed for promotion to stable profiles.

* **Security Tier:** Tier 2 (Guidance Logging)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

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
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.task_guidance_log_add",
  "arguments": {
    "guidanceKind": "workaround",
    "sourceKind": "agent_observation",
    "text": "Modal requires clicking backdrop rather than close icon.",
    "taskProfileId": "tp-checkout-01"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Logged guidance observation log-guid-401."
    }
  ],
  "structuredContent": {
    "ok": true,
    "guidanceLogId": "log-guid-401",
    "status": "Logged"
  }
}
```

---

## 4. Operational Best Practices

* **Non-Destructive Learning:** Logs do not alter active profile contracts until reviewed and promoted.

---

## 5. Related Tools

* [`nova.task_guidance_logs`](nova-task-guidance-logs.md)
* [`nova.task_promote_guidance`](nova-task-promote-guidance.md)
