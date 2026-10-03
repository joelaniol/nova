# `nova.task_profile_upsert`

Creates or updates a task profile with semantic content revision tracking.

---

## 1. Overview

`nova.task_profile_upsert` registers a reusable task template. Bumps `contentRev` on semantic changes, preserving proven operational guidance across runs.

* **Security Tier:** Tier 2 (Profile Mutation)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | No | — | — | Profile ID. Omit for create (auto-generated). |
| `expectedContentRev` | `integer` | No | — | — | Expected contentRev for optimistic concurrency on update. Optional. |
| `taskType` | `string` | Yes | — | — | Normalized task type identifier, e.g. 'language_quality_review'. |
| `displayName` | `string` | Yes | — | — | Human-readable display name. |
| `domain` | `string` | No | — | — | Optional domain category, e.g. 'content_qa', 'site_audit'. |
| `platform` | `string` | No | — | — | Optional platform scope, e.g. 'vxmodels'. Null = platform-agnostic. |
| `goal` | `string` | Yes | — | — | What this task type aims to achieve. |
| `stableGuidance` | `array` of `object` | No | — | — | Stable guidance entries that should travel with every future instance of this profile. |
| `mandatoryChecks` | `array` of `object` | No | — | — | Mandatory checks that later progress updates can satisfy, fail, waive, or mark as not applicable. |
| `completionCondition` | `object` | No | — | — | Completion condition for this task profile. Invalid enum values and missing threshold stopValue are rejected fail-fast. |
| `completionCondition.coverageMode` | `string` | Yes | — | `exhaustive`, `threshold`, `exploratory` | Coverage evaluation mode. exhaustive requires frozen discovery plus no open/blocked/failed units, threshold completes when stopMetric reaches stopValue, exploratory completes after the minimum sample threshold. |
| `completionCondition.unitKind` | `string` | Yes | — | `page`, `url`, `selector`, `file`, `item`, `state`, `modal`, `role` | Kind of work unit counted by completion. page counts pages, url counts URLs, selector counts DOM selector targets, file counts files, item counts generic list items, state counts captured UI states, modal counts dialog/overlay states, and role counts semantic role targets. |
| `completionCondition.stopMetric` | `string` | Yes | — | `all_units_processed`, `checked_units`, `distinct_findings` | Metric checked against stopValue. all_units_processed requires no remaining units, checked_units counts checked units, distinct_findings counts distinct findings reported during progress. |
| `completionCondition.stopValue` | `integer or null` | No | — | — | Integer threshold used by threshold and optional exploratory modes. Required as an integer when coverageMode is threshold; null is allowed for exhaustive and optional for exploratory. |
| `completionCondition.evidencePolicy` | `object` | No | — | — | Optional server-trusted evidence-gap policy. mode none disables the gate, require_observed counts strong or weak TOB evidence, require_strong counts only strong evidence. maxGapPercent is 0..100. treatUnknownAs controls whether unknown evidence passes or counts as a gap. |
| `knownExceptions` | `array` of `object` | No | — | — | Known exception rules or caveats that the agent should keep in mind for this task profile. |
| `confidence` | `number` | No | — | 0–1 | Profile confidence score 0.0-1.0. Default: 0.5. |
| `sourceInstanceId` | `string` | No | — | — | Optional: seed profile content from this instance's effectiveContextJson. |

Capability bundle: `task_memory` (load it with `nova.tools_bundle(bundle='task_memory')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.task_profile_upsert",
  "arguments": {
    "taskType": "audit",
    "displayName": "Support Portal Link Audit",
    "goal": "Audit all links under /support",
    "domain": "support.example.com"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Upserted task profile tp-support-audit (rev: 1)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "profileId": "tp-support-audit",
    "contentRev": 1,
    "status": "Active"
  }
}
```

---

## 4. Operational Best Practices

* **Reusable Task Profiles:** Define profiles for recurring audits and automated checks to standardize completion quality.

---

## 5. Related Tools

* [`nova.task_profile_get`](nova-task-profile-get.md)
* [`nova.task_profiles`](nova-task-profiles.md)
