# Agent & MCP Connection Issues

This guide resolves common connection, discovery, and handshake failures across **Anthropic Claude**, **Google Antigravity / Gemini**, **OpenAI Codex**, and custom MCP clients.

---

## 1. The Agent Cannot Reach Nova

### Symptoms
* The AI program lists Nova as failed or disconnected, or shows no Nova tools at all.
* The agent says it has no browser tools, or its Nova calls time out.

### How the connection works
Your AI program starts Nova's stdio bridge, `NovaBrowser.McpProxy.exe`. The bridge reads Nova's current address and access token from Nova's profile folder and forwards every request to Nova's local server (`http://127.0.0.1:27183/mcp` by default). If Nova is not running, the bridge starts it and waits up to 90 seconds for it to become ready.

Nova's profile folder is `%LOCALAPPDATA%\nova-cognitive\Nova`; installations from before the product rename use `%LOCALAPPDATA%\NovaBrowser`. Use whichever exists on your machine in the commands below.

### Diagnosis, step by step
1. **Is Nova's server up?** With Nova running:
   ```powershell
   Invoke-RestMethod http://127.0.0.1:27183/health
   ```
   `status : ready` means yes. If you changed Nova's port in the settings, use that port. No answer: start Nova and check that **Allow agents to control the browser** is ticked in its settings (it is by default).
2. **Does the bridge exist and work?**
   ```powershell
   & "$env:LOCALAPPDATA\nova-cognitive\Nova\bin\NovaBrowser.McpProxy.exe" --self-test
   ```
   Expected: `NovaBrowser.McpProxy self-test OK`. If the file is missing, start Nova once; it puts the bridge there.
3. **Does your AI program point at that bridge?** Its `nova` entry must start exactly this file. An entry with `--pipe` or other unknown switches makes the bridge stop with exit code 2 — those come from outdated instructions; remove them. The only switches are `--antigravity-tool-names` (Antigravity only) and `--mirror-structured-content`.
4. **Read the bridge log:** `<profile folder>\Logs\novabrowser-mcp-stdio-proxy.log` records each connection attempt and why it failed.
5. **Same Windows user:** Nova and the AI program must run under the same Windows account. The bridge looks in the profile folder of the account it runs under.

The simplest repair for steps 2–3 is the connection wizard in Nova's settings: it rewrites the entry for the AI program you choose. Restart the AI program afterwards — clients read their MCP configuration only at startup.

---

## 2. Claude Desktop Shows No Nova Tools

### Causes & Diagnosis
1. **Invalid JSON escaping:** In `%APPDATA%\Claude\claude_desktop_config.json`, every backslash in a Windows path must be doubled. A single backslash makes the whole file invalid.
2. **Wrong program:** The entry must start `NovaBrowser.McpProxy.exe`, not `NovaAIWorkspace.exe` — Nova itself is a window application, not an MCP server on stdio.
3. **Claude Desktop still running in the tray:** it reads the config only when it starts. Quit it from the system tray, then start it again.

### Resolution
* The entry should look like this (with your user name in place of `<you>`):
  ```json
  {
    "mcpServers": {
      "nova": {
        "command": "C:\\Users\\<you>\\AppData\\Local\\nova-cognitive\\Nova\\bin\\NovaBrowser.McpProxy.exe"
      }
    }
  }
  ```
* Claude Desktop's own logs are in `%APPDATA%\Claude\logs\` (`mcp.log`, `mcp-server-nova.log`).

---

## 3. Google Antigravity & Gemini CLI Issues

Antigravity has two quirks of its own: it rejects tool names with dots, and it passes only the text of a tool result to the model. Nova's entry for Antigravity therefore starts the bridge with `--antigravity-tool-names`, which handles both. Nova keeps that entry in `%USERPROFILE%\.gemini\config\mcp_config.json` up to date by itself.

Symptoms, causes and fixes are collected in **[MCP troubleshooting → Antigravity](../mcp-troubleshooting/antigravity.md)**.

---

## 4. The Agent Sees Only Summaries Instead of Data (`--mirror-structured-content`)

### Symptoms
* Nova executes a tool call successfully (e.g. `nova.tabs`), but the agent only sees a short summary such as *"Use structuredContent.tabs"*, or reports an empty result.

### Cause
Nova returns the actual data as **`structuredContent`** (a JSON object next to the text block), as the MCP specification allows. Some MCP clients pass only the text block to the model and drop `structuredContent`.

### Resolution
Add `--mirror-structured-content` to the `args` of that program's `nova` entry:

```json
{
  "mcpServers": {
    "nova": {
      "command": "C:\\Users\\<you>\\AppData\\Local\\nova-cognitive\\Nova\\bin\\NovaBrowser.McpProxy.exe",
      "args": ["--mirror-structured-content"]
    }
  }
}
```

The bridge then copies the structured data into the text block, so the model sees it. Claude Code and Codex read `structuredContent` and do not need the switch; for Antigravity it is already part of `--antigravity-tool-names`.

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
