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
| **[`nova.agent_activity_summary`](nova-agent-activity-summary.md)** | Returns a per-agent summary of this session's MCP tool calls: call counts, tab targets, and failure reason codes. |
| **[`nova.app_info`](nova-app-info.md)** | Returns runtime environment metadata: app version, WebView2/OS runtime info, MCP endpoint, and storage paths. |
| **[`nova.app_quit`](nova-app-quit.md)** | Gracefully terminates the Nova host application process and all child WebView2 runtimes. |
| **[`nova.bookmarks_folder_create`](nova-bookmarks-folder-create.md)** | Creates a hierarchical folder in the browser bookmark collection. |
| **[`nova.bookmarks_folder_delete`](nova-bookmarks-folder-delete.md)** | Deletes a bookmark folder and either moves its contents to the root or deletes them with it. |
| **[`nova.bookmarks_folder_rename`](nova-bookmarks-folder-rename.md)** | Renames an existing bookmark folder. |
| **[`nova.bookmarks_folders_list`](nova-bookmarks-folders-list.md)** | Lists all bookmark folders with hierarchical parent-child relationships and depths. |
| **[`nova.cdp`](nova-cdp.md)** | Executes a raw Chrome DevTools Protocol (CDP) method directly on the target WebView2 instance. |
| **[`nova.clipboard_read`](nova-clipboard-read.md)** | Reads the current plain text contents from the Windows OS system clipboard. |
| **[`nova.clipboard_write`](nova-clipboard-write.md)** | Writes plain text to the Windows OS system clipboard. |
| **[`nova.create_dump`](nova-create-dump.md)** | Writes a diagnostic dump of a browser tab (screenshot, DOM, page info, and in full mode MHTML and resources) to a folder on disk. |
| **[`nova.devtools_open`](nova-devtools-open.md)** | Opens the Chromium DevTools inspection window for a specified browser tab. |
| **[`nova.devtools_select_panel`](nova-devtools-select-panel.md)** | Dispatches the keyboard shortcut for a DevTools panel (Console, Elements, Network, Sources, ...) in an already-open DevTools window. |
| **[`nova.favorites_add`](nova-favorites-add.md)** | Adds a URL to the browser favorites collection with optional title and target folder. |
| **[`nova.favorites_list`](nova-favorites-list.md)** | Lists all saved browser favorites. |
| **[`nova.favorites_move`](nova-favorites-move.md)** | Moves a bookmark favorite into a different folder or to the root collection. |
| **[`nova.favorites_open`](nova-favorites-open.md)** | Opens a saved favorite in the current or a new browser tab. |
| **[`nova.favorites_remove`](nova-favorites-remove.md)** | Removes a saved favorite by its id or URL. |
| **[`nova.get_instructions`](nova-get-instructions.md)** | Retrieves the complete Nova AI operational contract, conventions, and agent guidelines. |
| **[`nova.get_onboarding`](nova-get-onboarding.md)** | Returns a manual edit plan — reference file contents and marker-block edits — for onboarding an agent to Nova's MCP tools, as an alternative to the one-call `nova.install_onboarding`. |
| **[`nova.grep_resources`](nova-grep-resources.md)** | Searches the text of a tab's loaded resources (scripts, stylesheets, documents) for literal text or a regex. |
| **[`nova.install_onboarding`](nova-install-onboarding.md)** | Writes Nova's reference files and a Nova block in the project's agent instruction file into a project directory. |
| **[`nova.list_resources`](nova-list-resources.md)** | Lists all network resources (scripts, stylesheets, frames, images) loaded by the target tab. |
| **[`nova.mcp_transport_log`](nova-mcp-transport-log.md)** | Reads recent redacted entries from Nova's internal MCP JSON-RPC transport log. |
| **[`nova.ok_observe`](nova-ok-observe.md)** | Records structured Operational Knowledge (OK) claims about the service open in a tab, such as login state or active model. |
| **[`nova.ok_signal_schema`](nova-ok-signal-schema.md)** | Lists the canonical Operational Knowledge signal keys accepted by nova.ok_observe. |
| **[`nova.permission_center_get`](nova-permission-center-get.md)** | Retrieves the global default permission modes for camera, microphone, speaker, and geolocation, plus the detected hardware devices. |
| **[`nova.permission_center_set`](nova-permission-center-set.md)** | Sets the global Permission Center defaults for camera, microphone, speaker and location, and the preferred media devices. |
| **[`nova.permission_prompt`](nova-permission-prompt.md)** | Asks the Nova operator to approve or deny an action that an agent wants to run. |
| **[`nova.read_resource`](nova-read-resource.md)** | Fetches the raw text content of a loaded web resource by its URL. |
| **[`nova.read_screenshot_resource`](nova-read-screenshot-resource.md)** | Reads a screenshot resource URI (`nova://screenshot/...`) returned by a capture tool and returns its image bytes as base64. |
| **[`nova.reference_doc_read`](nova-reference-doc-read.md)** | Reads the complete text content of an allowlisted internal Nova reference document. |
| **[`nova.reference_docs_list`](nova-reference-docs-list.md)** | Lists all internal Nova reference documents available for in-session reading. |
| **[`nova.setup_status`](nova-setup-status.md)** | Reports the connection and configuration health of AI agent runtimes on the host machine. |
| **[`nova.setup_wizard_open`](nova-setup-wizard-open.md)** | Opens Nova's guided connection setup wizard dialog in the graphical user interface. |
| **[`nova.tools_bundle`](nova-tools-bundle.md)** | Discovers, searches, and activates curated MCP tool capability bundles or queries tools by natural language. |
| **[`nova.ui_auth_prompt_resolve`](nova-ui-auth-prompt-resolve.md)** | Answers Nova's HTTP sign-in dialog with a stored vault entry, or cancels it. |
| **[`nova.ui_certificate_prompt_resolve`](nova-ui-certificate-prompt-resolve.md)** | Answers Nova's dialog for a server certificate it could not verify: refuse the connection or proceed for this session. |
| **[`nova.ui_client_certificate_prompt_resolve`](nova-ui-client-certificate-prompt-resolve.md)** | Answers Nova's client-certificate dialog: send a named certificate or continue without one. |
| **[`nova.ui_close_downloads`](nova-ui-close-downloads.md)** | Closes the download manager drawer panel in the Nova host user interface. |
| **[`nova.ui_close_settings`](nova-ui-close-settings.md)** | Closes the settings drawer overlay in the Nova host user interface. |
| **[`nova.ui_confirm_native_dialog`](nova-ui-confirm-native-dialog.md)** | Presses a button in the open dialog: by name in any dialog, including Nova's own, or the affirmative button of a Windows dialog. |
| **[`nova.ui_dismiss_native_dialog`](nova-ui-dismiss-native-dialog.md)** | Dismisses or cancels the currently active host-owned Win32 native dialog. |
| **[`nova.ui_download_security_prompt_resolve`](nova-ui-download-security-prompt-resolve.md)** | Answers Nova's "Keep this file?" question for a download that Windows can run (for example .exe, .msi, .bat, .ps1). |
| **[`nova.ui_get_state`](nova-ui-get-state.md)** | Inspects host application UI state: active tab, overlay visibility, responsiveness, and open dialogs. |
| **[`nova.ui_inspect_native_dialog`](nova-ui-inspect-native-dialog.md)** | Inspects the open dialog — a Windows dialog Nova owns or one of Nova's own dialogs — with its texts and buttons. |
| **[`nova.ui_open_downloads`](nova-ui-open-downloads.md)** | Opens the download manager drawer panel in the Nova host user interface. |
| **[`nova.ui_open_settings`](nova-ui-open-settings.md)** | Opens the settings drawer overlay in the Nova host user interface. |
| **[`nova.ui_permission_prompt_resolve`](nova-ui-permission-prompt-resolve.md)** | Defers or answers the permission dialog that Nova is showing for a site (for example location, notifications, clipboard read or advanced device access). |
| **[`nova.ui_restore_tabs_prompt_resolve`](nova-ui-restore-tabs-prompt-resolve.md)** | Resolves the startup tab restoration prompt modal after an abnormal browser termination. |
| **[`nova.ui_restore_tabs_prompt_state`](nova-ui-restore-tabs-prompt-state.md)** | Inspects whether a startup tab restoration prompt is active and previews saved session tabs. |
| **[`nova.ui_set_native_dialog_file_name`](nova-ui-set-native-dialog-file-name.md)** | Fills the file path or name field of an active Win32 native file picker dialog. |
| **[`nova.webview_get_zoom`](nova-webview-get-zoom.md)** | Retrieves the current zoom factor of the target tab's WebView2 control. |
| **[`nova.webview_reset_zoom`](nova-webview-reset-zoom.md)** | Resets the target tab's WebView2 zoom factor back to the default 1.0 (100%). |
| **[`nova.webview_set_zoom`](nova-webview-set-zoom.md)** | Sets the zoom factor for a target tab's WebView2 instance. |
| **[`nova.window_get_bounds`](nova-window-get-bounds.md)** | Returns host application window boundaries (position, size) and monitor inventory metadata. |
| **[`nova.window_move`](nova-window-move.md)** | Moves the Nova application window to a monitor, by index. |
| **[`nova.window_set_size`](nova-window-set-size.md)** | Resizes the Nova application window to specified pixel width and height. |
| **[`nova.window_set_state`](nova-window-set-state.md)** | Sets host application window state: minimize, maximize, restore, or bring to foreground. |
<!-- /generated:tool-list -->

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
