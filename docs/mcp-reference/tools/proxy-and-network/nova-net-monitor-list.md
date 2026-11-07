# `nova.net_monitor_list`

Lists the network monitors with their state, the last 15 minutes, disk size and the free probe budget.

> **Upcoming in 1.0.0-alpha.21:** this tool is not in a published setup yet.

---

## 1. Overview

`nova.net_monitor_list` shows what is being monitored right now. It reads memory and the local file and sends nothing.

* **`state`** per monitor: `running`, `starting`, `target_down`, `measurement_degraded` (rounds missed their slot or storage fell behind) or `stopped`.
* **`last15m`**: measured probes, `probeSuccessPct`, `lossPct`, `p50Ms`, `p95Ms`, `overruns` and `hopProbesNotMeasured` (hop probes skipped to give way to other probes; never counted as loss).
* **Size**: stored rounds and summaries and an approximate byte count, which is what deleting the monitor frees.
* **`freeProbesPerSecond`**: how much room is left for new monitors.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `monitorId` | `string` | No | — | ≤ 64 characters | Only this monitor. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

```json
{
  "name": "nova.net_monitor_list",
  "arguments": {}
}
```

---

## 4. Related Tools

* [`nova.net_monitor_start`](nova-net-monitor-start.md) — Starts or resumes a monitor
* [`nova.net_monitor_report`](nova-net-monitor-report.md) — What a monitor measured over a window
* [`nova.net_monitor_stop`](nova-net-monitor-stop.md) — Pauses a monitor, keeps its data
* [`nova.net_monitor_delete`](nova-net-monitor-delete.md) — Removes a monitor and its data
* [`nova.net_ping`](nova-net-ping.md) — A one-off ping or route with findings
