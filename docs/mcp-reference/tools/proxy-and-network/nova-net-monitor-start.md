# `nova.net_monitor_start`

Starts a long-term connection monitor (like PingPlotter or Smokeping) that keeps measuring while Nova runs, or resumes a paused one.

> **Upcoming in 1.0.0-alpha.21:** this tool is not in a published setup yet.

---

## 1. Overview

`nova.net_monitor_start` answers questions such as **"does my connection drop at night?"** or **"watch the server for a few days"**. A one-off [`nova.net_ping`](nova-net-ping.md) shows the connection right now; a monitor keeps measuring and stores the history, so an agent can read it later with [`nova.net_monitor_report`](nova-net-monitor-report.md). There is nothing to poll.

* **What is measured.** One ICMP echo per `intervalMs` (default 1 s in the local network, 2 s otherwise), or with `method: "tcp"` and `port` the TCP connect time for hosts that drop ICMP. With `route: true` (interval at least 2.5 s) every hop on the path is measured too, each about every 10 seconds; the whole path is found again every 5 minutes, and a new path is accepted only after a second identical discovery.
* **Runs while Nova runs.** Also after a restart: stored monitors start again by themselves. The time Nova was closed or the PC was asleep is recorded as a gap with its reason, never as an outage.
* **Visible to the user.** While any monitor exists, Nova's toolbar shows a button with each monitor's state, the last 15 minutes and a small chart; the user can pause or delete it there.
* **No duplicates.** The same host, method and port as an existing monitor answer `status: "already_exists"` with that `monitorId`, so repeating a start after a timeout is harmless.
* **Limits.** At most 20 monitors and 35 probes per second for all of them together; a start that would exceed this answers `probe_budget_exceeded` with `freeProbesPerSecond`. A host name is looked up again every 5 minutes; a new address starts a new target epoch instead of mixing two hosts.
* **Events.** Nova notes outages, loss, high or unsteady latency and route or address changes by itself; the report lists them with their probable location. Latency events compare against what is normal for the target (a baseline that needs about an hour of clean measurement) unless you pass your own `thresholds`; `profile: "custom"` means you do and requires them.
* **`monitorId` alone** resumes a paused monitor as it was stored.
* **Sent directly from this PC**, never through the browser's proxy. No administrator rights.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `host` | `string` | No | — | ≤ 253 characters | Host name or IP address to monitor (no scheme, path or port). A name resolving to several addresses: the first IPv4 address is used; pass an IPv6 literal for an IPv6 monitor. Exactly one of host or deviceId. |
| `deviceId` | `string` | No | — | ≤ 64 characters | A device from nova.net_devices instead of host; its current address is followed when the inventory learns a new one. |
| `method` | `string` | No | `"icmp"` | `icmp`, `tcp` | 'icmp' (default) or 'tcp' (connect time to 'port', for hosts that drop ICMP; no route). |
| `port` | `integer` | No | — | 1–65535 | TCP port for method='tcp' (e.g. 443). |
| `route` | `boolean` | No | `false` | — | true: also measure every hop of the path (where loss or delay starts). Needs intervalMs >= 2500 and costs about 1.5 probes per second more. |
| `intervalMs` | `integer` | No | — | 1000–60000 | Time between rounds. Default 1000 (lan), 2000 (wan), 2500 with route; at least 1000, with route at least 2500. Longer intervals are kinder to servers that rate-limit ICMP. |
| `timeoutMs` | `integer` | No | — | 500–5000 | How long a probe may take before it counts as lost; at most intervalMs. Default 1000 (lan) or 1500. |
| `payloadBytes` | `integer` | No | `32` | 0–1472 | ICMP payload in bytes. ICMP only. |
| `profile` | `string` | No | — | `lan`, `wan`, `custom` | Sets the defaults: 'lan' (private address; 1 s, 1 s timeout; latency events from 20 ms p95, RTT variation from 5 ms), 'wan' (public address; 2 s, 1.5 s timeout; 100 ms, 20 ms), 'custom' (your own event thresholds - needs 'thresholds'). Default from the address. |
| `thresholds` | `object` | No | — | — | Your own event thresholds; each set value replaces the profile floor and the baseline rule of its kind. Without them: loss 5 %, latency max(floor, 2x baseline p95), RTT variation max(floor, 3x baseline) - the last two only once a baseline exists. |
| `thresholds.lossPct` | `number` | No | — | 0.1–50 | Loss event at this % of target probes lost (outside outages) over the loss window; closes below 40 % of it. |
| `thresholds.latencyP95Ms` | `number` | No | — | 1–10000 | Latency event when the p95 RTT of two consecutive halves (5 min, or 20 rounds at long intervals, at most 30 min each) is above this; closes when both are below 80 % of it. |
| `thresholds.rttVariationMs` | `number` | No | — | 0.1–5000 | RTT-variation event when the mean \|difference\| of consecutive RTTs in two consecutive halves is above this. |
| `label` | `string` | No | — | ≤ 80 characters | Name shown in the toolbar and list. Default: host or device name. |
| `monitorId` | `string` | No | — | ≤ 64 characters | Resume this stopped monitor as it was stored; no other argument with it. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### Watch a server and its route
```json
{
  "name": "nova.net_monitor_start",
  "arguments": { "host": "example.com", "route": true, "intervalMs": 2500, "label": "Web server" }
}
```

### Response (shortened)
```json
{
  "structuredContent": {
    "status": "started",
    "monitor": { "monitorId": "mon_3f9a1c2b7d4e", "label": "Web server", "host": "example.com", "method": "icmp", "route": true, "intervalMs": 2500, "profile": "wan" },
    "costProbesPerSecond": 1.9,
    "freeProbesPerSecond": 33.1,
    "next": "Measuring now, while Nova runs. Read nova.net_monitor_report(monitorId) later; there is nothing to poll."
  }
}
```

### A host that drops ICMP
```json
{
  "name": "nova.net_monitor_start",
  "arguments": { "host": "example.com", "method": "tcp", "port": 443 }
}
```

### Resume a paused monitor
```json
{
  "name": "nova.net_monitor_start",
  "arguments": { "monitorId": "mon_3f9a1c2b7d4e" }
}
```

---

## 4. Operational Best Practices

* **Longer intervals are kinder.** Some servers limit how many pings they answer; 2 to 5 seconds is enough to see drops and latency spikes over a night.
* **Use `route: true` only when the path matters.** It costs about 1.5 more probes per second per monitor.
* **Read the report later**, for example the next morning with `last: "12h"`; do not call the report in a loop.
* **Clean up.** A monitor runs until it is stopped or deleted; stop it when the question is answered.

---

## 5. Related Tools

* [`nova.net_monitor_report`](nova-net-monitor-report.md) — What a monitor measured over a window
* [`nova.net_monitor_list`](nova-net-monitor-list.md) — The monitors and their last 15 minutes
* [`nova.net_monitor_stop`](nova-net-monitor-stop.md) — Pauses a monitor, keeps its data
* [`nova.net_monitor_delete`](nova-net-monitor-delete.md) — Removes a monitor and its data
* [`nova.net_ping`](nova-net-ping.md) — A one-off ping or route with findings
