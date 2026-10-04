# `nova.perceive_snapshot_query`

> **Queries structured state and elements from a cached perceive snapshot without re-rendering.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.perceive_snapshot_query` performs fast queries against the most recent perception cache, avoiding redundant screenshot generation and DOM parsing.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `snapshotId` | `string` | Yes | — | — | Snapshot ID from structuredContent.snapshot.snapshotId returned by nova.perceive when a full-mode response was saved for overflow follow-up. |
| `op` | `string` | No | `"summary"` | `summary`, `read_path`, `read_chunk`, `search`, `outline`, `read_node` | Query operation. 'summary': snapshot metadata + available paths. 'read_path': first chunk for a resolved path. 'read_chunk': specific chunk index for a path. 'search': find text or regex matches inside a serialized path payload. 'outline': bounded structural overview of the snapshot tree. 'read_node': read a named alias (see `node`) without typing the full dotted path. |
| `path` | `string` | No | — | — | Optional snapshot path such as 'extraction', 'extraction.outerHTML', 'extraction.elements', or 'deepModalScan'. Dotted segments support array indexes like 'extraction.iframes[0]'. |
| `node` | `string` | No | — | `activeElement`, `ctas`, `elements`, `forms`, `headings`, `iframes`, `landmarks`, `rootElement`, `scroll`, `stats`, `viewport` | Required when op='read_node'. Named alias for a common DOM region; resolved internally to the canonical snapshot path. |
| `query` | `string` | No | — | — | Search text or regex pattern. Required when op='search'. |
| `match` | `string` | No | `"contains"` | `contains`, `regex` | Search mode for op='search'. 'contains': substring search. 'regex': .NET regular expression applied to the serialized path payload with a bounded 200 ms safety timeout. |
| `caseSensitive` | `boolean` | No | `false` | — | If true, search matching is case-sensitive. Applies to both 'contains' and 'regex' modes. |
| `chunkIndex` | `integer` | No | `0` | ≥ 0 | Zero-based chunk index for op='read_chunk' or op='read_node'. Ignored by summary, read_path, and outline. |
| `chunkChars` | `integer` | No | `4000` | 200–50000 | Maximum characters per returned chunk when reading path or node payloads. |
| `maxResults` | `integer` | No | `10` | 1–100 | Maximum number of search matches to return for op='search'. |
| `contextChars` | `integer` | No | `120` | 20–1000 | Number of surrounding characters to include before and after each search match snippet. |

Capability bundles: `browser_automation`, `form_submission`, `page_read_debug`.
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova.perceive_snapshot_query",
  "arguments": {
    "snapshotId": "snap-4012",
    "op": "search",
    "query": "Sign Up",
    "path": "extraction.outerHTML"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "[{\"index\":1824,\"length\":7,\"contextStart\":1764,\"snippet\":\"...<button class=\\\"signup-btn\\\">Sign Up</button>...\"}]"
    }
  ],
  "structuredContent": {
    "snapshotId": "snap-4012",
    "op": "search",
    "path": "extraction.outerHTML",
    "query": "Sign Up",
    "match": "contains",
    "caseSensitive": false,
    "maxResults": 10,
    "contextChars": 120,
    "totalChars": 48213,
    "matchCount": 1,
    "matches": [
      { "index": 1824, "length": 7, "contextStart": 1764, "snippet": "...<button class=\"signup-btn\">Sign Up</button>..." }
    ],
    "artifactFilePath": "C:\\Users\\GNetwork\\AppData\\Local\\NovaBrowser\\perceive-snapshots\\snap-4012.json",
    "queryTool": "nova.perceive_snapshot_query"
  }
}
```

There is no `ok` or `results` field: matches come back as `matches[]` with `index`/`length`/
`contextStart`/`snippet` (character offsets into the serialized path payload, not DOM selectors).
`op` defaults to `'summary'` when omitted, which ignores `query` entirely and instead returns
snapshot metadata (`availableOps`, `availablePaths`, `page`, `screenshot`, `metrics`) — pass
`op: 'search'` explicitly to search.

---

## 4. Operational Best Practices

* **Token & Perf Optimization:** Query cached perception snapshots instead of repeatedly invoking full perception.

---

## 5. Related Tools

* [`nova.perceive`](nova-perceive.md)
* [`nova.read_text_structured`](nova-read-text-structured.md)
