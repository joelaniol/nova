# `nova.perceive_snapshot_query`

> **Queries structured state and elements from a cached perceive snapshot without re-rendering.**

* **Capability Bundle:** `page_read_debug`
* **Security Tier:** Tier 1 (Read-Only Extraction)
* **Core Feature Guide:** [DOM Perception & Semantic Extraction](../../../core-features/tob.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.perceive_snapshot_query` performs fast queries against the most recent perception cache, avoiding redundant screenshot generation and DOM parsing.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `caseSensitive` | `boolean` | No | If true, search matching is case-sensitive. Applies to both 'contains' and 'regex' modes. |
| `chunkChars` | `integer` | No | Maximum characters per returned chunk when reading path or node payloads. |
| `chunkIndex` | `integer` | No | Zero-based chunk index for op='read_chunk' or op='read_node'. Ignored by summary, read_path, and outline. |
| `contextChars` | `integer` | No | Number of surrounding characters to include before and after each search match snippet. |
| `match` | `string` | No | Search mode for op='search'. 'contains': substring search. 'regex': .NET regular expression applied to the serialized path payload with a bounded 200 ms safety timeout. |
| `maxResults` | `integer` | No | Maximum number of search matches to return for op='search'. |
| `node` | `string` | No | Required when op='read_node'. Named alias for a common DOM region; resolved internally to the canonical snapshot path. |
| `op` | `string` | No | Query operation. 'summary': snapshot metadata + available paths. 'read_path': first chunk for a resolved path. 'read_chunk': specific chunk index for a path. 'search': find text or regex matches inside a serialized path payload. 'outline': bounded structural overview of the snapshot tree. 'read_node': read a named alias (see `node`) without typing the full dotted path. |
| `path` | `string` | No | Optional snapshot path such as 'extraction', 'extraction.outerHTML', 'extraction.elements', or 'deepModalScan'. Dotted segments support array indexes like 'extraction.iframes[0]'. |
| `query` | `string` | No | Search text or regex pattern. Required when op='search'. |
| `snapshotId` | `string` | **Yes** | Snapshot ID from structuredContent.snapshot.snapshotId returned by nova.perceive when a full-mode response was saved for overflow follow-up. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_perceive_snapshot_query",
  "arguments": {
    "snapshotId": "snap-4012",
    "query": "buttons in header"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Found 3 buttons in snapshot header region."
    }
  ],
  "structuredContent": {
    "ok": true,
    "snapshotId": "snap-4012",
    "results": [
      {
        "text": "Log In",
        "selector": "header .login-btn"
      },
      {
        "text": "Sign Up",
        "selector": "header .signup-btn"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Token & Perf Optimization:** Query cached perception snapshots instead of repeatedly invoking full perception.

---

## 5. Related Tools

* [`nova.perceive`](nova-perceive.md)
* [`nova.read_text_structured`](nova-read-text-structured.md)
