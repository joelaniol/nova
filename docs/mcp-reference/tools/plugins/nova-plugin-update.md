# `nova.plugin_update`

> **Update an installed plugin's source code and/or manifest.**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

Update an installed plugin's source code and/or manifest. Stops the runtime, writes new files, re-registers, and preserves disabled/testing state. At least one of 'code', 'files', or 'manifest' must be provided. Plugin JS can use: nova.dom (querySelectorAll/getTextContent/getAttribute/getBounds + observe/unobserve for MutationObserver summaries), nova.overlay (mount/patch/unmount/setBadge/notify Shadow-DOM overlays with structured content JSON, plus onEvent/offEvent for delegated click/change/input/submit on data-nova-id sub-elements), nova.tools.register/unregister (binds plugin-declared MCP tools from manifest.mcpTools to JS handlers, exposed to agents as 'plugin.{pluginId}.{toolName}'), nova.mutation (addClass/removeClass/setStyle/unsetStyle/injectCss with nova-p-{id}- prefix), nova.storage (local/sync/session typed storage via get/set/remove/keys, read-only managed storage via get/keys, plus onChanged/offChanged for local/sync/session/managed diffs), nova.diag (raw storageGet/Set/Delete/Keys + reportError), nova.net (HTTPS GET fetch, URL must match manifest.network.allow), nova.runtime (onMessage/offMessage/sendMessage one-shot JSON-only runtime message bus with structured responses, plus onConnect/offConnect/connect(name) for long-lived ports on the current live runtime; Nova uses those ports today for ui.actionPopup/ui.options/ui.sidePanel plus overlay.session/page.session/browser.tabs, can reuse runtime-initiated popup/options/side-panel ports when those surfaces open later, and mirrors live overlay/page-session plus browser-tab host events onto the same bus), nova.on (lifecycle events: install/startup/documentMatched/routeChanged/windowFocusChanged/windowStateChanged/tabCreated/tabClosed/tabActivated/tabUpdated/disable/alarm; install/startup are queued host events delivered on the next live session, windowFocusChanged/windowStateChanged broadcast main-window focus/state for windowId='main' to already-live runtimes, tabCreated/tabClosed broadcast only to already-live runtimes, tabActivated fires only for already-live sessions on the newly active browser tab, and tabUpdated reports host URL/title changes for already-live sessions on that tab), nova.alarms (set/clear/list timer-based alarms). All methods are synchronous. Use plugin_get_code first to read existing source before editing.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `pluginId` | `string` | Yes | — | — | The plugin ID to update. |
| `code` | `string` | No | — | — | New JS source code for the plugin's entry-point file. |
| `files` | `object` | No | — | — | Optional map of src-relative JavaScript file paths to source strings. Use this to add or update manifest.contentScripts[] files without replacing the entry-point shorthand. |
| `manifest` | `string` | No | — | — | New manifest JSON string. Must be a valid plugin manifest. |
| `changeNote` | `string` | No | — | — | Optional human-readable note describing the update (max 500 chars). Stored in plugin_version_history for agent-readable changelog. |
| `deferActivation` | `boolean` | No | `false` | — | If true and the plugin is currently Installed, move it into Testing state after the update so it cannot auto-activate until a passing smoke run uses activateAfterPass=true or plugin_enable is called manually. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `plugin_management` (load it with `nova.tools_bundle(bundle='plugin_management')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## See Also

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins/README.md)
