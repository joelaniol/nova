# Nova AI Workspace Documentation

## I want to use Nova

**[Install Nova](getting-started/installation.md) → [Your first five minutes](getting-started/quickstart.md)**

Connect your AI program and watch it complete a short research task. Then choose [What's next?](getting-started/whats-next.md): everyday browsing, regular agent work or how Nova works. For any problem, start at [Troubleshooting](troubleshooting/README.md).

## I want to understand Nova

**[Architecture and processes](components/README.md) → [Core features](core-features/README.md) → [MCP reference](mcp-reference/README.md)**

Explore how Nova acts, verifies and learns; identify its helper processes; or look up a tool in the [catalog](mcp-reference/tool-catalog.md).

[Gemini code-review reliability](research/gemini/nova-code-review/README.md) — 552 findings separately counterchecked by another agent, outcome charts and a timeline alongside project growth.

## Complete reference

<details>
<summary>Browse all documentation sections and pages</summary>

## Getting started

[Overview](getting-started/README.md)

| Page | What it covers |
|---|---|
| [Installation](getting-started/installation.md) | System requirements and the setup on Windows |
| [Your first five minutes](getting-started/quickstart.md) | Launch, connect, restart your AI program, complete a task and stay in control |
| [Emergency Stop](getting-started/emergency-stop.md) | Interrupt work, understand the effects and release the stop |
| [Use Learn Mode](getting-started/learn-mode.md) | Understand recurring website workflows and ask your agent to learn them |
| [What's next?](getting-started/whats-next.md) | Everyday browsing, optional onboarding, recurring workflows and architecture |
| [How the connection works](getting-started/mcp-setup.md) | Restarting, automatic reconnect and connection concepts |
| [Advanced onboarding](getting-started/advanced-onboarding.md) | Optional project references and explicit bootstrap |

## User guide

[Overview](user-guide/README.md)

| Section | What it covers |
|---|---|
| [Browser](user-guide/browser/README.md) | Tabs, favorites, history, downloads, private browsing and shortcuts |
| [Identity & security](user-guide/identity-and-security/README.md) | Passwords, permissions, certificates, sandboxes and proxies |
| [Agents](user-guide/agents/README.md) | Connection, watching work, taking over, Domain Notes and onboarding |
| [Tools](user-guide/tools/README.md) | Terminal, transcription, scheduled tasks and recordings |
| [Settings](user-guide/settings/README.md) | General, appearance, site permissions and AI & agents |

## Agent integration

[Overview](integration/README.md)

| Page | What it covers |
|---|---|
| [Claude Code](integration/claude-code.md) | Connecting the Claude Code CLI |
| [Claude Desktop](integration/claude-desktop.md) | Connecting the Claude Desktop app |
| [OpenAI Codex](integration/openai-codex.md) | Connecting the Codex CLI |
| [Antigravity](integration/google-antigravity.md) | Connect and restart Antigravity |
| [Custom integrations — developers](integration/custom-agents.md) | Build your own MCP client against the actual contracts |

## MCP reference

[Overview](mcp-reference/README.md)

| Page | What it covers |
|---|---|
| [Tool catalog](mcp-reference/tool-catalog.md) | Every tool by area, each linked to its own page |
| [Protocol and transport](mcp-reference/protocol-and-transport.md) | Wire format, transports and error contract |

[One page per tool](mcp-reference/tools/README.md), grouped by area:

| Area | Tools |
|---|---|
| [App shell and UI](mcp-reference/tools/app-shell-and-ui/) | Window, settings, dialogs, favorites, discovery |
| [Browser automation](mcp-reference/tools/browser-automation/) | Tabs, navigation, clicking, typing, scrolling |
| [DOM and reading](mcp-reference/tools/dom-and-reading/) | Page text, DOM, tables, PDFs |
| [Visual evidence](mcp-reference/tools/visual-evidence/) | Screenshots and visual comparison |
| [Layout and QA](mcp-reference/tools/layout-and-qa/) | Overflow, layout metrics, accessibility checks |
| [Device emulation](mcp-reference/tools/device-emulation/) | Viewport, device, locale, media emulation |
| [Guarded actions](mcp-reference/tools/guarded-actions/) | Sign-in, sending and submitting with a safety check |
| [Downloads](mcp-reference/tools/downloads/) | Listing, waiting for and handling downloads |
| [Site data and identity](mcp-reference/tools/site-data-and-identity/) | Cookies, storage, fingerprint, identity |
| [Proxy and network](mcp-reference/tools/proxy-and-network/) | Proxies, network log, request interception |
| [Vault and security](mcp-reference/tools/vault-and-security/) | Stored logins and secrets |
| [Crawler and discovery](mcp-reference/tools/crawler-and-discovery/) | Crawling sites and mapping their pages |
| [PKS and learning](mcp-reference/tools/pks-and-learning/) | Learned site knowledge and its review |
| [Task memory](mcp-reference/tools/task-memory/) | Task profiles, progress and memory notes |
| [Scheduled tasks](mcp-reference/tools/scheduled-tasks/) | Jobs that run on a schedule |
| [Session recording](mcp-reference/tools/session-recording/) | Recording and replaying a session |
| [Media and transcription](mcp-reference/tools/media-and-transcription/) | Camera, microphone, capture, speech to text |
| [Notifications](mcp-reference/tools/notifications/) | Site notifications and their permissions |
| [Connectors and mail](mcp-reference/tools/connectors-and-mail/) | Mail, SSH, SFTP and FTP/FTPS |
| [Terminal](mcp-reference/tools/terminal-ops/) | Opening and driving terminals |
| [External MCP servers](mcp-reference/tools/external-mcp/) | Other MCP servers run through Nova |
| [Plugins](mcp-reference/tools/plugins/) | Plugins an agent writes, tests and installs for a site |

## Components and processes

[Overview](components/README.md) — What each process does, when it runs and why it is separate.

| Component | Learn more |
|---|---|
| Main app | [Nova AI Workspace](components/nova-ai-workspace.md) |
| Native work | [Outrider](components/outrider.md) |
| Agent connection | [MCP Proxy](components/mcp-proxy.md) |
| Console host | [TerminalRunner](components/terminal-runner.md) |
| Recording diagnostics | [ReplayValidator](components/replay-validator.md) |
| Microsoft browser runtime and task programs | [WebView2 and child processes](components/webview2-and-child-processes.md) |

## Core features

[Overview](core-features/README.md)

[Agent-Native Affordances](core-features/agent-native-affordances/README.md) — Built with agents: familiar naming patterns, scoped aliases and client compatibility.

**Seeing and acting on pages**

| Page | What it covers |
|---|---|
| [Input Dispatch & Shadow DOM Traversal](core-features/humanized-input-engine/README.md) | How clicks, keys and drags reach the page; open Shadow DOM |
| [Native Dialogs & UI Prompts](core-features/native-dialogs-and-prompts/README.md) | Dialogs outside the web page |
| [Auth Surface Detection (ASD)](core-features/auth-surface-detection-asd/README.md) | Recognising login pages and checking a sign-in worked |
| [Autonomous Crawler & Surface Explorer](core-features/crawler-and-discovery/README.md) | Exploring whole sites instead of single pages |

**Research**

| Page | What it covers |
|---|---|
| [Research](core-features/research/README.md) | Evidence Verification Mode (EVM), factual claims, sources and visual evidence |

**Verification and safety**

| Page | What it covers |
|---|---|
| [Closed-Loop System (CLS)](core-features/closed-loop-system-cls/README.md) | Expected state, action, checked outcome |
| [Ambient Auto-Apply](core-features/learning/ambient-auto-apply/README.md) | Eligible automatic playbook application during agent work |
| [Agent Awareness Gates (AAG)](core-features/agent-awareness-gates-aag/README.md) | Checks that stop an agent from acting blind |
| [Tool Observation Bus (TOB)](core-features/tool-observation-bus-tob/README.md) | What the agent really did, recorded on Nova's side |
| [Password Vault & Secret Injection](core-features/vault-and-secrets/README.md) | Passwords filled in without the agent seeing them |
| [Nova Outrider — Native Process Boundary](core-features/outrider-boundary/README.md) | Risky Windows and hardware probes in a separate, killable process |

**[Learning overview](core-features/learning/README.md)**

| Page | What it covers |
|---|---|
| [Phenomenological Knowledge Store (PKS)](core-features/learning/phenomenological-knowledge-store-pks/README.md) | What Nova learns about how a site works |
| [Operational Knowledge (OK)](core-features/learning/operational-knowledge-ok/README.md) | Login state, plan and active model of a site, as signals agents report |
| [Domain Notes](core-features/learning/domain-notes/README.md) | Persistent website instructions, scope, warnings and required acknowledgement |
| [Operator Notes](core-features/learning/operator-notes/README.md) | Searchable working guidance, preferences and environment context with sandbox scope |
| [Episodic Task Memory (ETM)](core-features/learning/episodic-task-memory-etm/README.md) | Recurring tasks and their progress |
| [Task URL Coverage (TUC)](core-features/learning/task-url-coverage-tuc/README.md) | URL work units, scan evidence and coverage gates |
| [Agent Learning Pipeline (ALP)](core-features/learning/agent-learning-pipeline-alp/README.md) | How a lesson is checked before it is kept |
| [Learning Candidate Journal (LCJ)](core-features/learning/learning-candidate-journal-lcj/README.md) | Observations and candidate evidence used by the pipeline |
| [Browser Memory](core-features/learning/browser-memory/README.md) | Notes and preferences per site |
| [Agent Knowledge Board](core-features/learning/agent-knowledge-board/README.md) | Experimental; currently not enabled for regular use. Investigative records of Nova tool problems |

**Sessions, network and identity**

| Page | What it covers |
|---|---|
| [Multi-Sandbox Session Isolation](core-features/sandbox-isolation/README.md) | Separate profiles with their own logins |
| [Site Data & Privacy Management (Cookies, Storage, Cache)](core-features/site-data-management/README.md) | Cookies, storage and cache |
| [Network](core-features/network/README.md) | Proxy routing, interception, request replay and SSL/TLS diagnostics |
| [Fingerprint Protection & Browser Identity](core-features/fingerprint-and-identity/README.md) | Browser fingerprint protection |
| [Session Recording & Time-Travel Debugging](core-features/session-recording/README.md) | Recording a run to see later what happened |

**Beyond the browser**

| Page | What it covers |
|---|---|
| [Terminal Workspaces & ConPTY Integration](core-features/terminal-workspaces/README.md) | Terminals the agent can use |
| [Scheduled Tasks & Background Automation Engine](core-features/scheduled-tasks/README.md) | Work that runs on its own |
| [Connectors](core-features/connectors/README.md) | Mail, SSH, SFTP, FTP/FTPS and external MCP servers |
| [Media Intelligence](core-features/media-intelligence/README.md) | Speech transcription, image viewing, PDFs, playback, capture and media devices |
| [Agent-Authored Plugins (AAP) & Jint JavaScript Runtime](core-features/plugins/README.md) | Small scripts an agent writes for a site |

## Troubleshooting

[One troubleshooting hub](troubleshooting/README.md) covers installation, connection, agent behavior, browser sessions, diagnostics and client-specific quirks.

| Page | What it covers |
|---|---|
| [Connection issues](troubleshooting/agent-connection-issues.md) | Missing connections, local server and bridge checks |
| [Agent behavior](troubleshooting/agent-behavior.md) | Connected but not using tools, missing data or unchecked outcomes |
| [Antigravity compatibility](troubleshooting/antigravity.md) | Nova's client-compatible names and result handling |
| [Diagnostics](troubleshooting/diagnostics.md) | Logs and failure evidence |
| [Sandbox and session recovery](troubleshooting/sandbox-and-session-recovery.md) | Abandoned tabs, held claims and missing sandboxes |

## Research

[Overview](research/README.md)

| Page | What it covers |
|---|---|
| [BREACH](research/breach/README.md) | A method for structurally new concepts by breaking load-bearing assumptions |
| [The BREACH prompt](research/breach/prompt.md) | The meta-prompt that runs the method with a language model |

## Changelog & releases

[Overview](changelog/README.md)

| Version | Release date | Highlights |
|---|---|---|
| [1.0.0-alpha.18](changelog/v1.0.0-alpha.18.md) | 2026-10-07 | New product name & look, favorites panel, SQLite history, native permission dialogs, AI setup, expanded sandboxes, password vault, resumable transfers, local transcription |
| [1.0.0-alpha.17](changelog/v1.0.0-alpha.17.md) | 2026-09-10 | Targeted hotfix for blank context menu spellcheck rows, official slogan adoption ("Built for what's next."), UI blank label scanner |
| [1.0.0-alpha.16](changelog/v1.0.0-alpha.16.md) | 2026-09-10 | Background agent mode with notification area icon, taskbar integration & autostart fix, console read for agent devtools |
| [1.0.0-alpha.15](changelog/v1.0.0-alpha.15.md) | 2026-09-08 | Network request inspection & interception rules for agents, agent tab pinning & reordering, terminal settings & NO_COLOR chip, media file info, update & install repair |
| [1.0.0-alpha.14](changelog/v1.0.0-alpha.14.md) | 2026-09-04 | Local speech-to-text transcription engine (Whisper), browser-built and streaming media capture, PDF reading/saving, private tabs, loops in agent sequences |

## More

- [Interactive demo](../demos/README.md) — an experience loop with repeat visits, a changed page and checked outcomes, plus eight browser exercises ([German guide](../demos/README.de.md))
- [Alpha notes](../ALPHA.md) · [Privacy](../PRIVACY.md) · [Acceptable use](../ACCEPTABLE-USE.md) · [Disclaimer](../DISCLAIMER.md) · [License](../LICENSE)

</details>

## Dokumentation auf Deutsch

Der [Demo-Guide](../demos/README.de.md), die [Installation](getting-started/installation.md#nova-ai-workspace-installieren), die [Hilfe zum Agentenverhalten](troubleshooting/agent-behavior.md#deutsch-der-agent-ist-verbunden-arbeitet-aber-nicht-richtig) und die [Antigravity-Hinweise](troubleshooting/antigravity.md#google-antigravity-deutsch) sind auch auf Deutsch verfügbar. Die übrige Dokumentation ist überwiegend englisch.

Zum Einstieg: [Installieren](getting-started/installation.md#nova-ai-workspace-installieren) → [KI-Programm verbinden](integration/README.md) → [Erste Aufgabe](getting-started/quickstart.md).
