# `nova.resolve_sandbox`

Resolves the best matching sandbox container for a given workflow intent.

---

## 1. Overview

`nova.resolve_sandbox` scores every registered sandbox against a task intent key (e.g. `email.compose`), an optional `serviceHint`, and an optional `accountHint`, then returns the best match plus the full ranked candidate list and reasons for each score. It also reports four agent-guidance gates (low confidence, multiple close matches, account mismatch, target not ready) that can warn or block depending on settings.

* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `intentKey` | `string` | Yes | — | — | Normalized intent key describing the desired action (e.g. 'email.compose', 'chat.ask', 'project.open', 'code.review', 'docs.edit'). |
| `serviceHint` | `string` | No | — | — | Optional service key hint (e.g. 'gmail', 'chatgpt', 'jira'). Boosts sandboxes running this service. |
| `accountHint` | `string` | No | — | — | Optional account label hint (e.g. 'work', 'personal', 'pro'). Boosts sandboxes with matching detected account. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.resolve_sandbox",
  "arguments": {
    "intentKey": "email.compose",
    "serviceHint": "gmail"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Resolved sandbox intent 'email.compose'."
    }
  ],
  "structuredContent": {
    "matched": true,
    "intentKey": "email.compose",
    "serviceHint": "gmail",
    "accountHint": null,
    "best": {
      "targetId": "A",
      "profileId": "sb-work-01",
      "sandboxId": null,
      "sandboxRef": "8f3a2c1d9e4b4a7fa6c1d2e3f4a5b6c7",
      "semanticScore": 0.55,
      "affinityBoost": 0.0,
      "score": 0.55,
      "reasons": ["purpose=email(settings)", "service=gmail(url_match)", "url_available(live)", "webview_ready"]
    },
    "candidates": [
      {
        "targetId": "A",
        "profileId": "sb-work-01",
        "sandboxId": null,
        "sandboxRef": "8f3a2c1d9e4b4a7fa6c1d2e3f4a5b6c7",
        "semanticScore": 0.55,
        "affinityBoost": 0.0,
        "score": 0.55,
        "reasons": ["purpose=email(settings)", "service=gmail(url_match)", "url_available(live)", "webview_ready"]
      }
    ],
    "status": "ok",
    "_aagGates": {
      "scoreBelowThreshold": { "gateId": "sandbox.score_below_threshold", "status": "passed" },
      "multiMatch": { "gateId": "sandbox.multi_match", "status": "passed" },
      "accountMismatch": { "gateId": "sandbox.account_mismatch", "status": "passed" },
      "notReady": { "gateId": "sandbox.not_ready", "status": "passed" }
    }
  }
}
```

`candidates` lists every sandbox with a non-zero score, sorted best first; shown shortened to one entry here. A gate reports `status: "warned"` (or blocks the call outright, depending on settings) instead of `"passed"` when its condition triggers — for example when the best semantic score is below 0.40, or the best sandbox's WebView is not ready yet. This response has no `ok` field; use `matched`/`status` instead.

---

## 4. Operational Best Practices

* **Intent-Based Dispatch:** Always resolve sandboxes dynamically rather than hardcoding sandbox IDs in multi-tenant agent setups.
* **Read the Gates:** A `notReady` warning means the best sandbox's WebView has not been activated yet — call `nova.set_active_tab` on its `targetId` before using it.

---

## 5. Related Tools

* [`nova.sandbox_context`](nova-sandbox-context.md)
* [`nova.sandbox_create`](nova-sandbox-create.md)
