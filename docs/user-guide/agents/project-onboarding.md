# Project Onboarding: Equipping Agents with Nova Knowledge

> [!NOTE]
> Project onboarding writes concise Nova reference guidelines into your software repository (such as `AGENTS.md`), ensuring that coding agents understand Nova's browser tools, conventions, and safety rules without guesswork.

---

## 1. Overview & Why Onboarding Matters

When you open a software repository in Claude Code, Codex, or Antigravity, the AI agent reads your project's repository rules to determine how to run tests, write code, and navigate the environment.

However, unless informed about Nova, an agent asked to perform browser tasks may attempt to install Playwright, download headless Chromium, or spawn external terminal daemons—wasting memory, duplicating browser instances, and bypassing your authenticated desktop sessions.

**Project Onboarding** solves this by generating standardized reference notes inside your repository. These instructions inform the agent that Nova AI Workspace is already running and provide the exact conventions for interacting with your tabs.

```mermaid
flowchart TD
    Repo["Software Repository"] --> Check{"Does Repository have Nova Instructions?"}
    Check -->|No| Confusion["Agent tries to launch headless Chromium<br>or raw Selenium scripts"]
    Check -->|Yes (Onboarded)| Native["Agent calls Nova's MCP tools directly<br>(nova.navigate, nova.click_selector)"]

    Native --> UserSession["Uses existing desktop tabs & logins"]
    Native --> Visible["Renders visible AI assist cursor"]
    Native --> Safe["Enforces User Domain Notes & AAG"]
```

---

## 2. How to Trigger Project Onboarding

Project onboarding is entirely optional and can be initialized in three convenient ways:

### Option A: Via Nova Settings
1. Open **Menu → Settings**.
2. Navigate to **AI & agents → Connection & setup**.
3. Under the **Project onboarding** section, click **Generate onboarding notes**.
4. Choose your project directory to write the guidelines.

### Option B: Asking Your AI Agent in Chat
In your coding client's conversation, simply instruct the agent:
> *"Please onboard this repository to use Nova AI Workspace. Call `nova.get_onboarding` and write the reference guidelines into AGENTS.md."*

The agent retrieves the authoritative onboarding specification directly from Nova and creates or updates your repository's instruction file.

### Option C: Calling the Onboarding Tool Directly
Agents can call the specialized MCP tool [`nova.install_onboarding`](../../mcp-reference/tools/app-shell-and-ui/nova-install-onboarding.md) to automatically inject the guidelines into your workspace.

---

## 3. What Guidelines Are Added to Your Repository?

Nova's onboarding notes are designed to be lightweight, vendor-neutral, and strictly focused on browser interaction etiquette:

1. **Workspace Awareness:** Informs the agent that Nova AI Workspace is the primary browser interface and process.
2. **Tab Reuse:** Instructs the agent to inspect and use existing browser tabs rather than opening dozens of unnecessary windows.
3. **Sandbox Scoping:** Explains how to target the appropriate sandbox profile (e.g. keeping work and personal web tasks separate).
4. **Safety & Domain Notes:** Mandates that the agent inspect and technically acknowledge [Domain Notes](domain-notes.md) before performing mutating actions on web portals.
5. **No Password Guessing:** Instructs the agent never to guess credentials and to request saved passwords securely via the [Nova Vault](../identity-and-security/passwords-and-vault.md).

```markdown
<!-- Example snippet from generated onboarding notes -->
# Browser Automation Contract
- Primary Browser: Nova AI Workspace (WinUI 3 + WebView2)
- Interface: Model Context Protocol (MCP) via `nova.*` tools
- Invariant: Do not launch external headless browsers (Playwright/Puppeteer)
- Invariant: Check for existing tabs before creating new ones
- Invariant: Respect user Domain Notes on target web portals
```

---

## 4. What Project Onboarding Does NOT Do

To maintain system integrity and user security, project onboarding enforces strict boundaries:

* **No Client Allowlist Modification:** Onboarding does not alter or weaken your AI client's permission settings. Tool approval dialogs inside Claude Code or Codex are governed strictly by those clients.
* **No Credential Access:** It does not read, write, or export website cookies, passwords, or vault secrets.
* **Separate from Domain Notes:** Onboarding configures code repositories; [Domain Notes](domain-notes.md) provide per-website instructions stored inside Nova.
* **Separate from Learn Mode:** Onboarding provides high-level browser guidelines; [Learn Mode](../../getting-started/learn-mode.md) records precise, step-by-step automation sequences for specific web portals.

---

## 5. Verifying Agent Awareness

After onboarding is complete, you can verify that your agent correctly recalls its guidelines:

1. Ask your agent in chat:
   > *"What browser tools do you have available, and how should you interact with web pages in this project?"*
2. Verify that the agent describes using `nova.*` tools (such as `nova.navigate`, `nova.read_dom`, `nova.click_selector`) rather than proposing external browser scripts.
3. Agents can also call [`nova.learn_onboarding_confirm`](../../mcp-reference/tools/pks-and-learning/nova-learn-onboarding-confirm.md) to register that they have read and understood the repository guidelines.

For advanced customization and multi-agent workflows, see the [Advanced Onboarding Guide](../../getting-started/advanced-onboarding.md).

---

[Back to agents](README.md) · [Connecting an agent](connecting-an-agent.md) · [Domain notes](domain-notes.md) · [Advanced onboarding](../../getting-started/advanced-onboarding.md) · [All user guides](../README.md)
