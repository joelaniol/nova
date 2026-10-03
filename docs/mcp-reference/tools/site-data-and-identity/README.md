# Site Data, Fingerprinting & Sandboxes

Cookie jars, localStorage/sessionStorage, cache purging, browser fingerprint spoofing, and sandbox isolation.

* **Capability Bundle(s):** `site_data_management, fingerprint_protection`
* **Core Architecture Guide:** [Core Features: sandbox-isolation.md](../../../core-features/sandbox-isolation.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (23 Tools)

| Tool Name | Status | Description |
| :--- | :---: | :--- |
| **[`nova.cache_clear`](nova-cache-clear.md)** | Documented | Clear browsing data (cache, storage, cookies) for the target's profile. |
| **[`nova.cookie_clear`](nova-cookie-clear.md)** | Documented | Delete cookies for the target's profile, with optional domain filtering. |
| **[`nova.cookie_delete`](nova-cookie-delete.md)** | Documented | Delete a specific cookie by identity (cookieId or tuple). |
| **[`nova.cookie_list`](nova-cookie-list.md)** | Documented | List cookies for the target's profile with flags and expiry metadata. |
| **[`nova.cookie_set`](nova-cookie-set.md)** | Documented | Set or update a cookie in the target sandbox profile. |
| **[`nova.fingerprint_get`](nova-fingerprint-get.md)** | Documented | Read the current fingerprint protection state and active overrides. |
| **[`nova.fingerprint_set_global`](nova-fingerprint-set-global.md)** | Documented | Set the global browser fingerprint protection level across all sandboxes. |
| **[`nova.fingerprint_set_sandbox`](nova-fingerprint-set-sandbox.md)** | Documented | Set or clear the per-sandbox fingerprint protection override. |
| **[`nova.fingerprint_set_tab`](nova-fingerprint-set-tab.md)** | Documented | Set or clear an ephemeral per-tab fingerprint protection override. |
| **[`nova.identity_get`](nova-identity-get.md)** | Documented | Read current browser identity configuration, preset, and effective User-Agent. |
| **[`nova.identity_presets`](nova-identity-presets.md)** | Documented | List all available browser identity presets and selectable versions. |
| **[`nova.identity_set`](nova-identity-set.md)** | Documented | Persist a new browser identity profile (preset + version/custom UA). |
| **[`nova.resolve_sandbox`](nova-resolve-sandbox.md)** | Documented | Resolves the best matching sandbox container for a given workflow intent. |
| **[`nova.sandbox_context`](nova-sandbox-context.md)** | Documented | Returns detailed identity and context metadata for a specific sandbox. |
| **[`nova.sandbox_create`](nova-sandbox-create.md)** | Documented | Creates a new sandbox profile with isolated browser storage and cookies. |
| **[`nova.sandbox_delete`](nova-sandbox-delete.md)** | Documented | Permanently removes a sandbox profile and its browser data. |
| **[`nova.sandbox_update`](nova-sandbox-update.md)** | Documented | Updates properties, labels, and colors of an existing sandbox profile. |
| **[`nova.site_mcp_connect_request`](nova-site-mcp-connect-request.md)** | Documented | Request authenticated connection to a discovered MCP server via OAuth 2.1. |
| **[`nova.site_mcp_inspect`](nova-site-mcp-inspect.md)** | Documented | Inspect a discovered MCP server from cached discovery metadata. |
| **[`nova.site_permissions_reset_origin`](nova-site-permissions-reset-origin.md)** | Documented | One-click reset of all stored per-site permission state for an origin. |
| **[`nova.storage_delete`](nova-storage-delete.md)** | Documented | Delete a key from localStorage or sessionStorage for the target's current page. |
| **[`nova.storage_inspect`](nova-storage-inspect.md)** | Documented | Read localStorage or sessionStorage for the target's current page. |
| **[`nova.storage_set`](nova-storage-set.md)** | Documented | Set a key-value pair in localStorage or sessionStorage for the target page. |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
