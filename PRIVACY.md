# Privacy Policy / Datenschutzerklärung

*Last updated: July 2026*

---

## English

### Overview

Nova Cognitive Browser is designed to keep your data local. It does not collect usage analytics, does not track your browsing behavior, and does not build a behavioral profile of you. Nova only contacts its own server (`nova-cognitive.com`) for two purposes: **license activation and renewal** (required for the licensed app to run), and **optional, user-consented crash reports** after an unclean shutdown. Everything else stays on your machine.

### What Nova Does NOT Collect

- No browsing history is sent anywhere
- No usage analytics or telemetry during normal operation
- No behavioral tracking, browser/canvas fingerprinting, or usage profiling
- No automatic collection of your files, content, or activity
- No advertising identifiers

Note: license activation sends a small, defined set of data (including a hashed device identifier and your device name) so your license can be validated. This is described in full under "License Activation" below.

### License Activation

Nova is a licensed application. To activate your license and keep it valid, Nova contacts its own server at `nova-cognitive.com` over HTTPS. This happens when you activate a license and, afterwards, as an automatic background renewal while you use Nova (so your license lease stays current).

**What is sent during activation and renewal:**
- The **email address** and **license key** you entered
- A **device fingerprint hash** (SHA-256) derived from your Windows installation ID, Windows user SID, and Windows MachineGuid. The raw values are **never** sent — only the one-way hash. It is used solely to identify and count license seats (which device an activation belongs to), not to track you.
- Your **device name** (Windows hostname) in plain text, so you can recognize your own devices when managing activations
- Basic **environment info**: Windows edition and build, CPU architecture, and UI language

**Why this data is used:** to validate the license, enforce the number of allowed devices per license, and let you manage your own activations and deactivations. It is **not** used for advertising, cross-site tracking, or behavioral profiling.

**Where it is sent:**
- Endpoint: `nova-cognitive.com`
- Protocol: HTTPS (encrypted in transit)
- No third-party analytics services are involved

You can deactivate a device at any time, which removes that activation from the server.

### Crash Reports (Opt-In Only)

If Nova did not shut down cleanly (crash, forced termination, system failure), it will show a dialog on the next launch offering to send a crash report.

**This is entirely opt-in:**
- You see the full report content as a JSON preview before deciding
- You choose "Send" or "Don't send"
- If you choose "Don't send", nothing is transmitted
- No data is sent automatically or in the background

**What a crash report contains:**
- Nova version and display version
- Operating system version, edition, and build number
- Anonymous installation ID (randomly generated, not linked to any account or identity)
- Application log tail (last 200 lines of the previous run's log)
- Crash exception type and stack trace
- Application uptime at the time of crash
- Open tab URLs, active sandbox names, and recent agent activity context

**What a crash report does NOT contain:**
- No real names, email addresses, or account information
- No passwords, API keys, or authentication tokens
- No browsing history beyond the tabs open at crash time
- No file contents, downloads, or local documents
- No cookies or session data

**Automatic PII redaction:**
Before the report is shown to you and before it could be sent, Nova automatically redacts:
- Local file paths → `<redacted-path>`
- Email addresses → `<redacted-email>`
- Bearer tokens → `Bearer <redacted>`
- Authorization headers → `<redacted>`
- Cookie values → `<redacted>`
- URL query parameters are stripped (only scheme, host, and path are kept)

**Where crash reports are sent:**
- Endpoint: `nova-cognitive.com`
- Protocol: HTTPS (encrypted in transit)
- No third-party analytics services are involved
- Reports are used solely to diagnose and fix bugs

### Third-Party AI Providers

When you use AI features in Nova (Claude, Codex, Gemini), your prompts and interactions are sent to the respective AI provider's API. Nova does not control how these providers handle your data. Please refer to their individual privacy policies:

- Claude: https://www.anthropic.com/privacy
- Codex/ChatGPT: https://openai.com/policies/privacy-policy
- Gemini: https://ai.google.dev/gemini-api/terms

Nova does not send your AI conversations to nova-cognitive.com or any other Nova server.

### MCP Server

Nova's local MCP server runs on localhost only by default. When enabled, it allows MCP-compatible tools on your machine to interact with Nova. This is a local communication channel — no data is sent to external servers through the MCP server unless you explicitly configure remote access.

### Local Data Storage

All application data is stored locally on your machine:

```
%LOCALAPPDATA%\NovaBrowser\
```

This includes settings, browser profiles, history, favorites, vault entries, knowledge stores, conversation archives, logs, and task workspaces. You can delete this folder at any time to remove all Nova data. The uninstaller offers this option as well.

### Children

Nova Cognitive Browser is not directed at children under 13. We do not knowingly collect data from children.

### Contact

For privacy-related questions: [LinkedIn](https://www.linkedin.com/in/joelaniol/)

---

## Deutsch

### Überblick

Nova Cognitive Browser ist darauf ausgelegt, deine Daten lokal zu halten. Es werden keine Nutzungsanalysen gesammelt, dein Browserverhalten wird nicht getrackt und es wird kein Verhaltensprofil von dir erstellt. Nova kontaktiert seinen eigenen Server (`nova-cognitive.com`) nur für zwei Zwecke: **Lizenzaktivierung und -verlängerung** (erforderlich, damit die lizenzierte App läuft) und **optionale, von dir bestätigte Absturzberichte** nach einem unsauberen Beenden. Alles andere bleibt auf deinem Rechner.

### Was Nova NICHT sammelt

- Kein Browserverlauf wird irgendwohin gesendet
- Keine Nutzungsanalysen oder Telemetrie im Normalbetrieb
- Kein Verhaltens-Tracking, kein Browser-/Canvas-Fingerprinting, kein Nutzungsprofiling
- Keine automatische Erfassung deiner Dateien, Inhalte oder Aktivitäten
- Keine Werbe-Identifikatoren

Hinweis: Die Lizenzaktivierung sendet einen kleinen, klar definierten Datensatz (u.a. einen gehashten Geräte-Identifikator und deinen Gerätenamen), damit deine Lizenz validiert werden kann. Das ist unten unter „Lizenzaktivierung" vollständig beschrieben.

### Lizenzaktivierung

Nova ist eine lizenzierte Anwendung. Um deine Lizenz zu aktivieren und gültig zu halten, kontaktiert Nova seinen eigenen Server unter `nova-cognitive.com` über HTTPS. Das passiert bei der Aktivierung einer Lizenz und danach als automatische Hintergrund-Verlängerung, während du Nova nutzt (damit deine Lizenz-Lease aktuell bleibt).

**Was bei Aktivierung und Verlängerung gesendet wird:**
- Die von dir eingegebene **E-Mail-Adresse** und der **Lizenzschlüssel**
- Ein **Geräte-Fingerprint-Hash** (SHA-256), abgeleitet aus deiner Windows-Installations-ID, deiner Windows-Benutzer-SID und der Windows-MachineGuid. Die Rohwerte werden **nie** gesendet — nur der Einweg-Hash. Er dient ausschließlich dazu, Lizenzplätze zu identifizieren und zu zählen (welchem Gerät eine Aktivierung gehört), nicht um dich zu tracken.
- Dein **Gerätename** (Windows-Hostname) im Klartext, damit du deine eigenen Geräte bei der Verwaltung der Aktivierungen wiedererkennst
- Grundlegende **Umgebungsinfos**: Windows-Edition und -Build, CPU-Architektur und UI-Sprache

**Wozu diese Daten dienen:** um die Lizenz zu validieren, die Anzahl erlaubter Geräte pro Lizenz durchzusetzen und dir die Verwaltung deiner eigenen Aktivierungen/Deaktivierungen zu ermöglichen. Sie werden **nicht** für Werbung, seitenübergreifendes Tracking oder Verhaltensprofiling verwendet.

**Wohin es gesendet wird:**
- Endpunkt: `nova-cognitive.com`
- Protokoll: HTTPS (verschlüsselt bei der Übertragung)
- Keine Drittanbieter-Analysedienste sind beteiligt

Du kannst ein Gerät jederzeit deaktivieren, wodurch diese Aktivierung vom Server entfernt wird.

### Absturzberichte (nur auf Zustimmung)

Wenn Nova nicht sauber beendet wurde (Absturz, erzwungenes Beenden, Systemfehler), wird beim nächsten Start ein Dialog angezeigt, der das Senden eines Absturzberichts anbietet.

**Dies geschieht ausschließlich auf Zustimmung (Opt-in):**
- Du siehst den vollständigen Berichtsinhalt als JSON-Vorschau vor der Entscheidung
- Du wählst "Senden" oder "Nicht senden"
- Bei "Nicht senden" wird nichts übertragen
- Es werden keine Daten automatisch oder im Hintergrund gesendet

**Was ein Absturzbericht enthält:**
- Nova-Version und Anzeige-Version
- Betriebssystem-Version, Edition und Build-Nummer
- Anonyme Installations-ID (zufällig generiert, nicht mit einem Konto oder einer Identität verknüpft)
- Anwendungs-Log-Ende (letzte 200 Zeilen des vorherigen Programmlaufs)
- Absturz-Ausnahmetyp und Stack-Trace
- Anwendungslaufzeit zum Zeitpunkt des Absturzes
- Geöffnete Tab-URLs, aktive Sandbox-Namen und aktueller Agentenaktivitäts-Kontext

**Was ein Absturzbericht NICHT enthält:**
- Keine echten Namen, E-Mail-Adressen oder Kontoinformationen
- Keine Passwörter, API-Schlüssel oder Authentifizierungs-Tokens
- Keinen Browserverlauf über die zum Absturzzeitpunkt offenen Tabs hinaus
- Keine Dateiinhalte, Downloads oder lokale Dokumente
- Keine Cookies oder Sitzungsdaten

**Automatische PII-Schwärzung:**
Bevor der Bericht dir angezeigt wird und bevor er gesendet werden könnte, schwärzt Nova automatisch:
- Lokale Dateipfade → `<redacted-path>`
- E-Mail-Adressen → `<redacted-email>`
- Bearer-Tokens → `Bearer <redacted>`
- Autorisierungs-Header → `<redacted>`
- Cookie-Werte → `<redacted>`
- URL-Query-Parameter werden entfernt (nur Schema, Host und Pfad bleiben erhalten)

**Wohin Absturzberichte gesendet werden:**
- Endpunkt: `nova-cognitive.com`
- Protokoll: HTTPS (verschlüsselt bei der Übertragung)
- Keine Drittanbieter-Analysedienste sind beteiligt
- Berichte werden ausschließlich zur Diagnose und Behebung von Fehlern verwendet

### Drittanbieter-KI-Provider

Bei Nutzung der KI-Funktionen in Nova (Claude, Codex, Gemini) werden deine Eingaben und Interaktionen an die API des jeweiligen KI-Anbieters gesendet. Nova hat keinen Einfluss darauf, wie diese Anbieter deine Daten verarbeiten. Bitte beachte deren individuelle Datenschutzerklärungen:

- Claude: https://www.anthropic.com/privacy
- Codex/ChatGPT: https://openai.com/policies/privacy-policy
- Gemini: https://ai.google.dev/gemini-api/terms

Nova sendet deine KI-Konversationen nicht an nova-cognitive.com oder andere Nova-Server.

### MCP-Server

Novas lokaler MCP-Server läuft standardmäßig nur auf localhost. Wenn aktiviert, ermöglicht er MCP-kompatiblen Werkzeugen auf deinem Rechner die Interaktion mit Nova. Dies ist ein lokaler Kommunikationskanal — es werden keine Daten über den MCP-Server an externe Server gesendet, es sei denn, du konfigurierst ausdrücklich den Remote-Zugriff.

### Lokale Datenspeicherung

Alle Anwendungsdaten werden lokal auf deinem Rechner gespeichert:

```
%LOCALAPPDATA%\NovaBrowser\
```

Dies umfasst Einstellungen, Browser-Profile, Verlauf, Favoriten, Vault-Einträge, Wissensspeicher, Gesprächsarchive, Logs und Task-Workspaces. Du kannst diesen Ordner jederzeit löschen, um alle Nova-Daten zu entfernen. Der Deinstaller bietet diese Option ebenfalls an.

### Kinder

Nova Cognitive Browser richtet sich nicht an Kinder unter 13 Jahren. Es werden wissentlich keine Daten von Kindern erhoben.

### Kontakt

Für datenschutzbezogene Fragen: [LinkedIn](https://www.linkedin.com/in/joelaniol/)
