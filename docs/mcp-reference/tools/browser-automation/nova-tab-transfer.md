# `nova.tab_transfer`

> **Moves an open browser tab from one sandbox container profile to another.**

* **Capability Bundle:** `browser_automation`
* **Security Tier:** Tier 2 (Sandbox Management)
* **Core Feature Guide:** [Humanized Input & Navigation](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.tab_transfer` migrates a live URL context between sandboxes, switching cookie jars and storage partitions cleanly.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Agent identity for claim authorization on the destination tab. Defaults to 'default'. |
| `destSelector` | `string` | **Yes** | CSS selector on the destination tab to write into. Must be an input/textarea/contenteditable element. |
| `destTargetId` | `string` | **Yes** | Destination tab target ID from nova.tabs. Data is written to this tab. Must be claimed by the calling agent. |
| `maxChars` | `integer` | No | Maximum characters to transfer. |
| `sourceSelector` | `string` | **Yes** | CSS selector on the source tab to extract text from. Reads innerText of the matched element. |
| `sourceTargetId` | `string` | **Yes** | Source tab target ID from nova.tabs. Data is read from this tab. |
| `transform` | `string` | No | Optional transform: 'none' = raw text, 'trim' = whitespace trimmed, 'number' = extract first numeric value. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_tab_transfer",
  "arguments": {
    "targetId": "tab-1",
    "targetSandboxId": "sandbox-b"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Transferred tab-1 to sandbox-b."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "newSandboxId": "sandbox-b"
  }
}
```

---

## 4. Operational Best Practices

* **Profile Isolation:** Transfer authenticated tabs into isolated work sandboxes to segment tasks.

---

## 5. Related Tools

* [`nova.resolve_sandbox`](../site-data-and-identity/nova-resolve-sandbox.md)
* [`nova.tab_snapshot`](nova-tab-snapshot.md)
