# `nova.ssh_shell_close`

Closes an interactive terminal (closes the channel, typically SIGHUP-ing the remote shell). Requests termination; never a proof the remote died.

---

## 1. Overview

`nova.ssh_shell_close` ends a terminal opened with [`nova.ssh_shell_open`](nova-ssh-shell-open.md). Closing the channel typically sends `SIGHUP` to the remote shell, but this **requests** termination — it is never a proof the remote shell or its children died. A backgrounded or disowned child can survive, so `descendants` is always `"unknown"`.

* **Idempotent.** Closing an already-ended terminal is fine.
* **Always close what you opened.** A terminal you abandon runs until its idle timeout; close it so it does not hold a server session slot.
* **Honest termination.** The result's `termination` reports channel-closed / connection-lost / signal-requested facts; `remoteProcessState` is `"unknown"` unless the end was confirmed.

* **Core Architecture Guide:** [Secure Shell (SSH)](../../../core-features/connectors/ssh/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `execId` | `string` | Yes | — | — | Terminal id from nova.ssh_shell_open. |
| `operationId` | `string` | No | — | — | Optional idempotency key for a retried close. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.ssh_shell_close",
  "arguments": {
    "execId": "ssh_3f9a1c22"
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
    "state": "ended",
    "closeRequested": true,
    "descendants": "unknown"
  }
}
```

---

## 4. Operational Best Practices

* **Close before you forget the `execId`.** A lost terminal lingers until its idle cap; `nova.ssh_shell_list` recovers one you still own.
* **Exit cleanly when you can.** For a shell, sending `exit` (then reading) is gentler than a channel close; use `close` to guarantee teardown.
* **Do not treat close as a kill.** The remote process may survive; `descendants` is always `"unknown"`.
