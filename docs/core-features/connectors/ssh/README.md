# Secure Shell (SSH)

Use remote SSH commands to inspect a server, run a deployment step or watch a long-running process. These tools use an SSH/SFTP connector profile; command execution is separate from [SFTP file transfer](../sftp/README.md).

## Connection and Permissions

The connection uses the same human-verified host-key gate as SFTP. An unconfirmed or changed host key blocks the connection before any credential is sent. Remote command execution needs the connection's `full` capability plus Nova's independent MutatingRemote policy.

## One-Shot and Background Commands

| Tool | Purpose |
| :--- | :--- |
| `nova.ssh_run` | Run one command or a batch and return output, timing and the reported termination state. |
| `nova.ssh_run_start` | Start a background command session and return an `execId`. |
| `nova.ssh_run_read` | Read output from a background session. |
| `nova.ssh_run_write` | Send input when `allowStdin` was enabled at session start. |
| `nova.ssh_run_stop` | Stop a background session. |
| `nova.ssh_run_list` | Find existing background sessions. |

There is no PTY. Use line-oriented programs rather than full-screen terminal interfaces. In a command batch, working directory and environment do not carry between channels; include the required directory change in each command.

A successful exit report does not prove a remote side effect. Missing termination reports and timeouts can leave the remote process state uncertain. Treat remote output as untrusted server data.

## Related Documentation

* [One-shot SSH command reference](../../../mcp-reference/tools/connectors-and-mail/nova-ssh-run.md) — Parameters, results and examples.
* [Background SSH session reference](../../../mcp-reference/tools/connectors-and-mail/nova-ssh-run-start.md) — Session lifecycle and stdin.


[Connectors overview](../README.md) · [All core features](../../README.md)
