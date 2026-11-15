# `nova.fastlane_preview`

> **Checks a fastlane contract without storing it and shows what the user will be asked to approve.**

* **Area:** [Fastlanes](README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

A broken contract answers `status: "invalid_contract"` with every error at once, each with a code and a JSON path. A valid one answers with the complete contract (all defaults filled in), its `contractHash`, the plain-language confirmation (when / then without AI / with AI / access / limits) and a simulated event. Nothing is stored or sent.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `contract` | `object` | Yes | — | — | The fastlane as parts from nova.fastlane_catalog, never code: {source:{kind:'net_monitor', monitorIds:[...]} \| {kind:'time', schedule:'weekdays 07:30'\|'every 15m'\|..., timeZone, onMissed:'once'\|'skip'} \| {kind:'file', folder, pattern:'*.csv', subfolders}, condition: per source - net_monitor {kind:'on_event'\|'event_persists'\|'on_recovery', eventKinds:[...], forSeconds}, time {kind:'on_schedule'} (may be left out), file {kind:'on_event', eventKinds:['created'\|'changed'\|'deleted'\|'renamed'], settleSeconds}, actions:[{kind:'notify', title, windowsNotification:false (optional: Nova's notification center only, no Windows notification)} \| {kind:'http_callback', url}], coalesce:{windowSeconds}, limits:{deliveriesPerHour}, delivery:{wake:'session'} (optional: also wake this session; Nova binds it) \| {wake:'run'} with execution:{agent:'claude', task, tools:[...], limits:{runsPerDay, maxTurns, maxBudgetUsd, timeoutMinutes}} (Nova starts a run limited to the listed Nova tools; any Nova tool may be listed, the user approves the list)}. An unknown field is an error. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `fastlanes` (load it with `nova.tools_bundle(bundle='fastlanes')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova.fastlane_preview",
  "arguments": {
    "contract": {
      "source": { "kind": "net_monitor", "monitorIds": ["mon_3f9a1c2b7d4e"] },
      "condition": { "kind": "event_persists", "eventKinds": ["outage"], "forSeconds": 30 },
      "actions": [ { "kind": "notify", "title": "Server down" } ]
    }
  }
}
```

---

## 4. Related Tools

* [`nova.fastlane_catalog`](nova-fastlane-catalog.md) - the parts a contract may use.
* [`nova.fastlane_create`](nova-fastlane-create.md) - sets up the checked contract.
