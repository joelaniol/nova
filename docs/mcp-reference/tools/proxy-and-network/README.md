# Proxy Routing & Network Interception

Proxy profile management, authentication, traffic redirection, and CDP network request/response interception.

* **Capability Bundle(s):** `proxy_management`
* **Core Architecture Guide:** [Core Features: proxy-and-network.md](../../../core-features/proxy-and-network.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (15 Tools)

| Tool Name | Status | Description |
| :--- | :---: | :--- |
| **[`nova.network_intercept_add`](nova-network-intercept-add.md)** | Documented | Deposit a rule that changes what the PAGE gets for matching requests: let them fail, answer them from the rule, send them out c... |
| **[`nova.network_intercept_clear`](nova-network-intercept-clear.md)** | Documented | Remove interception rules: one rule with ruleId, one tab's rules with targetId, or — with no arguments — every rule in the brow... |
| **[`nova.network_intercept_list`](nova-network-intercept-list.md)** | Documented | List the interception rules that are currently armed, with hits used and time left. |
| **[`nova.network_replay`](nova-network-replay.md)** | Documented | Targeted HTTP Repeater, not an automatic scanner. |
| **[`nova.proxy_create`](nova-proxy-create.md)** | Documented | Create a new proxy profile. |
| **[`nova.proxy_disconnect`](nova-proxy-disconnect.md)** | Documented | Manually disconnect the proxy for a target scope. |
| **[`nova.proxy_list`](nova-proxy-list.md)** | Documented | List all configured proxy profiles with their settings and sandbox assignments. |
| **[`nova.proxy_log`](nova-proxy-log.md)** | Documented | Read recent browser web-proxy diagnostic log entries from Logs/proxy (redacted — no credentials exposed). |
| **[`nova.proxy_reconnect`](nova-proxy-reconnect.md)** | Documented | Reconnect a previously disconnected proxy. |
| **[`nova.proxy_remove`](nova-proxy-remove.md)** | Documented | Delete a proxy profile and its stored credentials. |
| **[`nova.proxy_set_password`](nova-proxy-set-password.md)** | Documented | Store or clear the password for a proxy profile. |
| **[`nova.proxy_status`](nova-proxy-status.md)** | Documented | Get the live health status of a proxy profile (or the active global default). |
| **[`nova.proxy_switch`](nova-proxy-switch.md)** | Documented | Switch the active proxy for global browser tabs or a specific sandbox. |
| **[`nova.proxy_test`](nova-proxy-test.md)** | Documented | Run a health probe against a proxy profile. |
| **[`nova.proxy_update`](nova-proxy-update.md)** | Documented | Update an existing proxy profile. |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
