# `nova.external_server_import`

Imports MCP server definitions from Claude Desktop, VS Code, Claude Code, or JSON config files.

---

## 1. Overview

`nova.external_server_import` scans external agent configurations (e.g. `claude_desktop_config.json`, VS Code MCP configs) and imports registered servers into Nova, skipping existing entries.

* **Capability Bundle:** `external_mcp`
* **Security Tier:** Tier 3 (High-Impact)
* **Core Architecture Guide:** [Plugins & External Extensions](../../../core-features/plugins.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`source`** | `string` | Yes | `none` | Config source: `"claude_desktop"`, `"vscode"`, `"claude_code"`, or `"file"`. |
| **`filePath`** | `string` | Conditional | `auto-detected` | File path to config. Auto-detected for standard clients; required when `source: "file"`. |
| **`serverName`** | `string` | No | `all` | Import specific server by name. Omit to import all. |
| **`autoStart`** | `boolean` | No | `false` | Automatically start imported servers after registration. |
| **`_meta`** | `object` | Yes | `none` | Audit intent metadata. |

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
