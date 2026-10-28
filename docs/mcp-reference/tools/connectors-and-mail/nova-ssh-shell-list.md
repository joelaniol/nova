# `nova.ssh_shell_list`

Lists the interactive terminals you own, so a lost `execId` does not leave one running until its idle timeout.

---

## 1. Overview

`nova.ssh_shell_list` returns the interactive terminals the current owner has open. Use it to recover an `execId` you lost track of before it times out, or to check how many terminals you are holding against the concurrency caps. Each row gives `execId`, `profileId`, `state` and `startedAtUtc`.

* **Owner-scoped.** You see only the terminals you opened, the same scope that guards read/send/resize/close.
* **Shell only.** This lists PTY sessions; background command sessions are listed separately by [`nova.ssh_run_list`](nova-ssh-run-list.md).

* **Core Architecture Guide:** [Interactive PTY Terminals & Screen Reconstruction](../../../core-features/connectors/ssh/interactive-pty-terminals/README.md)
* **Subsystem Overview:** [Secure Shell (SSH)](../../../core-features/connectors/ssh/README.md)

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
  "name": "nova.ssh_shell_list",
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
        "startedAtUtc": "2026-10-11T19:40:00Z"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Recover, then close.** If a terminal shows up that you no longer need, end it with [`nova.ssh_shell_close`](nova-ssh-shell-close.md).
* **Watch the caps.** Only a few sessions run at once across both the shell and command families; list and close idle ones before opening more.

---

## 5. Related Tools

* [`nova.ssh_shell_open`](nova-ssh-shell-open.md) — Opens an interactive pseudo-terminal
* [`nova.ssh_shell_read`](nova-ssh-shell-read.md) — Reads the reconstructed terminal screen
* [`nova.ssh_shell_close`](nova-ssh-shell-close.md) — Closes an owned terminal session
