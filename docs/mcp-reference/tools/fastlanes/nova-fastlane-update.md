# `nova.fastlane_update`

> **Proposes a new revision of a fastlane; the approved one keeps running until the user approves the change.**

* **Area:** [Fastlanes](README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

Every change is a new revision the user approves; a revision still waiting is replaced. Status `pending_user_approval`, `unchanged` (same as the running revision), `already_proposed`, `not_found` or `invalid_contract`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `fastlaneId` | `string` | Yes | — | ≤ 32 characters | Fastlane id from nova.fastlane_create or nova.fastlane_list (e.g. 'fl_3f9a1c2b7d4e'). |
| `contract` | `object` | Yes | — | — | The fastlane as parts from nova.fastlane_catalog, never code: {source:{kind:'net_monitor', monitorIds:[...]}, condition:{kind:'on_event'\|'event_persists'\|'on_recovery', eventKinds:[...], forSeconds}, actions:[{kind:'notify', title} \| {kind:'http_callback', url}], coalesce:{windowSeconds}, limits:{deliveriesPerHour}, delivery:{wake:'session'} (optional: also wake this session; Nova binds it)}. An unknown field is an error. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `fastlanes` (load it with `nova.tools_bundle(bundle='fastlanes')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova.fastlane_update",
  "arguments": {
    "fastlaneId": "fl_3f9a1c2b7d4e",
    "contract": {
      "source": { "kind": "net_monitor" },
      "condition": { "kind": "on_recovery" },
      "actions": [ { "kind": "notify", "title": "Connection back" } ]
    }
  }
}
```

---

## 4. Related Tools

* [`nova.fastlane_get`](nova-fastlane-get.md) - shows the running and the waiting revision.
