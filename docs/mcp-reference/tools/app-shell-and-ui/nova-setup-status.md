# `nova.setup_status`

> **Reports the connection and configuration health of AI agent runtimes on the host machine.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 1 (System Configuration Status)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.setup_status` audits active integrations with Claude Code, Codex, Antigravity, and Claude Desktop, checking MCP config files and bearer token freshness.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_setup_status",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Agent setup status: Claude Code (Connected), Antigravity (Connected), Codex (Not Configured)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "integrations": [
      {
        "client": "Claude Code",
        "status": "Connected"
      },
      {
        "client": "Antigravity",
        "status": "Connected"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Diagnostics:** Run when an agent experiences connection drops or authentication failures.

---

## 5. Related Tools

* [`nova.setup_wizard_open`](nova-setup-wizard-open.md)
* [`nova.install_onboarding`](nova-install-onboarding.md)
