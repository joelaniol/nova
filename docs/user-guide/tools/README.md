# Workspace Tools

Nova AI Workspace integrates development, automation, and forensic tools directly into the browser shell, providing both human operators and AI agents with unified local capabilities beyond standard tab browsing.

---

## Available Tools

| Tool | Focus Area | Key Features |
| :--- | :--- | :--- |
| **[Integrated Terminal Dock](terminal.md)** | ConPTY Shell & PowerShell | Embedded slide-up terminal dock (`Ctrl+~`), multi-session management, AI agent terminal access, workspace isolation. |
| **[Audio & Video Transcription](transcription.md)** | Offline Whisper Speech-to-Text | 100% local transcription via `whisper.cpp`, multi-language support, model downloads, text and `.srt`/`.vtt` subtitle export. |
| **[Scheduled Tasks & Automation](scheduled-tasks.md)** | Background Jobs & Cron Scheduling | Recurring background jobs, Claude Code & Codex CLI execution, PowerShell scripts, DPAPI encrypted secrets, run history. |
| **[Session Recordings](recordings.md)** | Forensics & Time-Travel Debugging | Tamper-resistant, encrypted event streams (network, console, interactions, DOM snapshots) for post-mortem debugging. |

---

## Related Documentation

* **[User Guide Overview](../README.md)** — Daily browsing, sandboxes, settings, and agent collaboration.
* **[Core Features Hub](../../core-features/README.md)** — Architectural documentation for all Nova subsystems.
* **[MCP Reference](../../mcp-reference/README.md)** — Model Context Protocol tool catalog and schema definitions.
