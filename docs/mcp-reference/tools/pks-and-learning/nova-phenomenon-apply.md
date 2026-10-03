# `nova.phenomenon_apply`

> **Executes a stored PKS phenomenon fast-path interaction sequence directly on the page.**

* **Security Tier:** Tier 2 (Macro Execution)
* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.phenomenon_apply` executes a compiled, verified phenomenological playbook with built-in retries and assertions.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `scope` | `string` | Yes | — | — | Domain scope (e.g. 'chatgpt.com'). |
| `phenomenonId` | `string` | Yes | — | — | Phenomenon ID from PKS. |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `maxSteps` | `integer` | No | `10` | 1–20 | Maximum playbook steps to execute before stopping. |
| `timeoutMs` | `integer` | No | `15000` | 1000–60000 | Total timeout for the entire playbook execution. |
| `observation` | `object` | No | — | — | Optional fresh fingerprint snapshot from a recent perceive/match pass. When provided, Nova evaluates drift against the phenomenon baseline before applying. |
| `observation.signals` | `array` of `object` | No | — | — | Observed fingerprint signals used for drift evaluation. Each signal provides kind, match, and optional locale. |
| `observation.minConfidence` | `number` | No | `0.5` | 0–1 | Minimum confidence for the provided observation snapshot. |

Capability bundle: `pks_learning` (load it with `nova.tools_bundle(bundle='pks_learning')`).
<!-- /generated:parameters -->

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
