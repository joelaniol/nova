# Auth Surface Detection (ASD) & Surface Safety

> [!NOTE]
> **Auth Surface Detection (ASD)** assesses authentication states, session persistence, and interaction risks using heuristic page probing, three-valued truth logic, host-level cookie inspection, and embedded multi-lingual safety lexicons. It determines whether a browser surface presents an interactive login wall, an active authenticated session, a multi-factor authentication (MFA) challenge, or an identity error. Operating alongside the **Surface Safety Lexicon Shield**, Nova actively prevents autonomous agents, background crawlers, and surface explorers from accidentally triggering destructive account mutations, financial checkouts, or unintended session logouts.

---

## 1. Executive Summary & The Problem of Blind Automation

Browser automation frequently collapses when encountering modern authentication workflows. Traditional automation frameworks make three catastrophic assumptions:

1. **Boolean Coercion:** An automated script asks: *"Is the user logged in?"* If the page presents an intermediate MFA challenge, an email-first identifier step, or an ambiguous session rehydration state, a naive boolean check returns `false`. The automation engine then falls back to re-submitting saved login credentials—triggering account lockouts, rate limits, or security alarms.
2. **Selector Fragility:** Scripts relying on fixed DOM selectors (`#login-button`, `.sign-in`) fail immediately upon minor frontend redesigns, A/B testing variations, single sign-on (SSO) redirects, or shadow DOM encapsulation.
3. **Exploratory Destruction:** When autonomous agents or web crawlers explore an application interface, they indiscriminately interact with buttons and links. Without contextual safety boundaries, automated crawlers routinely click `Logout`, `Sign Out`, `Abmelden`, `Delete Account`, or `Cancel Subscription`, instantly terminating valid sessions or destroying customer data.
4. **DOM-Blindness to `HttpOnly` State:** Standard JavaScript in-page probing cannot read cookies flagged with the W3C `HttpOnly` directive. Purely script-based checkers mistakenly classify high-security cookie-backed sessions as unauthenticated or ephemeral.

Nova solves these challenges through deeply coordinated architectural subsystems:
* **Auth Surface Detection (ASD):** A top-document heuristic probing system that fuses DOM structures, accessibility attributes, client-side storage keys, framework state stores, and **native host-level `HttpOnly` cookie inspection**, resolving signals into strict **three-valued truth logic** (`Yes`, `No`, `Unknown`).
* **The Surface Safety Lexicon Shield:** A multi-layered safety pipeline backed by multi-lingual embedded JSON lexicons that classifies interactive triggers and enforces **hard-denials** on high-risk identity and destructive actions (e.g. logouts, profile impersonations, account purges, financial transactions).
* **Guarded Login & Closed-Loop Contracts:** Deterministic submission verification ensuring that non-idempotent login attempts are never blindly repeated upon ambiguous responses.
* **Target-Bound Crawl Gating & SSRF Protection:** Pre-flight crawl validation preventing detached crawlers from bypassing session requirements or probing private network infrastructure.

```mermaid
flowchart TD
    Page["Active Web Page / DOM Surface"] --> Probe["ASD Multi-Signal Probe"]
    Host["Host-Level Browser Engine"] -->|Inspect HttpOnly Cookie Jar| Probe
    Probe --> Detectors["Signal Detectors (Inputs, Storage, Account, Overlays)"]
    Detectors --> Confidence["Confidence Scoring & Threshold Engine"]
    Confidence --> TriState["Tri-State Verdicts (auth.loggedIn, auth.loginWallVisible, auth.stage)"]

    Page --> Explorer["Autonomous Agent / Crawler Interaction"]
    Explorer --> SafetyPipe["Surface Safety Pipeline"]
    SafetyPipe --> Lexicons["Multi-Lingual Safety Lexicons (high-risk-identity, dangerous, automation)"]
    Lexicons --> HardDeny{"Hard Deny or Operator Veto?"}
    HardDeny -->|High-Risk / Logout / Destruction| Deny["VETO / DENY (Protect Session & Data)"]
    HardDeny -->|Safe Read-Only / Navigation| Allow["ALLOW Action Execution"]
```

---

## 2. The Tri-State Logic Paradigm (`Yes`, `No`, `Unknown`)

In security-critical browser automation, **absence of positive evidence is not evidence of absence**. 

If Nova cannot definitively verify whether a user is logged in, answering `No` would cause an agent to assume the session is terminated and execute re-login procedures. Conversely, answering `Yes` might cause an agent to attempt privileged actions against an unauthenticated public redirect.

ASD mandates **Three-Valued Logic (`AuthTriState`)**:

| Tri-State Value | Wire Representation | Operational Meaning | System Behavior |
| :--- | :--- | :--- | :--- |
| **`Yes`** | `true` | Observed signals firmly exceed the positive confidence threshold ($\ge 0.50$). | Preconditions requiring the state succeed; guarded transitions proceed. |
| **`No`** | `false` | Observed signals firmly fall below the negative confidence threshold ($< 0.20$). | Preconditions requiring the state fail cleanly without ambiguous retry loops. |
| **`Unknown`** | `null` | Evidence is ambiguous, contradictory, or between thresholds ($[0.20, 0.50)$). | **Never coerced to false.** Guarded actions requiring `true` or `false` halt and request clarification. |

### Core Invariants of the Tri-State Model
* **No Silent Defaulting:** If an in-page script fails, if the DOM is unreadable, or if conflicting indicators appear simultaneously (e.g., a visible password field on an account management page that also features a logout button), ASD returns `Unknown` (`null`).
* **Fail-Closed Architecture:** Security gates and guarded tools treat `Unknown` as non-passing for assertions requiring explicit affirmative verification.
* **Dual-Fact Reflection:** Facts are mapped to both simple scalar booleans (`auth.loggedIn`) and full diagnostic objects (`auth.assessment`) on the Tool Observation Bus (TOB).

---

## 3. Multi-Signal Probing & Heuristic Detection Architecture

ASD evaluates pages through a sandboxed, top-document probe paired with native host-level inspection. Gathered signals feed into dedicated detector modules without introducing external network dependencies.

```mermaid
flowchart LR
    subgraph ProbingLayer [Dual-Layer Signal Collection]
        DOM["In-Page JavaScript Probe (DOM, Autocomplete, Storage, Globals)"]
        HostJar["Native Host Inspection (HttpOnly Cookies & Headers)"]
    end

    subgraph Detectors [Detector Modules]
        D1["PasswordFieldDetector"]
        D2["AutocompleteDetector"]
        D3["AccountSurfaceDetector"]
        D4["IdentityOverlayDetector"]
    end

    DOM --> D1 & D2 & D3 & D4
    HostJar --> D3
```

### 3.1 DOM Input & Autocomplete Analysis
The probe inspects visible `<input>` and `<textarea>` elements across top-level documents and accessible DOM scopes:
* **Password Fields:** Counts visible fields with `type="password"`. A single password field indicates a login surface; multiple password fields indicate registration or password change workflows.
* **W3C Autocomplete Semantics:** Reads standard autocomplete tokens:
  * `autocomplete="current-password"`: Strongly weights toward an explicit login surface.
  * `autocomplete="new-password"`: Indicates account creation, onboarding, or password reset; suppresses login-wall scoring.
  * `autocomplete="one-time-code"`: Signals a Multi-Factor Authentication (MFA) challenge or SMS/TOTP step.
  * `autocomplete="username"` / `autocomplete="email"`: Identifies credential identifier fields.
* **Identifier Fields:** Evaluates visible inputs by attributes (`name`, `id`, `placeholder`, `aria-label`, `data-testid`) containing tokens like `email`, `username`, `login`, `user-id`, or `identifier`.

### 3.2 Form Linkage & Multi-Lingual Action Dictionaries
Auth surfaces vary across internationalized applications. ASD embeds multi-lingual keyword dictionaries to recognize action anchors, submission buttons, and headings across English, German, French, and Spanish:

* **Auth Action URLs (`authHrefKeywords`):** Detects navigation links pointing to `/login`, `/signin`, `/sign-in`, `/auth`, `/oauth`, `/sso`, `/account/login`, `/session`, `/connexion`, `/connect`, `/acceso`, `/entrar`, `/iniciar-sesion`, `/registro`.
* **Action Button Text (`authTextKeywords` & `submitKeywords`):** Identifies textual triggers matching:
  * English: `log in`, `login`, `sign in`, `signin`, `continue with`, `submit`, `next`.
  * German: `anmelden`, `einloggen`, `weiter`, `fortfahren`, `anmelden mit`.
  * French: `se connecter`, `connexion`, `continuer`, `suivant`, `continuer avec`.
  * Spanish: `iniciar sesion`, `acceder`, `entrar`, `continuar`, `siguiente`, `continuar con`.
* **Federated Identity Providers (`providerKeywords`):** Recognizes branded SSO buttons for `Google`, `Microsoft`, `GitHub`, `Apple`, `Okta`, and `Auth0`.
* **Auth Headings (`authHeadingKeywords`):** Inspects `<h1>`–`<h3>`, `<legend>`, and `[role="heading"]` for phrases announcing login or account access.

### 3.3 Account Controls & Authenticated Surface Detection
To determine if a page represents an already authenticated session, ASD searches for controls that only appear when logged in:
* **Logout Links (`logoutSels`):** Inspects anchors and buttons matching `a[href*="logout"]`, `a[href*="abmelden"]`, `a[href*="signout"]`, `a[href*="sign-out"]`, `button[data-testid*="logout"]`.
* **Profile & Settings Anchors:** Evaluates links matching `/profile`, `/account`, `/user`, `/settings`, `/preferences`, and corresponding localized ARIA labels (`Profil`, `Einstellungen`, `Konto`).
* **User Avatars:** Identifies user profile icons or images located inside `<header>`, `<nav>`, `[role="banner"]`, or `[role="navigation"]`. Checks image `src`, `alt`, and `class` attributes, as well as `<svg>` icons with user-related ARIA labels (`avatar`, `user`, `profile`).

### 3.4 Host-Level `HttpOnly` Cookie Inspection
In standard browser automation, client-side JavaScript (`document.cookie`) cannot read cookies marked with the `HttpOnly` directive. As a result, standard headless scripts fail to see secure session cookies, falsely concluding that no session exists.

Nova bridges this gap at the host level:
* When the in-page JavaScript probe reports `HasAnyCookie == false` on the main frame, Nova's fact provider initiates a host-level asynchronous cookie probe against the browser runtime's native cookie store.
* If active session cookies exist in the native store for the target origin, the probe result is enriched with `HasAnyCookie = true`.
* This ensures high-security corporate sites and enterprise applications using `HttpOnly` session tokens are correctly recognized as authenticated rather than mistaken for ephemeral or logged-out pages.

### 3.5 Storage & Runtime State Inspection
Authentication often resides in client-side storage rather than visible DOM elements:
* **Web Storage (`localStorage` & `sessionStorage`):** Scans key names and structured values for authentication evidence, user profiles, or JWT tokens.
* **SPA Framework State Stores:** Detects active state management frameworks (React Redux, Pinia, Vuex, Angular) holding user authentication objects.
* **Global Auth Objects:** Checks for runtime globals such as `window.__auth`, `window.firebase`, or active Service Workers managing offline session sync.

---

## 4. Identity Overlay & SSO Detection (`IdentityOverlayDetector`)

Modern web applications frequently embed third-party identity providers in floating dialogs, modals, or iframes (e.g. Google One Tap, Microsoft Entra / MSA, Okta, Atlassian, Apple Sign-In).

When an agent interacts with a web page, these overlays can intercept clicks, obscure form controls, or present unexpected authentication prompts. Nova's `IdentityOverlayDetector` operates across four catalog families while filtering out non-auth overlays:

```mermaid
flowchart TD
    Overlay["Observed Floating Frame / Modal / Shadow Root"] --> Negative{"Matches Negative Pattern? (Ads, CMP, Media, Chat, Captcha)"}
    Negative -->|Yes| Ignored["EXCLUDE (Not an Identity Overlay)"]
    Negative -->|No| Family{"Match Provider Catalog"}

    Family -->|Consumer SSO| C1["Google One Tap, Apple, Meta, GitHub, LinkedIn, X, Discord"]
    Family -->|Enterprise IdP| C2["Microsoft Entra ID, Okta, Auth0, OneLogin, Ping, AWS Cognito"]
    Family -->|SaaS IdP| C3["Atlassian, Shopify, Adobe, Zoom, Salesforce, Workday"]
    Family -->|Web Component| C4["Clerk, Auth0 Lock, Okta Sign-In Widget, Descope, Stytch"]

    C1 & C2 & C3 & C4 --> Score["Geometrical & Origin Confidence Scoring"]
    Score -->|Confidence >= 0.70| Warn["Emit Advisory Warning: safety.identity_overlay"]
```

### 4.1 Provider Catalog Families
1. **Consumer SSO (`ConsumerSso`):** Google (`accounts.google.com`, `/gsi/`, `credential_picker`), Apple (`appleid.apple.com`), Meta/Facebook (`connect.facebook.net`), GitHub, GitLab, LinkedIn, X/Twitter, Discord, Slack, Dropbox, Box, Amazon.
2. **Enterprise IdP (`EnterpriseIdp`):** Microsoft Entra ID / MSA (`login.microsoftonline.com`, `login.live.com`), Okta (`okta.com`, `okta-emea.com`), Auth0, OneLogin, Ping Identity, Duo, JumpCloud, Cloudflare Access, AWS Cognito, Keycloak.
3. **SaaS IdP (`SaasIdp`):** Atlassian, Shopify, Adobe, Zoom, Salesforce, Workday.
4. **Web Component & Shadow DOM (`WebComponentIdentity`):** Walks open shadow roots to detect encapsulated custom elements such as `auth0-lock`, `okta-signin-widget`, `apple-id-signin-button`, and Google Identity Services components (`<g_id_onload>`).

### 4.2 Negative Pattern Exclusion
To eliminate false alarms, the detector applies strict negative pattern rules:
* **Advertisements & Tracking:** Excludes `doubleclick.net`, `googlesyndication.com`, `adsrvr.org`, `criteo`, `taboola`, `outbrain`.
* **Cookie Consent Management (CMP):** Excludes `onetrust`, `cookielaw`, `cookiebot`, `didomi`, `usercentrics`, `sourcepoint`, `quantcast`, `trustarc`, `consensu.org`, `iubenda`.
* **Embedded Media:** Excludes `youtube.com/embed`, `vimeo.com`, `spotify.com/embed`, `soundcloud.com`, `twitch.tv/embed`.
* **Support & Live Chat:** Excludes `intercom.io`, `zendesk.com`, `crisp.chat`, `drift.com`, `tawk.to`, `freshchat.com`.
* **Bot Challenges:** Excludes `recaptcha`, `hcaptcha`, `challenges.cloudflare.com` (Turnstile), `arkose`.

### 4.3 Geometrical Scoring & Advisory Warning
* **Base Confidence:** $0.38$ to $0.45$ per catalog provider.
* **Boosts:** $+0.20$ for visible cross-origin iframe; $+0.15$ for overlay geometry ($\ge 10\%$ viewport area or $\ge 12{,}000\text{ px}^2$); $+0.10$ for high `z-index` ($\ge 1000$) or fixed/absolute positioning; $+0.10$ for auth-related titles.
* **Dampening:** $-0.25$ if offscreen, very small, or `pointer-events: none`.
* **Advisory Warning:** Emitted when confidence $\ge 0.70$. Projected as `structuredContent.identityOverlayWarning` and triggers AAG gate `safety.identity_overlay` (`status="warned"`), alerting the agent that an authentication overlay is obscuring the viewport.

---

## 5. The 6 Lifecycle Stages (`auth.stage`) & Confidence Scoring Matrix

ASD maps gathered signals to an explicit authentication lifecycle stage, providing agents with complete situational awareness of the current page context.

```mermaid
stateDiagram-v2
    [*] --> public_page: Unauthenticated Content
    public_page --> login_wall: Credentials Required
    public_page --> identity_step: Identifier-First Flow
    public_page --> federated_login: Third-Party SSO Surface

    identity_step --> login_wall: Password Prompt
    identity_step --> federated_login: Redirect to IdP

    login_wall --> mfa_challenge: One-Time Code Required
    federated_login --> mfa_challenge: 2FA Prompt

    login_wall --> authenticated: Login Succeeded
    federated_login --> authenticated: SSO Handshake Complete
    mfa_challenge --> authenticated: 2FA Succeeded

    login_wall --> unknown: Ambiguous Signals
    authenticated --> public_page: Logged Out / Session Expired
```

### 5.1 Stage Definitions

| Stage Identifier | Characteristic Surface | Key Evidentiary Signals |
| :--- | :--- | :--- |
| **`public_page`** | Standard unauthenticated content | No password fields, no login prompts, low auth confidence ($< 0.20$), standard navigation. |
| **`login_wall`** | Traditional sign-in form | Visible password input, form submit button, login action anchors, or explicit password submit readiness. |
| **`identity_step`** | Multi-step sign-in (email/username first) | Identifier input field visible, "Continue" / "Next" action, no password field yet, auth headings present. |
| **`federated_login`** | Third-party SSO portal | Provider buttons (`Google`, `Microsoft`, `Apple`, `Okta`), no local credential inputs. |
| **`mfa_challenge`** | Two-Factor / Multi-Factor challenge | One-time code field (`autocomplete="one-time-code"`), SMS/TOTP prompts, previous auth step completed. |
| **`authenticated`** | Active logged-in user session | Visible logout controls, profile/avatar navigation, valid storage keys, or active runtime auth globals. |
| **`unknown`** | Ambiguous or conflicting page state | Signup forms with both current and new password fields, contradictory signals, or failed probe execution. |

### 5.2 Confidence Scoring & Threshold Engine
The scoring engine computes continuous confidence values between `0.0` and `1.0`:
* **Login Wall Scoring:**
  * Password input inside a form with a submit button: **Base `0.90`**.
  * Standalone visible password field: **Base `0.65`**.
  * Identity step surface with "Continue" trigger: **Base `0.75`** (or `0.60` without explicit step action).
  * Federated SSO surface: **Base `0.55`**.
  * Presence of "Forgot Password" or login actions adds $+0.10$ each (clamped to `1.0`).
  * *Signup Discounting:* If `new-password`, second password confirmation, or terms-and-conditions checkboxes appear without `current-password`, login confidence is discounted to $\le 0.20$ to prevent false positives.
* **Authenticated Scoring:**
  * Visible logout link: **Base `0.95`**.
  * $\ge 3$ account controls (profile link, settings link, avatar in header): **`0.80`**.
  * 2 account controls: **`0.45`** (yields `Unknown`).
  * 1 account control: **`0.20`** (yields `No`).
  * Active auth globals or SPA state stores: **Up to `0.90`** depending on storage backing.
  * Active login walls or password fields depress logged-in confidence to $\le 0.30$.

### 5.3 Dual-Fact Mapping
Verdicts are published to the Tool Observation Bus (TOB) and dual-facts dictionary:

| Fact Key | Type | Description |
| :--- | :--- | :--- |
| `auth.loginWallVisible` | `boolean \| null` | `true` if $\ge 0.50$, `false` if $< 0.20$, `null` if between. |
| `auth.loggedIn` | `boolean \| null` | `true` if $\ge 0.50$, `false` if $< 0.20$, `null` if between. |
| `auth.mfaChallenge` | `boolean \| null` | `true` if qualifying OTC field exists with auth context. |
| `auth.authError` | `boolean \| null` | `true` if error messages are detected on an active auth surface. |
| `auth.stage` | `string` | One of the 6 lifecycle stages (`login_wall`, `identity_step`, etc.). |
| `auth.persistence` | `string` | Persistence tier (`persistent`, `session_scoped`, `ephemeral`, etc.). |
| `auth.assessment` | `object` | Full diagnostic record including signal traces, raw confidences, and framework name. |

---

## 6. Session Persistence Classification (`auth.persistence`) & Navigation Safety

Modern Single Page Applications (SPAs) manage user credentials across varying storage tiers. A destructive page reload or cross-origin navigation can instantly destroy an in-memory session. ASD classifies persistence to enable predictive navigation gating.

```mermaid
flowchart TD
    Verdict["auth.loggedIn == Yes"] --> Classify{"Where does session state reside?"}
    Classify -->|Cookies or localStorage| Persistent["persistent: Survives reloads & tab close"]
    Classify -->|sessionStorage only| SessionScoped["session_scoped: Survives same-origin navigation; lost on tab close"]
    Classify -->|Cookies + SPA State Store| SpaHybrid["spa_cookie_plus_state: Rehydration required; cross-origin navigation risky"]
    Classify -->|Memory only / JS closure| Ephemeral["ephemeral: Hard navigation DESTROYS session"]

    Ephemeral --> Gate["AAG Gate: pks.spa_navigation_block (Enforce client-side routing)"]
    SpaHybrid --> Warn["Warn: Prefer nova.route over full nova.navigate"]
```

### 6.1 The Four Persistence Tiers

1. **`persistent`:**
   * **Backing:** Persistent cookies or `localStorage` auth tokens.
   * **Safety:** Highly resilient. The session survives full-page hard refreshes (`nova.reload`), browser tab recycling, and browser restarts.
2. **`session_scoped`:**
   * **Backing:** Stored in `sessionStorage`.
   * **Safety:** Survives same-origin full-page navigations (`nova.navigate`) within the same tab, but is completely lost if the tab is closed or a new tab is opened.
3. **`spa_cookie_plus_state`:**
   * **Backing:** Standard cookies exist, but active user state is managed in an in-memory client store (Redux, Pinia, Vuex) or runtime auth global.
   * **Safety:** A hard navigation or reload may cause visual de-synchronization or state loss if server rehydration fails. Nova warns agents to prefer client-side SPA routing (`nova.route`) over full-page navigation (`nova.navigate`).
4. **`ephemeral`:**
   * **Backing:** Pure memory-only authentication (e.g. JWT held only in a JavaScript closure or React component state). No tokens exist in cookies or web storage.
   * **Safety: CRITICAL.** Any standard browser reload (`F5`) or external navigation causes **immediate, unrecoverable session loss**.

### 6.2 The Navigation Safety Gate & Persistence Cache
Whenever an agent invokes navigation tools (`nova.navigate`, `nova.reload`), Nova's navigation safety pipeline evaluates the target:
* **10-Minute Persistence Cache (`AuthPersistenceCache`):** Caches persistence classifications per `(profileId, origin)` for up to 10 minutes to minimize IPC latency during frequent interactions.
* **`forceAuthProbe` Parameter:** Agents can pass `forceAuthProbe=true` to invalidate the cache and force a fresh live evaluation.
* **Fail-Open Deadline:** The safety gate enforces a 3-second deadline (`AuthPersistenceGateTimeout`); if the renderer is wedged, the gate logs a diagnostic warning and proceeds rather than permanently freezing execution.
* **Cross-Origin Enforcement:**
  * For `session_scoped` sessions, same-origin navigation is permitted, while cross-origin navigation is blocked (`auth.session_scoped_cross_origin`).
  * For `spa_cookie_plus_state`, same-origin issues an advisory warning (`auth.spa_cookie_plus_state_same_origin`), while cross-origin is blocked.
  * For `ephemeral` sessions, **any full-page navigation or reload is strictly blocked** (`auth.ephemeral`) unless the agent explicitly confirms session destruction (`confirmSessionDestruction=true`).

---

## 7. The Surface Safety Lexicon Shield & Exclusion Dictionaries

Autonomous surface exploration (`nova.explore_surface`) and background web crawlers (`nova.crawl_start`) navigate web applications by discovering interactive elements and clicking them.

Without strict safety guardrails, automated explorers create havoc:
* Clicking `Abmelden` or `Sign Out` terminates authenticated sessions.
* Clicking `Delete Workspace`, `Cancel Subscription`, or `Purge Data` destroys user environments.
* Clicking `Buy Now` or `Place Order` executes unintended financial transactions.

To prevent this, Nova equips ASD and the Surface Explorer with the **Surface Safety Lexicon Shield**.

### 7.1 Multi-Lingual Safety Lexicons
Nova embeds comprehensive, multi-lingual JSON lexicon dictionaries that classify interface elements into risk tiers:

```mermaid
flowchart TD
    Trigger["Candidate Interactive Trigger (Button, Link, Icon)"] --> Matcher["Surface Safety Matcher"]
    Matcher --> L1["high-risk-identity.json (Logout, Impersonation, Roles)"]
    Matcher --> L2["dangerous.json (Account Deletion, Purge, Wipe, 2FA)"]
    Matcher --> L3["high-risk-automation.json (Checkout, Billing, Orders)"]
    Matcher --> L4["high-risk-bulk.json (Bulk Delete, Batch Actions)"]
    Matcher --> L5["high-risk-public-sharing.json (Publish, Share Publicly)"]

    L1 & L2 --> HardVeto["HARD DENY / VETO (Blocked from Crawling & Exploration)"]
    L3 & L4 & L5 --> Approval["PROBE_REQUIRED (Requires Explicit User Approval)"]
```

| Lexicon Category | File Fragment | Target Languages | Example Triggers Matched | Explorer & Crawler Action |
| :--- | :--- | :--- | :--- | :--- |
| **`HighRiskIdentity`** | `high-risk-identity.json` | DE, EN, ES, FR | `logout`, `abmelden`, `sign out`, `se déconnecter`, `cerrar sesión`, `switch profile`, `impersonate`, `assume role`, `transfer admin`, `identität wechseln`. | **HARD DENY.** Crawlers and automated explorers are strictly prohibited from clicking identity-altering triggers. |
| **`Dangerous`** | `dangerous.json` | DE, EN, ES, FR (9,000+ phrases) | `delete account`, `alle daten löschen`, `cancel subscription`, `abo kündigen`, `2fa zurücksetzen`, `reset 2fa`, `purge`, `wipe`, `destroy`. | **HARD DENY.** Catastrophic and permanent mutations are vetoed immediately. |
| **`HighRiskAutomation`** | `high-risk-automation.json` | DE, EN, ES, FR | `buy now`, `jetzt kaufen`, `place order`, `kostenpflichtig bestellen`, `checkout`, `pay`, `zahlen`. | **PROBE_REQUIRED.** Financial checkout triggers require human-in-the-loop confirmation. |
| **`HighRiskBulk`** | `high-risk-bulk.json` | DE, EN, ES, FR | `bulk delete`, `alle löschen`, `select all and delete`, `batch cancel`. | **PROBE_REQUIRED.** High-volume mutations are quarantined. |
| **`HighRiskPublicSharing`** | `high-risk-public-sharing.json` | DE, EN, ES, FR | `share publicly`, `öffentlich freigeben`, `publish to web`, `make public`. | **PROBE_REQUIRED.** Privacy-altering visibility toggles require approval. |
| **`SafeReadonly`** | `safe-readonly.json` | Multi | `view`, `details`, `expand`, `anzeigen`, `öffnen`. | **ALLOW.** Read-only inspection triggers are permitted. |
| **`SafeNavigation`** | `safe-navigation.json` | Multi | `next`, `previous`, `page 2`, `weiter`, `zurück`. | **ALLOW.** Pagination and read-navigation triggers are permitted. |

### 7.2 The 5-Module Surface Safety Pipeline
When evaluating candidate elements, Nova executes a deterministic 5-module evaluation pipeline:

1. **SemanticAllowModule:** Identifies declarative open controls (e.g. `<details>`, ARIA popups, tabs, accordions) designed for safe content disclosure.
2. **DomContextHardDenyModule (Structural Veto):**
   * Automatically denies form-owned submit elements (`input[type="submit"]`, `<button>` defaulting to submit inside `<form>`).
   * Automatically denies form-associated overrides (`formaction`, `formmethod`).
   * Automatically denies file download triggers (`download` attribute).
   * Automatically denies external protocol schemes (`mailto:`, `tel:`, `javascript:`).
   * Automatically denies confirmation dialog triggers (`role="alertdialog"`).
3. **KeywordSoftEvidenceModule (Lexicon Shield):**
   * Matches element text, accessible names, titles, and IDs against the multi-lingual lexicon fragments.
   * Triggers matching `HighRiskIdentity` or `Dangerous` receive an immediate veto.
4. **HeuristicQualificationModule:** Evaluates complex disclosure patterns (e.g. custom elements with popup heuristics).
5. **ReadNavQualificationModule:** Qualifies read-only pagination controls (`load more`, `next page`).

**Aggregation Invariant:** *Hard Deny > Runtime Invariants > Strong Allow > Soft Evidence.* A trigger matching `logout` or `delete account` can **never** be clicked by autonomous exploration, regardless of its semantic markup or button appearance.

---

## 8. Crawler Integration & SSRF Defense-in-Depth

The web crawler (`nova.crawl_start`, `nova.crawl_status`, `nova.crawl_verify`) shares ASD and surface safety engines to maintain security boundaries while indexing web applications.

```mermaid
flowchart LR
    Crawler["Crawl Engine"] --> PolicyCheck{"Pre-Flight Policy Check"}
    PolicyCheck -->|Target on Auth Wall| AbortWall["BLOCK: auth.wall"]
    PolicyCheck -->|Target uses Fragile Persistence| AbortPersist["BLOCK: session_scoped / ephemeral"]
    PolicyCheck -->|Safe Target Path| NavGuard["URL Safety & SSRF Validator"]

    NavGuard --> IPCheck{"Is Host Private / Loopback?"}
    IPCheck -->|127.0.0.1, 10.0.0.0/8, 192.168.0.0/16, etc.| BlockSSRF["BLOCK Navigation (Prevent SSRF)"]
    IPCheck -->|Public Routable IP| Fetch["Execute Page Fetch & Continuous ASD Probing"]
```

### 8.1 Target-Bound Pre-Flight Gating (`CrawlerAccessPolicy`)
When an agent attempts to start a target-bound crawl (`nova.crawl_start(targetId=...)`), Nova performs a pre-flight probe using ASD:
* **Interactive Login Wall (`auth.wall`):** If the visible target currently shows an authentication surface, the crawl is blocked (`-32001`): *"Target-bound crawl blocked: the visible target currently shows an auth/login surface that should be continued in the live tab."* A headless crawler cannot solve user authentication.
* **Session-Scoped Storage:** If the target relies on `sessionStorage` (`session_scoped`), target-bound crawling is blocked: detached background WebViews do not share tab-scoped session storage.
* **Hydrated SPA State & Ephemeral Tokens:** If the target uses `spa_cookie_plus_state` or `ephemeral`, the crawl is blocked because background WebViews cannot reproduce volatile in-memory client state.
* **Safe Fallback:** Nova advises the agent to use `nova.crawl_links` (direct in-tab traversal) instead of launching a detached hidden crawler.

### 8.2 Continuous Auth Probing & Session Parity
During crawling, every newly loaded page is continuously evaluated by ASD:
* **Login Wall Avoidance:** If a crawl job encounters `auth.loginWallVisible == true` on a public crawl, it halts crawling along that path to prevent becoming trapped in authentication loops.
* **Target Auth Parity Verification:** When a crawl is bound to an authenticated tab session, Nova continuously compares the crawl's authentication status against the target tab (`HasTargetAuthParityMismatch`). If the target is logged in but the crawler encounters a login wall or logged-out state, the crawler immediately aborts with error code `crawl.target_session_mismatch`, preventing unauthenticated page corruption.

### 8.3 Network Boundary & SSRF Prevention
To prevent autonomous crawlers from being weaponized for Server-Side Request Forgery (SSRF) or scanning private internal intranets, Nova enforces strict network boundary validation:
* **Scheme Restrictions:** Crawlers strictly permit `http://` and `https://` URLs.
* **Prohibited Hostnames:** Blocks `localhost` and all `.local` mDNS domains.
* **Private & Link-Local IP Blocking:** Literal IP addresses and DNS-resolved target IPs are strictly blocked if they fall within RFC 1918 or local ranges:
  * `127.0.0.0/8` (IPv4 Loopback)
  * `10.0.0.0/8` (Private Class A)
  * `172.16.0.0/12` (Private Class B)
  * `192.168.0.0/16` (Private Class C)
  * `169.254.0.0/16` (Link-Local / APIPA / Cloud Metadata Services like `169.254.169.254`)
  * `::1` (IPv6 Loopback) and `fe80::/10` (IPv6 Link-Local)

### 8.4 Ghost Surface Reaper (`HiddenCrawlSurfaceRegistry`)
Headless crawling utilizes hidden WebViews. If a crawl process terminates unexpectedly or encounters a worker fault, leaked WebViews could continue executing scripts or playing background media ("ghost audio").
* **Continuous Registry Tracking:** Every hidden crawl WebView is registered with its active job ID and idle timestamp.
* **Sweeper Daemon:** A background sweeper evaluates registered surfaces every 60 seconds.
* **5-Minute Idle Threshold:** Any hidden WebView that remains idle without navigation or script execution for $\ge 5$ minutes is automatically disposed and garbage collected.

---

## 9. Guarded Interactions & Vault Workflow

Submitting authentication credentials requires deterministic synchronization between password vaults, form submission, and ASD verification.

```mermaid
sequenceDiagram
    autonumber
    actor Agent
    participant Vault as Password Vault
    participant Nova as Nova Browser Host
    participant Page as Web Page / DOM
    participant ASD as Auth Surface Detection

    Agent->>Nova: Call nova.page_info / ASD Probe
    Nova-->>Agent: auth.loginWallVisible = true, stage = "login_wall"
    Agent->>Vault: nova.vault_prepare_fill(site="github.com")
    Vault-->>Page: Injects credentials securely into DOM fields
    Agent->>Nova: nova.guarded_login(selector="button[type=submit]")
    Nova->>Page: Executes submit click
    Nova->>ASD: Polls ASD post-submission transition
    alt Transition to Logged In
        ASD-->>Nova: auth.loggedIn = true, stage = "authenticated"
        Nova-->>Agent: Success (Session established)
    else Transition to MFA
        ASD-->>Nova: auth.mfaChallenge = true, stage = "mfa_challenge"
        Nova-->>Agent: Undecided (Request TOTP / 2FA code)
    else Transition to Error
        ASD-->>Nova: auth.authError = true
        Nova-->>Agent: Failed (Invalid credentials detected)
    end
```

### 9.1 The Non-Idempotent Contract in `nova.guarded_login`
`nova.guarded_login` enforces strict Closed-Loop System (CLS) invariants tailored to authentication:

```json
{
  "actionKind": "submit_form",
  "retryPolicy": "non_idempotent",
  "ambiguityPolicy": "signal",
  "preconditions": {
    "all": [
      { "factKey": "auth.loginWallVisible", "op": "eq", "value": true }
    ]
  },
  "postconditions": {
    "success": {
      "all": [
        { "factKey": "auth.loggedIn", "op": "eq", "value": true }
      ]
    },
    "forbidden": {
      "forbidden": [
        { "factKey": "auth.authError", "op": "eq", "value": true }
      ]
    },
    "ambiguous": {
      "any": [
        { "factKey": "auth.mfaChallenge", "op": "eq", "value": true },
        { "factKey": "auth.stage", "op": "eq", "value": "mfa_challenge" },
        { "factKey": "auth.stage", "op": "eq", "value": "identity_step" },
        { "factKey": "auth.stage", "op": "eq", "value": "federated_login" }
      ]
    }
  }
}
```

* **Non-Idempotent Retry Policy:** Authentication submissions are inherently non-idempotent. If a network lag occurs or an intermediate MFA prompt appears, Nova prohibits automated retries of the submit action, preventing rate limiting or account lockouts.
* **Frame Scoping:** If a login form is embedded within a same-origin `<iframe>`, `nova.guarded_login` accepts an optional `frameId`, scoping both click execution and fact assertions directly to that frame context.

### 9.2 Secret Masking with the Password Vault
Agents should never read plaintext passwords into their language model context.
* **Safe Fill Preparation:** The agent calls `nova.vault_prepare_fill` or `nova.type_selector_secret`, specifying a secret reference key.
* **Direct IPC Injection:** Nova injects the decrypted secret directly into the WebView2 DOM input buffer via native OS messaging.
* **Zero Model Exposure:** Plaintext passwords are never reflected in tool outputs, transcripts, or MCP message payloads.

---

## 10. Procedural Knowledge & Zero-Leak Credential Redaction

Nova's Procedural Knowledge Store (PKS) monitors and learns recurring interaction patterns. During authentication flows, PKS observes sequences while enforcing strict data hygiene:

* **Sequence Analysis:** The tracker identifies the sequence pattern: `type(identifier)` $\rightarrow$ `type(password)` $\rightarrow$ `click(submit)`.
* **Zero Credential Ingestion:** Password and identifier values are never ingested into PKS event buffers. Element roles (`InputKind`) are inferred structurally from element attributes, not input contents.
* **URL Token Redaction:** Post-auth redirects frequently append sensitive query parameters (`?code=...`, `?token=...`, `?session=...`). PKS automatically strips query strings before persisting URL evidence, preventing accidental secret leakage into shared knowledge stores.
* **Reflection Gate Integration:** If an origin requires qualified multi-factor authentication (MFA / SSO), Nova's reflection tracker generates domain notes (e.g. *"example.com requires qualified authentication (2FA/SSO)"*) to guide subsequent agent sessions.

---

## 11. Native Dialog Authentication (HTTP Basic & Client Certificates)

In-page DOM probing cannot intercept authentication challenges that occur at the network protocol layer (HTTP 401 Basic, Digest, Proxy Authentication, or TLS Client Certificates).

Nova routes these challenges through native UI dialog handlers:
* **HTTP Basic / Digest Dialogs:** Answered via `nova.ui_auth_prompt_resolve(decision='use_vault' | 'confirm' | 'cancel')`. When using `'use_vault'`, Nova matches the origin against stored vault credentials and submits them directly to the network stack without DOM exposure.
* **TLS Client Certificates:** Answered via `nova.ui_client_certificate_prompt_resolve(decision='send' | 'send_none')`.
* **Server Certificate Warnings:** Handled via `nova.ui_certificate_prompt_resolve(decision='proceed' | 'refuse')`.

---

## 12. Sensitive Action Re-Authentication Gate

When an operator or agent attempts to reveal or export credentials stored inside Nova's Password Vault, software-only permissions are insufficient.

Nova enforces the **Sensitive Action Re-Authentication Gate**:
* **Hardware Biometrics First:** Triggers Windows Hello (`UserConsentVerifier`) requiring biometric verification (fingerprint or facial recognition).
* **Credential UI Fallback:** If biometrics are unavailable, falls back to Win32 Credential UI (`CredUIPromptForWindowsCredentials`) verified via secure local `LogonUser`.
* **Hardware-Backed TTL:** Upon successful biometric confirmation, an in-memory stopwatch cache suppresses re-prompts for a strictly limited Time-To-Live (TTL). The cache is invalidated immediately if settings are modified or the application restarts.

---

## 13. Summary: The ASD & Surface Safety Architectural Matrix

| Subsystem | Primary Responsibility | Governing Invariant | Outcome on Violation |
| :--- | :--- | :--- | :--- |
| **ASD Tri-State Logic** | Evaluates `loginWallVisible`, `loggedIn`, `mfaChallenge`, `authError`. | Three-valued logic: `Unknown` is never coerced to `false`. | Prevents destructive re-login loops. |
| **Host Cookie Inspection** | Inspects native browser store for `HttpOnly` session cookies. | Host inspection enriches probe when DOM is cookie-blind. | Prevents false ephemeral classifications. |
| **Identity Overlay** | Detects Google One Tap, Entra, Okta, and Apple SSO iframes. | Read-only awareness; non-invasive advisory payload. | Alerts agent with `safety.identity_overlay` warning. |
| **Persistence Gating** | Classifies `persistent`, `session_scoped`, `spa_cookie_plus_state`, `ephemeral`. | Volatile sessions must not undergo hard reloads or external navigations. | AAG blocks navigation with `pks.spa_navigation_block`. |
| **Lexicon Shield** | Classifies triggers against multi-lingual dictionaries (`dangerous`, `high-risk-identity`). | Hard Deny > Runtime Invariants > Strong Allow > Soft Evidence. | Vetoes crawler/explorer clicks on `logout`, `delete`, or checkout. |
| **Crawler Access Policy** | Pre-flight validation for target-bound crawls. | Detached crawlers cannot solve login walls or share tab storage. | Blocks crawl on `auth.wall` or ephemeral session; suggests `crawl_links`. |
| **Network SSRF Boundary** | Blocks crawler access to private RFC 1918 and loopback IPs. | Complete network isolation against internal intranets. | Rejects navigation to `127.0.0.1`, `10.0.0.0/8`, `169.254.0.0/16`. |
| **Ghost Surface Reaper** | Sweeps idle background crawl WebViews every 60 seconds. | Surfaces idle $> 5$ minutes are terminated. | Prevents ghost audio and background resource leaks. |
| **Guarded Login Contract** | Executes login form submission under Closed-Loop verification. | Requires `auth.loginWallVisible == true`; non-idempotent retry policy. | Reports intermediate MFA challenges; prevents blind re-submission. |
| **PKS Knowledge Redaction** | Learns interaction sequences while scrubbing credentials and tokens. | Zero credential ingestion; query tokens redacted. | Protects secrets from persistent knowledge logs. |
| **Native Auth Dialogs** | Resolves HTTP 401 Basic, Digest, and Client Certificate prompts. | Bridges network-layer challenges without DOM script exposure. | Securely answers prompts using stored vault entries. |
| **Sensitive Re-Auth Gate** | Protects password export and plaintext credential reveal. | Windows Hello / CredUI hardware confirmation required. | Blocks credential disclosure without operator presence. |

---

## Related Documentation

* **[Agent Awareness Gates (AAG)](../agent-awareness-gates-aag/README.md)** — Situational awareness gates and pre-execution safety rules.
* **[Agent-Native Affordances](../agent-native-affordances/README.md)** — Atomic compound primitives and closed-loop interaction mechanics.
* **[Closed-Loop System (CLS)](../closed-loop-system-cls/README.md)** — Post-action verification and assertion contracts.
* **[Password Vault & Secret Injection](../privacy/vault-and-secrets/README.md)** — Secure credential storage and hardware-gated injection.
* **[Web Crawler & Discovery](../crawler-and-discovery/README.md)** — Autonomous indexing, target session parity, and surface discovery.
* **[Operational Knowledge (OK)](../learning/operational-knowledge-ok/README.md)** — Real-time tab state, session observation, and capability tracking.
* **[Native Dialogs & UI Prompts](../native-dialogs-and-prompts/README.md)** — Handling dialogs and prompts outside the page.

[All core features](../README.md)
