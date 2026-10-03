# `nova.downloads_wait`

Blocks until downloads reach a terminal state (completed, failed, or cancelled) and returns disk file paths.

---

## 1. Overview

`nova.downloads_wait` is the missing synchronization join point for download automation. Instead of guessing polling intervals after a download click, agents call `nova.downloads_wait` to deterministically pause execution until the download completes or times out, returning exact disk destinations.

* **Security Tier:** Tier 1 (Safe / Synchronization)
* **Core Architecture Guide:** [Native Dialogs & Download Prompts](../../../core-features/native-dialogs-and-prompts.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `id` | `string` | No | — | — | Optional: wait for exactly this download ID (from nova.downloads_list or a previous nova.downloads_wait). Mutually exclusive with sinceMs. |
| `sinceMs` | `integer` | No | `10000` | 0–600000 | Optional: wait for downloads started within this many milliseconds before the call (0-600000, default 10000). Mutually exclusive with id. |
| `timeoutMs` | `integer` | No | `60000` | 1000–300000 | Maximum time to wait in milliseconds (1000-300000, default 60000). On timeout the current state is returned with status='timeout' — never an error. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.downloads_wait",
  "arguments": {
    "sinceMs": 15000,
    "timeoutMs": 30000
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "1 download(s) settled in 3240 ms (1 completed, 0 failed, 0 cancelled)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "settled",
    "reasonCode": null,
    "settled": true,
    "timedOut": false,
    "waitedMs": 3240,
    "timeoutMs": 30000,
    "matchedCount": 1,
    "completedCount": 1,
    "failedCount": 0,
    "cancelledCount": 0,
    "pendingCount": 0,
    "downloads": [
      {
        "id": "dl-4f8a19bc",
        "fileName": "dataset.csv",
        "url": "https://data.example.com/dataset.csv",
        "status": "completed",
        "filePath": "C:\\Users\\GNetwork\\Downloads\\dataset.csv",
        "bytesReceived": 1450200,
        "totalBytes": 1450200,
        "errorReason": null
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Anchor Window:** When calling right after a button click (e.g. `nova.click_selector`), the default `sinceMs: 10000` catches the newly initiated transfer immediately.
* **Reason Code Inspection:** Inspect `reasonCode` on completion: `all_failed`, `all_cancelled`, or `partial_failure` provide immediate diagnostics without manual array filtering.
* **Never Polling Guesswork:** Always use `nova.downloads_wait` in multi-step workflows like `nova.run_sequence` to ensure subsequent steps operate on real files.

---

## See Also

* [`nova.downloads_list`](nova-downloads-list.md) - List active and historical downloads.
* [`nova.downloads_preview`](nova-downloads-preview.md) - Preview completed file in tab.
* [`nova.downloads_open_folder`](nova-downloads-open-folder.md) - Reveal in Windows Explorer.
* [Downloads Management Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
