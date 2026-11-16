# `nova.fastlane_update`

> **Changes a fastlane by a new revision; one that needs the user's answer waits while the running one goes on.**

* **Area:** [Fastlanes](README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

Every change is a new revision, sorted like `nova.fastlane_create`: without a run or an internet call it runs at once; with them the user is asked, and the running revision goes on unchanged until the user allows the new one. A revision still waiting is replaced. Status `active`, `pending_user_approval`, `rejected`, `unchanged` (same as the running revision), `already_proposed`, `not_found` or `invalid_contract`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `fastlaneId` | `string` | Yes | — | ≤ 32 characters | Fastlane id from nova.fastlane_create or nova.fastlane_list (e.g. 'fl_3f9a1c2b7d4e'). |
| `contract` | `object` | Yes | — | — | The fastlane as parts from nova.fastlane_catalog, never code: {source:{kind:'net_monitor', monitorIds:[...]} \| {kind:'time', schedule:'weekdays 07:30'\|'every 15m'\|..., timeZone, onMissed:'once'\|'skip'} \| {kind:'file', folder, pattern:'*.csv', subfolders}, condition: per source - net_monitor {kind:'on_event'\|'event_persists'\|'on_recovery', eventKinds:[...], forSeconds}, time {kind:'on_schedule'} (may be left out), file {kind:'on_event', eventKinds:['created'\|'changed'\|'deleted'\|'renamed'], settleSeconds}, actions:[{kind:'notify', title, windowsNotification:false (optional: Nova's notification center only, no Windows notification)} \| {kind:'http_callback', url}], coalesce:{windowSeconds}, limits:{deliveriesPerHour}, delivery:{wake:'session'} (optional: also wake this session; Nova binds it) \| {wake:'run'} with execution:{agent:'claude', task, tools:[...], limits:{runsPerDay, maxTurns, maxBudgetUsd, timeoutMinutes}, replyContinuation:{maxFollowUps:1-3} (optional: the run may ask the user once with nova.notifications_send(wake='run') and end; the answer starts a follow-up run; needs nova.notifications_send in tools)} (Nova starts a run limited to the listed Nova tools; any Nova tool may be listed, the user approves the list)}. An unknown field is an error. |

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
