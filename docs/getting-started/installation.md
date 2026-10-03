# Installation & System Requirements

This guide outlines system requirements and step-by-step instructions for installing **Nova AI Workspace** on Windows.

---

## 1. System Requirements

Nova AI Workspace is built natively for 64-bit Windows environments.

| Component | Minimum Requirement | Recommended |
| :--- | :--- | :--- |
| **Operating System** | Windows 10 (version 1809 / build 17763 or newer) | Windows 11 (23H2 or newer) |
| **Architecture** | 64-bit (x64) | 64-bit (x64) |
| **Processor** | 2-core x64 CPU | 4-core+ modern x64 CPU |
| **Memory (RAM)** | 4 GB RAM | 8 GB+ RAM (especially for multi-sandbox workflows) |
| **Disk Space** | 500 MB free space | 2 GB+ (for local Whisper models, caches, recordings) |
| **Runtime 1** | **Microsoft Edge WebView2 Runtime (Evergreen)** | Evergreen Runtime (pre-installed on Windows 10/11) |
| **Runtime 2** | **Microsoft .NET 8 Desktop Runtime (x64)** | Bundled in self-contained installer |

> [!NOTE]
> Microsoft Edge WebView2 Evergreen Runtime is installed by default on modern Windows 10 and 11 installations. If missing, it can be downloaded from Microsoft's official [WebView2 Evergreen Bootstrapper](https://developer.microsoft.com/en-us/microsoft-edge/webview2/).

---

## 2. Package Options

Nova AI Workspace is released in two formats:

### Option A: Standard Setup Installer (`NovaSetup.exe`)
* **Recommended for end users and workstations.**
* Automatically configures user-level registry entries, Start Menu shortcuts, and sets up path environment variables.
* Packages all necessary dependencies (.NET 8 self-contained).

### Option B: Portable Archive (`NovaAIWorkspace.zip`)
* **Recommended for developers, CI/CD runners, and custom workspaces.**
* No administrator privileges required; extract anywhere (e.g. `C:\Tools\Nova\` or user workspace).
* Portable directory must preserve the relative paths of the three sibling executables.

---

## 3. The Core Executables

A valid Nova installation consists of three complementary binaries in the same directory:

```
Nova/
├── NovaAIWorkspace.exe          # Main application (WinUI 3 Host, WebViews, Local MCP Server)
├── NovaBrowser.Outrider.exe     # Outrider isolation process (native hardware & audio worker)
└── NovaBrowser.McpProxy.exe     # Stdio MCP Proxy (bridges CLI/Desktop clients to Named Pipes)
```

> [!IMPORTANT]
> `NovaBrowser.Outrider.exe` **must remain in the exact same directory** as `NovaAIWorkspace.exe`. The parent application lazily spawns Outrider via a private, parent-governed Named Pipe for risky native operations (hardware diagnostics, local Whisper transcription, audio capture). If Outrider is missing or moved, those capabilities fail-closed.

---

## 4. Post-Installation Verification

1. **Launch the Workspace:**
   Double-click `NovaAIWorkspace.exe` or launch from Start Menu. The Nova main window should open with the initial tab interface.
2. **CLI Smoke Check:**
   Open PowerShell or Windows Terminal in the installation directory and run:
   ```powershell
   .\NovaAIWorkspace.exe --version
   ```
3. **Verify MCP Discovery Pipe:**
   When Nova is running, it opens a secure, user-scoped Named Pipe (`\\.\pipe\nova-mcp`). You can verify pipe availability in PowerShell:
   ```powershell
   Get-ChildItem \\.\pipe\ | Where-Object { $_.Name -match "nova" }
   ```

---

## 5. Security & Antivirus Notes

* **Local-Only Bound:** Nova binds its internal HTTP endpoints and Named Pipes exclusively to `127.0.0.1` (`IPAddress.Loopback`) and `PipeOptions.CurrentUserOnly`. It does not accept remote network connections.
* **Windows SmartScreen:** If installing a pre-release or self-compiled build without a public code-signing certificate, Windows SmartScreen may show a *"Windows protected your PC"* notification. Click **More info** $\rightarrow$ **Run anyway** to proceed.

---

## Next Step

Proceed to **[First Run & UI Tour](first-run.md)** to configure your workspace profiles and learn the navigation layout.
