# `nova.net_scan`

Scans a network from this PC: finds the devices in a range, checks which TCP ports answer, and names what each device probably is, with the evidence behind it.

> **Upcoming in 1.0.0-alpha.21:** this tool is not in a published setup yet.

---

## 1. Overview

`nova.net_scan` answers **"what is in this network, and what is open on it?"** It works without administrator rights and without extra software, and every device it finds goes into Nova's network inventory ([`nova.net_devices`](nova-net-devices.md)).

* **Targets.** A CIDR range (`192.168.1.0/24`, at most `/20` = 4096 addresses), a range (`10.0.0.10-10.0.0.80` or short `10.0.0.10-80`), a single IP, a host name, or `local`: the networks of this PC's adapters that have a gateway or are a VPN. Networks that exist only inside this PC (Hyper-V or WSL switches without a gateway) are left out of `local` and listed in `context.skippedNetworks`; pass one explicitly to scan it. IPv4 needs all four numbers.
* **How devices are found.** Windows' neighbor table (finds devices that ignore ping), ping, mDNS/Bonjour, SSDP/UPnP, WS-Discovery, NetBIOS and reverse DNS. Choose with `discovery`; the default is all of them.
* **Ports.** Named port lists (`quick`, `admin`, `web`, `mail`, `nas`, `printer`, `iot`, `database`, `ot`) and your own ports or ranges. One plain TCP connect per port; nothing is logged in and no data is sent. `open` means the connection was accepted, `closed` that it was refused. No answer is counted as `no_response` and listed only as a number: without raw sockets a firewall cannot be proven, so silence says nothing.
* **What answers on a port.** Open web, https, SSH, SMB, printer (IPP) and directory (LDAP) ports are asked once what they are (`probes`, default all): the page title, the `Server` header and a login prompt's name, the certificate in front of https, the SSH banner; for SMB the dialect, whether signing is required, the computer name, domain and Windows version, and whether the outdated SMBv1 is still on; for a printer its make and model; for a directory server its host name, its domain, whether it is an Active Directory domain controller (with its functional level) and whether it is a global catalog (the directory ports are in the `admin` port set). One anonymous request per port; nothing is logged in, no password is sent and nothing is printed. The answers show in `services[]` as `protocol`, `product`, `title`, `realm` and `flags`, and they make the judgement more exact. A web port alone no longer makes a device a server: routers, printers and cameras all have a web page.
* **Judgement with evidence.** Each device gets a class (router, access point, printer, NAS, camera, TV/media player, smart-home device, Windows PC, server ...), vendor, model and operating-system family, each with a confidence and the sources it came from. The MAC vendor comes from the IEEE registry shipped with Nova.
* **Inventory and changes.** Devices are recognised again by MAC address or device UUID, also after their IP changed. The answer says which devices are new (`isNew`), which known devices were not seen (`notSeen`), and which addresses or ports changed.
* **Findings.** Risky open services are named in `findings` (for example Telnet, FTP, databases, VNC, remote desktop, directory servers, industrial control, a password prompt over unencrypted HTTP, or SMBv1 still switched on), one level more severe on a public address.
* **Long scans.** A scan that is not done within `waitSeconds` keeps running and the answer carries `scanId` with `status: "running"`. Ask again with [`nova.net_scan_status`](nova-net-scan-status.md); [`nova.net_scan_stop`](nova-net-scan-stop.md) ends it and keeps what was found.

### Approval

* **One permission for all scans.** The first scan asks you: **once**, **for this Nova session**, or **always**. "Always" is the switch **Settings > AI & agents > Access permissions > Agent may scan the network without asking**, which you can turn off there at any time.
* **Public addresses ask per range**, also with the switch on, because scanning someone else's network is a different question than scanning your own. A yes holds for that range until Nova restarts. Servers Nova already logged into through a connection are not asked about. Only scan networks you run or may test.
* **Scheduled tasks** (no one to ask) scan only with the switch on, and never public addresses; otherwise the call fails with `scan_approval_required`.

### Protecting this PC and the network

* **Bounded.** Up to 4096 addresses and 1,000,000 address × port checks per scan, 2 scans at a time, at most `timeBudgetSeconds` run time.
* **Gentle on this PC.** Each checked connection is closed at once with a reset, so Windows keeps no closed connections waiting. If this PC still runs short of sockets or local ports, Nova pauses briefly, tries again, and then stops the scan with `incompleteReason: "local_resources_exhausted"` instead of reporting silence that is its own. Lower `parallel` then.
* **Slow on public addresses.** One connection per address at a time, about 8 attempts per second overall, slower when a host stays silent. No multicast or NetBIOS leaves the local network.
* **Adjustable.** `timeoutMs`, `parallel`, `discoveryWindowMs` and `timeBudgetSeconds` can be set per call; the values used are in `context.limits`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targets` | `array` of `string` | Yes | — | 1–32 items | What to scan: CIDR ('192.168.1.0/24', at most /20), range ('10.0.0.10-10.0.0.80' or short '10.0.0.10-80'), single IP, host name (up to 8 of its addresses), or 'local' (the networks of this PC's adapters that have a gateway or are a VPN, without network and broadcast address; networks inside this PC such as Hyper-V/WSL switches are left out and listed in context.skippedNetworks - pass one explicitly to scan it). IPv4 needs all four numbers: '192.168.1' is refused, not read as 192.168.0.1. Private ranges (RFC 1918, CGNAT, link-local) need no extra approval; public ones are asked about per entry. |
| `portSets` | `array` of `string` | No | — | ≤ 16 items | Named TCP port lists, combined with 'ports'. quick (default when neither portSets nor ports is given: 20 common ports), admin (remote access, directory), web, mail, nas, printer, iot (cameras, smart home), database, ot (industrial control: S7 102, Modbus 502, EtherNet/IP 44818). The answer names the list version (context.portListVersion). An empty array with no 'ports' checks no ports - discovery only. |
| `ports` | `array` of `integer or string` | No | — | ≤ 256 items | Extra TCP ports: numbers (8123) or ranges as strings ('8000-8100'). Without portSets only these ports are checked. |
| `discovery` | `array` of `string` | No | — | ≤ 6 items | How devices are found; default all. arp (Windows' neighbor table - finds devices that ignore ping, LAN only), icmp (ping), mdns, ssdp, wsd (multicast, LAN only), netbios (Windows names). Devices of the inventory are counted as not seen only when arp and icmp are both on. Public targets never get multicast or NetBIOS. |
| `probes` | `array` of `string` | No | — | ≤ 6 items | Ask the services on open ports what they are; default all. http (web ports: Server header, page title, login realm), tls (https ports: certificate subject and issuer, then the same page), ssh (port 22: the SSH banner, e.g. software and distribution), smb (port 445: SMB dialect, signing, whether outdated SMBv1 is still on, and from the NTLM challenge the computer name, domain and Windows version - the challenge is never answered, no session is opened), ipp (port 631: printer make and model, info and name via Get-Printer-Attributes; nothing is printed), ldap (ports 389/3268, and 636/3269 over TLS: one anonymous search of the RootDSE - host name, DNS domain, Active Directory domain controller level, global catalog, directory vendor; no bind, nothing below the RootDSE is read; these ports are in portSets admin, not in the default quick). Nothing is logged in and no password is sent. The answers fill services[].protocol/product/title/realm/flags and make the device judgement more exact. An empty array checks ports only. |
| `timeoutMs` | `integer` | No | — | 200–10000 | Wait per ping and per port connect before counting no_response. Default 1500 for private ranges, 3000 when public addresses are included. Raise it for slow VPN/WAN links; lower it for a fast LAN scan. |
| `parallel` | `integer` | No | — | 1–128 | Probes at the same time. Default 64 for private ranges; for public addresses at most 4 (one connection per address). Lower it for weak devices or when a scan stopped with local_resources_exhausted. |
| `discoveryWindowMs` | `integer` | No | `3000` | 1000–10000 | How long Nova collects mDNS/SSDP/WS-Discovery answers. Raise it when sleeping devices (phones, TVs) are missing. |
| `timeBudgetSeconds` | `integer` | No | `300` | 10–3600 | Longest run time of the whole scan. When it runs out the scan ends with complete:false, incompleteReason time_budget, and keeps what it found. |
| `waitSeconds` | `integer` | No | `20` | 0–60 | How long this call waits for the result. A scan that is not done by then keeps running and the answer carries scanId with status 'running'. 0 returns at once. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### Scanning the home network
```json
{
  "name": "nova.net_scan",
  "arguments": {
    "targets": ["local"],
    "portSets": ["quick"]
  }
}
```

### Response (shortened)
```json
{
  "structuredContent": {
    "ok": true,
    "scanId": "scan_3f9a1c07be52",
    "status": "done",
    "complete": true,
    "incompleteReason": null,
    "context": {
      "targets": ["192.168.178.0/24"],
      "addressesScanned": 254,
      "skippedNetworks": ["172.20.16.0/20 (vEthernet (WSL)): no gateway - a network inside this PC (virtual switch); pass it as a target to scan it"],
      "portSets": ["quick"],
      "portCount": 20,
      "limits": { "timeoutMs": 1500, "parallel": 64, "discoveryWindowMs": 3000, "timeBudgetSeconds": 300 },
      "portChecks": 760,
      "portChecksNoResponse": 12
    },
    "devices": [
      {
        "deviceId": "dev_4f1c2a",
        "isNew": false,
        "addresses": ["192.168.178.1"],
        "macs": ["3C:A6:2F:00:00:01"],
        "names": [{ "name": "fritz.box", "source": "ptr" }],
        "class": { "value": "router_gateway", "confidence": 0.95, "sources": ["route", "ssdp", "oui"] },
        "vendor": { "value": "AVM", "confidence": 0.9, "sources": ["oui", "ssdp"] },
        "services": [
          { "transport": "tcp", "port": 80, "state": "open", "protocol": "http", "portHint": "http", "product": null, "title": "FRITZ!Box" },
          { "transport": "tcp", "port": 443, "state": "open", "protocol": "https", "portHint": "https", "product": null, "title": "FRITZ!Box" }
        ],
        "presence": "seen"
      }
    ],
    "summary": { "seen": 14, "new": 1, "notSeen": 2, "likelyGone": 0, "byClass": { "router_gateway": 1, "printer_scanner": 1, "windows_client": 4 } },
    "findings": [
      { "severity": "medium", "code": "telnet_open", "deviceId": "dev_9e0d11", "text": "192.168.178.40 (iot): Telnet (plain text, passwords readable on the network) on port 23 is open in the network." }
    ],
    "notSeen": [
      { "deviceId": "dev_77aa01", "label": "Tablet kitchen", "class": "tv_media", "missCount": 1, "presence": "not_seen" }
    ]
  }
}
```

### A VPN range with a longer timeout
```json
{
  "name": "nova.net_scan",
  "arguments": {
    "targets": ["10.8.0.0/24"],
    "portSets": ["admin", "web"],
    "timeoutMs": 4000,
    "parallel": 16
  }
}
```

---

## 4. Operational Best Practices

* **Start with `local` and `quick`.** That answers "what is in my network"; add port lists only where you need them.
* **Compare like with like.** Devices are counted as not seen only by scans with both `arp` and `icmp` on. For a before/after comparison scan the same targets with the same ports, then use `nova.net_devices(fromScanId, toScanId)`.
* **`no_response` is not "filtered".** Silence can be a firewall, a sleeping device or a lost packet. Only `open` and `closed` are facts.
* **Name the devices.** Give important devices a label with [`nova.net_devices_update`](nova-net-devices-update.md); later answers and changes are much easier to read.
* **Sleeping devices.** Phones and TVs often answer only after a few seconds; raise `discoveryWindowMs` when they are missing.
* **Stopped with `local_resources_exhausted`?** Run again with a smaller `parallel` (for example 16) or a smaller range.

---

## 5. Related Tools

* [`nova.net_devices`](nova-net-devices.md) — Reads the network inventory and the difference between two scans
* [`nova.net_scan_status`](nova-net-scan-status.md) — Progress or result of a running scan
* [`nova.net_probe`](nova-net-probe.md) — Checks the ports of one host from this PC, including an HTTP proxy
* [`nova.tls_inspect`](nova-tls-inspect.md) — Inspects the certificate and TLS setup of an open port
