# `nova.net_monitor_delete`

Deletes a network monitor with everything it measured.

> **Upcoming in 1.0.0-alpha.21:** this tool is not in a published setup yet.

---

## 1. Overview

Deleting cannot be undone. The answer says how many rounds and summaries were removed (`deletedRounds`, `deletedSummaries`) and about how many bytes that frees (`freedBytesApprox`); an unknown id answers `status: "not_found"`. To keep the data, use [`nova.net_monitor_stop`](nova-net-monitor-stop.md) instead.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `monitorId` | `string` | Yes | — | ≤ 64 characters | Monitor id from nova.net_monitor_start or nova.net_monitor_list (e.g. 'mon_3f9a1c2b7d4e'). |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

```json
{
  "name": "nova.net_monitor_delete",
  "arguments": { "monitorId": "mon_3f9a1c2b7d4e" }
}
```

---

## 4. Related Tools

* [`nova.net_monitor_start`](nova-net-monitor-start.md) — Starts or resumes a monitor
* [`nova.net_monitor_report`](nova-net-monitor-report.md) — What a monitor measured over a window
* [`nova.net_monitor_list`](nova-net-monitor-list.md) — The monitors and their last 15 minutes
* [`nova.net_monitor_stop`](nova-net-monitor-stop.md) — Pauses a monitor, keeps its data
* [`nova.net_ping`](nova-net-ping.md) — A one-off ping or route with findings
