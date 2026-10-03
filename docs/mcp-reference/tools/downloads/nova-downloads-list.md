# `nova.downloads_list`

Lists recent downloads tracked by the browser with status, progress, speed, and error categorization.

---

## 1. Overview

`nova.downloads_list` inspects download history and live in-progress transfers across all sandboxes. It reports detailed telemetry including byte counts, transfer rates, estimated remaining time, network/disk error categories, and live operation capabilities (`canPause`, `canResume`).

* **Capability Bundle:** `app_shell_recovery`
* **Security Tier:** Tier 1 (Safe)
* **Core Architecture Guide:** [Native Dialogs & Download Prompts](../../../core-features/native-dialogs-and-prompts.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`id`** | `string` | No | `null` | Optional: fetch a single download by exact ID. |
| **`status`** | `string` | No | `null` | Optional status filter: `"queued"`, `"in_progress"`, `"paused"`, `"completed"`, `"cancelled"`, `"failed"`. |
| **`limit`** | `integer` | No | `all` | Max number of results (1 - 1000). |
| **`offset`** | `integer` | No | `0` | Number of entries to skip for pagination. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.downloads_list",
  "arguments": {
    "status": "in_progress",
    "limit": 10
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "1 result(s) of 12 download(s), 1 active."
    }
  ],
  "structuredContent": {
    "totalCount": 12,
    "activeCount": 1,
    "filtered": true,
    "downloads": [
      {
        "id": "dl-4f8a19bc",
        "fileName": "release-v2.4.0.zip",
        "url": "https://releases.example.com/builds/release-v2.4.0.zip",
        "status": "in_progress",
        "bytesReceived": 45088768,
        "totalBytes": 104857600,
        "speedBytesPerSecond": 5242880,
        "stalled": false,
        "estimatedSecondsRemaining": 11.4,
        "canPause": true,
        "canResume": false,
        "filePath": "C:\\Users\\GNetwork\\Downloads\\release-v2.4.0.zip",
        "sandboxId": "A",
        "startedUtc": "2026-10-02T20:45:10.0000000Z",
        "errorCategory": null,
        "retryable": false
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Deterministic Automation:** Rather than polling `nova.downloads_list` in a loop after triggering a download, use `nova.downloads_wait` to block deterministically until files land on disk.
* **Error Categories:** Inspect `errorCategory` (`network`, `disk`, `permission`, `server`, `cancelled`, `app_restart`) to determine recovery steps.
* **Retryable Signal:** Check `retryable: true` before attempting `nova.downloads_retry`.

---

## See Also

* [`nova.downloads_wait`](nova-downloads-wait.md) - Block until downloads reach terminal state.
* [`nova.downloads_pause`](nova-downloads-pause.md) - Pause active transfer.
* [`nova.downloads_open_file`](nova-downloads-open-file.md) - Open completed file.
* [Downloads Management Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
