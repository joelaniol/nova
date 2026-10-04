# `nova.learn_onboarding_recall`

> **Re-reads the PKS learn-mode onboarding briefing for a domain without re-triggering the gate.**

* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

This is not about dismissing a website's own onboarding tour. The first learn-eligible PKS tool call for a (session, domain) pair fires an onboarding gate that delivers a fixed briefing — PKS mechanics, recommended tools/tactics, existing domain/operator notes, the operator-feedback contract, and the mandatory deliverable — which the agent must acknowledge via [`nova.learn_onboarding_confirm`](nova-learn-onboarding-confirm.md) before further learn-mode calls stop being gated. `nova.learn_onboarding_recall` is a read-only way to re-fetch that same briefing mid-session (e.g. if the agent lost the original gate response) without changing any state. When `domain` is omitted, the session's currently activated learn-mode domain is used; if none is active, the call fails with invalid params.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `domain` | `string` | No | — | — | Optional. When omitted, the session's currently activated learn-mode domain is used. |

Capability bundle: `task_memory` (load it with `nova.tools_bundle(bundle='task_memory')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_learn_onboarding_recall",
  "arguments": {
    "domain": "app.example.com"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Learn-onboarding payload for app.example.com."
    }
  ],
  "structuredContent": {
    "learnOnboarding": {
      "gateId": "learn.onboarding_required",
      "status": "awaiting_confirm",
      "domain": "app.example.com",
      "pksMechanics": "PKS phenomena are written as Shadow (LearningLevel.Shadow). nova.learn_promote moves a Shadow phenomenon to Active. ...",
      "recommendedToolsAndTactics": "This list is not exhaustive ... (abbreviated)",
      "existingPksDataHint": "Before writing new phenomena: check via nova.pks_list(scope=<domain>) or nova.pks_match ... (abbreviated)",
      "operatorFeedbackContract": "Watch for operator feedback in chat. ... (abbreviated)",
      "existingMemory": {
        "domainNotes": null,
        "operatorNotes": null,
        "domainNotesTruncated": false,
        "operatorNotesTruncated": false
      },
      "deliverable": "Mandatory final output: a PLATFORM_PLAYBOOK artifact with the sections defined in the learn-mode contract. ... (abbreviated)",
      "templateHash": "sha256:..."
    },
    "isLearnSessionActive": true
  }
}
```

The long prose fields above are abbreviated here; the real response returns their full fixed text. `status` is always the literal `"awaiting_confirm"` label from the template — it does not reflect whether this particular session already confirmed (see `isLearnSessionActive` for that).

---

## 4. Operational Best Practices

* **Re-read Mid-Session:** Call this when the original onboarding gate response from `nova.get_instructions(mode='learn', domain=...)` was lost, instead of guessing the contract's contents.

---

## 5. Related Tools

* [`nova.learn_onboarding_confirm`](nova-learn-onboarding-confirm.md)
