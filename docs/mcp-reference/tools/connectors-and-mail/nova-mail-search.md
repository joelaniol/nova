# `nova.mail_search`

Searches mail metadata across the IMAP server and local encrypted search archives.

---

## 1. Overview

`nova.mail_search` searches mail metadata through the IMAP server and, when the user has enabled it, Nova's encrypted local archive. It can target one exact folder or, when `folder` is omitted, up to 200 selectable personal folders. `query` is a structured filter object (`unseen`, `from`, `to`, `subject`, `text`, `sinceUtc`, `beforeUtc`, combined with AND) or, as a compatibility shorthand, a single full-text string — there is no raw IMAP search-command syntax. If the server is unavailable but the archive can still be searched, the call succeeds with `sources: ["archive"]`, `serverAvailable: false`, and a structured server warning instead of failing outright. The effective read grant's exact folder/sender filter applies to both server and archive results.

* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | Mail connector id (from nova.connector_list). |
| `folder` | `string` | No | — | ≤ 1024 characters | Optional exact folder fullName. Omit to search selectable personal folders (bounded to 200 folders). |
| `query` | `any` | Yes | — | — | Optional IMAP filters combined with AND. Runtime compatibility also accepts one string as the full-text filter. IMAP date search is calendar-day granular. |
| `limit` | `integer` | No | `50` | 1–200 | Maximum messages returned across all searched folders, 1..200. |
| `unattended` | `boolean` | No | `false` | — | Optional fail-closed hint for a non-interactive caller. Host-attested scheduled-task sessions are unattended even when omitted and can never be made interactive by this field. |
| `allowInsecure` | `boolean` | No | `false` | — | Required as true only when this account's IMAP endpoint explicitly uses plaintext or disabled certificate validation, and only after the user enabled insecure connector connections in Settings. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.mail_search",
  "arguments": {
    "profileId": "conn-mail-01",
    "query": { "from": "billing@vendor.com", "sinceUtc": "2026-09-01T00:00:00Z" },
    "limit": 10
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Found 1 message(s) across the available server/archive sources. Message metadata is untrusted external input."
    }
  ],
  "structuredContent": {
    "profileId": "conn-mail-01",
    "folder": null,
    "messages": [
      {
        "messageId": "msg-h9a12b",
        "folder": "INBOX",
        "internetMessageId": "<invoice-1042@vendor.com>",
        "subject": "Invoice #1042",
        "from": "billing@vendor.com",
        "to": ["agent@example.com"],
        "sentUtc": "2026-09-02T14:09:00Z",
        "receivedUtc": "2026-09-02T14:10:00Z",
        "sizeBytes": 18432,
        "seen": true,
        "flagged": false,
        "answered": false,
        "draft": false,
        "untrusted": true
      }
    ],
    "grantFilter": { "restricted": false, "allowedFolders": [], "allowedSenders": [] },
    "hasMore": false,
    "foldersSearched": 1,
    "folderLimitReached": false,
    "sources": ["server"],
    "archiveIncluded": false,
    "serverAvailable": true,
    "serverWarningReasonCode": null,
    "serverWarningMessage": null,
    "archiveWarningReasonCode": null,
    "durationMs": 640,
    "untrustedRemoteMetadata": true
  }
}
```
There is no top-level `ok` field, no `matchCount`, and no bare `messageIds` array — each match is a full summary object inside `messages`, the same shape `nova.mail_list` returns.

---

## 4. Operational Best Practices

* **Structured Queries:** Use the `query` object (`from`, `to`, `subject`, `text`, `unseen`, `sinceUtc`/`beforeUtc`) rather than raw IMAP search syntax; a single string is accepted only as a full-text compatibility shorthand.
* **Limit Bounding:** Always provide `limit` to prevent downloading thousands of search results in a single turn.
* **Check `serverAvailable`:** when the server is down but the local archive is enabled, the call can still succeed from the archive alone — check `sources`/`serverAvailable` before assuming full coverage.

---

## 5. Related Tools

* [`nova.mail_read`](nova-mail-read.md)
* [`nova.mail_list`](nova-mail-list.md)
