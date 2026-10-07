# Connectors, Mail & File Transfer

IMAP/SMTP email client automation, EML exports, SFTP/FTP server operations, and credential access grants.

* **Core Architecture Guide:** [Core Features: connectors-and-protocols.md](../../../core-features/connectors-and-protocols/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

<!-- generated:tool-list (from the tool pages in this folder; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
## Tool Inventory (46 Tools)

Capability bundles of these tools: `connector_ops`.

| Tool | What it does |
| :--- | :--- |
| **[`nova.connector_create`](nova-connector-create.md)** | Creates an E-Mail account (IMAP/SMTP) or remote server connection (SFTP/FTP). |
| **[`nova.connector_delete`](nova-connector-delete.md)** | Deletes a connector profile, associated capability grants, and backing DPAPI secrets. |
| **[`nova.connector_grant_set`](nova-connector-grant-set.md)** | Sets capability access modes (ask, always, blocked) for a connector. |
| **[`nova.connector_list`](nova-connector-list.md)** | Lists configured E-Mail accounts and remote file transfer server connections. |
| **[`nova.connector_probe`](nova-connector-probe.md)** | Diagnoses a configured mail account or SFTP/FTP server: reachability, TLS, server identity, features and limits, read-only. |
| **[`nova.connector_recipient_set`](nova-connector-recipient-set.md)** | Configures recipient allow-lists for autonomous email sending without human prompts. |
| **[`nova.connector_update`](nova-connector-update.md)** | Updates configuration, endpoints, credentials, or signatures of an existing connection. |
| **[`nova.ftp_delete`](nova-ftp-delete.md)** | Deletes a remote regular file or empty directory on an FTP/FTPS server. |
| **[`nova.ftp_get`](nova-ftp-get.md)** | Downloads a remote regular file over FTP/FTPS into Downloads or the workspace. |
| **[`nova.ftp_list`](nova-ftp-list.md)** | Lists remote directory entries or inspects file metadata through an FTP/FTPS connector. |
| **[`nova.ftp_put`](nova-ftp-put.md)** | Uploads a local regular file over FTP/FTPS to a remote server. |
| **[`nova.ftp_rename`](nova-ftp-rename.md)** | Renames or moves a remote file or directory on an FTP/FTPS server. |
| **[`nova.ftp_transfer_status`](nova-ftp-transfer-status.md)** | Reports progress and result of background FTP transfers started by `nova.ftp_get` or `nova.ftp_put`. |
| **[`nova.ftp_transfer_stop`](nova-ftp-transfer-stop.md)** | Stops a running background FTP transfer softly and keeps everything for a resume. |
| **[`nova.mail_attachment_save`](nova-mail-attachment-save.md)** | Saves a specific email attachment to Downloads or the workspace directory. |
| **[`nova.mail_backup_start`](nova-mail-backup-start.md)** | Launches a background job to back up an entire mail account or specific folders. |
| **[`nova.mail_backup_status`](nova-mail-backup-status.md)** | Reports progress, downloaded message counts, and active phase of a mail backup job. |
| **[`nova.mail_backup_stop`](nova-mail-backup-stop.md)** | Gracefully stops an in-flight mail backup job, committing all downloaded messages. |
| **[`nova.mail_delete`](nova-mail-delete.md)** | Moves up to 200 messages into the account's Trash folder (non-permanent delete). |
| **[`nova.mail_draft_create`](nova-mail-draft-create.md)** | Saves an email draft to the server's Drafts folder without sending. |
| **[`nova.mail_export_eml`](nova-mail-export-eml.md)** | Exports raw RFC 822 EML files preserving complete MIME headers and original parts. |
| **[`nova.mail_folder_create`](nova-mail-folder-create.md)** | Creates a top-level personal IMAP message folder. |
| **[`nova.mail_folders`](nova-mail-folders.md)** | Lists the personal IMAP folder tree with total and unread message counts. |
| **[`nova.mail_list`](nova-mail-list.md)** | Lists bounded message metadata (headers, dates, senders) from an exact IMAP folder. |
| **[`nova.mail_mark`](nova-mail-mark.md)** | Updates seen and/or flagged status flags for up to 200 messages. |
| **[`nova.mail_move`](nova-mail-move.md)** | Moves up to 200 messages from one mail account to an exact IMAP destination folder. |
| **[`nova.mail_read`](nova-mail-read.md)** | Reads the sanitized body and attachment inventory of a specific email. |
| **[`nova.mail_search`](nova-mail-search.md)** | Searches mail metadata across the IMAP server and local encrypted search archives. |
| **[`nova.mail_send`](nova-mail-send.md)** | Sends an email with optional HTML body, CC/BCC, priority, and attachments via SMTP. |
| **[`nova.sftp_chmod`](nova-sftp-chmod.md)** | Changes the POSIX permissions of a remote file or directory over an SFTP connection. |
| **[`nova.sftp_chown`](nova-sftp-chown.md)** | Changes the owner and/or group of a remote file or directory over an SFTP connection. |
| **[`nova.sftp_delete`](nova-sftp-delete.md)** | Deletes a remote file, empty directory, or bounded directory tree over SFTP. |
| **[`nova.sftp_get`](nova-sftp-get.md)** | Downloads a remote file or directory tree of any size over SFTP into Downloads or the workspace, as a resumable background job. |
| **[`nova.sftp_list`](nova-sftp-list.md)** | Lists remote directory entries or inspects file metadata through an SFTP connector. |
| **[`nova.sftp_mkdir`](nova-sftp-mkdir.md)** | Creates a remote directory over an SFTP connection, optionally with its parent directories and POSIX permissions. |
| **[`nova.sftp_put`](nova-sftp-put.md)** | Uploads a local file or directory tree of any size over SFTP, as a resumable background job. |
| **[`nova.sftp_rename`](nova-sftp-rename.md)** | Renames or moves a remote file or directory over SFTP. |
| **[`nova.sftp_symlink`](nova-sftp-symlink.md)** | Creates a symbolic link on the server over an SFTP connection. |
| **[`nova.sftp_transfer_status`](nova-sftp-transfer-status.md)** | Reports progress and result of background SFTP transfers started by `nova.sftp_get` or `nova.sftp_put`. |
| **[`nova.sftp_transfer_stop`](nova-sftp-transfer-stop.md)** | Stops a running background SFTP transfer softly and keeps everything for a resume. |
| **[`nova.ssh_run`](nova-ssh-run.md)** | Runs shell commands on the server of an SSH/SFTP connection and reports exit status, output and timing honestly. |
| **[`nova.ssh_run_list`](nova-ssh-run-list.md)** | Lists the background SSH sessions you own, so a lost `execId` never leaves a session running until its timeout. |
| **[`nova.ssh_run_read`](nova-ssh-run-read.md)** | Reads a background SSH session's live output by independent byte offsets, non-consuming, with honest gap reporting. |
| **[`nova.ssh_run_start`](nova-ssh-run-start.md)** | Starts a background command session on an SSH/SFTP server and returns an `execId` you poll, feed and stop over time. |
| **[`nova.ssh_run_stop`](nova-ssh-run-stop.md)** | Requests termination of a background SSH session — honestly, never claiming the remote process died. |
| **[`nova.ssh_run_write`](nova-ssh-run-write.md)** | Writes to a background SSH session's stdin with ordered, retry-safe sequencing and an honest half-close. |
<!-- /generated:tool-list -->

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
