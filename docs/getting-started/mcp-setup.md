# How the Agent Connection Works

Nova AI Workspace provides seamless integration with external AI agent programs (including Anthropic Claude Code, OpenAI Codex, Google Antigravity, Cursor, and Claude Desktop) through the **Model Context Protocol (MCP)**.

Nova's built-in **Connection Wizard** (**Menu → Settings → AI & agents → Setup**) automates client registration. You do not need to manually configure JSON files or copy API keys to get started.

---

## 1. The MCP Proxy Runner (`NovaBrowser.McpProxy.exe`)

When an AI program connects to Nova, it communicates with Nova's native proxy runner:
```
%LOCALAPPDATA%\NovaBrowser\bin\NovaBrowser.McpProxy.exe
```

```mermaid
flowchart LR
    Agent["External AI Program<br/>(Claude Code, Codex, Antigravity)"] -->|Standard I/O (stdio)| Runner["Native MCP Proxy Runner<br/>(%LOCALAPPDATA%\NovaBrowser\bin\NovaBrowser.McpProxy.exe)"]
    Runner -->|Local HTTP / SSE<br/>http://127.0.0.1:27183/mcp| Nova["Nova AI Workspace<br/>(Desktop UI & Tool Engine)"]
```

### Why Does the Configuration Point to `%LOCALAPPDATA%`?
Software updates or developer rebuilds periodically wipe and regenerate the application directory (`dist/`). If client configurations pointed directly to the build folder, every update would break your AI program's connection. 

Nova deploys a rebuild-stable, mutex-synchronized copy of the proxy executable into `%LOCALAPPDATA%\NovaBrowser\bin\`. This path remains permanent across updates, reboots, and workspace rebuilds.

---

## 2. Lazy Autostart & Reconnection

You do not need to keep Nova open before launching your AI tools:
* **Automatic Cold-Start:** When an agent CLI issues a tool call while Nova is closed, `NovaBrowser.McpProxy.exe` automatically starts Nova in the background (using an autostart lease to prevent duplicate instances).
* **Job Object Breakaway:** The browser is spawned with process breakaway guarantees (`CREATE_BREAKAWAY_FROM_JOB`), ensuring the browser stays open even if your agent terminal session terminates.
* **Zero Token Management:** The proxy automatically reads the current access token from encrypted local storage (`mcp-identity.dat`). You never need to manually paste bearer tokens into client config files.
* **Transparent Reconnection:** If Nova restarts or reloads, the proxy runner reconnects upstream automatically without interrupting the AI program's active session.

---

## 3. Client Configuration Reference

When Nova's Connection Wizard configures an AI program, it registers the native proxy runner with client-specific settings:

### Anthropic Claude Code (`~/.claude.json`)
```json
{
  "mcpServers": {
    "nova": {
      "command": "C:\\Users\\<user>\\AppData\\Local\\NovaBrowser\\bin\\NovaBrowser.McpProxy.exe"
    }
  }
}
```

### OpenAI Codex (`~/.codex/config.toml`)
```toml
[mcp_servers.nova]
command = "C:\\Users\\<user>\\AppData\\Local\\NovaBrowser\\bin\\NovaBrowser.McpProxy.exe"
```

### Claude Desktop (`%APPDATA%\Claude\claude_desktop_config.json`)
```json
{
  "mcpServers": {
    "nova": {
      "command": "C:\\Users\\<user>\\AppData\\Local\\NovaBrowser\\bin\\NovaBrowser.McpProxy.exe"
    }
  }
}
```

### Google Antigravity & Gemini CLI (`%USERPROFILE%\.gemini\config\mcp_config.json`)
```json
{
  "mcpServers": {
    "nova": {
      "command": "C:\\Users\\<user>\\AppData\\Local\\NovaBrowser\\bin\\NovaBrowser.McpProxy.exe",
      "args": ["--antigravity-tool-names"]
    }
  }
}
```
*(The `--antigravity-tool-names` switch projects tool names from `nova.tabs` to `nova_tabs`, adhering to Antigravity's identifier rules).*

---

## 4. Why Must You Restart the AI Program?

AI programs read their MCP configuration files once during process startup. A CLI terminal or desktop client that was already running when you clicked **Connect** in Nova retains its previous settings. 

* **Terminal CLIs:** Close and restart your terminal session or run a new CLI instance.
* **Claude Desktop:** Completely quit the application from the Windows system tray before relaunching it.

---

## 5. Verifying Your Connection

Once restarted, verify that your AI program recognizes Nova:
1. In Claude Code, run `/mcp` to confirm `nova` is listed as connected.
2. Ask your agent: *"What tabs are open in Nova?"* or prompt it to call [`nova.app_info`](../mcp-reference/tools/app-shell-and-ui/nova-app-info.md).
3. If the connection fails, verify the runner using the built-in self-test:
   ```powershell
   & "$env:LOCALAPPDATA\NovaBrowser\bin\NovaBrowser.McpProxy.exe" --self-test
   ```
   *(Expected output: `NovaBrowser.McpProxy self-test OK`).*

---

## Related Documentation

* **[MCP Stdio Proxy Architecture](../components/mcp-proxy.md)** — In-depth technical specification of the proxy runner and autostart engine.
* **[Agent Connection Troubleshooting](../troubleshooting/agent-connection-issues.md)** — Solutions for connection timeouts, missing tools, and log inspection.
* **[Agent Governance & Settings](../user-guide/settings/agent-governance-and-mcp.md)** — Permission controls and settings catalog.
* **[Quickstart Guide](quickstart.md)** — First-time orientation and five-minute walkthrough.
