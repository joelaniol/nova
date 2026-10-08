# `nova.storage_set`

Sets a key-value pair in localStorage or sessionStorage for the target page.

---

## 1. Overview

`nova.storage_set` writes data into `localStorage` or `sessionStorage` on the target page's origin.

* **Core Feature Guide:** [Web Storage](../../../core-features/site-data-management/web-storage/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | Yes | — | — | Tab or sandbox ID. Required. |
| `storageType` | `string` | Yes | — | `local`, `session` | Storage type. |
| `key` | `string` | Yes | — | — | Storage key. Required. |
| `value` | `string` | Yes | — | — | Storage value. Required. |

Capability bundle: `site_data_management` (load it with `nova.tools_bundle(bundle='site_data_management')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.storage_set",
  "arguments": {
    "targetId": "tab-1",
    "storageType": "local",
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
      "text": "Set localStorage key 'app_theme' (all_browser_tabs)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "storageType": "local",
    "key": "app_theme",
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

* **State Seeding:** Pre-seed local storage keys to bypass first-run onboarding guides or set client feature flags.

---

## 5. Related Tools

* [`nova.storage_inspect`](nova-storage-inspect.md)
* [`nova.storage_delete`](nova-storage-delete.md)
