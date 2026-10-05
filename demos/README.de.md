# Nova ausprobieren: Interaktive Browser-Demo

[English guide](README.md) · Die Demo-Oberfläche ist englisch.

Probiere acht Browser-Aufgaben mit Nova und deinem verbundenen KI-Agenten aus. Melde dich an, suche einen Eintrag, verschiebe eine Karte und arbeite mit Dateien und Seiteninhalten. Die Ergebnisse kannst du direkt auf der Seite prüfen.

Stand: 2026-10-05

## Loslegen

1. Lade das Repository über **Code → Download ZIP** herunter und entpacke es. Der Ordner `demos` und sein Unterordner `assets` müssen zusammenbleiben.
2. Öffne die heruntergeladene Datei `demos/lab.html` in Nova. Ein Webserver ist nicht nötig.
3. Verbinde deinen Agenten mithilfe der [Integrationsanleitung](../docs/integration/README.md) und stelle ihm eine Aufgabe. Du kannst die Steuerelemente auch selbst ausprobieren.

GitHub zeigt den HTML-Quelltext. Für die interaktive Seite musst du die Dateien herunterladen. Die Demo selbst stellt keine externen Netzwerkanfragen; dein Agent nutzt seinen konfigurierten Dienst.

## Eine erste Aufgabe

> Melde dich mit dem Benutzernamen **demo** und dem Passwort **nova** an. Finde Build 8472 in der langen Liste und verschiebe die Karte „Deploy release“ nach Done. Beschreibe, was sich auf der Seite geändert hat.

Prüfe den Anmeldestatus, den hervorgehobenen Build und die Karte in Done. Lade die Seite im selben Browserprofil neu und kontrolliere, ob die Demo-Anmeldung erhalten bleibt. Das ist eine lokale Simulation, kein echtes Konto.

## Weitere Aufgaben

| Bereich auf der Seite | Beispielaufgabe | Sichtbares Ergebnis |
| :--- | :--- | :--- |
| **Session** | „Melde dich an, lade neu und prüfe die Anmeldung auch auf der verlinkten zweiten Seite.“ | Der gespeicherte Demo-Anmeldestatus. |
| **Long list** | „Finde Build 8472.“ | Der hervorgehobene Eintrag in einer Liste mit 10.000 Einträgen. |
| **Embedded controls** | „Drücke den verschachtelten Button und sende DEMO-123 im eingebetteten Formular ab.“ | Button-Bestätigung und angezeigtes Ticket. |
| **Drag and drop** | „Verschiebe ‘Deploy release’ nach Done.“ | Die Karte in ihrer neuen Spalte; es wird nichts veröffentlicht. |
| **Files** | „Wähle die Beispieldatei, die ich dir gebe, und lade den Bericht herunter.“ | Dateiname und Größe auf der Seite sowie die CSV in den Downloads. |
| **Dialogs** | „Zeige den Cookie-Banner und lehne optionale Cookies ab. Öffne danach das Beispielmodal und schließe es ohne Speichern.“ | Die Demo-Auswahl und der Modalstatus. |
| **Waiting** | „Starte den verzögerten Button und drücke ihn, sobald er erscheint. Lade danach den Wert und nenne das Endergebnis.“ | Der gedrückte Button und der endgültige Wert statt des Platzhalters. |
| **Reading data** | „Fasse die Beispieltabelle zusammen und lies den gezeichneten Code.“ | Tabellenwerte und der visuell lesbare Code. |

Wähle zuerst den passenden Bereich. Toolnamen und Selektoren brauchst du für diese Aufgaben nicht.

## Ergebnisse einordnen

**Page activity** zeigt Ereignisse, die diese Demo verarbeitet hat. Prüfe dazu das sichtbare Ergebnis. Die Liste ist kein vollständiges Nova-Aktionsprotokoll und kein unabhängiger Nachweis für den Erfolg einer externen Aufgabe.

Die Demo zeigt kleine, lokale Interaktionsbeispiele, keinen Leistungsbenchmark. Anmeldung, Cookie-Auswahl und Board-Aktionen sind simuliert. Die Tabelle enthält fiktive Daten. Eine ausgewählte Datei wird nicht hochgeladen; der Download erzeugt eine CSV aus der Beispieltabelle. Das eingebettete Formular demonstriert keinen Zugriff auf eine fremde Website.

Die Anmeldung bleibt nur erhalten, soweit das Browserprofil lokalen Speicher bereitstellt. **Sign out** löscht sie. Ein Reload setzt die meisten anderen Interaktionen zurück; Anmeldung und zuletzt gewählter Bereich können gespeichert bleiben. **Back to top** und **Clear activity** setzen die jeweiligen Ansichten zurück. Verzögerte Inhalte erscheinen nach einigen Sekunden.

## Mehr erfahren

* [Nova herunterladen](../README.md)
* [Agenten verbinden](../docs/integration/README.md)
* [Core Features](../docs/core-features/README.md)
