# `nova.goal_register`

Manages closed-loop task goals, verifying step advancement and milestone criteria.

---

## 1. Overview

`nova.goal_register` registers, annotates, and tracks multi-step goals. The Nova runtime verifies goal criteria and step advancements against live browser observations.

* **Capability Bundle:** `task_memory`
* **Security Tier:** Tier 2 (Goal Management)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`content`** | `string` | No | `null` | Annotation content (required for annotate). |
| **`eventsLimit`** | `integer` | No | `50` | Maximum events to return when includeEvents=true. |
| **`goalId`** | `string` | No | `null` | Goal identifier for query(close by id), close, annotate. |
| **`includeEvents`** | `boolean` | No | `false` | If true, include event log entries in query responses. |
| **`includeSteps`** | `boolean` | No | `true` | If true (default), include step details in query responses. |
| **`leaseMs`** | `integer` | No | `120000` | Canonical goal lease duration in ms. Goal is auto-aborted if no progress within this window. |
| **`leaseTimeoutMs`** | `integer` | No | `120000` | Legacy alias for leaseMs. Prefer leaseMs for new clients. |
| **`mode`** | `string` | No | `"agent_driven"` | Goal execution mode. 'agent_driven': agent controls each step. 'runtime_assisted': runtime advances steps automatically. 'fully_autonomous': runtime handles entire goal. |
| **`op`** | `string` | Yes | `null` | Goal register operation. 'create' opens a new goal with summary, mode, and optional steps, 'query' reads an existing goal, 'close' writes a terminal goal state, 'annotate' appends free-form notes/events to an existing goal. |
| **`ownerAgent`** | `string` | No | `null` | Legacy alias for ownerAgentId. Prefer ownerAgentId for new clients. |
| **`ownerAgentId`** | `string` | No | `null` | Canonical goal owner identity. When provided it must match the effective agentId of the call. |
| **`ownerSession`** | `string` | No | `null` | Legacy alias for sidecarSessionId. Prefer sidecarSessionId for new clients. |
| **`preconditions`** | `object` | No | `null` | Optional structured goal-level preconditions. These assertions must already hold when the goal is opened and are stored as the durable goal contract. |
| **`preconditionsJson`** | `string` | No | `null` | Legacy fallback: optional JSON string with goal preconditions. Prefer the structured 'preconditions' object for new MCP clients. |
| **`sidecarSessionId`** | `string` | No | `null` | Canonical sidecar session identifier for cross-session goal tracing. Mirrors the X-Nova-Sidecar-Session concept. |
| **`source`** | `string` | No | `"agent"` | Annotation source identifier (default 'agent'). |
| **`state`** | `string` | No | `null` | Final state for close. 'completed' = goal finished successfully, 'failed' = goal ended with an unrecovered failure, 'aborted' = goal was intentionally stopped before completion. |
| **`steps`** | `array` | No | `null` | Optional ordered step plan for create. Maximum 50 steps. Each item describes one runtime-visible goal step; the runtime interprets the list in order and can persist either the structured 'contract' object or the legacy serialized 'contractJson' fallback for that step. |
| **`summary`** | `string` | No | `null` | Goal summary (required for create). |
| **`targetId`** | `string` | No | `null` | Optional target scope for create/query. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.goal_register",
  "arguments": {
    "op": "create",
    "goal": "Complete quarterly compliance audit",
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
      "text": "Registered goal 'goal-881a' with 4 verification milestones."
    }
  ],
  "structuredContent": {
    "ok": true,
    "goalId": "goal-881a",
    "status": "Active",
    "milestonesCount": 4
  }
}
```

---

## 4. Operational Best Practices

* **Milestone Criteria:** Structure complex jobs into discrete, testable milestones rather than open-ended instructions.

---

## 5. Related Tools

* [`nova.task_instance_create`](nova-task-instance-create.md)
* [`nova.task_instance_complete`](nova-task-instance-complete.md)
