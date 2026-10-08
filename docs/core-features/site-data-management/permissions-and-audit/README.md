# Site Data Permissions & Audit

Before allowing an agent to read session values or clear data, check the target profile, requested operation and stated reason. Metadata inspection and revealing a cookie or token are different operations.

## Agent access controls

The **Agent cookie/storage access** setting offers **Always ask** (the default), **Ask once per session** and **Always allow**. The **Website data access** prompt offers **Allow once** and **Allow for session**. Existing grants can be revoked under **Active agent permissions**.

The target's actual browser profile determines the scope of profile-level operations and grants. A different tab can still share that profile; a sandbox has its own profile. Do not treat a tab ID as an isolation guarantee.

## What a session grant covers

A grant is scoped to the agent, browser profile, action group and, where specified, domain. Reading values, writing an entry, deleting one entry and clearing a category are separate action groups: permission to read a token is not permission to delete its cookie.

A domain-specific grant does not cover every domain in the profile. A grant without a domain is broader and covers that profile/action scope. Tabs sharing a profile can share the effect of a grant; another sandbox has a different profile.

* **Allow once** permits the current request without creating a session grant.
* **Allow for session** records a grant for that scope. The global policy can independently allow later requests.
* Metadata-only cookie and storage inspection is allowed by this site-data gate without a value-read prompt. Other tool requirements can still apply.
* An explicit denial blocks subsequent protected requests in the same scope until that session state is reset. Switching the global policy to **Always allow** does not override a recorded session denial.
* Closing, cancelling or timing out a prompt does not grant access and is not stored as an explicit session denial.

## Revoke a grant

Under **Active agent permissions**, find the entry for the intended agent, profile, action and domain. Choose **Revoke** and confirm the dialog. Revocation removes that stored grant; it does not undo a completed read, change or deletion.

To require approval again, also check the global policy: **Always allow** can authorize later requests even after an individual grant is revoked. Session grants are not permanent website permissions.

## Sensitive reads and destructive clears

| Operation | Relevant distinction |
|---|---|
| Cookie inspection | Metadata is the default; values require `includeValues=true` plus a `domainFilter` and are a high-impact secret read. |
| Web Storage inspection | Keys are the default; requesting values can expose tokens or application state and is treated as a sensitive read. |
| Cookie or cache clearing | Requires `_meta.intent` and goes through the site-data permission gate. Check domain versus profile scope before allowing it. |
| Replay session adoption | Uses the existing cookie/storage-value permission gate to populate a request draft for a checked destination. |

A tool's baseline category does not mean every combination of its parameters has the same impact. The current [tool reference](../../../mcp-reference/tools/site-data-and-identity/README.md) describes parameter-dependent intent requirements.

## What the audit records mean

The current site-data log records the operation and tool, agent, target, profile, origin, affected cookie or storage key, whether a value changed, the result and the user-decision field. It does not log the raw cookie or storage values.

Although the operation paths can calculate value hashes, those hashes are not included in the current emitted site-data log entry. The log therefore does not provide a before/after value-hash comparison or a backup from which deleted data can be recovered. An authorized value read can still disclose the requested value to the agent; the audit log and the tool response are separate outputs.

[Request replay adoption](../../network/network-interception/README.md#adopt-a-browser-session-with-a-redacted-preview) provides redacted preview provenance, such as header names and the storage keys used. Adopted values are still sent to the destination when the separately prepared request is sent. Check that destination as well as the source profile.

## Separate permission systems

These controls govern agent access to browser site data. They are distinct from [website permissions](../../../user-guide/settings/site-permissions.md), the Cookie Inspector's visibility setting and approval rules in an external AI client. Clearing cookies does not revoke those other permissions.

[Site Data Management](../README.md)
