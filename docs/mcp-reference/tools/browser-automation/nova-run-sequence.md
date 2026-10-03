# `nova.run_sequence`

> **Executes an atomic sequence of navigation, click, type, and wait steps in a single RPC round-trip.**

* **Security Tier:** Tier 2 (Composite Macro Execution)
* **Core Feature Guide:** [Humanized Input & Navigation](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.run_sequence` bundles multiple UI actions together, minimizing network latency when performing multi-step interactions like filling a 5-field registration form.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs. Resolved once and injected only into target-aware steps. |
| `agentId` | `string` | No | `"default"` | — | Optional agent identity for claim ownership checks. Propagated only to claim-sensitive inner step tools. Defaults to 'default'. |
| `totalTimeoutMs` | `integer` | No | `120000` | 5000–300000 | Sequence-level timeout budget in milliseconds. |
| `steps` | `array` of `object` | Yes | — | 1–50 items | Ordered list of tool calls to execute. |
| `defaults` | `object` | No | — | — | Default retry/onError policy applied to all steps unless a step overrides it. |
| `defaults.stepPolicy` | `object` | No | — | — | Default retry policy applied to steps that do not provide their own policy. |
| `defaults.onError` | `object` | No | — | — | Default error handling applied to all steps. |
| `options` | `object` | No | — | — | Sequence-level response and PKS options. |
| `options.compactTrace` | `boolean` | No | `true` | — | If true, return condensed per-step results (status + timing only). |
| `options.includeTabState` | `boolean` | No | `true` | — | If true, include tab URL/title after the sequence completes. |
| `options.includeSummary` | `boolean` | No | `true` | — | If true, include pass/fail/skip counts after the sequence completes. |
| `options.verboseStepResults` | `boolean` | No | `false` | — | If true, include the full tool result in each step trace. This can be large. |
| `options.maxTraceSteps` | `integer` | No | `200` | 1–500 | Maximum number of trace entries (including retries) before truncation. |
| `options.pksMode` | `string` | No | `"match"` | `off`, `match`, `telemetry` | off suppresses PKS hints, match returns compact PKS hints, telemetry returns the full PKS payload and advice. |

Capability bundles: `browser_automation`, `form_submission`.
<!-- /generated:parameters -->

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
