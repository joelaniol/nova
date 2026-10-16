# `nova.archive_extract_stop`

> **Stops a running extraction of nova.archive_extract and removes what it had written.**

* **Core Feature Guide:** [Document Conversion](../../../core-features/media-intelligence/document-conversion/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with 1.0.0-alpha.21, which is not published yet.

`nova.archive_extract_stop` stops a job started by [`nova.archive_extract`](nova-archive-extract.md). The extraction ends after the block it is writing and then removes every file and folder it had created, so no half-unpacked folder is left behind. Follow it with [`nova.archive_extract_status`](nova-archive-extract-status.md) until the state is `stopped`. A job that has already finished is not touched (`status: "not_running"`).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `jobId` | `string` | Yes | — | — | The jobId nova.archive_extract returned. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_archive_extract_stop",
  "arguments": {
    "jobId": "ax_5f0c2a9e41b7d3c8a6e29f10"
  }
}
```

### JSON-RPC Response

```json
{
  "structuredContent": {
    "ok": true,
    "jobId": "ax_5f0c2a9e41b7d3c8a6e29f10",
    "status": "stop_requested",
    "nextAction": "poll_archive_extract_status_until_terminal"
  }
}
```

---

## 4. Related Tools

* [`nova.archive_extract_status`](nova-archive-extract-status.md) to see when the stop has finished.
* [`nova.archive_extract`](nova-archive-extract.md) to start again.
