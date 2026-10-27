# `nova.ssh_shell_send`

Sends input to an interactive terminal: a named key (encoded mode-aware), literal text, a paste, or raw bytes.

---

## 1. Overview

`nova.ssh_shell_send` feeds input into a terminal opened with [`nova.ssh_shell_open`](nova-ssh-shell-open.md). The result means the bytes were **handed to the channel**, never that the remote application processed them.

* **`inputKind` decides the encoding.**
  * `key` — a named key encoded for the terminal's **current modes**, so arrow keys work in `vim`/`htop`. Names: `Enter`, `Tab`, `Escape`, `Backspace`, `Space`, `Up`, `Down`, `Left`, `Right`, `Home`, `End`, `PageUp`, `PageDown`, `Insert`, `Delete`, `F1`–`F12`, with optional `Ctrl-`/`Alt-`/`Shift-` prefixes; or a `Ctrl-`/`Alt-` single character such as `Ctrl-C` or `Ctrl-D`.
  * `text` — literal UTF-8 text typed at the cursor.
  * `paste` — UTF-8 text wrapped in bracketed-paste markers when the remote app enabled that mode.
  * `raw` — your bytes verbatim (you craft any escape sequences yourself).
* **`writeSequence` is required.** A monotone per-session integer (`1, 2, 3, …`) keeps writes ordered and retry-safe: repeating the last sequence is an idempotent no-op (never re-sent), a lower one is rejected as stale.
* **Honest `writeState`.** `transport_write_returned` = the bytes were written and flushed to the channel; `rejected` = the input controller declined it (see `reasonCode`); `duplicate` = an idempotent repeat; `outcome_unknown` = the channel write did not complete in time and the session was torn down (never auto-retry the same bytes). `remoteApplicationProcessed` is always `"unknown"`.
* **Causal gap.** `observedScreenRevision` is the screen revision at send time. A [`nova.ssh_shell_read`](nova-ssh-shell-read.md) that still shows that revision has simply not reflected your input yet — that is normal, not a failed send.
* **Ctrl-D is an ordinary key.** There is no stdin half-close; send `Ctrl-D` as a key when a program expects EOF.

* **Core Architecture Guide:** [Interactive PTY Terminals & Screen Reconstruction](../../../core-features/connectors/ssh/interactive-pty-terminals/README.md)
* **Subsystem Overview:** [Secure Shell (SSH)](../../../core-features/connectors/ssh/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `execId` | `string` | Yes | — | — | Terminal id from nova.ssh_shell_open. |
| `inputKind` | `string` | No | `"text"` | `key`, `text`, `paste`, `raw` | How to encode data: a named key, literal text, a bracketed paste, or raw bytes. |
| `data` | `string` | Yes | — | — | For 'key': the key name (e.g. 'Up', 'Enter', 'Ctrl-C'). For 'text'/'paste'/'raw': the UTF-8 content (max 256 KiB). |
| `writeSequence` | `integer` | Yes | — | ≥ 1 | Monotone per-session sequence number for ordering + idempotent retry. |
| `waitFor` | `string` | No | — | ≤ 1000 characters | Wait after sending: 'prompt' (the last line is a short line ending in $ # % or > and nothing arrives for 300 ms) or a .NET regex (multiline) matched against the output since this send. The result then carries output {text, matched, timedOut, waitedMs, leftOutBytes}. For a program that asks a question, pass a regex for the question (e.g. '\[y/N\]'). |
| `waitMs` | `integer` | No | `30000` | 0–120000 | With waitFor: how long to wait for it. On expiry output.timedOut=true with what came so far; continue with nova.ssh_shell_read(waitFor=...). |
| `maxOutputBytes` | `integer` | No | `32768` | 1024–262144 | With waitFor: bytes of output text returned; a longer output keeps its start and end (leftOutBytes). |
| `redactSecrets` | `boolean` | No | `true` | — | With waitFor: mask recognised password hashes, PEM private keys and mysql_native_password hashes in the output. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request (a named key)
```json
{
  "name": "nova.ssh_shell_send",
  "arguments": {
    "execId": "ssh_3f9a1c22",
    "inputKind": "key",
    "data": "Down",
    "writeSequence": 7
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
    "inputKind": "key",
    "writeSequence": 7,
    "bytesRequested": 3,
    "accepted": true,
    "writeState": "transport_write_returned",
    "remoteApplicationProcessed": "unknown",
    "observedScreenRevision": 42
  }
}
```

---

## 4. Operational Best Practices

* **Use `key` for special keys.** Do not hand-craft arrow sequences; `inputKind:"key"` encodes them mode-aware so they work whether or not the app is in application-cursor mode.
* **Keep `writeSequence` monotone.** Track it per terminal; reuse the last value only to safely retry the exact same send.
* **Read after you send, but expect lag.** Poll `nova.ssh_shell_read` with `sinceRevision`/`waitMs`; a brief unchanged result after a send is the normal causal gap.
* **Never log raw input you send to `sudo`/`passwd`.** Treat typed secrets as secrets.
* **`outcome_unknown` means stop.** The channel wedged and the session is tearing down; do not blindly re-send.
