# Agent-Authored Plugins

Write, test, and ship agent-authored browser plugins that change how pages behave.

* **Core Architecture Guide:** [Core Features: plugins.md](../../../core-features/plugins/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

<!-- generated:tool-list (from the tool pages in this folder; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
## Tool Inventory (22 Tools)

Capability bundles of these tools: `plugin_management`.

| Tool | What it does |
| :--- | :--- |
| **[`nova.plugin_create`](nova-plugin-create.md)** | Create and install a new agent-authored plugin from a manifest JSON string. |
| **[`nova.plugin_css_reset`](nova-plugin-css-reset.md)** | Remove the plugin's host-owned injected stylesheet from active page sessions. |
| **[`nova.plugin_disable`](nova-plugin-disable.md)** | Disable a plugin. |
| **[`nova.plugin_enable`](nova-plugin-enable.md)** | Activate a plugin that is either disabled or waiting in Testing state. |
| **[`nova.plugin_export`](nova-plugin-export.md)** | Export a plugin as a base64-encoded .novaplugin ZIP bundle containing manifest, source code, and optionally persistent KV storage data (including typed storage.local / storage.sync snapshots). |
| **[`nova.plugin_get_code`](nova-plugin-get-code.md)** | Read the declared JavaScript source files of an installed plugin. |
| **[`nova.plugin_get_version_code`](nova-plugin-get-version-code.md)** | Read a specific historical snapshot of a plugin's code + manifest from plugin_version_history. |
| **[`nova.plugin_grant_active_tab`](nova-plugin-grant-active-tab.md)** | Start an installed plugin on the current browser tab with temporary activeTab-style access. |
| **[`nova.plugin_icons_list`](nova-plugin-icons-list.md)** | List all plugin icon names known to the host (used in manifest.ui.icon). |
| **[`nova.plugin_import`](nova-plugin-import.md)** | Import a plugin from a base64-encoded .novaplugin ZIP bundle. |
| **[`nova.plugin_inject_reset`](nova-plugin-inject-reset.md)** | Unmount all overlay elements injected by a plugin. |
| **[`nova.plugin_inspect`](nova-plugin-inspect.md)** | Detailed inspection of a plugin: full state snapshot, manifest details, granted permissions, contentScriptInventory for static/dynamic scripts vs active/known live frames, plugin storage key counts (persistent KV plus host-managed keys), active mutation count, and recent mutations. |
| **[`nova.plugin_list`](nova-plugin-list.md)** | List all installed agent-authored plugins with their install state, runtime state, permissions, and error/crash counts. |
| **[`nova.plugin_logs`](nova-plugin-logs.md)** | Retrieve recent error log entries for a specific plugin. |
| **[`nova.plugin_managed_storage_get`](nova-plugin-managed-storage-get.md)** | Read host-controlled managed storage for an installed plugin. |
| **[`nova.plugin_managed_storage_update`](nova-plugin-managed-storage-update.md)** | Create, update, or delete host-controlled managed storage values for an installed plugin. |
| **[`nova.plugin_request_permission`](nova-plugin-request-permission.md)** | Grant review-gated permissions or scopes for an installed plugin. |
| **[`nova.plugin_rollback`](nova-plugin-rollback.md)** | Restore an installed plugin to a specific snapshot from plugin_version_history. |
| **[`nova.plugin_security_log`](nova-plugin-security-log.md)** | Read recent security policy violations recorded by the bridge enforcement layer (permission_denied, quota_exceeded, url_blocked, script_blocked, redirect_blocked, oversize_attempt). |
| **[`nova.plugin_test`](nova-plugin-test.md)** | Execute or smoke-test a JS script in a plugin's Jint runtime. |
| **[`nova.plugin_uninstall`](nova-plugin-uninstall.md)** | Uninstall a plugin. |
| **[`nova.plugin_update`](nova-plugin-update.md)** | Update an installed plugin's source code and/or manifest. |
<!-- /generated:tool-list -->
---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
