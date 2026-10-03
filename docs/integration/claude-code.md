# Integrating Anthropic Claude Code

This guide explains how to connect Anthropic's **Claude Code** CLI assistant with **Nova AI Workspace** for autonomous, verified browser automation.

---

## 1. Overview

Claude Code communicates with Nova using the Model Context Protocol (MCP) via the bundled Stdio Proxy (`NovaBrowser.McpProxy.exe`). This proxy translates Claude Code's standard input/output streams into high-performance, asynchronous Windows Named Pipe frames.

---

## 2. Configuration Setup

You can register Nova either at the **project level** (recommended for shared repositories) or at the **global user level**.

### A. Project-Level Configuration (`.mcp.json`)
Create or edit `.mcp.json` in your repository root:

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

> [!TIP]
> If `NovaBrowser.McpProxy.exe` is not in your system `PATH`, specify its full absolute path (e.g., `C:\\Program Files\\Nova\\NovaBrowser.McpProxy.exe` or `E:\\Tools\\Nova\\NovaBrowser.McpProxy.exe`).

### B. Global Configuration (`~/.claude.json`)
To enable Nova across all Claude Code sessions on your workstation, add Nova to `~/.claude.json`:

```json
{
  "mcpServers": {
    "nova": {
      "command": "C:\\Program Files\\Nova\\NovaBrowser.McpProxy.exe",
      "args": ["--pipe", "nova-mcp"]
    }
  }
}
```

---

## 3. Automated Onboarding (`nova.install_onboarding`)

Once Claude Code connects to Nova for the first time, execute the onboarding tool:

```
Run nova.install_onboarding to setup project documentation.
```

### What `install_onboarding` Does:
1. **Generates `.nova/nova-mcp.quick.md`:** The compact tool router, bootstrap instructions, and recovery procedures.
2. **Generates `.nova/nova-mcp.md`:** The comprehensive 100KB+ reference of all 800+ tools, schemas, and parameter options.
3. **Injects the Session Marker Block into `CLAUDE.md` / `AGENTS.md`:**
   ```markdown
   <!-- NOVA-BROWSER-MCP-START version=4.39.0 -->
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
   nova.tab_claim({ "targetId": "tab-1", "purpose": "Scraping product catalog" })
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
* Learn about [OpenAI Codex & Antigravity](codex-and-antigravity.md) configuration.
