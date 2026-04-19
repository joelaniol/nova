# Nova Cognitive Browser

> **BETA SOFTWARE — USE AT YOUR OWN RISK**
>
> Nova Cognitive Browser is in active beta development. Bugs, crashes, data loss, and breaking changes
> may occur. There is no warranty of any kind. Do not rely on this software for critical tasks.
> By using Nova you accept the [Disclaimer](DISCLAIMER.md), [Acceptable Use Policy](ACCEPTABLE-USE.md), [Privacy Policy](PRIVACY.md), and the [License](LICENSE).
>
> **BETA-SOFTWARE — NUTZUNG AUF EIGENE GEFAHR**
>
> Nova Cognitive Browser befindet sich in aktiver Beta-Entwicklung. Fehler, Abstuerze, Datenverlust und
> Breaking Changes koennen auftreten. Es gibt keinerlei Gewaehrleistung. Verwende diese Software
> nicht fuer kritische Aufgaben. Mit der Nutzung akzeptierst du den
> [Haftungsausschluss](DISCLAIMER.md), die [Nutzungsrichtlinie](ACCEPTABLE-USE.md), die [Datenschutzerklaerung](PRIVACY.md) und die [Lizenz](LICENSE).

---

**The first autonomous AI agent framework with a real browser as its runtime.**

Nova is not a chatbot with a browser tab. It is a full agent operating system where AI models get a live Chromium desktop, persistent local memory, fully automated task scheduling, deep web exploration, and browser-enforced safety — all running locally on your machine.

Agents don't just respond. They plan, execute, learn, verify, and run on schedule — unattended, around the clock.

## Why Nova

- **Fully autonomous agent scheduling** — Define tasks once. Nova runs them on intervals, file triggers, chained workflows, or manual dispatch. No human babysitting required.
- **Real browser, real context** — Agents operate inside a full WebView2 desktop browser with tabs, sandboxes, sessions, cookies, proxy profiles, and browser identity. Not a headless scraper — a complete browsing environment.
- **Persistent local intelligence** — LCJ, ALP, PKS, OK, task memory, and operator notes give agents a growing local knowledge base. They learn verified website behavior, remember what worked, and adapt when sites change.
- **Deep autonomous exploration** — Website MCP discovery, hidden-WebView crawling, live-tab crawling for authenticated SPAs, Surface Explorer for UI states without URLs. Agents explore like a human would — but faster and more systematic.
- **Open agent protocol** — A localhost MCP server exposes 200+ browser and knowledge tools to Claude Code, Cursor, Windsurf, custom scripts, and any MCP-compatible client. Nova is the platform, not the model.
- **Multi-model, one workspace** — Claude, Codex, and Gemini run through the same agent panel with live transcript, tool cards, and seamless provider switching. Best model for each job.
- **Safety without handholding** — Domain rules, claims, audit logs, vault SecretRefs, emergency stop, kill switches, and strict MCP validation live in the browser runtime, not in a model prompt. Agents get guardrails, not a leash.

## Quick Start

1. Download the latest release from [Releases](https://github.com/joelaniol/nova/releases)
2. Extract the ZIP (portable) or run the installer
3. Run `NovaBrowser.exe`
4. Open Settings to configure language, sandboxes, AI provider accounts, MCP access, and agent permissions

> On first launch, Windows SmartScreen may warn that the app is not code-signed.
> For independent beta builds this is expected. Choose "More info" > "Run anyway".

## What Makes Nova Different

| | Traditional agent tools | Nova Cognitive Browser |
|---|---|---|
| **Browser** | Headless or screenshot-based | Full desktop Chromium with tabs, sessions, identity |
| **Autonomy** | Human triggers every action | Fully scheduled, chained, unattended execution |
| **Memory** | Stateless per session | Persistent local knowledge stores that grow over time |
| **Exploration** | Scripted selectors | Autonomous discovery, crawling, surface exploration |
| **Safety** | Prompt-based rules | Browser-enforced domain policy, claims, audit, kill switches |
| **Integration** | Closed ecosystem | Open MCP server — any client, any model |

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

Third-party components are subject to their own licenses. See [THIRD-PARTY-LICENSES.txt](THIRD-PARTY-LICENSES.txt).

## Videos

See Nova in action: [YouTube Channel](https://www.youtube.com/@novainweb)

Browse the full video index with thumbnails and direct links in [videos/](videos/).

## Links

- **Website:** [nova-cognitive.com](http://nova-cognitive.com/)
- **Releases:** [GitHub Releases](https://github.com/joelaniol/nova/releases)
- **YouTube:** [@novainweb](https://www.youtube.com/@novainweb)
- **Contact:** Joel Aniol — [LinkedIn](https://www.linkedin.com/in/joelaniol/)

---

# Nova Cognitive Browser (Deutsch)

**Das erste autonome KI-Agent-Framework mit einem echten Browser als Runtime.**

Nova ist kein Chatbot mit Browser-Tab. Es ist ein vollstaendiges Agent-Betriebssystem, in dem KI-Modelle einen Live-Chromium-Desktop, persistenten lokalen Speicher, vollautomatisches Task-Scheduling, tiefe Web-Exploration und browserseitige Sicherheit bekommen — alles lokal auf deinem Rechner.

Agenten antworten nicht nur. Sie planen, fuehren aus, lernen, verifizieren und laufen nach Zeitplan — unbeaufsichtigt, rund um die Uhr.

## Warum Nova

- **Vollautonomes Agent-Scheduling** — Tasks einmal definieren. Nova fuehrt sie nach Intervall, Datei-Trigger, verketteten Workflows oder manuellem Dispatch aus. Kein manuelles Babysitting noetig.
- **Echter Browser, echter Kontext** — Agenten arbeiten in einem vollstaendigen WebView2-Desktop-Browser mit Tabs, Sandboxes, Sessions, Cookies, Proxy-Profilen und Browser-Identitaet. Kein Headless-Scraper — eine komplette Browsing-Umgebung.
- **Persistente lokale Intelligenz** — LCJ, ALP, PKS, OK, Task Memory und Operator Notes geben Agenten eine wachsende lokale Wissensbasis. Sie lernen verifiziertes Website-Verhalten, merken sich was funktioniert hat und passen sich an wenn sich Seiten aendern.
- **Tiefe autonome Exploration** — Website-MCP-Discovery, Hidden-WebView-Crawling, Live-Tab-Crawling fuer authentifizierte SPAs, Surface Explorer fuer UI-Zustaende ohne URLs. Agenten erkunden wie ein Mensch — nur schneller und systematischer.
- **Offenes Agent-Protokoll** — Ein lokaler MCP-Server stellt 200+ Browser- und Wissens-Tools fuer Claude Code, Cursor, Windsurf, eigene Scripts und jeden MCP-kompatiblen Client bereit. Nova ist die Plattform, nicht das Modell.
- **Multi-Model, ein Workspace** — Claude, Codex und Gemini laufen im selben Agentenpanel mit Live-Transcript, Tool-Cards und nahtlosem Provider-Wechsel. Bestes Modell fuer jeden Job.
- **Sicherheit ohne Gaengelband** — Domain-Regeln, Claims, Audit-Logs, Vault SecretRefs, Emergency Stop, Kill-Switches und strikte MCP-Validierung leben in der Browser-Runtime, nicht in einem Model-Prompt. Agenten bekommen Leitplanken, keine Leine.

## Schnellstart

1. Neuestes Release von [Releases](https://github.com/joelaniol/nova/releases) herunterladen
2. ZIP entpacken (portabel) oder Installer ausfuehren
3. `NovaBrowser.exe` starten
4. In den Einstellungen Sprache, Sandboxes, KI-Provider-Konten, MCP-Zugriff und Agentenrechte konfigurieren

> Beim ersten Start kann Windows SmartScreen melden, dass die App nicht signiert ist. Bei Beta-Builds ist das erwartbar. "Weitere Informationen" > "Trotzdem ausfuehren".

## Was Nova anders macht

| | Traditionelle Agent-Tools | Nova Cognitive Browser |
|---|---|---|
| **Browser** | Headless oder Screenshot-basiert | Voller Desktop-Chromium mit Tabs, Sessions, Identitaet |
| **Autonomie** | Mensch triggert jede Aktion | Voll geplant, verkettet, unbeaufsichtigte Ausfuehrung |
| **Gedaechtnis** | Zustandslos pro Sitzung | Persistente lokale Wissensspeicher die mitwachsen |
| **Exploration** | Geskriptete Selektoren | Autonome Discovery, Crawling, Surface Exploration |
| **Sicherheit** | Prompt-basierte Regeln | Browser-erzwungene Domain-Policy, Claims, Audit, Kill-Switches |
| **Integration** | Geschlossenes Oekosystem | Offener MCP-Server — jeder Client, jedes Modell |

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

Drittanbieter-Komponenten unterliegen eigenen Lizenzen. Siehe [THIRD-PARTY-LICENSES.txt](THIRD-PARTY-LICENSES.txt).

## Videos

Nova in Aktion: [YouTube-Kanal](https://www.youtube.com/@novainweb)

Alle Videos mit Thumbnails und Direktlinks in [videos/](videos/).

## Links

- **Website:** [nova-cognitive.com](http://nova-cognitive.com/)
- **Releases:** [GitHub Releases](https://github.com/joelaniol/nova/releases)
- **YouTube:** [@novainweb](https://www.youtube.com/@novainweb)
- **Kontakt:** Joel Aniol — [LinkedIn](https://www.linkedin.com/in/joelaniol/)
