# `nova.bookmarks_folder_delete`

> **Deletes a bookmark folder and either moves its contents to the root or deletes them with it.**

* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.bookmarks_folder_delete` removes a folder from the bookmark tree. With `mode: "moveToRoot"` (the default), the folder's favorites and subfolders are moved to the top level; with `mode: "deleteContents"`, they are deleted together with the folder. An unknown folder id returns `deleted: false` ("Folder not found.").

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `id` | `string` | Yes | — | — | Folder id. |
| `mode` | `string` | No | `"moveToRoot"` | `moveToRoot`, `deleteContents` | Behavior for the folder's contents. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_bookmarks_folder_delete",
  "arguments": {
    "id": "3f2a9c1e7b4d4e0f9a6b2c8d1e5f7a90",
    "mode": "deleteContents"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Folder deleted with 6 favorite(s) + 2 subfolder(s)."
    }
  ],
  "structuredContent": {
    "deleted": true,
    "id": "3f2a9c1e7b4d4e0f9a6b2c8d1e5f7a90",
    "mode": "deleteContents",
    "movedFavorites": 0,
    "movedSubfolders": 0,
    "deletedFavorites": 6,
    "deletedSubfolders": 2
  }
}
```

---

## 4. Operational Best Practices

* **Choose the mode deliberately:** Omit `mode` (or pass `moveToRoot`) to keep the favorites; `deleteContents` removes them as well.
* **Verify Contents:** Run `nova.bookmarks_folders_list` beforehand to confirm the target folder id.

---

## 5. Related Tools

* [`nova.bookmarks_folder_create`](nova-bookmarks-folder-create.md)
* [`nova.bookmarks_folders_list`](nova-bookmarks-folders-list.md)
