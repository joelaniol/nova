# Downloads Management & Queue Control

Download tracking, pause/resume, security prompt resolution, and directory management.

* **Capability Bundle(s):** `app_shell_recovery`
* **Core Architecture Guide:** [Core Features: native-dialogs-and-prompts.md](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (15 Tools)

| Tool Name | Status | Description |
| :--- | :---: | :--- |
| **[`nova.downloads_auto_open_get`](nova-downloads-auto-open-get.md)** | Documented | Get the list of extensions that auto-open with the OS default app after a successful download, along with the hardcoded executa... |
| **[`nova.downloads_auto_open_set`](nova-downloads-auto-open-set.md)** | Documented | Bulk-replace the list of extensions that auto-open after download. |
| **[`nova.downloads_cancel`](nova-downloads-cancel.md)** | Documented | Cancel an active download by ID. |
| **[`nova.downloads_cancel_all`](nova-downloads-cancel-all.md)** | Documented | Cancel every non-terminal download (queued/in_progress/paused). |
| **[`nova.downloads_clear`](nova-downloads-clear.md)** | Documented | Clear download history. |
| **[`nova.downloads_list`](nova-downloads-list.md)** | Documented | List recent downloads tracked by the browser. |
| **[`nova.downloads_open_file`](nova-downloads-open-file.md)** | Documented | Open the downloaded file with the system default handler. |
| **[`nova.downloads_open_folder`](nova-downloads-open-folder.md)** | Documented | Reveal the downloaded file in Windows Explorer. |
| **[`nova.downloads_pause`](nova-downloads-pause.md)** | Documented | Pause a live WebView2-native download by ID. |
| **[`nova.downloads_pause_all`](nova-downloads-pause-all.md)** | Documented | Pause every in-progress WebView2-native download that supports pausing. |
| **[`nova.downloads_preview`](nova-downloads-preview.md)** | Documented | Open a completed download inline in a new browser tab using a file:// URL. |
| **[`nova.downloads_resume`](nova-downloads-resume.md)** | Documented | Resume a paused live WebView2-native download by ID. |
| **[`nova.downloads_resume_all`](nova-downloads-resume-all.md)** | Documented | Resume every paused download whose WebView2 operation reports CanResume=true. |
| **[`nova.downloads_retry`](nova-downloads-retry.md)** | Documented | Retry a failed download by navigating to its original URL. |
| **[`nova.downloads_wait`](nova-downloads-wait.md)** | Documented | Block until downloads reach a terminal state (completed/failed/cancelled) and return where the bytes landed. |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
