# `nova.run_rows_stop`

> **Stops a nova.run_rows run; an action already under way finishes first.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with 1.0.0-alpha.21, which is not published yet.

`nova.run_rows_stop` stops a [`nova.run_rows`](nova-run-rows.md) run. No new step starts. A read or wait under way ends at once; an action under way (a click, a submit) finishes first, so it is never cut in half. Then the run is `stopped` and its tab and claim are free again.

A row that was cut off before any action is pending again. A row cut off after an action is `outcome_unknown`. Stopping again, or stopping a run that has ended, changes nothing. Continue later with `nova.run_rows(resumeRunId)`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `runId` | `string` | Yes | — | — | The runId nova.run_rows returned. |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_run_rows_stop",
  "arguments": {
    "runId": "rr_3f9c0a7d21e84b56"
  }
}
```

### JSON-RPC Response

```json
{
  "structuredContent": {
    "runId": "rr_3f9c0a7d21e84b56",
    "state": "stopping",
    "message": "Stop asked: no new step starts; a step under way finishes first. Read nova.run_rows_status(runId, wait) until state is stopped."
  }
}
```

---

## 4. Related Tools

* [`nova.run_rows_status`](nova-run-rows-status.md) to see when the stop has finished.
* [`nova.run_rows`](nova-run-rows.md) to resume the run later.
