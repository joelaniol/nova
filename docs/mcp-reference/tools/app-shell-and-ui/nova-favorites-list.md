# `nova.favorites_list`

> **Lists all saved browser favorites.**

* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.favorites_list` returns every stored favorite with its stable id, URL, title, creation timestamp, folder id and sort order. Favorites with the same URL in different folders appear as separate entries, each with its own id. The tool takes no filter; filter by `folderId` on the client side (`null` = top level).

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
  "name": "nova_favorites_list",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "1 favorite(s)."
    }
  ],
  "structuredContent": {
    "favorites": [
      {
        "id": "8d0c4b6e2f1a4c7e9b3d5a1f6e2c8b40",
        "url": "https://docs.example.com/api",
        "title": "Example API",
        "createdUtc": "2026-09-14T08:12:45.0000000Z",
        "folderId": "3f2a9c1e7b4d4e0f9a6b2c8d1e5f7a90",
        "sortOrder": 0
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Use the id for follow-up calls:** `nova.favorites_move` and `nova.favorites_remove` accept the `id` from this list and then target exactly one entry, even when the same URL is saved more than once.
* **Folder names:** Resolve `folderId` to a name with `nova.bookmarks_folders_list`.

---

## 5. Related Tools

* [`nova.favorites_add`](nova-favorites-add.md)
* [`nova.favorites_open`](nova-favorites-open.md)
