# `nova.phenomenon_apply`

> **Executes a stored PKS phenomenon fast-path interaction sequence directly on the page.**

* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.phenomenon_apply` executes a stored phenomenon's playbook step by step (click/type/press_key/wait/dismiss actions), with fallback-selector retries per step and post-run `verify` checks. The phenomenon must be at learning level `Active`; Candidate or Shadow phenomena are rejected (`reasonCode: "pks.not_active"`) so an agent cannot auto-apply an unverified playbook. The call also reports its own outcome back into PKS telemetry — a separate `nova.telemetry_report` call is optional, not required, after this tool.

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
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_phenomenon_apply",
  "arguments": {
    "scope": "example.com",
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
      "text": "Playbook executed successfully: 2 steps for phenom-dismiss-newsletter@example.com in 340ms."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "reasonCode": null,
    "scope": "example.com",
    "phenomenonId": "phenom-dismiss-newsletter",
    "phenomenonType": "modal",
    "policy": "reject_preferred",
    "stepsExecuted": 2,
    "failedStepIndex": null,
    "stepResults": [
      { "index": 0, "action": "click", "selector": "button#btn-reject-all", "ok": true, "elapsedMs": 180 }
    ],
    "verifyResults": null,
    "telemetryReported": true,
    "elapsedMs": 340,
    "driftGate": null
  }
}
```

`stepResults` is abbreviated here; each entry's shape depends on the action type (click/type/press_key/wait/dismiss). On failure, `ok` is `false`, `status` becomes `"error"`/`"rejected"`/`"blocked"`, `reasonCode` is set (e.g. `pks.not_active`, `pks.playbook_timeout`, `pks.drift_blocked`, `pks.empty_playbook`), and `failedStepIndex` points at the failing step.

---

## 4. Operational Best Practices

* **Zero-Prompt Fast Paths:** Use learned phenomena to bypass complex multi-step UI obstacles instantly — but only phenomena already promoted to `Active` are eligible; Shadow/Candidate phenomena must be promoted first (see [`nova.explain`](nova-explain.md)).

---

## 5. Related Tools

* [`nova.pks_get`](nova-pks-get.md)
* [`nova.explain`](nova-explain.md) — Check promotion status before relying on auto-apply.
* [`nova.revalidate`](nova-revalidate.md)
