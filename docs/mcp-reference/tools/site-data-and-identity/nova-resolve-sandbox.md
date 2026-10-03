# `nova.resolve_sandbox`

Resolves the best matching sandbox container for a given workflow intent.

---

## 1. Overview

`nova.resolve_sandbox` evaluates registered sandbox profiles against a task intent key (e.g. `email.compose`, `crm.salesforce`, `personal.shopping`) to route agents to the correct isolated cookie jar and login session.

* **Capability Bundle:** `site_data_management`
* **Security Tier:** Tier 1 (Resolution Routing)
* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`accountHint`** | `string` | No | `null` | Optional account label hint (e.g. 'work', 'personal', 'pro'). Boosts sandboxes with matching detected account. |
| **`intentKey`** | `string` | Yes | `null` | Normalized intent key describing the desired action (e.g. 'email.compose', 'chat.ask', 'project.open', 'code.review', 'docs.edit'). |
| **`serviceHint`** | `string` | No | `null` | Optional service key hint (e.g. 'gmail', 'chatgpt', 'jira'). Boosts sandboxes running this service. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.resolve_sandbox",
  "arguments": {
    "intentKey": "email.work",
    "serviceHint": "google"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Resolved intent 'email.work' to sandbox sb-work-01 (Work)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "intentKey": "email.work",
    "matchedSandboxId": "sb-work-01",
    "sandboxName": "Work",
    "confidence": 0.95
  }
}
```

---

## 4. Operational Best Practices

* **Intent-Based Dispatch:** Always resolve sandboxes dynamically rather than hardcoding sandbox IDs in multi-tenant agent setups.

---

## 5. Related Tools

* [`nova.sandbox_context`](nova-sandbox-context.md)
* [`nova.sandbox_create`](nova-sandbox-create.md)
