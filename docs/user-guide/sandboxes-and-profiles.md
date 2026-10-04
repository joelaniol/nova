# Sandboxes & Profile Isolation

> [!NOTE]
> In Nova AI Workspace you do not need separate browser windows or profile switching to use several accounts. **Sandboxes** keep separate logins side by side in one window.

---

## 1. What Are Sandboxes?

Traditional browsers isolate accounts into separate profile windows, which makes side-by-side work and automated switching clumsy.

In Nova:
* **One window, several identities:** sandbox A can be logged into one account of a service while sandbox B is logged into a second account of the same service, and your normal tabs use a third session.
* **Separate browser profiles:** each sandbox has its own browser profile with its own cookies, sessions, site storage and cache. Proxy, fingerprint protection and vault autofill can be set per sandbox.
* **Normal tabs and private tabs** are separate from all sandboxes. Normal tabs share one common profile; a private tab (`Ctrl+Shift+N`) starts logged out and keeps nothing after it closes.

```mermaid
flowchart TD
    subgraph NovaWindow["Nova AI Workspace - one window"]
        PillA["Sandbox pill A - Work"]
        PillB["Sandbox pill B - Personal"]
        Tabs["Normal tabs"]
        Private["Private tab"]
    end

    subgraph Profiles["Separate browser profiles"]
        ProfA["Profile of sandbox A - cookies, storage, cache"]
        ProfB["Profile of sandbox B - cookies, storage, cache"]
        ProfTabs["Shared tab profile"]
        ProfPrivate["Private session - in memory only"]
    end

    PillA --> ProfA
    PillB --> ProfB
    Tabs --> ProfTabs
    Private --> ProfPrivate
```

---

## 2. Working with Sandboxes in the UI

### 2.1 Opening a Sandbox
* Each visible sandbox appears as a **pill** in the title bar next to the tabs. Click it to switch to that sandbox.
* With many sandboxes, **Find a sandbox** opens a searchable list (**Search sandboxes**, **Manage sandboxes...**).
* A sandbox without a remembered page shows **Sandbox needs a start page**, where you set its **Start URL**.

### 2.2 Creating and Managing Sandboxes
* Under **Settings → Sandboxes**, **+ Add sandbox** creates a new one (up to 100). Each sandbox has a **Name**, a colour and a **Start URL**, and can use its own **Proxy**, fingerprint protection and vault autofill setting.
* **Hide** removes a sandbox from the title bar without deleting its data; hidden sandboxes are listed under **Hidden sandboxes** and can be shown again.
* **Clear data...** clears the **Cache**, **Cookies and site data** or **History and last URL** of one sandbox, or **Reset entire sandbox**. **Delete...** removes the sandbox and all its data permanently.

### 2.3 The Pill Menu
Right-click a sandbox pill for:
* **Mark** — show nothing, a **Colour** or the **Site icon** in front of the name.
* **Proxy** — disconnect or reconnect the sandbox's proxy, or open **Proxy settings...**.
* **Allow tabs in this sandbox** — see below.
* **Hide from toolbar** and **Clear sandbox data...**.
* **Release agent** — releases an agent's claim on this sandbox (shown while an agent holds one).

### 2.4 Tabs Inside a Sandbox
A sandbox shows one page. When a page in it opens a link in a new tab or a popup, Nova opens a **sandbox tab** that keeps the sandbox's session, so a sign-in or payment flow does not lose its login. The tab carries a badge: *Tab of sandbox {name} — shares its session*. This is on by default and can be switched off per sandbox with **Allow tabs in this sandbox**.

### 2.5 Leaving the Sandbox
If a page in a sandbox tries to continue on a host that does not belong to the sandbox — often an age check, sign-in or payment step — Nova asks **This page wants to leave the sandbox** with **Allow for this step** or **Always in this sandbox**.

> [!NOTE]
> Site permissions (camera, microphone, notifications) currently apply to all sandboxes: granting access in one sandbox grants it everywhere.

---

## 3. Agent & MCP Interaction

AI agents work with sandboxes through MCP tools:
* `nova.tabs` lists sandboxes and tabs as targets; `nova.sandbox_context` describes one sandbox.
* `nova.sandbox_create`, `nova.sandbox_update` and `nova.sandbox_delete` manage sandboxes.
* `nova.tab_new` with the parameter `sandbox` (the sandbox's letter id, e.g. `A`) opens a tab that shares that sandbox's session; `private: true` opens a private tab instead.

More background: [Sandbox Isolation](../core-features/sandbox-isolation.md).
