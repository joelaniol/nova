# `nova.net_monitor_report`

What a network monitor measured over a window: probe success, reachability and coverage kept apart, percentiles, RTT variation, gaps with their reason and, with a route, every hop.

> **Upcoming in 1.0.0-alpha.21:** this tool is not in a published setup yet.

---

## 1. Overview

`nova.net_monitor_report` answers **"how stable was the connection last night?"**, **"how much loss this week?"** or **"when did it drop?"** for a monitor started with [`nova.net_monitor_start`](nova-net-monitor-start.md).

* **Three numbers that are often mixed up stay apart.** `probeSuccessPct` is the share of answered test packets; `reachabilityPct` is the share of time the target counted as up (down after 3 unanswered probes in a row, up again after 2 answers; `reachabilityRule` says so in the answer); `window.coveragePct` is how much of the asked window was measured at all.
* **Gaps are named, never counted as outages.** `window.gaps` lists each with its reason: `nova_not_running`, `system_suspended`, `local_scheduler_overrun`, `unknown_process_gap`, `paused`.
* **Resolution follows the window.** `measurement.resolution` is `raw` for windows up to 6 hours within the last 14 days, `1m_rollup` up to 7 days (exact percentiles), otherwise `1h_rollup` (approximate percentiles, `percentileMethod: "histogram_approx"`). Data older than is kept shows up as `window.notRetainedBefore`.
* **Latency.** `rtt` with min, p50, p95, p99, max and `sampleCount`; `rttVariation` with the mean difference between consecutive answers and a smoothed value (`ewmaMs`, from raw rounds). This is the variation of round-trip times, not RTP jitter, which needs one-way times.
* **Route.** With a route monitor, `routes` lists each path version and `hops` gives sent, answered and loss per hop; a hop that never answered carries `lossNote: "hop_icmp_silent"` (a router that sends no ICMP, common at providers), and loss at a hop that clearly exceeds the target's loss carries `"icmp_rate_limit_likely"` - a router limiting answers to itself. Neither is lost traffic.
* **`format: "series"`** adds up to `maxPoints` time buckets with measured, lost, min, average and max; buckets without measurements are left out.
* **`limitations`** lists what the numbers cannot say. Outage and latency events are not built yet (`events_not_built`).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `monitorId` | `string` | Yes | — | ≤ 64 characters | Monitor id from nova.net_monitor_start or nova.net_monitor_list (e.g. 'mon_3f9a1c2b7d4e'). |
| `last` | `string` | No | — | ≤ 8 characters | Window up to now: '15m', '6h', '24h', '7d', up to '90d'. Default '1h'. Not with from/to. |
| `from` | `string` | No | — | ≤ 40 characters | Window start, ISO 8601 (e.g. '2026-11-07T00:00:00Z'). |
| `to` | `string` | No | — | ≤ 40 characters | Window end, ISO 8601; default now. |
| `format` | `string` | No | `"summary"` | `summary`, `series` | 'summary' (default) or 'series' (summary plus time buckets). |
| `maxPoints` | `integer` | No | `120` | 1–1000 | format='series' only: at most this many buckets. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### Last night
```json
{
  "name": "nova.net_monitor_report",
  "arguments": { "monitorId": "mon_3f9a1c2b7d4e", "last": "12h" }
}
```

### Response (shortened)
```json
{
  "structuredContent": {
    "schemaVersion": 1,
    "monitorId": "mon_3f9a1c2b7d4e",
    "window": { "requestedSeconds": 43200, "coveredSeconds": 41400, "coveragePct": 95.83,
                "gaps": [ { "from": "2026-11-07T01:10:00Z", "to": "2026-11-07T01:40:00Z", "reason": "system_suspended" } ] },
    "measurement": { "resolution": "1m_rollup", "probeType": "icmp_echo", "intervalMs": 2500, "attempted": 16560, "answered": 16497 },
    "probeSuccessPct": 99.62,
    "reachabilityPct": 99.95,
    "downSeconds": 20,
    "rtt": { "minMs": 17, "p50Ms": 21, "p95Ms": 34, "p99Ms": 61, "maxMs": 240, "sampleCount": 16497, "percentileMethod": "exact" },
    "rttVariation": { "meanAbsDeltaMs": 2.4, "ewmaMs": null, "samplePairs": 16420 },
    "limitations": ["one_way_delay_not_measured", "events_not_built", "rtt_resolution_1ms", "rtt_variation_ewma_needs_raw"]
  }
}
```

### Time buckets for a chart
```json
{
  "name": "nova.net_monitor_report",
  "arguments": { "monitorId": "mon_3f9a1c2b7d4e", "last": "7d", "format": "series", "maxPoints": 168 }
}
```

---

## 4. Operational Best Practices

* **Check `window.coveragePct` first.** A perfect `probeSuccessPct` over 10 % coverage says little.
* **Do not read a gap as an outage.** A closed Nova or a sleeping PC measured nothing.
* **Hop loss with a healthy target** is usually a router limiting ICMP answers to itself.

---

## 5. Related Tools

* [`nova.net_monitor_start`](nova-net-monitor-start.md) — Starts or resumes a monitor
* [`nova.net_monitor_list`](nova-net-monitor-list.md) — The monitors and their last 15 minutes
* [`nova.net_monitor_stop`](nova-net-monitor-stop.md) — Pauses a monitor, keeps its data
* [`nova.net_monitor_delete`](nova-net-monitor-delete.md) — Removes a monitor and its data
* [`nova.net_ping`](nova-net-ping.md) — A one-off ping or route with findings
