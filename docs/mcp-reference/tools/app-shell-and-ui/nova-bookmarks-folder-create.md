# `nova.bookmarks_folder_create`

> **Creates a hierarchical folder in the browser bookmark collection.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.bookmarks_folder_create` creates a named container for bookmarks, either at the root level or nested inside an existing parent folder. Folders are capped at 256 total and 5 levels of nesting; a request that would exceed either limit, or that names an invalid parent, is rejected without throwing (`created: false` in the response, not an error).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `name` | `string` | Yes | — | — | Folder name (1..64 printable characters). |
| `parentId` | `string` | No | — | — | Optional parent folder id. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
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
      "text": "Folder created: E-Commerce Research"
    }
  ],
  "structuredContent": {
    "created": true,
    "folder": {
      "id": "f-7c2a1e90",
      "name": "E-Commerce Research",
      "parentId": null,
      "sortOrder": 3,
      "createdUtc": "2026-10-03T12:00:00.0000000Z"
    }
  }
}
```
A rejected request (limit/depth exceeded or invalid parent) returns `{ "created": false, "parentId": ... }` with a text explanation instead of an error.

---

## 4. Operational Best Practices

* **Structured Research:** Organize batch browsing outputs into dedicated session folders.
* **Hierarchy Depth:** Nesting is capped at 5 levels and 256 folders total; avoid excessive nesting for easier retrieval across automation workflows.

---

## 5. Related Tools

* [`nova.bookmarks_folders_list`](nova-bookmarks-folders-list.md)
* [`nova.favorites_add`](nova-favorites-add.md)
