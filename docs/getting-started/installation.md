# Installation & System Requirements

> [!IMPORTANT]
> **Upgrading from alpha.17 or earlier?** Those versions cannot detect alpha.18 automatically because the product name and updater changed. Download and run the [current setup](https://github.com/joelaniol/nova/releases) once manually. It updates your existing installation; automatic updates work again from alpha.18 onward.

Install Nova on Windows, then continue to your first task.

Deutsch: [weiter unten](#nova-ai-workspace-installieren).

---

## 1. Requirements

- **Windows 10 (version 1809 / build 17763 or newer) or Windows 11, x64.**
- An internet connection to download Nova, activate the license, and download WebView2 if it is missing.

You do not need to install .NET: Nova ships with its own runtime. The setup installs WebView2 and the Microsoft Visual C++ runtime if needed.

---

## 2. Download and Install

1. Open [Releases](https://github.com/joelaniol/nova/releases) and download the **Windows x64 setup (.exe)** under **Assets**. Its name ends in `-Setup-<version>.exe`. The `.mcpb` and `.sha256` attachments do not install Nova.
2. Run the setup. It asks for administrator rights because it installs for all users into
   `C:\Program Files\Nova AI Workspace`.
3. Follow the wizard. It creates a Start menu entry and, if you tick the box, a desktop shortcut.
   If WebView2 is missing, the setup downloads and installs it.

Once installed, Nova checks for new versions by itself and offers the update.

> [!NOTE]
> **Windows SmartScreen.** Alpha builds are signed with a certificate Windows does not know yet, so
> SmartScreen may show *"Windows protected your PC"* and *"Unknown publisher"*. Click
> **More info** → **Run anyway** to continue.

---

## Next Step

**[Your first five minutes with Nova](quickstart.md)** — open Nova, connect your AI program, restart it, and try a research task.

If installation or connection fails, use [Troubleshooting](../troubleshooting/README.md).

---

# Nova AI Workspace installieren

> [!IMPORTANT]
> **Upgrade von alpha.17 oder älter?** Diese Versionen erkennen alpha.18 wegen des Namens- und Updater-Wechsels nicht automatisch. Lade das [aktuelle Setup](https://github.com/joelaniol/nova/releases) einmal manuell herunter und führe es aus. Es aktualisiert die bestehende Installation; ab alpha.18 funktionieren automatische Updates wieder.

## Voraussetzungen

- Windows 10 ab Version 1809 oder Windows 11, 64 Bit (x64)
- Internetverbindung zum Herunterladen, zur Lizenzaktivierung und zum Nachladen von WebView2, falls es fehlt
- Microsoft-Edge-WebView2-Laufzeit: ist bei Windows 10/11 meist schon da, sonst installiert sie
  das Setup mit

.NET musst du nicht installieren, Nova bringt seine Laufzeit selbst mit.

## Installation

1. Unter [Releases](https://github.com/joelaniol/nova/releases) das **Windows-x64-Setup (.exe)** bei **Assets** herunterladen. Der Name endet auf `-Setup-<version>.exe`. Die Anhänge `.mcpb` und `.sha256` installieren Nova nicht.
2. Setup starten. Es fragt nach Administratorrechten, weil es für alle Nutzer nach
   `C:\Program Files\Nova AI Workspace` installiert.
3. Dem Assistenten folgen. Er legt einen Startmenü-Eintrag an und auf Wunsch eine
   Desktop-Verknüpfung. Fehlt WebView2, lädt das Setup es nach.

Meldet Windows SmartScreen „Der Computer wurde durch Windows geschützt“ bzw. „Unbekannter
Herausgeber“: auf **Weitere Informationen** → **Trotzdem ausführen** klicken. Das liegt am
Signaturzertifikat der Alpha-Versionen, das Windows noch nicht kennt.

Nach der Installation sucht Nova selbst nach neuen Versionen und bietet das Update an.

## Nächster Schritt

Weiter mit **[Your first five minutes with Nova (Englisch)](quickstart.md)**: Nova öffnen, KI-Programm verbinden, neu starten und eine Recherche ausprobieren.

Bei Problemen: [Fehlerbehebung (Englisch)](../troubleshooting/README.md).
