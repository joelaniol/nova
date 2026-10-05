# `nova.favorites_list`

> **Lists all saved browser favorites.**

* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.favorites_list` returns stored favorites with their stable id, URL, title, creation timestamp, folder id and sort order. Favorites with the same URL in different folders appear as separate entries, each with its own id.

Without arguments it lists every favorite in stored order. `folderId` limits the list to one bookmark folder and its subfolders. `query` searches the way the user's favorites search box does: word start before substring before letters in order, title before address before folder name, case and accents ignored, often visited pages first among equal matches, and a favorite the user already picked for this text in the address bar or the favorites search first. Each hit then carries `folderPath`. `maxResults` caps the list; `totalMatches` and `truncated` say whether it was cut.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `query` | `string` | No | — | ≤ 200 characters | Optional search text, e.g. 'cha' for ChatGPT. All words must match. Omit to list favorites in stored order. |
| `folderId` | `string` | No | — | ≤ 200 characters | Optional bookmark folder id (from nova.bookmarks_folders_list). Limits the result to this folder and all its subfolders. Unknown ids are rejected. |
| `maxResults` | `integer` | No | — | 1–500 | Optional cap on returned favorites. Default: all (a query returns at most 500). |

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
