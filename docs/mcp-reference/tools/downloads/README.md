# Downloads Management & Queue Control

Download tracking, pause/resume, security prompt resolution, and directory management.

* **Core Architecture Guide:** [Core Features: native-dialogs-and-prompts.md](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

<!-- generated:tool-list (from the tool pages in this folder; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
## Tool Inventory (15 Tools)

Capability bundles of these tools: `app_shell_recovery`.

| Tool | What it does |
| :--- | :--- |
| **[`nova.downloads_auto_open_get`](nova-downloads-auto-open-get.md)** | Retrieves the list of file extensions configured to open automatically upon download completion. |
| **[`nova.downloads_auto_open_set`](nova-downloads-auto-open-set.md)** | Bulk-replaces the list of file extensions that auto-open with the OS default application. |
| **[`nova.downloads_cancel`](nova-downloads-cancel.md)** | Cancels an active in-progress or queued download by ID. |
| **[`nova.downloads_cancel_all`](nova-downloads-cancel-all.md)** | Cancels every non-terminal download currently queued, in progress, or paused. |
| **[`nova.downloads_clear`](nova-downloads-clear.md)** | Clears terminal download history from the UI and persistent storage. |
| **[`nova.downloads_list`](nova-downloads-list.md)** | Lists recent downloads tracked by the browser with status, progress, speed, and error categorization. |
| **[`nova.downloads_open_file`](nova-downloads-open-file.md)** | Opens a completed download using the operating system default application. |
| **[`nova.downloads_open_folder`](nova-downloads-open-folder.md)** | Reveals the downloaded file in Windows Explorer with the item selected. |
| **[`nova.downloads_pause`](nova-downloads-pause.md)** | Pauses an active WebView2-native download by ID. |
| **[`nova.downloads_pause_all`](nova-downloads-pause-all.md)** | Pauses all in-progress WebView2-native downloads that support pausing. |
| **[`nova.downloads_preview`](nova-downloads-preview.md)** | Opens a completed download inline in a new browser tab using a secure file:// URL. |
| **[`nova.downloads_resume`](nova-downloads-resume.md)** | Resumes a paused live WebView2-native download by ID. |
| **[`nova.downloads_resume_all`](nova-downloads-resume-all.md)** | Resumes all paused downloads, and interrupted ones that can continue where they stopped, when their underlying WebView2 operation supports resumption. |
| **[`nova.downloads_retry`](nova-downloads-retry.md)** | Retries a failed download by re-navigating to its original URL. |
| **[`nova.downloads_wait`](nova-downloads-wait.md)** | Blocks until downloads reach a terminal state (completed, failed, or cancelled) and returns disk file paths. |
<!-- /generated:tool-list -->

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
