# `nova.memory_recall`

Recalls browsing memories and stored preferences for a domain or across all sites.

---

## 1. Overview

`nova.memory_recall` retrieves relevant user preferences, session contexts, and domain notes using semantic relevance and keyword scoring.

* **Capability Bundle:** `task_memory`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`domain`** | `string` | No | `null` | Filter to this domain (e.g. 'github.com'). Omit to search across all domains. |
| **`includeExpired`** | `boolean` | No | `false` | Include memories with very low decay scores that would normally be filtered. Defaults to false. |
| **`limit`** | `integer` | No | `10` | Max results to return. Defaults to 10. |
| **`memoryType`** | `string` | No | `null` | Filter by memory type. note = explicit agent/user notes, preference = user behavioral preferences, context = last session state on a domain. |
| **`query`** | `string` | No | `null` | Free-text search in memory content. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.memory_recall",
  "arguments": {
    "domain": "billing.example.com"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Recalled 1 memory for billing.example.com."
    }
  ],
  "structuredContent": {
    "ok": true,
    "memories": [
      {
        "memoryId": "mem-301a",
        "content": "User prefers German language invoices...",
        "memoryType": "preference"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Pre-Task Orientation:** Recall memories when starting a user-centric task to adopt personal preferences.

---

## 5. Related Tools

* [`nova.memory_note`](nova-memory-note.md)
* [`nova.operator_notes_query`](nova-operator-notes-query.md)
