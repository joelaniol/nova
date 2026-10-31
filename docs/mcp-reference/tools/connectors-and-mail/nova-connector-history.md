# `nova.connector_history`

Shows what agents did on a server through Nova: every writing SSH, SFTP, FTP and database call, newest first.

---

## 1. Overview

Nova keeps a local journal of each call that changes something on a server: commands run with `nova.ssh_run` or `nova.ssh_run_start`, input and stop signals sent to a running command, terminal sessions opened, typed into and closed, files uploaded, deleted, renamed or changed in mode and owner, database writes and database exports. Use it to reconstruct changes after a restore, or to see what another agent session did on the same machine.

* **What an entry holds:** time, duration, tool, outcome (`ok`, `failed`, `cancelled`), exit codes, the command or SQL statement, paths, the agent session and the client.
* **Never stored:** the content of `stdin`, of `nova.ssh_run_write` data and of text typed into a terminal. Only its size and its source are kept. Command lines, SQL and paths are masked for common credential forms before they are stored.
* **Not covered:** reads (listing, downloading, reading output), terminal resizing, mail, and anything done on the server outside Nova. An empty answer therefore does not prove the server is unchanged; the answer lists these gaps in `notCovered`.
* **Same server, other connection:** entries made through another connection, or through one that has since been deleted, with the same host and port are included and marked with `viaProfileId`.
* **Storage:** only on this PC, encrypted for the current Windows user, kept for 90 days, never sent anywhere.

* **Subsystem Overview:** [Secure Shell (SSH)](../../../core-features/connectors/ssh/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | Connector id from nova.connector_list (a deleted connector's id still finds its entries). |
| `since` | `string` | No | — | — | ISO 8601 start, inclusive (default: 7 days before until; at most 90 days back). |
| `until` | `string` | No | — | — | ISO 8601 end, exclusive (default: now). For the next page pass the previous answer's nextUntil. |
| `agentId` | `string` | No | — | — | Only entries of this agent (matches agentId or agentSessionId of an entry). |
| `limit` | `integer` | No | — | 1–500 | Maximum entries (default 100). |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.connector_history",
  "arguments": {
    "profileId": "cn_9f2c41",
    "since": "2026-10-25T00:00:00Z",
    "limit": 50
  }
}
```

### Response (shortened)
```json
{
  "structuredContent": {
    "profileId": "cn_9f2c41",
    "entries": [
      {
        "startedAtUtc": "2026-10-27T14:02:11.4810000+00:00",
        "durationMs": 1840,
        "tool": "nova.ssh_run",
        "outcome": "ok",
        "exitCodes": [0],
        "details": { "command": "systemctl reload nginx" },
        "agentSessionId": "as_51c0e2",
        "clientType": "claude-code",
        "server": "deploy@203.0.113.10:22"
      }
    ],
    "returnedCount": 1,
    "hasMore": false,
    "retentionDays": 90
  }
}
```

---

## 4. Operational Best Practices

* **Page through long periods:** while `hasMore` is `true`, call again with `until` set to the previous answer's `nextUntil`.
* **Narrow to one agent:** pass `agentId` with an agent session id from an earlier entry to see only that session's work.
* **Check the server too:** for changes made outside Nova, read the server's own logs, for example with [`nova.ssh_run`](nova-ssh-run.md).

---

## 5. Related Tools

* [`nova.connector_list`](nova-connector-list.md) — Lists connections and their ids.
* [`nova.ssh_run`](nova-ssh-run.md) — Runs commands on the server.
* [`nova.sftp_put`](nova-sftp-put.md) — Uploads files to the server.
* [`nova.db_query`](nova-db-query.md) — Queries databases over SSH without password exposure.
