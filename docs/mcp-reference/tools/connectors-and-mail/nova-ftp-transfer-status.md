# `nova.ftp_transfer_status`

Reports progress and result of background FTP transfers started by `nova.ftp_get` or `nova.ftp_put`.

---

## 1. Overview

`nova.ftp_transfer_status` reads one transfer job (`jobId`) or the 20 newest jobs of one connection (`profileId`). It never changes anything and stays usable while a Nova dialog is open. A job is one logical transfer; every resume is a new `attempt` of the same job.

`state` is one of `preparing`, `scanning`, `transferring`, `verifying`, `committing`, `stop_requested` (running) or `completed`, `stopped`, `interrupted`, `failed`, `access_revoked` (terminal). `error.code` names the cause, for example `network_retries_exhausted`, ``source_changed`, `destination_changed`, `target_full`, `remote_storage_limit`, `access_revoked` or `reauthorization_required`. An unfinished job is resumed by repeating its original `nova.ftp_get`/`nova.ftp_put` call; `nextAction` says which step comes next.

* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `jobId` | `string` | No | — | — | Job id returned by nova.ftp_get or nova.ftp_put. Pass this or profileId. |
| `profileId` | `string` | No | — | — | FTP connector id: lists its 20 newest transfer jobs. Pass this or jobId. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.ftp_transfer_status",
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
      "text": "Download tr_4f1c2a9b7d3e5f60718293a4 is interrupted (network_retries_exhausted). The connection was lost repeatedly; the transfer stopped and can be resumed."
    }
  ],
  "structuredContent": {
    "ok": false,
    "jobId": "tr_4f1c2a9b7d3e5f60718293a4",
    "attempt": 1,
    "operation": "ftp_get",
    "profileId": "conn-ftp-01",
    "state": "interrupted",
    "terminal": true,
    "running": false,
    "resumable": true,
    "progress": { "phase": "done", "bytesCompleted": 279964000000, "bytesTotal": 322122547200, "filesCompleted": 0, "filesTotal": 1 },
    "error": { "code": "network_retries_exhausted", "message": "The connection was lost repeatedly; the transfer stopped and can be resumed." },
    "suggestedPollMs": null,
    "nextAction": "repeat_the_same_call_to_resume"
  }
}
```
An unknown `jobId` is refused with `reasonCode: "job_not_found"`; passing both or neither of `jobId` and `profileId` is an invalid call.

---

## 4. Operational Best Practices

* **Poll at `suggestedPollMs`:** while `running` is true, every 5 seconds is enough; progress, rate and ETA come with each read.
* **Resume by repeating:** do not start a new transfer for an interrupted one - repeat the original call, and the part already on disk is continued after a prefix check.

---

## 5. Related Tools

* [`nova.ftp_transfer_stop`](nova-ftp-transfer-stop.md)
* [`nova.ftp_get`](nova-ftp-get.md)
* [`nova.ftp_put`](nova-ftp-put.md)
