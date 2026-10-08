# Nova AI Workspace — Core Features

> [!NOTE]
> This hub lists the core-feature topics of **Nova AI Workspace** (`NovaAIWorkspace.exe`): what each one covers and which MCP tools belong to it. The tools are listed in full in the [tool catalog](../mcp-reference/tool-catalog.md).

---

## Overview

Nova AI Workspace is a Windows browser built on **.NET 8, WinUI 3 and Microsoft WebView2**. AI agents control it through the Model Context Protocol (MCP); Nova provides a [tool catalog](../mcp-reference/tools/README.md). The pages below explain the parts of Nova that sit behind those tools: how it reads and acts on pages, how it checks that an action worked, what it remembers between sessions, how it keeps logins apart, and what it can do outside the browser.

---

The [alpha status page](../../ALPHA.md) lists current limitations, including plugins being unavailable and connectors not yet recommended for terminal use.

## Core features by topic

### Seeing and acting on pages

| Page | What it covers | Main MCP tools |
| :--- | :--- | :--- |
| [Input Dispatch & Shadow DOM Traversal](humanized-input-engine/README.md) | How clicks, keys and drags reach the page; open Shadow DOM | `nova.input_click`, `nova.input_drag_humanized`, `nova.click_selector`, `nova.input_text` |
| [Evidence Verification Mode (EVM)](evidence-verification-mode-evm/README.md) | Screenshots as proof of what the page shows | `nova.capture_screenshot`, `nova.screenshot_diff`, `nova.screenshot_baseline` |
| [Native Dialogs & UI Prompts](native-dialogs-and-prompts/README.md) | Dialogs outside the web page | `nova.ui_inspect_native_dialog`, `nova.ui_confirm_native_dialog`, `nova.ui_*_prompt_resolve` |
| [Auth Surface Detection (ASD)](auth-surface-detection-asd/README.md) | Recognising login pages and checking a sign-in worked | `nova.guarded_login`, `nova.ok_observe` |
| [Autonomous Crawler & Surface Explorer](crawler-and-discovery/README.md) | Exploring whole sites instead of single pages | `nova.crawl_start`, `nova.site_urls`, `nova.explore_surface` |

### Verification and safety

| Page | What it covers | Main MCP tools |
| :--- | :--- | :--- |
| [Closed-Loop System (CLS)](closed-loop-system-cls/README.md) | Expected state, action, checked outcome | `nova.goal_register`, `nova.run_sequence`, `nova.phenomenon_apply` |
| [Ambient Auto-Apply](ambient-auto-apply/README.md) | Eligible automatic playbook application during agent work | `nova.perceive`, `nova.phenomenon_apply` |
| [Agent Awareness Gates (AAG)](agent-awareness-gates-aag/README.md) | Checks that stop an agent from acting blind | `nova.guarded_*`, `nova.tab_claim`, `nova.task_instance_verify` |
| [Tool Observation Bus (TOB)](tool-observation-bus-tob/README.md) | What the agent really did, recorded on Nova's side | `nova.task_instance_verify`, `nova.task_instance_progress`, `nova.task_instance_get` |
| [Password Vault & Secret Injection](vault-and-secrets/README.md) | Saved-password delivery through references; scoped terminal secrets | `nova.vault_*`, `nova.type_selector_secret`, `nova.secret_*` |
| [Nova Outrider — Native Process Boundary](outrider-boundary/README.md) | Risky Windows and hardware probes in a separate, killable process | `nova.permission_center_get`, `nova.media_transcribe_start` |

### Agent interface

| Page | What it covers | Main MCP tools |
| :--- | :--- | :--- |
| [Agent-Native Affordances](agent-native-affordances/README.md) | Learned agent expectations, aliases and client naming compatibility | `nova.get_instructions`, `nova.tools_bundle` |

### Memory and learning

| Page | What it covers | Main MCP tools |
| :--- | :--- | :--- |
| [Phenomenological Knowledge Store (PKS)](phenomenological-knowledge-store-pks/README.md) | What Nova learns about how a site works | `nova.pks_get`, `nova.pks_match`, `nova.pks_upsert`, `nova.learn_promote` |
| [Operational Knowledge (OK)](operational-knowledge-ok/README.md) | Login state, plan and active model of a site, as signals agents report; domain notes | `nova.ok_observe`, `nova.ok_signal_schema`, `nova.domain_note` |
| [Episodic Task Memory (ETM)](episodic-task-memory-etm/README.md) | Recurring tasks and their progress | `nova.task_match`, `nova.task_instance_create`, `nova.task_instance_complete` |
| [Task URL Coverage (TUC)](task-url-coverage-tuc/README.md) | URL work units, trusted scan evidence and coverage gates | `nova.coverage_scan`, `nova.task_instance_reconcile_coverage` |
| [Agent Learning Pipeline (ALP)](agent-learning-pipeline-alp/README.md) | How a lesson is checked before it is kept | `nova.learn_suggest`, `nova.learn_generate`, `nova.learn_promote` |
| [Learning Candidate Journal (LCJ)](learning-candidate-journal-lcj/README.md) | Observations and candidate evidence used by the learning pipeline | `nova.memory_stats`, `nova.memory_add_candidate` |
| [Browser Memory](browser-memory/README.md) | Notes and preferences per site | `nova.memory_note`, `nova.memory_recall`, `nova.memory_forget` |
| [Agent Knowledge Board](agent-knowledge-board/README.md) | Opt-in investigative records of Nova tool problems | `nova.board_get`, `nova.board_contribute` |

### Sessions, network and identity

| Page | What it covers | Main MCP tools |
| :--- | :--- | :--- |
| [Multi-Sandbox Session Isolation](sandbox-isolation/README.md) | Separate profiles with their own logins | `nova.sandbox_context`, `nova.resolve_sandbox`, `nova.sandbox_create` |
| [Site Data & Privacy Management (Cookies, Storage, Cache)](site-data-management/README.md) | Cookies, storage and cache | `nova.cookie_list`, `nova.cookie_set`, `nova.storage_inspect`, `nova.cache_clear` |
| [Network](network/README.md) | Shared browser proxy, tab-scoped interception and request replay | `nova.proxy_switch`, `nova.proxy_status`, `nova.network_intercept_*` |
| [Fingerprint Protection & Browser Identity](fingerprint-and-identity/README.md) | Browser fingerprint protection | `nova.fingerprint_*`, `nova.identity_*`, `nova.emulation_*` |
| [Session Recording & Time-Travel Debugging](session-recording/README.md) | Recording a run to see later what happened | `nova.session_record_start`, `nova.session_record_query`, `nova.session_record_export` |

### Beyond the browser

| Page | What it covers | Main MCP tools |
| :--- | :--- | :--- |
| [Terminal Workspaces & ConPTY Integration](terminal-workspaces/README.md) | Terminals the agent can use | `nova.terminal_open`, `nova.terminal_run_command`, `nova.terminal_read` |
| [Scheduled Tasks & Background Automation Engine](scheduled-tasks/README.md) | Work that runs on its own | `nova.scheduled_task_create`, `nova.scheduled_task_runs`, `nova.scheduled_task_workspace_*` |
| [Connectors](connectors/README.md) | Mail, SSH, SFTP, FTP/FTPS and external MCP servers | `nova.connector_*`, `nova.mail_*`, `nova.ssh_run*`, `nova.sftp_*`, `nova.ftp_*`, `nova.external_*` |
| [Media Intelligence & Speech Transcription](media-intelligence/README.md) | Audio, video and transcription | `nova.media_transcribe_start`, `nova.media_capture_start`, `nova.media_activity_*` |
| [Agent-Authored Plugins (AAP) & Jint JavaScript Runtime](plugins/README.md) | Reference only: unavailable during the public alpha | `nova.plugin_create`, `nova.plugin_test`, `nova.plugin_inspect` |

---

## Related Documentation

* **[Getting Started](../getting-started/README.md)** — Installation, system requirements and the first start.
* **[Agent Integration](../integration/README.md)** — Connecting Claude Code, Claude Desktop, Codex, Antigravity and your own agents.
* **[MCP Reference](../mcp-reference/README.md)** — Tool catalog, capability bundles and the protocol.
* **[Troubleshooting](../troubleshooting/README.md)** — Connection problems, logs and session recovery.
