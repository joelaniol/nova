# Integrating OpenAI Codex & Google Antigravity

This guide covers setting up **OpenAI Codex CLI** and **Google Antigravity / Gemini** agents to control **Nova AI Workspace**, including parallel subagent orchestration.

---

## 1. OpenAI Codex CLI Setup

OpenAI Codex CLI supports MCP servers through its central configuration file.

### Configuration (`~/.codex/config.toml`)
Open `%USERPROFILE%\.codex\config.toml` (create if needed) and add the Nova server entry:

```toml
[mcp_servers.nova]
command = "C:\\Program Files\\Nova\\NovaBrowser.McpProxy.exe"
args = ["--pipe", "nova-mcp"]
```

### Running Autonomous Tasks with Codex
Once configured, you can launch autonomous tasks requiring browser verification:

```bash
codex "Audit the pricing table on https://example.com/pricing and verify subscription tiers using Nova."
```

Codex will automatically invoke Nova tools to navigate, claim the tab, extract structured pricing matrices, and verify results against live DOM evidence.

---

## 2. Google Antigravity & Gemini CLI Setup

Google Antigravity (AGY) and Gemini CLI integrate with Nova via either project-level `.mcp.json` or user-level tool definitions.

### Project Configuration (`.mcp.json`)
Place this in your active project workspace:

```json
{
  "mcpServers": {
    "nova": {
      "command": "NovaBrowser.McpProxy.exe",
      "args": ["--pipe", "nova-mcp"]
    }
  }
}
```

### Lazy Tool Schema Loading
Antigravity supports both eager tools and lazy-loaded MCP schemas:
1. Nova exposes its catalog through `nova.tools_bundle(includeUnavailable=true)`.
2. Antigravity can query specific tool schemas on demand (e.g. `nova.tools_bundle(toolName='nova.dom_extract')`), avoiding the massive token overhead of loading all 800+ schemas into the agent context upfront.

---

## 3. Multi-Agent & Subagent Swarm Workflows

Both Codex and Antigravity frequently spawn subagents (`invoke_subagent` / `delegate_task`) for parallel research, verification, and code generation. Nova provides native multi-agent coordination primitives:

```mermaid
flowchart TD
    Parent["Parent Agent (Coordinator)"]
    SubA["Subagent A (Market Researcher)"]
    SubB["Subagent B (Checkout Auditor)"]

    Nova["Nova AI Workspace Engine"]
    Tab1["Tab 1 (Leased by Subagent A)"]
    Tab2["Tab 2 (Leased by Subagent B)"]
    Board["Knowledge Board (Shared Facts)"]

    Parent -->|Spawns| SubA
    Parent -->|Spawns| SubB

    SubA -->|nova.tab_claim(tab-1)| Nova
    SubB -->|nova.tab_claim(tab-2)| Nova

    Nova --> Tab1
    Nova --> Tab2

    SubA -->|nova.board_contribute| Board
    SubB -->|nova.board_get| Board
```

### A. Preventing Tab Collisions (`nova.tab_claim`)
When multiple subagents operate simultaneously, they must not navigate or click on each other's pages:
```json
// Subagent claims exclusive access to targetId for 3 minutes (180,000 ms)
nova.tab_claim({
  "targetId": "tab-1",
  "purpose": "Product price audit",
  "leaseDurationMs": 180000
})
```
* If Subagent B attempts to click or navigate on `tab-1` while the lease is active, Nova returns an **AAG Concurrency Violation (`-32002`)**, protecting Subagent A's work.
* When finished, the subagent calls `nova.tab_release({ "targetId": "tab-1" })`.

### B. Cross-Agent Knowledge Sharing (Knowledge Board)
Subagents can exchange factual discoveries without forwarding huge conversation histories:
* **Posting a finding:**
  ```json
  nova.board_contribute({
    "topic": "competitor-pricing",
    "claim": "Pro plan is $49/mo billed annually with 14-day trial",
    "confidence": 0.95
  })
  ```
* **Reading shared findings:**
  ```json
  nova.board_get({ "topic": "competitor-pricing" })
  ```

---

## Next Steps

* Build custom agents in Python or Node.js via **[Custom Agents](custom-agents.md)**.
* Learn about the underlying [Agent Awareness Gates (AAG)](../core-features/aag.md).
