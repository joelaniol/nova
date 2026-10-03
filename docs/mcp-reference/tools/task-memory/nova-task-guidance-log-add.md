# `nova.task_guidance_log_add`

Logs a guidance observation or proposal without directly mutating task profiles.

---

## 1. Overview

`nova.task_guidance_log_add` records procedural findings, unexpected DOM drift, or failure workarounds into the guidance audit log. Entries are reviewed for promotion to stable profiles.

* **Capability Bundle:** `task_memory`
* **Security Tier:** Tier 2 (Guidance Logging)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`guidanceKind`** | `string` | Yes | `null` | Kind of guidance. Canonical MCP kinds are style, terminology, scope_rule, workflow, quality, match_telemetry, and custom. match_telemetry is the system telemetry kind used for match acceptance/rejection observations and imports. |
| **`instanceId`** | `string` | No | `null` | Optional: associate with an instance. |
| **`payload`** | `object` | No | `null` | Structured payload with guidance details. Common fields include text, appliesTo, rationale, notes, telemetry scores, evidenceRefs, and optional observed overrides; additional keys stay allowed for guidance-kind-specific metadata. |
| **`profileId`** | `string` | No | `null` | Optional: associate with a profile. When omitted, the entry is stored as a proposal (`status=proposed`) instead of a profile-scoped log. |
| **`sourceKind`** | `string` | Yes | `null` | Who created this guidance entry. 'user' = direct operator input, 'agent' = autonomous or assistant-generated guidance, 'reviewer' = human review decision, 'migration' = imported historical data, 'system' = runtime-generated guidance or telemetry. |
| **`sourceRef`** | `string` | No | `null` | Optional reference to the source (e.g. conversation ID, user name). |

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
