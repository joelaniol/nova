# `nova.explore_surface`

Discovers interactive UI triggers (buttons, tabs, accordions) and activates them to reveal hidden DOM.

---

## 1. Overview

`nova.explore_surface` performs automated single-page surface exploration across four modes: `discover` scans the page for interactive triggers, `activate` clicks or focuses one of them under strict safety guards, `hover` does a read-only hover peek for tooltip/hover content, and `close` ends an exploration run.

* **Core Architecture Guide:** [Surface Explorer](../../../core-features/crawler-and-discovery/surface-explorer/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `mode` | `string` | Yes | — | `discover`, `activate`, `close`, `hover` | Operation mode. 'discover': scan page for interactive triggers. 'activate': click a specific trigger from a prior discover run. 'close': close a run with cleanup. 'hover': read-only hover peek on a trigger (tooltip/hover-content detection). |
| `targetId` | `string` | Yes | `"active"` | — | Target ID from nova.tabs (browser tab ID, sandbox ID, 'active', 'activeBrowserTab'). |
| `agentId` | `string` | No | `"default"` | — | Agent identity for claim authorization. |
| `executionSurface` | `string` | Yes | `"live_tab"` | `live_tab` | Execution surface. Supported value: live_tab. |
| `guardProfile` | `string` | Yes | `"phase1_default"` | `phase1_default` | Guard profile. Supported value: phase1_default. |
| `expectedUrl` | `string` | No | — | — | Optional URL precondition. If set and current URL doesn't match, returns EXPECTED_URL_MISMATCH error. |
| `routeId` | `string` | No | — | — | Optional route ID for site_urls binding. |
| `stability` | `object` | No | — | — | DOM stability gate configuration. |
| `stability.domQuietMs` | `integer` | No | `250` | 100–2000 | DOM quiet window in ms before snapshot. |
| `stability.maxWaitMs` | `integer` | No | `1500` | 250–10000 | Max wait for stability. On timeout: best-effort (warning, not abort). |
| `discover` | `object` | No | — | — | Options for mode='discover'. |
| `discover.persist` | `boolean` | No | `false` | — | If true, persist discover results to crawl.db with an exploration_run. |
| `discover.keepRunOpen` | `boolean` | No | `false` | — | If true (with persist=true), keep the run open for subsequent activate calls. |
| `discover.includeDenied` | `boolean` | No | `true` | — | Include DENY-classified triggers in response. |
| `discover.includeEvidence` | `boolean` | No | `true` | — | Include safety evidence details per trigger. |
| `discover.maxTriggers` | `integer` | No | `40` | 1–200 | Max triggers to return. |
| `discover.returnTextExcerptChars` | `integer` | No | `800` | 0–4000 | Max chars for text excerpts. |
| `discover.userApproved` | `boolean` | No | `false` | — | Set to true after user confirmation when SurfaceExplorerDiscoverPolicy='ask'. First call returns blocked with permissionRequired info. |
| `discover.axEnrich` | `boolean` | No | `false` | — | If true, query CDP Accessibility Tree for computed roles/names on all candidates before pipeline evaluation. Improves heuristic confidence but has performance cost. Capped at 50 elements. |
| `discover.includeOpaqueFrames` | `boolean` | No | `false` | — | If true, list cross-origin iframes as opaque frame blocks (origin, URL, frameId) without discovering inside them. Provides blind-spot transparency. |
| `discover.snapshot` | `object` | No | — | — | Optional snapshot configuration. When snapshot.write=true, creates a frozen baseline bundle (surface screenshot + trigger inventory + manifest) for later diff comparisons. Implies persist=true. |
| `activate` | `object` | No | — | — | Options for mode='activate'. Required fields: runId, sourceStateId, triggerId. |
| `activate.runId` | `string` | Yes | — | — | Run ID from a prior discover(persist=true, keepRunOpen=true) call. |
| `activate.sourceStateId` | `string` | Yes | — | — | State ID where the trigger was discovered. |
| `activate.triggerId` | `string` | Yes | — | — | Trigger ID to activate. Must be phase1Eligible (ALLOW_OPEN_STRONG). phase15Eligible (ALLOW_OPEN_SEMANTIC) is also activatable when SurfaceExplorerSemanticTriggersEnabled=true — always requires activate.userApproved=true. |
| `activate.requestedMethod` | `string` | No | `"auto"` | `auto`, `focus`, `keyboard`, `click` | Activation method. 'auto' tries keyboard then click. |
| `activate.closeRun` | `boolean` | No | `false` | — | If true, close the run after this activation. |
| `activate.returnTextExcerptChars` | `integer` | No | `800` | 0–4000 | Max chars for delta text excerpts. |
| `activate.userApproved` | `boolean` | No | `false` | — | Set to true after user confirmation when activation policy requires approval (always_ask/ask_unknown). First call returns blocked with permissionRequired info, re-send with userApproved=true after approval. |
| `close` | `object` | No | — | — | Options for mode='close'. Explicitly close an exploration run, dispose guard sessions, clear caches, and return a final health summary. Idempotent: closing an already-closed run returns ok with 'already_closed' status. |
| `close.runId` | `string` | Yes | — | — | Run ID to close (from a prior discover with persist=true, keepRunOpen=true). |
| `close.closeReason` | `string` | No | `"agent_done"` | `agent_done`, `task_complete`, `agent_error`, `manual`, `superseded` | Reason for closing the run. Default: 'agent_done'. |
| `hover` | `object` | No | — | — | Options for mode='hover'. Read-only peek: dispatches mouseMoved via CDP, waits for dwell, captures before/after screenshots to detect tooltip/hover content. No click, no keyboard, no state mutation. Result status is 'content_revealed' on visual diff, 'no_change' with reasonCode='NO_VISUAL_DELTA' after a completed comparison, or 'inconclusive' with reasonCode='HOVER_EVIDENCE_UNAVAILABLE' when before/after evidence could not be captured. Required: runId, triggerId, sourceStateId. |
| `hover.runId` | `string` | Yes | — | — | Run ID from a prior discover. |
| `hover.triggerId` | `string` | Yes | — | — | Trigger ID to hover over. |
| `hover.sourceStateId` | `string` | Yes | — | — | State ID where the trigger was discovered. |
| `hover.dwellMs` | `integer` | No | `300` | 100–2000 | How long to hover before capturing after-state (ms). |
| `hover.userApproved` | `boolean` | No | `false` | — | Mandatory approval for hover interaction. |

**`_meta.intent` is required for certain arguments.** Passing a short reason in `_meta.intent` is always safe; a rejected call names the argument that made it required.

Capability bundle: `surface_explorer` (load it with `nova.tools_bundle(bundle='surface_explorer')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.explore_surface",
  "arguments": {
    "targetId": "tab-1",
    "mode": "discover",
    "executionSurface": "live_tab",
    "guardProfile": "phase1_default"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Discovered 8 triggers (5 eligible, 1 denied) on https://example.com/page"
    }
  ],
  "structuredContent": {
    "ok": true,
    "tool": "nova.explore_surface",
    "mode": "discover",
    "tab": { "targetId": "tab-1", "claimAccepted": true },
    "guardProfile": "phase1_default",
    "operation": {
      "status": "discovered",
      "surface": {
        "contentStats": {
          "interactiveTriggerCount": 8,
          "eligibleTriggerCount": 5,
          "deniedTriggerCount": 1
        }
      }
    }
  }
}
```

---

## 4. Operational Best Practices

* **Guard Profile:** `guardProfile` currently only accepts `"phase1_default"`, which classifies triggers before activation and restricts `activate` to triggers the safety pipeline marked eligible — it does not hand an agent free rein to click anything discovered.

---

## 5. Related Tools

* [`nova.coverage_scan`](nova-coverage-scan.md)
* [`nova.dom_extract`](../dom-and-reading/nova-dom-extract.md)
