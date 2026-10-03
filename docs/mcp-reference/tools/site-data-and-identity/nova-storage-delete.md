# `nova.storage_delete`

Deletes a key from localStorage or sessionStorage for the target page.

---

## 1. Overview

`nova.storage_delete` removes a single key from `localStorage` or `sessionStorage` for the active page origin.

* **Capability Bundle:** `site_data_management`
* **Security Tier:** Tier 2 (Storage Deletion)
* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`key`** | `string` | Yes | `null` | Storage key to delete. Required. |
| **`storageType`** | `string` | Yes | `null` | Storage type. |
| **`targetId`** | `string` | Yes | `null` | Tab or sandbox ID. Required. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.storage_delete",
  "arguments": {
    "targetId": "tab-1",
    "storageType": "localStorage",
    "key": "app_theme"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Deleted localStorage key 'app_theme' on tab-1."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "storageType": "localStorage",
    "key": "app_theme",
    "status": "Deleted"
  }
}
```

---

## 4. Operational Best Practices

* **Reset Client State:** Delete cached client tokens or feature flags to test unauthenticated or pristine states.

---

## 5. Related Tools

* [`nova.storage_inspect`](nova-storage-inspect.md)
* [`nova.storage_set`](nova-storage-set.md)
