# `nova.downloads_list`

Lists recent downloads tracked by the browser with status, progress, speed, and error categorization.

---

## 1. Overview

`nova.downloads_list` inspects download history and live in-progress transfers across all sandboxes. It reports detailed telemetry including byte counts, transfer rates, estimated remaining time, network/disk error categories, and live operation capabilities (`canPause`, `canResume`).

* **Core Architecture Guide:** [Native Dialogs & Download Prompts](../../../core-features/native-dialogs-and-prompts.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `id` | `string` | No | — | — | Optional: fetch a single download by ID (exact match). Useful for monitoring a specific download. |
| `status` | `string` | No | — | `queued`, `in_progress`, `paused`, `completed`, `cancelled`, `failed` | Optional: filter by status. |
| `limit` | `integer` | No | — | — | Optional: max number of results (1-1000, default: all loaded). |
| `offset` | `integer` | No | — | — | Optional: skip N entries (default: 0). Combine with limit for pagination. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
        "errorCategory": null,
        "retryable": false,
        "canPause": true,
        "canResume": false,
        "status": "in_progress",
        "bytesReceived": 45088768,
        "totalBytes": 104857600,
        "filePath": "C:\\Users\\GNetwork\\Downloads\\release-v2.4.0.zip",
        "sandboxId": "A",
        "startedUtc": "2026-10-02T20:45:10.0000000Z",
        "speedBytesPerSecond": 5242880,
        "stalled": false,
        "estimatedSecondsRemaining": 11.4,
        "completedUtc": null,
        "errorReason": null,
        "lastUpdatedUtc": "2026-10-02T20:45:21.0000000Z",
        "elapsedSeconds": 11.0
      }
    ],
    "idNotFound": null,
    "proxy": {
      "mode": "global",
      "browserDownloads": "no proxy configured (Windows default route)",
      "novaDownloads": "no proxy configured (Windows default route)",
      "direct": false
    }
  }
}
```

The `downloads` array shows one entry with every field the handler returns; `proxy` describes which
route Nova's own downloads take versus the browser's own downloads (see the proxy-and-network tools
for configuring one). `direct: true` only appears when the download proxy mode is explicitly set to
off.

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
