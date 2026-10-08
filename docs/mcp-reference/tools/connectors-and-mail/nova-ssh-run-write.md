# `nova.ssh_run_write`

Writes to a background SSH session's stdin with ordered, retry-safe sequencing and an honest half-close.

---

## 1. Overview

`nova.ssh_run_write` sends input to a session started with [`nova.ssh_run_start`](nova-ssh-run-start.md) with `allowStdin: true`. A successful result means the bytes were **handed to the channel**, not that the program read them.

* **Ordered and retry-safe.** `writeSequence` is a required monotone per-session integer (`1, 2, 3, …`). Repeating the last sequence is an idempotent no-op (never re-sent); a lower sequence is rejected as stale. This makes a retried write safe after a network hiccup.
* **Honest half-close.** Set `eof: true` to send SSH EOF so a command reading stdin stops waiting. After EOF no further writes are accepted (`stdinState` becomes `eof_sent`).
* **Not an escalation.** stdin had to be enabled at start; a write cannot turn it on. Writing to a session started without `allowStdin` is rejected.
* **Bounded.** `data` is UTF-8 text up to 256 KiB per call; upload larger input over SFTP and read it in the command instead.

* **Core Architecture Guide:** [Secure Shell (SSH)](../../../core-features/connectors/ssh/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `execId` | `string` | Yes | — | — | Session id from nova.ssh_run_start (must have been started with allowStdin). |
| `data` | `string` | Yes | — | — | UTF-8 text to send to stdin (max 256 KiB). May be empty when only sending EOF. |
| `eof` | `boolean` | No | `false` | — | Half-close stdin after this write (sends SSH EOF). No further writes accepted afterwards. |
| `writeSequence` | `integer` | Yes | — | ≥ 1 | Monotone per-session sequence number for ordering + idempotent retry. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.ssh_run_write",
  "arguments": {
    "execId": "ssh_3f9a1c22",
    "data": "yes\n",
    "writeSequence": 1
  }
}
```

### Response (shortened)
```json
{
  "structuredContent": {
    "schemaVersion": 1,
    "ok": true,
    "execId": "ssh_3f9a1c22",
    "stdinState": "open",
    "bytesWritten": 4,
    "applied": true,
    "duplicate": false,
    "note": "bytes_handed_to_channel_not_read_by_program"
  }
}
```

---

## 4. Operational Best Practices

* **Keep `writeSequence` monotone.** One counter per session, increment on every new write; reuse the same number only to retry the identical write.
* **A result is not a read receipt.** `bytesWritten` is what Nova handed the channel; the program may not have consumed it yet.
* **Send EOF when input is done.** A command blocked on stdin (`cat`, a prompt) only proceeds after `eof: true`.
* **Handle `stdin_not_enabled`.** If you need input, start the session with `allowStdin: true`; it cannot be enabled afterwards.
