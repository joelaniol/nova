# `nova.ui_open_favorites`

> **Opens the favorites panel in the Nova user interface, optionally with a search already typed.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_open_favorites` shows the user the same favorites panel they get from a bookmark bar folder or from "Search favorites..." in the main menu: a search box on top, the favorites below. With `query` the search box is pre-filled and the panel lists the matches, ranked exactly like `nova.favorites_list(query=...)`. With `folderId` the panel opens on that bookmark folder and searches it and its subfolders.

Use it to point the user at something, for example "here are your favorites matching 'invoice'". To read favorites yourself, use `nova.favorites_list`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `query` | `string` | No | — | ≤ 200 characters | Optional text to pre-fill in the panel's search box, e.g. 'cha'. |
| `folderId` | `string` | No | — | ≤ 200 characters | Optional bookmark folder id (from nova.bookmarks_folders_list) the panel opens on. Unknown ids are rejected. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ui_open_favorites",
  "arguments": { "query": "cha" }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Favorites panel opened, searching 'cha'."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "opened",
    "query": "cha",
    "folderId": null
  }
}
```

An unknown `folderId` is rejected with `-32602`; folder ids come from `nova.bookmarks_folders_list`.

---

## 4. Operational Best Practices

* **Show, do not click:** the panel closes as soon as the user clicks elsewhere or opens an entry. Close it yourself with `nova.ui_close_favorites` when you are done showing it.
* **Same ranking as the list:** call `nova.favorites_list` with the same `query` when you need to know which entries the user sees.

---

## 5. Related Tools

* [`nova.ui_close_favorites`](nova-ui-close-favorites.md)
* [`nova.favorites_list`](nova-favorites-list.md)
* [`nova.favorites_open`](nova-favorites-open.md)
