# `nova.downloads_cancel`

Cancels an active in-progress or queued download by ID.

---

## 1. Overview

`nova.downloads_cancel` aborts an ongoing transfer. It works across both native WebView2 downloads and background HttpClient fallbacks, returning status confirmation once the cancellation is registered.

* **Security Tier:** Tier 2 (Control)
* **Core Architecture Guide:** [Native Dialogs & Download Prompts](../../../core-features/native-dialogs-and-prompts.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `id` | `string` | Yes | — | — | The download ID to cancel (from nova.downloads_list). |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.downloads_cancel",
  "arguments": {
    "id": "dl-4f8a19bc"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Download dl-4f8a19bc cancelled."
    }
  ],
  "structuredContent": {
    "cancelled": true,
    "cancelRequested": true,
    "id": "dl-4f8a19bc",
    "status": "cancelled",
    "terminal": true,
    "pollRequired": false,
    "reason": null
  }
}
```

---

## 4. Operational Best Practices

* **Pending vs Terminal:** If `cancelled: false` with `cancelRequested: true` and `reason: "cancel_pending"`, the abort command was sent to WebView2 but final cancellation has not yet settled; poll `nova.downloads_list` if necessary.
* **Failure Discriminants:** Returns `reason: "not_found"` for invalid IDs or `reason: "not_eligible"` if the download has already completed or failed.

---

## See Also

* [`nova.downloads_cancel_all`](nova-downloads-cancel-all.md) - Cancel all active transfers.
* [`nova.downloads_list`](nova-downloads-list.md) - Inspect current transfers.
* [Downloads Management Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
