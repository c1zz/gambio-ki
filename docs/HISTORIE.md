# Release-Angebot und Versionshistorie

Seit dem 11. November 2026 steht in dieser Testphase nur das aktuelle geprüfte Release je Modul im öffentlichen Download- und Updateangebot. Ältere Releases und ihre angehängten Installer, Prüfsummen und Signaturdateien wurden entfernt. Das bedeutet nicht, dass jede ältere Version einen schweren Fehler enthielt: Auch abgelöste Teststände wurden aus dem Angebot genommen, damit die Auswahl eindeutig bleibt.

Tags und Commit-Historie bleiben unverändert. Frühere Dateien einschließlich damaliger Installer sind dadurch weiterhin über die Git-Historie einsehbar; die Bereinigung entfernt die Release-Downloads und ihre Einträge im Updateangebot. Alte Workflow-Läufe oder Tags dürfen nicht erneut zur Veröffentlichung zurückgezogener Pakete verwendet werden. Bereits veröffentlichte Pakete werden niemals unter derselben Versionsnummer mit anderen Bytes ersetzt.

Aktuelles Release: **[v0.12.7-rc.1](https://github.com/c1zz/gambio-ki/releases/tag/v0.12.7-rc.1)**. Es bleibt ein Release Candidate mit dokumentierten Prüfgrenzen. Für eine vorhandene Installation zuerst sichern und den aktuellen Updateweg aus der [Installationsanleitung](INSTALLATION.md) verwenden. Sehr alte Stände ohne integrierten Updater benötigen den aktuellen Root-Installer; bei beiden Modulen zuerst den Blog aktualisieren.

## Dokumentierte wichtige Korrekturen

| Frühere Version / Verhalten | Korrektur | Bedeutung |
|---|---|---|
| KI 0.9.0: Das Schlüsselfeld wurde vor dem Modulcontroller von der nativen Request-Diagnose nicht zuverlässig maskiert | [0.10.0](https://github.com/c1zz/gambio-ki/blob/v0.10.0-rc.1/RELEASE_NOTES.md) | Sicherheitsrelevante frühe Maskierung ergänzt. Bei aktivierter Request-Diagnose bzw. entsprechender Fehlerprotokollierung konnte der übermittelte Schlüssel im Diagnosedatensatz stehen. |
| KI 0.12.0: Normale Deinstallation erhielt die Ideenhistorie; ein bestätigter vollständiger Löschlauf fehlte im Deinstallationsdialog | [0.12.1](https://github.com/c1zz/gambio-ki/blob/v0.12.1-rc.1/RELEASE_NOTES.md) | Ausdrücklich bestätigte vollständige Bereinigung von Themenvorschlägen und Update-Einstellungen ergänzt. |

Diese konkret dokumentierten Befunde sind keine pauschale Aussage über jede historische Version. Die aktuelle Version enthält die Korrekturen. Historische Testergebnisse gelten nur für den dort genannten Prüfumfang; sie sind kein unabhängiges Codeaudit.

## Am 11. November 2026 aus dem Release-Angebot entfernt

Die Links führen zur erhaltenen Versionshistorie, nicht zu einem empfohlenen Installationspaket. Die damaligen Release-Beschreibungen sind zusätzlich als [historische Metadaten](release-history.json) archiviert; darin enthaltene Downloadhinweise sind überholt.

| Version | Ursprünglich veröffentlicht (UTC) | Status |
|---|---|---|
| [v0.12.2-rc.1](https://github.com/c1zz/gambio-ki/tree/v0.12.2-rc.1) | 2026-11-11 | Abgelöst; Release-Downloads entfernt |
| [v0.12.1-rc.1](https://github.com/c1zz/gambio-ki/tree/v0.12.1-rc.1) | 2026-11-10 | Abgelöst; Release-Downloads entfernt |
| [v0.12.0-rc.1](https://github.com/c1zz/gambio-ki/tree/v0.12.0-rc.1) | 2026-11-10 | Abgelöst; Release-Downloads entfernt |
| [v0.11.1-rc.1](https://github.com/c1zz/gambio-ki/tree/v0.11.1-rc.1) | 2026-11-10 | Abgelöst; Release-Downloads entfernt |
| [v0.11.0-rc.1](https://github.com/c1zz/gambio-ki/tree/v0.11.0-rc.1) | 2026-11-10 | Abgelöst; Release-Downloads entfernt |
| [v0.10.0-rc.1](https://github.com/c1zz/gambio-ki/tree/v0.10.0-rc.1) | 2026-11-10 | Abgelöst; Release-Downloads entfernt |
| [v0.9.0-rc.1](https://github.com/c1zz/gambio-ki/tree/v0.9.0-rc.1) | 2026-11-09 | Abgelöst; Release-Downloads entfernt |
| [v0.8.3-rc.1](https://github.com/c1zz/gambio-ki/tree/v0.8.3-rc.1) | 2026-11-09 | Abgelöst; Release-Downloads entfernt |
| [v0.8.2-rc.1](https://github.com/c1zz/gambio-ki/tree/v0.8.2-rc.1) | 2026-11-09 | Abgelöst; Release-Downloads entfernt |

Am 11. November 2026 wird auch **v0.12.3-rc.1** nach Veröffentlichung und Downloadprüfung des neuen Stands abgelöst. Seine Beschreibung ist in [release-history.json](release-history.json) gesichert; Tag und Commit bleiben erhalten.

Der Vorgänger **v0.12.6-rc.1** führte die responsive Bloggestaltung und den gemeinsamen Eingabestil ein. Dieses Release ergänzt die direkte Übernahme automatischer Updatefunde und die gemeinsame Kopfzeile. Der Vorgänger ist nicht pauschal als schwer fehlerhaft einzustufen; seine Beschreibung und Prüfsummen bleiben im historischen Bericht erhalten.
