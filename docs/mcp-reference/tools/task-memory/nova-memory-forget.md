# `nova.memory_forget`

Deletes browsing memories matching domain, memoryType, or text query filters.

---

## 1. Overview

`nova.memory_forget` removes outdated or incorrect browsing memories from Nova's long-term semantic store.

* **Security Tier:** Tier 2 (Memory Deletion)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `domain` | `string` | No | — | — | Delete memories for this domain. Combine with memoryType to delete only that type on this domain. |
| `memoryId` | `integer` | No | — | ≥ 1 | Delete a single memory by its ID. |
| `memoryType` | `string` | No | — | `note`, `preference`, `context` | Delete all memories of this type across all domains, or only within domain when domain is also provided. |
| `all` | `boolean` | No | `false` | — | Delete ALL browsing memories. Use with care. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.memory_forget",
  "arguments": {
    "domain": "example.com",
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
      "text": "Deleted 2 memory entries for example.com."
    }
  ],
  "structuredContent": {
    "ok": true,
    "domain": "example.com",
    "deletedCount": 2
  }
}
```

---

## 4. Operational Best Practices

* **Targeted Filters:** Supply `domain` or `memoryType` to prevent deleting unrelated user memories.

---

## 5. Related Tools

* [`nova.memory_recall`](nova-memory-recall.md)
* [`nova.memory_note`](nova-memory-note.md)
