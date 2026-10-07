# `nova.ssh_run_list`

Lists the background SSH sessions you own, so a lost `execId` never leaves a session running until its timeout.

---

## 1. Overview

`nova.ssh_run_list` returns the background command sessions owned by the caller. Use it to recover an `execId` you lost, or to see what is still running before you start another session (a small number run concurrently).

* **Owner-scoped.** You only see sessions you started; another owner's sessions are never listed.
* **What each row gives.** `execId`, `profileId`, `state` (`starting` / `active` / `finishing` / `ended`), `startedAtUtc`, `allowStdin` and `stdinState`.
* **Recovery.** A session whose `execId` you lost keeps running until its idle cap; list it, then read or stop it.

* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.ssh_run_list",
  "arguments": {}
}
```

### Response (shortened)
```json
{
  "structuredContent": {
    "schemaVersion": 1,
    "ok": true,
    "count": 1,
    "sessions": [
      {
        "execId": "ssh_3f9a1c22",
        "profileId": "cn_9f2c41",
        "state": "active",
        "startedAtUtc": "2026-10-07T12:00:00Z",
        "allowStdin": false,
        "stdinState": "not_enabled"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **List before starting another.** Concurrency is capped; a forgotten active session may be why a new start is refused.
* **Clean up.** Stop sessions you no longer need instead of leaving them to the idle timeout.
