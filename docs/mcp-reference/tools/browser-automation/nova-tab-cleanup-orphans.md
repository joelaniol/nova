# `nova.tab_cleanup_orphans`

Scans for and safely closes abandoned MCP-created tabs whose lease has expired, preserving user-opened tabs and preventing memory leaks in autonomous multi-agent environments.

---

## 1. Overview

In multi-agent workflows, agents frequently spawn temporary tabs via [`nova.tab_new`](nova-tab-new.md). If an agent crashes, finishes work without releasing, or loses its context, background WebView2 processes can accumulate over time.

`nova.tab_cleanup_orphans` identifies and closes these orphaned tabs. To guarantee user safety, Nova enforces strict cleanup boundaries:
* **User Tabs are Inviolable:** Tabs opened manually by the user are never flagged or closed.
* **Active Viewing Protection:** If the user is currently looking at an MCP-created tab, it is exempt from cleanup.
* **Grace Period Window (`graceMinutes`):** Tabs must be idle (no MCP tool calls, no active claim lease) for at least the grace duration (default 15 minutes).
* **Deterministic Execution:** Nova never runs hidden background cleanup threads; cleanup occurs only when explicitly triggered via this tool.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `dryRun` | `boolean` | No | `false` | — | Preview only: list orphan candidates without closing anything. |
| `graceMinutes` | `integer` | No | `15` | — | Idle window in minutes a tab must exceed (no tool activity, no live claim) to count as orphaned. Range 1-720. |
| `agentId` | `string` | No | — | — | Calling agent's ID for attribution in logs. |
<!-- /generated:parameters -->

---

## 3. Example Calls

### Preview Candidate Orphans (Dry Run)
```json
{
  "dryRun": true,
  "graceMinutes": 30
}
```

### Clean Up Orphaned Background Tabs
```json
{
  "dryRun": false,
  "graceMinutes": 15
}
```

---

## 4. Return Value Structure

```json
{
  "dryRun": false,
  "scannedTabs": 8,
  "closedCount": 2,
  "closedTabs": [
    {
      "targetId": "tab-108",
      "url": "https://example.com/temporary-search",
      "idleMinutes": 42,
      "openedByAgent": "subagent-crawler-2"
    },
    {
      "targetId": "tab-111",
      "url": "https://example.com/receipt-view",
      "idleMinutes": 18,
      "openedByAgent": "subagent-billing"
    }
  ]
}
```

---

## 5. Related Tools & Documentation

* [`nova.tabs`](nova-tabs.md) — Query open tabs and inspect `mcpOrigin.orphaned` status.
* [`nova.tab_close`](nova-tab-close.md) — Explicitly close a single known tab.
* [`nova.tab_release`](nova-tab-release.md) — Voluntarily release a claim before closing.
* [Sandbox Isolation Architecture](../../../core-features/sandbox-isolation.md) — Multi-session boundary separation.
