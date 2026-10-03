# `nova.bookmarks_folder_create`

> **Creates a hierarchical folder in the browser bookmark collection.**

* **Security Tier:** Tier 2 (Bookmark Management)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.bookmarks_folder_create` creates a named container for bookmarks, either at the root level or nested inside an existing parent folder.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `name` | `string` | Yes | — | — | Folder name (1..64 printable characters). |
| `parentId` | `string` | No | — | — | Optional parent folder id. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_bookmarks_folder_create",
  "arguments": {
    "name": "E-Commerce Research",
    "parentId": null
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Created folder 'E-Commerce Research' (folder-101)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "folderId": "folder-101",
    "name": "E-Commerce Research",
    "parentId": null
  }
}
```

---

## 4. Operational Best Practices

* **Structured Research:** Organize batch browsing outputs into dedicated session folders.
* **Hierarchy Depth:** Avoid excessive nesting for easier retrieval across automation workflows.

---

## 5. Related Tools

* [`nova.bookmarks_folders_list`](nova-bookmarks-folders-list.md)
* [`nova.favorites_add`](nova-favorites-add.md)
