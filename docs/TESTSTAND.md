# Teststand und Grenzen

Stand: 9. November 2026. Modulversion **0.8.2**. Der ausgelieferte Installer entspricht bytegenau dem bereits im Haupttestshop geprüften Paket.

## Echte Anbieteraufrufe

| Anbieter | Nachweis |
|---|---|
| OpenAI | Echte Themenvorschläge und Entwurfserstellung zuvor bestätigt; erzeugter Entwurf im Editor und in der Vorschau geprüft. |
| Gemini | Modelllistentest und Entwurfserstellung vom Nutzer bestätigt. Anschließend auch Themenideen, erhaltener Verlauf nach Neuladen und Übernahme einer Idee in einen Entwurf am 09.11.2026 ausdrücklich bestätigt. |
| Anthropic | Noch kein echter Anbieteraufruf nachgewiesen; Antworten und Fehlerfälle simuliert geprüft. |

Die Nutzerabnahme ist kein automatisierter Testbericht. Sie bestätigt auch nicht, dass Google einen bestimmten Aufruf kostenlos abgerechnet hat.

## Vorherige automatisierte Prüfung von 0.8.0

- **119 isolierte Anbieter- und Fehlerprüfungen:** feste Ziele und Header, kleines Gemini-Modell, Anfragebegrenzung, gültige Antworten, sichere Textausgabe, Schlüssel-/Berechtigungsfehler, Kontingent, Abbruch und blockierte Antworten. Keine echten Anbieteraufrufe.
- **187 native Prüfungen mit getrennten MariaDB-Testtabellen:** verschlüsselte Zugänge, native Blogentwürfe, Wiederholschutz, ausgewählte Quellen, dauerhaft gespeicherte Vorschläge, Besitzergrenzen und Datenbereinigung. Testtabellen danach entfernt.
- **15 Chromium-Prüfungen am lokalen Hauptshop:** tatsächliches Installer-Update, neue Anbieteranzeige, bisheriger OpenAI-Standard, Kostenhinweise, Gemini-Auswahl und Ideenübernahme. Gemini-Oberflächentests mit echtem Smarty-Template, künstlich aktivierten Anbietern und abgefangenen Testantworten.
- **Syntax und Paket:** 18 PHP-Dateien syntaktisch geprüft; alle 30 eingebetteten Dateien gegen das Manifest kontrolliert. 29 installierte Nutzdateien verifiziert.
- **Bestandserhalt beim Update:** 17 Tabellen und 161 Dateien einschließlich Blogdaten, Medien, gespeicherter Ideen und Zugangsdaten unverändert. Root-Installer nach Abschluss entfernt.

## Aktueller Release-Abgleich

**Aktuelle gemeinsame Abnahme bestanden:** 48 Ablaufprüfungen und 17 Chromium-Prüfungen im frischen GX26-Shop. Beide tatsächlichen Installer wurden nativ ausgeführt und anschließend entfernt. Native De-/Wiederinstallation erhält Blogartikel, Kategorien und Bilder sowie gespeicherte KI-Vorschläge; KI-Zugangsdaten werden bei Deinstallation entfernt. Keine hängende 95-Prozent-Anzeige.

**Update im Haupttestshop bestanden:** sechs Browserprüfungen, beide Installer abgeschlossen und entfernt, alle 180 installierten Nutzdateien geprüft. Inhalte, Medien, Sortiment und verschlüsselte KI-Zugänge unverändert; lediglich der installierte Blogversionswert und seine Paketbelege wurden aktualisiert. 100 PHP-Dateien einschließlich beider Installer syntaktisch geprüft. 119 Anbieter-/Fehlerprüfungen mit simulierten Antworten erneut bestanden. Keine echten KI-Aufrufe für diese Release-Abnahme.


0.8.2 ergänzt die kompakte Oberfläche und den gemeinsamen Stil. 19 gezielte Browserprüfungen für die kompakte Oberfläche mit 0.8.1 und 16 Stilprüfungen mit 0.8.2 bestanden. Rote Entfernen-Aktionen wurden zusätzlich lesend geprüft. Die Anbieterlogik wurde dabei nicht verändert.

Die aktuellen Ergebnisse der frischen Installation von Blog 0.43.0 und KI 0.8.2, der nativen De-/Wiederinstallation und des Bestandserhalts stehen in `test-results.json`. Nur künstliche Zugangsdaten werden dort verwendet; es werden keine kostenpflichtigen KI-Aufrufe ausgelöst. Die zusätzliche Umgebung wurde vollständig entfernt.

## Geltungsbereich

Geprüfte Kombination: **Gambio GX26.11.0, PHP 8.2.31, MariaDB 10.10, Malibu**. Keine pauschale Zusage für andere Shopversionen, PHP-Versionen oder Themes. Für dieses KI-Release liegt noch kein eigener Nachweis für Shop-Unterverzeichnisse vor.

Bilderzeugung, Webrecherche, Browser-Kontoanmeldung und eine externe Blog-REST-API sind nicht enthalten. Kategorien werden vorgeschlagen, nicht automatisch angelegt. Veröffentlichung bleibt eine gesonderte Aktion. Ein Modelllistentest garantiert keine spätere Generierungsberechtigung und kein verfügbares Kontingent.

Normale Deinstallation erhält redaktionelle Vorschläge und Bloginhalte, entfernt aber Anbieterzugänge. Es gibt noch keine eigene Funktion zum vollständigen Löschen des Vorschlagsverlaufs.
