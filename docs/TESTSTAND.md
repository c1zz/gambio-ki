# Teststand und Grenzen

Stand: 9. November 2026. Modulversion **0.8.3**, Blog **0.43.0**. Geprüfte Kombination: **Gambio GX26.11.0, PHP 8.2.31, MariaDB 10.10, Malibu**.

## Aktuelle Releaseprüfung

- **47 Ablaufprüfungen und 17 Chromium-Prüfungen im frischen GX26-Shop:** exakte Installer, leere Neuinstallation, native Modulverwaltung, De-/Wiederinstallation mit Datenerhalt, Entfernung der Root-Installer und der KI-Zugänge bei Deinstallation. Nur künstliche Zugangsdaten; die temporäre Umgebung ist vollständig entfernt.
- **4 Browserprüfungen beim Update des Hauptshops:** KI-Installer 0.8.3 abgeschlossen und entfernt, Blogversionsanzeige unverändert, vorhandene geprüfte Anbieterzugänge und native Modulversionen korrekt.
- **14 gezielte Chromium-Prüfungen am installierten 0.8.3:** automatischer Wechsel zwischen zwei gespeicherten Vorschlagssätzen, vollständige Texte und Gliederung, Aufklappen, Übernahme in das Entwurfsformular, Reload sowie 900/600-Pixel-Ansichten ohne eigenen Scrollbereich.
- **Bestandserhalt:** Fingerprints von 17 Tabellen und 161 geschützten Dateien vor/nach Update unverändert. Einschließlich Artikeln, Medien, Sortiment, gespeicherten Vorschlägen und verschlüsselten KI-Zugängen. Alle 180 Nutzdateien beider Module gegen ihre Manifeste geprüft.
- **Syntax und Paket:** 19 PHP-Dateien einschließlich des ausgelieferten Installers syntaktisch geprüft. JavaScript-Syntax und alle 30 eingebetteten Paketdateien geprüft. Gemeinsamer Adminstil synchron.
- **Abbildungen:** fünf aktuelle Ansichten; illustrative redaktionelle Texte ausschließlich in der Browseransicht ersetzt. Keine Speicherung und keine KI-Anfrage.

Diese Releaseprüfung hat **keine echten Anbieteraufrufe** ausgelöst. Die Anbieterlogik wurde nicht geändert. Die detaillierten aktuellen Ergebnisse stehen in [test-results.json](test-results.json).

## Frühere Nachweise

OpenAI: echte Entwürfe und Themenideen bereits bestätigt. Gemini: Modelllistentest, Entwürfe, Themenideen, Verlauf nach Reload und Themenübernahme am 09.11.2026 durch den Nutzer bestätigt. Anthropic: weiterhin nur simulierte Antworten und Fehlerfälle.

119 isolierte Anbieter-/Fehlerprüfungen wurden zuletzt für 0.8.2 erneut ausgeführt. 187 native Prüfungen mit getrennten Testtabellen stammen aus 0.8.0. Diese früheren Ergebnisse sind keine erneut ausgeführten Tests von 0.8.3.

## Grenzen

Keine pauschale Freigabe anderer Shop-, PHP-, Datenbank- oder Theme-Versionen. Für das KI-Modul liegt noch kein eigener Nachweis für Shop-Unterverzeichnisse vor.

Die verwendete MariaDB 10.10 wird seit November 2023 nicht mehr gewartet. GX26.11.0 nennt offiziell weiterhin MariaDB bis 10.10 bzw. MySQL bis 8.4. Ein zusätzlicher Test mit MySQL 8.4 ist offen; die Testdatenbank wurde nicht umgestellt. [MariaDB-Wartungsstand](https://mariadb.com/docs/release-notes/community-server/old-releases/10.10/what-is-mariadb-1010), [Gambio-Systemvoraussetzungen](https://developers.gambio.de/release-notes/26.11.0/).

Bilderzeugung, Webrecherche, Browser-Kontoanmeldung und externe Blog-REST-API sind nicht enthalten. Kategorien werden vorgeschlagen, nicht automatisch angelegt. Veröffentlichung bleibt eine gesonderte Aktion. Ein Modelllistentest garantiert kein Guthaben oder Kontingent. Gemini ist nur im verfügbaren Free Tier kostenlos; eine bestätigte Texterstellung ist kein Abrechnungsnachweis.

Normale Deinstallation erhält Vorschläge und Bloginhalte, entfernt aber Anbieterzugänge. Eine eigene Funktion zum vollständigen Löschen des Vorschlagsverlaufs fehlt weiterhin.
