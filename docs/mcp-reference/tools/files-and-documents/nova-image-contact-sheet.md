# `nova.image_contact_sheet`

> **Draws every image of a folder as a thumbnail with its name, in one PNG or JPEG or on A4 PDF pages.**

* **Core Feature Guide:** [Local Image Processing](../../../core-features/media-intelligence/image-processing/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with 1.0.0-alpha.21, which is not published yet.

A contact sheet shows what a folder holds at a glance: every picture small, in a grid, with its name under it. Your agent can use it to pick photos with you, check a folder before sorting it, or hand you an overview to print. Everything runs on your computer with Nova's own image engine; the folder is never changed and no file is overwritten.

Nova takes the images in the folder and, unless `recursive` is `false`, in its subfolders, in the order of their paths. Each picture is shown upright, as a photo viewer shows it. An image that cannot be read keeps its place in the grid, crossed out and with its name in red, and the answer names it with the reason.

* **One image** (`png`, the default, or `jpeg`): `columns` sets how many pictures stand in a row (default close to a square, up to 8), `thumbSize` the size of each picture in pixels (default 256). One image holds at most 16,383 pixels per side; a folder too large for that is refused before any work starts, with the advice to use PDF pages, more columns or smaller pictures.
* **A4 PDF pages** (`pdf`): four pictures per row by default, as many rows as fit, and as many pages as needed, numbered at the bottom. The pictures are sharp enough to print.

Under each picture stands its path inside the folder (`labels: "path"`), only the file name (`"name"`) or nothing (`"none"`). Long names are shortened in the middle, so the folder at the start and the number at the end stay readable. A `title` goes on top, on every PDF page.

A large folder takes a while, so the sheet is made as a job. The call waits up to `wait` seconds (default 45). If the sheet is not ready by then, the answer carries a `jobId`: [`nova.image_transform_status`](nova-image-transform-status.md) follows the job, and [`nova.image_transform_stop`](nova-image-transform-stop.md) ends it without writing a sheet.

The sheet goes to `outputPath`, or with a fresh name into Nova's Exports folder. The summary names the file, how many pictures are shown and how many could not be read, the number of pages and the size.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `folder` | `string` | Yes | — | — | Absolute path of the folder whose images go on the sheet. |
| `recursive` | `boolean` | No | `true` | — | Include subfolders. |
| `outputPath` | `string` | No | — | — | Absolute path of the new sheet (.png, .jpg or .pdf, matching format). Default: Exports/Images. |
| `format` | `string` | No | — | `png`, `jpeg`, `pdf` | png (default), jpeg, or pdf for A4 pages. |
| `columns` | `integer` | No | — | 1–12 | Pictures per row; default 4 on PDF, otherwise near-square up to 8. |
| `thumbSize` | `integer` | No | `256` | 64–1024 | PNG/JPEG only: the square box each picture is fitted into, in pixels. |
| `labels` | `string` | No | `"path"` | `path`, `name`, `none` | Under each picture: its path relative to folder, the file name only, or nothing. |
| `title` | `string` | No | — | ≤ 100 characters | Heading on top of the sheet (on every PDF page). |
| `wait` | `integer` | No | `45` | 0–540 | Seconds this call waits for the sheet; the job runs on (nova.image_transform_status). |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova.image_contact_sheet",
  "arguments": {
    "folder": "C:/Workspace/Screenshots",
    "format": "png",
    "columns": 4,
    "thumbSize": 256,
    "labels": "name",
    "title": "Audit Captures"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Contact sheet generated with 12 images: C:/Workspace/Exports/Images/audit_captures_sheet.png"
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "completed",
    "outputPath": "C:/Workspace/Exports/Images/audit_captures_sheet.png",
    "format": "png",
    "imageCount": 12,
    "unreadableCount": 0,
    "columns": 4,
    "dimensions": {
      "width": 1024,
      "height": 768
    }
  }
}
```

---

## 4. Operational Best Practices

* **Dimension Limits on Single Sheets:** For PNG and JPEG exports, the maximum allowable canvas size is 16,383 pixels per dimension. When cataloging folders with hundreds of images, switch to `format: "pdf"` to paginate across printable A4 pages or reduce `thumbSize`.
* **Async Job Tracking:** For very large directory trees, set `wait` to a bounded polling interval. If the generation exceeds `wait` seconds, the call returns a `jobId`. Monitor progress using [`nova.image_transform_status`](nova-image-transform-status.md) rather than issuing redundant creation requests.
* **Label Formatting:** Use `labels: "name"` for shallow folders with distinct file names. Use `labels: "path"` when recursing deep subdirectories to disambiguate identical filenames located in different branches.

---

## 5. Related Tools

* [`nova.image_transform`](nova-image-transform.md) — Transform, resize, and convert individual images or directory batches.
* [`nova.image_info`](nova-image-info.md) — Inspect geometry, orientation, and EXIF metadata of source images.
* [`nova.pdf_compose`](nova-pdf-compose.md) — Merge PDF contact sheets with audit reports and summary documents.
