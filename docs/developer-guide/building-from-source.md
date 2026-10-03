# Building Nova AI Workspace from Source

> [!NOTE]
> Instructions for configuring your local development environment and compiling Nova AI Workspace from source on Windows.

---

## 1. Prerequisites

Nova is a native Windows 11 / Windows 10 (x64) application. Ensure your development workstation meets the following requirements:

* **Operating System:** Windows 10 Version 19041 (20H1) or later; Windows 11 recommended.
* **Runtime:** Microsoft Edge WebView2 Runtime (Evergreen version installed by default on Windows 11).
* **Build SDK:** Nova utilizes a repository-local .NET 8 SDK located in `.dotnet/dotnet.exe` to ensure deterministic, reproducible builds across machines.

---

## 2. Repository Structure

```
NovaBrowser/
+-- .dotnet/                   # Local .NET 8 SDK (do not use system dotnet)
+-- NovaBrowser/               # Main WinUI 3 + WebView2 host project
+-- NovaBrowser.Outrider/      # Isolated worker subprocess project
+-- NovaBrowser.McpProxy/      # Standalone MCP proxy helper
+-- NovaBrowser.TerminalRunner/# ConPTY terminal runner process
+-- NovaBrowser.Tests/         # xUnit unit and integration test suite
+-- dist/                      # Publish destination for deployable binaries
+-- build.ps1                  # Primary clean publish script
+-- rebuild.bat                # Fast local developer build and smoke loop
```

---

## 3. Compilation Commands

> [!WARNING]
> Always invoke the repository-local SDK at `.dotnet\dotnet.exe`. Do not use the global system `dotnet` command, as SDK version mismatches can break WinUI 3 XAML compilation.

### 3.1 Quick Developer Build & Smoke Gate (`rebuild.bat`)
The fastest way to verify changes is the repository build script:

```cmd
rebuild.bat
```

To publish without executing the post-build smoke test:
```cmd
rebuild.bat --publish-only
```

### 3.2 Clean Production Publish (`build.ps1`)
To produce clean, self-contained publish artifacts in `dist/`:

```powershell
powershell -ExecutionPolicy Bypass -File .\build.ps1 -RuntimeIdentifier win-x64 -Configuration Release -Clean
```

---

## 4. Output Artifacts in `dist/`

A successful build produces deployable binaries in the `dist/` directory:

| Binary | Description |
| :--- | :--- |
| **`NovaAIWorkspace.exe`** | The primary browser executable (host process). |
| **`NovaBrowser.Outrider.exe`** | The supervised native worker subprocess. |
| **`NovaBrowser.McpProxy.exe`** | Lightweight MCP proxy utility. |
| **`NovaBrowser.TerminalRunner.exe`** | ConPTY terminal bridge worker. |
| **`Assets/`** | WinUI icons, Aurora brand marks, and static resources. |

---

## 5. Naming Contract & Process Identity

* **Product Display Name:** Nova AI Workspace
* **Short Name:** Nova
* **Primary Binary & Process:** `NovaAIWorkspace.exe`
* **C# Project & Namespace:** `NovaBrowser`
