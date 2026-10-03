# `nova.phenomenon_apply`

> **Executes a stored PKS phenomenon fast-path interaction sequence directly on the page.**

* **Capability Bundle:** `pks_learning`
* **Security Tier:** Tier 2 (Macro Execution)
* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.phenomenon_apply` executes a compiled, verified phenomenological playbook with built-in retries and assertions.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `maxSteps` | `integer` | No | Maximum playbook steps to execute before stopping. |
| `observation` | `object` | No | Optional fresh fingerprint snapshot from a recent perceive/match pass. When provided, Nova evaluates drift against the phenomenon baseline before applying. |
| `phenomenonId` | `string` | **Yes** | Phenomenon ID from PKS. |
| `scope` | `string` | **Yes** | Domain scope (e.g. 'chatgpt.com'). |
| `targetId` | `string` | No | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `timeoutMs` | `integer` | No | Total timeout for the entire playbook execution. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_phenomenon_apply",
  "arguments": {
    "targetId": "tab-1",
    "phenomenonId": "phenom-dismiss-newsletter"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Applied phenomenon phenom-dismiss-newsletter successfully."
    }
  ],
  "structuredContent": {
    "ok": true,
    "phenomenonId": "phenom-dismiss-newsletter",
    "executedSteps": 2
  }
}
```

---

## 4. Operational Best Practices

* **Zero-Prompt Fast Paths:** Use learned phenomena to bypass complex multi-step UI obstacles instantly.

---

## 5. Related Tools

* [`nova.pks_get`](nova-pks-get.md)
* [`nova.revalidate`](nova-revalidate.md)
