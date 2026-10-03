# `nova.downloads_cancel_all`

Cancels every non-terminal download currently queued, in progress, or paused.

---

## 1. Overview

`nova.downloads_cancel_all` bulk-dispatches abort signals to all pending and active download operations, clearing network queues during emergency stops or workflow resets.

* **Capability Bundle:** `app_shell_recovery`
* **Security Tier:** Tier 2 (Bulk Control)
* **Core Architecture Guide:** [Native Dialogs & Download Prompts](../../../core-features/native-dialogs-and-prompts.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

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
      "text": "cancel requested: 3 dispatched, 0 skipped."
    }
  ],
  "structuredContent": {
    "cancelRequested": [
      "dl-1",
      "dl-2",
      "dl-3"
    ],
    "cancelled": [
      "dl-1",
      "dl-2",
      "dl-3"
    ],
    "pending": [],
    "terminalOther": [],
    "skipped": []
  }
}
```

---

## 4. Operational Best Practices

* **Workflow Abort:** Use this tool when an agent task fails early and background downloads are no longer needed, conserving user bandwidth.

---

## See Also

* [`nova.downloads_cancel`](nova-downloads-cancel.md) - Cancel a single download.
* [`nova.downloads_pause_all`](nova-downloads-pause-all.md) - Pause all transfers without cancelling.
* [Downloads Management Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
