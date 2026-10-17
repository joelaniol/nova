# `nova.ocr_stop`

> **Stops a running OCR job and keeps the pages read so far.**

* **Core Feature Guide:** [Offline Optical Character Recognition (OCR)](../../../core-features/media-intelligence/ocr/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with 1.0.0-alpha.21, which is not published yet.

`nova.ocr_stop` ends a job started by [`nova.ocr_read`](nova-ocr-read.md) or [`nova.convert_to_markdown`](nova-convert-to-markdown.md). Recognition stops at once. [`nova.ocr_status`](nova-ocr-status.md) then returns what was read so far as a partial result and names the pages that were not read, so they can be read later with `pages`. A job that has already finished is not touched (`status: "not_running"`).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `jobId` | `string` | Yes | — | — | The jobId nova.ocr_read or nova.convert_to_markdown returned. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ocr_stop",
  "arguments": {
    "jobId": "ocr_3b9d0c7e5a1f42e8b6d0a913"
  }
}
```

### JSON-RPC Response

```json
{
  "structuredContent": {
    "ok": true,
    "jobId": "ocr_3b9d0c7e5a1f42e8b6d0a913",
    "status": "stop_requested",
    "nextAction": "poll_ocr_status_until_terminal"
  }
}
```

---

## 4. Related Tools

* [`nova.ocr_status`](nova-ocr-status.md) to get the pages read before the stop.
* [`nova.ocr_read`](nova-ocr-read.md) to read the remaining pages later.
