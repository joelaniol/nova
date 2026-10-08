# Proxy Routing & Traffic Isolation

> [!NOTE]
> Nova AI Workspace provides an enterprise-grade proxy and traffic isolation subsystem supporting HTTP, HTTPS, SOCKS4, and SOCKS5 protocols. It enforces zero plaintext credentials on Chromium command lines, comprehensive WebRTC and SOCKS5 DNS leak protection, auxiliary tool routing parity via `NovaWebTrafficProxy`, download-specific fail-safe policies, live URL-bar health monitoring with exponential latency smoothing, and a fail-closed disconnect/reconnect circuit breaker.

---

## 1. Architectural Overview & Threat Model

Autonomous web agents face severe privacy and networking challenges during web interactions. Standard browser automation frameworks frequently suffer from critical leak vectors:

1. **Plaintext Command-Line Credential Exposure:** Automation frameworks often embed proxy credentials directly into process startup arguments (e.g. `--proxy-server=http://user:pass@host:port`), exposing sensitive passwords in OS process listings, task managers, and crash dumps.
2. **WebRTC IP Leakage:** Even when all HTTP traffic routes through a proxy, WebRTC peer connections can establish non-proxied UDP bindings, leaking the host machine's local LAN and true public IP address.
3. **SOCKS5 DNS Leakage:** Standard SOCKS5 proxies often route DNS resolution through the host's local system resolver rather than through the proxy tunnel, revealing requested domains to local ISPs or network operators.
4. **Auxiliary Traffic Bypass:** While the browser WebView routes through a proxy, auxiliary background tasks—such as network replay, crawler discovery, website MCP inspection, or file downloads—often use bare HTTP clients that bypass the proxy entirely, exposing the true IP address.
5. **Silent Fallback to Direct Connection:** When a configured proxy fails, poorly designed tools frequently fall back to a direct connection, deanonymizing the session without warning.

Nova addresses these vulnerabilities with an end-to-end traffic isolation architecture:

```mermaid
flowchart TD
    subgraph UI_MCP["Control Surfaces"]
        Settings["Settings > Proxies"]
        URLBar["URL-Bar Proxy Flyout & Status"]
        MCP["MCP Tools (proxy_management)"]
    end

    subgraph Security_Core["Security & Credential Core"]
        CredStore[("DPAPI Credential Store\nproxy-credentials.dat")]
        ProbeService["ProxyProbeService\n(4KB Bounded Probing & Health)"]
        DisconnectGuard["Fail-Closed Disconnect Guard\n(Blocks HTTP/S Navigation)"]
        ProxyLogger["Redacted Asynchronous Logger\n(Logs/proxy/)"]
    end

    subgraph Browser_Runtime["Browser Traffic (Shared UDF)"]
        Policy["ProxyChromiumRuntimePolicy"]
        Tabs["Normal Browser Tabs"]
        Sandboxes["Sandbox Profiles"]
    end

    subgraph Auxiliary_Traffic["Auxiliary & Download Routing"]
        WebTraffic["NovaWebTrafficProxy (IWebProxy)"]
        Downloader["DownloadProxyResolver"]
        Replay["Network Replay & Crawler"]
    end

    UI_MCP --> Security_Core
    Security_Core --> Policy
    Policy -->|--proxy-server\n--force-webrtc\n--host-resolver-rules| Tabs
    Policy --> Sandboxes
    Security_Core --> WebTraffic
    WebTraffic --> Replay
    Security_Core --> Downloader
    CredStore -.->|BasicAuth Challenge| Tabs
    CredStore -.->|BasicAuth Challenge| Sandboxes
```

---

## 2. Profile Management & Normalization Contract

Proxy configurations are managed as reusable profiles stored in `settings.json` under `AppSettings.ProxyProfiles`. Passwords are intentionally excluded from configuration files and stored separately in encrypted form.

### 2.1 Profile Schema

| Field | Type | Description |
| :--- | :--- | :--- |
| `Id` | `string` | Stable identifier, normalized to alphanumeric characters, dashes, and underscores. |
| `Name` | `string` | User-facing display label. |
| `Protocol` | `string` | Protocol scheme: `http`, `https`, `socks4`, or `socks5`. |
| `Host` | `string` | Normalized host or IP address (rejects control characters, whitespace, quotes, slashes). |
| `Port` | `int` | Destination port number (`1` to `65535`). |
| `Username` | `string?` | Optional authentication username. |
| `PasswordSecretId` | `string` | Stable indirection key referencing encrypted DPAPI credential storage. |
| `BypassList` | `string` | Semicolon-delimited bypass rules (e.g. `localhost;127.0.0.1;*.internal`). |
| `Enabled` | `bool` | Profile availability toggle. |
| `IsGlobalDefault` | `bool` | Designates the profile as the global proxy for normal browser tabs. |

### 2.2 Normalization & Input Validation
- **Profile Limit:** Maximum of 12 profiles (`AppSettings.MaxProxyProfiles`).
- **Endpoint Paste Parsing:** When pasting complete proxy strings (e.g. `socks5://user:pass@proxy.example.com:1080`), Nova automatically parses the protocol, host, port, and username. Passwords are excised immediately and stored in DPAPI; they are never kept in plaintext configuration.
- **IPv6 Endpoint Formatting:** IPv6 addresses are automatically bracketed for Chromium and display compatibility (e.g. `socks5://[2001:db8::1]:1080`).
- **Bypass List Sanitization:** Entries are split on commas or semicolons, stripped of whitespace and quotes, deduplicated case-insensitively, and capped at 64 entries and 4,096 characters total. Supports `<local>`, CIDR notation, domain wildcards (`*.internal`), and exact hostnames.

---

## 3. Chromium Runtime Projection & Leak Protection

### 3.1 Chromium Command-Line Projection
Nova projects the active proxy profile into WebView2 environment startup arguments via `ProxyChromiumRuntimePolicy`:

```text
--proxy-server=<protocol>://<host>:<port>
--proxy-bypass-list=<entry;entry;...>
```

All argument values are sanitized and quoted using standard Windows command-line quoting rules (`WindowsCommandLine.QuoteArgument`) to prevent argument injection.

### 3.2 WebRTC IP Leak Protection
When "Protect WebRTC local IP leaks" is enabled in Settings or MCP, Nova adds:

```text
--force-webrtc-ip-handling-policy=disable_non_proxied_udp
```

This enforces that WebRTC media traffic routes exclusively through the proxy or falls back to TURN relays, completely preventing UDP packets from bypassing the proxy to discover real local or public IP addresses.

### 3.3 SOCKS5 DNS Leak Protection
Standard SOCKS5 implementations often resolve hostnames on the local machine before connecting to the proxy. When WebRTC leak protection is enabled on a SOCKS5 proxy, Nova injects:

```text
--host-resolver-rules="MAP * ~NOTFOUND , EXCLUDE <socks5-proxy-host>"
```

- `MAP * ~NOTFOUND`: Instructs Chromium's internal resolver that all direct host lookups fail. This forces the browser to delegate DNS resolution entirely to the remote SOCKS5 proxy.
- `EXCLUDE <socks5-proxy-host>`: Excludes the proxy endpoint itself from the lookup ban so its own domain name can still be resolved locally by the operating system.

### 3.4 Shared Process Architecture & Sandbox Routing

In WebView2, all browser profiles sharing the same User Data Folder (`userDataDir`) run inside **one shared browser process** and share a single command-line argument configuration:

- **Normal Tabs:** Route through the profile marked `IsGlobalDefault`. If no global proxy is configured, normal tabs use the direct system route.
- **Sandbox Profiles:** Sandboxes support three configuration modes:
  - `global`: Inherits the global proxy configuration.
  - `none`: Configured for direct connection.
  - `profile`: Bound to a specific proxy profile.
- **Fail-Closed Sandbox Invariant:** If a sandbox explicitly selects an existing profile that is disabled or unusable, Nova uses a direct connection for that sandbox rather than silently falling back to the global proxy. If a selected profile is deleted, settings normalization resets that sandbox back to `global`.
- **Dynamic Recreation:** When switching the proxy of an active sandbox via the URL-bar flyout or MCP, Nova recreates that sandbox's WebView instance so WebView2 receives the updated routing arguments immediately.

---

## 4. Credential Security & DPAPI Storage

### 4.1 DPAPI Storage (`proxy-credentials.dat`)
Proxy passwords are never stored in `settings.json`. Instead, they are persisted in a protected binary datastore:
```
%LOCALAPPDATA%\NovaBrowser\proxy-credentials.dat
```
- **Encryption:** Encrypted using Windows Data Protection API (`ProtectedData.Protect` with `DataProtectionScope.CurrentUser`), binding access exclusively to the current Windows user account.
- **Storage Limits:** Capped at 64 newest entries and a maximum file size of 1 MB.
- **Write-Protection Invariant:** If an existing credential file cannot be read (e.g. transient file locking), `ProxyCredentialStore` refuses to perform writes. This prevents accidental credential wipes from replacing existing credentials with an empty set.

### 4.2 Browser-Compatible Challenge Handling
Because credentials cannot be placed on the command line, HTTP and HTTPS proxies must authenticate dynamically via HTTP 407 challenges:

1. When a proxy requires credentials, WebView2 raises the `BasicAuthenticationRequested` event.
2. **Security Root URI Guard:** Before supplying credentials, Nova validates that:
   - The challenge host and port match the configured proxy profile.
   - The challenge URI points to the proxy endpoint root.
   - The top-level web page being viewed is not hosted on that same proxy host.
3. This guard prevents malicious web servers hosted on the same IP as a public proxy from triggering fake authentication dialogs to harvest proxy credentials.

> [!WARNING]
> **SOCKS Credential Limitation:** Chromium and WebView2 do not support username/password authentication for SOCKS4 or SOCKS5 proxies at the browser engine level. Nova actively warns if SOCKS credentials are provided, recommending HTTP(S) proxies, IP allowlisting, or a local loopback relay instead.

---

## 5. Auxiliary Traffic & Download Routing Parity

### 5.1 Internal Request Routing (`NovaWebTrafficProxy`)

Standard browser extensions and tools frequently suffer from traffic bifurcation: the browser routes through a proxy, but background automation tools (e.g. HTTP replay, crawler discovery, site probes) execute directly via `.NET HttpClient`, exposing the real IP.

Nova eliminates this vulnerability via `NovaWebTrafficProxy`, an `IWebProxy` implementation shared by all internal services:
- **Automatic Route Synchronization:** Reads effective proxy configuration dynamically from `SettingsStore.LastKnownGoodSnapshot`. When the global proxy changes, all static internal HTTP clients switch immediately without requiring process restarts.
- **Protected Subsystems:**
  - Network Request Replay (`nova.network_replay`)
  - Crawler & Discovery Probes (`nova.site_discovery_probe`)
  - Website MCP Server Inspection (`nova.site_mcp_inspect`)
  - Plugin & connector fetch operations
- **Bypass Enforcement:** Local loopback addresses and hosts matching the active bypass list are excluded from proxying, matching Chromium's internal rules.

### 5.2 Download Proxy Routing (`DownloadProxyResolver`)

File downloads can be routed independently from browsing tasks:

| Mode | Behavior | Fail-Safe Guarantees |
| :--- | :--- | :--- |
| `Off` | Direct connection | Only active when explicitly selected by the user. |
| `Global` | Follows the global proxy profile | Defaults to system route if no global proxy exists. |
| `Sandbox` | Follows the active sandbox proxy | Falls back to global proxy if sandbox has no proxy. |
| `Custom` | Uses a dedicated download proxy profile | **Fail-closed:** If the chosen profile is unavailable, downloads fall back to the global proxy rather than exposing the real IP on a direct connection. |

---

## 6. Real-Time Health Probing, URL-Bar Status & Fail-Closed Disconnect

### 6.1 Probing Engine (`ProxyProbeService`)
Nova continuously evaluates proxy health and latency:
- **30-Second Bounded Interval:** Probes run automatically every 30 seconds for active proxies.
- **Default Probe URL:** `https://api.ipify.org/?format=json`.
- **4 KB Bounded Reading:** Custom probe endpoints are read header-first and capped at 4 KB (`MaxProbeResponseBytes`), protecting against memory exhaustion from large or infinite streaming endpoints.
- **External IP Detection:** Extracts remote IP addresses from standard JSON attributes (`ip`, `origin`, `query`, `clientIp`, `client_ip`) or plain text.
- **Actionable Error Mapping:** Instead of raw exceptions, probe failures map to user-friendly diagnostic guidance:
  - `HTTP 407`: Proxy authentication required; check username/password.
  - `HTTP 401`: Probe URL requires login; choose an open probe endpoint.
  - `SocketError.HostNotFound`: Proxy hostname unresolvable; check DNS.
  - `SocketError.ConnectionRefused`: Proxy refused connection; check port.
  - `SocketError.TimedOut`: Connection timed out; verify firewall.
  - `AuthenticationException`: TLS handshake failed; verify certificate.

### 6.2 Rolling Latency Smoothing
Latency jitter is smoothed using an Exponential Moving Average (EMA):
$$\text{Latency}_{\text{avg}} = \text{Latency}_{\text{prev}} \times 0.65 + \text{Sample}_{\text{new}} \times 0.35$$

### 6.3 Visual Health Indicators

The URL-bar proxy icon reflects live operational states:

| Visual State | Indicator | Condition |
| :--- | :---: | :--- |
| **Hidden** | — | No proxy active on current tab. |
| **Unknown** | ⚪ | Proxy configured but pending initial probe. |
| **Healthy** | 🟢 | Last probe succeeded; average latency $< 1000$ ms. |
| **Slow** | 🟡 | Last probe succeeded; average latency $1000\text{--}2499$ ms. |
| **Degraded** | 🟠 | Last probe succeeded; average latency $\ge 2500$ ms. |
| **Failed** | 🔴 | Last probe failed or timed out. |
| **Disconnected** | ⛔ | Manually paused; traffic is strictly blocked. |

### 6.4 Fail-Closed Disconnect & Reconnect Circuit Breaker

Nova provides a manual and programmatic traffic killswitch for emergency isolation:

```mermaid
sequenceDiagram
    participant A as Agent / Operator
    participant G as Disconnect Guard
    participant W as CoreWebView2
    participant P as Proxy Probe

    A->>G: nova.proxy_disconnect(targetId)
    G->>W: CoreWebView2.Stop()
    G->>G: Register Disconnected Target
    Note over G,W: All HTTP / HTTPS navigations blocked
    
    A->>G: nova.proxy_reconnect(targetId)
    G->>P: Run Isolated Health Probe
    alt Probe Succeeded (probeOk = true)
        P-->>G: Health Confirmed
        G->>G: Unregister Disconnected Target
        G-->>A: Status: reconnected (Traffic Unblocked)
    else Probe Failed (probeOk = false)
        P-->>G: Probe Failed
        Note over G,W: Target stays blocked (probe_failed)
        G-->>A: Status: probe_failed (Traffic Stays Blocked)
    end
```

- **Disconnect (`nova.proxy_disconnect`):** Halts active WebViews via `CoreWebView2.Stop()` and intercepts all subsequent HTTP and HTTPS navigations, preventing traffic from leaving the browser.
- **Reconnect (`nova.proxy_reconnect`):** Runs an isolated health probe while browsing remains paused. The block is lifted **only if the health probe succeeds**. If the probe fails, browsing remains blocked (`probe_failed`) to prevent accidental leaks.

---

## 7. Redacted & Bounded Logging (`ProxyLog`)

Diagnostic logging is isolated in a dedicated log channel:
```
%LOCALAPPDATA%\NovaBrowser\Logs\proxy\proxy-YYYYMMDD.log
```
- **Non-Blocking Architecture:** Log calls enqueue into a bounded `BlockingCollection<LogEntry>(4096)`. Disk I/O executes on a dedicated background thread (`NovaBrowser.ProxyLogWriter`), preventing UI or network thread stalls.
- **Credential Redaction:** Automatically strips credentials from URLs and strings (replacing `user:pass@host` with `***@host`) and sanitizes carriage returns to prevent log injection.
- **Tail Reads:** `nova.proxy_log` reads only tail segments (up to 256 KB) from the 3 newest log files, avoiding high memory consumption on large logs.
- **Automated Retention:** Pruned automatically after 7 days by default (configurable: 3, 7, or 30 days).

---

## 8. MCP Tool Matrix & Automation Workflows

Proxy management tools belong to the `proxy_management` bundle. Load them via:
```json
{
  "name": "nova.tools_bundle",
  "arguments": { "bundle": "proxy_management" }
}
```

### 8.1 Tool Reference Table

| Tool | Category | Parameters | Purpose |
| :--- | :--- | :--- | :--- |
| `nova.proxy_list` | `safe` | — | Lists all configured proxy profiles and sandbox bindings. |
| `nova.proxy_status` | `safe` | `targetId?`, `profileId?` | Returns connection status, latency, remote IP, and visual state. |
| `nova.proxy_create` | `normal` | `name`, `protocol`, `host`, `port`, `username?`, `password?`, `bypassList?`, `isGlobalDefault?` | Creates a new proxy profile. |
| `nova.proxy_update` | `normal` | `profileId`, `name?`, `protocol?`, `host?`, `port?`, `username?`, `password?`, `bypassList?`, `isGlobalDefault?` | Modifies an existing profile. |
| `nova.proxy_remove` | `normal` | `profileId` | Deletes a profile and purges its DPAPI credentials. |
| `nova.proxy_set_password` | `normal` | `profileId`, `password?` | Stores or clears a DPAPI-encrypted password. |
| `nova.proxy_switch` | `normal` | `profileId?`, `sandboxId?`, `mode?` | Changes global proxy or sandbox proxy routing (`global`, `none`, `profile`). |
| `nova.proxy_test` | `safe` | `profileId`, `probeUrl?` | Runs an immediate probe and returns latency and external IP. |
| `nova.proxy_disconnect` | `normal` | `targetId` | Engages fail-closed killswitch for a target (`browser-tabs` or sandbox ID). |
| `nova.proxy_reconnect` | `normal` | `targetId` | Probes proxy and unblocks browsing only upon success. |
| `nova.proxy_log` | `safe` | `maxLines?` | Reads recent redacted proxy log lines (1 to 500 lines). |

### 8.2 Automation Workflow Examples

#### 1. Checking Proxy Route Before Browsing
```json
{
  "name": "nova.proxy_test",
  "arguments": {
    "profileId": "us-east-proxy",
    "probeUrl": "https://api.ipify.org/?format=json"
  }
}
```

#### 2. Switching Sandbox to a Dedicated Proxy
```json
{
  "name": "nova.proxy_switch",
  "arguments": {
    "sandboxId": "sandbox-research",
    "mode": "profile",
    "profileId": "us-east-proxy"
  }
}
```

#### 3. Emergency Disconnect & Controlled Reconnect
```json
{
  "name": "nova.proxy_disconnect",
  "arguments": {
    "targetId": "browser-tabs"
  }
}
```
*Response confirms browsing is blocked:*
```json
{
  "structuredContent": {
    "success": true,
    "targetId": "browser-tabs",
    "status": "disconnected",
    "isDisconnected": true
  }
}
```

*Reconnecting runs an automatic health check before unblocking:*
```json
{
  "name": "nova.proxy_reconnect",
  "arguments": {
    "targetId": "browser-tabs"
  }
}
```

---

## 9. Related Documentation

- [Privacy](../../privacy/README.md) — How routing relates to browser identity and session data.

- [Network Interception & Request Replay](../network-interception/README.md) — Traffic rules and separate HTTP request repeater.
- [TLS Certificate Inspection](../tls-inspection/README.md) — Host certificate chains and fingerprint verification.
- [Multi-Sandbox Session Isolation](../../sandbox-isolation/README.md) — Isolated browser environments and profile storage.
- [Fingerprint Protection & Browser Identity](../../privacy/fingerprint-and-identity/README.md) — Client hints, canvas noise, and WebGL emulation.

[Network overview](../README.md) · [All core features](../../README.md)
