# `nova.bookmarks_folders_list`

> **Lists all bookmark folders with hierarchical parent-child relationships and depths.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.bookmarks_folders_list` retrieves the bookmark folder tree, returning each folder's id, name, parent id, sort order, creation timestamp, and computed nesting depth.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_bookmarks_folders_list",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Found 4 bookmark folders."
    }
  ],
  "structuredContent": {
    "folders": [
      {
        "id": "f-7c2a1e90",
        "name": "Research",
        "parentId": null,
        "sortOrder": 0,
        "createdUtc": "2026-10-03T12:00:00.0000000Z",
        "depth": 0
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Lookup Before Insertion:** Retrieve folder IDs here before calling `nova.favorites_add` or `nova.favorites_move`.

---

## 5. Related Tools

* [`nova.favorites_list`](nova-favorites-list.md)
* [`nova.bookmarks_folder_create`](nova-bookmarks-folder-create.md)
