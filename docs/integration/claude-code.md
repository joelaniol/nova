# Integrating Anthropic Claude Code

**Start here:** use Nova's connection wizard, click **Connect** if offered, and restart your AI program. Then follow the [first-task Quickstart](../getting-started/quickstart.md). The sections below cover manual configuration and advanced workflows.

This guide explains how to connect Anthropic's **Claude Code** CLI assistant with **Nova AI Workspace** for autonomous, verified browser automation.

---

## 1. Overview

Claude Code talks to Nova over the Model Context Protocol (MCP) through Nova's stdio bridge, `NovaBrowser.McpProxy.exe`. Claude Code starts the bridge and speaks MCP with it over standard input/output; the bridge forwards every request to Nova's local MCP server (`http://127.0.0.1:27183/mcp` by default) and adds Nova's access token itself.

Because the bridge reads the current address and token from Nova's runtime file on every connect, your Claude Code config never contains a token, keeps working after Nova restarts or changes its port, and starts Nova for you if it is not running yet.

---

## 2. Configuration Setup

### A. Automatic (recommended)
Nothing to do: when Nova starts, it adds a `nova` entry to Claude Code's user config (`~/.claude.json`) and keeps it up to date. Restart Claude Code once afterwards, then run `/mcp` in Claude Code — `nova` should be listed as connected.

If the entry is missing, open the connection wizard in Nova's settings and choose Claude Code.

### B. Manual
If you prefer to add it yourself, point Claude Code at the bridge copy in your Nova profile folder:

```powershell
claude mcp add --scope user nova -- "$env:LOCALAPPDATA\nova-cognitive\Nova\bin\NovaBrowser.McpProxy.exe"
```

The entry in `~/.claude.json` then looks like this:

```json
{
  "mcpServers": {
    "nova": {
      "command": "C:\\Users\\<you>\\AppData\\Local\\nova-cognitive\\Nova\\bin\\NovaBrowser.McpProxy.exe"
    }
  }
}
```

> [!NOTE]
> Installations from before the product rename keep their profile in `%LOCALAPPDATA%\NovaBrowser`; the bridge is then at `%LOCALAPPDATA%\NovaBrowser\bin\NovaBrowser.McpProxy.exe`. Use the folder that exists on your machine.

> [!TIP]
> Prefer the user-level entry over a project `.mcp.json`. A project entry takes precedence inside that repository, so an outdated one there hides the working user entry.

---

## 3. Automated Onboarding (`nova.install_onboarding`)

For recurring project work, you can optionally install Nova's reference files in a project folder you choose. This is not needed for your first browser task.

Nova writes references under `.nova/` and marked sections in supported project agent files. It does not change Claude Code's permission configuration. Follow [Advanced onboarding](../getting-started/advanced-onboarding.md) for the folder confirmation and current tool options.

---

## 4. Session Startup Contract

The agent should load Nova's current instructions and discover the capabilities needed for the task. You do not need to paste this sequence into every chat. Custom workflows can use the [explicit bootstrap guide](../getting-started/advanced-onboarding.md#explicit-session-bootstrap).

---

## 5. Token Optimization Best Practices for Claude Code

1. **Minimal Output Mode:** When querying tabs or crawl results, always request minimal output to conserve context tokens:
   ```json
   nova.tabs({ "outputDetail": "minimal" })
   ```
2. **Target Claiming in Subagents:** When using subagents, always claim the tab explicitly:
   ```json
   nova.tab_claim({ "targetId": "d2d64991", "agentId": "subagent-catalog" })
   ```
   This prevents concurrent subagents from switching URLs or clicking elements out from under each other.
3. **Structured DOM Over Full Vision:** Prefer `nova.read_text_structured` or `nova.extract_table` over `nova.capture_screenshot`. Screenshots should only be captured when visual verification (EVM) is strictly necessary.
4. **Feed Back Learned Fast-Paths:** If Claude solves a difficult cookie consent wall or dynamic modal, store it for future sessions:
   ```json
   nova.pks_upsert({
     "scope": "domain:example.com",
     "phenomenon": {
       "id": "cookie-banner",
       "fingerprint": { "type": "dom_signature", "value": "#cmpbox" },
       "playbook": { "steps": [{ "action": "click", "selector": "#cmpbox button.accept" }] }
     }
   })
   ```

---

## Next Steps

* Explore [Claude Desktop Integration](claude-desktop.md) if you also use the graphical desktop client.
* Learn about [OpenAI Codex](openai-codex.md) and [Google Antigravity](google-antigravity.md) configurations.
