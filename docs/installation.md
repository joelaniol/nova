# Installing Nova AI Workspace

Status: 2026-10-01 · Deutsche Fassung weiter unten.

## Requirements

- Windows 10 or Windows 11, 64-bit (x64)
- Administrator rights for the setup
- An internet connection during setup, unless Microsoft Edge WebView2 is already installed

The setup installs the two Microsoft runtimes Nova needs — **Microsoft Edge WebView2** and the
**Windows App Runtime 1.8** — by itself if they are missing.

## Install

1. Download `NovaAIWorkspace-Setup-<version>.exe` from [Releases](https://github.com/joelaniol/nova/releases).
2. Run it. Windows SmartScreen may warn about an unknown publisher — expected for independent alpha
   builds. Choose **More info → Run anyway**.
3. Enter the license. During the alpha a shared trial key is pre-filled; it is also listed in the
   [README](../README.md#try-it--3-minutes-no-sign-up).
4. Finish the setup. Nova is installed to `C:\Program Files\Nova AI Workspace` and starts as
   **Nova AI Workspace** from the Start menu.

## Connect your AI agent

### Easy setup (recommended)

On first start Nova opens its setup for AI programs by itself (the setup option
**Open the setup guide for AI programs on first start** makes sure of that).

1. **Let your AI use Nova** — switch on access.
2. **Your AI programs** — Nova lists the AI programs it found on your PC. Click **Connect** next to the
   one you want to use. Nova adds its connection — an entry named `nova` — and keeps it up to date.
   It does not touch your other MCP servers or your permission settings.
3. **Restart that AI program** so it reads the new connection. This is the step most often missed: if
   Nova does not show up, restart the AI program, not Nova.
4. Ask it: **"Can you use Nova?"** Once it finds Nova, tell it **"please run the Nova onboarding"** — it
   then learns what Nova can do.

Nova sets up Claude Code, Codex, Claude Desktop and Google Antigravity by itself. You can reopen the
setup any time under **Settings → Set up**.

### Set up manually

For an AI program Nova cannot set up by itself — or if you prefer to do it yourself:

1. In the setup, open **Connect another program** and click **Copy setup text**
   (also on **Settings → AI & agents → Connection & setup**).
2. Open your AI agent, for example in its terminal (CLI), and paste the text.
3. The agent sets up the connection itself. Restart it afterwards and continue with step 4 above.

Problems: see [MCP troubleshooting](mcp-troubleshooting/README.md).

## Updates

Nova checks for new versions by itself and tells you when one is available. It installs only after you
agree, and an update never restarts Windows.

## Uninstall

**Windows Settings → Apps → Installed apps → Nova AI Workspace → Uninstall.**

## If Nova does not start

- **Windows App Runtime missing** (for example blocked by a company policy): run
  `repair-windows-app-runtime.ps1` from Nova's install folder, or install it from
  [Microsoft](https://aka.ms/windowsappsdk/1.8/latest/windowsappruntimeinstall-x64.exe).
- **WebView2 missing** (no internet during setup): connect to the internet and start Nova again — it
  offers to finish installing the runtime. Manual download:
  [Microsoft WebView2](https://developer.microsoft.com/microsoft-edge/webview2/).

---

# Nova AI Workspace installieren

Stand: 2026-10-01

## Voraussetzungen

- Windows 10 oder Windows 11, 64 Bit (x64)
- Administratorrechte für das Setup
- Internetverbindung während des Setups, sofern Microsoft Edge WebView2 noch nicht installiert ist

Fehlen die beiden Microsoft-Laufzeiten, die Nova braucht — **Microsoft Edge WebView2** und die
**Windows App Runtime 1.8** —, installiert das Setup sie selbst.

## Installation

1. `NovaAIWorkspace-Setup-<Version>.exe` unter [Releases](https://github.com/joelaniol/nova/releases)
   herunterladen.
2. Ausführen. Windows SmartScreen warnt eventuell vor einem unbekannten Herausgeber — bei unabhängigen
   Alpha-Builds erwartet. **Weitere Informationen → Trotzdem ausführen** wählen.
3. Lizenz eingeben. Während der Alpha ist ein gemeinsamer Testschlüssel vorbelegt; er steht auch in der
   [README](../README.md#try-it--3-minutes-no-sign-up).
4. Setup abschließen. Nova liegt dann unter `C:\Program Files\Nova AI Workspace` und startet als
   **Nova AI Workspace** aus dem Startmenü.

## KI-Agent verbinden

### Einfach einrichten (empfohlen)

Beim ersten Start öffnet Nova seine Einrichtung für KI-Programme von selbst (dafür sorgt die
Setup-Option **Einrichtung für KI-Programme beim ersten Start öffnen**).

1. **Deine KI darf Nova bedienen** — Zugriff einschalten.
2. **Deine KI-Programme** — Nova zeigt die KI-Programme, die es auf deinem PC gefunden hat. Beim
   gewünschten Programm auf **Verbinden** klicken. Nova ergänzt dort seine Verbindung — einen Eintrag
   namens `nova` — und hält sie aktuell. Andere MCP-Server und deine Berechtigungseinstellungen fasst
   es nicht an.
3. **Das KI-Programm neu starten**, damit es die neue Verbindung liest. Das ist der am häufigsten
   vergessene Schritt: Taucht Nova nicht auf, das KI-Programm neu starten, nicht Nova.
4. Fragen: **„Kannst du Nova verwenden?“** Findet es Nova, sagen: **„please run the Nova onboarding“** —
   dann lernt es, was Nova kann.

Claude Code, Codex, Claude Desktop und Google Antigravity richtet Nova selbst ein. Die Einrichtung lässt
sich jederzeit unter **Einstellungen → Einrichten** erneut öffnen.

### Selbst einrichten

Für ein KI-Programm, das Nova nicht selbst einrichten kann — oder wenn du es lieber selbst machst:

1. In der Einrichtung **Anderes Programm verbinden** öffnen und **Einrichtungstext kopieren** klicken
   (auch unter **Einstellungen → KI & Agenten → Verbindung & Einrichtung**).
2. Deinen KI-Agenten öffnen, etwa in seinem Terminal (CLI), und den Text einfügen.
3. Der Agent richtet die Verbindung selbst ein. Danach neu starten und mit Schritt 4 oben weitermachen.

Probleme: siehe [MCP-Fehlerbehebung](mcp-troubleshooting/README.md#mcp-fehlerbehebung).

## Updates

Nova sucht selbst nach neuen Versionen und meldet, wenn eine bereitsteht. Installiert wird erst, wenn du
zustimmst, und ein Update startet Windows nie neu.

## Deinstallieren

**Windows-Einstellungen → Apps → Installierte Apps → Nova AI Workspace → Deinstallieren.**

## Wenn Nova nicht startet

- **Windows App Runtime fehlt** (etwa durch eine Unternehmensrichtlinie blockiert):
  `repair-windows-app-runtime.ps1` aus Novas Installationsordner ausführen oder die Laufzeit bei
  [Microsoft](https://aka.ms/windowsappsdk/1.8/latest/windowsappruntimeinstall-x64.exe) installieren.
- **WebView2 fehlt** (kein Internet während des Setups): Internetverbindung herstellen und Nova erneut
  starten — es bietet an, die Laufzeit fertig zu installieren. Manueller Download:
  [Microsoft WebView2](https://developer.microsoft.com/microsoft-edge/webview2/).
