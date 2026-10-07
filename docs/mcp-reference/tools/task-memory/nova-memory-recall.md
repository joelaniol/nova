# `nova.memory_recall`

Recalls browsing memories and stored preferences for a domain or across all sites.

---

## 1. Overview

`nova.memory_recall` retrieves stored browsing memories (notes, preferences and context entries saved with `nova.memory_note`), optionally filtered by domain, free-text query, or memory type. Each hit resets the memory's access time and increases its access count, which slows its relevance decay.

* **Core Architecture Guide:** [Browser Memory & Knowledge Board](../../../core-features/browser-memory/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `domain` | `string` | No | — | — | Filter to this domain (e.g. 'github.com'). Omit to search across all domains. |
| `query` | `string` | No | — | — | Free-text search in memory content. |
| `memoryType` | `string` | No | — | `note`, `preference`, `context` | Filter by memory type. note = explicit agent/user notes, preference = user behavioral preferences, context = last session state on a domain. |
| `limit` | `integer` | No | `10` | 1–50 | Max results to return. Defaults to 10. |
| `includeExpired` | `boolean` | No | `false` | — | Include memories with very low decay scores that would normally be filtered. Defaults to false. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "{\"memories\":[{\"memoryId\":301,\"domain\":\"billing.example.com\",\"urlPattern\":null,\"memoryType\":\"preference\",\"content\":\"User prefers German language invoices when available\",\"source\":\"agent\",\"decayScore\":0.97,\"accessCount\":3}],\"count\":1}"
    }
  ],
  "structuredContent": {
    "memories": [
      {
        "memoryId": 301,
        "domain": "billing.example.com",
        "urlPattern": null,
        "memoryType": "preference",
        "content": "User prefers German language invoices when available",
        "source": "agent",
        "decayScore": 0.97,
        "accessCount": 3
      }
    ],
    "count": 1
  }
}
```

There is no top-level `ok` field. When nothing matches, `memories` is an empty array and `count` is `0`.

---

## 4. Operational Best Practices

* **Pre-Task Orientation:** Recall memories when starting a user-centric task to adopt personal preferences.

---

## 5. Related Tools

* [`nova.memory_note`](nova-memory-note.md)
* [`nova.memory_forget`](nova-memory-forget.md)
