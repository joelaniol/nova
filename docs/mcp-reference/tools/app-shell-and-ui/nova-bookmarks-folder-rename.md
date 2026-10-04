# `nova.bookmarks_folder_rename`

> **Renames an existing bookmark folder.**

* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.bookmarks_folder_rename` changes the display name of an existing bookmark folder. The folder id comes from `nova.bookmarks_folders_list`. An unknown id returns `renamed: false` ("Folder not found.").

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `id` | `string` | Yes | — | — | Folder id. |
| `name` | `string` | Yes | — | — | New folder name (1..64 printable characters). |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_bookmarks_folder_rename",
  "arguments": {
    "id": "3f2a9c1e7b4d4e0f9a6b2c8d1e5f7a90",
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
      "text": "Folder renamed: Competitor Pricing Analysis"
    }
  ],
  "structuredContent": {
    "renamed": true,
    "id": "3f2a9c1e7b4d4e0f9a6b2c8d1e5f7a90",
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
