# `nova.ocr_status`

> **Reads an OCR job: its progress while it runs, the finished result once it is done.**

* **Core Feature Guide:** [Offline Optical Character Recognition (OCR)](../../../core-features/media-intelligence/ocr/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with 1.0.0-alpha.21, which is not published yet.

Text recognition takes 2 to 12 seconds a page, so [`nova.ocr_read`](nova-ocr-read.md) and [`nova.convert_to_markdown`](nova-convert-to-markdown.md) run it in the background. When their call has waited its `wait` seconds and the document is not finished, they answer with a `jobId`. `nova.ocr_status` follows that job.

While the job runs, the answer is `status: "running"` with `state` (`queued` while another OCR job is running, since only one recognises at a time, otherwise `running`), `pagesRead` and `pagesTotal`. Once the job has ended, the answer is the finished result, exactly as the starting tool returns it: for `nova.convert_to_markdown` the Markdown with the recognised pages, and the written file when one was asked for.

Pass `wait` to let the call wait up to that many seconds for the job to end instead of asking again and again. Jobs are kept in memory until Nova closes; an unknown `jobId` means the call has to be started again.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `jobId` | `string` | Yes | — | — | The jobId nova.ocr_read or nova.convert_to_markdown returned. |
| `wait` | `integer` | No | `0` | 0–540 | Seconds to wait for the job to end before answering. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ocr_status",
  "arguments": {
    "jobId": "ocr_3b9d0c7e5a1f42e8b6d0a913",
    "wait": 60
  }
}
```

### JSON-RPC Response (still running)

```json
{
  "structuredContent": {
    "ok": true,
    "status": "running",
    "jobId": "ocr_3b9d0c7e5a1f42e8b6d0a913",
    "tool": "nova.convert_to_markdown",
    "state": "running",
    "terminal": false,
    "pagesRead": 34,
    "pagesTotal": 80,
    "suggestedPollMs": 5000,
    "nextAction": "poll_ocr_status"
  }
}
```

---

## 4. Related Tools

* [`nova.ocr_stop`](nova-ocr-stop.md) to end a job and keep what was read.
* [`nova.ocr_read`](nova-ocr-read.md) and [`nova.convert_to_markdown`](nova-convert-to-markdown.md), which start the jobs.
