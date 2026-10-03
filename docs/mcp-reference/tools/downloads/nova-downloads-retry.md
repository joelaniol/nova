# `nova.downloads_retry`

Retries a failed download by re-navigating to its original URL.

---

## 1. Overview

`nova.downloads_retry` initiates a fresh download request for a transfer marked `status: "failed"`. Cancelled, active, or completed downloads cannot be retried.

* **Capability Bundle:** `app_shell_recovery`
* **Security Tier:** Tier 2 (Execute)
* **Core Architecture Guide:** [Native Dialogs & Download Prompts](../../../core-features/native-dialogs-and-prompts.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `id` | `string` | Yes | — | — | The download ID to retry (from nova.downloads_list). Must have status 'failed'. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.downloads_retry",
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
      "text": "Download dl-4f8a19bc retry triggered."
    }
  ],
  "structuredContent": {
    "retried": true,
    "id": "dl-4f8a19bc",
    "reason": null
  }
}
```

---

## 4. Operational Best Practices

* **New Entry Created:** A retry operation registers a brand new download entry with its own ID; use `nova.downloads_wait` to monitor the new transfer.
* **Transient Errors Only:** Inspect `retryable: true` in `nova.downloads_list` before retrying (e.g. server timeouts, network drops).

---

## See Also

* [`nova.downloads_list`](nova-downloads-list.md) - Check error reasons and retryable status.
* [`nova.downloads_wait`](nova-downloads-wait.md) - Wait for retried download to finish.
* [Downloads Management Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
