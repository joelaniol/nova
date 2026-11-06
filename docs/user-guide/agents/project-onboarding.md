# Project Onboarding & In-Engine Reference Documentation

> [!NOTE]
> Project Onboarding equips AI coding agents (such as Claude Code, Codex, and Antigravity) with standardized Nova browser guidelines written directly into your repository (e.g. `AGENTS.md`). In addition, Nova provides an offline in-engine reference library accessible via MCP without internet dependencies.

---

## 1. Overview: The Headless Browser Anti-Pattern

When an autonomous AI agent opens a software repository to run tests, write code, or verify web interfaces, it inspects repository instructions to understand how the environment operates.

Without onboarding guidelines, agents frequently default to the **Headless Browser Anti-Pattern**:
* Installing heavy npm/pip packages (Playwright, Puppeteer, Selenium).
* Downloading separate Chromium or Firefox browser binaries into `.cache/`.
* Spawning headless background processes that cannot access your desktop cookies, active logins, or hardware-accelerated rendering.

**Project Onboarding** eliminates this waste by generating clean, vendor-neutral instructions inside your repository, directing connected agents to use Nova's existing browser window, active sandboxes, and authenticated sessions.

```mermaid
flowchart TD
    Repo["Software Repository"] --> Check{"Does Repository have Nova Instructions?"}
    Check -->|No| Confusion["Agent attempts to install Playwright/Selenium,<br>download headless binaries, and duplicate logins"]
    Check -->|Yes (Onboarded)| Native["Agent calls Nova's MCP tools directly<br>(nova.navigate, nova.click_selector, nova.read_dom)"]

    Native --> UserSession["Uses existing desktop tabs & logins"]
    Native --> Visible["Renders visible AI assist cursor"]
    Native --> Safe["Enforces User Domain Notes & AAG"]
```

---

## 2. In-Engine Reference Library over MCP

Nova embeds an authoritative, offline technical documentation library directly inside its engine. Connected agents can read architectural guidelines, MCP tool contracts, and automation patterns without external web access:

* **List Available Reference Docs ([`nova.reference_docs_list`](../../mcp-reference/tools/app-shell-and-ui/nova-reference-docs-list.md)):**
  Retrieves the catalog of available documentation chapters stored within the application binary:
  ```json
  {
    "name": "nova.reference_docs_list",
    "arguments": {}
  }
  ```
* **Read Reference Chapter ([`nova.reference_doc_read`](../../mcp-reference/tools/app-shell-and-ui/nova-reference-doc-read.md)):**
  Streams the contents of any reference document with pagination support:
  ```json
  {
    "name": "nova.reference_doc_read",
    "arguments": {
      "docId": "quickstart",
      "cursor": 0,
      "maxChars": 8000
    }
  }
  ```

---

## 3. How to Onboard a Project Repository

Project onboarding is lightweight, non-destructive, and can be initialized in three convenient ways:

### Option A: Asking Your AI Agent in Chat (Recommended)
Instruct your agent in natural language:
> *"Please onboard this repository to use Nova AI Workspace. Call `nova.get_onboarding` and write the reference guidelines into AGENTS.md."*

The agent retrieves the standardized onboarding contract directly from Nova and merges it into your project's agent instructions.

### Option B: Automatic Tool Injection ([`nova.install_onboarding`](../../mcp-reference/tools/app-shell-and-ui/nova-install-onboarding.md))
Agents can call Nova's automated installation tool to write guidelines directly into the current repository:
```json
{
  "name": "nova.install_onboarding",
  "arguments": {}
}
```

### Option C: Via Nova Settings UI
1. Open **Menu → Settings → AI & agents → Connection & setup**.
2. Under **Project onboarding**, click **Generate onboarding notes**.
3. Select your project folder to write `AGENTS.md`.

---

## 4. Structure of Generated Onboarding Guidelines

The generated instructions establish explicit behavioral invariants for connected models:

```markdown
# Nova AI Workspace — Browser Automation Contract
- Primary Browser: Nova AI Workspace (WinUI 3 + WebView2)
- Interface: Model Context Protocol (MCP) via `nova.*` tools
- Invariants:
  1. Do NOT launch external headless browsers (Playwright, Puppeteer, Selenium).
  2. Inspect existing tabs via `nova.tabs` before opening new ones.
  3. Scope interactions to the appropriate sandbox (Work, Personal, Staging).
  4. Inspect and acknowledge user Domain Notes via `nova.domain_note_ack`.
  5. Never guess passwords; request stored credentials via Nova Vault.
```

---

## 5. Verifying & Confirming Agent Awareness

After onboarding is written to disk, agents can verify and register their understanding:

* **Register Understanding ([`nova.learn_onboarding_confirm`](../../mcp-reference/tools/pks-and-learning/nova-learn-onboarding-confirm.md)):**
  The agent registers that it has parsed and accepted the project guidelines:
  ```json
  {
    "name": "nova.learn_onboarding_confirm",
    "arguments": {
      "projectPath": "E:\dev\project",
      "guidanceVersion": "1.0"
    }
  }
  ```
* **Recall Stored Guidance ([`nova.learn_onboarding_recall`](../../mcp-reference/tools/pks-and-learning/nova-learn-onboarding-recall.md)):**
  Verify previously registered project constraints across subsequent sessions.

---

## 6. What Project Onboarding Does NOT Do

To maintain system integrity and user privacy:
* **No Client Allowlist Modification:** Onboarding does not alter or weaken your AI client's permission settings. Tool approval dialogs inside Claude Code or Codex are governed strictly by those clients.
* **No Credential Access:** It does not read, write, or export website cookies, passwords, or vault secrets.
* **Separate from Domain Notes:** Onboarding configures software code repositories; [Domain Notes](domain-notes.md) provide per-website instructions stored inside Nova.
* **Separate from Learn Mode:** Onboarding provides high-level browser guidelines; [Learn Mode](../../getting-started/learn-mode.md) records precise, step-by-step automation sequences for specific web portals.

---

## 7. Summary Tool Matrix

| Tool | Capability | Primary Use Case |
| :--- | :--- | :--- |
| [`nova.reference_docs_list`](../../mcp-reference/tools/app-shell-and-ui/nova-reference-docs-list.md) | List reference docs | Discover offline architectural guides stored in the binary. |
| [`nova.reference_doc_read`](../../mcp-reference/tools/app-shell-and-ui/nova-reference-doc-read.md) | Read reference doc | Retrieve documentation chapters over MCP with cursor pagination. |
| [`nova.get_onboarding`](../../mcp-reference/tools/app-shell-and-ui/nova-get-onboarding.md) | Retrieve onboarding text | Fetch standardized `AGENTS.md` guidelines for code repositories. |
| [`nova.install_onboarding`](../../mcp-reference/tools/app-shell-and-ui/nova-install-onboarding.md) | Install onboarding notes | Automatically inject Nova guidelines into the current project workspace. |
| [`nova.learn_onboarding_confirm`](../../mcp-reference/tools/pks-and-learning/nova-learn-onboarding-confirm.md) | Register comprehension | Confirm that the agent has parsed project guidelines. |
| [`nova.learn_onboarding_recall`](../../mcp-reference/tools/pks-and-learning/nova-learn-onboarding-recall.md) | Recall project guidance | Retrieve stored guidelines across subsequent agent sessions. |

---

## 8. Related Documentation

* **[Advanced Onboarding Guide](../../getting-started/advanced-onboarding.md)** — Deep-dive on multi-agent collaboration and project rules.
* **[Domain Notes User Guide](domain-notes.md)** — Site-specific operational guidelines and AAG gates.
* **[Connecting an Agent Guide](connecting-an-agent.md)** — Setup instructions for Claude Code, Codex, and Antigravity.
* **[Taking Over & Emergency Stop](taking-over-and-emergency-stop.md)** — Halting agent workflows and revoking tab claims.

---

[Back to Agents Hub](README.md) · [All user guides](../README.md)
