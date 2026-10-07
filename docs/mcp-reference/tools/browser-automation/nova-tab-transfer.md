# `nova.tab_transfer`

> **Copies text from an element in one tab into an input field in another tab.**

* **Core Feature Guide:** [Input Dispatch & Shadow DOM Traversal](../../../core-features/humanized-input-engine/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.tab_transfer` copies text from an element in one tab into an input, textarea or contenteditable element in another tab, in one call. It reads the `innerText` of `sourceSelector` on the source tab, applies the optional `transform` (`trim`, or `number` to extract the first numeric value) and writes the result into `destSelector` on the destination tab. The source tab is only read and needs no claim; the destination tab must be claimed by the calling agent.

A failed read returns `ok: false` with `reasonCode: "tab_transfer.source_read_failed"`, a failed write `tab_transfer.dest_write_failed`. Transfers between a private and a persistent tab, or between two different private sessions, are refused.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `sourceTargetId` | `string` | Yes | — | — | Source tab target ID from nova.tabs. Data is read from this tab. |
| `destTargetId` | `string` | Yes | — | — | Destination tab target ID from nova.tabs. Data is written to this tab. Must be claimed by the calling agent. |
| `sourceSelector` | `string` | Yes | — | — | CSS selector on the source tab to extract text from. Reads innerText of the matched element. |
| `destSelector` | `string` | Yes | — | — | CSS selector on the destination tab to write into. Must be an input/textarea/contenteditable element. |
| `transform` | `string` | No | `"none"` | `none`, `trim`, `number` | Optional transform: 'none' = raw text, 'trim' = whitespace trimmed, 'number' = extract first numeric value. |
| `maxChars` | `integer` | No | `10000` | 1–50000 | Maximum characters to transfer. |
| `agentId` | `string` | No | — | — | Agent identity for claim authorization on the destination tab. Defaults to 'default'. |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_tab_transfer",
  "arguments": {
    "sourceTargetId": "tab-1",
    "destTargetId": "tab-2",
    "sourceSelector": "#order-number",
    "destSelector": "input[name='reference']",
    "transform": "trim"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Transferred 9 chars from tab-1 to tab-2"
    }
  ],
  "structuredContent": {
    "ok": true,
    "sourceTargetId": "tab-1",
    "destTargetId": "tab-2",
    "sourceSelector": "#order-number",
    "destSelector": "input[name='reference']",
    "transform": "trim",
    "transferredText": "A-1048-77",
    "chars": 9,
    "truncated": false
  }
}
```

---

## 4. Operational Best Practices

* **Claim First:** Claim the destination tab with `nova.tab_claim` before the transfer.
* **Clean Values:** Use `transform: "number"` when copying prices or counts into numeric fields.

---

## 5. Related Tools

* [`nova.tab_claim`](nova-tab-claim.md)
* [`nova.tab_snapshot`](nova-tab-snapshot.md)
