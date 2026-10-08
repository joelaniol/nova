# Web Storage

Start by inspecting storage keys on the affected page. If one saved preference or stale application value is the problem, changing or deleting that key is narrower than clearing all storage in a profile.

## Two storage types

| Type | Meaning |
|---|---|
| `localStorage` (`storageType: local`) | Origin-specific persistent Web Storage; tabs using that origin in the same profile can share it. |
| `sessionStorage` (`storageType: session`) | Web Storage associated with the page's origin and tab session. |

Nova's storage tools operate on the target's current top-level document. They do not provide a cross-origin inventory of every embedded frame or every website in the profile. Navigating the target can change the origin being inspected.

## Inspect, change or delete individual keys

`nova.storage_inspect` returns keys by default. `keyFilter` narrows the requested inventory; `maxEntries` and `valueMaxChars` bound the result. A limited result or shortened value is not a complete export. `includeValues=true` requests values and can require permission for a sensitive read.

`nova.storage_set` writes a string value to the chosen store. `nova.storage_delete` removes one named key. Choose the storage type explicitly and re-check the website after a change: the application may still hold an old value in memory or recreate a deleted entry.

## IndexedDB and other storage boundaries

These tools inspect and edit Web Storage only. They do not expose an IndexedDB record editor or a Cache Storage entry browser. IndexedDB can be removed through profile-level `allDomStorage` cleanup, which also removes localStorage and sessionStorage. Even the `localStorage` category accepted by `nova.cache_clear` clears that combined set; it is not an origin-local or localStorage-only operation.

For those broader categories, use [Cache & Cleanup](../cache-and-cleanup/README.md). For manual storage previews, see [Cookie Inspector](../cookie-inspector/README.md).

## Observe IndexedDB activity through Session Recording

[Session Recording](../../session-recording/README.md) offers a separate diagnostic path: a recording can capture IndexedDB operation metadata, including database/store names, operation types and hashed keys, in `indexeddb-ops.jsonl`. This describes captured activity; it is not an inventory or editor of every record already stored in a database.

Stored values are a separate opt-in stream requiring the secret-bearing `indexeddb_values` permission class. The default recording classes do not include those values. Captured streams, limits and any dropped events determine what evidence is available; an empty or missing stream does not prove that the database is empty. See the [recorded-events reference](../../../mcp-reference/tools/session-recording/nova-session-record-events.md).

## Map stored values into a replay request

[Request replay session adoption](../../network/network-interception/README.md#adopt-a-browser-session-with-a-redacted-preview) can read explicitly named local/session storage keys and map them to request headers. The mapping does not invent a header name or authentication prefix. Missing keys are errors, and adopted values are withheld from the preview. This integration uses the [site-data permission gate](../permissions-and-audit/README.md).

## Tool reference

[Inspect](../../../mcp-reference/tools/site-data-and-identity/nova-storage-inspect.md) · [Set](../../../mcp-reference/tools/site-data-and-identity/nova-storage-set.md) · [Delete](../../../mcp-reference/tools/site-data-and-identity/nova-storage-delete.md)

[Site Data Management](../README.md)
