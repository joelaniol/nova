# Mail: Internet Message Access Protocol (IMAP) & Simple Mail Transfer Protocol (SMTP)

A mail connector combines IMAP for reading, organizing and backing up messages with SMTP for sending. For example, an agent can read a folder of customer inquiries while sending remains subject to separate permission.

## Connection and Security

The connector type is `mail`. The documented default ports are IMAP 993 and SMTP 587. Transport modes are `auto` (requires TLS), `ssl_on_connect` and `start_tls`; `none` is a debug option.

Unencrypted connections and accepting an invalid mail-server certificate are off by default. They require the Settings option "Allow insecure mail and FTP connections for debugging" and `allowInsecure=true` on every affected call.

Reading, organizing and sending have separate capabilities: `read`, `organize` and `send`. See the [Connectors overview](../README.md) for credential storage, access modes, recipient approval, send limits and unattended runs.

## Mail Tools

* **E-mail (`nova.mail_*`):**
  * `nova.mail_folders`, `nova.mail_folder_create`: List folders, create a folder.
  * `nova.mail_list`, `nova.mail_search`: List messages of a folder (up to 200 per call, with cursors) and search with IMAP filters.
  * `nova.mail_read`: Read a message.
  * `nova.mail_mark`, `nova.mail_move`, `nova.mail_delete`: Change flags, move or delete messages.
  * `nova.mail_draft_create`, `nova.mail_send`: Create a draft or send a mail — up to 20 recipients each in To, Cc and Bcc (50 in total), up to 20 attachments with 25 MB in total, optional HTML body, signature, priority, read-receipt request and threaded replies.
  * `nova.mail_attachment_save`: Save an attachment locally.
  * `nova.mail_export_eml`: Export one message as `.eml` or several (up to 200) as `.zip`; existing files are never overwritten.
  * `nova.mail_backup_start`, `nova.mail_backup_status`, `nova.mail_backup_stop`: Back up a mailbox in the background as local ZIP part files. The resume point survives a Nova restart, so `incremental` continues where the last backup stopped.

[Mail tool reference](../../../mcp-reference/tools/connectors-and-mail/README.md) — Parameters and examples.

[Connectors overview](../README.md) · [All core features](../../README.md)
