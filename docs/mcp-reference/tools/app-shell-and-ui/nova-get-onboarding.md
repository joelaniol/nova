# `nova.get_onboarding`

> **Retrieves manual onboarding instructions and template markdown files for external AI agents.**

* **Security Tier:** Tier 1 (Read-Only Onboarding)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.get_onboarding` outputs instructions for configuring MCP client configurations in Claude Desktop, Codex, and other LLM runtimes.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

Capability bundles: `onboarding`, `system_tools`.
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_get_onboarding",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Onboarding setup instructions returned."
    }
  ],
  "structuredContent": {
    "ok": true,
    "clientTypes": [
      "Claude Code",
      "Codex",
      "Claude Desktop"
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Manual Setup Fallback:** Use when `nova.install_onboarding` cannot write to target project directories.

---

## 5. Related Tools

* [`nova.install_onboarding`](nova-install-onboarding.md)
* [`nova.setup_status`](nova-setup-status.md)
