# Guarded Actions & Blocker Clearance

High-impact interaction macros with pre-flight safety gates, auth surface verification, and cookie banner dismissals.

* **Capability Bundle(s):** `form_submission`
* **Core Architecture Guide:** [Core Features: aag.md](../../../core-features/aag.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (7 Tools)

| Tool | What it does |
| :--- | :--- |
| **[`nova.cmp_apply`](nova-cmp-apply.md)** | Applies a typed privacy consent policy directly through recognized Consent Management Platform (CMP) vendor JavaScript APIs (OneTrust, Sourcepoint, Cookiebot), verifying consent vector state before and after execution. |
| **[`nova.dismiss_blockers`](../browser-automation/nova-dismiss-blockers.md)** | Identifies and removes click-blocking overlays, cookie consent banners, notification prompts, and modal backdrops. |
| **[`nova.guarded_login`](nova-guarded-login.md)** | High-level guarded macro for login form submissions, featuring integrated Auth Surface Detection (ASD) that distinguishes between authentication rejections and multi-factor (2FA/MFA) follow-up states. |
| **[`nova.guarded_send_message`](nova-guarded-send-message.md)** | High-level guarded macro for chat interfaces (ChatGPT, Claude.ai, Gemini, Slack, Teams): auto-discovers the composer, types text with read-back verification, resolves the send button, clicks it, and verifies delivery in a single atomic operation. |
| **[`nova.guarded_submit_form`](nova-guarded-submit-form.md)** | High-level guarded macro for form submissions, wrapping click dispatch in an automated transition contract to verify validation rules, prevent duplicate submissions, and confirm post-submit transitions. |
| **[`nova.guarded_switch_model`](nova-guarded-switch-model.md)** | Safely switches the model in an AI web provider interface (ChatGPT, Claude, Gemini) with verification. |
| **[`nova.guarded_switch_sandbox`](nova-guarded-switch-sandbox.md)** | Switches the active sandbox container for a tab while verifying session state and cookies. |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
