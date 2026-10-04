# Downloads Panel & Download Safety

> [!NOTE]
> Nova AI Workspace shows downloads in its own **Downloads** panel and asks before it saves a file that Windows could run. Agents can manage downloads through MCP tools.

---

## 1. Overview

Downloads during agent browsing carry a specific risk: a page can start a download nobody asked for, and an agent could fetch a program file that later gets run. Nova handles this with two parts:

* the **Downloads** panel, where every download is visible and can be controlled, and
* a confirmation before a file Windows can execute is written to disk.

---

## 2. The Downloads Panel (`Ctrl+J`)

Open the panel with `Ctrl+J`, from **Menu → Downloads**, or with the **Downloads** button in the toolbar (shown while downloads are active or recent).

* **Status and progress:** each entry shows its state (**Active**, **Queued**, **Paused**, **Done**, **Failed**, **Canceled**), progress, speed and remaining time, plus which profile or sandbox it came from.
* **Actions per entry:** **Open**, **Open folder**, **Preview**, **Pause**, **Resume**, **Cancel**, **Retry**, **Remove** (removes the entry from the list; the file stays on disk) and **Details**, with **Copy URL**, **Copy path** and **Copy error**.
* **Actions for all:** **Pause all**, **Resume all**, **Cancel all**, and **Clear**, which removes completed, failed and cancelled entries from the history after a confirmation.
* **Auto-open:** in an entry's details, **Always open {type} files** opens future files of that type automatically. The list is managed under **Settings → General → Auto-open file types**. Executable types (`.exe`, `.bat`, …) cannot be added.

The download folder is set under **Settings → General → Downloads** (**Choose download folder**, **Use default Downloads folder**).

---

## 3. Executable Files: "Keep this file?"

When a download is a file type Windows can run — for example `.exe`, `.msi`, `.bat`, `.cmd`, `.ps1`, `.lnk` or `.reg` — Nova stops before saving and asks **Keep this file?**, naming the file and the site it came from.

* **Discard** is the default answer and writes nothing to disk. `Escape` also discards.
* **Keep** saves the file to the download folder.
* On surfaces nobody is watching, Nova refuses such downloads instead of asking.

Nova makes this decision itself; it does not add a separate Windows SmartScreen check on top of this question.

An agent that triggers such a download can answer the same question with `nova.ui_download_security_prompt_resolve` (`keep` or `discard`). The decision is logged either way.

---

## 4. Agent MCP Controls

Agents manage downloads with these tools:

* `nova.downloads_list` — lists active and finished downloads.
* `nova.downloads_wait` — waits until downloads reach a final state (completed, failed or cancelled) and returns the file paths.
* `nova.downloads_pause` / `nova.downloads_resume` / `nova.downloads_cancel` / `nova.downloads_retry` — control a single download; the `*_all` variants act on every download.
* `nova.downloads_open_file` / `nova.downloads_open_folder` / `nova.downloads_preview` — open or preview a finished file.
* `nova.ui_open_downloads` / `nova.ui_close_downloads` — show or hide the panel.

Full parameter lists: [Downloads tools](../mcp-reference/tools/downloads/README.md).
