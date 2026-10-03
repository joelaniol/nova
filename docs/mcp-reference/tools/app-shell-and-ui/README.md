# App Shell, Dialogs & DevTools

WinUI window controls, native OS dialog handling, DevTools panels, setup wizard, and onboarding injection.

* **Capability Bundle(s):** `app_shell_recovery, onboarding`
* **Core Architecture Guide:** [Core Features: native-dialogs-and-prompts.md](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (59 Tools)

| Tool Name | Status | Description |
| :--- | :---: | :--- |
| **[`nova.agent_activity_summary`](nova-agent-activity-summary.md)** | Documented | Aggregate this session's MCP tool calls per agent: which agentId ran how many calls on which tabs (targets), top tools, success... |
| **[`nova.app_info`](nova-app-info.md)** | Documented | Read app/version/build/runtime/storage metadata (Info / Version / Sysinfo).. |
| **[`nova.app_quit`](nova-app-quit.md)** | Documented | Gracefully shut down the entire Nova app. |
| **[`nova.bookmarks_folder_create`](nova-bookmarks-folder-create.md)** | Documented | Create a bookmark folder. |
| **[`nova.bookmarks_folder_delete`](nova-bookmarks-folder-delete.md)** | Documented | Delete a bookmark folder. |
| **[`nova.bookmarks_folder_rename`](nova-bookmarks-folder-rename.md)** | Documented | Rename a bookmark folder.. |
| **[`nova.bookmarks_folders_list`](nova-bookmarks-folders-list.md)** | Documented | List bookmark folders (id, name, parentId, sortOrder, depth, createdUtc). |
| **[`nova.cdp`](nova-cdp.md)** | Documented | Raw CDP passthrough: call an arbitrary DevTools protocol method (dangerous). |
| **[`nova.clipboard_read`](nova-clipboard-read.md)** | Documented | Read the current text content from the Windows clipboard.. |
| **[`nova.clipboard_write`](nova-clipboard-write.md)** | Documented | Write text to the Windows clipboard. |
| **[`nova.create_dump`](nova-create-dump.md)** | Documented | Create a debug dump (screenshot, DOM, resources) for a tab. |
| **[`nova.devtools_open`](nova-devtools-open.md)** | Documented | Open DevTools for a target. |
| **[`nova.devtools_select_panel`](nova-devtools-select-panel.md)** | Documented | Dispatch the DevTools panel shortcut for a target (for example: elements, console, network). |
| **[`nova.favorites_add`](nova-favorites-add.md)** | Documented | Add or update a favorite/bookmark by URL. |
| **[`nova.favorites_list`](nova-favorites-list.md)** | Documented | List saved favorites/bookmarks.. |
| **[`nova.favorites_move`](nova-favorites-move.md)** | Documented | Move a favorite into a bookmark folder (or to root when folderId is null). |
| **[`nova.favorites_open`](nova-favorites-open.md)** | Documented | Open a saved favorite URL in the current active browser tab, or in a new browser tab when requested. |
| **[`nova.favorites_remove`](nova-favorites-remove.md)** | Documented | Remove a favorite/bookmark. |
| **[`nova.get_instructions`](nova-get-instructions.md)** | Documented | Get the Nova agent contract and operational instructions. |
| **[`nova.get_onboarding`](nova-get-onboarding.md)** | Documented | Manual onboarding fallback — write the files yourself. |
| **[`nova.grep_resources`](nova-grep-resources.md)** | Documented | Search loaded text resources (scripts, stylesheets, documents) for a literal string or regex and return compact match contexts. |
| **[`nova.install_onboarding`](nova-install-onboarding.md)** | Documented | Primary onboarding entrypoint — call this when asked to onboard, set up, or install Nova into a project. |
| **[`nova.list_resources`](nova-list-resources.md)** | Documented | List loaded resources for a tab (scripts/stylesheets/documents). |
| **[`nova.mcp_transport_log`](nova-mcp-transport-log.md)** | Documented | Read a bounded, redacted view of Nova's own MCP transport/server log from Logs/mcp/mcp-*.log. |
| **[`nova.ok_observe`](nova-ok-observe.md)** | Documented | Push structured observations about current page state. |
| **[`nova.ok_signal_schema`](nova-ok-signal-schema.md)** | Documented | List canonical Operational Knowledge signal keys accepted by nova.ok_observe. |
| **[`nova.permission_center_get`](nova-permission-center-get.md)** | Documented | Get global Permission Center defaults (camera/microphone/speaker/geolocation) and currently available media devices, including ... |
| **[`nova.permission_center_set`](nova-permission-center-set.md)** | Documented | Update global Permission Center defaults plus preferred camera/microphone/speaker device IDs. |
| **[`nova.permission_prompt`](nova-permission-prompt.md)** | Documented | Request permission from the Nova operator to perform an action. |
| **[`nova.read_resource`](nova-read-resource.md)** | Documented | Read resource content (best-effort). |
| **[`nova.read_screenshot_resource`](nova-read-screenshot-resource.md)** | Documented | Read a Nova screenshot resource URI returned by capture tools (nova://screenshot/...). |
| **[`nova.reference_doc_read`](nova-reference-doc-read.md)** | Documented | Read one allowlisted Nova reference document by docId. |
| **[`nova.reference_docs_list`](nova-reference-docs-list.md)** | Documented | List Nova's bundled reference documents that agents can fetch through MCP when the Nova source repository is not available in t... |
| **[`nova.setup_status`](nova-setup-status.md)** | Documented | Report whether AI programs on this machine are connected to this Nova. |
| **[`nova.setup_wizard_open`](nova-setup-wizard-open.md)** | Documented | Open Nova's guided connection setup dialog, which walks the user through connecting AI programs (Claude Code, Codex, Claude Des... |
| **[`nova.tools_bundle`](nova-tools-bundle.md)** | Documented | Two ways in, and the second is the one to reach for when you are unsure: (1) bundle='<id>' returns a curated toolset; (2) query... |
| **[`nova.ui_auth_prompt_resolve`](nova-ui-auth-prompt-resolve.md)** | Documented | Answer Nova's HTTP sign-in dialog (the one raised by a server's 401 challenge). |
| **[`nova.ui_certificate_prompt_resolve`](nova-ui-certificate-prompt-resolve.md)** | Documented | Answer Nova's certificate dialog (raised when a server presents a certificate Nova cannot verify). |
| **[`nova.ui_client_certificate_prompt_resolve`](nova-ui-client-certificate-prompt-resolve.md)** | Documented | Answer Nova's client-certificate dialog (raised when a server asks the browser to identify itself with a certificate). |
| **[`nova.ui_close_downloads`](nova-ui-close-downloads.md)** | Documented | Close the download manager panel in the app UI.. |
| **[`nova.ui_close_settings`](nova-ui-close-settings.md)** | Documented | Close the settings overlay in the app UI.. |
| **[`nova.ui_confirm_native_dialog`](nova-ui-confirm-native-dialog.md)** | Documented | Best-effort trigger the primary affirmative action on the currently open host-owned native dialog. |
| **[`nova.ui_dismiss_native_dialog`](nova-ui-dismiss-native-dialog.md)** | Documented | Best-effort cancel the currently open host-owned native dialog (for example a file picker or print dialog) by focusing it and s... |
| **[`nova.ui_download_security_prompt_resolve`](nova-ui-download-security-prompt-resolve.md)** | Documented | Answer Nova's question about a download Windows could execute (.exe, .msi, .ps1, .bat and the like). |
| **[`nova.ui_get_state`](nova-ui-get-state.md)** | Documented | Get app UI state (active tab, overlay visibility, UI responsiveness, and whether a host-owned native dialog is currently open). |
| **[`nova.ui_inspect_native_dialog`](nova-ui-inspect-native-dialog.md)** | Documented | Inspect the currently open host-owned native dialog. |
| **[`nova.ui_open_downloads`](nova-ui-open-downloads.md)** | Documented | Open the download manager panel in the app UI.. |
| **[`nova.ui_open_settings`](nova-ui-open-settings.md)** | Documented | Open the settings overlay (gear icon) in the app UI. |
| **[`nova.ui_permission_prompt_resolve`](nova-ui-permission-prompt-resolve.md)** | Documented | End a Nova permission dialog that is blocking tool calls (e.g. |
| **[`nova.ui_restore_tabs_prompt_resolve`](nova-ui-restore-tabs-prompt-resolve.md)** | Documented | Resolve the startup restore-tabs prompt with a decision (restore, discard, or not_now).. |
| **[`nova.ui_restore_tabs_prompt_state`](nova-ui-restore-tabs-prompt-state.md)** | Documented | Get startup restore-tabs prompt state and preview of the pending tab snapshot.. |
| **[`nova.ui_set_native_dialog_file_name`](nova-ui-set-native-dialog-file-name.md)** | Documented | Best-effort fill the standard file-name field of the currently open host-owned file picker dialog. |
| **[`nova.webview_get_zoom`](nova-webview-get-zoom.md)** | Documented | Get the WebView zoom factor (CSS zoom, best-effort).. |
| **[`nova.webview_reset_zoom`](nova-webview-reset-zoom.md)** | Documented | Reset the WebView zoom factor to the default 1.0 / 100% (CSS zoom, best-effort). |
| **[`nova.webview_set_zoom`](nova-webview-set-zoom.md)** | Documented | Set the WebView zoom factor (CSS zoom, best-effort). |
| **[`nova.window_get_bounds`](nova-window-get-bounds.md)** | Documented | Get the app window bounds (position + size) plus current-monitor and monitor-inventory metadata.. |
| **[`nova.window_move`](nova-window-move.md)** | Documented | Move the app window to a selected monitor work area using a monitor index from nova.window_get_bounds.availableMonitors (best-e... |
| **[`nova.window_set_size`](nova-window-set-size.md)** | Documented | Resize the app window (best-effort).. |
| **[`nova.window_set_state`](nova-window-set-state.md)** | Documented | Set the app window state: minimize, maximize, restore, or bring to foreground.. |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
