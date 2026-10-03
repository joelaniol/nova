# Site Data, Fingerprinting & Sandboxes

Cookie jars, localStorage/sessionStorage, cache purging, browser fingerprint spoofing, and sandbox isolation.

* **Core Architecture Guide:** [Core Features: sandbox-isolation.md](../../../core-features/sandbox-isolation.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

<!-- generated:tool-list (from the tool pages in this folder; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
## Tool Inventory (23 Tools)

Capability bundles of these tools: `browser_automation`, `fingerprint_protection`, `identity_management`, `site_data_management`, `system_tools`.

| Tool | What it does |
| :--- | :--- |
| **[`nova.cache_clear`](nova-cache-clear.md)** | Clears HTTP cache, cookies, DOM storage, and indexedDB for the target profile. |
| **[`nova.cookie_clear`](nova-cookie-clear.md)** | Clears cookies across the target profile, with optional domain filtering. |
| **[`nova.cookie_delete`](nova-cookie-delete.md)** | Deletes a specific cookie by cookieId or by name, domain, and path tuple. |
| **[`nova.cookie_list`](nova-cookie-list.md)** | Lists cookies for the target tab's profile with metadata (domain, path, flags, expiry). |
| **[`nova.cookie_set`](nova-cookie-set.md)** | Sets or updates a cookie in the target sandbox profile's cookie jar. |
| **[`nova.fingerprint_get`](nova-fingerprint-get.md)** | Reads the active browser fingerprint protection level (global, sandbox, or tab override). |
| **[`nova.fingerprint_set_global`](nova-fingerprint-set-global.md)** | Sets the global browser fingerprint protection level across all sandboxes. |
| **[`nova.fingerprint_set_sandbox`](nova-fingerprint-set-sandbox.md)** | Sets or clears the per-sandbox fingerprint protection override. |
| **[`nova.fingerprint_set_tab`](nova-fingerprint-set-tab.md)** | Sets an ephemeral per-tab fingerprint protection override that expires on tab close. |
| **[`nova.identity_get`](nova-identity-get.md)** | Reads the active browser identity profile, spoofed User-Agent, and client hints. |
| **[`nova.identity_presets`](nova-identity-presets.md)** | Lists available browser identity presets and selectable browser engine versions. |
| **[`nova.identity_set`](nova-identity-set.md)** | Configures and persists a new browser identity profile (preset + version/custom UA). |
| **[`nova.resolve_sandbox`](nova-resolve-sandbox.md)** | Resolves the best matching sandbox container for a given workflow intent. |
| **[`nova.sandbox_context`](nova-sandbox-context.md)** | Returns detailed identity, cookie jar bounds, and context metadata for a specific sandbox. |
| **[`nova.sandbox_create`](nova-sandbox-create.md)** | Creates a new isolated sandbox profile with dedicated storage, cookies, and cache. |
| **[`nova.sandbox_delete`](nova-sandbox-delete.md)** | Permanently removes a sandbox profile and deletes its storage, cookies, and cache. |
| **[`nova.sandbox_update`](nova-sandbox-update.md)** | Updates configuration, display name, color tag, or purpose of an existing sandbox. |
| **[`nova.site_mcp_connect_request`](nova-site-mcp-connect-request.md)** | Requests an authenticated OAuth 2.1 connection to a website's discovered MCP server. |
| **[`nova.site_mcp_inspect`](nova-site-mcp-inspect.md)** | Inspects a discovered MCP server from cached discovery metadata (identity, transport, auth status). |
| **[`nova.site_permissions_reset_origin`](nova-site-permissions-reset-origin.md)** | One-click reset of all stored permissions (media, notifications, geolocation) for an origin. |
| **[`nova.storage_delete`](nova-storage-delete.md)** | Deletes a key from localStorage or sessionStorage for the target page. |
| **[`nova.storage_inspect`](nova-storage-inspect.md)** | Reads localStorage or sessionStorage key-value pairs for the target page. |
| **[`nova.storage_set`](nova-storage-set.md)** | Sets a key-value pair in localStorage or sessionStorage for the target page. |
<!-- /generated:tool-list -->

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
