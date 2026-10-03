# `nova.bookmarks_folders_list`

> **Lists all bookmark folders with hierarchical parent-child relationships and depths.**

* **Security Tier:** Tier 1 (Read-Only)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.bookmarks_folders_list` retrieves the bookmark tree structure, returning IDs, labels, parent references, sort orders, and item counts.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
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
    "ok": true,
    "folders": [
      {
        "folderId": "folder-101",
        "name": "Research",
        "parentId": null,
        "depth": 0,
        "itemsCount": 5
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
