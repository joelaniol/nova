# Programmatic CMP Vendor API Engine

> [!NOTE]
> The Consent Management Platform (CMP) Engine powers [`nova.cmp_apply`](../../../mcp-reference/tools/guarded-actions/nova-cmp-apply.md). Rather than attempting to click buttons through arbitrary DOM selectors, the engine interfaces directly with the runtime JavaScript APIs of recognized enterprise consent providers (OneTrust, Sourcepoint / TCF v2, and Cookiebot). It enforces a strict 8-step execution pipeline, verifies ground truth through cryptographic state vectors, and prevents unauthorized consent escalation via autonomous safety gates.

---

## 1. Executive Summary & Core Mission

Enterprise websites deploy standardized Consent Management Platforms to comply with GDPR, ePrivacy, and CCPA regulations. These platforms maintain complex client-side state machines, register cryptographic consent strings, and gate analytics scripts behind legal status tokens.

Naive visual button-clicking frequently fails against these systems because DOM mutations do not guarantee internal state transitions, and dark patterns frequently mislead text-matching algorithms.

The Nova CMP Engine provides:
1. **Direct Runtime API Dispatch:** Direct invocation of vendor methods (`window.OneTrust.RejectAll()`, `__tcfapi('postRejectAll', 2, ...)`, `window.Cookiebot.submitCustomConsent()`).
2. **Deterministic 8-Step Pipeline:** Strict sequencing from settings evaluation and ordered adapter detection to settle debouncing and Serilog auditing.
3. **Cryptographic State Verification:** Capture and comparison of typed `ConsentStateVector` snapshots with anti-spoofing provenance validation.
4. **Autonomous Safety Gate:** Unconditional rejection of commercial tracking acceptance (`AcceptAll` error `-32035`).

---

## 2. Comprehensive Documentation Index

The CMP Engine architecture is detailed across specialized subguides:

| Architecture Guide | Focus Areas & Key Invariants | Primary Components |
| :--- | :--- | :--- |
| **[Execution Pipeline & Vendor Adapters](execution-pipeline-and-adapters/README.md)** | The 8-stage execution pipeline, ordered adapter detection priority (Sourcepoint $\rightarrow$ Cookiebot $\rightarrow$ OneTrust), runtime protocols, cryptographic TC string hashing, and event bus listener guards. | `McpCmpApplyHandler`<br>`CmpAdapterRegistry`<br>`SourcepointAdapter`<br>`CookiebotAdapter`<br>`OneTrustAdapter` |
| **[Consent State & Safety Gates](consent-state-and-safety-gates/README.md)** | Ground-truth verification via `ConsentStateVector`, anti-spoofing data provenance (`OneTrust.GetDomainData().Groups`), strongly-typed `ConsentIntent`, autonomous `AcceptAll` barrier (-32035), user choice preservation, and visual hidden probing. | `ConsentStateVector`<br>`ConsentIntent`<br>`OneTrustGroupsFromDomainData`<br>`CmpHideList`<br>`bannerVisuallyHidden` |

---

## 3. High-Level Engine Architecture

```mermaid
flowchart TD
    Agent["Autonomous Agent"] --> Invocation["nova.cmp_apply(targetId, intent, mode)"]

    subgraph CMPEngine["Nova CMP Vendor API Engine"]
        Invocation --> Stage1["1. Settings Gate (CmpVendorAdapterEnabled)"]
        Stage1 --> Stage2["2. Ordered Adapter Detection"]
        
        subgraph Registry["Ordered Adapter Detection Sequence"]
            Stage2 --> Det1{"1. Sourcepoint (TCF cmpId == 6)"}
            Det1 -- "No" --> Det2{"2. Cookiebot (submitCustomConsent)"}
            Det2 -- "No" --> Det3{"3. OneTrust (window.OneTrust)"}
            Det3 -- "No" --> DetFail["failureCode: 'no_adapter'\nnextAction: 'fallback_dismiss_blockers'"]
        end

        Det1 -- "Yes" --> SelectedAdapter["Active Vendor Adapter Selected"]
        Det2 -- "Yes" --> SelectedAdapter
        Det3 -- "Yes" --> SelectedAdapter

        SelectedAdapter --> Stage3["3. Semantic Preflight Validation"]
        Stage3 --> Stage4["4. Pre-State Capture (ConsentStateVector)"]
        
        Stage4 --> Stage5{"5. mode == 'dry_run'?"}
        Stage5 -- "Yes" --> ReturnDry["Return ok: true, preState (No Mutation)"]
        
        Stage5 -- "No" --> Stage6{"6. intent.mode == 'AcceptAll'?"}
        Stage6 -- "Yes" --> BlockAccept["Halt with JSON-RPC -32035\n(accept_all_blocked)"]
        
        Stage6 -- "No" --> Stage7["7. Mutation Dispatch & Settle (50ms)"]
        Stage7 --> PostRead["Capture Post-State ConsentStateVector"]
        PostRead --> VerifyDiff["Verify State Mutation vs Intent"]
        VerifyDiff --> CheckHidden["Probe bannerVisuallyHidden"]
        CheckHidden --> Stage8["8. Structured Serilog Audit Logging"]
    end

    Stage8 --> FinalResult["Return Structured Result\n(ok, verified, preState, postState, bannerVisuallyHidden)"]
```

---

## 4. Key Architectural Invariants

* **Identity Gate Ordering:** The detection sequence must always prioritize cryptographic/registry gates (`Sourcepoint` cmpId=6) before general API objects (`Cookiebot`) and broad DOM markers (`OneTrust`). Unordered detection is strictly prohibited to prevent shadowing.
* **Anti-Spoofing Provenance:** Post-apply state verification for OneTrust strictly rejects global properties like `OptanonActiveGroups` and requires validation through internal engine models (`OneTrust.GetDomainData().Groups`).
* **Autonomous Tracking Protection:** Autonomous agents are barred from executing `AcceptAll`. Any attempt to accept commercial tracking without human operator authorization terminates immediately with error `-32035`.
* **State vs. Visibility Decoupling:** Verification measures underlying engine data. The companion probe `bannerVisuallyHidden` indicates whether visual backdrop cleanup is required via [`nova.dismiss_blockers`](../../../mcp-reference/tools/guarded-actions/nova-dismiss-blockers.md).

---

## Related Documentation

* [Execution Pipeline & Vendor Adapters Subguide](execution-pipeline-and-adapters/README.md)
* [Consent State & Safety Gates Subguide](consent-state-and-safety-gates/README.md)
* [Parent: Consent Management Architecture Overview](../README.md)
* [3-Stage Hijack & Dark Pattern Defense](../hijack-protection/README.md)
* [Blocker & Overlay Remediation](../blocker-dismissal/README.md)
* [Tool Reference: `nova.cmp_apply`](../../../mcp-reference/tools/guarded-actions/nova-cmp-apply.md)
