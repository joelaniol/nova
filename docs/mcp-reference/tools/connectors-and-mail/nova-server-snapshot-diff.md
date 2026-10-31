# `nova.server_snapshot_diff`

Compares two stored snapshots of one connection and lists, per part, what was added and what was removed.

---

## 1. Overview

`nova.server_snapshot_diff` reads two snapshots taken with [`nova.server_snapshot`](nova-server-snapshot.md) from this PC and compares them. It does not contact the server.

* **By id or label.** `a` (the earlier snapshot) and `b` (the later one) are a `snapshotId` or a label; a label means the newest snapshot with it.
* **Added and removed per part.** For each part that differs, the answer lists `added` and `removed` items with their full counts, for example a service that stopped, a port that now listens or a firewall rule that is gone. Parts without a difference are named in `unchangedSections`.
* **Unreadable is not changed.** If a part could not be read in one of the snapshots, it is listed with `comparable: false`. That says nothing about the server; read it again or check by hand.
* **Long lists.** `maxItems` (default 100) limits the listed items per part and side; `addedCount` and `removedCount` are always complete, and `truncated` says when items were left out.
* **Unknown reference.** A reference that matches no snapshot fails with `snapshot_not_found` and lists the connection's snapshots.

* **Core Architecture Guides:** [SFTP Architecture Hub](../../../core-features/connectors/sftp/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | SSH/SFTP connection id the snapshots belong to. |
| `a` | `string` | Yes | — | — | Earlier snapshot: snapshotId or label. |
| `b` | `string` | Yes | — | — | Later snapshot: snapshotId or label. |
| `maxItems` | `integer` | No | `100` | 1–1000 | Most added/removed items listed per part; the counts are always complete. Default 100. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.server_snapshot_diff",
  "arguments": {
    "profileId": "cn_c0ffee1234",
    "a": "before-ufw",
    "b": "after-ufw"
  }
}
```

### Response (shortened)
```json
{
  "structuredContent": {
    "ok": true,
    "a": { "id": "snap_3f9a1c07be", "label": "before-ufw", "takenAt": "2026-10-31T12:00:00+00:00" },
    "b": { "id": "snap_81d2e0aa45", "label": "after-ufw", "takenAt": "2026-10-31T12:06:10+00:00" },
    "changed": true,
    "sections": {
      "iptables": {
        "stateA": "ok", "stateB": "ok", "comparable": true,
        "added": ["-A ufw-user-input -p tcp --dport 443 -j ACCEPT"],
        "removed": ["-A ufw-user-input -p tcp --dport 8080 -j ACCEPT"],
        "addedCount": 1, "removedCount": 1, "truncated": false
      }
    },
    "unchangedSections": ["services_running", "services_enabled", "units_failed", "listening_tcp", "listening_udp", "mounts", "fail2ban_jails", "ip6tables"],
    "remoteOutputTrust": "untrusted_remote_output"
  }
}
```

---

## 4. Operational Best Practices

* **Read `comparable` first.** A part that became `unavailable` (for example because sudo rights changed) shows every item as removed; that is no change on the server.
* **Use labels for repeated work.** Taking `before` and `after` again on the next change keeps the call the same; the newest snapshot with each label is used.

---

## 5. Related Tools

* [`nova.server_snapshot`](nova-server-snapshot.md) — Records the state to compare
* [`nova.net_probe`](../proxy-and-network/nova-net-probe.md) — Checks from this PC which ports are reachable
