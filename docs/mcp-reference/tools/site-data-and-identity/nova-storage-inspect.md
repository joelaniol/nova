# `nova.storage_inspect`

Reads localStorage or sessionStorage key-value pairs for the target page.

---

## 1. Overview

`nova.storage_inspect` reads HTML5 Web Storage (`localStorage` or `sessionStorage`) for the target tab's origin. By default, it returns keys only; use `includeValues: true` to inspect stored values.

* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | Yes | — | — | Tab or sandbox ID. Required. |
| `storageType` | `string` | Yes | — | `local`, `session` | Storage type to inspect. |
| `keyFilter` | `string` | No | — | — | Optional substring match on key name. |
| `includeValues` | `boolean` | No | `false` | — | Include storage values. Default: false (keys only). When true, the request may be treated as a HIGH-IMPACT secret read because values may contain JWTs, tokens, or app state. |
| `valueMaxChars` | `integer` | No | `120` | 1–10000 | Max characters per value. Default: 120. |
| `maxEntries` | `integer` | No | `100` | 1–1000 | Max entries to return. Default: 100. |

**`_meta.intent` is required for certain arguments.** Passing a short reason in `_meta.intent` is always safe; a rejected call names the argument that made it required.

Capability bundle: `site_data_management` (load it with `nova.tools_bundle(bundle='site_data_management')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.storage_inspect",
  "arguments": {
    "targetId": "tab-1",
    "storageType": "local",
    "includeValues": true,
    "keyFilter": "auth_"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Inspected localStorage for all_browser_tabs."
    }
  ],
  "structuredContent": {
    "ok": true,
    "storageType": "local",
    "data": {
      "entries": [
        {
          "key": "auth_token",
          "value": "eyJh...",
          "valueTruncated": false,
          "valueLength": 142
        }
      ],
      "totalCount": 1,
      "truncated": false
    },
    "scope": {
      "profileId": "Tabs",
      "profileScope": "all_browser_tabs",
      "isSharedProfile": true
    },
    "includeValues": true,
    "topLevelOriginOnly": true
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
