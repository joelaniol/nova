# SSH File Transfer Protocol (SFTP)

Use an SFTP connector to list, download, upload and manage files on a remote server over SSH. SFTP supports files and whole directories; it is separate from FTP and FTPS.

## Connection and Trust

The connector type is `sftp`, with SSH transport (`auto`) and default port 22. Password authentication and an existing private key with an optional passphrase are supported. A person must confirm the server's host-key fingerprint in Settings; agents cannot add or replace trusted host keys. An unconfirmed or changed key blocks the connection before credentials are sent.

File operations use the connection's `read` or `full` capability. The same profile can also serve [remote SSH commands](../ssh/README.md), which require `full` and the independent MutatingRemote policy.

## Transfers and File Operations

* `nova.sftp_list`: List a remote directory.
* `nova.sftp_get`, `nova.sftp_put`: Download or upload files and directories (`recursive=true`) as resumable background jobs. A call returns a `jobId` when the transfer outlasts `wait`.
* `nova.sftp_transfer_status`, `nova.sftp_transfer_stop`: Read progress or pause a transfer. Repeating its original call resumes it.
* `nova.sftp_rename`, `nova.sftp_delete`: Rename or delete remote files.
* `nova.sftp_mkdir`, `nova.sftp_symlink`: Create remote directories or symbolic links.
* `nova.sftp_chmod`, `nova.sftp_chown`: Change remote file permissions or ownership.

Local transfer paths must stay inside Downloads or the current workspace project folder. See the [Connectors overview](../README.md) for credentials and access permissions.

[SFTP tool reference](../../../mcp-reference/tools/connectors-and-mail/nova-sftp-get.md) — Transfer parameters and examples.


[Connectors overview](../README.md) · [All core features](../../README.md)
