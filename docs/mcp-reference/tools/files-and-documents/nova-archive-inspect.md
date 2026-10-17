# `nova.archive_inspect`

> **Lists what a local ZIP or TAR archive holds, without unpacking it.**

* **Core Feature Guide:** [Archive Inspection & Secure Extraction](../../../core-features/media-intelligence/archives/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with 1.0.0-alpha.21, which is not published yet.

`nova.archive_inspect` looks inside an archive on disk, for example a download from `nova.downloads_list` or a server backup, and lists its entries with their size, plus the totals. ZIP, TAR and gzip-compressed TAR (`.tar.gz`, `.tgz`) are read; for ZIP the answer also has each entry's packed size and compression ratio. Nothing is unpacked and nothing is written.

Each entry also says whether [`nova.archive_extract`](nova-archive-extract.md) would ever write it: entries whose path is absolute or climbs out of the folder (`problem: "unsafe_path"`), symbolic links, hard links and special files such as devices are never extracted. Warnings name such entries, encrypted entries (Nova does not ask for archive passwords) and entries that unpack to more than 100 times their packed size, the typical shape of a zip bomb. Entry names come from whoever made the archive, so the answer is marked as untrusted content.

A compressed TAR has no table of contents, so Nova reads it through. For a very large backup the scan stops after two minutes with `complete: false`; the counts then cover the entries read so far.

RAR, 7z, xz and bzip2 are reported as `archive_inspect.unsupported_format`. Files in Nova's download folder and Exports folder can always be read; any other path needs the setting "Allow local files (file://)".

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `path` | `string` | Yes | — | — | Absolute path to the archive, e.g. the filePath from nova.downloads_list. |
| `maxEntries` | `integer` | No | `100` | 1–1000 | How many entries to list; the counts and totals cover every entry read. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_archive_inspect",
  "arguments": {
    "path": "C:\\Users\\me\\Downloads\\report-files.zip"
  }
}
```

### JSON-RPC Response

```json
{
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "fileName": "report-files.zip",
    "contentTrust": "untrusted_document",
    "entryCount": 3,
    "fileCount": 2,
    "directoryCount": 1,
    "totalSize": 48213,
    "totalCompressedSize": 12077,
    "entries": [
      { "path": "data/", "size": 0, "compressedSize": 0, "ratio": 0, "directory": true, "encrypted": false, "problem": null },
      { "path": "data/summary.csv", "size": 1240, "compressedSize": 512, "ratio": 2.4, "directory": false, "encrypted": false, "problem": null },
      { "path": "report.pdf", "size": 46973, "compressedSize": 11565, "ratio": 4.1, "directory": false, "encrypted": false, "problem": null }
    ],
    "truncated": false,
    "warnings": []
  }
}
```

---

## 4. Related Tools

* [`nova.archive_extract`](nova-archive-extract.md) to unpack the archive or chosen entries.
* [`nova.convert_to_markdown`](nova-convert-to-markdown.md) to read the unpacked documents.
