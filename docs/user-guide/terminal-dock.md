# Integrated Terminal Dock

> [!NOTE]
> Nova AI Workspace embeds a full-featured Windows ConPTY terminal dock directly beneath the browser canvas. Run PowerShell 7, Git CLI, build scripts, or agent CLI tools without ever leaving your browser workspace.

---

## 1. Overview & Motivation

Developers and operators constantly switch back and forth between browser tabs and external terminal windows. When an AI agent modifies code, starts a local dev server, or triggers a deployment, verifying results in the browser requires continuous Alt-Tabbing.

Nova eliminates this friction by integrating a **hardware-accelerated ConPTY terminal dock** powered by native Windows pseudo-console APIs.

```
+-----------------------------------------------------------------------------------+
|                             Active Browser Tab                                    |
|                       http://localhost:3000/dashboard                             |
+===================================================================================+
| [>_ PowerShell 7] [+]  |  Encoding: UTF-8  |  PID: 14208              [^] [_] [X] |
+-----------------------------------------------------------------------------------+
| PS C:\Project\NovaBrowser> git status                                              |
| On branch main                                                                    |
| Your branch is up to date with 'origin/main'.                                     |
|                                                                                   |
| PS C:\Project\NovaBrowser> npm run dev                                            |
| > ready - started server on 0.0.0.0:3000, url: http://localhost:3000              |
+-----------------------------------------------------------------------------------+
```

---

## 2. Dock Modes

The terminal dock supports three responsive display states:

| Mode | Shortcut | Behavior |
| :--- | :--- | :--- |
| **Hidden** | `Ctrl+`` | Completely closes the terminal panel, allocating 100% of window height to the web canvas. |
| **Collapsed** | Click Chevron | Collapses the terminal to a sleek 32px bottom status bar showing active shell, exit status, and last command. |
| **Expanded** | Click Expand | Expands the terminal to half-screen or full-screen height for deep debugging or log inspection. |

*You can also smoothly resize the dock height by dragging the split-handle between the browser and terminal.*

---

## 3. Key Terminal Features

1. **Native ConPTY Engine:** Full support for VT100/VT220 escape sequences, ANSI colors, cursor positioning, and interactive CLI programs (`vim`, `htop`, `lazygit`, `fzf`).
2. **Multiple Shell Profiles:**
   * PowerShell 7 (pwsh)
   * Windows PowerShell 5.1
   * Command Prompt (cmd.exe)
   * Git Bash / WSL (Ubuntu, Debian)
3. **Agent Shared Workspaces:**
   * AI agents can interact with the terminal dock via MCP tools (`nova.terminal_run_command`, `nova.terminal_read`, `nova.terminal_write`).
   * When an agent executes commands, the output streams into the dock in real time, allowing you to observe installations, test runs, and git operations live.
4. **Theme Synchronization:** The terminal dock inherits Nova's dark/light theme, typography settings, and custom font family (default: Cascadia Code / Consolas).
