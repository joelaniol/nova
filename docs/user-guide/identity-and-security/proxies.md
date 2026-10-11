# Proxies & Network Routing

> [!NOTE]
> Nova AI Workspace includes a comprehensive **Proxy Management Subsystem** supporting HTTP, HTTPS, SOCKS4, and SOCKS5 proxies. Proxies can be assigned **globally** across the workspace or configured **per-sandbox**, allowing you to route different client sessions, geographic profiles, and research workflows through distinct network egress paths simultaneously.

---

## 1. Overview & Architecture

Whether you need to test geo-restricted web applications, route sensitive research through encrypted gateways, or isolate client environments by external IP address, Nova makes proxy configuration straightforward and leak-resistant:

* **Dual-Tier Proxy Routing:** Set a global default proxy or bind individual proxy profiles to specific sandboxes.
* **Protocol Support:** Supports HTTP, HTTPS (CONNECT tunneling), SOCKS4, and SOCKS5 endpoints.
* **Built-in WebRTC Leak Protection:** Automatically disables WebRTC local IP candidate discovery to prevent your real IP address from leaking via STUN/TURN requests.
* **Integrated Health & Diagnostics:** Built-in connection testing, live activity logs, and external IP reflection checks directly in the settings UI.
* **Full MCP Agent Parity:** AI agents can query proxy status, test connections, and switch profiles programmatically via [`nova.proxy_*`](../../mcp-reference/tools/proxy-and-network/README.md) tools.

```
+-----------------------------------------------------------------------------------+
|  Settings > Identity & Security > Proxies                                         |
+-----------------------------------------------------------------------------------+
|  [X] WebRTC leak protection (Prevent local IP exposure via STUN/TURN)            |
|                                                                                   |
|  PROXY PROFILES                                            [ + Add Proxy Profile ]|
|  +-----------------------------------------------------------------------------+  |
|  | [*] US Residential Gateway (Default Global)                                 |  |
|  |     Protocol: HTTP | Endpoint: 198.51.100.24:8080 | Auth: Username/Password |  |
|  |     Status: Connected (IP: 198.51.100.24 - New York, US)                    |  |
|  |     Actions: [ Test Proxy ]  [ Edit ]  [ Delete ]                           |  |
|  +-----------------------------------------------------------------------------+  |
|  | [ ] EU Research Node                                                        |  |
|  |     Protocol: SOCKS5 | Endpoint: 203.0.113.50:1080 | Auth: IP Allowlist     |  |
|  |     Status: Idle (Assigned to Sandbox "EU Client")                          |  |
|  |     Actions: [ Test Proxy ]  [ Edit ]  [ Delete ]                           |  |
|  +-----------------------------------------------------------------------------+  |
|                                                                                   |
|  DIAGNOSTICS & LOGGING                                                            |
|  Test Target: [ https://api.ipify.org?format=json   ] [ Run Test ]                |
|  Log Retention: [ 7 days v ]  [ Refresh Log ]  [ Clear Log ]                      |
|  Log preview: [2026-10-11 16:30] Tunnel established to 198.51.100.24:8080 (HTTP) |
+-----------------------------------------------------------------------------------+
```

---

## 2. Adding and Editing Proxy Profiles

Open **Menu → Settings → Identity & security → Proxies** and click **Add Proxy Profile**:

1. **Profile Name:** Enter a recognizable name (e.g., *"US Residential Gateway"* or *"Staging VPN Proxy"*).
2. **Protocol:** Select from the dropdown:
   * **HTTP:** Standard web proxy; supports proxy username and password authentication.
   * **HTTPS:** Secure CONNECT tunnel to the proxy endpoint.
   * **SOCKS4:** Basic TCP proxy without authentication.
   * **SOCKS5:** Advanced TCP/UDP proxy (see authentication note below).
3. **Server & Port:** Enter the hostname or IP address and the port number (e.g., `proxy.example.com` and `8080`).
4. **Authentication (Optional):**
   * Check **Requires authentication** and enter your **Username** and **Password**.
   * Passwords are encrypted locally using the **Windows Data Protection API (DPAPI)**.

> [!IMPORTANT]
> **SOCKS5 Authentication Notice:**
> The underlying Chromium and Microsoft WebView2 network stack does not natively support embedded username/password authentication for SOCKS5 proxies. If your SOCKS5 proxy requires credentials, use **IP address allowlisting**, a local proxy forwarder/relay, or an **HTTP/HTTPS** proxy with credential authentication instead.

---

## 3. Global vs. Per-Sandbox Proxy Assignment

Nova provides complete flexibility in how proxies are applied across your browsing sessions:

### 1. Global Proxy Mode
In the Proxies panel, select a profile and click **Set as global proxy**. All standard browser tabs, unassigned sandboxes, and background downloads immediately route their traffic through this proxy endpoint. To revert to a direct connection, click **Disable global proxy**.

### 2. Per-Sandbox Proxy Assignment
You can assign different proxies to different sandboxes to maintain completely isolated geographic or corporate network identities:
1. Open **Menu → Settings → Identity & security → Sandboxes**.
2. Select or edit a sandbox (e.g., Sandbox B).
3. In the **Proxy** dropdown, choose:
   * **No proxy:** Connects directly to the internet, bypassing any global proxy.
   * **Use global proxy:** Inherits whatever global proxy is active.
   * **Specific Profile:** Binds the sandbox exclusively to a configured profile (e.g. *"EU Research Node"*).
4. All tabs opened under that sandbox pill immediately use the assigned proxy, while other sandboxes continue using their own independent connections.

---

## 4. WebRTC Leak Protection

Traditional browsers routing through a proxy often leak the user's real public and local LAN IP addresses through WebSockets or WebRTC peer-to-peer connection requests.

In Nova:
* **WebRTC Leak Protection** is enabled by default in **Settings → Proxies**.
* When enabled, WebView2 suppresses local host IP address candidates in WebRTC session descriptions (SDP), ensuring websites only see the proxy's IP address.

---

## 5. Testing & Diagnostics

Before navigating to sensitive sites, verify that your proxy is working and not leaking data:

1. **In-UI Proxy Test:**
   * Enter a test URL in the **Test Target** field (defaults to `https://api.ipify.org?format=json`).
   * Click **Test Proxy**.
   * Nova sends a verified probe request through the proxy tunnel, displaying the round-trip latency and confirming the reflected external IP address.
2. **Proxy Activity Log:**
   * Review connection events, TLS handshake timestamps, and authentication challenges in the **Proxy Log** viewer.
   * Configure retention periods (**3 days**, **7 days**, or **30 days**), or click **Clear Log** to scrub diagnostic traces.
3. **Status Indicator:**
   * When an active proxy is routing traffic, a **Proxy chip** appears in the main toolbar and URL bar.
   * Hover over the chip to view the active profile name, protocol, and connection health.

---

## 6. AI Agent Integration

Connected AI agents can inspect, test, and rotate proxies via Nova's Model Context Protocol (MCP) tools:

* [`nova.proxy_status`](../../mcp-reference/tools/proxy-and-network/nova-proxy-status.md): Returns active proxy configuration, effective endpoints, and WebRTC leak state.
* [`nova.proxy_switch`](../../mcp-reference/tools/proxy-and-network/nova-proxy-switch.md): Dynamically changes the active global proxy profile.
* [`nova.proxy_test`](../../mcp-reference/tools/proxy-and-network/nova-proxy-test.md): Tests connection reachability and retrieves external IP reflection data.
* [`nova.proxy_log`](../../mcp-reference/tools/proxy-and-network/nova-proxy-log.md): Inspects recent network tunnel events and errors.

---

## Related Documentation

* **[Core Features: Network Subsystem](../../core-features/network/README.md)** — Architectural details on network interception, replay, and TLS inspection.
* **[Sandboxes & Profiles](sandboxes-and-profiles.md)** — Multi-profile session isolation and sandbox configuration.
* **[Website & Agent Permissions](permissions.md)** — Controlling origin permissions and network requests.
* **[Passwords & Vault](passwords-and-vault.md)** — Managing stored credentials and proxy secrets.
