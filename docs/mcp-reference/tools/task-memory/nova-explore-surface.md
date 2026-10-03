# `nova.explore_surface`

Discovers interactive UI triggers (buttons, tabs, accordions) and activates them to reveal hidden DOM.

---

## 1. Overview

`nova.explore_surface` performs automated single-page surface exploration. It detects interactive elements, simulates clicks under strict safety guards, and maps out hidden menus and modals.

* **Capability Bundle:** `task_memory`
* **Security Tier:** Tier 2 (Surface Discovery)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`activate`** | `object` | No | `null` | Options for mode='activate'. Required fields: runId, sourceStateId, triggerId. |
| **`close`** | `object` | No | `null` | Options for mode='close'. Explicitly close an exploration run, dispose guard sessions, clear caches, and return a final health summary. Idempotent: closing an already-closed run returns ok with 'already_closed' status. |
| **`discover`** | `object` | No | `null` | Options for mode='discover'. |
| **`executionSurface`** | `string` | Yes | `"live_tab"` | Execution surface. Supported value: live_tab. |
| **`expectedUrl`** | `string` | No | `null` | Optional URL precondition. If set and current URL doesn't match, returns EXPECTED_URL_MISMATCH error. |
| **`guardProfile`** | `string` | Yes | `"phase1_default"` | Guard profile. Supported value: phase1_default. |
| **`hover`** | `object` | No | `null` | Options for mode='hover'. Read-only peek: dispatches mouseMoved via CDP, waits for dwell, captures before/after screenshots to detect tooltip/hover content. No click, no keyboard, no state mutation. Result status is 'content_revealed' on visual diff, 'no_change' with reasonCode='NO_VISUAL_DELTA' after a completed comparison, or 'inconclusive' with reasonCode='HOVER_EVIDENCE_UNAVAILABLE' when before/after evidence could not be captured. Required: runId, triggerId, sourceStateId. |
| **`mode`** | `string` | Yes | `null` | Operation mode. 'discover': scan page for interactive triggers. 'activate': click a specific trigger from a prior discover run. 'close': close a run with cleanup. 'hover': read-only hover peek on a trigger (tooltip/hover-content detection). |
| **`routeId`** | `string` | No | `null` | Optional route ID for site_urls binding. |
| **`stability`** | `object` | No | `null` | DOM stability gate configuration. |
| **`targetId`** | `string` | Yes | `"active"` | Target ID from nova.tabs (browser tab ID, sandbox ID, 'active', 'activeBrowserTab'). |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.explore_surface",
  "arguments": {
    "targetId": "tab-1",
    "mode": "passive",
    "executionSurface": "tab",
    "guardProfile": "safe"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Explored page surface: discovered 8 interactive triggers (3 expanded)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "triggersDiscovered": 8,
    "elementsExpanded": 3,
    "revealedDomNodes": 45
  }
}
```

---

## 4. Operational Best Practices

* **Safe Guard Profiles:** Use `guardProfile: "safe"` to prevent the explorer from clicking destructive buttons (delete, submit, checkout).

---

## 5. Related Tools

* [`nova.coverage_scan`](nova-coverage-scan.md)
* [`nova.dom_extract`](../dom-and-reading/nova-dom-extract.md)
