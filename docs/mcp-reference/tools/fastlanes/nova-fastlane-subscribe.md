# `nova.fastlane_subscribe`

> **Tells the agent session a fastlane wakes whether events wait for it.**

* **Area:** [Fastlanes](README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

A fastlane whose contract has `delivery: {wake: 'session'}` keeps its events for the agent session that proposed it; Nova binds that session itself and the user approves the binding with the rest of the contract. This tool answers only for that session. Status `invitation` names the waiting delivery (`invitation.deliveryId`, number of bundles, times - ids and counts only, no event content); `waiting` means the fastlane runs and nothing is there yet; `not_running` means it is not approved yet or paused. Another session gets `not_bound_to_session` and never sees the events; to have the fastlane wake a new session, propose the same contract again with `nova.fastlane_update`. A fastlane without `delivery` answers `no_delivery`.

The answer also carries `wait`: a background waiter the agent starts as its own command (`command` plus `args`, i.e. `NovaBrowser.McpProxy.exe --wait <ticket>`). It uses no tokens while it waits and ends with exactly one JSON line on stdout: `event_available` (with `deliveryId` - call `nova.fastlane_claim`), `timeout` (start it again), `transport_error` (Nova was unreachable for a minute), `subscription_revoked`, `binding_lost` or `update_required` (call `nova.fastlane_subscribe` to learn why). The ticket only asks whether a delivery waits for this session; it grants no tool call. Each call issues a new ticket and ends an older waiter of the same session.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `fastlaneId` | `string` | Yes | — | ≤ 32 characters | Fastlane id from nova.fastlane_create or nova.fastlane_list (e.g. 'fl_3f9a1c2b7d4e'). |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `fastlanes` (load it with `nova.tools_bundle(bundle='fastlanes')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova.fastlane_subscribe",
  "arguments": { "fastlaneId": "fl_3f9a1c2b7d4e" }
}
```

---

## 4. Related Tools

* [`nova.fastlane_claim`](nova-fastlane-claim.md) - take the waiting events.
* [`nova.fastlane_ack`](nova-fastlane-ack.md) - report the result.
