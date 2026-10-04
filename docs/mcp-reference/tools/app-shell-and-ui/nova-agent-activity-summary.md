# `nova.agent_activity_summary`

> **Returns a per-agent summary of this session's MCP tool calls: call counts, tab targets, and failure reason codes.**

* **Core Feature Guide:** [Tool Observation Bus (TOB)](../../../core-features/tob.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.agent_activity_summary` aggregates the current session's MCP action log per agent: which `agentId` ran how many calls on which tabs (targets), top tools, success/failure counts, and failure reason codes. Attribution comes from an explicit `agentId` argument or from the target's claim owner; calls without either are only counted as unattributed. The tool requires the MCP action-log channel to be enabled for the session and returns `status: "action_log_disabled"` otherwise.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `agentId` | `string` | No | — | — | Only aggregate calls attributed to this agentId. Omit for all agents. |
| `sinceMinutes` | `integer` | No | `240` | 1–10080 | Look-back window in minutes over the current session's action log. Default 240 (4h). |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "2 agent(s) active in the last 240 min; 3 unattributed call(s). Details in structuredContent.agents."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "sinceMinutes": 240,
    "agentIdFilter": null,
    "agentCount": 2,
    "unattributedCalls": 3,
    "parseErrors": 0,
    "agents": [
      {
        "agentId": "agent-1",
        "toolCallCount": 42,
        "successCount": 40,
        "failureCount": 2,
        "firstAtUtc": "2026-10-02T08:00:00.0000000Z",
        "lastAtUtc": "2026-10-02T09:12:00.0000000Z",
        "targets": [
          { "targetId": "tab-1", "calls": 20, "lastTool": "nova.navigate", "lastAtUtc": "2026-10-02T09:12:00.0000000Z" }
        ],
        "targetsTruncated": false,
        "topTools": [ { "tool": "nova.navigate", "calls": 12 } ],
        "topToolsTruncated": false,
        "failureReasons": [],
        "failureReasonsTruncated": false
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Reconstructing Fleet Work:** Use this instead of reading raw logs to see what a (sub)agent fleet did, e.g. after parallel tab work.
* **Tab Affinity:** Check `targets` to verify agent-to-tab mappings when multiple subagents operate concurrently.
* **Unattributed Calls:** Calls without an `agentId` argument or a tab claim only increment `unattributedCalls`; they are not attributed to any agent row.

---

## 5. Related Tools

* [`nova.mcp_transport_log`](nova-mcp-transport-log.md)
* [`nova.app_info`](nova-app-info.md)
