# `nova.emulation_set_user_agent`

Overrides the HTTP User-Agent header, navigator.userAgent, and client hints for a tab.

---

## 1. Overview

`nova.emulation_set_user_agent` overrides browser identity for a specific tab via CDP. For Chromium user agents, it automatically populates `navigator.userAgentData` and `Sec-CH-UA` headers to pass sophisticated bot detection checks.

* **Capability Bundle:** `device_emulation`
* **Security Tier:** Tier 2 (Identity Emulation)
* **Core Architecture Guide:** [Fingerprint & Identity Systems](../../../core-features/fingerprint-and-identity.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`userAgent`** | `string` | Yes | `none` | Full user agent string to report. |
| **`platform`** | `string` | No | `derived` | `navigator.platform` override (e.g. `"Win32"`, `"iPhone"`, `"MacIntel"`). |
| **`acceptLanguage`** | `string` | No | `null` | `Accept-Language` header value (e.g. `"en-US,en;q=0.9"`). |
| **`targetId`** | `string` | No | `"active"` | Target tab ID. |
| **`agentId`** | `string` | No | `"default"` | Optional agent identifier. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

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
      "text": "User-agent override applied (platform=iPhone, clientHints=False)."
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "platform": "iPhone",
    "clientHintsApplied": false
  }
}
```

---

## 4. Operational Best Practices

* **Session-Scoped:** Stays active on the target tab until closed or overwritten; `clear_device_metrics` does not clear user agent.

---

## See Also

* [`nova.emulation_use_device`](nova-emulation-use-device.md) - Preset with device UA.
* [Device Emulation Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
