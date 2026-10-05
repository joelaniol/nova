# Privacy Policy / Datenschutzerklärung

*Last updated: October 2026*

---

## English

### Overview

Nova AI Workspace is designed to keep your data local. It does not collect usage analytics, does not track your browsing behavior, and does not build a behavioral profile of you. Nova only contacts its own server (`nova-cognitive.com`) for two purposes: **license activation and renewal** (required for the licensed app to run), and **optional, user-consented crash reports** after an unclean shutdown. A few features also connect directly to other services; they are listed under "Connections to Other Services". Your browsing, files and Nova data stay on your machine.

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
- The **Nova version** you are running
- Whether Nova's **data folder** has already been moved to its current location (one of two fixed words, `current` or `legacy` — never a path or user name)

**Why this data is used:** to validate the license, enforce the number of allowed devices per license, and let you manage your own activations and deactivations. The Nova version and the data-folder state are also used to **plan updates**: they tell us when compatibility code for older installations can be removed without leaving anyone's data behind. It is **not** used for advertising, cross-site tracking, or behavioral profiling.

**Where it is sent:**
- Endpoint: `nova-cognitive.com`
- Protocol: HTTPS (encrypted in transit)
- No third-party analytics services are involved

You can deactivate a device at any time, which removes that activation from the server.

### Optional Address-Bar Diagnostics

If you enable developer options and host performance timings, Nova records technical address-bar measurements in its local application log to investigate delays and flicker. These include elapsed times, suggestion counts, text lengths, cursor and selection positions, popup changes and navigation events. This diagnostic trace does not record the addresses or search phrases you type. It is off by default and stops collecting when host performance timings are disabled.

These measurements are not automatically transmitted. If you choose to send a crash report, its application-log excerpt may include them, as described below.

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

### Connections to Other Services

Apart from the license and crash-report requests above, Nova itself contacts these services. Each of them receives your IP address and Nova's request, but nothing from your Nova profile:

- **Update check — GitHub** (`api.github.com`). Nova asks GitHub for its newest release, at most about once a day and when you click **Check for updates**. If you install an update, the setup file is downloaded from GitHub. On by default; turn it off in Settings → About with **Check for new versions automatically**.
- **Search suggestions — your search engine.** While you type in the address bar, Nova sends the typed text to your default search engine (Google unless you changed it; Bing or DuckDuckGo otherwise) to show search suggestions. If that engine returns none, Nova asks DuckDuckGo. On by default; turn it off in Settings with **Show search suggestions from the internet**.
- **Speech models — Hugging Face** (`huggingface.co`). Only when you or an agent installs an additional transcription model is it downloaded from there. The basic model ships with Nova.
- **Proxy check — ipify** (`api.ipify.org`). Only if you use a proxy: while it is active, Nova asks this service about every 30 seconds, and whenever you or an agent tests a proxy, which public IP address the proxy shows. The request goes through the proxy, so ipify sees the proxy's address.
- **WebView2 runtime — Microsoft.** Only if the browser engine is missing or damaged does Nova download it from Microsoft.

The websites you open in Nova are contacted by the browser engine as in any browser; that traffic is not covered by this list.

### Third-Party AI Providers

When you use AI features in Nova (Claude, Codex, Gemini), your prompts and interactions are sent to the respective AI provider's API. Nova does not control how these providers handle your data. Please refer to their individual privacy policies:

- Claude: https://www.anthropic.com/privacy
- Codex/ChatGPT: https://openai.com/policies/privacy-policy
- Gemini: https://ai.google.dev/gemini-api/terms

Nova does not send your AI conversations to nova-cognitive.com or any other Nova server.

### MCP Server

Nova's local MCP server runs on localhost only by default. When enabled, it allows MCP-compatible tools on your machine to interact with Nova. This is a local communication channel — no data is sent to external servers through the MCP server unless you explicitly configure remote access.

### Recorded Network Traffic

Nova can record the requests a page makes, including headers and bodies, and an agent can replay or
intercept them. This is off until you ask for it, and it changes nothing about where your data goes:

- **Nova does not store recorded traffic.** The recording lives in the page while the tab is open. No
  request, header or body is written to disk by this feature, and none of it is sent to
  `nova-cognitive.com`
- **The action log keeps metadata only** — which tool ran, on which host, whether it succeeded, how
  long it took and, if you switch that on, how many bytes the answer had. Never headers or bodies
- **What an agent receives, leaves your machine if that agent is a cloud service.** A recorded body
  handed to Claude, Codex or Gemini reaches that provider like any other part of the conversation —
  see "Third-Party AI Providers" above
- **`redact` masks credentials before an agent sees them** — tokens, cookies and credentials in URLs.
  Use it when the traffic is not yours to share
- **An interception rule is visible and temporary** — the toolbar shows it while it is armed, it is
  bound to one tab and a URL scope, and it expires on its own

### TLS Inspection

An agent can ask Nova to check a server's TLS certificate and configuration (`nova.tls_inspect`). This
runs only when an agent calls it:

- **Nova connects to the server the agent named**, over the same proxy route your browser uses, and
  reads what the server presents to every client. The result goes to that agent and is not stored
- **The optional subdomain lookup sends the domain name to crt.sh**, a public Certificate
  Transparency search operated by Sectigo. Only the domain is sent, nothing about you or your
  browsing. Nova asks crt.sh only when the agent requests this lookup explicitly
- **The action log keeps metadata only**, as for every other tool

### Local Data Storage

All application data is stored locally on your machine:

```
%LOCALAPPDATA%\nova-cognitive\Nova\
```

Installations up to version 1.0.0-alpha.17 used `%LOCALAPPDATA%\NovaBrowser\`. The setup of a newer version moves that folder to the new location; if the move is not possible, the data stays in the old folder.

This includes settings, browser profiles, history, favorites, vault entries, knowledge stores, conversation archives, logs, and task workspaces. You can delete this folder at any time to remove all Nova data. The uninstaller offers this option as well.

### Children

Nova AI Workspace is not directed at children under 13. We do not knowingly collect data from children.

### Contact

For privacy-related questions: [LinkedIn](https://www.linkedin.com/in/joelaniol/)

---

## Deutsch

### Überblick

Nova AI Workspace ist darauf ausgelegt, deine Daten lokal zu halten. Es werden keine Nutzungsanalysen gesammelt, dein Browserverhalten wird nicht getrackt und es wird kein Verhaltensprofil von dir erstellt. Nova kontaktiert seinen eigenen Server (`nova-cognitive.com`) nur für zwei Zwecke: **Lizenzaktivierung und -verlängerung** (erforderlich, damit die lizenzierte App läuft) und **optionale, von dir bestätigte Absturzberichte** nach einem unsauberen Beenden. Einige Funktionen verbinden sich außerdem direkt mit anderen Diensten; sie stehen unter „Verbindungen zu anderen Diensten“. Dein Surfen, deine Dateien und deine Nova-Daten bleiben auf deinem Rechner.

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
- Die **Nova-Version**, die du nutzt
- Ob Novas **Datenordner** schon an seinem aktuellen Ort liegt (eines von zwei festen Wörtern, `current` oder `legacy` — nie ein Pfad oder Benutzername)

**Wozu diese Daten dienen:** um die Lizenz zu validieren, die Anzahl erlaubter Geräte pro Lizenz durchzusetzen und dir die Verwaltung deiner eigenen Aktivierungen/Deaktivierungen zu ermöglichen. Nova-Version und Lage des Datenordners dienen außerdem der **Update-Planung**: Sie zeigen, wann Kompatibilitätscode für ältere Installationen entfernt werden kann, ohne dass jemandes Daten zurückbleiben. Sie werden **nicht** für Werbung, seitenübergreifendes Tracking oder Verhaltensprofiling verwendet.

**Wohin es gesendet wird:**
- Endpunkt: `nova-cognitive.com`
- Protokoll: HTTPS (verschlüsselt bei der Übertragung)
- Keine Drittanbieter-Analysedienste sind beteiligt

Du kannst ein Gerät jederzeit deaktivieren, wodurch diese Aktivierung vom Server entfernt wird.

### Optionale Adresszeilen-Diagnose

Wenn du Entwickleroptionen und Host-Performance-Zeiten aktivierst, protokolliert Nova technische Messwerte der Adresszeile im lokalen Anwendungslog, um Verzögerungen und Flackern zu untersuchen. Dazu gehören verstrichene Zeiten, Vorschlagszahlen, Textlängen, Cursor- und Auswahlpositionen, Popup-Wechsel und Navigationsereignisse. Diese Diagnose zeichnet die eingegebenen Adressen oder Suchphrasen nicht auf. Sie ist standardmäßig aus und erfasst keine weiteren Messwerte, sobald Host-Performance-Zeiten deaktiviert sind.

Diese Messwerte werden nicht automatisch übertragen. Wenn du einen Absturzbericht sendest, kann dessen Anwendungslog-Auszug sie enthalten, wie unten beschrieben.

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

### Verbindungen zu anderen Diensten

Neben den oben beschriebenen Anfragen für Lizenz und Absturzberichte kontaktiert Nova selbst diese Dienste. Jeder davon erhält deine IP-Adresse und die Anfrage von Nova, aber nichts aus deinem Nova-Profil:

- **Update-Prüfung — GitHub** (`api.github.com`). Nova fragt bei GitHub nach der neuesten Version, höchstens etwa einmal am Tag und wenn du auf **Nach Updates suchen** klickst. Installierst du ein Update, wird die Setup-Datei von GitHub geladen. Standardmäßig an; abschalten unter Einstellungen → Info mit **Automatisch nach neuen Versionen suchen**.
- **Suchvorschläge — deine Suchmaschine.** Während du in die Adressleiste tippst, sendet Nova den getippten Text an deine Standardsuchmaschine (Google, sofern du nichts anderes gewählt hast, sonst Bing oder DuckDuckGo), um Suchvorschläge anzuzeigen. Liefert diese keine, fragt Nova bei DuckDuckGo. Standardmäßig an; abschalten in den Einstellungen mit **Suchvorschläge aus dem Internet**.
- **Sprachmodelle — Hugging Face** (`huggingface.co`). Nur wenn du oder ein Agent ein zusätzliches Transkriptionsmodell installiert, wird es von dort geladen. Das Basismodell liefert Nova mit.
- **Proxy-Prüfung — ipify** (`api.ipify.org`). Nur wenn du einen Proxy nutzt: Solange er aktiv ist, fragt Nova diesen Dienst etwa alle 30 Sekunden, und bei jedem Test durch dich oder einen Agenten, welche öffentliche IP-Adresse der Proxy zeigt. Die Anfrage läuft über den Proxy, ipify sieht also dessen Adresse.
- **WebView2-Laufzeit — Microsoft.** Nur wenn die Browser-Engine fehlt oder beschädigt ist, lädt Nova sie von Microsoft.

Die Websites, die du in Nova öffnest, kontaktiert die Browser-Engine wie in jedem Browser; dieser Verkehr ist von dieser Liste nicht erfasst.

### Drittanbieter-KI-Provider

Bei Nutzung der KI-Funktionen in Nova (Claude, Codex, Gemini) werden deine Eingaben und Interaktionen an die API des jeweiligen KI-Anbieters gesendet. Nova hat keinen Einfluss darauf, wie diese Anbieter deine Daten verarbeiten. Bitte beachte deren individuelle Datenschutzerklärungen:

- Claude: https://www.anthropic.com/privacy
- Codex/ChatGPT: https://openai.com/policies/privacy-policy
- Gemini: https://ai.google.dev/gemini-api/terms

Nova sendet deine KI-Konversationen nicht an nova-cognitive.com oder andere Nova-Server.

### MCP-Server

Novas lokaler MCP-Server läuft standardmäßig nur auf localhost. Wenn aktiviert, ermöglicht er MCP-kompatiblen Werkzeugen auf deinem Rechner die Interaktion mit Nova. Dies ist ein lokaler Kommunikationskanal — es werden keine Daten über den MCP-Server an externe Server gesendet, es sei denn, du konfigurierst ausdrücklich den Remote-Zugriff.

### Aufgezeichneter Netzwerkverkehr

Nova kann die Anfragen einer Seite aufzeichnen, inklusive Header und Inhalte, und ein Agent kann sie
erneut senden oder abfangen. Das ist aus, bis du es verlangst, und es ändert nichts daran, wohin
deine Daten gehen:

- **Nova speichert aufgezeichneten Verkehr nicht.** Die Aufzeichnung lebt in der Seite, solange der
  Tab offen ist. Diese Funktion schreibt keine Anfrage, keinen Header und keinen Inhalt auf die
  Platte, und nichts davon geht an `nova-cognitive.com`
- **Das Aktionsprotokoll führt nur Metadaten** — welches Werkzeug lief, auf welchem Host, ob es
  erfolgreich war, wie lange es dauerte und, wenn du das einschaltest, wie viele Bytes die Antwort
  hatte. Niemals Header oder Inhalte
- **Was ein Agent bekommt, verlässt deinen Rechner, wenn dieser Agent ein Cloud-Dienst ist.** Ein
  aufgezeichneter Inhalt, den du Claude, Codex oder Gemini übergibst, erreicht diesen Anbieter wie
  jeder andere Teil des Gesprächs — siehe „Drittanbieter-KI-Provider" weiter oben
- **`redact` schwärzt Zugangsdaten, bevor ein Agent sie sieht** — Tokens, Cookies und Zugangsdaten in
  URLs. Nutze es, wenn der Verkehr nicht dir gehört
- **Eine Abfang-Regel ist sichtbar und vorübergehend** — die Symbolleiste zeigt sie, solange sie
  scharf ist, sie ist an einen Tab und einen URL-Bereich gebunden, und sie läuft von selbst ab

### TLS-Prüfung

Ein Agent kann Nova das TLS-Zertifikat und die TLS-Konfiguration eines Servers prüfen lassen
(`nova.tls_inspect`). Das läuft nur, wenn ein Agent es aufruft:

- **Nova verbindet sich mit dem Server, den der Agent nennt**, über denselben Proxy-Weg wie dein
  Browser, und liest, was der Server jedem Client zeigt. Das Ergebnis geht an diesen Agenten und
  wird nicht gespeichert
- **Die optionale Subdomain-Suche schickt den Domainnamen an crt.sh**, eine öffentliche Suche in den
  Certificate-Transparency-Logs, betrieben von Sectigo. Gesendet wird nur die Domain, nichts über
  dich oder dein Surfen. Nova fragt crt.sh nur, wenn der Agent diese Suche ausdrücklich anfordert
- **Das Aktionsprotokoll führt nur Metadaten**, wie bei jedem anderen Werkzeug

### Lokale Datenspeicherung

Alle Anwendungsdaten werden lokal auf deinem Rechner gespeichert:

```
%LOCALAPPDATA%\nova-cognitive\Nova\
```

Installationen bis Version 1.0.0-alpha.17 nutzten `%LOCALAPPDATA%\NovaBrowser\`. Das Setup einer neueren Version verschiebt diesen Ordner an den neuen Ort; ist das nicht möglich, bleiben die Daten im alten Ordner.

Dies umfasst Einstellungen, Browser-Profile, Verlauf, Favoriten, Vault-Einträge, Wissensspeicher, Gesprächsarchive, Logs und Task-Workspaces. Du kannst diesen Ordner jederzeit löschen, um alle Nova-Daten zu entfernen. Der Deinstaller bietet diese Option ebenfalls an.

### Kinder

Nova AI Workspace richtet sich nicht an Kinder unter 13 Jahren. Es werden wissentlich keine Daten von Kindern erhoben.

### Kontakt

Für datenschutzbezogene Fragen: [LinkedIn](https://www.linkedin.com/in/joelaniol/)
