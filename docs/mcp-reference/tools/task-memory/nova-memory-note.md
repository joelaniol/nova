# `nova.memory_note`

Saves a persistent browsing memory (user preference, workflow hint, domain context).

---

## 1. Overview

`nova.memory_note` records persistent notes and preferences that survive across sessions and tasks. Automatically recalled on future interactions.

* **Capability Bundle:** `task_memory`
* **Security Tier:** Tier 2 (Memory Storage)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`content`** | `string` | Yes | `null` | What to remember. Keep concise and actionable (max 2000 chars). |
| **`domain`** | `string` | No | `null` | Domain to bind this memory to (e.g. 'github.com'). Defaults to the active tab's domain. |
| **`memoryType`** | `string` | No | `"note"` | note = explicit observation/reminder, preference = user behavioral preference, context = session state snapshot. Defaults to 'note'. |
| **`urlPattern`** | `string` | No | `null` | Optional URL path scope (e.g. '/pulls/*'). Memory applies only to matching paths on this domain. |

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
      "text": "Saved browsing memory note for billing.example.com."
    }
  ],
  "structuredContent": {
    "ok": true,
    "memoryId": "mem-301a",
    "status": "Saved"
  }
}
```

---

## 4. Operational Best Practices

* **Concise Observations:** Store clear, declarative statements of fact or preference.

---

## 5. Related Tools

* [`nova.memory_recall`](nova-memory-recall.md)
* [`nova.memory_forget`](nova-memory-forget.md)
