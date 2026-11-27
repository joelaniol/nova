# `nova.run_rows_status`

> **Reads a nova.run_rows run: state, counts, reasons and one page of row results.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with 1.0.0-alpha.21, which is not published yet.

`nova.run_rows_status` answers how far a [`nova.run_rows`](nova-run-rows.md) run has come and how its rows ended. It returns the run's state and reason, the number of rows per state, the most frequent row reasons, and one page of rows with their outcome. Each row also says what its actions did (`effectState`: `none`, `confirmed` or `unknown`) and, for read steps, what they returned.

Page with `cursor` and `nextCursor`. `rowState` filters, for example `outcome_unknown` for the rows to check on the page, or `pending` for the rows still to come. With `wait`, the call waits until the run changes state or finishes another row. Without `runId`, it lists the runs of the last 7 days. The rows' own input values are never returned.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `runId` | `string` | No | — | — | The runId nova.run_rows returned. Omit to list the runs of the last 7 days. |
| `cursor` | `integer` | No | `0` | ≥ 0 | Start of the page: 0 for the first, then the nextCursor of the previous answer (with the same rowState). |
| `limit` | `integer` | No | `50` | 1–500 | Rows per page. |
| `rowState` | `string` | No | — | `pending`, `running`, `ok`, `skipped`, `failed`, `outcome_unknown` | Only rows in this state. Finished states come in finishing order, pending and running in row order. outcome_unknown lists the rows to check by hand before anything is repeated. |
| `wait` | `integer` | No | `0` | 0–600 | Seconds to wait for the run to change state or finish another row before answering. |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_run_rows_status",
  "arguments": {
    "runId": "rr_3f9c0a7d21e84b56",
    "rowState": "outcome_unknown",
    "limit": 50
  }
}
```

### JSON-RPC Response

```json
{
  "structuredContent": {
    "runId": "rr_3f9c0a7d21e84b56",
    "state": "blocked",
    "reasonCode": "rows.outcome_unknown",
    "counts": { "pending": 40, "running": 0, "ok": 95, "skipped": 1, "failed": 0, "outcome_unknown": 1 },
    "reasons": { "outcome_unknown": [ { "reason": "element.not_found", "count": 1 } ], "skipped": [ { "reason": "locked", "count": 1 } ] },
    "rows": [
      { "i": 96, "key": "1097", "state": "outcome_unknown", "effectState": "unknown", "reason": "element.not_found", "step": 4, "ms": 31840 }
    ],
    "hasMore": false,
    "nextCursor": 97
  }
}
```

---

## 4. Operational Best Practices

* **Wait instead of polling:** pass `wait` (up to 600 seconds) to get the next change without repeated calls.
* **Check unclear rows before repeating:** rows in `outcome_unknown` may already have changed the page. Look at them first, then repeat only what is missing in a new run with `onlyRows`.

---

## 5. Related Tools

* [`nova.run_rows`](nova-run-rows.md) to start or resume a run.
* [`nova.run_rows_stop`](nova-run-rows-stop.md) to stop it.
