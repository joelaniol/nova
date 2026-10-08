# `nova.network_replay`

Targeted HTTP request repeater for replaying, editing, and comparing network payloads out-of-band.

---

## 1. Overview

`nova.network_replay` provides an out-of-band HTTP repeater (similar to Burp Repeater) executed via an independent .NET HTTP client. Agents can freeze a captured request (`prepare`), mutate headers or body parameters, dispatch it once (`send`), and compare the outcome against a baseline (`compareTo`).

* **Core Architecture Guide:** [Network Interception & Request Replay](../../../core-features/network/network-interception/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `agentId` | `string` | No | — | — | Agent identity owning the draft/result. Use the same identity for prepare/send/get/discard; defaults to 'default'. Does not claim a tab. |
| `action` | `string` | No | `"prepare"` | `prepare`, `send`, `get`, `discard` | prepare validates/freezes a request; send consumes replayId once; get reads status/result; discard releases an idle draft/result, never undoing server actions. |
| `replayId` | `string` | No | — | — | Opaque ID returned by prepare; required for send/get/discard. Never replace it to retry an uncertain send. |
| `url` | `string` | No | — | — | prepare: required absolute HTTP(S) URL, max 16384 characters, no userinfo or fragment. Destination is explicit, not taken from an active tab. |
| `method` | `string` | No | `"GET"` | — | prepare: HTTP method token, max 32 characters. CONNECT is unsupported. |
| `headers` | `object` | No | — | — | prepare: explicit request headers including Cookie/Authorization if desired; max 100 and 32768 total characters. Omit a header to remove it. Content-Length, Transfer-Encoding, Connection, Upgrade, Proxy-Authorization, Proxy-Connection, Trailer, TE and Expect are transport-owned and must be omitted. |
| `body` | `string` | No | — | — | prepare: exact UTF-8 body, including empty string. Mutually exclusive with bodyBase64; max 1 MiB encoded. |
| `bodyBase64` | `string` | No | — | — | prepare: binary body as base64, max 1 MiB decoded. Do not send truncated or redacted captures; supply the complete intended body. |
| `timeoutMs` | `integer` | No | `8000` | 100–60000 | prepare: total send/read deadline in milliseconds. A timeout may occur after the server acted; never blindly create a new draft. If raised inside run_sequence, increase its outer step budget too. |
| `maxResponseBytes` | `integer` | No | `262144` | 1–1048576 | prepare: maximum returned response-body bytes. One extra byte detects truncation; no full-body hash/equality is claimed when truncated. |
| `compareTo` | `string` | No | — | — | prepare: completed replayId from this agent to compare response status, header names and complete body hash. Does not resend the baseline. |
| `adoptSessionFrom` | `object` | No | — | — | prepare: let Nova fill the session of an open tab into this request instead of copying it by hand. This is the answer to "why does my own client see different data than the browser?" - the page's own reads cannot show a field the server sends only to other clients. Reading these values is permission-gated exactly like cookie_list/storage_inspect with values (the user may be prompted) and is written to the site-data audit log. The request host must be the tab's host or a sub/parent domain of it; Nova does not copy a session to an unrelated host. Adopted headers are sent but withheld from the preview (see adoptedHeaderNames and adoptedSession provenance), and a header you set yourself is never overwritten silently. |
| `adoptSessionFrom.targetId` | `string` | Yes | — | — | Tab or sandbox ID whose session to adopt. Required. No claim is taken. |
| `adoptSessionFrom.cookies` | `boolean` | No | `true` | — | Send the tab's cookies that apply to this url as one Cookie header. If no cookie applies, no header is added and the provenance says so. |
| `adoptSessionFrom.headersFromStorage` | `object` | No | — | — | Header name -> storage key, e.g. {"Authorization":"auth_token"}. Nova cannot guess whether a token belongs in Authorization or X-Session-Id, so the mapping is explicit. A missing key fails the call instead of sending an empty header. Max 12 entries. Prefix the value with 'Bearer ' by setting the header yourself if the raw token is not the whole header value. |
| `adoptSessionFrom.storageType` | `string` | No | `"local"` | `local`, `session` | Which storage the keys come from. |

**`_meta.intent` is required for certain arguments.** Passing a short reason in `_meta.intent` is always safe; a rejected call names the argument that made it required.

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.network_replay",
  "arguments": {
    "action": "send",
    "replayId": "8f12a4b0c3d9e4f5a6b7c8d9e0f1a2b3",
    "_meta": {
      "intent": "Repeat GraphQL query with modified pagination variable"
    }
  }
}
```

### JSON-RPC Response
Both `content[0].text` and `structuredContent` carry the same serialized result object.
```json
{
  "content": [
    {
      "type": "text",
      "text": "{\"status\":\"response\",\"replayId\":\"8f12a4b0c3d9e4f5a6b7c8d9e0f1a2b3\",\"reused\":false,\"actionDispatched\":true,\"httpOk\":true,\"response\":{...},\"comparison\":null}"
    }
  ],
  "structuredContent": {
    "status": "response",
    "replayId": "8f12a4b0c3d9e4f5a6b7c8d9e0f1a2b3",
    "reused": false,
    "actionDispatched": true,
    "httpOk": true,
    "response": {
      "statusCode": 200,
      "headers": {
        "content-type": ["application/json; charset=utf-8"]
      },
      "bodyBase64": "eyJyZXN1bHRzIjogW119",
      "capturedBytes": 20,
      "truncated": false,
      "sha256": "2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae",
      "elapsedMs": 120,
      "outcome": "response",
      "mayHaveBeenSent": true
    },
    "comparison": null
  }
}
```
`status`/`response.outcome` is `"response"` on a completed send, not an HTTP status — the HTTP status lives at `response.statusCode`. Other outcomes are `"cancelled"` and `"transport_error"`. `comparison` is only populated when the prepared request carried `compareTo`.

---

## 4. Operational Best Practices

* **Two-Phase Execution:** Always call `prepare` first to freeze the request payload, verify headers, then dispatch with `send`.
* **Explicit Session:** `nova.network_replay` operates outside the browser tab's cookie jar. Send cookies explicitly in `headers`, or request permission-gated adoption during `prepare` with `adoptSessionFrom`. Without either choice, browser cookies are not attached automatically.
* **Idempotent Retries:** Re-sending an already executed `replayId` returns the cached outcome rather than sending duplicate requests.

---

## See Also

* [`nova.network_intercept_add`](nova-network-intercept-add.md) - Intercept in-page requests.
* [Proxy Routing Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
