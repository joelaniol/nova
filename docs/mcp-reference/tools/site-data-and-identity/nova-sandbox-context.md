# `nova.sandbox_context`

Returns detailed identity, cookie jar bounds, and context metadata for a specific sandbox.

---

## 1. Overview

`nova.sandbox_context` returns profile metadata for a sandbox container: profile id, name, current/start URL, detected account, recognized service, user-declared purpose and routing hints (`aliases`, `preferredFor`), and last-active timestamp. `targetId` must name a sandbox (`kind=sandbox` in `nova.tabs`); passing a sandbox tab's target resolves to its owning sandbox, and passing an ordinary browser tab's target is rejected.

* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | Yes | — | — | Sandbox target ID from nova.tabs (e.g. 'A', 'B'). |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.sandbox_context",
  "arguments": {
    "targetId": "sb-work-01"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Sandbox context for 'sb-work-01'."
    }
  ],
  "structuredContent": {
    "targetId": "sb-work-01",
    "profileId": "sb-work-01",
    "sandboxId": null,
    "sandboxRef": "8f3a2c1d9e4b4a7fa6c1d2e3f4a5b6c7",
    "kind": "sandbox",
    "name": "Work",
    "isActive": true,
    "webViewReady": true,
    "currentUrl": "https://mail.google.com/mail/u/0/",
    "startUrl": "https://mail.google.com",
    "title": "Inbox - Gmail",
    "detectedAccountName": "jane@work.example",
    "serviceKey": "gmail",
    "serviceLabel": "Gmail",
    "purpose": "Corporate email",
    "accountLabel": "work",
    "homeOrigin": "mail.google.com",
    "aliases": ["email"],
    "preferredFor": ["email.compose"],
    "lastActiveAtUtc": "2026-10-03T12:00:00Z",
    "status": "ok"
  }
}
```

This response has no `ok` field; use `status` instead. Unknown `targetId`, and a target that is a browser tab rather than a sandbox, both return a JSON-RPC error with a `repairHint` pointing back to `nova.tabs`.

---

## 4. Operational Best Practices

* **Profile Verification:** Verify sandbox context before executing operations that require specific corporate credentials.

---

## 5. Related Tools

* [`nova.resolve_sandbox`](nova-resolve-sandbox.md)
* [`nova.sandbox_update`](nova-sandbox-update.md)
