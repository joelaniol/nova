# `nova.image_transform_stop`

> **Stops a folder job of nova.image_transform and keeps every copy already written.**

* **Core Feature Guide:** [Local Image Processing](../../../core-features/media-intelligence/image-processing/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with 1.0.0-alpha.21, which is not published yet.

`nova.image_transform_stop` ends a folder job of [`nova.image_transform`](nova-image-transform.md). The images being processed at that moment are dropped; every copy already written stays complete in the output folder. [`nova.image_transform_status`](nova-image-transform-status.md) then returns the summary with `status: "stopped"` and `notReached` for the images that were not processed. A job that has already finished is not touched (`status: "not_running"`).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `jobId` | `string` | Yes | — | — | The jobId nova.image_transform returned for a folder, or nova.image_contact_sheet. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_image_transform_stop",
  "arguments": {
    "jobId": "img_8c41d0e2a97b3f5d16e0c482"
  }
}
```

### JSON-RPC Response

```json
{
  "structuredContent": {
    "ok": true,
    "jobId": "img_8c41d0e2a97b3f5d16e0c482",
    "status": "stop_requested",
    "nextAction": "poll_image_transform_status_until_terminal"
  }
}
```

---

## 4. Related Tools

* [`nova.image_transform_status`](nova-image-transform-status.md) for the summary after the stop.
* [`nova.image_transform`](nova-image-transform.md) to start again.
