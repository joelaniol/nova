# `nova.bookmarks_folder_rename`

> **Renames an existing bookmark folder.**

* **Security Tier:** Tier 2 (Bookmark Management)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.bookmarks_folder_rename` updates the human-readable display label of an existing bookmark container.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `id` | `string` | Yes | — | — | Folder id. |
| `name` | `string` | Yes | — | — | New folder name (1..64 printable characters). |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_bookmarks_folder_rename",
  "arguments": {
    "folderId": "folder-101",
    "name": "Competitor Pricing Analysis"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Renamed folder-101 to 'Competitor Pricing Analysis'."
    }
  ],
  "structuredContent": {
    "ok": true,
    "folderId": "folder-101",
    "name": "Competitor Pricing Analysis"
  }
}
```

---

## 4. Operational Best Practices

* **Descriptive Naming:** Maintain clear names indicating workflow purpose or project tags.

---

## 5. Related Tools

* [`nova.bookmarks_folders_list`](nova-bookmarks-folders-list.md)
