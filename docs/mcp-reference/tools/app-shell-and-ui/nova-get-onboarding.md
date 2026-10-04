# `nova.get_onboarding`

> **Returns a manual edit plan — reference file contents and marker-block edits — for onboarding an agent to Nova's MCP tools, as an alternative to the one-call `nova.install_onboarding`.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.get_onboarding` returns Nova's MCP reference content (a quickstart and a full reference, plus connector capability references) together with the exact marker-block edits an agent would need to apply itself to its project's agent-config files (for example `CLAUDE.md`/`AGENTS.md`). It is the write-it-yourself fallback; `nova.install_onboarding` does the same job in one call by writing the files directly. This tool is only available when agent self-onboarding is enabled in settings.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

Capability bundles: `onboarding`, `system_tools`.
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_get_onboarding",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Nova MCP onboarding reference (version 4.39.0)"
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "version": "4.39.0",
    "files": [
      { "path": ".nova/nova-mcp.quick.md", "content": "...", "sha256": "..." },
      { "path": ".nova/nova-mcp.md", "content": "...", "sha256": "..." }
    ],
    "edits": [
      {
        "path": "CLAUDE.md",
        "mode": "append_or_replace_between_markers",
        "startMarker": "<!-- NOVA-BROWSER-MCP-START",
        "startMarkerMatch": "line_prefix",
        "endMarker": "<!-- NOVA-BROWSER-MCP-END -->",
        "createIfMissing": true,
        "createIfMissingNote": "..."
      }
    ],
    "bootstrapNow": {
      "steps": [
        "nova.get_instructions(taskKeywords=[...])",
        "nova.tools_bundle(bundle='browser_automation', includeUnavailable=true)"
      ],
      "note": "Run capability discovery now. Then call task tools directly; target selection, explicit claims, and perception are task-driven."
    },
    "preserveOtherContent": true,
    "verify": [
      "Re-open each edited file and confirm the block exists exactly once.",
      "Do not modify any content outside the marker block.",
      "If CLAUDE.md already imports AGENTS.md, skip the AGENTS.md edit."
    ],
    "bundles": ["browser_automation", "page_read_debug", "..."],
    "preferredAlternative": {
      "tool": "nova.install_onboarding",
      "reason": "One call — Nova writes all reference files and marker blocks for you. Use get_onboarding only when you must write the files yourself."
    }
  }
}
```

This example shortens `files`/`edits`/`bundles`; the real response includes every reference file (quickstart, full reference, and the mail/SFTP/FTP connector capability references) and every marker-block edit, plus the full bundle id list.

---

## 4. Operational Best Practices

* **Manual Setup Fallback:** Use when you need to write the reference files and marker blocks yourself instead of letting `nova.install_onboarding` write them directly.

---

## 5. Related Tools

* [`nova.install_onboarding`](nova-install-onboarding.md)
* [`nova.setup_status`](nova-setup-status.md)
