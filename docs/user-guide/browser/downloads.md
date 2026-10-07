# Downloads Panel & Download Safety

> [!NOTE]
> Nova AI Workspace shows downloads in its own **Downloads** panel and asks before it saves a file that Windows could run. Agents can manage downloads through MCP tools.

---

## 1. Overview

Open Downloads to find a file, check progress or retry a failed transfer. Whether you or an agent started it, Nova provides:

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

* **Discard** refuses the download. `Escape` also discards. No default button is selected.
* **Keep** saves the file to the download folder.
* On surfaces nobody is watching, Nova refuses such downloads instead of asking.

This check identifies a runnable file type; it is not a malware verdict. **Keep** does not mean the file is safe to run.

An agent that triggers such a download can answer the same question with `nova.ui_download_security_prompt_resolve` (`keep` or `discard`). The decision is logged either way.

---

## 4. Downloads started by an agent

Agent downloads appear in the same panel. Agents can wait for completion, inspect paths and control transfers. For these interfaces, see [Downloads tools](../../mcp-reference/tools/downloads/README.md).

Private browsing does not delete files you download. Removing a list entry or clearing download history also leaves saved files on disk.

[Back to this section](README.md) · [All user guides](../README.md)
