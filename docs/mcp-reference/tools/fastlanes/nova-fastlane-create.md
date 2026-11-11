# `nova.fastlane_create`

> **Proposes a fastlane; it runs only after the user approves it.**

* **Area:** [Fastlanes](README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

Stores the contract as a proposal with `status: "pending_user_approval"`. Nothing runs until the user approves this exact contract in Nova's agents panel; an agent cannot approve it. Once approved, Nova waits for the event itself and runs the actions the moment it happens. The same contract still waiting answers `already_proposed` with that fastlane, so a repeated call after a timeout does no harm. Each agent session may have a few proposals waiting at once; unanswered proposals expire after a week.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `name` | `string` | Yes | — | ≤ 80 characters | Short name the user sees in the approval and the list, e.g. 'web-1 down for 30 s'. |
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
  "name": "nova.fastlane_create",
  "arguments": {
    "name": "web-1 down for 30 s",
    "contract": {
      "source": { "kind": "net_monitor", "monitorIds": ["mon_3f9a1c2b7d4e"] },
      "condition": { "kind": "event_persists", "eventKinds": ["outage"], "forSeconds": 30 },
      "actions": [ { "kind": "notify", "title": "web-1 is down" } ]
    }
  }
}
```

---

## 4. Related Tools

* [`nova.fastlane_preview`](nova-fastlane-preview.md) - check the contract first.
* [`nova.fastlane_get`](nova-fastlane-get.md) - see whether the user approved it.
