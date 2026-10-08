# `nova.task_match`

Finds the best matching task profiles for a task description with score breakdowns.

---

## 1. Overview

`nova.task_match` evaluates a user prompt or task description against existing task profiles, returning the top candidates with confidence scores and guidance previews.

* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/learning/episodic-task-memory-etm/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `taskDescription` | `string` | Yes | — | — | Free-text description of the task to match against known profiles. |
| `taskType` | `string` | No | — | — | Optional: narrow search to a specific task type. |
| `domain` | `string` | No | — | — | Optional: narrow search to a specific domain. |
| `platform` | `string` | No | — | — | Optional: platform for matching. If omitted, platform weight is redistributed to other signals. |
| `targetUrl` | `string` | No | — | — | Optional canonical target URL for context and matching. Prefer this top-level field over currentScope.targetUrl. |
| `currentScope` | `object` | No | — | — | Optional structured scope used for context and matching query-term enrichment. Common keys include route, locale/languages, section/sections, authState, tags, entities, and variables; additional scope keys are allowed. Legacy currentScope.targetUrl is still tolerated as an alias when top-level targetUrl is omitted. |
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

Capability bundle: `task_memory` (load it with `nova.tools_bundle(bundle='task_memory')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.task_match",
  "arguments": {
    "taskDescription": "Audit broken links on the support portal"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "{\"matches\":[{\"profileId\":\"tp-support-audit\",\"displayName\":\"Support Portal Link Audit\",\"finalScore\":0.94,\"accepted\":true, ...}], ...}"
    }
  ],
  "structuredContent": {
    "matches": [
      {
        "profileId": "tp-support-audit",
        "displayName": "Support Portal Link Audit",
        "finalScore": 0.94,
        "accepted": true,
        "scoreBreakdown": { "keywordRaw": 0.8, "keywordWeight": 0.45, "tfidfRaw": 0.6 },
        "thresholdUsed": 0.45
      }
    ],
    "bestMatch": { "profileId": "tp-support-audit", "displayName": "Support Portal Link Audit", "finalScore": 0.94, "accepted": true },
    "count": 1,
    "targetUrl": null,
    "currentScope": null,
    "taskAwareness": {
      "source": "profile",
      "profileId": "tp-support-audit",
      "taskType": "audit",
      "displayName": "Support Portal Link Audit",
      "confidence": 0.94,
      "goal": "Audit all links under /support",
      "completionCondition": { "coverageMode": "exploratory", "unitKind": "page", "stopMetric": "checked_units", "stopValue": null },
      "guidanceSummary": "...",
      "mandatoryChecksSummary": "...",
      "knownExceptionsCount": 0
    }
  }
}
```

There is no separate summary sentence: `content[0].text` is the same structured data serialized as plain JSON text. `scoreBreakdown` carries more fields than shown here (platform, domain, and per-field keyword contributions); this example is trimmed.

---

## 4. Operational Best Practices

* **Early Profile Discovery:** Match task descriptions before creating ad-hoc instances to reuse existing completion criteria.

---

## 5. Related Tools

* [`nova.task_search`](nova-task-search.md)
* [`nova.task_profile_get`](nova-task-profile-get.md)
