# `nova.run_sequence`

> **Executes an ordered sequence of tool calls (navigation, click, type, wait, and more) in a single RPC round-trip.**

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
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

Each step is a tool call: `tool` names an existing MCP tool (e.g. `nova.type_selector`), and `args` carries that tool's own arguments. There is no shorthand `action`/`selector` step syntax — resolve each step's argument contract from `tools/list` or `nova.tools_bundle(includeInputSchema=true)`.

### JSON-RPC Request
```json
{
  "name": "nova.run_sequence",
  "arguments": {
    "targetId": "tab-1",
    "steps": [
      {
        "tool": "nova.type_selector",
        "args": { "selector": "#first-name", "text": "Jane" }
      },
      {
        "tool": "nova.type_selector",
        "args": { "selector": "#last-name", "text": "Doe" }
      },
      {
        "tool": "nova.click_selector",
        "args": { "selector": "#submit" }
      }
    ]
  }
}
```

### JSON-RPC Response (abbreviated)
```json
{
  "content": [
    {
      "type": "text",
      "text": "Sequence OK: 3/3 steps, 842ms."
    }
  ],
  "structuredContent": {
    "ok": true,
    "completedSteps": 3,
    "totalSteps": 3,
    "durationMs": 842,
    "failedAt": null,
    "failedTool": null,
    "reasonCode": null,
    "summary": "Sequence completed: 3/3 steps in 842ms."
  }
}
```
The full payload also carries `trace[]` (per-step results), `tabState`, and `pksMode`/`advice`; this is a trimmed excerpt. On failure, `failedAt` is the 1-based step index and `failedTool` names the tool that failed.

---

## 4. Operational Best Practices

* **Multi-Field Forms:** Reduces round-trip overhead when filling several fields and submitting in one call.
* **Fail-Fast by Default:** The default `onError.action` is `abort`, which halts the sequence at the first failing step. Pass `defaults.onError` or a per-step `onError` to `continue`, `retryStep`, or run recovery steps (`runThenRetry`) instead.

---

## 5. Related Tools

* [`nova.click_selector`](nova-click-selector.md)
* [`nova.type_selector`](nova-type-selector.md)
