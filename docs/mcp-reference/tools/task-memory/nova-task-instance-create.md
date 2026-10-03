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
<!-- /generated:parameters -->

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
