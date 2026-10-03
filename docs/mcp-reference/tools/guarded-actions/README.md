# Guarded Actions & Blocker Clearance

High-impact interaction macros with pre-flight safety gates, auth surface verification, and cookie banner dismissals.

* **Capability Bundle(s):** `form_submission`
* **Core Architecture Guide:** [Core Features: aag.md](../../../core-features/aag.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (7 Tools)

| Tool Name | Status | Description |
| :--- | :---: | :--- |
| **[`nova.cmp_apply`](nova-cmp-apply.md)** | Documented | Apply a typed consent intent against a recognized CMP vendor. |
| **[`nova.dismiss_blockers`](../browser-automation/nova-dismiss-blockers.md)** | Documented | Close/accept blocking modals, consent dialogs, overlays and ad blockers. |
| **[`nova.guarded_login`](nova-guarded-login.md)** | Documented | High-level guarded macro for login submit actions. |
| **[`nova.guarded_send_message`](nova-guarded-send-message.md)** | Documented | High-level guarded macro for sending a message. |
| **[`nova.guarded_submit_form`](nova-guarded-submit-form.md)** | Documented | High-level guarded macro for form submit actions. |
| **[`nova.guarded_switch_model`](nova-guarded-switch-model.md)** | Documented | High-level guarded macro for model switching actions. |
| **[`nova.guarded_switch_sandbox`](nova-guarded-switch-sandbox.md)** | Documented | High-level guarded macro for sandbox/workspace switch actions. |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
