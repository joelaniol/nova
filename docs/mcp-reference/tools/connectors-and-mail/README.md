# Connectors, Mail & File Transfer

IMAP/SMTP email client automation, EML exports, SFTP/FTP server operations, and credential access grants.

* **Capability Bundle(s):** `connector_ops`
* **Core Architecture Guide:** [Core Features: connectors-and-protocols.md](../../../core-features/connectors-and-protocols.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (31 Tools)

| Tool Name | Status | Description |
| :--- | :---: | :--- |
| **[`nova.connector_create`](nova-connector-create.md)** | Documented | Create an E-mail account or server connection. |
| **[`nova.connector_delete`](nova-connector-delete.md)** | Documented | Delete a connection and clean up its grants + backing password secret. |
| **[`nova.connector_grant_set`](nova-connector-grant-set.md)** | Documented | Set the access mode for one capability of a connection: 'ask', 'allow', or 'blocked'. |
| **[`nova.connector_list`](nova-connector-list.md)** | Documented | List configured E-Mail accounts and server connections. |
| **[`nova.connector_recipient_set`](nova-connector-recipient-set.md)** | Documented | Replace a mail account's recipient allow-list for unprompted sending. |
| **[`nova.connector_update`](nova-connector-update.md)** | Documented | Update an existing connection. |
| **[`nova.ftp_delete`](nova-ftp-delete.md)** | Documented | Delete one remote FTP/FTPS regular file or empty directory. |
| **[`nova.ftp_get`](nova-ftp-get.md)** | Documented | Download one remote regular file over FTP/FTPS into Downloads or workspace. |
| **[`nova.ftp_list`](nova-ftp-list.md)** | Documented | List one remote FTP/FTPS directory or inspect one remote regular file. |
| **[`nova.ftp_put`](nova-ftp-put.md)** | Documented | Upload one policy-approved local regular file over FTP/FTPS. |
| **[`nova.ftp_rename`](nova-ftp-rename.md)** | Documented | Rename or move one remote FTP/FTPS file or directory. |
| **[`nova.mail_attachment_save`](nova-mail-attachment-save.md)** | Documented | Save exactly one attachment identified by attachmentIndex from a message. |
| **[`nova.mail_backup_start`](nova-mail-backup-start.md)** | Documented | Back up a whole mail account (or chosen folders) as a background job. |
| **[`nova.mail_backup_status`](nova-mail-backup-status.md)** | Documented | Progress of mail backups. |
| **[`nova.mail_backup_stop`](nova-mail-backup-stop.md)** | Documented | Stop a running mail backup. |
| **[`nova.mail_delete`](nova-mail-delete.md)** | Documented | Move up to 200 messages from one mail account into its detected Trash folder. |
| **[`nova.mail_draft_create`](nova-mail-draft-create.md)** | Documented | Save one draft in the configured account's server Drafts folder. |
| **[`nova.mail_export_eml`](nova-mail-export-eml.md)** | Documented | Export original RFC 822 EML messages preserving complete MIME parts. |
| **[`nova.mail_folder_create`](nova-mail-folder-create.md)** | Documented | Create one top-level personal IMAP message folder. |
| **[`nova.mail_folders`](nova-mail-folders.md)** | Documented | List the configured account's personal IMAP folder tree with message counts. |
| **[`nova.mail_list`](nova-mail-list.md)** | Documented | List bounded message metadata from one exact IMAP folder without changing state. |
| **[`nova.mail_mark`](nova-mail-mark.md)** | Documented | Set seen and/or flagged state for up to 200 messages from one mail account. |
| **[`nova.mail_move`](nova-mail-move.md)** | Documented | Move up to 200 messages from one mail account to one exact IMAP folder. |
| **[`nova.mail_read`](nova-mail-read.md)** | Documented | Read one message body and attachments through opaque messageId. |
| **[`nova.mail_search`](nova-mail-search.md)** | Documented | Search mail metadata through the IMAP server and local encrypted archive. |
| **[`nova.mail_send`](nova-mail-send.md)** | Documented | Send an e-mail with optional HTML body, CC/BCC, attachments, and priority. |
| **[`nova.sftp_delete`](nova-sftp-delete.md)** | Documented | Delete one remote SFTP file, empty directory, or bounded directory tree. |
| **[`nova.sftp_get`](nova-sftp-get.md)** | Documented | Download one remote SFTP file or directory tree into Downloads or workspace. |
| **[`nova.sftp_list`](nova-sftp-list.md)** | Documented | List one remote SFTP directory or inspect one remote file through SFTP. |
| **[`nova.sftp_put`](nova-sftp-put.md)** | Documented | Upload one local file or bounded directory tree over SFTP. |
| **[`nova.sftp_rename`](nova-sftp-rename.md)** | Documented | Rename or move one remote SFTP path. |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
