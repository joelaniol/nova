# First Run & UI Tour

When you launch **Nova AI Workspace** for the first time, you are presented with a unified workspace combining modern browser ergonomics with native agentic controls.

---

## 1. The Setup Wizard

On its initial boot, Nova opens the **Setup Wizard** (`nova.setup_wizard_open`) to guide you through essential preferences:

* **Theme Selection:** Dark Mode (default, optimized for developer ergonomics) or Light Mode.
* **Search Engine & Start URL:** Configure your preferred landing surface.
* **MCP Remote Control:** Enable the local Model Context Protocol engine so that external AI agents (Claude Code, Antigravity, Codex) can connect via Named Pipes and stdio proxies.
* **Initial Sandboxes:** Initialize your first isolated browsing environments (e.g., Sandbox A for work, Sandbox B for personal research).

---

## 2. Workspace Anatomy

```
+-----------------------------------------------------------------------------------+
|  [+] [Tab 1: Dashboard] [Tab 2: Docs]            [Sandbox: A (Work) v] [-][ ][x]  |
+-----------------------------------------------------------------------------------+
|  [<] [>] [R]  https://example.com/portal                   [Lock] [Cookie] [MCP]  |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|                                                                                   |
|                           WebView2 Active Surface                                 |
|                                                                                   |
|                                                                                   |
+-----------------------------------------------------------------------------------+
| >_ Terminal Dock: powershell.exe                      [^ Expand] [v Hide] [x]     |
| PS E:\Projects> git status                                                        |
+-----------------------------------------------------------------------------------+
```

### A. The Omnibox & Navigation Bar
* **Deterministic Navigation:** Back, Forward, Reload, and URL entry.
* **Security & Inspection Indicators:**
  * **SSL / Certificate Lock:** Inspects native X.509 certificate chains and TLS negotiation.
  * **Cookie & Site Data Badge:** Opens the native Site Data Inspector (`nova.storage_inspect`, `nova.cookie_list`).
  * **MCP Activity Glow:** Visually pulses when an active AI agent is reading the DOM, dispatching Bézier mouse movements, or executing a task.

### B. Sandbox Profile Switcher (Top-Right)
* **What are Sandboxes?**
  Unlike typical browser profiles that require opening completely separate OS windows, Nova embeds multiple **Sandboxes** (`A`, `B`, `C`, ...) inside the same application window.
* **Total Isolation:**
  Each sandbox has its own isolated `EBWebView` user data folder, independent cookie jars (allowing you to be logged into two different accounts on the same site simultaneously), distinct proxy settings (SOCKS5/HTTP), and unique anti-fingerprint seeds.
* **Agent Control:**
  Agents can switch contexts programmatically using `nova.sandbox_context` or `nova.resolve_sandbox`.

### C. The Embedded Terminal Dock (ConPTY)
* **Native Console in Workspace:**
  Located at the bottom of the window, the Terminal Dock embeds a persistent Windows Pseudo Console (ConPTY) running PowerShell, CMD, or Git Bash.
* **Agent-Accessible:**
  AI agents can open terminal sessions, run build scripts, git operations, or CLI tools through `nova.terminal_open`, `nova.terminal_run_command`, and `nova.terminal_read`.
* **State Persistence:**
  Terminal sessions survive UI reloads, tab navigation, and background task execution without losing shell state.

### D. The Downloads Drawer & Dialog Inspector
* **Downloads Drawer:**
  Active downloads appear in a clean, non-intrusive tray displaying file size, transfer rate, and security validation status.
* **Native Dialog Automation:**
  When web applications trigger native Win32 dialogs (File Pickers, HTTP Basic Authentication prompts, Client Certificate selectors), Nova does not freeze. It surfaces them through the **Dialog Inspector**, allowing both human users and AI agents (`nova.ui_inspect_native_dialog`) to inspect and resolve prompts cleanly.

### E. Permission Center
* Accessed via Settings or `nova.permission_center_get`, this hub manages device permissions (Camera, Microphone, Notifications, Geolocation).
* Supports **three-tier authorization**:
  1. Global defaults (Allow, Deny, Prompt).
  2. Per-origin overrides (e.g. allow mic on `meet.google.com`, block on others).
  3. Single-session grants with instant emergency revocation (`nova.media_stop_all`).

---

## Next Step

Now that you understand the UI, proceed to the **[5-Minute Quickstart](quickstart.md)** to connect an AI agent and execute your first automated task.
