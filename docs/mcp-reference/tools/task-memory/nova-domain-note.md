# `nova.domain_note`

Stores or updates a domain-scoped operational note automatically surfaced during navigation.

---

## 1. Overview

`nova.domain_note` registers persistent, site-specific instructions for a domain. Depending on the enforcement level, a note is either passive (surfaced on perceive only), shown as a warning on each tool call on that domain, or required to be acknowledged (`nova.domain_note_ack`) before further tool calls on that domain proceed.

* **Core Architecture Guide:** [Operational Knowledge](../../../core-features/learning/operational-knowledge-ok/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `domain` | `string` | Yes | — | — | The domain to attach this note to (e.g. 'vxlive.net', 'chat.openai.com'). |
| `key` | `string` | Yes | — | — | Short identifier for this note (alphanumeric, hyphens, underscores; e.g. 'auth', 'nav', 'i18n'). Max 50 chars. |
| `value` | `string` | Yes | — | — | The note content. Free-form text up to 100,000 chars — large enough for full system-prompt-style instructions when the note is set to MUST-read on a user-authored note. |
| `enforcement` | `string` | No | — | `none`, `warn`, `block`, `must_read`, `mustread` | Optional enforcement level. 'none' = passive perceive hint (default for new agent-authored notes), 'warn' = warning injected into structuredContent on each tool call on this domain, 'block' (alias 'must_read') = the agent gets a MUST-read acknowledge-block and must retry to proceed. Changing this on a user-authored note runs through the user-confirmation gate. |
| `repeatMinutes` | `integer or null` | No | — | ≥ 0 | Optional re-acknowledge interval in minutes for MUST-read notes. After this many minutes since the last acknowledge, the next tool call on this tab/domain triggers another acknowledge-block. 0 = never repeat (one-shot per tab). null/omitted = fall back to the global default in settings. |
| `repeatToolCalls` | `integer or null` | No | — | ≥ 0 | Optional re-acknowledge interval in tool calls on the domain. After this many calls since the last acknowledge, the next tool call triggers another acknowledge-block. 0 = never repeat. null/omitted = use the global default. |
| `sandboxId` | `string` | No | — | — | Optional sandbox letter-id (e.g. 'A', 'B') to bind this note to a specific sandbox. Omit for global note. Required together with sandboxRef. |
| `sandboxRef` | `string` | No | — | — | Opaque PersistentUid token from nova.tabs / nova.sandbox_context / perceive.targetContext. Mandatory when sandboxId is set; protects against letter-id recycling races. Mismatch with current sandbox UID → -32602 stale_sandbox_reference. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.domain_note",
  "arguments": {
    "domain": "internal.corp",
    "key": "auth_hint",
    "value": "Use SAML single sign-on button; avoid username/password form."
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Domain note created: internal.corp/auth_hint"
    }
  ],
  "structuredContent": {
    "action": "created",
    "domain": "internal.corp",
    "key": "auth_hint",
    "noteCount": 3,
    "sandboxRef": null,
    "scopeAdvisory": null
  }
}
```

`action` is `created` or `updated`. `noteCount` is the total number of stored notes after the write (not specific to this domain). `scopeAdvisory` is set only when a global note's text looks account- or identity-specific, hinting that it should probably be bound to a `sandboxId` instead.

---

## 4. Operational Best Practices

* **Must-Read Blocking:** Set `enforcement: "must_read"` (or its alias `block`) for critical instructions that require explicit acknowledgment (`nova.domain_note_ack`) before further tool calls on that domain proceed.

---

## 5. Related Tools

* [`nova.domain_notes_list`](nova-domain-notes-list.md)
* [`nova.domain_note_ack`](nova-domain-note-ack.md)
* [`nova.domain_note_delete`](nova-domain-note-delete.md)
