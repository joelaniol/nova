# Connectors

Connectors are saved connections that let an agent work with a mailbox or a remote server through Nova. Nova manages the connection, keeps stored credentials on its side and applies the access permissions you choose for each capability.

> [!IMPORTANT]
> During the public alpha, do not use connectors inside Nova's terminal yet. See the [current alpha limitations](../../../ALPHA.md).

## Choose a Connector Area

| Area | What it covers |
| :--- | :--- |
| [Mail: IMAP & SMTP](mail/README.md) | Read and organize mail with IMAP; send mail with SMTP. |
| [Secure Shell (SSH)](ssh/README.md) | Run remote commands and manage background command sessions using an SSH/SFTP connection. |
| [SSH File Transfer Protocol (SFTP)](sftp/README.md) | Transfer files and directories over SSH. |
| [File Transfer Protocol (FTP) & FTP over TLS (FTPS)](ftp-and-ftps/README.md) | Transfer files using plain FTP or TLS-protected FTP. |
| [External Model Context Protocol (MCP) Servers](external-mcp/README.md) | Register other MCP servers and call their tools. |

## How the Areas Relate

IMAP and SMTP serve different parts of one mail account. FTP and FTPS use the same FTP connector with different transport-security settings. SFTP is a separate protocol over SSH; it is not FTPS. Remote SSH commands and SFTP transfers share a connection profile and host-key trust, but perform different actions.

External MCP servers are a separate integration mechanism with their own `external_mcp` tool bundle.

## Credentials Stay in Nova

* **Write-only secrets:** A password or key passphrase is passed once (in Settings or with `nova.connector_create` / `nova.connector_update`) and stored encrypted with Windows DPAPI. The connection profile only holds a reference to it. No tool returns it — `nova.connector_list` shows the profile without the secret.
* **Copy from the Vault:** Instead of a password, `passwordFromVault` takes the id of a saved login from the [Vault](../vault-and-secrets/README.md). Nova copies the password internally after the user confirms it in a dialog; the agent never sees it.
* **SSH keys:** For SSH/SFTP connections with `authMode='private_key'`, Nova stores the path to an existing private key file and an optional passphrase; both are write-only.
* **SSH host keys:** Nova connects to an SSH/SFTP server only when its host key is trusted. Trust is given by a person in Settings ("Confirm this SSH host"), after comparing the shown fingerprint; agents cannot add or replace host keys. A changed key is reported as "SSH host key changed".

## Connections and Access

All native connector tools are in the `connector_ops` bundle.

* `nova.connector_list`: Lists connections and their access modes.
* `nova.connector_create`, `nova.connector_update`, `nova.connector_delete`: Manage connections.
* `nova.connector_probe`: Diagnose reachability, transport security and server capabilities without changing remote data.
* `nova.connector_grant_set`: Sets the access mode for one capability.
* `nova.connector_recipient_set`: Replaces the recipient allow-list of a mail account.

Local files for downloads, uploads and attachments must lie inside the Downloads folder or the current workspace project folder.

## Security & Policy Enforcement

1. **Capabilities and access modes:** Mail connections have the capabilities `read`, `organize` and `send`; SFTP and FTP connections have `read` and `full`. Each capability is set to `ask` (prompt every time), `always` or `blocked`, globally or for one workspace. An `always` grant for mail reading can be limited to specific folders and senders.
2. **Recipient allow-list:** Recipients — addresses or whole domains — on the account's allow-list can be sent to directly; every other recipient needs the user's approval in a prompt.
3. **Send limit:** By default an account sends at most 20 mails per hour (rolling window, counted per workspace). Above that, `nova.mail_send` is refused and tells the agent when it can send again.
4. **Unattended runs fail closed:** In scheduled tasks, or with `unattended=true`, a call that would need a prompt is refused instead of waiting for a person.
5. **Risky attachments:** Attachment file names are sanitized. Executable-looking attachments are saved with an added `.isolated` extension so they cannot be launched by a double-click (a separate development option can turn this off); Nova never opens or runs them.
6. **Bounded transfers:** Byte and file limits are enforced on the transfer streams themselves, not only checked beforehand.

Remote command execution also requires Nova's independent MutatingRemote policy; see the [SSH guide](ssh/README.md).

[All core features](../README.md)
