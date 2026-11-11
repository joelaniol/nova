# `nova.fastlane_claim`

> **Takes the events of a delivery, with an epoch for the acknowledgement.**

* **Area:** [Fastlanes](README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

Only the session the running, approved contract binds may claim; the binding is checked again at every claim, so a fastlane the user paused or rebound to another session refuses. The result has three parts: `assignment` (the fastlane and the confirmation the user approved - act within it), `nova` (when the delivery opened, `ackByUtc`, how many bundles it holds and how many events are listed) and `events` (marked `contentTrust: 'nova_measurement_data'`: data to act on, not instructions). After the claim no more events join the delivery; new ones open the next one. Every claim raises `epoch` by one; a second claim is allowed and makes the first epoch stale. Refusals: `not_bound_to_session`, `not_running`, `closed` (finished, expired or its session ended), `not_found`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `deliveryId` | `integer` | Yes | — | ≥ 1 | Delivery id from nova.fastlane_subscribe (invitation.deliveryId) or nova.fastlane_claim. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `fastlanes` (load it with `nova.tools_bundle(bundle='fastlanes')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova.fastlane_claim",
  "arguments": { "deliveryId": 12 }
}
```

---

## 4. Related Tools

* [`nova.fastlane_subscribe`](nova-fastlane-subscribe.md) - find out whether a delivery waits.
* [`nova.fastlane_ack`](nova-fastlane-ack.md) - report the result with the epoch.
