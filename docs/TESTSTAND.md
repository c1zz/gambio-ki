# Teststand und Grenzen

**KI 0.12.6-rc.1**, 11. November 2026.

Die finalen Pakete wurden zusammen auf **Gambio 26.11.0 / PHP 8.2.31 / MariaDB 10.10 / Malibu** unter `/shop/` geprüft. **22 fokussierte native Prüfungen** sind bestanden. Der frische Lauf verwendet die exakten eingebetteten Paketdateien und die native Modulvorbereitung in einer getrennten Prüfdatenbank. Er prüft leeren Blog, Modulverwaltung, Beispielinhalte, Speichern und Wiederladen der neuen Gerätewerte, öffentliche Breite und normale De-/Wiederinstallation mit erhaltenen Einstellungen. Originaldatenbank, Medien und Konfiguration wurden danach unverändert bestätigt; die temporäre Umgebung wurde entfernt.

Die Root-Installer wurden im lokalen Migrationsshop schrittweise nativ ausgeführt, einschließlich Dateiprüfung, Installerentfernung und Datenerhalt. Für Blog 0.48.14 bestanden 48 Update-/Datenerhaltprüfungen; der finale Stand 0.48.15 enthält zusätzlich den gezielten Widget-Fix und bestand anschließend ebenfalls **48 native Update-/Datenerhaltprüfungen**. KI 0.12.6 wurde bereits mit 0.48.10 nativ aktualisiert; der frische Lauf verwendet erneut exakt dieses Paket.

Die vollständige isolierte PHP-Suite, PHP-/JavaScript-Syntax, zwei Buildertests und 79 Chromiumtests für Editor/DOM sind bestanden. Die browsergestützte Entwicklungsprüfung umfasst unter anderem 48 Prüfungen der Blogbreite mit echtem Swiper, 34 der in Kategorien eingereihten Suche und 36 der Such-/Artikelgestaltung. Im nativen Admin bestanden zuletzt 25 Breitenprüfungen und 13 Suchpositionsprüfungen. Diese gezielten Tests liefen auf den jeweiligen Zwischenständen; der finale Widget-Fix ändert diese Oberflächen nicht. Prüfumfang und Paketprüfsummen stehen im [maschinellen Bericht](test-results.json).

Die vollständige Suite fand vor der Veröffentlichung unbeabsichtigt angebotene Seiten-/Suchoptionen im Widget-Generator. Diese sind in 0.48.15 ausgeschlossen; 1051 isolierte Widget-/Adressprüfungen bestanden. Ein erster Dateirechtetest wurde versehentlich als Container-root gestartet und danach erfolgreich als normaler Benutzer ausgeführt. Ein frischer Prüflauf wurde wegen eines falschen Controllerpfads im Prüfhelfer wiederholt. Diese Fehler werden nicht als erfolgreiche Läufe gezählt.

Kein erneuter vollständiger GitHub-Updatelauf oder destruktiver Purge-Test für diese Darstellungsänderungen. Keine externen KI-Anfragen, kein Update des Haupttestshops und keine Änderungen an Frankenwaldhanf. Andere Themes und Gambio-Versionen wurden für dieses Release nicht neu geprüft. Historische Ergebnisse sind keine pauschale Zusage für andere Versionen.

Die Shopfunktion prüft Paketintegrität, noch keine kryptografische Herkunftssignatur. Die Workflow-Attestierung muss für den konkreten Download gegen das erwartete Repository und den Workflow geprüft werden. Kein unabhängiges Codeaudit.
