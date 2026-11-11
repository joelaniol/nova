# `nova.fastlane_ack`

> **Closes a claimed delivery with the agent's result.**

* **Area:** [Fastlanes](README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

`result` is `done` (handled as approved) or `failed` (say why in `summary`). Only the epoch of the latest claim is accepted; an older one answers `stale_epoch` and changes nothing, so an agent that stalled and came back cannot close a delivery a later claim is working on. Further refusals: `not_claimed`, `closed`, `not_bound_to_session`, `not_found`. A claimed delivery nobody acknowledges expires after 24 h as `unacknowledged`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `deliveryId` | `integer` | Yes | — | ≥ 1 | Delivery id from nova.fastlane_subscribe (invitation.deliveryId) or nova.fastlane_claim. |
| `epoch` | `integer` | Yes | — | ≥ 1 | epoch from the nova.fastlane_claim that took this delivery. |
| `result` | `string` | Yes | — | `done`, `failed` | 'done' (handled as approved) or 'failed' (could not handle it; say why in summary). |
| `summary` | `string` | No | — | ≤ 500 characters | Optional: what you did or why it failed, in one or two sentences for the user. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `fastlanes` (load it with `nova.tools_bundle(bundle='fastlanes')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova.fastlane_ack",
  "arguments": { "deliveryId": 12, "epoch": 1, "result": "done", "summary": "Restarted the web service; the monitor reports it back up." }
}
```

---

## 4. Related Tools

* [`nova.fastlane_claim`](nova-fastlane-claim.md) - returns the epoch to acknowledge with.
