# `nova.task_instance_create`

Creates a new episodic task instance from a profile or ad-hoc context with snapshot state.

---

## 1. Overview

`nova.task_instance_create` starts one run of a task. It takes either a stored task profile (`profileId`) or an `adHocContext` for a first run without a profile, applies `currentScope` and `overrides`, and stores the result as the instance's effective context (snapshotted, with a hash). The instance starts with status `pending`. Nova also starts evidence tracking for the active tab; if that is not possible, `evidenceScope` explains why (for example `evidence_scope_target_busy` when another open instance already tracks the tab). With `unitSource`, the instance's URL units for Task URL Coverage are filled from an explicit URL list or from the site URL index.

* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/learning/episodic-task-memory-etm/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | No | — | — | Profile to base the instance on. Omit for ad-hoc first-run. |
| `adHocContext` | `object` | No | — | — | Structured ad-hoc context when no profile exists. Must include taskType, displayName, goal, and a valid completionCondition. |
| `adHocContext.taskType` | `string` | Yes | — | — | Normalized task type identifier for the ad-hoc instance. |
| `adHocContext.displayName` | `string` | Yes | — | — | Human-readable task label for the ad-hoc instance. |
| `adHocContext.domain` | `string` | No | — | — | Optional domain category for the ad-hoc task. |
| `adHocContext.platform` | `string` | No | — | — | Optional platform scope for the ad-hoc task. |
| `adHocContext.goal` | `string` | Yes | — | — | What the ad-hoc task aims to achieve. |
| `adHocContext.stableGuidance` | `array` of `object` | No | — | — | Structured guidance objects carried into the snapshotted effective context. |
| `adHocContext.mandatoryChecks` | `array` of `object` | No | — | — | Mandatory check objects with stable checkIds for later evidence updates. |
| `adHocContext.completionCondition` | `object` | Yes | — | — | Completion condition for the ad-hoc instance. Invalid enum values and missing threshold stopValue are rejected fail-fast. |
| `adHocContext.knownExceptions` | `array` of `object` | No | — | — | Known exception objects carried into the ad-hoc effective context. |
| `targetUrl` | `string` | No | — | — | Optional canonical target URL for this instance. Prefer this top-level field over currentScope.targetUrl. |
| `currentScope` | `object` | No | — | — | Optional structured scope snapshot for the current run. Runtime merges this into effectiveContext.currentScope and also uses it for later match/resume logic. Legacy currentScope.targetUrl is still tolerated as an alias when top-level targetUrl is omitted. |
| `currentScope.route` | `string` | No | — | — | Current route, page path, or logical surface key. |
| `currentScope.pageType` | `string` | No | — | — | Optional page/surface classification such as listing, detail, editor, or settings. |
| `currentScope.locale` | `string` | No | — | — | Single active locale, e.g. de-DE. |
| `currentScope.language` | `string` | No | — | — | Single active language shorthand, e.g. de or en. |
| `currentScope.languages` | `array` of `string` | No | — | — | Multiple active languages when the task spans more than one locale. |
| `currentScope.section` | `string` | No | — | — | Primary content or product section currently in focus. |
| `currentScope.sections` | `array` of `string` | No | — | — | Multiple active sections or scopes. |
| `currentScope.authState` | `string` | No | — | `anonymous`, `logged_in`, `unknown` | Authentication state for the current surface. 'anonymous' = signed out, 'logged_in' = signed in, 'unknown' = not yet classified. |
| `currentScope.unitKind` | `string` | No | — | — | Current dominant work-unit kind, e.g. page, url, selector, file, or item. |
| `currentScope.tags` | `array` of `string` | No | — | — | Free-form scope tags that influence matching or context derivation. |
| `currentScope.entities` | `object` | No | — | — | Named entity map for IDs or semantic anchors relevant to the current task slice. |
| `currentScope.variables` | `object` | No | — | — | Ad-hoc variable map for operator or agent context. |
| `overrides` | `object` | No | — | — | Optional structured overrides applied on top of profile or ad-hoc context before the effective context is snapshotted. Runtime deep-merges objects, supports include/exclude collection patches, uses canonical 'overrides.currentScopePatch' for scope merges, keeps legacy 'overrides.scope' as a compatibility alias, and reserves 'overrides.mandatoryChecks' as invalid. |
| `overrides.currentScopePatch` | `object` | No | — | — | Canonical scope patch merged into currentScope before the effective context is snapshotted. |
| `overrides.scope` | `object` | No | — | — | Legacy alias for currentScopePatch. Merges into currentScope before the effective context is snapshotted. |
| `overrides.stableGuidance` | `object` | No | — | — | Collection patch for stableGuidance arrays. Use include/exclude lists to add or remove entries without replacing the full array. |
| `overrides.knownExceptions` | `object` | No | — | — | Collection patch for knownExceptions arrays. |
| `overrides.tags` | `object` | No | — | — | Collection patch for tag arrays. |
| `overrides.sections` | `object` | No | — | — | Collection patch for section arrays. |
| `overrides.languages` | `object` | No | — | — | Collection patch for language arrays. |
| `overrides.variables` | `object` | No | — | — | Named variable overrides merged into the effective context. |
| `agentId` | `string` | No | — | — | Optional agent identifier for tracking. |
| `declaredTaskKind` | `string` | No | — | `content_audit`, `compliance`, `ui_smoke`, `exploratory`, `accessibility`, `legal`, `security_review`, `route_inventory` | Task URL Coverage hint: agent declares the task kind used for sample-policy resolution. Summary heuristics may tighten, never loosen, this declaration. |
| `unitSource` | `object` | No | — | — | Task URL Coverage population. Pre-fills task_instance_unit rows when URLs are available, computes Reporting groups, and records coverage_schema_version=2 so coverage guidance can reason about this instance. |
| `unitSource.kind` | `string` | Yes | — | `site_urls`, `crawler`, `explicit` | Where the URL list comes from. Use explicit with explicitUrls, or site_urls/crawler with scopeDomain to copy the current persistent crawler Site-URL-Index. |
| `unitSource.scopeDomain` | `string` | No | — | — | Domain or origin anchor for site_urls/crawler lookup. Required when kind is site_urls or crawler. |
| `unitSource.explicitUrls` | `array` of `string` | No | — | — | Required when kind='explicit'. Each URL is normalized via TaskUrlNormalizer before insertion. |
| `unitSource.freezeAfterPopulate` | `boolean` | No | — | — | When true, transitions discoveryState to 'frozen' once units are written. Default: false. |

Capability bundle: `task_memory` (load it with `nova.tools_bundle(bundle='task_memory')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.task_instance_create",
  "arguments": {
    "profileId": "9b2c4e7a1f3d4c6e8a0b2d4f6a8c0e1f",
    "targetUrl": "https://shop.example.com/checkout",
    "declaredTaskKind": "ui_smoke"
  }
}
```

### JSON-RPC Response

The text block carries the same object as `structuredContent`, serialized as JSON. Shortened here: `effectiveContextJson` holds the full snapshotted context and `taskAwareness` the coverage and completion guidance for the instance.

```json
{
  "content": [
    {
      "type": "text",
      "text": "{\"instanceId\":\"c81f2a6e0d4b4f9a9e3c7b1d5a2f8e60\",\"profileId\":\"9b2c4e7a1f3d4c6e8a0b2d4f6a8c0e1f\", ...}"
    }
  ],
  "structuredContent": {
    "instanceId": "c81f2a6e0d4b4f9a9e3c7b1d5a2f8e60",
    "profileId": "9b2c4e7a1f3d4c6e8a0b2d4f6a8c0e1f",
    "profileRevApplied": 3,
    "instanceRev": 0,
    "effectiveContextHash": "5f0c9a2e7b1d4c8a6e3f0b9d2a7c5e1f8b4d6a0c3e9f2b7d1a5c8e4f6b0d3a9c",
    "effectiveContextJson": "{ ... }",
    "status": "pending",
    "discoveryState": "unknown",
    "agentId": null,
    "taskAwareness": { },
    "evidenceScope": null,
    "urlCoverage": null
  }
}
```

`urlCoverage` is filled when `unitSource` was given (`unitsWritten`, `urlsSkipped`, `reportingGroups`, `coverageSchemaVersion`, `persistenceFailed`). Without `profileId` and without `adHocContext` the call is rejected.

---

## 4. Operational Best Practices

* **Profile binding:** Base instances on an existing task profile whenever possible, so stable guidance and mandatory checks carry over.
* **One open instance per tab:** Complete the previous instance on a tab before starting the next, otherwise the new one runs without evidence tracking.

---

## 5. Related Tools

* [`nova.task_instance_get`](nova-task-instance-get.md)
* [`nova.task_instance_progress`](nova-task-instance-progress.md)
