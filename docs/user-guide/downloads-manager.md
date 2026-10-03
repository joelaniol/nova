# Downloads Manager & Safety Shield

> [!NOTE]
> Nova AI Workspace includes a sliding download drawer with integrated Windows SmartScreen protection, automated cryptographic hash verification (SHA-256), and granular agent download policies.

---

## 1. Overview

Downloading files during autonomous agent browsing is high-risk:
* Malicious websites may trigger drive-by downloads.
* Agents could inadvertently download executable binaries (`.exe`, `.msi`, `.bat`) or oversized media files that fill the local disk.

Nova's **Downloads Manager** combines a user-friendly UI panel with a strict background safety policy.

```
+--------------------------------------------------------------------+
| Downloads                                             [Clear] [X]  |
+--------------------------------------------------------------------+
| [File Icon] release-v1.4.0.zip                                     |
|             42.5 MB / 42.5 MB  *  Completed                        |
|             SHA256: 7f83b165...                                    |
|             [Show in Folder] [Verify Hash] [Delete]                |
|--------------------------------------------------------------------|
| [Shield]    setup-unknown.exe                                      |
|             Blocked by Windows SmartScreen Policy                  |
|             [Keep Anyway] [Discard]                                |
+--------------------------------------------------------------------+
```

---

## 2. Key Features

### 2.1 The Downloads Flyout Panel (`Ctrl+J`)
* Toggle the downloads drawer anytime with `Ctrl+J` or by clicking the download icon in the top toolbar.
* View real-time download speeds, remaining time estimates, and progress bars.
* Single-click actions to **Open File**, **Open Containing Folder**, or **Cancel**.

### 2.2 Windows SmartScreen & File Policy
Nova coordinates with the Windows security architecture:
* Executable files are held in a staging area until verified.
* If a file trigger originates from an automated agent action, Nova checks the **Download Security Policy**:
  * Safe file extensions (PDF, CSV, JSON, PNG, TXT) are permitted according to user settings.
  * Executable or script formats require explicit operator confirmation before disk persistence.

### 2.3 Automated Checksum Verification
* For developers downloading releases, ISOs, or SDK packages:
* Right-click any completed download $ightarrow$ select **Verify SHA-256 Hash**.
* Paste the expected checksum; Nova validates the file on disk and displays a clear green confirmation or red discrepancy warning.

---

## 3. Agent MCP Controls

Agents manage downloads using programmatic tools:
* `nova.downloads_list`: Lists active and finished download items.
* `nova.downloads_wait`: Pauses agent execution until a designated download finishes and file locks release.
* `nova.downloads_cancel` / `pause` / `resume`: Controls transfer state.
