# `nova.wait_cancel`

Ends a resumable wait that is no longer needed.

> **Upcoming in v1.0.0-alpha.21 - not in a published release yet.** The current setup does not have this tool.

---

## 1. Overview

A wait started with `resumable=true` stays open until it finishes, expires or is cancelled. Each MCP session can hold 16 open waits; `nova.wait_cancel` frees a slot when a workflow is abandoned. It changes nothing on the page or in the downloads.

* `status='cancelled'` - the wait was open and is now ended.
* `status='noop'` with `reasonCode='wait.already_ended'` - the wait had already ended; nothing was cancelled.
* Unknown, foreign or pre-restart ids fail like in [`nova.wait_continue`](nova-wait-continue.md).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `watchId` | `string` | Yes | — | — | The watchId of the wait to end. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.wait_cancel",
  "arguments": { "watchId": "w_3f9c21_0a1b2c3d4e5f" }
}
```

### Result
```json
{
  "ok": true,
  "status": "cancelled",
  "message": "The wait was cancelled; nothing on the page or in the downloads was changed.",
  "watchId": "w_3f9c21_0a1b2c3d4e5f",
  "watchState": "cancelled"
}
```
