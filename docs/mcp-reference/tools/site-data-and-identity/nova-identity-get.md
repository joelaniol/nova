# `nova.identity_get`

Reads the active browser identity profile, spoofed User-Agent, and client hints.

---

## 1. Overview

`nova.identity_get` returns the current browser persona configuration: active preset (`default`, `chrome`, `firefox`, `safari`, or `custom`), version string, custom User-Agent (when set), and whether the spoofed identity's client hints (`Sec-CH-UA` etc.) are internally coherent. `identity_set` applies the chosen identity globally, not per tab or sandbox.

* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

Capability bundle: `identity_management` (load it with `nova.tools_bundle(bundle='identity_management')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.identity_get",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Browser identity: preset=chrome, version=150.0.4078.65, overrideActive=True, clientHintsCoherent=True"
    }
  ],
  "structuredContent": {
    "preset": "chrome",
    "version": "150.0.4078.65",
    "customUserAgent": null,
    "effectiveUserAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.4078.65 Safari/537.36",
    "overrideActive": true,
    "platform": "Win32",
    "clientHintsCoherent": true,
    "userAgentDataBrands": "Not/A)Brand 8, Chromium 150, Google Chrome 150"
  }
}
```

This response has no `ok` field. `clientHintsCoherent` is true for the native default and Chromium-based spoofs; it is false for `firefox`/`safari`, where the browser engine cannot express the absent non-Chromium client hints.

---

## 4. Operational Best Practices

* **Client Hint Coherence:** Check `clientHintsCoherent` before relying on a spoofed identity against a fingerprinting check — Firefox/Safari presets cannot fully hide the underlying Chromium engine's client hints.

---

## 5. Related Tools

* [`nova.identity_presets`](nova-identity-presets.md)
* [`nova.identity_set`](nova-identity-set.md)
