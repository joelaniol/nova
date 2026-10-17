# `nova.archive_extract`

> **Unpacks a local ZIP or TAR archive of any size, or chosen entries of it, into a new folder - safely, in the background.**

* **Core Feature Guide:** [Archive Inspection & Secure Extraction](../../../core-features/media-intelligence/archives/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with 1.0.0-alpha.21, which is not published yet.

`nova.archive_extract` unpacks a ZIP, TAR or gzip-compressed TAR (`.tar.gz`, `.tgz`) file on disk. Without `destinationDir` the files go into a new folder in Nova's Exports folder, named after the archive and the time; a folder of your own choice needs the setting "Allow local files (file://)" and must be new or empty, so nothing that was there before is ever overwritten. Because the tool writes files, it follows your confirmation setting for saving data permanently in Nova's agent permissions.

Archives of any size are unpacked in the background. The call waits up to `wait` seconds (60 by default) and then returns either the finished result or `state: "running"` with a `jobId`; follow the job with [`nova.archive_extract_status`](nova-archive-extract-status.md) and stop it with [`nova.archive_extract_stop`](nova-archive-extract-stop.md). While it runs, a file named `.nova-extract-in-progress` in the folder shows that the folder is not complete yet.

There is no fixed size limit. Nova counts the bytes that are really unpacked and stops before the destination drive falls below 2 GB of free space (`archive_extract.insufficient_space`); a ZIP that clearly cannot fit is refused before anything is written. You can set your own upper bound with `maxTotalBytes`. A stop, an error or a full drive removes everything the extraction had written.

Entries with an absolute path or a path that climbs out of the folder, symbolic and hard links, devices, encrypted entries, a second entry with the same name, and anything below a folder in the destination that is a link or junction are never written; they are listed in `skipped` with their reason. Use [`nova.archive_inspect`](nova-archive-inspect.md) first to see the entry names, and pass `entries` to unpack only some of them.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `path` | `string` | Yes | — | — | Absolute path to the archive, e.g. the filePath from nova.downloads_list. |
| `destinationDir` | `string` | No | — | — | Absolute folder to unpack into; it must not exist yet or be empty. Needs the user's 'Allow local files' setting. Omit to unpack into a new folder in Nova's Exports folder. |
| `entries` | `array` of `string` | No | — | ≤ 1000 items | Entry paths exactly as nova.archive_inspect lists them; omit to unpack every entry. |
| `maxTotalBytes` | `integer` | No | — | ≥ 1 | Optional upper bound for the unpacked bytes; without it only the free space of the destination drive limits the extraction. |
| `wait` | `integer` | No | `60` | 0–540 | Seconds to wait for the result; the job keeps running afterwards either way. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_archive_extract",
  "arguments": {
    "path": "C:\\Users\\me\\Downloads\\report-files.zip",
    "entries": ["report.pdf"]
  }
}
```

### JSON-RPC Response

```json
{
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "jobId": "ax_5f0c2a9e41b7d3c8a6e29f10",
    "state": "completed",
    "destinationDir": "C:\\Users\\me\\AppData\\Local\\NovaBrowser\\Exports\\Archives\\report-files-20261016-091500",
    "createdDestination": true,
    "extractedCount": 1,
    "directoryCount": 0,
    "totalBytes": 46973,
    "extracted": [
      { "path": "report.pdf", "outputPath": "C:\\Users\\me\\AppData\\Local\\NovaBrowser\\Exports\\Archives\\report-files-20261016-091500\\report.pdf", "size": 46973 }
    ],
    "truncated": false,
    "skipped": [],
    "skippedCount": 0,
    "unknownEntries": []
  }
}
```

---

## 4. Related Tools

* [`nova.archive_inspect`](nova-archive-inspect.md) to list the entries first.
* [`nova.archive_extract_status`](nova-archive-extract-status.md) and [`nova.archive_extract_stop`](nova-archive-extract-stop.md) for a large archive.
* [`nova.convert_to_markdown`](nova-convert-to-markdown.md) to read the unpacked documents.
