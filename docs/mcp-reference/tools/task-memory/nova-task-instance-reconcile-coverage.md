# `nova.task_instance_reconcile_coverage`

Replays an instance’s observation log against the unit table to propose discovered-to-checked upgrades.

---

## 1. Overview

`nova.task_instance_reconcile_coverage` replays recorded observations against the Task URL Coverage table and proposes discovered-to-checked upgrades. By default (`dryRun=true`) it only proposes; applying the upgrades (`dryRun=false`) is gated behind a developer setting. Reconcile runs are rate-limited: at most 3 dry runs and 1 apply run per instance per hour.

* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/episodic-task-memory-etm/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `instanceId` | `string` | Yes | — | — | The instance to reconcile. |
| `dryRun` | `boolean` | No | `true` | — | True (default): propose upgrades without persisting. False: apply upgrades — requires developer setting. |
| `observationCutoff` | `string` | No | — | — | Optional ISO timestamp; observations after this point are ignored. Defaults to now. |

Capability bundle: `task_memory` (load it with `nova.tools_bundle(bundle='task_memory')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
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
      "text": "Reconcile (dryRun): 2 upgrades over 5 observations."
    }
  ],
  "structuredContent": {
    "instanceId": "inst-881a",
    "dryRun": true,
    "runId": "reconcile:inst-881a:a3f1c9e2b4d6487f9a21e0d4f1a2b3c4",
    "result": "ok",
    "ruleVersion": 1,
    "normalizerVersion": 1,
    "observationsConsidered": 5,
    "proposedUpgrades": [
      {
        "unitKey": "url:/checkout/confirm",
        "oldStatus": "discovered",
        "newStatus": "checked",
        "observationId": "obs-0042",
        "evidenceKind": "navigation",
        "eligibilityRule": "visited"
      }
    ],
    "historyCompleteness": 1.0
  }
}
```

When there are no new observations since the previous run, `result` is `no_new_evidence` instead, with `lastRunAt`/`lastObservationId` and no `proposedUpgrades`. With `dryRun=true` the upgrades listed in `proposedUpgrades` are not persisted — call again with `dryRun=false` (developer-gated) to apply them.

---

## 4. Operational Best Practices

* **Pre-Completion Step:** Run reconciliation before requesting completion to ensure all visited URLs are marked checked.

---

## 5. Related Tools

* [`nova.coverage_scan`](nova-coverage-scan.md)
* [`nova.task_instance_complete`](nova-task-instance-complete.md)
