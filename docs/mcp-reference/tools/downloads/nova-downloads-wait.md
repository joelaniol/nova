# `nova.downloads_wait`

Blocks until downloads reach a terminal state (completed, failed, or cancelled) and returns disk file paths.

---

## 1. Overview

`nova.downloads_wait` is the missing synchronization join point for download automation. Instead of guessing polling intervals after a download click, agents call `nova.downloads_wait` to deterministically pause execution until the download completes or times out, returning exact disk destinations.

* **Capability Bundle:** `app_shell_recovery`
* **Security Tier:** Tier 1 (Safe / Synchronization)
* **Core Architecture Guide:** [Native Dialogs & Download Prompts](../../../core-features/native-dialogs-and-prompts.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`id`** | `string` | No | `null` | Wait for a specific download ID. Mutually exclusive with `sinceMs`. |
| **`sinceMs`** | `integer` | No | `10000` | Lookback window in ms (0 - 600,000). Catches all downloads started within this window before the call. Mutually exclusive with `id`. |
| **`timeoutMs`** | `integer` | No | `60000` | Maximum wait time in ms (1,000 - 300,000). On timeout, partial state is returned with status='timeout' without throwing an error. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

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
