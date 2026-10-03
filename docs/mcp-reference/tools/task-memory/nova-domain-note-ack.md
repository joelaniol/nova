# `nova.domain_note_ack`

Explicitly acknowledges a MUST-read domain note block to unblock subsequent tool calls.

---

## 1. Overview

`nova.domain_note_ack` acknowledges a mandatory compliance or safety note encountered during navigation, satisfying the server-side safety gate.

* **Security Tier:** Tier 1 (Acknowledgment Gate)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `domain` | `string` | Yes | — | — | The domain of the note to acknowledge (must match the host of the active or specified tab). |
| `key` | `string` | Yes | — | — | The note key as shown in the MUST-read block message (the 'Title' field). |
| `targetId` | `string` | No | — | — | Optional tab targetId. Defaults to the active tab. Must point at a tab whose host matches `domain` for the acknowledge to apply where the gate fires. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.domain_note_ack",
  "arguments": {
    "domain": "internal.corp",
    "key": "auth_hint"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Acknowledged must-read note auth_hint for internal.corp."
    }
  ],
  "structuredContent": {
    "ok": true,
    "domain": "internal.corp",
    "key": "auth_hint",
    "acknowledged": true
  }
}
```

---

## 4. Operational Best Practices

* **Read-Before-Act:** Review the note content before calling `ack` to incorporate required constraints into your plan.

---

## 5. Related Tools

* [`nova.domain_note`](nova-domain-note.md)
* [`nova.domain_notes_list`](nova-domain-notes-list.md)
