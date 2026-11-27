# `nova.fastlane_memory_set`

> **Writes or deletes a note a fastlane's agent keeps for its next wake-up.**

* **Area:** [Fastlanes](README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

Writes one entry of the fastlane's memory, or removes it with `delete: true`. Use one entry per matter under a key of your choice, for example `item:4711/buyer:anna`; `text` replaces the whole entry. Write as soon as something was done on the page (an offer sent, a message answered), not only at the end: a run that stops early otherwise leaves the next one without the state. Do not store secrets or more about people than the matter needs.

Like reading, writing works only from a delivery the caller claimed, with the epoch of that claim. `expectedVersion` is the version `nova.fastlane_memory_get` returned for the key, or `0` for an entry that does not exist yet. The answer is `stored` (with the new `version`) or `deleted`. If the entry changed or was deleted since it was read, the answer is `conflict`: nothing is written, and `current` shows what the entry holds now, or `null` if it is gone. An entry the user deleted cannot be written back from an old read. At the entry limit the answer is `full`; existing entries can still be changed and deleted.

The user sees and deletes the entries in Nova's agents panel. They stay on this PC and end with the fastlane. Refusals: `not_claimed`, `stale_epoch`, `closed`, `not_bound_to_session`, `not_found`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `deliveryId` | `integer` | Yes | — | ≥ 1 | Delivery id from nova.fastlane_subscribe (invitation.deliveryId) or nova.fastlane_claim. |
| `epoch` | `integer` | Yes | — | ≥ 1 | epoch from the nova.fastlane_claim that took this delivery. |
| `key` | `string` | Yes | — | 1–128 characters | The entry's key, one per matter, no line breaks or surrounding spaces. |
| `text` | `string` | No | — | 1–16000 characters | The entry's whole new content. Exactly one of text and delete. |
| `delete` | `boolean` | No | — | — | true removes the entry (a matter that is finished). Exactly one of text and delete. |
| `expectedVersion` | `integer` | Yes | — | ≥ 0 | Version of the entry as you read it; 0 for an entry that does not exist yet. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `fastlanes` (load it with `nova.tools_bundle(bundle='fastlanes')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova.fastlane_memory_set",
  "arguments": { "deliveryId": 12, "epoch": 1, "key": "item:4711/buyer:anna", "text": "Offered 28 EUR on 26 Nov; waiting for the buyer's answer.", "expectedVersion": 0 }
}
```

---

## 4. Related Tools

* [`nova.fastlane_memory_get`](nova-fastlane-memory-get.md) - reads the entries and their versions.
* [`nova.fastlane_claim`](nova-fastlane-claim.md) - returns the epoch to write with.
