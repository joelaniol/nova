# `nova.run_sequence`

> **Executes an atomic sequence of navigation, click, type, and wait steps in a single RPC round-trip.**

* **Capability Bundle:** `browser_automation`
* **Security Tier:** Tier 2 (Composite Macro Execution)
* **Core Feature Guide:** [Humanized Input & Navigation](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.run_sequence` bundles multiple UI actions together, minimizing network latency when performing multi-step interactions like filling a 5-field registration form.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim ownership checks. Propagated only to claim-sensitive inner step tools. Defaults to 'default'. |
| `defaults` | `object` | No | Default retry/onError policy applied to all steps unless a step overrides it. |
| `options` | `object` | No | Sequence-level response and PKS options. |
| `steps` | `array` | **Yes** | Ordered list of tool calls to execute. |
| `targetId` | `string` | No | Target ID from nova.tabs. Resolved once and injected only into target-aware steps. |
| `totalTimeoutMs` | `integer` | No | Sequence-level timeout budget in milliseconds. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_run_sequence",
  "arguments": {
    "targetId": "tab-1",
    "steps": [
      {
        "action": "type",
        "selector": "#first-name",
        "text": "Jane"
      },
      {
        "action": "type",
        "selector": "#last-name",
        "text": "Doe"
      },
      {
        "action": "click",
        "selector": "#submit"
      }
    ]
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Executed sequence of 3 steps successfully."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "completedSteps": 3,
    "failedStep": null
  }
}
```

---

## 4. Operational Best Practices

* **Atomic Forms:** Reduces latency overhead on multi-field forms.
* **Fail-Fast:** Halts immediately if any intermediate step fails.

---

## 5. Related Tools

* [`nova.click_selector`](nova-click-selector.md)
* [`nova.type_selector`](nova-type-selector.md)
