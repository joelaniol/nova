# Network Discovery & Device Inventory Architecture

Modern enterprise environments, cloud VPCs, and home offices host heterogeneous device ecosystems: routers, switches, NAS appliances, IoT sensors, hypervisors, and domain controllers. Understanding what is running on a network is the foundational prerequisite for infrastructure security, automated monitoring, and reliable operational administration.

Nova AI Workspace includes a native, non-destructive network scanner ([`nova.net_scan`](../../../mcp-reference/tools/proxy-and-network/nova-net-scan.md)) and persistent device inventory engine ([`nova.net_devices`](../../../mcp-reference/tools/proxy-and-network/nova-net-devices.md)). Unlike conventional port scanners that require root or administrative privileges, deploy invasive kernel drivers (e.g. WinPcap or Npcap), or blindly guess passwords, Nova operates entirely from standard user-mode processes using a multi-probe evidence engine and strict security boundaries.

---

## 1. High-Level Architecture & Evidence Pipeline

Nova separates **raw observation** from **interpretative classification**. Rather than deciding a device's identity based on a single open port, Nova gathers multiple independent observations across the network stack and feeds them into a unified evidence evaluation engine:

```mermaid
flowchart TD
    subgraph Targets ["Target Definition & Scoping"]
        InputTarget["targets: 'local', CIDR ('192.168.1.0/24'), or IP Range"]
        BoundaryGate{"Target Boundary Gate<br/>(Private vs. Public)"}
        PrivatePerm["Private Subnets:<br/>Standard Agent Permission"]
        PublicPerm["Public Addresses:<br/>Mandatory User Dialog Approval"]
    end

    subgraph ProbingEngines ["User-Mode Multi-Probe Engine"]
        ArpProbe["Windows Neighbor Table (ARP / IPv6 Neighbor)"]
        IcmpProbe["ICMP Echo Probe"]
        TcpSweep["User-Mode TCP Connect (RST Cleanup)"]
        MulticastListen["Passive Multicast Listener (mDNS, SSDP, WSD)"]
        AppProbes["Application Banners & Handshakes<br/>(HTTP, TLS, SSH, SMB, IPP, LDAP, NTP, SNMP)"]
    end

    subgraph EvidenceEngine ["Evidence Evaluation & Inference"]
        RawObservations["Raw Observation Ledger<br/>(protocol, port, payload, timing)"]
        ConfidenceScorer["Multi-Factor Confidence Scorer<br/>(Separate: Class, Vendor, OS Family)"]
        RiskAnalyzer["Security & Hygiene Analyzer<br/>(Cleartext, weak crypto, clock drift)"]
    end

    subgraph InventoryStorage ["Persistent Inventory Storage"]
        DbStore[("netmonitor.db<br/>(SQLite Local Store)")]
        IdentityTracker["Identity Key Engine<br/>(MAC, SSH SPKI, UPnP UUID, TLS SPKI)"]
        PresenceReconciler["Presence State Engine<br/>(seen, new, not_seen, likely_gone)"]
    end

    InputTarget --> BoundaryGate
    BoundaryGate -->|"Private (RFC 1918 / CGNAT / Link-Local)"| PrivatePerm --> ProbingEngines
    BoundaryGate -->|"Public Range"| PublicPerm --> ProbingEngines

    ArpProbe --> RawObservations
    IcmpProbe --> RawObservations
    TcpSweep --> RawObservations
    MulticastListen --> RawObservations
    AppProbes --> RawObservations

    RawObservations --> ConfidenceScorer
    RawObservations --> RiskAnalyzer
    ConfidenceScorer --> IdentityTracker
    RiskAnalyzer --> IdentityTracker

    IdentityTracker --> PresenceReconciler
    PresenceReconciler --> DbStore
```

---

## 2. The Multi-Probe Evidence Engine

A single open port (such as TCP 80 or 443) does not prove that a host is a web server: routers, network printers, IP cameras, switches, and NAS appliances almost universally expose web management interfaces. Nova's evidence engine queries open ports with targeted, non-destructive application probes to observe factual properties:

| Discovery / Probe Source | Transport & Port | Observed Attributes & Evidence Extraction | Diagnostic Weight |
| :--- | :--- | :--- | :--- |
| **Neighbor Table (ARP / IPv6)** | User-mode API (`GetIpNetTable2`) | Physical MAC address, IPv4-to-IPv6 link correlation, interface index. Proves existence even if ICMP ping is blocked. | **Definitive** for LAN presence & MAC |
| **IEEE OUI Registry** | Shipped offline database | Resolves the vendor prefix of physical MAC addresses (e.g. `3C:A6:2F` $\rightarrow$ AVM). Locally administered (randomized) MACs are excluded from vendor tagging. | **Medium** for hardware vendor |
| **ICMP Echo** | Local ICMP API | Host responsiveness, round-trip latency, IPv4/IPv6 reachability. | **Definitive** for active layer-3 responsiveness |
| **User-Mode TCP Connect** | TCP handshake | `open` (SYN-ACK received), `closed` (RST received), or `no_response` (timeout). Connections are immediately terminated via TCP RST to prevent `TIME_WAIT` socket buildup. | **Definitive** for port reachability |
| **UPnP / SSDP Discovery** | UDP 1900 | Multicast `M-SEARCH` response and device description XML: Manufacturer, device friendly name, model name, model number, device type URI, unique device UUID. | **Very High** for device model & class |
| **WS-Discovery** | UDP 3702 | SOAP `Probe` and XML metadata exchange: device categories, endpoint references, printer/scanner capabilities. | **Very High** for Windows clients & printers |
| **mDNS / DNS-SD** | UDP 5353 | Service announcements (`_services._dns-sd._udp.local`): `_ipp._tcp` (printers), `_smb._tcp` (storage), `_airplay._tcp`, `_googlecast._tcp`, `_hap._tcp` (smart home). | **High** for device category & capabilities |
| **Printer Attributes (IPP)** | TCP 631 | Internet Printing Protocol `Get-Printer-Attributes` query: extracts printer manufacturer, exact model string, supported page formats, and firmware version without printing a byte. | **Very High** for printers and multifunction devices |
| **SMB Negotiation** | TCP 445 | SMB-2/3 dialect negotiation and unauthenticated NTLM challenge inspection: Server NetBIOS name, Active Directory domain name, Windows build number, SMB signing requirements, and SMBv1 legacy enablement. | **High** for Windows servers, domain members, and NAS |
| **SSH Server Banner** | TCP 22 | Protocol version string, server software package (e.g. OpenSSH, Dropbear), operating system/distribution indicators (e.g. `Debian-10`, `Ubuntu`), and server host key fingerprints. | **Medium–High** for Linux/BSD and network appliances |
| **Directory Services (LDAP)** | TCP 389, 636, 3268, 3269 | Anonymous RootDSE query: Active Directory domain controller status, forest functional level, domain DNS name, LDAP service vendor. (No bind attempted; restricted to RootDSE). | **Very High** for domain controllers and identity servers |
| **TLS Analysis & ALPN** | HTTPS / TLS ports | Server certificate Subject, SANs, Issuer, expiration date, self-signed status, and ALPN negotiated protocols (e.g. `h2`, `http/1.1`). | **Medium** for certificates & virtual host names |
| **HTTP Surface Probing** | HTTP ports | HTTP response status, `Server` header, `<title>` DOM tag, authentication realm name, and redirect location. | **Medium** for administrative web consoles |
| **NTP Clock Verification** | UDP 123 | Standard client query (Mode 3): Stratum, reference ID, round-trip latency, and `clockOffsetMs` relative to the local PC's clock. (Control/Monlist modes are never invoked). | **High** for clock drift and Kerberos/TLS risks |
| **SNMP Probing** | UDP 161 | Targeted single-OID GetRequest (`sysDescr`, `sysObjectID`, `sysName`, `sysUpTime`) using pre-configured SNMP credentials. (See [SNMP Connectors](../../connectors/snmp/README.md)). | **Very High** for managed switches, routers, and enterprise hardware |

---

## 3. Passive Multicast Listening Window

Active scanning alone can miss transient devices (such as mobile phones, tablets, or smart TVs) that enter low-power sleep modes and ignore direct unicast probes.

When scanning a local network (`"local"` or a private subnet), `nova.net_scan` opens a bounded **passive listening window** (governed by `listenSeconds`, default 8 seconds; 0 for public scans):
1. Nova temporarily joins local multicast groups:
   * **mDNS / Bonjour:** `224.0.0.251` (IPv4) and `ff02::fb` (IPv6).
   * **SSDP (UPnP):** `239.255.255.250`.
   * **WS-Discovery:** `239.255.255.250` and `ff02::c`.
2. It passively collects unsolicited presence announcements emitted by devices waking up or announcing services.
3. Observed devices are correlated with the active scan inventory without triggering firewall alerts or generating outbound traffic bursts.

> [!NOTE]
> Passive listening never captures raw packet streams or promiscuous link data. It only listens on designated multicast group sockets. If local Windows Firewall rules restrict multicast reception, Nova flags the scan with `passive: "blocked_by_firewall"` and completes the scan using active probes alone.

---

## 4. Target Scoping, Boundaries & Safety Gates

Network scanning involves sensitive infrastructure. Nova enforces strict security and resource controls:

```
+-----------------------------------------------------------------------------------+
| TARGET SPECIFICATION       | SCOPE & BOUNDARY RULES                               |
+-----------------------------------------------------------------------------------+
| "local"                    | Auto-resolves active adapter subnets with default    |
|                            | gateways or VPN routes. Internal Hyper-V, WSL, and   |
|                            | host-only interfaces are excluded from "local" and   |
|                            | listed in context.skippedNetworks.                   |
+----------------------------+------------------------------------------------------+
| CIDR Block                 | Explicit IPv4 or IPv6 prefix (e.g. 192.168.1.0/24).  |
|                            | Hard ceiling: /20 maximum (4096 addresses per scan). |
+----------------------------+------------------------------------------------------+
| IP Range                   | Bounded range (e.g. 10.0.0.10-10.0.0.80).            |
+----------------------------+------------------------------------------------------+
| Single Host / Domain       | Single IP or domain name (resolves up to 8 IPs).     |
+-----------------------------------------------------------------------------------+
```

### Safety & Permission Governance:
* **Private Ranges (Unrestricted within Agent Permissions):** RFC 1918 (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`), Carrier-Grade NAT (`100.64.0.0/10`), Link-Local (`169.254.0.0/16`, `fe80::/10`), and Loopback (`127.0.0.0/8`, `::1`) can be scanned once the operator grants general network scan permission in Settings.
* **Public Ranges (Mandatory Per-Range User Approval):** Scanning external public IP ranges presents significant operational and legal risks. Nova enforces an interactive UI confirmation prompt **per target range**. The user's approval is valid only for the current Nova session. Automated or unattended scheduled tasks that target public ranges without prior user confirmation fail immediately with `scan_approval_required`.
* **Public Scan Rate Limiting:** Public scans are throttled to a maximum of 1 concurrent connection per host, an aggregate rate of approximately 8 connection attempts per second, and randomized jitter to prevent triggering remote intrusion detection systems (IDS).
* **Resource Exhaustion Defense:** If local socket buffers or ephemeral ports become constrained, Nova pauses, attempts recovery, and halts the job with `incompleteReason: "local_resources_exhausted"` rather than misreporting dropped connections as remote firewalls.

---

## 5. Device Classification & Evidence Scoring

Nova separates device categorization into three independent assertions, each carrying its own normalized confidence score ($0.0 \dots 1.0$):
1. **Device Class (`class`):** `router_gateway`, `firewall`, `switch`, `access_point`, `server`, `nas_storage`, `printer_scanner`, `camera`, `tv_media`, `iot`, `windows_client`, `hypervisor`, `database`, `mail`, `unknown`.
2. **Hardware Vendor (`vendor`):** Manufacturer brand (e.g. `Synology`, `Cisco`, `AVM`, `HP`, `Apple`, `Dell`).
3. **Operating System Family (`osFamily`):** `windows`, `linux`, `freebsd`, `routeros`, `embedded_rtos`, `unknown`.

### Confidence Evaluation Rules:
* **Independent Source Aggregation:** Evidence must originate from independent network layers. Multiple HTTP headers on the same port count as a single HTTP evidence point.
* **Non-Misleading Negative Results:**
  * An ICMP drop is reported as `icmp_no_reply`, not as "device offline" (many secure firewalls and Windows PCs drop ping).
  * A TCP port timeout is reported as `no_response`, not `filtered` (without raw socket access, packet filtering cannot be proven).
  * Devices not observed in a single scan are marked `not_seen`, not "removed". A device transitions to `likely_gone` only after multiple consecutive scans over the same network interface fail to observe it.

---

## 6. Persistent Network Inventory (`netmonitor.db`)

Every device discovered by `nova.net_scan` is automatically stored in Nova's local SQLite database (`netmonitor.db`), accessible via [`nova.net_devices`](../../../mcp-reference/tools/proxy-and-network/nova-net-devices.md):

```mermaid
erDiagram
    DEVICES ||--o{ DEVICE_KEYS : "identified by"
    DEVICES ||--o{ OBSERVATIONS : "verified by"
    SCANS ||--o{ OBSERVATIONS : "records"

    DEVICES {
        string deviceId PK
        string primaryAddress
        string class
        float classConfidence
        string vendor
        string model
        string osFamily
        string friendlyName
        string operatorNote
        string presenceState
        datetime firstSeen
        datetime lastSeen
    }

    DEVICE_KEYS {
        string deviceId FK
        string keyType
        string keyValue PK
    }

    OBSERVATIONS {
        string observationId PK
        string deviceId FK
        string scanId FK
        string source
        string transport
        int port
        string rawObservation
        float confidence
        datetime observedUtc
    }

    SCANS {
        string scanId PK
        string targetScope
        string profile
        int deviceCount
        datetime startedUtc
        datetime endedUtc
    }
```

### Decoupling Identity from IP Addresses
In modern DHCP and Wi-Fi networks, IP addresses change frequently. Nova pins device identities to persistent hardware and cryptographic anchors:
* **Physical MAC Address:** Verified via local ARP / IPv6 neighbor tables (excluding locally administered/randomized addresses).
* **SSH Host Key Fingerprint:** SHA-256 fingerprint of the server's public key (`ssh-ed25519`, `ecdsa-sha2-nistp256`, `rsa-sha2-512`).
* **TLS Subject Public Key Info (SPKI):** SHA-256 hash of the public key certificate presented on HTTPS or FTPS ports.
* **UPnP / WS-Discovery UUID:** Globally unique device identifiers embedded in discovery payloads.

When a device obtains a new DHCP address, Nova detects the address change, updates `primaryAddress`, and marks `isNew: false`, preserving historical notes and telemetry.

---

## 7. Deep Protocol Probing & Automated Security Findings

Every scan automatically compiles risk indicators in the `findings` array:

```json
{
  "severity": "high",
  "code": "telnet_open",
  "deviceId": "dev_4b8f10a2",
  "text": "192.168.1.45 (camera): Telnet (plain text, passwords readable on the network) on port 23 is open in the network."
}
```

### 7.1 SNMP Hardware Telemetry & Connector Binding

When `snmp` is included in `probes`, Nova queries UDP port 161 on discovered devices using credentials provisioned in SNMP connectors (`nova.connector_create(type="snmp")`):

* **Target CIDR Constraints:** SNMP credentials are bound strictly to specific IP addresses or CIDR blocks. Hostnames are explicitly forbidden to prevent DNS spoofing from redirecting management credentials. Minimum prefix sizes are `/16` for IPv4 and `/48` for IPv6, with a maximum of 64 targets per profile.
* **Single-OID GetRequest:** Nova sends one standard SNMP GetRequest for exactly 4 fixed system group objects: `sysDescr` (`1.3.6.1.2.1.1.1.0`), `sysObjectID` (`1.3.6.1.2.1.1.2.0`), `sysName` (`1.3.6.1.2.1.1.5.0`), and `sysUpTime` (`1.3.6.1.2.1.1.3.0`). Nova never performs tree walks, `GetBulk`, or `SetRequest` operations.
* **SNMPv3 USM & Engine Pinning:**
  * For SNMPv3, Nova performs an initial discovery handshake, derives localized keys, and transmits a signed (and for `authPriv`, AES-128 CFB encrypted) request.
  * **Engine Pinning (`snmp_engine_id_changed`):** Nova pins the hex `snmpEngineID` upon the first verified response. If a subsequent probe to that IP returns a different engine ID, Nova halts signed requests and emits `snmp_engine_id_changed` (medium severity) to prevent credential replay attacks.
* **Protocol Findings:**
  * `snmp_v2c_in_use` (low severity): Emitted when a device answers via SNMPv2c. The community string traverses the network in cleartext, readable by anyone sniffing traffic.
  * `snmp_v3_auth_no_priv` (low severity): Device answers SNMPv3 signed but unencrypted (`authNoPriv`). Answers cannot be forged, but remain readable on the network.
  * `snmp_public_address` (medium severity): An SNMP agent responded on a public IP address. SNMP management should strictly be isolated to private out-of-band management subnets.

### 7.2 NTP Time Synchronization & Kerberos Invariants

When `ntp` is included in `probes`, Nova queries UDP port 123 on discovered hosts:

* **RFC 5905 Mode 3 Client Request:** Nova sends standard 48-byte Mode 3 client queries. Dangerous Mode 6 (`control`) or Mode 7 (`monlist`) queries are never used.
* **RFC 9109 Client Data Minimization:** Nova populates the 8-byte transmit timestamp with cryptographic random bytes. A server response (Mode 4) is accepted only if it echoes this exact random timestamp in its origin timestamp field.
* **Time Drift & Kerberos Invariants (`ntp_time_offset`):**
  * Nova measures true clock offset: $\text{Offset} = \frac{(T_2 - T_1) + (T_3 - T_4)}{2}$.
  * Thresholds: $\ge 5\text{ s}$ (`low`), $\ge 60\text{ s}$ (`medium`), $\ge 300\text{ s}$ (`high`).
  * **Critical Operational Impact:** In Active Directory and Kerberos realms, clock skew exceeding 5 minutes causes immediate ticket authentication failures (`KRB_AP_ERR_SKEW`). In addition, TLS client/server certificates appear expired or not yet valid.
* **Unsynchronized Clock (`ntp_unsynchronized`):** Emitted (medium severity) when a server responds on UDP 123 but reports Stratum 16 or Leap Indicator 3 (`alarm`), indicating its clock is free-running and uncalibrated.

### 7.3 Active Directory & LDAP RootDSE Exploration

When probing LDAP ports (TCP 389/3268 for plain/StartTLS and 636/3269 for TLS):

* **Anonymous RootDSE Exploration:** Nova executes a single RFC 4511 BER-encoded search against base `""` with scope `baseObject` and filter `(objectClass=*)`.
* **Harvested Attributes:** Extracts `dnsHostName`, `defaultNamingContext`, `rootDomainNamingContext`, `domainControllerFunctionality`, `isGlobalCatalogReady`, `vendorName`, and `vendorVersion`.
* **Zero Bind Policy:** Nova never sends an LDAP bind, never transmits passwords, and never reads objects below the RootDSE.
* **Port Set Classification:** LDAP ports are classified under `portSets: ["admin"]` (not included in the default `quick` set).
* **Early Completion:** Nova parses BER application tags `5` (`SearchResultDone`) and `24` (`Notice of Disconnection`) to immediately close the TCP connection once RootDSE metadata is received, rather than waiting for socket timeouts.

### 7.4 SMB Dialects & NTLM Challenge Fingerprinting

When probing SMB on port 445:

* **Dialect Negotiation:** Interrogates supported SMB-2/3 dialects and verifies whether packet signing is enforced (`signingRequired`).
* **NTLM Challenge Inspection:** Inspects the server's unauthenticated NTLMSSP challenge to observe the NetBIOS computer name, Active Directory domain name, and Windows OS build version. Nova never replies to the challenge or attempts session setup.
* **Legacy SMBv1 Alert (`smb1_enabled`):** Emitted at `high` severity if the target still supports SMBv1 (the vulnerable protocol exploited by EternalBlue / WannaCry).

### 7.5 Exposed Service Findings Taxonomy

Nova correlates open ports against a hardened risk matrix:

| Finding Code | Default Severity | Monitored Services & Ports | Rationale |
| :--- | :---: | :--- | :--- |
| `telnet_open` | `medium` (private) / `high` (public) | TCP 23 | Plaintext terminal management; credentials transmitted unencrypted across the network. |
| `ftp_open` | `low` (private) / `medium` (public) | TCP 21 | Plaintext file transfer protocol unless explicit TLS is enforced. |
| `login_without_tls` | `medium` (private) / `high` (public) | TCP 80, 8080 | HTTP service presents a Basic/Digest authentication prompt over unencrypted HTTP. |
| `rdp_reachable` | `low` (private) / `medium` (public) | TCP 3389 | Microsoft Remote Desktop exposed. |
| `vnc_reachable` | `medium` (private) / `high` (public) | TCP 5900 | VNC remote desktop, frequently configured without encryption or robust authentication. |
| `database_reachable` | `medium` (private) / `high` (public) | TCP 1433, 3306, 5432, 6379, 9200, 27017 | Database engine exposed. Redis (6379) is flagged `high` due to lack of default authentication. |
| `ot_reachable` | `high` (both private and public) | TCP 102 (S7), 502 (Modbus), 44818 (EtherNet/IP) | Operational Technology / Industrial Control System interfaces lacking cryptographic authentication. |

### 7.6 Scanner Resource Limits & Ephemeral Socket Protection

Scanning dense subnets generates high socket turnover. Nova protects local operating system resources:

* **Socket Exhaustion Detection:** If Windows ephemeral ports or socket buffers are exhausted, Nova halts the scan safely with `incompleteReason: "local_resources_exhausted"` rather than misreporting dropped packets as remote firewalls.
* **Tuning Recommendations:** Reduce `parallel` from default 64 to 16 or 8, and increase `timeoutMs` to 3000 ms.
* **Asynchronous Scan Execution:** Scans running longer than `waitSeconds` return `status: "running"` with a `scanId`. Agents poll progress using `nova.net_scan_status(scanId="...")` or abort via `nova.net_scan_stop(scanId="...")`.

---

## 8. MCP Protocol Examples

### Example 1: Local Subnet Discovery Scan
```json
{
  "name": "nova.net_scan",
  "arguments": {
    "targets": [
      "local"
    ],
    "portSets": [
      "quick"
    ],
    "discovery": [
      "arp",
      "icmp",
      "mdns",
      "ssdp"
    ],
    "waitSeconds": 20
  }
}
```

### Example 2: Targeted Server Admin Scan with Background Polling
```json
{
  "name": "nova.net_scan",
  "arguments": {
    "targets": [
      "10.0.10.0/24"
    ],
    "portSets": [
      "admin",
      "database"
    ],
    "probes": [
      "ssh",
      "tls",
      "smb",
      "ldap"
    ],
    "timeBudgetSeconds": 300,
    "waitSeconds": 0
  }
}
```
*When `waitSeconds: 0` is passed, the tool returns immediately with a `scanId` and `status: "running"`. The agent subsequently checks progress with `nova.net_scan_status(scanId="...")` or halts execution with `nova.net_scan_stop(scanId="...")`.*

### Example 3: Querying the Device Inventory with Filtering
```json
{
  "name": "nova.net_devices",
  "arguments": {
    "class": "nas_storage",
    "presence": "seen"
  }
}
```

### Example 4: Assigning Operator Name and Context Note
```json
{
  "name": "nova.net_devices_update",
  "arguments": {
    "deviceId": "dev_7f3a91c0",
    "name": "Backup-NAS-Primary",
    "note": "Synology DS920+ hosting nightly database backups and media library."
  }
}
```

---

## 9. Related Documentation

* [Master Network Architecture Hub](../README.md): Overview of all 5 network disciplines and the complete 24-tool reference matrix.
* [Network & Protocol Troubleshooting](../../../troubleshooting/network-and-proxies.md): Resolving port probe approvals, SNMP engine mismatches, NTP clock drift, and socket exhaustion.
* [SNMP Connectors Architecture](../../connectors/snmp/README.md): Integrating authenticated SNMPv3/v2c hardware telemetry with network scanning.
* [DNS Diagnostics & Mail Security](../dns-diagnostics/README.md): Resolving domain records, delegation paths, and mail security records.
* [Path Diagnostics, MTR & Probing](../path-diagnostics-and-probing/README.md): Measuring hop-by-hop packet loss, jitter, and MTU limits to discovered hosts.
* [MCP Tool Reference: `nova.net_scan`](../../../mcp-reference/tools/proxy-and-network/nova-net-scan.md): Detailed parameter schema and return structures.
