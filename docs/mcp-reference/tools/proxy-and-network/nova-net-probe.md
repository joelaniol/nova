# `nova.net_probe`

Checks from this PC which TCP ports of a host are reachable, and whether an HTTP proxy there opens a CONNECT tunnel.

---

## 1. Overview

`nova.net_probe` answers the question a command on the server itself cannot: **is this port open from the outside?** After a firewall change (`ufw`, `iptables`, `nftables` or a hoster's firewall panel), `ss -ltn` on the server only shows what listens, not what the firewall lets through. `nova.net_probe` connects from the PC Nova runs on and reports what it sees.

* **One TCP connect per port.** Nova opens a plain TCP connection to each port and closes it again. Nothing is logged in and no data is sent (except the CONNECT request below).
* **Four answers.** `open` (the connection was accepted), `closed` (refused: the host is reachable, but nothing listens or a REJECT rule answers), `filtered` (no answer within `timeoutMs`: typically a DROP rule or a firewall on the way), `unreachable` (no route to the host). Anything else is `error` with the socket error name.
* **HTTP proxy test.** `httpProxyConnect={port, target}` sends one `CONNECT target HTTP/1.1` request to a proxy on the host and reports `tunnel_established` (2xx), `auth_required` (407, with the `Proxy-Authenticate` scheme), `refused` (any other status), `not_http`, `no_answer` or `connection_closed`. No credentials are sent. If the proxy port itself is not open, the state is `port_closed`, `port_filtered` and so on.
* **TCP only.** UDP is not offered: without a protocol answer, an open UDP port cannot be told apart from a filtered one.
* **Direct route.** The connections go directly from this PC (`route: "direct"`), the same way Nova's SSH and SFTP connections do, not through the browser's proxy.
* **Asked once per host.** The first check of a host asks you once; until Nova restarts, further checks of that host run without asking. Hosts of connections that already logged in successfully are not asked about. In an unattended session (a scheduled task) an unconfirmed host fails with `connector_approval_required`.
* **Bounded.** Up to 32 ports per call, 8 at a time; a host name resolves to its first IPv4 address when there is one, and all resolved addresses are listed.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `host` | `string` | Yes | — | ≤ 253 characters | Host name or IP address to check, without scheme, path or port (e.g. 'server.example.com', '203.0.113.7'). The first IPv4 address is used when there is one; all resolved addresses are listed. |
| `tcpPorts` | `array` of `integer` | No | — | 1–32 items | TCP ports to check, e.g. [22, 80, 443, 3306]. Duplicates are checked once. |
| `httpProxyConnect` | `object` | No | — | — | Optional: test an HTTP proxy on host with one CONNECT request (no credentials are sent). |
| `httpProxyConnect.port` | `integer` | Yes | — | 1–65535 | Port of the HTTP proxy on host. |
| `httpProxyConnect.target` | `string` | Yes | — | ≤ 260 characters | 'host:port' the proxy should open a tunnel to, e.g. 'example.com:443'. |
| `timeoutMs` | `integer` | No | `3000` | 200–10000 | How long to wait for each connect (and for the proxy answer) before reporting filtered. Default 3000. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.net_probe",
  "arguments": {
    "host": "server.example.com",
    "tcpPorts": [22, 80, 443, 3306]
  }
}
```

### Response (shortened)
```json
{
  "structuredContent": {
    "ok": true,
    "host": "server.example.com",
    "route": "direct",
    "addresses": ["203.0.113.7"],
    "probedAddress": "203.0.113.7",
    "timeoutMs": 3000,
    "ports": [
      { "port": 22, "state": "open", "elapsedMs": 31, "socketError": null },
      { "port": 80, "state": "open", "elapsedMs": 29, "socketError": null },
      { "port": 443, "state": "open", "elapsedMs": 30, "socketError": null },
      { "port": 3306, "state": "filtered", "elapsedMs": 3001, "socketError": null }
    ],
    "byState": { "open": [22, 80, 443], "filtered": [3306] },
    "proxyConnect": null
  }
}
```

### Testing an HTTP proxy
```json
{
  "name": "nova.net_probe",
  "arguments": {
    "host": "proxy.example.com",
    "httpProxyConnect": { "port": 3128, "target": "example.com:443" }
  }
}
```

---

## 4. Operational Best Practices

* **Check before and after a firewall change.** Run it once before the change and once after, with the same ports, and compare `byState`.
* **Keep the SSH port in every check.** When you change a firewall over SSH, include port 22 (or your SSH port) so you notice at once if the change would lock you out.
* **`closed` is not `filtered`.** `closed` means packets arrive and are answered; `filtered` means they are dropped on the way. A port that should be blocked from the internet is usually expected as `filtered`.
* **Your own network can filter too.** A corporate or hotel network may block outgoing ports; a `filtered` result then says something about this PC's network, not the server.

---

## 5. Related Tools

* [`nova.ssh_run`](../connectors-and-mail/nova-ssh-run.md) — Changes the firewall on the server and shows what listens there
* [`nova.connector_probe`](../connectors-and-mail/nova-connector-probe.md) — Checks one configured connection, including the login
* [`nova.tls_inspect`](nova-tls-inspect.md) — Inspects the certificate and TLS setup of an open port
* [`nova.proxy_test`](nova-proxy-test.md) — Tests a proxy configured in Nova
