# `nova.setup_status`

> **Reports the connection and configuration health of AI agent runtimes on the host machine.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.setup_status` reports, for Claude Code, Codex, Antigravity, and Claude Desktop, whether each client is installed, registered with Nova's MCP endpoint, and currently connected, plus whether an access key exists for this Nova instance.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
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
      "text": "Connected programs: 1/2 installed."
    }
  ],
  "structuredContent": {
    "ok": true,
    "agentAccessEnabled": true,
    "alreadyConfigured": true,
    "anyConnected": true,
    "anyNeedsAction": true,
    "endpoint": "http://127.0.0.1:27183/mcp",
    "endpointIsLive": true,
    "hasAccessKey": true,
    "programs": [
      {
        "program": "Claude Code",
        "state": "connected",
        "installed": true,
        "connected": true,
        "needsAction": false,
        "detail": null,
        "configPath": "C:\\Users\\<user>\\.claude.json"
      },
      {
        "program": "Codex",
        "state": "not_registered",
        "installed": true,
        "connected": false,
        "needsAction": true,
        "detail": null,
        "configPath": "C:\\Users\\<user>\\.codex\\config.toml"
      }
    ]
  }
}
```

`state` is one of `connected`, `not_installed`, `not_registered`, `outdated`, `sync_disabled`, `proxy_missing`, or `unreadable`.

---

## 4. Operational Best Practices

* **Diagnostics:** Run when an agent experiences connection drops or when a client appears not to see Nova's tools.

---

## 5. Related Tools

* [`nova.setup_wizard_open`](nova-setup-wizard-open.md)
* [`nova.install_onboarding`](nova-install-onboarding.md)
