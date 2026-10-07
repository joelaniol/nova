# `nova.cache_clear`

Clears selected browsing data (cache, cookies, storage, service workers, or history) for the target profile.

---

## 1. Overview

`nova.cache_clear` performs a comprehensive purge of browser data for the target sandbox profile. As a high-impact destructive tool, it requires explicit confirmation or user intent.

* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | Yes | — | — | Tab or sandbox ID. Required. |
| `dataTypes` | `array` of `string` | Yes | — | ≥ 1 items | Data types to clear. Maps 1:1 to CoreWebView2BrowsingDataKinds. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `site_data_management` (load it with `nova.tools_bundle(bundle='site_data_management')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

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
      "cacheStorage",
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
      "text": "Cleared browsing data (diskCache, cacheStorage, serviceWorkers) for sandbox:tab-1."
    }
  ],
  "structuredContent": {
    "ok": true,
    "clearedDataTypes": [
      "diskCache",
      "cacheStorage",
      "serviceWorkers"
    ],
    "scope": {
      "profileId": "tab-1",
      "profileScope": "sandbox:tab-1",
      "isSharedProfile": false
    },
    "accountStateInvalidated": false,
    "warnings": []
  }
}
```

---

## 4. Operational Best Practices

* **Granular Data Types:** Select specific data types (`diskCache`, `cacheStorage`, `cookies`, `localStorage`, `serviceWorkers`) to avoid blowing away session logins when only cache clearing is needed. `localStorage` also covers sessionStorage and indexedDB — WebView2 does not separate them.
* **Profile-Wide Scope:** The clear applies to the whole profile, not just the current page, and may affect every tab sharing that profile.

---

## 5. Related Tools

* [`nova.cookie_clear`](nova-cookie-clear.md)
* [`nova.storage_delete`](nova-storage-delete.md)
