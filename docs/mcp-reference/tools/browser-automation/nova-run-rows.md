# `nova.run_rows`

> **Runs the same steps once for every row of a list, in the background on one tab, for minutes to days.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with 1.0.0-alpha.21, which is not published yet.

`nova.run_rows` takes a step template (the same steps as [`nova.run_sequence`](nova-run-sequence.md)) and a list of rows, and runs the steps once per row on a tab the agent has claimed. Typical use: update the price of 136 listings, where each row holds the listing's address and its new price. Inside the step arguments, `{"$row": "price"}` stands for the current row's value.

The run lives in Nova, not in the agent's call: the call waits up to `wait` seconds and then returns the run's state. Follow it with [`nova.run_rows_status`](nova-run-rows-status.md) and stop it with [`nova.run_rows_stop`](nova-run-rows-stop.md). A run that ended blocked, stopped or interrupted continues with `resumeRunId`; Nova keeps its steps and rows.

Every row ends as `ok`, `skipped`, `failed` or `outcome_unknown`:

* `ok` only when the last tool step of the template ran and was ok, so the agent puts its confirmation check last.
* `outcome_unknown` when an action (a click, a submit) went out and nobody saw it end, or the row failed after it. The run stops there, so nothing is repeated before someone looks at the page.
* Nova records every action before it sends it, so even a crash cannot make it forget one.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | — | — | The tab every row runs on; you must have claimed it with nova.tab_claim. On resume: optional, a new tab (also claimed by you) when the old one is gone. |
| `agentId` | `string` | No | `"default"` | — | Your agent identity: the owner of the claim and of the run. Resume needs the same agentId unless takeover is set. |
| `steps` | `array` of `object` | No | — | 1–50 items | The steps run for every row, in order. |
| `defaults` | `object` | No | — | — | Default retry/onError policy for every step, as in nova.run_sequence. |
| `defaults.stepPolicy` | `object` | No | — | — | Default retry policy for steps without their own policy. |
| `defaults.onError` | `object` | No | — | — | Default error handling for every step. |
| `rows` | `array` of `object` | No | — | ≤ 10000 items | The rows, each an object of values (at most 10000 rows, 4 MB). Exactly one of rows and rowsPath. |
| `rowsPath` | `string` | No | — | — | Instead of rows: absolute path to a local .json file with the array of row objects (at most 4 MB); needs the user's 'Allow local files' setting. |
| `rowKey` | `string` | No | — | — | The property that names each row (e.g. 'listingId'); it must be present and unique. Shown as key in the status and usable in onlyRows. |
| `requestKey` | `string` | No | — | — | Your idempotency key: a repeated call with the same key returns the same run; the same key with other steps or rows is refused (rows.request_key_conflict). |
| `startRow` | `integer` | No | `0` | ≥ 0 | New run only: start at this row index; earlier rows are not part of the run. |
| `onlyRows` | `array` of `integer or string` | No | — | — | New run only: run just these rows, by index or rowKey value - e.g. to repeat checked outcome_unknown rows in a new run. |
| `rowDelayMs` | `integer` | No | `0` | 0–3600000 | Pause between two rows (status waiting, rows.row_delay). Counts to the run time, not the row time. |
| `rowJitterMs` | `integer` | No | `0` | 0–3600000 | Up to this many extra milliseconds, random, on each pause. |
| `maxConsecutiveFailures` | `integer or null` | No | `3` | 1–10000 | The run ends blocked after this many failed rows in a row (ok resets the count, skipped leaves it). null turns the brake off. |
| `runTimeoutMs` | `integer` | No | `14400000` | 60000–259200000 | Time for the whole run from this start or resume (default 4 h, at most 72 h); waits and pauses count. When it is over the run ends blocked (rows.run_timeout) and can be resumed. |
| `rowTimeoutMs` | `integer` | No | `120000` | 1000–3600000 | Time for one row (default 120 s); a wait for the user's approval or an account-rule gap does not count. A row over it ends with reason rows.row_timeout and the run goes on. |
| `resumeRunId` | `string` | No | — | — | Continue this blocked, stopped or interrupted run instead of starting one; only its pending rows run, outcome_unknown and partly done rows stay. Takes only targetId, takeover, retryRows and wait. |
| `takeover` | `boolean` | No | `false` | — | Resume only: take over a run another agentId started (e.g. your own earlier session); you become its owner. |
| `retryRows` | `string` | No | — | `no_effect` | Resume only: also run failed rows again whose actions provably never reached a page (effectState none). Rows with an effect or an unclear one never run again by themselves. |
| `wait` | `integer` | No | `25` | 0–600 | Seconds this call waits for the run to end before answering; the run goes on either way. |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_run_rows",
  "arguments": {
    "targetId": "tab-7",
    "agentId": "price-agent",
    "requestKey": "prices-2026-11",
    "rowKey": "id",
    "rows": [
      { "id": "1001", "url": "https://shop.example/edit/1001", "price": "4,50" },
      { "id": "1002", "url": "https://shop.example/edit/1002", "price": "5,00" }
    ],
    "steps": [
      { "tool": "nova.navigate", "args": { "url": { "$row": "url" }, "waitForLoad": true } },
      { "endRow": { "outcome": "skipped", "reason": "locked" }, "when": { "selectorExists": ".locked-notice" } },
      { "tool": "nova.type_selector", "args": { "selector": "#price", "text": { "$row": "price" }, "clear": true } },
      { "tool": "nova.click_selector", "args": { "selector": "button[type=submit]" } },
      { "tool": "nova.wait_for_selector", "args": { "selector": ".saved", "timeoutMs": 30000 } }
    ],
    "wait": 25
  }
}
```

### JSON-RPC Response

```json
{
  "structuredContent": {
    "runId": "rr_3f9c0a7d21e84b56",
    "state": "running",
    "reasonCode": null,
    "rowCount": 2,
    "counts": { "pending": 1, "running": 1, "ok": 0, "skipped": 0, "failed": 0, "outcome_unknown": 0 },
    "currentRow": 1,
    "next": "Running in the background. Follow it with nova.run_rows_status(runId='rr_3f9c0a7d21e84b56', wait=60); stop it with nova.run_rows_stop."
  }
}
```

---

## 4. Operational Best Practices

* **Claim first:** open the tab with `nova.tab_new` and claim it with `nova.tab_claim`. The run keeps the claim alive and holds the tab; other calls on it get `rows.tab_busy` with the run's id.
* **Finished values in the rows:** there are no placeholders inside strings. Put the whole address and the formatted price into each row.
* **Confirmation last:** a row is `ok` only when the last tool step succeeded. Make that step the check that the page accepted the change.
* **Repeat safely:** the same `requestKey` returns the same run instead of starting a second. After checking `outcome_unknown` rows by hand, repeat them in a new run with `onlyRows`.
* **Stop early:** `maxConsecutiveFailures` (default 3) ends the run as blocked after that many failed rows in a row.

---

## 5. Related Tools

* [`nova.run_rows_status`](nova-run-rows-status.md) for progress, counts and the row results.
* [`nova.run_rows_stop`](nova-run-rows-stop.md) to stop a run.
* [`nova.run_sequence`](nova-run-sequence.md) for a few steps once.
