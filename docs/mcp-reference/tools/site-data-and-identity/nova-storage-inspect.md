# `nova.storage_inspect`

Reads localStorage or sessionStorage key-value pairs for the target page.

---

## 1. Overview

`nova.storage_inspect` reads HTML5 Web Storage (`localStorage` or `sessionStorage`) for the target tab's origin. By default, it returns keys only; use `includeValues: true` to inspect stored values.

* **Capability Bundle:** `site_data_management`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`includeValues`** | `boolean` | No | `false` | Include storage values. Default: false (keys only). When true, the request may be treated as a HIGH-IMPACT secret read because values may contain JWTs, tokens, or app state. |
| **`keyFilter`** | `string` | No | `null` | Optional substring match on key name. |
| **`maxEntries`** | `integer` | No | `100` | Max entries to return. Default: 100. |
| **`storageType`** | `string` | Yes | `null` | Storage type to inspect. |
| **`targetId`** | `string` | Yes | `null` | Tab or sandbox ID. Required. |
| **`valueMaxChars`** | `integer` | No | `120` | Max characters per value. Default: 120. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.storage_inspect",
  "arguments": {
    "targetId": "tab-1",
    "storageType": "localStorage",
    "includeValues": true,
    "keyFilter": "auth_*"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Inspected localStorage on tab-1: 1 key found."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "storageType": "localStorage",
    "entries": [
      {
        "key": "auth_token",
        "value": "eyJh..."
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Origin Confinement:** Web Storage is bound strictly to the target page's active origin.
* **Value Truncation:** Use `valueMaxChars` to avoid loading massive serialized JSON states into LLM context.

---

## 5. Related Tools

* [`nova.storage_set`](nova-storage-set.md)
* [`nova.storage_delete`](nova-storage-delete.md)
