# Proxy Routing & Network Interception

Proxy profile management, authentication, traffic redirection, and CDP network request/response interception.

* **Core Architecture Guide:** [Core Features: proxy-and-network.md](../../../core-features/proxy-and-network.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

<!-- generated:tool-list (from the tool pages in this folder; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
## Tool Inventory (16 Tools)

Capability bundles of these tools: `page_read_debug`, `proxy_management`.

| Tool | What it does |
| :--- | :--- |
| **[`nova.network_intercept_add`](nova-network-intercept-add.md)** | Deposits a CDP network interception rule to mock responses, inject delays, modify headers, or fail requests. |
| **[`nova.network_intercept_clear`](nova-network-intercept-clear.md)** | Disarms network interception rules: by rule ID, by tab ID, or globally across the entire browser. |
| **[`nova.network_intercept_list`](nova-network-intercept-list.md)** | Lists currently armed network interception rules with remaining hit budgets and expiration timers. |
| **[`nova.network_replay`](nova-network-replay.md)** | Targeted HTTP request repeater for replaying, editing, and comparing network payloads out-of-band. |
| **[`nova.proxy_create`](nova-proxy-create.md)** | Creates a new proxy profile with host, port, protocol, and optional credentials. |
| **[`nova.proxy_disconnect`](nova-proxy-disconnect.md)** | Manually disconnects the proxy for a target scope, blocking all HTTP(S) traffic as an emergency kill switch. |
| **[`nova.proxy_list`](nova-proxy-list.md)** | Lists all configured proxy profiles with connection settings, protocols, and sandbox bindings. |
| **[`nova.proxy_log`](nova-proxy-log.md)** | Reads recent redacted proxy routing and diagnostic log entries from disk. |
| **[`nova.proxy_reconnect`](nova-proxy-reconnect.md)** | Reconnects a disconnected proxy and verifies connectivity before unblocking network traffic. |
| **[`nova.proxy_remove`](nova-proxy-remove.md)** | Deletes a proxy profile and resets any sandbox bindings back to the global default. |
| **[`nova.proxy_set_password`](nova-proxy-set-password.md)** | Stores or clears encrypted proxy authentication credentials using Windows DPAPI. |
| **[`nova.proxy_status`](nova-proxy-status.md)** | Queries real-time connectivity status, latency, and external IP for a proxy profile. |
| **[`nova.proxy_switch`](nova-proxy-switch.md)** | Dynamically switches the active proxy for global tabs or a specific sandbox without restarting Nova. |
| **[`nova.proxy_test`](nova-proxy-test.md)** | Executes an active network diagnostic probe through a proxy profile to verify connectivity and external IP. |
| **[`nova.proxy_update`](nova-proxy-update.md)** | Updates host, port, protocol, or bypass list of an existing proxy profile. |
| **[`nova.tls_inspect`](nova-tls-inspect.md)** | Inspects the TLS certificate and server configuration of one host in depth: full chain, names, purpose, validation level, protocol and cipher support, HSTS and Certificate Transparency subdomains. |
<!-- /generated:tool-list -->

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
