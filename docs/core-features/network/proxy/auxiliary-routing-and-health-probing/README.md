# Auxiliary Routing, Health Probing & Circuit Breakers

> [!NOTE]
> Configuring a proxy for a browser's UI does not guarantee complete privacy if background processes, file downloaders, and standalone API diagnostic tools bypass the proxy and establish direct network connections. Nova AI Workspace enforces **auxiliary traffic routing parity** through `NovaWebTrafficProxy`, isolates file download streams via `DownloadProxyResolver`, monitors connection health via `ProxyProbeService`, and provides a fail-closed disconnect/reconnect circuit breaker.

---

## 1. The Auxiliary Traffic Bifurcation Problem

In conventional browser automation architectures, traffic frequently splits along two divergent paths:

```mermaid
flowchart TD
    subgraph DefectiveSystem["Flawed Browser Architecture"]
        B1["Browser UI (WebView)"] -->|Uses Proxy| P1["Proxy Server"] --> Internet1["Target Web Server"]
        B2["Crawler / Replay Client"] -->|Bypasses Proxy!| Direct1["Direct ISP Route\n(REAL IP EXPOSED!)"] --> Internet1
        B3["File Downloader"] -->|Bypasses Proxy!| Direct2["Direct ISP Route\n(REAL IP EXPOSED!)"] --> Internet1
    end
```

This vulnerability—**auxiliary traffic bifurcation**—deanonymizes autonomous agents without warning. An agent may navigate through a secure residential proxy, but the moment it invokes a crawler probe, replays an API request, or downloads a file, its true IP address is revealed to external servers.

Nova resolves this by routing all auxiliary .NET HTTP clients through `NovaWebTrafficProxy`.

---

## 2. Auxiliary Traffic Routing Parity (`NovaWebTrafficProxy`)

`NovaWebTrafficProxy` is an implementation of `System.Net.IWebProxy` that synchronizes dynamically with Nova's active browser proxy profile:

```mermaid
flowchart TD
    Settings["SettingsStore.LastKnownGoodSnapshot"] --> Router["NovaWebTrafficProxy (IWebProxy)"]

    subgraph ProtectedClients["All Internal .NET HTTP Clients"]
        Replay["nova.network_replay"]
        Crawler["nova.crawl_start / probe"]
        SiteMcp["nova.site_mcp_inspect"]
        Plugins["Plugin / Connector Fetch"]
    end

    ProtectedClients --> Router
    Router --> CheckBypass{"Matches Bypass List\nor Localhost?"}

    CheckBypass -- "Yes" --> Direct["Direct Network Route\n(Bypassed)"]
    CheckBypass -- "No" --> Tunnel["Active Proxy Tunnel\n(HTTP / HTTPS / SOCKS5)"]
```

### Architectural Guarantees:
1. **Dynamic Route Synchronization:** When the global proxy profile is changed via UI or MCP, `NovaWebTrafficProxy` updates immediately. Existing static `HttpClient` instances switch their egress route without requiring application restarts.
2. **Bypass Parity:** Evaluates the active profile's `BypassList` (including `<local>`, CIDR notation, and domain wildcards) identically to Chromium's internal resolver.
3. **No Direct Route Fallback:** If the configured proxy goes offline, auxiliary tools **never fall back silently to a direct connection**. Requests fail with connection errors, protecting the agent's identity.

---

## 3. Dedicated Download Routing (`DownloadProxyResolver`)

File downloads can impose heavy bandwidth loads or require independent routing policies. Nova provides dedicated download routing modes:

| Mode | Operational Behavior | Fail-Safe & Privacy Enforcements |
| :--- | :--- | :--- |
| **`Off`** | Direct connection | Only active when explicitly selected by the operator. |
| **`Global`** | Inherits the active global proxy profile | Defaults to system route if no global proxy is configured. |
| **`Sandbox`** | Inherits the active sandbox proxy profile | Falls back to the global proxy profile if the sandbox has no proxy. |
| **`Custom`** | Routes downloads through a dedicated download proxy | **Fail-Closed Invariant:** If the selected custom profile is unavailable, downloads fall back to the global proxy rather than exposing the real IP on a direct connection. |

---

## 4. Real-Time Health Probing (`ProxyProbeService`)

To prevent agents from getting stuck behind dead or unresponsive proxies, Nova continuously monitors proxy connectivity and round-trip latency:

```mermaid
sequenceDiagram
    autonumber
    participant ProbeService as ProxyProbeService
    participant Proxy as Remote Proxy Server
    participant ProbeEndpoint as Remote Probe URL (api.ipify.org)

    Note over ProbeService: 30-Second Bounded Interval Triggered
    ProbeService->>Proxy: Establish TCP Tunnel
    Proxy->>ProbeEndpoint: HTTPS GET /?format=json
    ProbeEndpoint-->>Proxy: Return JSON Response
    Proxy-->>ProbeService: 4KB Bounded Stream
    Note over ProbeService: Measure Latency & Parse Egress IP
    Note over ProbeService: Apply Exponential Moving Average (EMA)
    ProbeService-->>ProbeService: Update Visual Health Indicator
```

### 4.1 Probing Specifications:
* **Bounded Probing Interval:** Probes execute automatically every 30 seconds for active proxy profiles.
* **Default Probe Endpoint:** `https://api.ipify.org/?format=json`.
* **4 KB Bounded Read (`MaxProbeResponseBytes`):** Custom probe URLs are read header-first and strictly capped at 4,096 bytes. This prevents memory leaks or thread hanging if a misconfigured probe URL points to an infinite streaming endpoint.
* **Remote IP Extraction:** Extracts the outward egress IP from JSON response attributes (`ip`, `origin`, `query`, `clientIp`, `client_ip`) or plaintext bodies.

### 4.2 Rolling Latency Smoothing
Raw network latency fluctuates significantly. Nova calculates smoothed latency using an Exponential Moving Average (EMA):

$$\text{Latency}_{\text{avg}} = (\text{Latency}_{\text{prev}} \times 0.65) + (\text{Sample}_{\text{new}} \times 0.35)$$

This filter eliminates single-packet jitter while maintaining sensitivity to persistent network degradation.

---

## 5. Visual Health Indicators & URL-Bar Flyout

The live proxy status is continuously projected to the browser's URL bar:

| Visual State | Indicator Glyph | Technical Trigger Condition |
| :--- | :---: | :--- |
| **Hidden** | — | No proxy active on the current tab. |
| **Unknown** | ⚪ | Proxy configured but pending initial probe. |
| **Healthy** | 🟢 | Last probe succeeded; average latency $< 1000$ ms. |
| **Slow** | 🟡 | Last probe succeeded; average latency $1000\text{--}2499$ ms. |
| **Degraded** | 🟠 | Last probe succeeded; average latency $\ge 2500$ ms. |
| **Failed** | 🔴 | Last probe failed, timed out, or returned an HTTP error. |
| **Disconnected** | ⛔ | Manually paused via circuit breaker; traffic is strictly blocked. |

---

## 6. The Fail-Closed Disconnect / Reconnect Circuit Breaker

Nova includes an emergency traffic killswitch for rapid isolation:

```mermaid
flowchart TD
    Agent["Agent / Operator"] --> Disconnect["nova.proxy_disconnect(targetId)"]

    subgraph CircuitBreaker["Fail-Closed Circuit Breaker"]
        Disconnect --> HaltWebViews["Halt Active WebViews (CoreWebView2.Stop())"]
        HaltWebViews --> BlockNav["Block All HTTP / HTTPS Navigations"]
        
        BlockNav --> Reconnect["nova.proxy_reconnect(targetId)"]
        Reconnect --> Probe["Run Isolated Health Probe (4KB bounded)"]
        
        Probe --> ProbeCheck{"Probe Succeeded?"}
        ProbeCheck -- "Yes" --> Unblock["Unregister Block & Restore Navigations"]
        ProbeCheck -- "No" --> KeepBlocked["Maintain Traffic Block (probe_failed)"]
    end

    Unblock --> Restored["Browsing Restored (Status: reconnected)"]
    KeepBlocked --> AlertAgent["Alert: Proxy Unhealthy (Status: probe_failed)"]
```

### Circuit Breaker Invariants:
1. **Immediate Navigation Interception:** Invoking [`nova.proxy_disconnect`](../../../../mcp-reference/tools/proxy-and-network/nova-proxy-disconnect.md) halts active WebViews and registers a navigation blocker. Any attempt to navigate fails immediately with an error.
2. **Probe-Gated Reconnection:** Invoking [`nova.proxy_reconnect`](../../../../mcp-reference/tools/proxy-and-network/nova-proxy-reconnect.md) **does not unblock traffic unconditionally**. It executes an isolated health probe while browsing remains paused. The block is lifted **only if the health probe confirms connectivity**. If the probe fails, traffic remains strictly blocked to protect the user's real IP address.

---

## Related Documentation

* [Domain Hub: Proxy Routing & Traffic Isolation](../README.md)
* [Subguide: Profile Management & Runtime Leak Protection](../profile-management-and-runtime-leak-protection/README.md)
* [Subguide: Credential Security & DPAPI Storage](../credential-security-and-dpapi-storage/README.md)
* [Master Hub: Network Architecture & Traffic Control](../../README.md)
* [Tool Reference: `nova.proxy_status`](../../../../mcp-reference/tools/proxy-and-network/nova-proxy-status.md)
* [Tool Reference: `nova.proxy_disconnect`](../../../../mcp-reference/tools/proxy-and-network/nova-proxy-disconnect.md)
