# `nova.bookmarks_folder_delete`

> **Deletes a bookmark folder and optionally its contained bookmarks and subfolders.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 2 (Destructive Bookmark Management)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.bookmarks_folder_delete` removes a folder from the bookmark tree. If recursive is true, all descendants are purged.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `id` | `string` | Yes | — | — | Folder id. |
| `mode` | `string` | No | `"moveToRoot"` | `moveToRoot`, `deleteContents` | Behavior for the folder's contents. |
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_bookmarks_folder_delete",
  "arguments": {
    "folderId": "folder-101",
    "recursive": true
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Folder 'folder-101' and contents deleted."
    }
  ],
  "structuredContent": {
    "ok": true,
    "folderId": "folder-101",
    "deletedCount": 8
  }
}
```

---

## 4. Operational Best Practices

* **Recursive Caution:** Set `recursive: true` deliberately to prevent orphan bookmark generation.
* **Verify Contents:** Run `nova.bookmarks_folders_list` beforehand to confirm the target folder ID.

---

## 5. Related Tools

* [`nova.bookmarks_folder_create`](nova-bookmarks-folder-create.md)
* [`nova.bookmarks_folders_list`](nova-bookmarks-folders-list.md)
