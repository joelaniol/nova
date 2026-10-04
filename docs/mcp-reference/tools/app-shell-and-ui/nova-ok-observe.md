# `nova.ok_observe`

> **Records structured Operational Knowledge (OK) claims about the service open in a tab, such as login state or active model.**

* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ok_observe` stores what an agent has observed about the service in a tab as facts in Nova's Operational Knowledge store. Each claim has a `signalKey`, a JSON `value`, an optional `certainty` (`certain`, `likely` or `tentative`; default `likely`) and optional `evidence` text. Canonical keys such as `core.login_state` or `core.model.active` come from `nova.ok_signal_schema`; an unknown `core.*` key is rejected with `-32602`, while keys in another namespace (for example `vendor.*`) are accepted without registration. Up to 50 claims per call.

A claim that contradicts a stronger existing fact is recorded but not applied (`conflicted`); a weaker differing claim may be stored as `observation_only`. Only `accepted` claims changed the stored fact.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string or null` | No | `"active"` | — | Tab ID, sandbox ID, or 'active'. Use null or omit for default 'active'. |
| `perceptionId` | `string or null` | No | — | — | Optional perception/trace ID to group claims from the same observation moment. Use null or omit when no trace grouping is available. |
| `claims` | `array` of `object` | Yes | — | ≥ 1 items | Structured observations about the current page state. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ok_observe",
  "arguments": {
    "targetId": "tab-1",
    "claims": [
      {
        "signalKey": "core.login_state",
        "value": "logged_in",
        "certainty": "certain",
        "evidence": "Account menu with avatar is visible"
      }
    ]
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "OK observe: 1 accepted, 0 rejected, 0 conflicted, 0 observation-only, 0 superseded."
    }
  ],
  "structuredContent": {
    "ok": true,
    "accepted": 1,
    "rejected": 0,
    "conflicted": 0,
    "observationOnly": 0,
    "superseded": 0,
    "facts": [
      {
        "key": "core.login_state",
        "value": "logged_in",
        "state": "fresh",
        "isNew": true
      }
    ],
    "warnings": null
  }
}
```

---

## 4. Operational Best Practices

* **Signal Keys:** Query `nova.ok_signal_schema` first to use canonical signal names and value types.
* **Honest certainty:** Use `certain` only for directly visible evidence; `tentative` claims do not override an existing fact with a different value.
* **Read the counters:** `rejected`, `conflicted` and `observationOnly` mean the stored fact was not changed; `warnings` names the reason.

---

## 5. Related Tools

* [`nova.ok_signal_schema`](nova-ok-signal-schema.md)
* [`nova.dismiss_blockers`](../browser-automation/nova-dismiss-blockers.md)
