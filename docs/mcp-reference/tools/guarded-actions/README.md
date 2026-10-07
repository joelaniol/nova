# Guarded Actions & Blocker Clearance

High-impact interaction macros with pre-flight safety gates, auth surface verification, and cookie banner dismissals.

* **Core Architecture Guide:** [Core Features: aag.md](../../../core-features/agent-awareness-gates-aag/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

<!-- generated:tool-list (from the tool pages in this folder; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
## Tool Inventory (6 Tools)

Capability bundles of these tools: `browser_automation`, `form_submission`, `system_tools`, `vault_auth`.

| Tool | What it does |
| :--- | :--- |
| **[`nova.cmp_apply`](nova-cmp-apply.md)** | Applies a typed privacy consent policy directly through recognized Consent Management Platform (CMP) vendor JavaScript APIs (OneTrust, Sourcepoint, Cookiebot), verifying consent vector state before and after execution. |
| **[`nova.guarded_login`](nova-guarded-login.md)** | High-level guarded macro for login form submissions, featuring integrated Auth Surface Detection (ASD) that distinguishes between authentication rejections and multi-factor (2FA/MFA) follow-up states. |
| **[`nova.guarded_send_message`](nova-guarded-send-message.md)** | High-level guarded macro for chat interfaces (ChatGPT, Claude.ai, Gemini, Slack, Teams): auto-discovers the composer, types text with read-back verification, resolves the send button, clicks it, and verifies delivery in a single atomic operation. |
| **[`nova.guarded_submit_form`](nova-guarded-submit-form.md)** | High-level guarded macro for form submissions, wrapping click dispatch in an automated transition contract to verify validation rules, prevent duplicate submissions, and confirm post-submit transitions. |
| **[`nova.guarded_switch_model`](nova-guarded-switch-model.md)** | Clicks a model entry in a web app's model menu and verifies that the selected model changed. |
| **[`nova.guarded_switch_sandbox`](nova-guarded-switch-sandbox.md)** | Clicks a workspace switcher entry in a web app and verifies that the workspace changed. |
<!-- /generated:tool-list -->

---

## Related Documentation

* [`nova.dismiss_blockers`](../browser-automation/nova-dismiss-blockers.md) — clears overlays and cookie banners; listed under browser automation
* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
