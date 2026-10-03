# `nova.task_instance_create`

Creates a new episodic task instance from a profile or ad-hoc context with snapshot state.

---

## 1. Overview

`nova.task_instance_create` initializes an episodic task instance. It snapshots effective context, anchors mandatory verification checks, and binds the task to a Task URL Coverage tracker.

* **Capability Bundle:** `task_memory`
* **Security Tier:** Tier 2 (Instance Creation)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`adHocContext`** | `object` | No | `null` | Structured ad-hoc context when no profile exists. Must include taskType, displayName, goal, and a valid completionCondition. |
| **`currentScope`** | `object` | No | `null` | Optional structured scope snapshot for the current run. Runtime merges this into effectiveContext.currentScope and also uses it for later match/resume logic. Legacy currentScope.targetUrl is still tolerated as an alias when top-level targetUrl is omitted. |
| **`declaredTaskKind`** | `string` | No | `null` | Task URL Coverage hint: agent declares the task kind used for sample-policy resolution. Summary heuristics may tighten, never loosen, this declaration. |
| **`overrides`** | `object` | No | `null` | Optional structured overrides applied on top of profile or ad-hoc context before the effective context is snapshotted. Runtime deep-merges objects, supports include/exclude collection patches, uses canonical 'overrides.currentScopePatch' for scope merges, keeps legacy 'overrides.scope' as a compatibility alias, and reserves 'overrides.mandatoryChecks' as invalid. |
| **`profileId`** | `string` | No | `null` | Profile to base the instance on. Omit for ad-hoc first-run. |
| **`targetUrl`** | `string` | No | `null` | Optional canonical target URL for this instance. Prefer this top-level field over currentScope.targetUrl. |
| **`unitSource`** | `object` | No | `null` | Task URL Coverage population. Pre-fills task_instance_unit rows when URLs are available, computes Reporting groups, and records coverage_schema_version=2 so coverage guidance can reason about this instance. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.task_instance_create",
  "arguments": {
    "taskProfileId": "tp-checkout-01",
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
      "text": "Created task instance inst-881a for profile tp-checkout-01."
    }
  ],
  "structuredContent": {
    "ok": true,
    "instanceId": "inst-881a",
    "taskProfileId": "tp-checkout-01",
    "status": "InProgress",
    "currentRev": 1
  }
}
```

---

## 4. Operational Best Practices

* **Profile Binding:** Bind instances to existing task profiles whenever possible to inherit proven guidance and mandatory checks.

---

## 5. Related Tools

* [`nova.task_instance_get`](nova-task-instance-get.md)
* [`nova.task_instance_progress`](nova-task-instance-progress.md)
