# Network Interception & Request Replay

Use network interception to test how a page reacts to a failed, delayed or modified request. Use request replay to prepare, send and compare a separate HTTP request outside the page.

## A Concrete Example: Test a Failed API Request

An agent adds a temporary rule for a specific API URL in one tab, then triggers the page action that calls that API and checks the result. Nova shows an indicator while rules are active. Clear the rule when the check is finished; rules also expire automatically.

## Network Interception

`nova.network_intercept_add` arms a rule for one tab: let matching requests fail, answer them without reaching the network, change the request or the server's response, or delay them. A rule needs a URL pattern with at least 4 literal characters, lives at most 15 minutes (`ttlMs`, default 2 minutes) and removes itself after `maxHits` requests (default 20). Nova shows an indicator while rules are active. The tools are available whenever agent control is enabled; listing them does not arm anything.

## Request Replay

`nova.network_replay` prepares, sends and compares a single HTTP request outside the page, optionally with the cookies or storage-held token of an open tab (`adoptSessionFrom`).

Replay is separate from the page's requests and its tab-scoped interception rules. See the tool reference for session adoption and request parameters.

## MCP Tools

Interception and replay tools are in the `page_read_debug` bundle.

| Tool | Purpose |
| :--- | :--- |
| `nova.network_intercept_add` | Adds a tab-scoped interception rule. |
| `nova.network_intercept_list`, `nova.network_intercept_clear` | Lists rules; removes them by rule, by tab or everywhere. |
| `nova.network_replay` | Prepares, sends and compares a single HTTP request. |

## Related Documentation

* [Interception Tool Reference](../../../mcp-reference/tools/proxy-and-network/nova-network-intercept-add.md) — Rule parameters and examples.
* [Request Replay Tool Reference](../../../mcp-reference/tools/proxy-and-network/nova-network-replay.md) — Request preparation, sending and comparison.
* [Proxy Routing](../proxy/README.md) — Shared browser routing, profiles and leak protection.
* [Session Recording](../../session-recording/README.md) — Inspect recorded requests before replaying them.

[Network overview](../README.md) · [All core features](../../README.md)
