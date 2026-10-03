# `nova.agent_activity_summary`

> **Returns an aggregated summary of active MCP sessions, tool execution counts, and failure rates.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 1 (Telemetry & Observability)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.agent_activity_summary` provides observability into how AI agents are interacting with Nova. It details per-agent session duration, tool invocation frequencies, error ratios, and tab allocations.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Only aggregate calls attributed to this agentId. Omit for all agents. |
| `sinceMinutes` | `integer` | No | Look-back window in minutes over the current session's action log. Default 240 (4h). |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_agent_activity_summary",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Active agents: 2. Total calls: 142. Success rate: 98.6%."
    }
  ],
  "structuredContent": {
    "ok": true,
    "activeAgents": 2,
    "totalCalls": 142,
    "errorRate": 0.014,
    "topTools": [
      "nova.navigate",
      "nova.dom_extract",
      "nova.click_selector"
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Performance Auditing:** Inspect failure rates to detect stuck automation loops early.
* **Tab Affinity:** Verify agent-to-tab mappings when multiple subagents operate concurrently.

---

## 5. Related Tools

* [`nova.mcp_transport_log`](nova-mcp-transport-log.md)
* [`nova.app_info`](nova-app-info.md)
