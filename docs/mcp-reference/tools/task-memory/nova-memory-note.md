# `nova.memory_note`

Saves a persistent browsing memory (user preference, workflow hint, domain context).

---

## 1. Overview

`nova.memory_note` records a persistent note, preference or context entry bound to a domain (and optionally a URL path pattern) that survives across sessions. Relevance decays over time by memory type; a later `nova.memory_recall` is needed to retrieve it.

* **Core Architecture Guide:** [Browser Memory & Knowledge Board](../../../core-features/learning/browser-memory/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `content` | `string` | Yes | — | ≤ 2000 characters | What to remember. Keep concise and actionable (max 2000 chars). |
| `memoryType` | `string` | No | `"note"` | `note`, `preference`, `context` | note = explicit observation/reminder, preference = user behavioral preference, context = session state snapshot. Defaults to 'note'. |
| `domain` | `string` | No | — | — | Domain to bind this memory to (e.g. 'github.com'). Defaults to the active tab's domain. |
| `urlPattern` | `string` | No | — | — | Optional URL path scope (e.g. '/pulls/*'). Memory applies only to matching paths on this domain. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.memory_note",
  "arguments": {
    "content": "User prefers German language invoices when available",
    "domain": "billing.example.com",
    "memoryType": "preference"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Memory saved (id=301, domain=billing.example.com, type=preference)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "saved": true,
    "memoryId": 301,
    "domain": "billing.example.com",
    "memoryType": "preference"
  }
}
```

If the domain is excluded by privacy policy, the response instead returns `isError: true` with `structuredContent.ok: false`, `saved: false` and `reasonCode: "browsing_memory.domain_excluded"`.

---

## 4. Operational Best Practices

* **Concise Observations:** Store clear, declarative statements of fact or preference.

---

## 5. Related Tools

* [`nova.memory_recall`](nova-memory-recall.md)
* [`nova.memory_forget`](nova-memory-forget.md)
