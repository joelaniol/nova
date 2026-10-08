# File Transfer Protocol (FTP) & FTP over TLS (FTPS)

FTP and FTPS share Nova's `ftp` connector. FTPS adds TLS to FTP; it is different from [SFTP over SSH](../sftp/README.md).

## Connection and Transport Security

The documented default port is 21. Match the transport mode and port to the server's configuration:

| Mode | Transport |
| :--- | :--- |
| `auto`, `start_tls` | Explicit FTPS. `auto` never downgrades to plaintext. |
| `ssl_on_connect` | Implicit FTPS. |
| `none` | Plain FTP, requiring the separate debug/legacy option and `allowInsecure=true` on each affected call. |

FTP connections have separate `read` and `full` capabilities. Credentials, access modes and unattended-call rules are described in the [Connectors overview](../README.md).

## Transfers and File Operations

* `nova.ftp_list`: List a remote directory.
* `nova.ftp_get`, `nova.ftp_put`: Download or upload one regular file as a resumable background job. Keep its `jobId` if the call returns before completion; FTP does not transfer whole directories recursively.
* `nova.ftp_transfer_status`, `nova.ftp_transfer_stop`: Read progress or stop a job. Repeating the original transfer call resumes an unfinished job.
* `nova.ftp_rename`, `nova.ftp_delete`: Rename or delete remote files.

Local transfer paths must stay inside Downloads or the current workspace project folder. An optional `maxBytes` budget limits a transfer; omitting it does not impose a caller-specified byte limit.

[FTP tool reference](../../../mcp-reference/tools/connectors-and-mail/nova-ftp-get.md) — Transfer parameters and examples.


[Connectors overview](../README.md) · [All core features](../../README.md)
