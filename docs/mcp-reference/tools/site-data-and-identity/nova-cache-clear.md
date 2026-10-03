# `nova.cache_clear`

Clears HTTP cache, cookies, DOM storage, and indexedDB for the target profile.

---

## 1. Overview

`nova.cache_clear` performs a comprehensive purge of browser data for the target sandbox profile. As a high-impact destructive tool, it requires explicit confirmation or user intent.

* **Capability Bundle:** `site_data_management`
* **Security Tier:** Tier 3 (Destructive Cache Clearance)
* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`dataTypes`** | `array` | Yes | `null` | Data types to clear. Maps 1:1 to CoreWebView2BrowsingDataKinds. |
| **`targetId`** | `string` | Yes | `null` | Tab or sandbox ID. Required. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.cache_clear",
  "arguments": {
    "targetId": "tab-1",
    "dataTypes": [
      "diskCache",
      "memoryCache",
      "serviceWorkers"
    ]
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Cleared diskCache, memoryCache, and serviceWorkers for profile on tab-1."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "clearedTypes": [
      "diskCache",
      "memoryCache",
      "serviceWorkers"
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Granular Data Types:** Select specific data types (`diskCache`, `memoryCache`, `cookies`, `indexedDb`, `serviceWorkers`) to avoid blowing away session logins when only cache clearing is needed.

---

## 5. Related Tools

* [`nova.cookie_clear`](nova-cookie-clear.md)
* [`nova.storage_delete`](nova-storage-delete.md)
