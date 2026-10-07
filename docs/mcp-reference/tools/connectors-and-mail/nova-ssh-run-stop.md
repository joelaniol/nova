# `nova.ssh_run_stop`

Requests termination of a background SSH session — honestly, never claiming the remote process died.

---

## 1. Overview

`nova.ssh_run_stop` ends a session started with [`nova.ssh_run_start`](nova-ssh-run-start.md). It sends KILL and tears the channel down.

* **A request, not a proof.** This **requests** termination; it is never proof the remote process died. A daemonised child or a process that ignores the signal can survive, so `descendants` is always `"unknown"`. `termination.confirmed` is true only if the server reported an exit status or signal before teardown.
* **Idempotent.** Stopping a session that is already finishing or ended is fine and does nothing new.
* **No escalation.** SSH cannot escalate TERM→KILL, so Nova sends KILL directly; the optional `signal` is recorded for honesty, not acted on as an escalation ladder.

* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `execId` | `string` | Yes | — | — | Session id from nova.ssh_run_start. |
| `signal` | `string` | No | — | — | Optional signal name hint (e.g. TERM, KILL). Nova sends KILL regardless; this is recorded for honesty, not escalation. |
| `operationId` | `string` | No | — | — | Optional idempotency key for a retried stop. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.ssh_run_stop",
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
    "stopRequested": true,
    "termination": { "confirmed": false, "signalRequested": true, "remoteProcessState": "unknown" },
    "descendants": "unknown"
  }
}
```

---

## 4. Operational Best Practices

* **Do not read `stopRequested: true` as "killed".** Confirm via `termination.confirmed` or a final `nova.ssh_run_read`.
* **Stop sessions you are done with.** It frees a session slot immediately instead of waiting for the idle cap.
* **Retrying is safe.** A second stop on an ended session is a harmless no-op.
