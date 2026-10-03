![Nova AI Workspace — the local browser workspace for AI agents](assets/nova-banner.jpg)

# Nova AI Workspace

<div align="center">

**The Autonomous AI Browser & Cognitive Runtime for Windows**  
*Built for Human Operators and AI Coding Assistants*

[![Platform](https://img.shields.io/badge/Windows-10%20%7C%2011%20(x64)-0078D4?logo=windows&logoColor=white)](#)
[![Status: Alpha](https://img.shields.io/badge/status-alpha-orange)](#)
[![UI Framework](https://img.shields.io/badge/UI-WinUI%203%20%2B%20Windows%20App%20SDK-512BD4)](#)
[![Engine](https://img.shields.io/badge/Engine-Microsoft%20Edge%20WebView2-0078D4?logo=microsoftedge&logoColor=white)](#)
[![Protocol](https://img.shields.io/badge/Protocol-Model%20Context%20Protocol%20(MCP)%20v3-FF6B6B)](#)
[![Tools](https://img.shields.io/badge/MCP%20Tools-408%20Active%20Tools-success)](#)
[![Terminal](https://img.shields.io/badge/Terminal-ConPTY%20PowerShell%207-2D7D9A?logo=powershell&logoColor=white)](#)
[![Local-first](https://img.shields.io/badge/data-local--first-2ea44f)](#)
[![Made in Germany](https://img.shields.io/badge/Made%20in-Germany-FFCC00?labelColor=DD0000)](#)

[Quickstart](docs/getting-started/quickstart.md) • [User Guide](docs/user-guide/README.md) • [Core Features](docs/core-features/README.md) • [Tool Catalog (408 Tools)](docs/mcp-reference/tool-catalog.md) • [Developer Guide](docs/developer-guide/README.md) • [Deutsch](#nova-ai-workspace-deutsch)

</div>

---

## 🌟 What is Nova AI Workspace?

**Nova AI Workspace** is a next-generation Windows browser designed from the ground up for the era of agentic computing. It bridges the gap between human browsing and autonomous AI coding assistants, providing a single unified workspace where humans and agents collaborate seamlessly.

Traditional browser automation tools (Puppeteer, Playwright, Selenium) run in headless black boxes, separate windows, or disposable containers. They cannot leverage your daily authenticated sessions, cookies, or password managers, and they freeze when encountering captchas or 2FA prompts.

Nova changes this paradigm with the **Dual-Operator Model**:
* **Shared Context:** You and your AI agent (Anthropic Claude Code, OpenAI Codex, Google Antigravity, or custom agents) share the same browser window, authenticated sessions, and tab strip.
* **Spectator Mode & Visual Feedback:** Watch your agent navigate, click, fill forms, and solve complex workflows in real time with glowing click rings and safety halos.
* **Instant Human Takeover:** Touch the mouse or press a hotkey to take immediate manual control at any moment.

---

## 🚀 Try It — 3 Minutes, No Sign-up Needed

1. **[Download Setup from Releases](https://github.com/joelaniol/nova/releases)** — Windows 10 / 11 (x64).
2. **Activate** with the shared alpha license — no account required:
   > **License key:** `NOVA-M89A9-JW3BT-RMTD7-Z4RWL-PQGT9`  
   > **Email:** `demo@example.com`
3. **Connect your agent.** Automatically configured for Claude Code, Codex, Claude Desktop and Google Antigravity.  
   Restart your agent, then say: **"please run the Nova onboarding."**

> [!NOTE]
> On first launch Windows SmartScreen may warn that the app is not code-signed — expected for independent alpha builds. Choose **"More info" → "Run anyway"**.

> [!WARNING]
> **ALPHA SOFTWARE — USE AT YOUR OWN RISK.** Nova is in active alpha development. Bugs, crashes, data loss and breaking changes may occur. By using Nova you accept the [Disclaimer](DISCLAIMER.md), [Acceptable Use Policy](ACCEPTABLE-USE.md), [Privacy Policy](PRIVACY.md), and [License](LICENSE). · [Alpha status & known issues →](ALPHA.md)

---

## 🔬 Don't Take Our Word For It — Test It on the Lab

[`demos/lab.html`](demos/) is a benchmark page built specifically for challenging automation limits: an active session that must survive, a virtualized list with 10,000 rows (only 12 in the DOM), nested shadow roots, an iframe boundary, drag-and-drop mechanics that click-synthesizers fail on, bidirectional file uploads/downloads, native dialogs that stop JavaScript execution, and a dynamic verification code that exists strictly as raw canvas pixels.

Open it directly in Nova with no server required, and give your agent the benchmark task:
> *"Sign in, locate build 8472 in the virtual list, drag 'Deploy release' to Done, and extract the verification code from the canvas."*

[Read the interactive lab guide and solutions →](demos/README.md)

---

## 🏛️ System Architecture

```mermaid
flowchart TD
    subgraph Agents["AI Assistants & Coding Agents"]
        Claude["Anthropic Claude Code / Desktop"]
        Codex["OpenAI Codex"]
        Antigrav["Google Antigravity"]
        Custom["Custom Python / Node.js MCP Clients"]
    end

    subgraph HostProcess["Nova AI Workspace Host (NovaAIWorkspace.exe)"]
        MCPServer["MCP JSON-RPC 2.0 Server\n(Named Pipes & HTTP/SSE)"]
        AAG["Agent Awareness Gates (AAG)\n(Visual Halos & Safety Checks)"]
        WinUI["WinUI 3 Modern Chrome\n(Mica Backdrop, Tab Strip)"]
        Terminal["Embedded ConPTY Dock\n(PowerShell 7, Git CLI)"]
        WebView["Microsoft WebView2 Runtimes\n(Isolated Sandbox Partitions)"]
    end

    subgraph OutriderWorker["Outrider Subprocess (NovaBrowser.Outrider.exe)"]
        Whisper["Whisper.cpp Local Speech Ingestion"]
        AudioParser["Native Audio Duration Probes"]
        HardProbes["Hardware & Device Probes"]
    end

    Agents <-->|JSON-RPC 2.0 (Named Pipe / HTTP)| MCPServer
    MCPServer --> AAG
    AAG --> WebView
    AAG --> WinUI
    MCPServer --> Terminal
    HostProcess <-->|Supervised Pipe & Watchdog| OutriderWorker
```

---

## 🚀 Key Highlights & Capabilities

### ⚡ 408 Deep Model Context Protocol (MCP) Tools
Nova provides the most comprehensive programmatic browser surface available. Agents can inspect DOM trees, compute element layout geometries, take baseline screenshot diffs, download files, execute background crawlers, capture WebAudio streams, and manage tabs across 25 functional domains.
* Explore the complete [MCP Tool Catalog](docs/mcp-reference/tool-catalog.md).

### 🛡️ Multi-Sandbox Tab Strip (Zero Cookie Bleed)
Run multiple enterprise identities, staging environments, and personal accounts in a single browser window. Each sandbox maintains a completely isolated cookie jar, local storage, and cache directory, visually distinguished by color-coded tab accents.
* Read the [Sandboxes & Profile Isolation Guide](docs/user-guide/sandboxes-and-profiles.md).

### 💻 Integrated ConPTY Terminal Dock
A hardware-accelerated Windows pseudo-console dock embedded directly beneath the web canvas. Run PowerShell 7, start dev servers, commit git branches, or watch agent CLI output side-by-side with live web applications.
* Read the [Terminal Dock Guide](docs/user-guide/terminal-dock.md).

### 👁️ Visual Spectator Mode & Human Takeover
Never wonder what an agent is doing. Nova renders visual click rings, field focus highlights, and safety halos in real time. If an agent encounters a payment checkout or complex 2FA screen, human operators can intervene seamlessly, solve the barrier, and let the agent resume.
* Read the [Live Assist & Spectator Mode Guide](docs/user-guide/live-assist-and-spectator.md).

### 🔒 Zero-Leak Vault & Secret References (`SecretRef`)
Credentials, passwords, and sensitive API keys never leak into LLM prompts or chat logs. Nova stores encrypted credentials in the Windows DPAPI Vault and injects them only in memory at the exact moment of HTTP authentication or form filling.
* Read the [Vault & Secret Isolation Guide](docs/core-features/vault-and-secrets.md).

### 🎙️ Local Whisper Speech Transcription (Offline & Private)
Transcribe voice notes, customer service calls, or podcast streams completely offline using embedded Whisper neural models running inside the isolated Outrider worker process.
* Read the [Media Intelligence Guide](docs/core-features/media-intelligence.md).

---

## 🧠 Cognitive Architecture: Beyond Generic Memory

Traditional agent tools provide raw browser automation commands. Nova surrounds the AI model with an integrated cognitive runtime directly in the browser:

| Cognitive Function | What Nova Contributes | Architecture Guide | Video Demo |
| :--- | :--- | :--- | :---: |
| **Perception** | Reads the live browser through DOM, accessibility, screenshots, network, and console | [Visual Evidence](docs/core-features/evm-and-visual-evidence.md) | — |
| **Procedural Memory** | Remembers website interaction recipes, state, health, and visual drift | [PKS Store](docs/core-features/pks.md) | [Watch](https://www.youtube.com/watch?v=7NwRGC3l-r8) |
| **Operational Awareness** | Tracks active capabilities, connections, sandboxes, and safety rules | [Operational Knowledge](docs/core-features/operational-knowledge.md) | [Watch](https://www.youtube.com/watch?v=LgShkPaSW7I) |
| **Episodic Task Memory** | Preserves recurring tasks, work units, progress, and learned guidance | [ETM Memory](docs/core-features/etm-and-task-memory.md) | [Watch](https://www.youtube.com/watch?v=9qXrleOhPAw) |
| **User Context** | Opt-in domain notes and preferences preserved across sessions | [Browser Memory](docs/core-features/browser-memory-and-board.md) | — |
| **Executive Control** | Goal Register and safety/reflection gates keep intent and steps visible | [AAG Gates](docs/core-features/aag.md) | [Watch](https://www.youtube.com/watch?v=xhicSiFxPdY) |
| **Closed-Loop Verification** | Expected state → action → verified outcome; evidence-based claims | [Closed-Loop System](docs/core-features/closed-loop-system.md) | [Watch](https://www.youtube.com/watch?v=aKNp_74B8DE) |
| **Adaptive Learning** | Candidate promotion pipeline that validates and re-checks on site drift | [Learning Pipeline (ALP)](docs/core-features/learning-pipeline-alp.md) | [Watch](https://www.youtube.com/watch?v=6iM3TbOL9o0) |

---

## ⚡ 1-Minute Agent Quickstart

Connecting your AI coding assistant to Nova AI Workspace is instant:

### Option A: Anthropic Claude Code (CLI)
Nova automatically registers Claude Code during setup. To add manually:
```bash
claude mcp add nova -- echo '{"jsonrpc":"2.0"}'
```
*(Or connect via local Windows Named Pipe: `\\.\pipe\nova-mcp-workspace`)*

### Option B: Google Antigravity
Nova registers seamlessly in your project's `.mcp.json`:
```json
{
  "mcpServers": {
    "nova": {
      "command": "NovaBrowser.McpProxy.exe",
      "args": ["--pipe", "nova-mcp-workspace"]
    }
  }
}
```

### Option C: OpenAI Codex
Add Nova to your `~/.codex/config.toml`:
```toml
[mcp_servers.nova]
command = "NovaBrowser.McpProxy.exe"
args = ["--pipe", "nova-mcp-workspace"]
```

For detailed configuration of custom clients, see the [Agent Integration Hub](docs/integration/README.md).

---

## 📚 Complete Documentation Index

Explore the comprehensive documentation for operators, developers, and AI agents:

| Section | Focus Area | Key Documents |
| :--- | :--- | :--- |
| **[Getting Started](docs/getting-started/README.md)** | Installation & Onboarding | [Installation](docs/getting-started/installation.md) • [First Run Tour](docs/getting-started/first-run.md) • [Quickstart](docs/getting-started/quickstart.md) |
| **[User Guide](docs/user-guide/README.md)** | Human Workspace & UI Controls | [Workspace Layout](docs/user-guide/workspace-layout.md) • [Sandboxes](docs/user-guide/sandboxes-and-profiles.md) • [Terminal Dock](docs/user-guide/terminal-dock.md) • [Spectator Mode](docs/user-guide/live-assist-and-spectator.md) • [Shortcuts](docs/user-guide/keyboard-shortcuts.md) |
| **[Core Features](docs/core-features/README.md)** | Deep Architecture & Systems | [AAG Gates](docs/core-features/aag.md) • [PKS Knowledge Store](docs/core-features/pks.md) • [Outrider Boundary](docs/core-features/outrider-boundary.md) • [Vault & Secrets](docs/core-features/vault-and-secrets.md) • [Session Recording](docs/core-features/session-recording.md) |
| **[MCP Reference](docs/mcp-reference/README.md)** | 408 Tool Schemas & API | [Tool Catalog](docs/mcp-reference/tool-catalog.md) • [Protocol & Transport](docs/mcp-reference/protocol-and-transport.md) • [Dedicated Tool Guides](docs/mcp-reference/tools/) |
| **[Integration](docs/integration/README.md)** | AI Assistants & Clients | [Claude Code](docs/integration/claude-code.md) • [Codex](docs/integration/openai-codex.md) • [Antigravity](docs/integration/google-antigravity.md) • [Claude Desktop](docs/integration/claude-desktop.md) • [Custom Agents](docs/integration/custom-agents.md) |
| **[Developer Guide](docs/developer-guide/README.md)** | Building & Contributing | [Building from Source](docs/developer-guide/building-from-source.md) • [Running Tests](docs/developer-guide/running-tests.md) • [Outrider IPC](docs/developer-guide/outrider-architecture.md) |
| **[Troubleshooting](docs/troubleshooting/README.md)** | Diagnostics & Error Recovery | [Connection Issues](docs/troubleshooting/agent-connection-issues.md) • [Diagnostics Logs](docs/troubleshooting/diagnostics.md) • [Session Recovery](docs/troubleshooting/sandbox-and-session-recovery.md) |

---

## 🔒 Privacy, Security & Data Sovereignty

* **100% Local Execution:** Nova AI Workspace runs locally on your Windows machine. No browsing telemetry, cookies, or tab contents are transmitted to external servers.
* **Encrypted Storage:** Passwords, authentication cookies, and session recordings are protected on disk using Windows Data Protection API (DPAPI) and per-session ephemeral AES-GCM encryption keys.
* **Supervised Outrider Process:** Native hardware access and audio parsing are quarantined in a dedicated child process with hard timeouts and watchdog supervision.

---

<a name="nova-ai-workspace-deutsch"></a>
## 🇩🇪 Nova AI Workspace (Deutsch)

**Der lokale KI-Browser & die kognitive Laufzeitumgebung für Windows.**  
Echte Browsersitzungen · ConPTY-Terminal · Wissensspeicher · Scheduler · 408 MCP-Tools — lokal, transparent und auditierbar.

### Schnellstart in 3 Schritten
1. **[Setup herunterladen](https://github.com/joelaniol/nova/releases)** (Windows 10 / 11 x64).
2. **Aktivieren** mit dem Alpha-Testschlüssel:
   > **Schlüssel:** `NOVA-M89A9-JW3BT-RMTD7-Z4RWL-PQGT9`  
   > **E-Mail:** `demo@example.com`
3. **Agenten verbinden:** Claude Code, Codex, Claude Desktop und Antigravity werden automatisch eingerichtet. Nach Neustart des Agenten sagen: **„please run the Nova onboarding“**.

Detaillierte Anleitungen: **[Installationsanleitung auf Deutsch](docs/getting-started/installation.md#nova-ai-workspace-installieren)**.

---

## 📄 License & Community

* **Nova AI Workspace** is developed by Joel Aniol and contributors.
* **Issues & Feedback:** Report issues and feature requests on [GitHub Issues](https://github.com/joelaniol/nova/issues).
* **Website:** [nova-cognitive.com](https://nova-cognitive.com)
* **YouTube:** [@novainweb](https://www.youtube.com/@novainweb)
* **Contact:** Joel Aniol — [LinkedIn](https://www.linkedin.com/in/joelaniol/)
