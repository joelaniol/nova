# Integrating Anthropic Claude Desktop

This guide explains how to connect Anthropic's official **Claude Desktop** application on Windows with **Nova AI Workspace**.

---

## 1. Overview

Claude Desktop connects to MCP servers exclusively via standard input/output (`stdio`). Because Nova AI Workspace runs as a native Windows application communicating over high-speed Named Pipes, the bundled **`NovaBrowser.McpProxy.exe`** acts as the bridge between Claude Desktop's stdio stream and Nova's Named Pipe engine.

```mermaid
flowchart LR
    CD["Claude Desktop (GUI)"] -->|stdio (stdin / stdout)| Proxy["NovaBrowser.McpProxy.exe"]
    Proxy -->|Named Pipe (\\\\.\\pipe\\nova-mcp)| Nova["Nova AI Workspace (NovaAIWorkspace.exe)"]
```

---

## 2. Configuration Setup

1. Open Windows File Explorer and navigate to your Claude configuration folder:
   ```
   %APPDATA%\Claude\
   ```
   *(Full path: `C:\Users\<YourUsername>\AppData\Roaming\Claude\`)*

2. Open `claude_desktop_config.json` in a text editor (create the file if it does not exist).

3. Add the `nova` server configuration:

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

> [!IMPORTANT]
> **Windows Path Escaping:** In JSON files, backslashes must be doubled (`\\\\`). Alternatively, you can use forward slashes (e.g., `"C:/Program Files/Nova/NovaBrowser.McpProxy.exe"`).

---

## 3. Starting the Session

1. **Start Nova AI Workspace:** Launch `NovaAIWorkspace.exe`. Make sure **MCP Remote Control** is enabled in Settings.
2. **Start Claude Desktop:** Open (or restart) Claude Desktop.
3. **Verify the Connection:** Look at the bottom-right corner of Claude Desktop's chat composer. You should see a **hammer icon** indicating active MCP tools. Clicking it should list Nova's tool capabilities.

---

## 4. Troubleshooting

### Issue: Hammer icon does not appear or shows an error
1. **Check if Nova is running:** The proxy expects Nova's Named Pipe (`\\.\pipe\nova-mcp`) to be available. Open PowerShell and verify:
   ```powershell
   Get-ChildItem \\.\pipe\ | Where-Object { $_.Name -match "nova" }
   ```
2. **Inspect Claude Desktop Logs:**
   Navigate to `%APPDATA%\Claude\logs\` and inspect `mcp.log` or `mcp-server-nova.log`.
3. **Test the Proxy Standalone:**
   Open PowerShell and test running the proxy directly:
   ```powershell
   & "C:\Program Files\Nova\NovaBrowser.McpProxy.exe" --pipe nova-mcp
   ```
   If it connects successfully, it will wait silently for JSON-RPC frames on stdin. Press `Ctrl+C` to exit.

---

## Next Steps

* Set up CLI workflows with **[Claude Code](claude-code.md)**.
* Learn how to configure **[OpenAI Codex](openai-codex.md)** and **[Google Antigravity](google-antigravity.md)**.
