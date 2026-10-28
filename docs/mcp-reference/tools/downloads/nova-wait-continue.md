# `nova.wait_continue`

Continues a wait that a wait tool started with `resumable=true`, keeping everything the wait already knew.

> **Upcoming in v1.0.0-alpha.21 - not in a published release yet.** The current setup does not have this tool.

---

## 1. Overview

A long operation (a large download, a render) does not have to fit into one tool call. Start the wait with `resumable=true` and a short `timeoutMs`; when it runs out while the work is still going, the result carries a `watchId`. `nova.wait_continue(watchId)` resumes exactly that wait: for downloads the window stays anchored at the first call and the downloads it already matched stay covered, so a download that started minutes ago is not lost.

`nova.downloads_wait`, `nova.wait_for_selector`, `nova.wait_for_eval` and `nova.wait_for_modal` support `resumable=true`; `nova.wait_for_selector` also supports `armOnly=true`.

* **Page waits** say how they saw the condition: `observation='current'` means Nova checked the page just now; `observation='latched'` means a recorder on the page caught the moment. A latched match carries `match.observedAt` and `match.evidence` (the element's tag and text) and `currentlySatisfied=null` - it happened then, it may be gone now.
* **Arm before you act:** `nova.wait_for_selector(armOnly=true)` answers `status='armed'` at once. Click or send next, then call `nova.wait_continue(watchId)` - a toast or short error banner that appeared and vanished in between is still reported.
* If the page was replaced while waiting (navigation, reload), the wait ends as `lost` with `reasonCode='wait.document_replaced'`. Check the page directly instead of repeating the action.

* Every answer has the shape of the original tool plus `watchId`, `watchState` (`pending`, `met`, `lost`, `expired`, `cancelled`), `watchTool`, `ageMs`, `activeWaitMs`, `watchExpiresInMs` and, while pending, `nextStep`.
* A pending answer that ran out of time carries `waitExpired=true` and is not a failed call.
* Once a wait has ended, asking again returns the same final answer with `replayed=true` for 10 minutes - useful when an earlier response got lost.
* A wait lives at most 35 minutes and ends as `expired` after 15 minutes without a call.
* The tool only reads. It never repeats the action that started the wait.

Related: [`nova.wait_cancel`](nova-wait-cancel.md), [`nova.downloads_wait`](nova-downloads-wait.md), [`nova.wait_for_selector`](../browser-automation/nova-wait-for-selector.md), [`nova.wait_for_eval`](../dom-and-reading/nova-wait-for-eval.md), [`nova.wait_for_modal`](../browser-automation/nova-wait-for-modal.md).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `watchId` | `string` | Yes | — | — | The watchId from a wait result with resumable=true or armOnly=true. |
| `timeoutMs` | `integer` | No | `30000` | 0–1800000 | How long this call waits, in ms (default 30000). Capped by the watch's remaining lifetime; a downloads watch waits at least 1000 ms per call. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### Start a resumable wait
Call `nova.downloads_wait` with `sinceMs: 15000`, `timeoutMs: 30000` and `resumable: true`. The download is still running after 30 s:
```json
{
  "ok": false,
  "status": "timeout",
  "waitExpired": true,
  "pendingCount": 1,
  "watchId": "w_3f9c21_0a1b2c3d4e5f",
  "watchState": "pending",
  "nextStep": {
    "tool": "nova.wait_continue",
    "args": { "watchId": "w_3f9c21_0a1b2c3d4e5f", "timeoutMs": 30000 }
  }
}
```

### Continue it
```json
{
  "name": "nova.wait_continue",
  "arguments": { "watchId": "w_3f9c21_0a1b2c3d4e5f", "timeoutMs": 30000 }
}
```

When the download has finished:
```json
{
  "ok": true,
  "status": "settled",
  "completedCount": 1,
  "downloads": [ { "id": "dl-7", "status": "completed", "filePath": "C:\\Users\\<user>\\Downloads\\render.mp4" } ],
  "watchState": "met",
  "nextStep": null
}
```

### Errors
`-32602` with `reasonCode`:
* `wait.watch_unknown` - no wait with this id, or it ended more than 10 minutes ago.
* `wait.watch_other_session` - the wait belongs to another MCP session.
* `wait.watch_host_restarted` - the wait was started before Nova restarted. Check the state directly (for downloads: `nova.downloads_list`) instead of repeating the action.

---

## 4. Related Tools

* [`nova.wait_cancel`](nova-wait-cancel.md) — Ends a resumable wait that is no longer needed
* [`nova.downloads_wait`](nova-downloads-wait.md) — Waits deterministically for active downloads
* [`nova.downloads_list`](nova-downloads-list.md) — Lists active and recent downloads
* [`nova.wait_for_selector`](../browser-automation/nova-wait-for-selector.md) — Waits for DOM elements with optional resumable watches
* [`nova.wait_for_eval`](../dom-and-reading/nova-wait-for-eval.md) — Waits for JavaScript expressions with optional resumable watches
