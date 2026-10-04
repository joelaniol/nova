# `nova.learn_onboarding_confirm`

> **Confirms the learn-mode onboarding for a domain with a paraphrase of its contract, so the onboarding gate stops blocking.**

* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

When an agent starts learn mode for a domain, Nova's onboarding gate returns the learn-mode contract (`structuredContent.learnOnboarding`) and holds further learn-eligible tool calls. `nova.learn_onboarding_confirm` answers that gate: the agent restates the contract in its own words (80-800 characters, no boilerplate such as "ok" or "understood", at least 4 distinct content tokens). A valid confirmation is bound to the session, the domain and the current version of the contract (`templateHash`); if the contract text changes in a later Nova version, the agent has to confirm again.

The `domain` must match an active learn-mode activation of this session, otherwise the call fails with `reasonCode: "learn.onboarding.domain_mismatch"`. A paraphrase that fails the form rules is rejected with a `learn.onboarding.paraphrase_*` reason code.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `domain` | `string` | Yes | — | — | The domain the AAG gate fired against. Must match an active learn-mode activation for this session. |
| `paraphrase` | `string` | Yes | — | 80–800 characters | Your restatement of the onboarding contract in your own words. 80-800 characters, no boilerplate, at least 4 distinct content tokens. |

Capability bundle: `task_memory` (load it with `nova.tools_bundle(bundle='task_memory')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_learn_onboarding_confirm",
  "arguments": {
    "domain": "app.example.com",
    "paraphrase": "I am learning app.example.com. I check PKS with nova.pks_match before acting, record new page behaviour as PKS candidates instead of guessing, and store every correction from the operator with nova.domain_note so later sessions reuse it."
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Onboarding confirmed for app.example.com. Future tool calls in this session will not be gated."
    }
  ],
  "structuredContent": {
    "gateId": "learn.onboarding_required",
    "status": "confirmed",
    "domain": "app.example.com",
    "templateHash": "sha256:9c1e...",
    "confirmedUtc": "2026-10-03T09:15:42.1234567Z",
    "paraphraseChars": 237
  }
}
```

---

## 4. Operational Best Practices

* **Re-read before confirming:** If the original gate response is lost, `nova.learn_onboarding_recall` returns the same contract without changing state.
* **Write a real restatement:** The paraphrase should name the platform being learned, how PKS is used and how operator corrections are kept with `nova.domain_note`.

---

## 5. Related Tools

* [`nova.learn_onboarding_recall`](nova-learn-onboarding-recall.md)
