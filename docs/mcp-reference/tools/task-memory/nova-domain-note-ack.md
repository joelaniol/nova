# `nova.domain_note_ack`

Explicitly acknowledges a MUST-read domain note block to unblock subsequent tool calls.

---

## 1. Overview

`nova.domain_note_ack` acknowledges a mandatory compliance or safety note encountered during navigation, satisfying the server-side safety gate.

* **Capability Bundle:** `task_memory`
* **Security Tier:** Tier 1 (Acknowledgment Gate)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`domain`** | `string` | Yes | `null` | The domain of the note to acknowledge (must match the host of the active or specified tab). |
| **`key`** | `string` | Yes | `null` | The note key as shown in the MUST-read block message (the 'Title' field). |
| **`targetId`** | `string` | No | `null` | Optional tab targetId. Defaults to the active tab. Must point at a tab whose host matches `domain` for the acknowledge to apply where the gate fires. |

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
