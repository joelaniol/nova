# `nova.goal_register`

Manages closed-loop task goals, verifying step advancement and milestone criteria.

---

## 1. Overview

`nova.goal_register` creates, reads, annotates and closes multi-step goals. `op: "create"` opens a goal with a `summary`, an execution `mode` and an optional ordered step plan (up to 50 steps). Goal-level `preconditions` are checked against the target when the goal is opened; if one does not hold, the goal is not created and the result names the failed precondition. A goal holds a lease (`leaseMs`, default 120 000 ms); a goal without progress inside that window is aborted automatically.

* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `op` | `string` | Yes | — | `create`, `query`, `close`, `annotate` | Goal register operation. 'create' opens a new goal with summary, mode, and optional steps, 'query' reads an existing goal, 'close' writes a terminal goal state, 'annotate' appends free-form notes/events to an existing goal. |
| `targetId` | `string` | No | — | — | Optional target scope for create/query. |
| `goalId` | `string` | No | — | — | Goal identifier for query(close by id), close, annotate. |
| `summary` | `string` | No | — | — | Goal summary (required for create). |
| `mode` | `string` | No | `"agent_driven"` | `agent_driven`, `runtime_assisted`, `fully_autonomous` | Goal execution mode. 'agent_driven': agent controls each step. 'runtime_assisted': runtime advances steps automatically. 'fully_autonomous': runtime handles entire goal. |
| `preconditions` | `object` | No | — | — | Optional structured goal-level preconditions. These assertions must already hold when the goal is opened and are stored as the durable goal contract. |
| `preconditionsJson` | `string` | No | — | — | Legacy fallback: optional JSON string with goal preconditions. Prefer the structured 'preconditions' object for new MCP clients. |
| `ownerAgentId` | `string` | No | — | — | Canonical goal owner identity. When provided it must match the effective agentId of the call. |
| `ownerAgent` | `string` | No | — | — | Legacy alias for ownerAgentId. Prefer ownerAgentId for new clients. |
| `sidecarSessionId` | `string` | No | — | — | Canonical sidecar session identifier for cross-session goal tracing. Mirrors the X-Nova-Sidecar-Session concept. |
| `ownerSession` | `string` | No | — | — | Legacy alias for sidecarSessionId. Prefer sidecarSessionId for new clients. |
| `leaseMs` | `integer` | No | `120000` | 1000–600000 | Canonical goal lease duration in ms. Goal is auto-aborted if no progress within this window. |
| `leaseTimeoutMs` | `integer` | No | `120000` | 1000–600000 | Legacy alias for leaseMs. Prefer leaseMs for new clients. |
| `steps` | `array` of `object` | No | — | ≤ 50 items | Optional ordered step plan for create. Maximum 50 steps. Each item describes one runtime-visible goal step; the runtime interprets the list in order and can persist either the structured 'contract' object or the legacy serialized 'contractJson' fallback for that step. |
| `includeSteps` | `boolean` | No | `true` | — | If true (default), include step details in query responses. |
| `includeEvents` | `boolean` | No | `false` | — | If true, include event log entries in query responses. |
| `eventsLimit` | `integer` | No | `50` | 1–200 | Maximum events to return when includeEvents=true. |
| `state` | `string` | No | — | `completed`, `failed`, `aborted` | Final state for close. 'completed' = goal finished successfully, 'failed' = goal ended with an unrecovered failure, 'aborted' = goal was intentionally stopped before completion. |
| `content` | `string` | No | — | — | Annotation content (required for annotate). |
| `source` | `string` | No | `"agent"` | — | Annotation source identifier (default 'agent'). |

Capability bundle: `task_memory` (load it with `nova.tools_bundle(bundle='task_memory')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.goal_register",
  "arguments": {
    "op": "create",
    "summary": "Complete quarterly compliance audit",
    "mode": "agent_driven",
    "targetId": "tab-1"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Goal 'a3f09c1e' created."
    }
  ],
  "structuredContent": {
    "op": "create",
    "ok": true,
    "goal": {
      "goalId": "a3f09c1e",
      "targetId": "tab-1",
      "summary": "Complete quarterly compliance audit",
      "mode": "agent_driven",
      "state": "active",
      "currentStep": 0,
      "ownerAgentId": null,
      "sidecarSessionId": null,
      "leaseMs": 120000,
      "leaseExpiresAtUtc": 1791019320000,
      "heartbeatAtUtc": 1791019200000,
      "contractRevision": 1,
      "createdAtUtc": 1791019200000,
      "updatedAtUtc": 1791019200000
    }
  }
}
```

The `*AtUtc` fields are Unix timestamps in milliseconds. `op: "close"` takes `goalId` and `state` (`completed`, `failed`, `aborted`); `op: "annotate"` takes `goalId` and `content`; `op: "query"` returns the goal with its steps and, with `includeEvents: true`, its event log.

---

## 4. Operational Best Practices

* **Discrete steps:** Split long jobs into an ordered `steps` plan rather than one open-ended summary.
* **Keep the lease alive:** Choose `leaseMs` to fit the slowest step; a goal without progress inside the lease is aborted.

---

## 5. Related Tools

* [`nova.task_instance_create`](nova-task-instance-create.md)
* [`nova.task_instance_complete`](nova-task-instance-complete.md)
