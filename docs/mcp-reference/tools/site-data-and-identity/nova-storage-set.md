# `nova.storage_set`

Sets a key-value pair in localStorage or sessionStorage for the target page.

---

## 1. Overview

`nova.storage_set` writes data into `localStorage` or `sessionStorage` on the target page's origin via the CoreWebView2 storage API.

* **Capability Bundle:** `site_data_management`
* **Security Tier:** Tier 2 (Storage Mutation)
* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`key`** | `string` | Yes | `null` | Storage key. Required. |
| **`storageType`** | `string` | Yes | `null` | Storage type. |
| **`targetId`** | `string` | Yes | `null` | Tab or sandbox ID. Required. |
| **`value`** | `string` | Yes | `null` | Storage value. Required. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.storage_set",
  "arguments": {
    "targetId": "tab-1",
    "storageType": "localStorage",
    "key": "app_theme",
    "value": "nordic"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Set localStorage key 'app_theme' on tab-1."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "storageType": "localStorage",
    "key": "app_theme",
    "status": "Set"
  }
}
```

---

## 4. Operational Best Practices

* **State Seeding:** Pre-seed local storage keys to bypass first-run onboarding guides or set client feature flags.

---

## 5. Related Tools

* [`nova.storage_inspect`](nova-storage-inspect.md)
* [`nova.storage_delete`](nova-storage-delete.md)
