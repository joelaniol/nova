# `nova.image_transform_status`

> **Follows a folder job of nova.image_transform: progress while it runs, the summary once it is done.**

* **Core Feature Guide:** [Local Image Processing](../../../core-features/media-intelligence/image-processing/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with 1.0.0-alpha.21, which is not published yet.

When [`nova.image_transform`](nova-image-transform.md) works on a whole folder and is not finished within its `wait` time, it answers with a `jobId`. `nova.image_transform_status` follows that job.

While it runs, the answer is `status: "running"` with `done`, `failed` and `filesTotal`. Once the job has ended, the answer is the summary: how many copies were written to the output folder, which files failed and why, how many other files were skipped, the size before and after, and how often each kind of metadata was removed.

Pass `wait` to let the call wait up to that many seconds for the job to end. Jobs are kept in memory until Nova closes; the copies already written stay in the output folder either way.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `jobId` | `string` | Yes | — | — | The jobId nova.image_transform returned for a folder, or nova.image_contact_sheet. |
| `wait` | `integer` | No | `0` | 0–540 | Seconds to wait for the job to end before answering. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_image_transform_status",
  "arguments": {
    "jobId": "img_8c41d0e2a97b3f5d16e0c482",
    "wait": 60
  }
}
```

### JSON-RPC Response (finished)

```json
{
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "jobId": "img_8c41d0e2a97b3f5d16e0c482",
    "outputFolder": "C:\\Users\\me\\AppData\\Local\\NovaBrowser\\Exports\\Images\\Urlaub-20261017-201500",
    "filesTotal": 380,
    "written": 379,
    "failed": 1,
    "otherFilesSkipped": 12,
    "bytesBefore": 1593835520,
    "bytesAfter": 1588592640,
    "metadataRemoved": { "gps": 214, "xmp": 97, "artist": 41 },
    "failures": [ { "file": "Strand\\IMG_0412.jpg", "reasonCode": "corrupt_file", "message": "The image could not be decoded." } ]
  }
}
```

---

## 4. Related Tools

* [`nova.image_transform_stop`](nova-image-transform-stop.md) to end a job and keep the copies written so far.
* [`nova.image_transform`](nova-image-transform.md), which starts the job.
