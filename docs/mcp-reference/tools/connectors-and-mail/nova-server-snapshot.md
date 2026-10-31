# `nova.server_snapshot`

Records the state of a server over an SSH/SFTP connection - services, listening ports, mounts, fail2ban jails and firewall rules - so it can be compared after a change.

---

## 1. Overview

Before a firewall change, a service migration or a package upgrade you want to know afterwards what changed. `nova.server_snapshot` collects the usual lists in one call and stores them on this PC; take one before and one after the change and compare them with [`nova.server_snapshot_diff`](nova-server-snapshot-diff.md).

* **A fixed, read-only command set.** Nova runs its own commands, never the agent's: running services, enabled services, failed units, listening TCP and UDP sockets, mounts, fail2ban jails, `iptables -S` and `ip6tables -S`. Nothing on the server is changed.
* **Same approval as `nova.ssh_run`.** Running commands needs the connection's `process.exec` permission; the prompt lists the commands. The same host-key check applies.
* **Root-only parts.** fail2ban and the firewall rules need root. When the login is not root, Nova runs them through `sudo -n`, which never asks for a password; without sudo rights those parts are `unavailable`.
* **A missing part is not empty.** A part whose command is missing (no fail2ban, no systemd) or fails is `state: "unavailable"` with its exit code and error line. Output cut by the size limit is `truncated`.
* **Noise filter.** Values that change by themselves are left out and counted in `noiseFiltered`: no process IDs are read, UDP sockets in the ephemeral port range (32768 and above, DNS and NTP client sockets) and fail2ban's per-address ban rules.
* **Stored only on this PC.** Snapshots are encrypted for your Windows account, kept for 90 days and then deleted. Nothing is written on the server.
* **Labels.** `label` (for example `before-ufw`) names a snapshot. The same label can be used again; the diff then takes the newest snapshot with that label.

* **Core Architecture Guides:** [SFTP Architecture Hub](../../../core-features/connectors/sftp/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | SSH/SFTP connection id (nova.connector_list). |
| `label` | `string` | No | — | ≤ 64 characters | Optional name such as 'before-ufw' or 'after-ufw'. The same label can be used again; nova.server_snapshot_diff takes the newest snapshot with it. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.server_snapshot",
  "arguments": {
    "profileId": "cn_c0ffee1234",
    "label": "before-ufw"
  }
}
```

### Response (shortened)
```json
{
  "structuredContent": {
    "ok": true,
    "snapshotId": "snap_3f9a1c07be",
    "label": "before-ufw",
    "profileId": "cn_c0ffee1234",
    "host": "server.example.com",
    "takenAt": "2026-10-31T12:00:00+00:00",
    "sections": {
      "services_running": { "state": "ok", "count": 23, "noiseFiltered": 0 },
      "listening_tcp": { "state": "ok", "count": 4, "noiseFiltered": 0 },
      "listening_udp": { "state": "ok", "count": 1, "noiseFiltered": 2 },
      "fail2ban_jails": { "state": "unavailable", "count": 0, "noiseFiltered": 0, "exitCode": 127, "error": "bash: fail2ban-client: command not found" },
      "iptables": { "state": "ok", "count": 18, "noiseFiltered": 5 }
    },
    "retentionDays": 90,
    "remoteOutputTrust": "untrusted_remote_output",
    "recentSnapshots": [ { "id": "snap_3f9a1c07be", "label": "before-ufw", "takenAt": "2026-10-31T12:00:00+00:00" } ]
  }
}
```

---

## 4. Operational Best Practices

* **Snapshot right before the change.** A snapshot taken hours earlier also shows changes that are not yours.
* **Compare with the diff, not by reading.** The snapshot answer holds counts only; [`nova.server_snapshot_diff`](nova-server-snapshot-diff.md) lists what was added and removed.
* **Check the outside view too.** A snapshot shows what listens and which rules exist; whether a port is reachable from outside shows [`nova.net_probe`](../proxy-and-network/nova-net-probe.md).

---

## 5. Related Tools

* [`nova.server_snapshot_diff`](nova-server-snapshot-diff.md) — Compares two snapshots of one connection
* [`nova.ssh_run`](nova-ssh-run.md) — Runs the change itself
* [`nova.net_probe`](../proxy-and-network/nova-net-probe.md) — Checks from this PC which ports are reachable
