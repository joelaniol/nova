# Integrating Anthropic Claude Code

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

Once Claude Code connects to Nova for the first time, execute the onboarding tool:

```
Run nova.install_onboarding to setup project documentation.
```

### What `install_onboarding` Does:
1. **Generates `.nova/nova-mcp.quick.md`:** The compact tool router, bootstrap instructions, and recovery procedures.
2. **Generates `.nova/nova-mcp.md`:** The comprehensive 100KB+ reference of all 400+ tools, schemas, and parameter options.
3. **Injects the Session Marker Block into `CLAUDE.md` / `AGENTS.md`:**
   ```markdown
   <!-- NOVA-BROWSER-MCP-START version=4.40.0 -->
   ## Nova MCP — Session startup
   1. Before the first Nova tool call, read .nova/nova-mcp.quick.md.
   2. Start session discovery: get_instructions -> tools_bundle(includeUnavailable=true).
   3. Call task tools directly. Use tabs for target choice, explicit tab_claim for ownership.
   ...
   <!-- NOVA-BROWSER-MCP-END -->
   ```

> [!IMPORTANT]
> **Zero Permission Pollution:** Nova strictly adheres to agent boundary policies. `nova.install_onboarding` will **never** modify your `.claude/settings.json` or force-approve tool permissions. Tool execution approvals remain 100% under your explicit control.

---

## 4. Session Startup Contract

Every Claude Code session calling Nova tools must execute the two-call bootstrap:

```
1. nova.get_instructions(taskKeywords=["search", "web", "automation"])
2. nova.tools_bundle(bundle="browser_automation", includeUnavailable=true)
```

This handshake:
* Loads active domain notes and site-specific quirks into Claude's context.
* Returns `bundleCatalog` (the authoritative list of capability bundles).
* Clears the bootstrap warning flag on the server.

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
