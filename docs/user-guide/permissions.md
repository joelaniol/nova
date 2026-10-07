# Website & Agent Permissions

A camera request from a website and an approval request from an AI program control different things. Check who is asking and what access the answer grants.

## Website access

Open the **site info** button beside the address bar to inspect the current site's permissions. **Settings → Site permissions** brings together defaults, remembered site choices and media activity.

This area covers camera, microphone, speaker selection, screen capture, location, clipboard reading and supported hardware requests. Notifications have their own controls, including site choices and do-not-disturb settings. Speaker selection controls audio output routing; it is different from microphone capture.

For supported prompts:

- **Allow once** gives temporary access for the request.
- **Always allow** remembers permission for the site.
- **Block** refuses access.

Use the site controls to change a site's decision, or remove its saved override in settings so the default applies again. A site still needs to request access; a saved permission does not itself start recording.

Sandbox login isolation is separate from permission policy. Do not assume that creating another sandbox gives it an independent set of remembered website permissions. Private browsing can use temporary decisions; it does not make device requests harmless.

## Agent access in Nova

Open **Settings → AI & agents → Access & rules** to review **Access permissions** and **Autonomy level**. Browser access determines whether agents may control Nova.

- **Fully automatic** is intended for independent work within the task and applicable permissions.
- **Semi-automatic** is intended to ask for clicks and input.
- **Supervised** adds approval requests for actions without their own confirmation policy.

The autonomy level does not override every permission decision. Tools with their own confirmation policy use that policy; standing and session grants can also affect prompts. Review those policies under **AI & agents → Confirmations & audit** when available. Do not interpret Supervised as a guarantee of a separate prompt for every tool call. Your AI program may additionally ask for its own approvals.

Site-data access and active site-data grants are also available under **Site permissions**. They concern agent access to website data, separately from a website using your camera or microphone.

For a live interruption, use **Menu → Emergency stop**. It remains active until released and also interrupts Nova terminal sessions, including your own. For a single tab, see [Staying in control](live-assist-and-spectator.md#3-staying-in-control).

## Approvals inside your AI program

Claude, Codex and other clients can ask for their own tool approvals. Those decisions belong to the client. Connecting Nova or installing Nova's onboarding notes does not write a permission allowlist into your client.

If you are connected but approvals or behavior are confusing, use [Agent behavior troubleshooting](../troubleshooting/agent-behavior.md).
