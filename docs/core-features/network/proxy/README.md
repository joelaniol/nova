# Proxy Routing

> [!NOTE]
> Nova AI Workspace routes browser traffic through HTTP, HTTPS, SOCKS4 or SOCKS5 proxy profiles and can block WebRTC from leaking the real IP address past the proxy.

---

## 1. A Concrete Example: Check the Route Before Using a Session

You select a proxy profile for a browsing task. Nova can probe that endpoint and report its latency and external IP. You then check the route from an actual browser page after applying the setting and any recommended restart.

These checks answer different questions. A proxy probe uses a separate HTTP client; a healthy endpoint does not prove that an already-open WebView is using it. Browser routing comes from the shared browser process's launch configuration, which applies to normal tabs and sandboxes together.

## 2. Why Route and Leak Checks Matter

Autonomous agents browsing the web encounter standard network hurdles:

* **IP Rate Limits & Geo-Blocking:** Region-restricted content (localized pricing, news) or IP rate limits during heavy research.
* **WebRTC IP Leaks:** Even with a proxy active, WebRTC can reveal local and public IP addresses to a page.
* **Plaintext Credential Exposure:** Automation frameworks commonly put proxy credentials into command-line arguments, where they show up in process lists.

Nova manages proxies as profiles with separately stored passwords and offers WebRTC and DNS leak protection.

---

## 3. Architecture & Routing Model

```mermaid
flowchart TD
    subgraph Control["Settings and MCP"]
        Switch["Proxies and network settings, nova.proxy_switch"]
    end

    subgraph ProxyCore["Proxy layer"]
        Profiles["Proxy profiles: HTTP, HTTPS, SOCKS4, SOCKS5"]
        LeakGuard["Optional WebRTC and SOCKS5 DNS leak protection"]
    end

    subgraph Browser["Shared browser process"]
        Tabs["Browser tabs"]
        Sandboxes["Sandboxes"]
    end

    Switch --> Profiles
    Profiles -->|global proxy| LeakGuard
    LeakGuard --> Tabs
    LeakGuard --> Sandboxes
```

---

## 4. Core Features in Detail

1. **One global proxy for all surfaces:**
   * The profile marked "Use as global proxy for normal tabs" carries the traffic. Browser tabs and all sandboxes run in one shared browser process, so this global proxy applies to every tab and every sandbox.
   * Sandboxes store their own proxy choice (follow the global proxy, no proxy, or a selected profile), but WebView2 currently offers no way to give one profile its own proxy. A sandbox set to its own profile is switched back to the global proxy when Nova starts, and a sandbox set to "no proxy" also goes through the global proxy.
2. **Protocols and authentication:**
   * Supported protocols: HTTP (CONNECT), HTTPS, SOCKS4 and SOCKS5. Each profile can have a bypass list (for example `localhost;127.0.0.1;*.internal`).
   * Username and password work for HTTP and HTTPS proxies. SOCKS credentials are not supported by Chromium/WebView2.
3. **Credential hygiene:**
   * Proxy passwords are stored encrypted with Windows DPAPI (`nova.proxy_set_password` or in Settings) and are answered to the proxy's authentication challenge, not passed on the browser command line. The proxy log redacts credentials.
4. **WebRTC and DNS leak protection:**
   * "Protect WebRTC local IP leaks" (off by default) stops WebRTC from using UDP outside the proxy; some calls then fall back to TURN or fail. With a SOCKS5 proxy, local DNS resolution is additionally blocked except for the proxy host itself.
5. **Applying changes:**
   * When the global proxy changes, Nova recreates the open tab WebViews. Because the proxy and WebRTC switches belong to the shared browser process, Nova shows "Restart recommended" — after a restart the setting applies to all tabs.
6. **Scoped traffic disconnect:**
   * `nova.proxy_disconnect` blocks HTTP(S) traffic for a scope; `nova.proxy_reconnect` checks the proxy and unblocks it.

---

## 5. MCP Tools

Proxy tools are in the `proxy_management` bundle.

| Tool | Purpose |
| :--- | :--- |
| `nova.proxy_list` | Lists proxy profiles with protocol, host, port and sandbox bindings. |
| `nova.proxy_create`, `nova.proxy_update`, `nova.proxy_remove` | Manages proxy profiles. |
| `nova.proxy_set_password` | Stores or clears a profile's password (DPAPI-encrypted). |
| `nova.proxy_switch` | Changes the global proxy, or the stored proxy choice of a sandbox. |
| `nova.proxy_status` | Connection status, latency and external IP of a proxy. |
| `nova.proxy_test` | Tests a proxy against a probe URL (default `https://api.ipify.org/?format=json`). |
| `nova.proxy_disconnect`, `nova.proxy_reconnect` | Blocks traffic for a scope; checks the proxy and unblocks it. |
| `nova.proxy_log` | Reads recent, redacted proxy log lines. |

## Related Documentation

* [Network Interception & Request Replay](../network-interception/README.md) — Tab-scoped rules and a separate HTTP request repeater.
* [Proxy Tool Reference](../../../mcp-reference/tools/proxy-and-network/README.md) — Parameters and examples.
* [Multi-Sandbox Session Isolation](../../sandbox-isolation/README.md) — Separate browser profiles per sandbox.
* [Fingerprint Protection & Browser Identity](../../fingerprint-and-identity/README.md) — Fingerprint protection and client hints.

[Network overview](../README.md) · [All core features](../../README.md)
