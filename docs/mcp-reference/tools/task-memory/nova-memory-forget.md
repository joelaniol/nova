# `nova.memory_forget`

Deletes browsing memories matching domain, memoryType, or text query filters.

---

## 1. Overview

`nova.memory_forget` permanently deletes browsing memories saved with `nova.memory_note`, matched by a single memory ID, by domain and/or memory type, or all of them at once. There is no recovery after deletion.

* **Core Architecture Guide:** [Browser Memory & Knowledge Board](../../../core-features/browser-memory/README.md)

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
Tool category: `normal` (standard risk class in Nova's agent permission settings).
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
      "text": "Deleted 2 browsing memories."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "deleted",
    "reasonCode": null,
    "deleted": 2,
    "domain": "example.com",
    "memoryId": null,
    "memoryType": "preference",
    "all": false
  }
}
```

When nothing matches (and `all` is not `true`), `deleted` is `0`, `status` is `"not_found"`, `reasonCode` is `"memory.not_found"`, and `ok` is `false`. With `all: true` and nothing to delete, `status` is `"noop"` and `ok` stays `true`.

---

## 4. Operational Best Practices

* **Targeted Filters:** Supply `domain` or `memoryType` to prevent deleting unrelated user memories.

---

## 5. Related Tools

* [`nova.memory_recall`](nova-memory-recall.md)
* [`nova.memory_note`](nova-memory-note.md)
