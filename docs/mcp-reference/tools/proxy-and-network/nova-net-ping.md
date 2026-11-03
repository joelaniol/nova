# `nova.net_ping`

Ping, traceroute in rounds (like mtr or PingPlotter), TCP ping and a Path-MTU check from this PC, with findings that say what the numbers mean.

> **Upcoming in 1.0.0-alpha.21:** this tool is not in a published setup yet.

---

## 1. Overview

`nova.net_ping` answers questions such as **"is the server reachable?"**, **"where on the route is the packet loss?"**, **"which hop is slow?"** and **"is the MTU on my VPN or PPPoE line too small?"**. It needs no extra software and no administrator rights.

* **Ping.** By default 10 ICMP echoes, one per second, with loss, min/avg/max/last, standard deviation and RTT variation.
* **Route in rounds (`route: true`).** The first round finds the path with rising TTL; every later round asks each hop again and sends one echo to the target. Each hop gets its loss, times and the routers that answered, with their reverse names. Unlike `ping.exe`-based tools, the times at intermediate hops are real values, not 0.
* **TCP ping (`method: "tcp"`, `port`).** The time until a TCP connection is established, for hosts that drop ICMP. It is not comparable with ICMP times (`comparableToIcmpRtt: false`); a refused connection still means the host answered.
* **Path-MTU (`mtuDiscovery: true`).** Finds the largest IPv4 packet that reaches the target with the Don't-Fragment bit. The result says whether a router confirmed the limit (`confirmed`) or larger packets only got no answer (`likely`).
* **Findings, not just numbers.** Every finding has a `confidence` (`observed`, `likely`, `inconclusive`) and a `location` (`local_network`, `hop`, `target`, `unknown`):
  * Loss only at a middle hop while later hops answer is a router that answers ICMP to itself slowly or rarely, not loss on the path.
  * A slow hop that later hops do not inherit is slow at answering ICMP itself; traffic through it is not delayed.
  * A silent hop, a silent gateway or a silent end of the trace is not an outage.
  * Several routers at one hop is load balancing, not a route change.
  * Loss is tied to a section of the route only when it happens in the same rounds as the loss at the target, and then only as `likely`.
* **What it cannot show** is listed in `limitations`: RTT differences between hops are not link latencies, and the way back can differ from the way there.
* **Sent directly from this PC** (`route: "direct"`), never through the browser's proxy. At most 20 probes per second across all calls.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `host` | `string` | Yes | — | ≤ 253 characters | Host name or IP address to measure (e.g. 'example.com', '192.168.1.1', '2001:db8::1', 'fe80::1%12' with zone). No scheme, path or port. A name is resolved once; the first address (of the chosen family) is used for the whole run. |
| `method` | `string` | No | `"icmp"` | `icmp`, `tcp` | 'icmp' (default): ICMP echo, also for route and mtuDiscovery. 'tcp': time until a TCP connection to 'port' is established, for hosts that drop ICMP; no route, no packet size. |
| `port` | `integer` | No | — | 1–65535 | TCP port for method='tcp' (e.g. 443, 22). Not used with ICMP. |
| `count` | `integer` | No | `10` | 1–100 | Number of echoes or connects (default 10, up to 100); with route=true the number of rounds (up to 30). Under 20 samples loss percentages are rough (sampleQuality='small'). |
| `intervalMs` | `integer` | No | `1000` | 1000–10000 | Time from the start of one echo (or round) to the next, in milliseconds. Default 1000. |
| `route` | `boolean` | No | `false` | — | true: traceroute/MTR rounds - every hop to the target is measured in each round. Only with method='icmp'. |
| `maxHops` | `integer` | No | `30` | 1–64 | Only with route=true: highest TTL tried. Default 30. |
| `packetSize` | `integer` | No | `32` | 0–1472 | ICMP payload in bytes (like ping -l), default 32. IPv4 up to 1472 (a 1500-byte packet), IPv6 up to 1452. |
| `dontFragment` | `boolean` | No | `false` | — | IPv4 ping only: set the Don't-Fragment bit (like ping -f); a too large packet then answers packet_too_big. |
| `mtuDiscovery` | `boolean` | No | `false` | — | IPv4 only: search the largest packet that reaches the target unfragmented (binary search with the Don't-Fragment bit, at most 12 sizes). The result says whether a router confirmed it ('packet too big') or sizes only timed out. |
| `timeoutMs` | `integer` | No | `2000` | 500–5000 | How long to wait for each echo or connect. Default 2000. |
| `family` | `string` | No | `"auto"` | `auto`, `ipv4`, `ipv6` | Which address of a name to use: 'auto' (the first one Windows returns), 'ipv4' or 'ipv6'. |
| `includeProbes` | `boolean` | No | `false` | — | true: also return every single probe (round, ttl, time, status, answering address, RTT), e.g. to correlate losses yourself. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### Route to a server
```json
{
  "name": "nova.net_ping",
  "arguments": { "host": "example.com", "route": true, "count": 10 }
}
```

### Response (shortened)
```json
{
  "structuredContent": {
    "ok": true,
    "host": "example.com",
    "route": "direct",
    "mode": "route",
    "metric": "icmp_echo_rtt",
    "destination": { "selectedAddress": "203.0.113.7", "addressFamily": "ipv4" },
    "source": { "hasRoute": true, "address": "192.168.1.20", "interface": "Ethernet" },
    "target": { "sent": 10, "received": 10, "lossPct": 0, "minMs": 21, "avgMs": 23.4, "maxMs": 31 },
    "targetReached": true,
    "traceComplete": true,
    "targetHop": 9,
    "hops": [
      { "hop": 1, "addresses": [ { "address": "192.168.1.1", "name": "router.lan", "count": 10 } ], "lossPct": 0, "avgMs": 1 },
      { "hop": 4, "addresses": [ { "address": "198.51.100.9", "count": 4 } ], "lossPct": 60, "avgMs": 14 }
    ],
    "flowConsistency": "unverified",
    "sampleQuality": "small",
    "findings": [
      { "severity": "info", "code": "intermediate_reply_suppression_likely", "confidence": "likely", "location": "hop", "hop": 4,
        "text": "Hop 4 answered only 40 % of its probes, while later hops and the target answer more: the router deprioritises ICMP to itself. Not loss on the path." }
    ],
    "limitations": ["RTT differences between hops are not link latencies.", "..."]
  }
}
```

### A host that drops ICMP
```json
{
  "name": "nova.net_ping",
  "arguments": { "host": "example.com", "method": "tcp", "port": 443 }
}
```

### Is the MTU too small?
```json
{
  "name": "nova.net_ping",
  "arguments": { "host": "example.com", "mtuDiscovery": true }
}
```

---

## 4. Operational Best Practices

* **Read `findings`, not the loss column.** A hop with 60 % loss and a target with 0 % loss is a normal picture on the internet.
* **Take enough samples.** Under 20 echoes the result says `sampleQuality: "small"`; a single lost echo is then already 10 %. For a flaky line use `count: 30` with `route: true`, or `count: 100` for a plain ping.
* **No answer to ICMP is not "down".** If `target_icmp_silent` appears, check a service port with `method: "tcp"`.
* **`includeProbes: true`** returns every single probe with round, TTL and time, to line up losses yourself.

---

## 5. Related Tools

* [`nova.net_probe`](nova-net-probe.md) — Checks whether the ports of the host are reachable
* [`nova.net_dns`](nova-net-dns.md) — Looks up the DNS records of the host
* [`nova.net_scan`](nova-net-scan.md) — Finds the devices of a network and what they are
