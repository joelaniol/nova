# `nova.fastlane_create`

> **Sets up a fastlane; one that starts a run or calls the internet asks the user first.**

* **Area:** [Fastlanes](README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

A fastlane that only notifies, wakes the calling session or calls an address on this PC or in the local network runs at once (`status: "active"`, `approvedBy: "policy"`); Nova tells the user, who can pause or delete it. One that starts a run on the user's Claude account or calls an address on the internet asks the user in Nova's usual prompt during this call: `active` when allowed, `rejected` when refused, `pending_user_approval` when the user has not answered within about 20 seconds: the prompt stays open, and the answer, given there or later in the agents panel, takes effect by itself. The user can switch either question off in Nova's settings; an agent cannot approve anything. Once running, Nova waits for the event itself and runs the actions the moment it happens. The same contract still waiting answers `already_proposed` with that fastlane, so a repeated call after a timeout does no harm. Each agent session may have a few proposals waiting at once; unanswered proposals expire after a week.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `name` | `string` | Yes | — | ≤ 80 characters | Short name the user sees in the approval and the list, e.g. 'web-1 down for 30 s'. |
| `contract` | `object` | Yes | — | — | The fastlane as parts from nova.fastlane_catalog, never code: {source:{kind:'net_monitor', monitorIds:[...]} \| {kind:'time', schedule:'weekdays 07:30'\|'every 15m'\|..., timeZone, onMissed:'once'\|'skip'} \| {kind:'file', folder, pattern:'*.csv', subfolders} \| {kind:'web_notification', domains:['ebay.de']} \| {kind:'custom', channel} (events raised with nova.fastlane_emit or an emit action) \| {kind:'page_watch', domains, urlMatches, target:{title:true}\|{selector, read:'text'\|'count'\|'exists'}} (any element of a page open in a tab), condition: per source - net_monitor {kind:'on_event'\|'event_persists'\|'on_recovery', eventKinds:[...], forSeconds}, time {kind:'on_schedule'} (may be left out), file {kind:'on_event', eventKinds:['created'\|'changed'\|'deleted'\|'renamed'], settleSeconds}, web_notification {kind:'on_event', titleMatches:'*Nachricht*', bodyMatches}, custom {kind:'on_event', titleMatches, bodyMatches}, page_watch {kind:'changes'\|'number_increases'\|'appears'\|'disappears', textMatches}, actions:[{kind:'notify', title, windowsNotification:false (optional: Nova's notification center only, no Windows notification)} \| {kind:'http_callback', url} \| {kind:'emit', channel} (pass the event on to fastlanes listening there)], coalesce:{windowSeconds}, limits:{deliveriesPerHour}, delivery:{wake:'session'} (optional: also wake this session; Nova binds it) \| {wake:'run'} with execution:{agent:'claude', task, tools:[...], limits:{runsPerDay, maxTurns, maxBudgetUsd, timeoutMinutes}, replyContinuation:{maxFollowUps:1-3} (optional: the run may ask the user once with nova.notifications_send(wake='run') and end; the answer starts a follow-up run; needs nova.notifications_send in tools)} (Nova starts a run limited to the listed Nova tools; any Nova tool may be listed, the user approves the list), briefing:{text} (optional, with delivery: standing instructions up to 20000 characters for the woken agent, approved word for word and handed over by nova.fastlane_claim; for a run it replaces execution.task)}. An unknown field is an error. |

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
* [`nova.fastlane_get`](nova-fastlane-get.md) - see whether it runs and who approved it.
