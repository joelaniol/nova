# `nova.favorites_remove`

> **Removes a bookmark favorite by its unique identifier.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 2 (Bookmark Management)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.favorites_remove` permanently deletes a bookmark from the browser database.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `id` | `string` | No | — | — | Stable favorite id (from nova.favorites_list). Targets exactly one entry. Preferred over url. |
| `url` | `string` | No | — | — | URL to remove (first match). Used when id is omitted. |
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_favorites_remove",
  "arguments": {
    "favoriteId": "fav-5501"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Removed favorite fav-5501."
    }
  ],
  "structuredContent": {
    "ok": true,
    "favoriteId": "fav-5501"
  }
}
```

---

## 4. Operational Best Practices

* **Verify ID:** Obtain exact `favoriteId` from `nova.favorites_list` before deletion.

---

## 5. Related Tools

* [`nova.favorites_list`](nova-favorites-list.md)
* [`nova.favorites_add`](nova-favorites-add.md)
