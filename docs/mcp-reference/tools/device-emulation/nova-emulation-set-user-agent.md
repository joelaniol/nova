# `nova.emulation_set_user_agent`

Overrides the HTTP User-Agent header, navigator.userAgent, and client hints for a tab.

---

## 1. Overview

`nova.emulation_set_user_agent` overrides browser identity for a specific tab via CDP. For Chromium user agents, it automatically populates `navigator.userAgentData` and `Sec-CH-UA` headers to pass sophisticated bot detection checks.

Additionally, passing `identifyAsAgent=true` enables transparent agent identification by appending `Agent/NovaAIWorkspace` to the browser's own user-agent string on user-whitelisted domains (`agentIdentificationSites`). While identified, `nova.input_drag_humanized` is rejected to prevent artificial humanization, and `sharedSessionTabs` identifies other open tabs of the same origin whose service worker requests carry the identity token.

* **Core Architecture Guide:** [Fingerprint & Identity Systems](../../../core-features/privacy/fingerprint-and-identity/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `userAgent` | `string` | No | — | — | Full user agent string, e.g. 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1'. |
| `acceptLanguage` | `string` | No | — | — | Accept-Language header value, e.g. 'en-US,en;q=0.9' or 'de-DE'. |
| `platform` | `string` | No | — | — | Navigator.platform override, e.g. 'iPhone', 'Linux x86_64', 'Win32', 'MacIntel'. |
| `identifyAsAgent` | `boolean` | No | — | — | Instead of userAgent: true marks this tab as an agent on a site the user listed (adds 'Agent/NovaAIWorkspace' to the browser's own user agent); false removes it. Refused off the list and on a tab that emulates another identity. |

Capability bundle: `device_emulation` (load it with `nova.tools_bundle(bundle='device_emulation')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.emulation_set_user_agent",
  "arguments": {
    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "platform": "iPhone"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "User agent override set."
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "acceptLanguage": null,
    "platform": "iPhone",
    "clientHintsApplied": false
  }
}
```

---

## 4. Operational Best Practices

* **Session-Scoped:** Stays active on the target tab until closed or overwritten; `clear_device_metrics` does not clear user agent.
* **Agent Transparency Mode (`identifyAsAgent`):** Restricted to operator-approved domains in `agentIdentificationSites`. Clears automatically upon navigation to non-whitelisted sites. Inspect `sharedSessionTabs` in the response to evaluate whether background service workers could affect concurrent sessions.

---

## Related Tools

* [`nova.emulation_use_device`](nova-emulation-use-device.md) - Preset with device UA.
* [Device Emulation Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
