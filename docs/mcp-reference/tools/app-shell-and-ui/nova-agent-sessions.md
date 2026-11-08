# `nova.agent_sessions`

> **Lists the agent sessions connected to Nova and whether each one is still working.**

> **Upcoming in v1.0.0-alpha.21 - not in a published release yet.** The current setup does not have this tool.

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.agent_sessions` shows which agent sessions (Claude Code, Codex and other MCP clients that connect through Nova's connector) talk to Nova, and in which state:

| State | Meaning |
| :--- | :--- |
| `active` | The session called Nova within the last 2 minutes. |
| `idle` | The agent's processes are alive, but it has been quiet. |
| `disconnected` | The agent is still running, but its connection to Nova is gone. |
| `exited` | The agent session has ended. |
| `unknown` | Nova cannot check this session, for example an older connector (`relay: "legacy_unverified"`). |

Nova checks each session's processes itself instead of trusting what the session reports. Sessions appear as soon as their connector talks to Nova; after a Nova restart a session shows up again with its next call.

Your own session (`isCaller: true`) comes with its folder, conversation id and process details. Other sessions are only summarized: state, client and folder name.

Every session also shows what it used:

| Field | Meaning |
| :--- | :--- |
| `callCount` | Nova calls of this session since Nova started. |
| `currentTool` | The Nova call running right now, or `null`. |
| `usage.tokens` | Tokens the model processed for this session: new input, input written to the prompt cache, and output. Read from the agent's own conversation file (Claude Code, Codex). Cache reads are listed separately in `usage.cacheReadTokens`. |
| `usage.status` | `ok`, `pending` (Nova is still reading the file), `not_supported` (this client keeps no file Nova can find, e.g. Antigravity), `no_conversation`, `transcript_not_found`. |

The same numbers appear in Nova's toolbar: an agents button next to the address bar shows up while agents are connected and opens a side panel that lists them with their state, last activity, calls and tokens. Clicking a session shows its details, including the token breakdown, how it ended and the command that resumes its conversation. The panel's **Stop all** button is Nova's emergency stop.

An ended session carries `end`:

| Field | Meaning |
| :--- | :--- |
| `reason` | `graceful` (the agent exited with code 0), `suspected_failure` (any other exit code, for example a crash or a closed terminal), `unclassified` (Nova only knew the connector, not the agent). |
| `exitCode` | The agent's exit code, when Nova knew the agent's process. |
| `openWork` | Why the end looks unfinished: `tool_call_in_flight:<tool>` (a Nova call was still running) or `active_until_end` (the session was working with Nova within its last 2 minutes). |
| `interrupted` | `true` when the session ended uncleanly with work open. |

When a session you started yourself is interrupted, Nova shows a notification with the folder and, for Claude Code and Codex, the command that resumes exactly that conversation. Runs that Nova started itself (scheduled tasks) are reported by the scheduler instead. `startedByNova` tells the two apart.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `action` | `string` | No | `"list"` | `list`, `get` | list: all sessions known since Nova started. get: one session (default: your own). |
| `sessionId` | `string` | No | — | — | For action=get: the session to show. Omit for your own session. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_agent_sessions",
  "arguments": { "action": "list" }
}
```

### JSON-RPC Response
```json
{
  "content": [
    { "type": "text", "text": "2 agent session(s): 1 active, 1 idle." }
  ],
  "structuredContent": {
    "callerSessionId": "0123456789abcdef0123456789abcdef",
    "count": 2,
    "stateCounts": { "active": 1, "idle": 1 },
    "sessions": [
      {
        "sessionId": "0123456789abcdef0123456789abcdef",
        "isCaller": true,
        "state": "active",
        "relay": "registered",
        "client": { "name": "claude-code", "version": "2.1.0" },
        "conversation": { "id": "5d2c...", "_source": "env:CLAUDE_CODE_SESSION_ID", "_binding_generation": 1 },
        "folder": { "path": "C:\\Projects\\shop", "_source": "proxy_cwd" },
        "lastSeenUtc": "2026-11-08T10:15:00+00:00"
      },
      {
        "sessionId": "fedcba9876543210fedcba9876543210",
        "isCaller": false,
        "state": "idle",
        "relay": "registered",
        "client": "codex-mcp-client",
        "folderName": "shop",
        "hasConversation": true,
        "lastSeenUtc": "2026-11-08T09:58:00+00:00"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Before taking over work:** check whether the session that started it is still `active` or `idle`. Only `exited` means nobody is working on it any more; `disconnected` means the agent is still running but cannot reach Nova.
* **Your own id:** `action: "get"` without `sessionId` returns your own session, including the `sessionId` other tools can refer to.
* **`unknown` is not `exited`:** an older connector cannot be checked. Treat it as possibly still working.
* **Picking up after a crash:** an `exited` session with `end.interrupted: true` left work unfinished. Check what it last did (folder, `openWork`) before continuing it.

---

## 5. Related Tools

* [`nova.agent_activity_summary`](nova-agent-activity-summary.md)
* [`nova.app_info`](nova-app-info.md)
