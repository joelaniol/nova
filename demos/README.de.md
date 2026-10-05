# Nova ausprobieren: Der Experience Loop

[English guide](README.md) · Die Demo-Oberfläche ist englisch.

Die neue Hauptdemo zeigt wiederverwendbare Erfahrung: einen wiederkehrenden Hinweis, einen erneuten Besuch, eine veränderte Oberfläche und ein geprüftes Speicherergebnis. Acht kleinere Browser-Aufgaben bleiben zusätzlich verfügbar.

Stand: 2026-10-05

## Loslegen

Lade das Repository über **Code → Download ZIP** herunter und entpacke es. Für persistentes Website-Wissen brauchst du eine lokale HTTP-Adresse. Mit installiertem Python startest du im entpackten Repository:

```sh
python -m http.server 8765 --bind 127.0.0.1 --directory demos
```

Öffne `http://127.0.0.1:8765/lab.html` in Nova und [verbinde deinen Agenten](../docs/integration/README.md). Behalte Adresse und Port für weitere Besuche bei. Ctrl+C beendet den Server. Direktes Öffnen von `demos/lab.html` ermöglicht die Seiteninteraktionen, stellt aber keinen Website-Scope für diese Wissensübung bereit.

## Drei Besuche

1. **First visit:** Bitte den Agenten, den Hinweis zu schließen und den Entwurf zu speichern. Er soll das Ergebnis prüfen, dich bei Bedarf um Bestätigung bitten und den Bestätigungsbutton dir überlassen. Danach soll er die verifizierte Erfahrung zur Hinweisbehandlung in Nova speichern und ID sowie Lernstufe zeigen. Der erste Speicherversuch lässt den Entwurf absichtlich ungespeichert. Erst ein weiterer Versuch mit deiner Bestätigung und vollständigen Feldern erzeugt einen Beleg.
2. **Return visit:** Starte für einen deutlicheren Nachweis einen neuen Chat mit derselben Nova-Instanz und demselben Browserprofil. Bitte den Agenten, das gespeicherte Wissen abzurufen, seine Anwendbarkeit zu prüfen und es innerhalb der aktuellen Vertrauensgrenzen zu verwenden. Ein Erfolg macht Wissen nicht automatisch aktiv. Shadow-Wissen bleibt bewusst zu prüfen; keine Promotion für die Demo erzwingen.
3. **Site changed:** Bitte den Agenten, das alte Rezept vor der Anwendung gegen die neue Oberfläche zu revalidieren und Novas tatsächliche Antwort zu zeigen. Der Hinweis hat jetzt einen anderen Buttonselektor und eine andere Beschriftung. Ein verifiziertes Vorgehen muss die Änderung berücksichtigen. Automatische Reparatur oder Herabstufung darf er nur behaupten, wenn Nova das tatsächlich meldet.

Die gespeicherte Erfahrung betrifft den Hinweis und die Prüfung, dass der Entwurf wieder bedienbar ist. Deine Bestätigung gehört nicht in dieses Rezept. **I confirm this demo draft** ist eine Übergabeübung, kein Identitätsnachweis und keine technische Berechtigungsgrenze.

Nutze den tatsächlich beobachteten Schließbutton als Erkennungssignal. Prüfe nach der Änderung auch das Ziel der gespeicherten Aktion: Ein breiter Fingerprint kann noch einen Teil der Seite erkennen, obwohl die Aktion nicht mehr ausführbar ist.

## Was die Demo belegt

Die einzelnen Klicks und Formularaktionen lassen sich auch mit Playwright automatisieren. Nova soll hier den zusammenhängenden Ablauf zeigen: persistente Erfahrung außerhalb des Chats, explizite Vertrauensstufen, Revalidierung nach einer Änderung und Ergebnisprüfung mit einer Übergabe an den Menschen.

Verlange echte Nova-Antworten zu gespeichertem Wissen, Revalidierung und Ausführungsprüfung. Die Seitenzähler und **Page activity** sind nur Zustände dieser Beispielswebsite. Wenn Lernen deaktiviert oder nicht verfügbar ist, bleibt die Lernvorführung unvollständig. Es gibt keine garantierte Einsparung von Aufrufen oder Tokens.

**Reset page** setzt den aktuellen Seitenbesuch zurück, löscht aber kein Nova-Wissen. Alle Entwürfe sind simuliert; nichts wird veröffentlicht. Die Seite stellt keine externen Netzwerkanfragen, dein Agent nutzt seinen konfigurierten Dienst.

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
