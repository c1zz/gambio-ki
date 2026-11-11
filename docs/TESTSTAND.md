# Teststand und Grenzen

**Blog 0.48.16 / KI 0.12.7, jeweils rc.1**, 11. November 2026.

Die exakten Pakete wurden zusammen auf **Gambio 26.11.0 / PHP 8.2.31 / MariaDB 10.10 / Malibu** unter `/shop/` frisch installiert. 19 fokussierte Prüfungen bestätigten Paketdateien, native Verwaltung, gemeinsame Kopfzeile, Update-Seiten und die Aufnahme aller 21 Screenshots. Die separate Prüfdatenbank und das temporäre Dateisystem wurden anschließend entfernt; ursprüngliche Datenbank, Medien, Konfiguration und Hauptshopdateien blieben unverändert.

Anschließend bestanden **52 native Update-/Datenerhaltprüfungen** beim Update des Migrationsshops von Blog 0.48.15 / KI 0.12.6. Beide Root-Installer wurden nativ ausgeführt, Paketdateien und Abschlussstatus geprüft und Installer entfernt. Artikel, Entwürfe, Kategorien, Einstellungen, Medien und KI-Daten blieben erhalten.

Die vollständige isolierte PHP-Suite, PHP-Syntax, zwei Buildertests und 79 Chromiumprüfungen für Editor/DOM bestanden. Darunter 62 Prüfungen für automatische Hinweise/Cache, 30 für Update-Controller und gemeinsame Ergebnisse, 58 für Rechte/CSRF sowie 89 für Integrität, Lifecycle und Wiederaufnahme. Zehn zusätzliche Prüfungen mit echter Smarty-Bibliothek sowie die Kopfzeile bei 900/600/280 Pixeln wurden bereits am identischen funktionalen Entwicklungsstand geprüft. [Maschineller Bericht](test-results.json).

Die Screenshots verwenden die optionalen Beispielartikel und synthetische KI-Zugangs-/Ideenfixtures, keine echten Schlüssel oder Anbieteranfragen. Der angezeigte KI-Verbindungsstatus ist kein aktueller Anbietertest. In der abgeschotteten Testumgebung ist GitHub nicht erreichbar; die Update-Aufnahmen zeigen deshalb auch den korrekten Fehlerzustand. Die Cacheübernahme und Startfreigabe wurden mit kontrollierten Transportantworten isoliert geprüft.

Kein erneuter vollständiger GitHub-Updatelauf oder destruktiver Purge-Test. Keine Installation im Haupttestshop, keine Änderungen an Frankenwaldhanf. Andere Themes und Gambio-Versionen wurden für dieses Release nicht neu geprüft. Die bisherigen Darstellungs-/Wiederinstallationstests gelten als historische Ergebnisse, nicht als neue Tests dieses Pakets.

Die Shopfunktion prüft Integrität, noch keine kryptografische Herkunftssignatur. Workflow-Attestierung für den konkreten Download separat gegen Repository, Workflow, Tag und Commit prüfen. Kein unabhängiges Codeaudit.
