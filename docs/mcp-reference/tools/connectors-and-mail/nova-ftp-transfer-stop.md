# `nova.ftp_transfer_stop`

Stops a running background FTP transfer softly and keeps everything for a resume.

---

## 1. Overview

`nova.ftp_transfer_stop` asks a running job from `nova.ftp_get`/`nova.ftp_put` to stop. The job writes a checkpoint, keeps the open file as a resumable part and ends with `state: "stopped"`; finished files stay committed and nothing is deleted. It stays usable while a Nova dialog is open. A job that has already ended is reported as `status: "not_running"` with `ok: false`. Repeating the original transfer call later resumes the job.

* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `jobId` | `string` | Yes | — | — | Job id returned by nova.ftp_get or nova.ftp_put. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.ftp_transfer_stop",
  "arguments": {
    "jobId": "tr_4f1c2a9b7d3e5f60718293a4"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Stop requested for tr_4f1c2a9b7d3e5f60718293a4: the current file is checkpointed and kept as a resumable part; finished files stay committed."
    }
  ],
  "structuredContent": {
    "ok": true,
    "jobId": "tr_4f1c2a9b7d3e5f60718293a4",
    "status": "stop_requested",
    "state": "stop_requested",
    "nextAction": "poll_ftp_transfer_status_until_terminal"
  }
}
```

---

## 4. Operational Best Practices

* **Stop is soft:** wait for `state: "stopped"` in `nova.ftp_transfer_status` before relying on the part being closed.
* **Paths stay locked while a job runs:** `nova.ftp_delete`/`nova.ftp_rename` on a path the job uses are refused with `path_busy` until it has stopped.

---

## 5. Related Tools

* [`nova.ftp_transfer_status`](nova-ftp-transfer-status.md)
* [`nova.ftp_get`](nova-ftp-get.md)
* [`nova.ftp_put`](nova-ftp-put.md)
