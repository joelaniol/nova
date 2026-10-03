# `nova.task_instance_reconcile_coverage`

Replays an instance’s observation log against the unit table to propose discovered-to-checked upgrades.

---

## 1. Overview

`nova.task_instance_reconcile_coverage` reconciles recorded page visits and interactions against the Task URL Coverage table, upgrading discovered URLs to checked status.

* **Security Tier:** Tier 2 (Coverage Reconciliation)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `instanceId` | `string` | Yes | — | — | The instance to reconcile. |
| `dryRun` | `boolean` | No | `true` | — | True (default): propose upgrades without persisting. False: apply upgrades — requires developer setting. |
| `observationCutoff` | `string` | No | — | — | Optional ISO timestamp; observations after this point are ignored. Defaults to now. |

Capability bundle: `task_memory` (load it with `nova.tools_bundle(bundle='task_memory')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.task_instance_reconcile_coverage",
  "arguments": {
    "instanceId": "inst-881a"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Coverage reconciled: 4 units upgraded to checked."
    }
  ],
  "structuredContent": {
    "ok": true,
    "instanceId": "inst-881a",
    "upgradedCount": 4,
    "remainingDiscovered": 2
  }
}
```

---

## 4. Operational Best Practices

* **Pre-Completion Step:** Run reconciliation before requesting completion to ensure all visited URLs are marked checked.

---

## 5. Related Tools

* [`nova.coverage_scan`](nova-coverage-scan.md)
* [`nova.task_instance_complete`](nova-task-instance-complete.md)
