# `nova.storage_delete`

Deletes a key from localStorage or sessionStorage for the target page.

---

## 1. Overview

`nova.storage_delete` removes a single key from `localStorage` or `sessionStorage` for the active page origin.

* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | Yes | — | — | Tab or sandbox ID. Required. |
| `storageType` | `string` | Yes | — | `local`, `session` | Storage type. |
| `key` | `string` | Yes | — | — | Storage key to delete. Required. |

Capability bundle: `site_data_management` (load it with `nova.tools_bundle(bundle='site_data_management')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.storage_delete",
  "arguments": {
    "targetId": "tab-1",
    "storageType": "local",
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
      "text": "Deleted localStorage key 'app_theme' (all_browser_tabs)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "storageType": "local",
    "key": "app_theme",
    "existed": true,
    "scope": {
      "profileId": "Tabs",
      "profileScope": "all_browser_tabs",
      "isSharedProfile": true
    }
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
