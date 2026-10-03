# Agent & MCP Connection Issues

This guide resolves common connection, discovery, and handshake failures across **Anthropic Claude**, **Google Antigravity / Gemini**, **OpenAI Codex**, and custom MCP clients.

---

## 1. Named Pipe Errors (`Pipe not found` or `Access Denied`)

### Symptoms
* Agent client hangs indefinitely on startup.
* Stdio Proxy outputs: `Failed to connect to Named Pipe \\.\pipe\nova-mcp`.

### Causes & Diagnosis
1. **Nova is not running:** Nova creates its Named Pipe when `NovaAIWorkspace.exe` launches and **MCP Remote Control** is enabled.
2. **User Context Mismatch:** Nova enforces Windows kernel-level `PipeOptions.CurrentUserOnly` security. If Nova runs under User Account A (or elevated as Administrator) and the CLI runs under User Account B (non-elevated), Windows kernel ACLs strictly block the connection.

### Resolution
* Verify the pipe exists in your current user session using PowerShell:
  ```powershell
  Get-ChildItem \\.\pipe\ | Where-Object { $_.Name -match "nova" }
  ```
* If Nova and your agent CLI are running under different privilege levels (e.g. one as Admin and one normal), launch both from the same user context.

---

## 2. Claude Desktop Hammer Icon Missing

### Symptoms
* Claude Desktop opens normally, but no hammer icon appears in the prompt composer.

### Causes & Diagnosis
1. **Invalid JSON Escaping:** In `%APPDATA%\Claude\claude_desktop_config.json`, single backslashes in Windows paths (e.g. `C:\Program Files\...`) break JSON parsing.
2. **Missing MCP Proxy Binary:** Claude Desktop only communicates over `stdio`. Pointing directly to `NovaAIWorkspace.exe` fails because it is a GUI application, not a stdio server.

### Resolution
* Ensure your configuration points to **`NovaBrowser.McpProxy.exe`** with escaped backslashes:
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
* Inspect Claude Desktop log files in `%APPDATA%\Claude\logs\mcp.log` or `mcp-server-nova.log` for exact startup error traces.

---

## 3. Google Antigravity & Gemini CLI Issues

### Symptoms
* Running `/mcp list` in Gemini CLI shows Nova as `DISCONNECTED` or tools fail with HTTP 401 Unauthorized.

### Causes & Diagnosis
1. **Terminal Caching Daemon:** Gemini CLI and Antigravity run background runner daemons that cache MCP configuration files (`.gemini/settings.json`). Editing the file while the daemon runs will not apply changes.
2. **Rotating Bearer Token Mismatch:** When communicating over HTTP (`http://127.0.0.1:27183/mcp`), Nova rotates its cryptographic Bearer token on every workspace restart. If the configuration holds a stale token, requests return `401 Unauthorized`.

### Resolution
1. **Fetch Latest Bearer Token:**
   Open the root `.mcp.json` file in your workspace directory and copy the current token from the `headers` block:
   ```json
   "headers": {
     "Authorization": "Bearer <LATEST_TOKEN_HERE>"
   }
   ```
2. **Reload or Restart Terminal:**
   Inside Gemini CLI / Antigravity, trigger a reload:
   ```
   /mcp reload
   ```
   If tools remain unresponsive, fully close and restart the terminal window to terminate cached daemon child processes.

---

## 4. Client Reports "Empty Tool Output" (`--mirror-structured-content`)

### Symptoms
* Nova executes a tool call successfully (e.g. `nova.tabs` or `nova.read_text_structured`), but the agent responds with: *"The tool returned no output"* or *"Empty response"*.

### Cause
Modern Model Context Protocol specifications support **`structuredContent`** (native JSON objects returned alongside text blocks). Several client implementations (including Cursor, Kiro, Goose, and certain Continue versions) discard the `structuredContent` object and only parse `content[0].text`.

### Resolution
Enable the Stdio Proxy's built-in compatibility mirror by appending the `--mirror-structured-content` switch:

```json
{
  "mcpServers": {
    "nova": {
      "command": "NovaBrowser.McpProxy.exe",
      "args": ["--pipe", "nova-mcp", "--mirror-structured-content"]
    }
  }
}
```

When this flag is active, Nova automatically serializes the structured JSON payload into the plain text content block, ensuring 100% visibility for legacy or restrictive agent clients.

---

## 5. Renderer Stalls & Bot Challenge Freezes (`cdp.renderer_stalled`)

### Symptoms
* A navigation or DOM query on heavy sites (e.g., AliExpress, Cloudflare Turnstile, Cloudflare WAF, Akamai) times out after 10–30 seconds with error `cdp.renderer_stalled`.

### Cause
Anti-bot systems intentionally suspend or freeze the JavaScript rendering thread (`window.stop()` or intensive worker loops) until a human solves an interactive captcha.

### Resolution
1. **Do not repeat the action in a tight loop:** Retrying the identical tool call will repeatedly hit the stalled thread.
2. **Inspect Page State:** Call `nova.perceive(mode="state")` or capture a visual proof crop via `nova.capture_screenshot(fullPage=false)`.
3. **Request Human Assistance:** Inform the human operator that an anti-bot challenge is blocking the page so they can complete the verification challenge directly in the Nova GUI window.
