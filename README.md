# Nova Browser

> **BETA SOFTWARE — USE AT YOUR OWN RISK**
>
> Nova Browser is in active beta development. Bugs, crashes, data loss, and breaking changes
> may occur. There is no warranty of any kind. Do not rely on this software for critical tasks.
> By using Nova you accept the [Disclaimer](DISCLAIMER.md), [Acceptable Use Policy](ACCEPTABLE-USE.md), and the [License](LICENSE).
>
> **BETA-SOFTWARE — NUTZUNG AUF EIGENE GEFAHR**
>
> Nova Browser befindet sich in aktiver Beta-Entwicklung. Fehler, Abstuerze, Datenverlust und
> Breaking Changes koennen auftreten. Es gibt keinerlei Gewaehrleistung. Verwende diese Software
> nicht fuer kritische Aufgaben. Mit der Nutzung akzeptierst du den
> [Haftungsausschluss](DISCLAIMER.md), die [Nutzungsrichtlinie](ACCEPTABLE-USE.md) und die [Lizenz](LICENSE).

---

**A supervised AI agent runtime built into a real desktop browser.**

Nova turns a local Windows browser into a controlled workspace for AI agents.
It combines a full Chromium/WebView2 browsing environment, an open local MCP server,
built-in Claude/Codex/Gemini sidecars, local knowledge stores, discovery and crawling tools,
scheduled automation, and browser-enforced safety gates.

The important part is not that an agent can click a page.
The important part is that the browser can **see, constrain, verify, remember, and explain**
what the agent is doing.

## Quick Start

1. Download the latest release from [Releases](https://github.com/joelaniol/nova/releases)
2. Extract the ZIP (portable) or run the installer
3. Run `NovaBrowser.exe`
4. Open Settings to configure language, browser identity, sandboxes, AI provider accounts, MCP access, and agent permissions

> On first launch, Windows SmartScreen may warn that the app is not code-signed.
> For independent beta builds this is expected. Choose "More info" > "Run anyway".

## At a Glance

- **Real desktop browser** — WebView2 tabs, sandboxes, history, favorites, downloads, zoom, print, find, site info, session restore, proxy profiles, and browser identity settings
- **Open agent platform** — A localhost MCP server exposes Nova's browser and knowledge tools to Claude Code, Cursor, Windsurf, custom scripts, and any MCP-compatible agent
- **Visible AI workspace** — Claude, Codex, and Gemini run through the same agent panel with live transcript, tool cards, approvals, interrupts, and provider switching
- **Local web memory** — LCJ, ALP, PKS, OK, task memory, and operator notes let agents learn verified website behavior without a cloud service
- **Deep exploration** — Website MCP discovery, hidden-WebView crawling, live-tab crawling for authenticated SPAs, and Surface Explorer for UI states without URLs
- **Scheduled automation** — Tasks run on intervals, file changes, manual triggers, or chained workflows
- **Browser-side safety** — Domain rules, claims, audit logs, vault SecretRefs, emergency stop, kill switches, and strict MCP validation live in Nova, not in a model prompt

## What Makes Nova Different

| Principle | How Nova implements it |
|---|---|
| **The browser is the agent boundary** | Agents get a live browser surface with explicit tools. Nova resolves targets, checks claims, validates input, applies domain policy, and logs decisions. |
| **Humans stay in the loop** | Agent work is visible in the browser and agent panel. High-impact actions require approval. Emergency Stop cancels all active agent work. |
| **Knowledge is local and quality-gated** | Nova observes website behavior, promotes it after checks, revalidates later, and downgrades when sites change. |
| **Automation is verified** | Preconditions, postconditions, and tri-state outcomes instead of "click dispatched = success". |
| **Agents are interchangeable** | Claude, Codex, and Gemini are built in, but any MCP-compatible client can connect. |

## Requirements

- Windows 10 or Windows 11
- Windows App SDK Runtime 1.8
- Microsoft Edge WebView2 Runtime

If Nova does not start because the Windows App Runtime is missing:

- **Option A:** Run `repair-windows-app-runtime.ps1` (included in the release)
- **Option B:** Download manually from [Microsoft](https://aka.ms/windowsappsdk/1.8/latest/windowsappruntimeinstall-x64.exe)

## MCP Integration

Nova runs a local MCP server while active. External clients can connect using the discovery file:

```
%LOCALAPPDATA%\NovaBrowser\mcp.json
```

This file contains the endpoint and bearer token. Treat it as a local credential.

## Local Data

All data is stored locally under `%LOCALAPPDATA%\NovaBrowser\` — settings, browser profiles, history, favorites, vault, logs, knowledge stores, crawler databases, task workspaces, and conversation archives.

Nova does not require a remote cloud service. When using third-party AI providers, their own data policies apply.

## License

All rights reserved. See [LICENSE](LICENSE) for details.

Third-party components are subject to their own licenses. See [THIRD-PARTY-LICENSES.txt](THIRD-PARTY-LICENSES.txt) in the release folder.

## Contact

Joel Aniol — [LinkedIn](https://www.linkedin.com/in/joelaniol/)

---

# Nova Browser (Deutsch)

**Eine beaufsichtigte KI-Agenten-Runtime in einem echten Desktop-Browser.**

Nova macht aus einem lokalen Windows-Browser einen kontrollierten Arbeitsraum fuer KI-Agenten. Es verbindet einen vollstaendigen Chromium-/WebView2-Browser, einen offenen lokalen MCP-Server, eingebaute Claude-/Codex-/Gemini-Sidecars, lokale Wissensspeicher, Discovery- und Crawler-Werkzeuge, geplante Automation und browserseitige Sicherheits-Gates.

Wichtig ist nicht, dass ein Agent auf einer Seite klicken kann. Wichtig ist, dass der Browser **sehen, begrenzen, verifizieren, erinnern und erklaeren** kann, was der Agent tut.

## Schnellstart

1. Neuestes Release von [Releases](https://github.com/joelaniol/nova/releases) herunterladen
2. ZIP entpacken (portabel) oder Installer ausfuehren
3. `NovaBrowser.exe` starten
4. In den Einstellungen Sprache, Browser-Identitaet, Sandboxes, KI-Provider-Konten, MCP-Zugriff und Agentenrechte konfigurieren

> Beim ersten Start kann Windows SmartScreen melden, dass die App nicht signiert ist. Bei Beta-Builds ist das erwartbar. "Weitere Informationen" > "Trotzdem ausfuehren".

## Auf einen Blick

- **Echter Desktop-Browser** — WebView2-Tabs, Sandboxes, History, Favoriten, Downloads, Zoom, Drucken, Suche, Site-Info, Session Restore, Proxy-Profile und Browser-Identitaet
- **Offene Agenten-Plattform** — Ein lokaler MCP-Server stellt Novas Browser- und Wissenswerkzeuge fuer Claude Code, Cursor, Windsurf, eigene Scripts und jeden MCP-faehigen Agent bereit
- **Sichtbarer KI-Arbeitsraum** — Claude, Codex und Gemini laufen im selben Agentenpanel mit Live-Transcript, Tool-Cards, Approvals, Interrupt und Provider-Wechsel
- **Lokales Web-Gedaechtnis** — LCJ, ALP, PKS, OK, Task Memory und Operator Notes helfen Agents, verifiziertes Website-Verhalten zu lernen
- **Tiefe Exploration** — Website-MCP-Discovery, Hidden-WebView-Crawling, Live-Tab-Crawling und Surface Explorer
- **Geplante Automation** — Tasks laufen nach Intervall, Dateiaenderung, manuellem Trigger oder Workflow-Kette
- **Browserseitige Sicherheit** — Domain-Regeln, Claims, Audit-Logs, Vault SecretRefs, Emergency Stop, Kill-Switches und strikte MCP-Validierung

## Voraussetzungen

- Windows 10 oder Windows 11
- Windows App SDK Runtime 1.8
- Microsoft Edge WebView2 Runtime

Falls Nova wegen fehlender Windows App Runtime nicht startet:

- **Option A:** `repair-windows-app-runtime.ps1` ausfuehren (im Release enthalten)
- **Option B:** Manuell herunterladen: [Microsoft](https://aka.ms/windowsappsdk/1.8/latest/windowsappruntimeinstall-x64.exe)

## MCP-Integration

Nova betreibt waehrend der Laufzeit einen lokalen MCP-Server. Externe Clients verbinden sich ueber:

```
%LOCALAPPDATA%\NovaBrowser\mcp.json
```

Diese Datei enthaelt Endpunkt und Bearer-Token. Als lokales Credential behandeln.

## Lokale Daten

Alle Daten liegen lokal unter `%LOCALAPPDATA%\NovaBrowser\` — Einstellungen, Browser-Profile, History, Favoriten, Vault, Logs, Wissensspeicher, Crawler-Datenbanken, Task-Workspaces und Gespraechsarchive.

Nova braucht keinen Cloud-Dienst. Bei Nutzung von Drittanbieter-KI-Providern gelten deren Datenregeln.

## Lizenz

Alle Rechte vorbehalten. Siehe [LICENSE](LICENSE).

Drittanbieter-Komponenten unterliegen eigenen Lizenzen. Siehe [THIRD-PARTY-LICENSES.txt](THIRD-PARTY-LICENSES.txt) im Release-Ordner.

## Kontakt

Joel Aniol — [LinkedIn](https://www.linkedin.com/in/joelaniol/)
