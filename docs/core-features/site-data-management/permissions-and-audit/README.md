# Site Data Permissions & Audit

Before allowing an agent to read session values or clear data, check the target profile, requested operation and stated reason. Metadata inspection and revealing a cookie or token are different operations.

## Agent access controls

The **Agent cookie/storage access** setting offers **Always ask** (the default), **Ask once per session** and **Always allow**. The **Website data access** prompt offers **Allow once** and **Allow for session**. Existing grants can be revoked under **Active agent permissions**.

The target's actual browser profile determines the scope of profile-level operations and grants. A different tab can still share that profile; a sandbox has its own profile. Do not treat a tab ID as an isolation guarantee.

## Sensitive reads and destructive clears

| Operation | Relevant distinction |
|---|---|
| Cookie inspection | Metadata is the default; values require `includeValues=true` plus a `domainFilter` and are a high-impact secret read. |
| Web Storage inspection | Keys are the default; requesting values can expose tokens or application state and is treated as a sensitive read. |
| Cookie or cache clearing | Requires `_meta.intent` and goes through the site-data permission gate. Check domain versus profile scope before allowing it. |
| Replay session adoption | Uses the existing cookie/storage-value permission gate to populate a request draft for a checked destination. |

A tool's baseline category does not mean every combination of its parameters has the same impact. The current [tool reference](../../../mcp-reference/tools/site-data-and-identity/README.md) describes parameter-dependent intent requirements.

## What the audit records mean

Site-data changes are audited using value hashes rather than plaintext values. That protects the audit trail from becoming a copy of session secrets; it does not mean an authorized value read is hidden from the requesting agent.

[Request replay adoption](../../network/network-interception/README.md#adopt-a-browser-session-with-a-redacted-preview) provides redacted preview provenance, such as header names and the storage keys used. Adopted values are still sent to the destination when the separately prepared request is sent. Check that destination as well as the source profile.

## Separate permission systems

These controls govern agent access to browser site data. They are distinct from [website permissions](../../../user-guide/settings/site-permissions.md), the Cookie Inspector's visibility setting and approval rules in an external AI client. Clearing cookies does not revoke those other permissions.

[Site Data Management](../README.md)
