# `nova.external_server_import`

Imports MCP server definitions from Claude Desktop, VS Code, Claude Code, or JSON config files.

---

## 1. Overview

`nova.external_server_import` scans external agent configurations (e.g. `claude_desktop_config.json`, VS Code MCP configs) and imports registered servers into Nova, skipping existing entries.

* **Core Architecture Guide:** [External MCP Servers](../../../core-features/connectors/external-mcp/README.md)

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
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
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
      "text": "Imported 2 server(s) from claude_desktop. Skipped 1."
    }
  ],
  "structuredContent": {
    "ok": true,
    "source": "claude_desktop",
    "filePath": "C:\\Users\\you\\AppData\\Roaming\\Claude\\claude_desktop_config.json",
    "totalFound": 3,
    "totalImported": 2,
    "imported": [
      {
        "serverKey": "f1a2b3c4",
        "displayName": "postgres-db",
        "transport": "stdio",
        "status": "Stopped"
      },
      {
        "serverKey": "a9b8c7d6",
        "displayName": "github-mcp",
        "transport": "stdio",
        "status": "Stopped"
      }
    ],
    "capReached": false,
    "skipped": [
      {
        "name": "filesystem-mcp",
        "reason": "Already exists."
      }
    ]
  }
}
```

Imported servers are never auto-started unless `autoStart: true` is passed; `status` is `"Stopped"` right after import in that case. `capReached: true` means the 50-server limit was hit partway through and the import stopped early.

---

## 4. Operational Best Practices

* **Deduplication:** An entry is skipped as "Already exists" when its transport, command (or endpoint URL), arguments, and working directory all match an already-configured server.

---

## See Also

* [`nova.external_servers`](nova-external-servers.md) - List configured servers.
* [External MCP Servers Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
