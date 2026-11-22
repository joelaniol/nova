# `nova.fastlane_emit`

> **Raises your own event on a channel; every fastlane listening there acts on it.**

* **Area:** [Fastlanes](README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

Turns anything an agent, a run or a script can detect into a fastlane trigger. A fastlane with `source: {kind: 'custom', channel: 'orders'}` reacts to every event raised on `orders` whose title and text match its condition: it notifies the user, wakes an agent, starts a run, calls a server or passes the event on with the action `{kind: 'emit', channel}`. The answer is `raised` with the ids of the fastlanes reached, or `no_listener` when no running fastlane listens (nothing is stored). Raising grants nothing: the listening fastlanes do what the user approved for them, and title, text and data reach them as foreign data.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `channel` | `string` | Yes | — | ≤ 128 characters | Channel name, letters, digits, '.', '_' and '-' (e.g. 'vinted', 'orders.new'); the same as the listening fastlane's source.channel (case-insensitive). |
| `title` | `string` | No | — | ≤ 200 characters | Optional short title; a fastlane's condition titleMatches tests it, notify shows it. |
| `text` | `string` | No | — | ≤ 2000 characters | Optional text; a fastlane's condition bodyMatches tests it. |
| `data` | `object` | No | — | — | Optional JSON object handed to the listeners (claim, callback body), at most 8192 bytes. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `fastlanes` (load it with `nova.tools_bundle(bundle='fastlanes')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova.fastlane_emit",
  "arguments": { "channel": "orders", "title": "New order", "text": "Order 1042 is paid.", "data": { "orderId": 1042 } }
}
```

---

## 4. Related Tools

* [`nova.fastlane_create`](nova-fastlane-create.md) - sets up the fastlane that listens on the channel.
* [`nova.fastlane_catalog`](nova-fastlane-catalog.md) - lists the custom source and the emit action.
