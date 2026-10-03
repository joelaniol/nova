# `nova.external_server_import`

Imports MCP server definitions from Claude Desktop, VS Code, Claude Code, or JSON config files.

---

## 1. Overview

`nova.external_server_import` scans external agent configurations (e.g. `claude_desktop_config.json`, VS Code MCP configs) and imports registered servers into Nova, skipping existing entries.

* **Security Tier:** Tier 3 (High-Impact)
* **Core Architecture Guide:** [Plugins & External Extensions](../../../core-features/plugins.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `source` | `string` | Yes | — | `claude_desktop`, `vscode`, `claude_code`, `file` | Config source to import from. |
| `filePath` | `string` | No | — | — | Path to config file. Auto-detected if omitted (except for source='file'). |
| `serverName` | `string` | No | — | — | Import only a specific server by name. Omit to import all. |
| `autoStart` | `boolean` | No | — | — | Automatically start imported servers after import. Default: false. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `external_mcp` (load it with `nova.tools_bundle(bundle='external_mcp')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.external_server_import",
  "arguments": {
    "source": "claude_desktop",
    "autoStart": false,
    "_meta": {
      "intent": "Import configured servers from Claude Desktop"
    }
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Imported 2 server(s) from claude_desktop (1 skipped)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "source": "claude_desktop",
    "importedCount": 2,
    "skippedCount": 1,
    "imported": [
      "postgres-db",
      "github-mcp"
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Deduplication:** Server entries with matching command and arguments are automatically recognized and skipped, preventing duplicate spawns.

---

## See Also

* [`nova.external_servers`](nova-external-servers.md) - List configured servers.
* [External MCP Servers Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
