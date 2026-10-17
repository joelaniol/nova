# `nova.archive_extract_status`

> **Reports how far a background extraction of nova.archive_extract has come, or its result.**

* **Core Feature Guide:** [Archive Inspection & Secure Extraction](../../../core-features/media-intelligence/archives/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with 1.0.0-alpha.21, which is not published yet.

`nova.archive_extract_status` reads a job started by [`nova.archive_extract`](nova-archive-extract.md). While the job runs, the answer has `state: "running"` and the progress: bytes and files written so far and the entry being unpacked. When it has finished, the answer is the same result `nova.archive_extract` would have returned; a failure or a stop has its `reasonCode`.

Instead of asking again and again, pass `wait` and the call waits up to that many seconds for the job to end. Jobs are kept while Nova runs; after a restart, a leftover `.nova-extract-in-progress` file in the destination folder means that folder is not complete.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `jobId` | `string` | Yes | — | — | The jobId nova.archive_extract returned. |
| `wait` | `integer` | No | `0` | 0–540 | Seconds to wait for the job to end before answering. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_archive_extract_status",
  "arguments": {
    "jobId": "ax_5f0c2a9e41b7d3c8a6e29f10",
    "wait": 60
  }
}
```

### JSON-RPC Response

```json
{
  "structuredContent": {
    "ok": true,
    "status": "running",
    "jobId": "ax_5f0c2a9e41b7d3c8a6e29f10",
    "state": "running",
    "terminal": false,
    "destinationDir": "C:\\Users\\me\\AppData\\Local\\NovaBrowser\\Exports\\Archives\\server-backup-20261016-091500",
    "progress": { "bytesWritten": 18253611008, "filesWritten": 48211, "currentEntry": "var/lib/mysql/ibdata1" },
    "suggestedPollMs": 5000,
    "nextAction": "poll_archive_extract_status"
  }
}
```

---

## 4. Related Tools

* [`nova.archive_extract`](nova-archive-extract.md) starts the job.
* [`nova.archive_extract_stop`](nova-archive-extract-stop.md) stops it.
