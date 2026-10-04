# `nova.favorites_add`

> **Adds a URL to the browser favorites collection with optional title and target folder.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.favorites_add` persists a URL as a favorite. If `title` is omitted, Nova derives one from the URL itself (the host name, or the full URL if no host can be parsed) — this tool has no open page to read a live page title from.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `url` | `string` | Yes | — | — | Absolute URL (http/https). If scheme is missing, https:// is assumed. |
| `title` | `string` | No | — | — | Optional custom title. |
| `folderId` | `string` | No | — | — | Optional bookmark folder id (see nova.bookmarks_folders_list). New favorites with null/omitted folderId land at root; existing favorites keep their current folder when folderId is null/omitted. Use nova.favorites_move to move to root explicitly. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_favorites_add",
  "arguments": {
    "url": "https://docs.example.com/api",
    "title": "Example API Reference",
    "folderId": "folder-101"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Favorite saved: Example API Reference"
    }
  ],
  "structuredContent": {
    "success": true,
    "favorite": {
      "id": "a1b2c3d4e5f6...",
      "url": "https://docs.example.com/api",
      "title": "Example API Reference",
      "createdUtc": "2026-10-03T12:00:00.0000000Z",
      "folderId": "folder-101",
      "sortOrder": 0
    }
  }
}
```

---

## 4. Operational Best Practices

* **Deduplication is per folder:** A repeated call with the same URL *and* the same `folderId` updates that favorite in place. The same URL added with a different `folderId` creates a separate favorite — favorites are not globally unique by URL, since the same page can be saved into more than one folder.

---

## 5. Related Tools

* [`nova.favorites_list`](nova-favorites-list.md)
* [`nova.favorites_remove`](nova-favorites-remove.md)
* [`nova.favorites_open`](nova-favorites-open.md)
