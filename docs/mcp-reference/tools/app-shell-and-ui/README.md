# App Shell, Dialogs & DevTools

WinUI window controls, native OS dialog handling, DevTools panels, setup wizard, and onboarding injection.

* **Core Architecture Guide:** [Core Features: native-dialogs-and-prompts.md](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

<!-- generated:tool-list (from the tool pages in this folder; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
## Tool Inventory (59 Tools)

Capability bundles of these tools: `app_shell_recovery`, `onboarding`, `page_read_debug`, `system_tools`, `visual_evidence`.

| Tool | What it does |
| :--- | :--- |
| **[`nova.agent_activity_summary`](nova-agent-activity-summary.md)** | Returns an aggregated summary of active MCP sessions, tool execution counts, and failure rates. |
| **[`nova.app_info`](nova-app-info.md)** | Returns runtime environment metadata, version numbers, process uptime, and storage paths. |
| **[`nova.app_quit`](nova-app-quit.md)** | Gracefully terminates the Nova host application process and all child WebView2 runtimes. |
| **[`nova.bookmarks_folder_create`](nova-bookmarks-folder-create.md)** | Creates a hierarchical folder in the browser bookmark collection. |
| **[`nova.bookmarks_folder_delete`](nova-bookmarks-folder-delete.md)** | Deletes a bookmark folder and optionally its contained bookmarks and subfolders. |
| **[`nova.bookmarks_folder_rename`](nova-bookmarks-folder-rename.md)** | Renames an existing bookmark folder. |
| **[`nova.bookmarks_folders_list`](nova-bookmarks-folders-list.md)** | Lists all bookmark folders with hierarchical parent-child relationships and depths. |
| **[`nova.cdp`](nova-cdp.md)** | Executes a raw Chrome DevTools Protocol (CDP) method directly on the target WebView2 instance. |
| **[`nova.clipboard_read`](nova-clipboard-read.md)** | Reads the current plain text contents from the Windows OS system clipboard. |
| **[`nova.clipboard_write`](nova-clipboard-write.md)** | Writes plain text to the Windows OS system clipboard. |
| **[`nova.create_dump`](nova-create-dump.md)** | Generates a forensic debug bundle for a browser tab (screenshot, DOM snapshot, console logs, resources). |
| **[`nova.devtools_open`](nova-devtools-open.md)** | Opens the Chromium DevTools inspection window for a specified browser tab. |
| **[`nova.devtools_select_panel`](nova-devtools-select-panel.md)** | Focuses a specific panel within an open DevTools window (Console, Elements, Network, Sources). |
| **[`nova.favorites_add`](nova-favorites-add.md)** | Adds a URL to the browser favorites collection with optional title and target folder. |
| **[`nova.favorites_list`](nova-favorites-list.md)** | Lists saved browser favorites, optionally filtered by bookmark folder. |
| **[`nova.favorites_move`](nova-favorites-move.md)** | Moves a bookmark favorite into a different folder or to the root collection. |
| **[`nova.favorites_open`](nova-favorites-open.md)** | Navigates to a stored favorite bookmark in the current or a new browser tab. |
| **[`nova.favorites_remove`](nova-favorites-remove.md)** | Removes a bookmark favorite by its unique identifier. |
| **[`nova.get_instructions`](nova-get-instructions.md)** | Retrieves the complete Nova AI operational contract, conventions, and agent guidelines. |
| **[`nova.get_onboarding`](nova-get-onboarding.md)** | Retrieves manual onboarding instructions and template markdown files for external AI agents. |
| **[`nova.grep_resources`](nova-grep-resources.md)** | Searches loaded page resources (scripts, stylesheets, HTML) for matching literal text or regex patterns. |
| **[`nova.install_onboarding`](nova-install-onboarding.md)** | Automatically injects Nova MCP server configurations and reference docs into the current agent workspace. |
| **[`nova.list_resources`](nova-list-resources.md)** | Lists all network resources (scripts, stylesheets, frames, images) loaded by the target tab. |
| **[`nova.mcp_transport_log`](nova-mcp-transport-log.md)** | Reads recent redacted entries from Nova's internal MCP JSON-RPC transport log. |
| **[`nova.ok_observe`](nova-ok-observe.md)** | Pushes a structured Operational Knowledge (OK) signal about page state, blocking patterns, or layout shifts. |
| **[`nova.ok_signal_schema`](nova-ok-signal-schema.md)** | Lists the canonical Operational Knowledge signal keys accepted by nova.ok_observe. |
| **[`nova.permission_center_get`](nova-permission-center-get.md)** | Retrieves global Permission Center default policies and detected hardware media devices. |
| **[`nova.permission_center_set`](nova-permission-center-set.md)** | Configures global Permission Center default policies and preferred media hardware devices. |
| **[`nova.permission_prompt`](nova-permission-prompt.md)** | Raises an interactive permission dialog asking the Nova human operator to approve a high-risk action. |
| **[`nova.read_resource`](nova-read-resource.md)** | Fetches the raw text content of a loaded web resource by its URL. |
| **[`nova.read_screenshot_resource`](nova-read-screenshot-resource.md)** | Reads an in-memory screenshot artifact URI (nova://screenshot/...) and returns base64 image data. |
| **[`nova.reference_doc_read`](nova-reference-doc-read.md)** | Reads the complete text content of an allowlisted internal Nova reference document. |
| **[`nova.reference_docs_list`](nova-reference-docs-list.md)** | Lists all internal Nova reference documents available for in-session reading. |
| **[`nova.setup_status`](nova-setup-status.md)** | Reports the connection and configuration health of AI agent runtimes on the host machine. |
| **[`nova.setup_wizard_open`](nova-setup-wizard-open.md)** | Opens Nova's guided connection setup wizard dialog in the graphical user interface. |
| **[`nova.tools_bundle`](nova-tools-bundle.md)** | Discovers, searches, and activates curated MCP tool capability bundles or queries tools by natural language. |
| **[`nova.ui_auth_prompt_resolve`](nova-ui-auth-prompt-resolve.md)** | Resolves an active HTTP 401 Basic or Digest authentication challenge dialog. |
| **[`nova.ui_certificate_prompt_resolve`](nova-ui-certificate-prompt-resolve.md)** | Resolves an untrusted or invalid SSL/TLS server certificate security dialog. |
| **[`nova.ui_client_certificate_prompt_resolve`](nova-ui-client-certificate-prompt-resolve.md)** | Selects a client certificate or cancels a mutual TLS (mTLS) authentication prompt. |
| **[`nova.ui_close_downloads`](nova-ui-close-downloads.md)** | Closes the download manager drawer panel in the Nova host user interface. |
| **[`nova.ui_close_settings`](nova-ui-close-settings.md)** | Closes the settings drawer overlay in the Nova host user interface. |
| **[`nova.ui_confirm_native_dialog`](nova-ui-confirm-native-dialog.md)** | Triggers the primary affirmative action on the currently active host-owned Win32 native dialog. |
| **[`nova.ui_dismiss_native_dialog`](nova-ui-dismiss-native-dialog.md)** | Dismisses or cancels the currently active host-owned Win32 native dialog. |
| **[`nova.ui_download_security_prompt_resolve`](nova-ui-download-security-prompt-resolve.md)** | Resolves Nova's executable download security warning dialog (.exe, .msi, .ps1, .bat). |
| **[`nova.ui_get_state`](nova-ui-get-state.md)** | Inspects host application UI state: active tab, overlay visibility, responsiveness, and open dialogs. |
| **[`nova.ui_inspect_native_dialog`](nova-ui-inspect-native-dialog.md)** | Inspects details of the currently active host-owned Win32 native dialog (title, class, control types). |
| **[`nova.ui_open_downloads`](nova-ui-open-downloads.md)** | Opens the download manager drawer panel in the Nova host user interface. |
| **[`nova.ui_open_settings`](nova-ui-open-settings.md)** | Opens the settings drawer overlay in the Nova host user interface. |
| **[`nova.ui_permission_prompt_resolve`](nova-ui-permission-prompt-resolve.md)** | Resolves an active web permission prompt modal (camera, microphone, geolocation, notifications). |
| **[`nova.ui_restore_tabs_prompt_resolve`](nova-ui-restore-tabs-prompt-resolve.md)** | Resolves the startup tab restoration prompt modal after an abnormal browser termination. |
| **[`nova.ui_restore_tabs_prompt_state`](nova-ui-restore-tabs-prompt-state.md)** | Inspects whether a startup tab restoration prompt is active and previews saved session tabs. |
| **[`nova.ui_set_native_dialog_file_name`](nova-ui-set-native-dialog-file-name.md)** | Fills the file path or name field of an active Win32 native file picker dialog. |
| **[`nova.webview_get_zoom`](nova-webview-get-zoom.md)** | Retrieves the current zoom factor of the target tab's WebView2 control. |
| **[`nova.webview_reset_zoom`](nova-webview-reset-zoom.md)** | Resets the target tab's WebView2 zoom factor back to the default 1.0 (100%). |
| **[`nova.webview_set_zoom`](nova-webview-set-zoom.md)** | Sets the zoom factor for a target tab's WebView2 instance. |
| **[`nova.window_get_bounds`](nova-window-get-bounds.md)** | Returns host application window boundaries (position, size) and monitor inventory metadata. |
| **[`nova.window_move`](nova-window-move.md)** | Moves the Nova application window to a specific monitor or coordinate offset. |
| **[`nova.window_set_size`](nova-window-set-size.md)** | Resizes the Nova application window to specified pixel width and height. |
| **[`nova.window_set_state`](nova-window-set-state.md)** | Sets host application window state: minimize, maximize, restore, or bring to foreground. |
<!-- /generated:tool-list -->

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
