# Proxy Profile Management & Runtime Leak Protection

> [!IMPORTANT]
> Standard browser automation frameworks suffer from critical privacy and security leaks: embedding plaintext proxy credentials directly into command-line arguments, leaking local IP addresses through non-proxied WebRTC UDP bindings, and broadcasting requested hostnames over local DNS resolvers when using SOCKS5. Nova AI Workspace enforces a **zero-leak runtime architecture** with sanitized command-line projection, mandatory WebRTC UDP blocking, remote SOCKS5 DNS resolution, and sandbox-isolated proxy routing.

---

## 1. Architectural Motivation: The Automation Leak Vectors

When an autonomous agent routes browser traffic through a proxy, naive browser implementations expose four major leakage channels:

1. **Plaintext Command-Line Credential Exposure:** Launching Chromium with `--proxy-server=http://user:pass@host:port` writes sensitive passwords into operating system process tables, making them readable by any local process, Task Manager, or crash reporting tool.
2. **WebRTC Local & Public IP Leaks:** WebRTC interactive media protocols (STUN/ICE) frequently open direct UDP connections that bypass HTTP and SOCKS proxy settings, transmitting the host machine's true local subnet IP (e.g. `192.168.1.100`) and ISP public IP.
3. **SOCKS5 Local DNS Leaks:** Many SOCKS implementations resolve hostnames locally before connecting to the SOCKS server, revealing every accessed website to the local network router and ISP.
4. **Cross-Sandbox IP Blurring:** Running multiple sandboxes in the same browser process can result in accidental traffic crossover if proxy configurations are not isolated cleanly.

Nova eliminates each of these vectors through low-level runtime policies and strict validation boundaries.

---

## 2. Profile Schema & Normalization Contract

Proxy configurations are stored as reusable profile records in `settings.json` under `AppSettings.ProxyProfiles`. Passwords are intentionally excluded from configuration files and stored exclusively in DPAPI:

```mermaid
classDiagram
    class ProxyProfile {
        +string Id
        +string Name
        +string Protocol
        +string Host
        +int Port
        +string? Username
        +string PasswordSecretId
        +string BypassList
        +bool Enabled
        +bool IsGlobalDefault
    }

    class DPAPIVault {
        +string proxy-credentials.dat
        +StorePassword(secretId, password)
        +GetPassword(secretId)
    }

    ProxyProfile --> DPAPIVault : References via PasswordSecretId
```

### 2.1 Complete Profile Schema

| Field | Type | Description & Validation Rules |
| :--- | :--- | :--- |
| `Id` | `string` | Immutable identifier; normalized to alphanumeric characters, dashes, and underscores. |
| `Name` | `string` | User-facing display label (e.g. `"US Residential Egress"`). |
| `Protocol` | `string` | Protocol scheme: `http`, `https`, `socks4`, or `socks5`. |
| `Host` | `string` | Normalized host or IP address (rejects control characters, whitespace, quotes, slashes). |
| `Port` | `int` | Destination port number (`1` to `65535`). |
| `Username` | `string?` | Optional authentication username. |
| `PasswordSecretId` | `string` | Stable indirection key referencing encrypted DPAPI credential storage. |
| `BypassList` | `string` | Semicolon-delimited bypass rules (e.g. `localhost;127.0.0.1;*.internal`). |
| `Enabled` | `bool` | Profile availability toggle. |
| `IsGlobalDefault` | `bool` | Designates the profile as the global proxy for normal browser tabs. |

### 2.2 Normalization & Input Validation Invariants

* **Profile Limit:** Maximum of 12 profiles (`AppSettings.MaxProxyProfiles`).
* **Endpoint String Ingestion:** When users or agents paste complete proxy URIs (e.g. `socks5://operator:secret@proxy.corp.net:1080`), Nova parses the components automatically. **The password is immediately excised** and forwarded to DPAPI storage; it is never persisted in plaintext settings.
* **IPv6 Formatting:** IPv6 host addresses are automatically enclosed in brackets for Chromium command-line compatibility (e.g. `socks5://[2001:db8::1]:1080`).
* **Bypass List Sanitization:** Entries are split on commas or semicolons, stripped of whitespace and quotes, deduplicated case-insensitively, and capped at 64 entries and 4,096 characters total. Supports `<local>`, CIDR notation, domain wildcards (`*.internal`), and exact hostnames.

---

## 3. Chromium Runtime Projection & Leak Protection

`ProxyChromiumRuntimePolicy` translates active proxy settings into sanitized WebView2 environment startup arguments:

```mermaid
flowchart TD
    Profile["Active Proxy Profile\n(Protocol, Host, Port, BypassList)"] --> PolicyEngine["ProxyChromiumRuntimePolicy"]

    subgraph Flags["Sanitized Chromium Startup Arguments"]
        ArgProxy["--proxy-server=&lt;protocol&gt;://&lt;host&gt;:&lt;port&gt;"]
        ArgBypass["--proxy-bypass-list=&lt;entries&gt;"]
        ArgWebRTC["--force-webrtc-ip-handling-policy=disable_non_proxied_udp"]
        ArgDNS["--host-resolver-rules=MAP * ~NOTFOUND , EXCLUDE &lt;proxy-host&gt;"]
    end

    PolicyEngine --> ArgProxy
    PolicyEngine --> ArgBypass

    CheckWebRTC{"WebRTC Leak Protection\nEnabled?"}
    PolicyEngine --> CheckWebRTC
    CheckWebRTC -- "Yes" --> ArgWebRTC

    CheckSocks{"Protocol == SOCKS5 &amp;\nLeak Protection Enabled?"}
    PolicyEngine --> CheckSocks
    CheckSocks -- "Yes" --> ArgDNS

    Flags --> WebView2["WebView2 Browser Engine Startup"]
```

### 3.1 Sanitized Command-Line Projection
Nova constructs standard Chromium proxy flags:
```text
--proxy-server=<protocol>://<host>:<port>
--proxy-bypass-list=<entry;entry;...>
```
Every argument value is quoted using `WindowsCommandLine.QuoteArgument` to guarantee safety against command injection.

### 3.2 WebRTC IP Leak Protection
When WebRTC protection is enabled, Nova injects:
```text
--force-webrtc-ip-handling-policy=disable_non_proxied_udp
```
This forces Chromium to block all direct, non-proxied UDP bindings. WebRTC media streams are constrained to route through the proxy tunnel or fall back to TURN relays, completely eliminating local and public IP exposure via ICE candidates.

### 3.3 SOCKS5 Remote DNS Leak Protection
Standard SOCKS5 implementations frequently leak domain names by resolving hostnames on the local machine prior to socket connection. When WebRTC leak protection is enabled for a SOCKS5 profile, Nova injects:
```text
--host-resolver-rules="MAP * ~NOTFOUND , EXCLUDE <socks5-proxy-host>"
```
* **`MAP * ~NOTFOUND`:** Forces Chromium's internal resolver to report all local lookups as unresolvable, compelling the browser to delegate DNS resolution entirely to the remote SOCKS5 proxy server.
* **`EXCLUDE <socks5-proxy-host>`:** Excludes the proxy endpoint itself so the operating system can resolve the initial proxy hostname.

---

## 4. Shared Process Architecture & Sandbox Isolation

In WebView2, all browser profiles sharing the same User Data Folder (`userDataDir`) run within **one shared browser process** and inherit startup command-line arguments:

```
┌────────────────────────────────────────────────────────────────────────┐
│                      WebView2 Routing Architecture                     │
├───────────────────┬────────────────────────────────────────────────────┤
│ Context           │ Routing Rule & Behavior                            │
├───────────────────┼────────────────────────────────────────────────────┤
│ Normal Tabs       │ Route through profile marked `IsGlobalDefault`.    │
│                   │ If none set, routes directly via system default.   │
├───────────────────┼────────────────────────────────────────────────────┤
│ Sandbox: global   │ Inherits the global proxy configuration.           │
├───────────────────┼────────────────────────────────────────────────────┤
│ Sandbox: none     │ Configured for direct unproxied connection.        │
├───────────────────┼────────────────────────────────────────────────────┤
│ Sandbox: profile  │ Bound to a specific named proxy profile.           │
└───────────────────┴────────────────────────────────────────────────────┘
```

### Fail-Closed Sandbox Invariants:
1. **Unusable Profile Fallback:** If a sandbox is configured for a specific profile that is disabled or unusable, Nova routes that sandbox directly rather than silently falling back to the global proxy.
2. **Profile Deletion Handling:** If a bound profile is deleted, settings normalization resets the sandbox's routing mode back to `global`.
3. **Dynamic Tab Recreation:** When switching a sandbox's proxy via MCP or the URL bar, Nova recreates the sandbox's WebView instance so WebView2 receives the updated routing arguments immediately without restarting the main application window.

---

## Related Documentation

* [Domain Hub: Proxy Routing & Traffic Isolation](../README.md)
* [Subguide: Credential Security & DPAPI Storage](../credential-security-and-dpapi-storage/README.md)
* [Subguide: Auxiliary Routing & Health Probing](../auxiliary-routing-and-health-probing/README.md)
* [Master Hub: Network Architecture & Traffic Control](../../README.md)
* [Multi-Sandbox Session Isolation](../../../sandbox-isolation/README.md)
* [Tool Reference: `nova.proxy_switch`](../../../../mcp-reference/tools/proxy-and-network/nova-proxy-switch.md)
