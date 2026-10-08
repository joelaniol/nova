![Nova AI Workspace — the local browser workspace for AI agents](assets/nova-banner.jpg)

# Nova AI Workspace

<div align="center">

### **Built for what's next.**

**The Autonomous AI Browser & Cognitive Runtime for Windows**  
*Built for Human Operators and AI Coding Assistants*

[![Platform](https://img.shields.io/badge/Windows-10%20%7C%2011%20(x64)-0078D4?logo=windows&logoColor=white)](docs/getting-started/installation.md#1-system-requirements)
[![Status: Alpha](https://img.shields.io/badge/status-alpha-orange)](ALPHA.md)
[![Tools](https://img.shields.io/badge/MCP-Tool%20Catalog-success)](docs/mcp-reference/tool-catalog.md)
[![Terminal](https://img.shields.io/badge/Terminal-ConPTY%20PowerShell-2D7D9A?logo=powershell&logoColor=white)](docs/user-guide/tools/terminal.md)
[![Local-first](https://img.shields.io/badge/data-local--first-2ea44f)](PRIVACY.md)

**[Download & install](docs/getting-started/installation.md#2-download-and-install) · [Connect your AI program](docs/getting-started/quickstart.md) · [Deutsch](#nova-ai-workspace-deutsch) · [Get help](docs/troubleshooting/README.md)**

[User Guide](docs/user-guide/README.md) · [Core Features](docs/core-features/README.md) · [Tool Catalog](docs/mcp-reference/tool-catalog.md) · [Changelog](docs/changelog/README.md)

</div>

---

## 🌟 What is Nova AI Workspace?

**Nova AI Workspace** is a Windows browser workspace where you and your connected AI program work in the same logged-in tabs. Ask your agent to browse, inspect a page, compare information or complete a task, and watch its browser actions in Nova.

Nova brings browser interaction, persistent procedural knowledge, outcome verification and human handoffs into the workspace you use every day. The [Experience loop demo](demos/README.md) makes that combination tangible, including what happens when a previously useful recipe no longer fits the page.

The **Dual-Operator Model** connects the person and the agent:
* **Shared Context:** You and your AI agent (Anthropic Claude Code, OpenAI Codex, Google Antigravity, or custom agents) share the same browser window, authenticated sessions, and tab strip.
* **AI Visualization:** Watch your agent navigate, click and fill forms in real time. An optional on-screen cursor labelled "AI" shows where the agent acts, with an optional card for the current and next step.
* **You Stay in Control:** A tab an agent is working in says so; click it and confirm **Take over** to end the agent's control of that tab. **Emergency stop** in the main menu interrupts all agents at once. Typing or moving the mouse does not pause the agent by itself.

---

## 🚀 Get Started — No Nova Account Needed

You need **Windows 10 / 11 (x64)** and an installed AI program such as Claude Code, Claude Desktop, Codex or Antigravity. Your conversation stays in that program; Nova provides the browser workspace. Your AI program may require its own account or subscription.

1. **[Download Setup from Releases](https://github.com/joelaniol/nova/releases)** — under **Assets**, choose the Windows x64 file ending in `-Setup-<version>.exe`. The other assets are an MCP bridge bundle (`.mcpb`) and a checksum (`.sha256`); neither installs Nova.
2. **Activate.** No account required — the setup comes with the shared alpha license already filled in.
3. **[Connect your AI program](docs/getting-started/quickstart.md).** Nova detects supported AI programs. Follow **Easy setup**, click **Connect** if offered, and restart your AI program. Then ask: **"Use Nova to research the current Microsoft Edge WebView2 release notes on Microsoft's official website. Open the relevant pages, summarize three recent changes, and give me source links and release dates."**

Installation details: [requirements and setup](docs/getting-started/installation.md). Looking for the trial key? → **[Alpha Trial License](docs/getting-started/trial-license.md)**

> [!NOTE]
> Windows SmartScreen may show **"Windows protected your PC"**. See the [installation notes](docs/getting-started/installation.md) before continuing with **"More info" → "Run anyway"**.

> [!WARNING]
> **ALPHA SOFTWARE — USE AT YOUR OWN RISK.** Nova is in active alpha development. Bugs, crashes, data loss and breaking changes may occur. By using Nova you accept the [Disclaimer](DISCLAIMER.md), [Acceptable Use Policy](ACCEPTABLE-USE.md), [Privacy Policy](PRIVACY.md), and [License](LICENSE). · [Alpha status & known issues →](ALPHA.md)

---

## 🔬 Try Nova with an Interactive Demo

The [interactive demo](demos/README.md) starts with an **Experience loop**: encounter a recurring notice, retrieve the experience on a return visit, handle a changed page, and verify an actual saved result. Eight smaller browser exercises are also included.

Download the repository and follow the guide to open the demo on a local HTTP address. Ask your connected agent:

> Clear the release notice and save the sample draft. Check the actual saved result, ask me to confirm when needed, and record the verified notice-handling experience in Nova. Show me what was stored and its current learning level.

The first save request deliberately leaves the draft unsaved. Later, **Site changed** invalidates the original dismissal selector. Look for real knowledge and verification evidence from Nova alongside the page's counters. All records are simulated; this is a workflow demonstration, not a performance benchmark.

[Open the demo guide →](demos/README.md) · [Deutsche Anleitung](demos/README.de.md)

---

## 🚀 Key Highlights & Capabilities

### ⚡ Deep Model Context Protocol (MCP) Tools
Agents can inspect DOM trees, measure element layout, compare screenshots against baselines, download files, run background crawlers, record and transcribe page audio, and manage tabs. The tools are grouped into 25 capability bundles that an agent loads as needed.
* Explore the complete [MCP Tool Catalog](docs/mcp-reference/tool-catalog.md).

### 🛡️ Multi-Sandbox Tab Strip (Zero Cookie Bleed)
Run multiple enterprise identities, staging environments, and personal accounts in a single browser window. Each sandbox maintains a completely isolated cookie jar, local storage, and cache directory, visually distinguished by color-coded tab accents.
* Read the [Sandboxes & Profile Isolation Guide](docs/user-guide/identity-and-security/sandboxes-and-profiles.md).

### 💻 Integrated ConPTY Terminal Dock
A Windows pseudo-console (ConPTY) dock inside the Nova window. It starts PowerShell 7 when it is installed and Windows PowerShell otherwise. Run commands, start dev servers or use git next to the page you are working on.
* Read the [Terminal Dock Guide](docs/user-guide/tools/terminal.md).

### 👁️ AI Visualization & Staying in Control
See what an agent is doing: the optional "AI" cursor marks where it acts, and a tab under agent control is marked as such. If an agent reaches a payment checkout or a 2FA screen, you can take over the tab, solve it yourself and hand the work back. **Emergency stop** in the main menu interrupts all agents.
* Read the [AI Visualization & Staying in Control guide](docs/user-guide/agents/watching-agent-work.md).

### 🔒 Password Vault & Secret References (`SecretRef`)
Agents can sign in with stored passwords without the plaintext passing through the AI model. Nova keeps vault entries encrypted with Windows DPAPI for your user account and fills them into the login form or HTTP sign-in itself. API keys go into a secret store whose management tools do not return their values. Authorized terminal programs receive them as environment variables and can read or output them; the destination website also receives a filled password.
* Read the [Password Vault & Secret Injection](docs/core-features/vault-and-secrets/README.md).

### 🎙️ Local Whisper Speech Transcription (Offline & Private)
Transcribe audio and video locally with Whisper speech models. Recognition runs in the separate Outrider helper process; the models are downloaded once and then work offline.
* Read the [Speech Transcription guide](docs/core-features/media-intelligence/transcription/README.md).

---

## 🧠 Cognitive Architecture: Beyond Generic Memory

Traditional agent tools provide raw browser automation commands. Nova surrounds the AI model with an integrated cognitive runtime directly in the browser:

| Cognitive Function | What Nova Contributes | Architecture Guide | Video Demo |
| :--- | :--- | :--- | :---: |
| **Agent-Native Interface** | Built with agents: familiar action names and scoped aliases connect learned expectations to Nova's canonical tools | [Agent-Native Affordances](docs/core-features/agent-native-affordances/README.md) | — |
| **Evidence-Based Research** | Supplies claim tests, source requirements and tools to capture and compare visible evidence | [Evidence Verification Mode (EVM) & Visual Evidence](docs/core-features/research/evidence-verification-mode-evm/README.md) | — |
| **Procedural Memory** | Remembers website interaction recipes, state, health, and visual drift | [Phenomenological Knowledge Store (PKS)](docs/core-features/learning/phenomenological-knowledge-store-pks/README.md) | [Watch](https://www.youtube.com/watch?v=7NwRGC3l-r8) |
| **Operational Awareness** | Login state, plan and active model of a site, preserved as reported observations | [Operational Knowledge (OK) & Real-Time Environment State](docs/core-features/learning/operational-knowledge-ok/README.md) | [Watch](https://www.youtube.com/watch?v=LgShkPaSW7I) |
| **Episodic Task Memory** | Preserves recurring tasks, work units, progress, and learned guidance | [Episodic Task Memory (ETM)](docs/core-features/learning/episodic-task-memory-etm/README.md) | [Watch](https://www.youtube.com/watch?v=9qXrleOhPAw) |
| **User Context** | Opt-in domain notes and preferences preserved across sessions | [Browser Memory](docs/core-features/learning/browser-memory/README.md) | — |
| **Executive Control** | Goal Register and safety/reflection gates keep intent and steps visible | [Agent Awareness Gates (AAG)](docs/core-features/agent-awareness-gates-aag/README.md) | [Watch](https://www.youtube.com/watch?v=xhicSiFxPdY) |
| **Closed-Loop Verification** | Expected state → action → verified outcome; evidence-based claims | [Closed-Loop System (CLS)](docs/core-features/closed-loop-system-cls/README.md) | [Watch](https://www.youtube.com/watch?v=aKNp_74B8DE) |
| **Adaptive Learning** | Candidate promotion pipeline that validates and re-checks on site drift | [Agent Learning Pipeline (ALP)](docs/core-features/learning/agent-learning-pipeline-alp/README.md) | [Watch](https://www.youtube.com/watch?v=6iM3TbOL9o0) |

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
        MCPServer["MCP JSON-RPC 2.0 Server<br>(Streamable HTTP, 127.0.0.1)"]
        AAG["Agent Awareness Gates (AAG)<br>(Safety Checks)"]
        WinUI["WinUI 3 Window<br>(Tab Strip, Panels)"]
        Terminal["Embedded ConPTY Dock<br>(PowerShell)"]
        WebView["Microsoft WebView2 Runtimes<br>(Isolated Sandbox Partitions)"]
    end

    subgraph OutriderWorker["Outrider Subprocess (NovaBrowser.Outrider.exe)"]
        Whisper["Whisper.cpp Local Speech Ingestion"]
        AudioParser["Native Audio Duration Probes"]
        HardProbes["Hardware & Device Probes"]
    end

    Agents <-->|"JSON-RPC 2.0 (stdio bridge or HTTP)"| MCPServer
    MCPServer --> AAG
    AAG --> WebView
    AAG --> WinUI
    MCPServer --> Terminal
    HostProcess <-->|Supervised Pipe & Watchdog| OutriderWorker
```

---

## 📚 Complete Documentation Index

Explore the comprehensive documentation for operators, developers, and AI agents:

| Section | Focus Area | Key Documents |
| :--- | :--- | :--- |
| **[Getting Started](docs/getting-started/README.md)** | Installation & First Task | [Installation](docs/getting-started/installation.md) • [Your First Five Minutes](docs/getting-started/quickstart.md) • [What's Next?](docs/getting-started/whats-next.md) |
| **[User Guide](docs/user-guide/README.md)** | Everyday browsing & workspace controls | [Browser](docs/user-guide/browser/README.md) • [Identity & Security](docs/user-guide/identity-and-security/README.md) • [Agents](docs/user-guide/agents/README.md) • [Tools](docs/user-guide/tools/README.md) • [Settings](docs/user-guide/settings/README.md) |
| **[Core Features](docs/core-features/README.md)** | Deep Architecture & Systems | [Agent Awareness Gates (AAG)](docs/core-features/agent-awareness-gates-aag/README.md) • [Phenomenological Knowledge Store (PKS)](docs/core-features/learning/phenomenological-knowledge-store-pks/README.md) • [Nova Outrider](docs/core-features/outrider-boundary/README.md) • [Password Vault & Secret Injection](docs/core-features/vault-and-secrets/README.md) • [Session Recording & Time-Travel Debugging](docs/core-features/session-recording/README.md) |
| **[Components & Processes](docs/components/README.md)** | Identify Nova-related processes | [Main app](docs/components/nova-ai-workspace.md) • [Outrider](docs/components/outrider.md) • [MCP Proxy](docs/components/mcp-proxy.md) • [TerminalRunner](docs/components/terminal-runner.md) • [ReplayValidator](docs/components/replay-validator.md) • [WebView2](docs/components/webview2-and-child-processes.md) |
| **[MCP Reference](docs/mcp-reference/README.md)** | Tools & Protocol | [Tool Catalog](docs/mcp-reference/tool-catalog.md) • [Protocol & Transport](docs/mcp-reference/protocol-and-transport.md) • [Dedicated Tool Guides](docs/mcp-reference/tools/README.md) |
| **[Integration](docs/integration/README.md)** | AI Assistants & Clients | [Claude Code](docs/integration/claude-code.md) • [Codex](docs/integration/openai-codex.md) • [Antigravity](docs/integration/google-antigravity.md) • [Claude Desktop](docs/integration/claude-desktop.md) • [Custom Agents](docs/integration/custom-agents.md) |
| **[Troubleshooting](docs/troubleshooting/README.md)** | Help by Symptom | [Connection Issues](docs/troubleshooting/agent-connection-issues.md) • [Agent Behavior](docs/troubleshooting/agent-behavior.md) • [Diagnostics Logs](docs/troubleshooting/diagnostics.md) • [Session Recovery](docs/troubleshooting/sandbox-and-session-recovery.md) |

---

## 🔒 Privacy, Security & Data Sovereignty

* **Local Execution:** Nova AI Workspace runs on your Windows machine and keeps its data in your profile folder. It collects no usage analytics and does not send your browsing, cookies or tab contents to its own server; it contacts `nova-cognitive.com` only for license activation, renewal and opt-in crash reports. What your AI program reads through Nova goes to that program's provider. Details: [Privacy Policy](PRIVACY.md).
* **Encrypted Storage:** Vault passwords, stored secrets and the MCP access token are encrypted with the Windows Data Protection API (DPAPI) for your user account; session recordings are encrypted with AES-GCM under a DPAPI-protected key.
* **Supervised Outrider Process:** Native hardware access and audio parsing are quarantined in a dedicated child process with hard timeouts and watchdog supervision.

---

<a name="nova-ai-workspace-deutsch"></a>
## 🇩🇪 Nova AI Workspace (Deutsch)

**Der lokale KI-Browser & die kognitive Laufzeitumgebung für Windows.**  
Echte Browsersitzungen · ConPTY-Terminal · Wissensspeicher · Scheduler · [MCP-Werkzeugkatalog](docs/mcp-reference/tool-catalog.md) — lokal, transparent und auditierbar.

### Schnellstart in 3 Schritten
Du brauchst **Windows 10 / 11 (x64)** und ein installiertes KI-Programm wie Claude Code, Claude Desktop, Codex oder Antigravity. Dein Gespräch bleibt dort; Nova stellt den Browser-Arbeitsplatz bereit. Das KI-Programm kann ein eigenes Konto oder Abo benötigen.

1. **[Setup herunterladen](https://github.com/joelaniol/nova/releases)**: Unter **Assets** die Datei mit der Endung `-Setup-<version>.exe` wählen. Die anderen Dateien sind ein MCP-Verbindungspaket (`.mcpb`) und eine Prüfsumme (`.sha256`); beide installieren Nova nicht.
2. **Aktivieren:** Kein Konto nötig, das Setup bringt den Alpha-Testzugang schon ausgefüllt mit.
3. **[KI-Programm verbinden](docs/getting-started/quickstart.md):** Nova erkennt unterstützte KI-Programme. Folge der einfachen Einrichtung, klicke bei Bedarf **Verbinden** und starte dein KI-Programm neu. Sage dann: **„Recherchiere mit Nova die aktuellen Microsoft-Edge-WebView2-Versionshinweise auf Microsofts offizieller Website. Öffne die relevanten Seiten, fasse drei aktuelle Änderungen zusammen und gib mir Quellenlinks und Veröffentlichungsdaten.“**

Testschlüssel gesucht? → **[Alpha-Testlizenz](docs/getting-started/trial-license.md#alpha-testlizenz)**

Weiter: **[Installation auf Deutsch](docs/getting-started/installation.md#nova-ai-workspace-installieren)** · [Erste Aufgabe (Englisch)](docs/getting-started/quickstart.md) · [Hilfe (Englisch)](docs/troubleshooting/README.md) · [Demo auf Deutsch](demos/README.de.md).

---

## 📄 License & Community

* **Nova AI Workspace** is developed by Joel Aniol and contributors.
* **License:** [License terms](LICENSE).
* **Security vulnerabilities:** Follow the [private reporting route](SECURITY.md).
* **Issues & Feedback:** Report issues and feature requests on [GitHub Issues](https://github.com/joelaniol/nova/issues).
  Agents can use [Nova's bug-report guide](docs/mcp-reference/tools/app-shell-and-ui/nova-get-instructions.md#reporting-bugs-and-work-session-feedback) via `nova.get_instructions(topic='bug_report')` for reporting rules and bug-ticket or work-session feedback templates. Review URLs and evidence for secrets and personal data; see the [alpha reporting policy](ALPHA.md#what-to-report).
* **Website:** [nova-cognitive.com](https://nova-cognitive.com)
* **YouTube:** [Nova Cognitive (@novacognitive)](https://www.youtube.com/@novacognitive)
* **Contact:** Joel Aniol — [LinkedIn](https://www.linkedin.com/in/joelaniol/)
