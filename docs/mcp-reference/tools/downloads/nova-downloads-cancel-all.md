# `nova.downloads_cancel_all`

Cancels every non-terminal download currently queued, in progress, or paused.

---

## 1. Overview

`nova.downloads_cancel_all` bulk-dispatches abort signals to all pending and active download operations, clearing network queues during emergency stops or workflow resets.

* **Core Architecture Guide:** [Native Dialogs & Download Prompts](../../../core-features/native-dialogs-and-prompts.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.downloads_cancel_all",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Cancel requested: 3 dispatched, 3 cancelled, 0 pending, 0 skipped."
    }
  ],
  "structuredContent": {
    "cancelled": [
      "dl-1",
      "dl-2",
      "dl-3"
    ],
    "cancelRequested": [
      "dl-1",
      "dl-2",
      "dl-3"
    ],
    "pending": [],
    "terminalOther": [],
    "skipped": [],
    "pollRequired": false,
    "statuses": [
      {
        "id": "dl-1",
        "status": "cancelled",
        "terminal": true,
        "reason": null,
        "lastUpdatedUtc": "2026-10-02T20:45:11.0000000Z"
      }
    ]
  }
}
```

`statuses` carries the per-download outcome (one entry per dispatched id; shortened here to one
entry). `pending` and `terminalOther` use the same per-item shape as `statuses` for ids that did not
end up cancelled.

---

## 4. Operational Best Practices

* **Workflow Abort:** Use this tool when an agent task fails early and background downloads are no longer needed, conserving user bandwidth.

---

## See Also

* [`nova.downloads_cancel`](nova-downloads-cancel.md) - Cancel a single download.
* [`nova.downloads_pause_all`](nova-downloads-pause-all.md) - Pause all transfers without cancelling.
* [Downloads Management Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
