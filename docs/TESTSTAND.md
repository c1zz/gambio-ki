# Teststand und Grenzen

**Blog 0.47.0-rc.1 / KI 0.12.0-rc.1**, 10. November 2026.

Die exakten Installer wurden in einem frisch installierten **Gambio 26.11.0 mit PHP 8.2.31, MariaDB 10.10 und Malibu** geprüft. Danach wurden Testcontainer, Datenbank-Volume, Netzwerke und Shopkopie entfernt. Der Haupttestshop bleibt auf dem vom Betreiber installierten Stand 0.46.1 / 0.11.1; dessen Updates führt er selbst aus.

- 19 native Prüfungen: frischer Shop, beide Root-Installer und ihre Entfernung, sämtliche ausgelieferten Dateiprüfsummen, echte automatische GitHub-Abfragen, erneuter Cacheabruf und verweigerter anonymer Zugriff.
- 29 native Chromiumprüfungen: modernes und älteres Adminlayout, beide Menübadges, keine Dopplungen, lesbare Darstellung, gespeicherte Einstellungen, Abschalten, Testversionsauswahl, Fehlerstatus und fehlender Fortschrittsblock ohne Updatelauf.
- 38 isolierte Fälle zur automatischen Versionsprüfung, 58 Rechte-/CSRF-/Statusprüfungen und 89 Updaterprüfungen. Die bestehenden isolierten Modulprüfungen, zwei Builderprüfungen und 79 Chromium-DOM-/Editorprüfungen bestanden ebenfalls.
- 22 Prüfungen der kompakten Erfolgsanzeige mit aufklappbaren Details, laufenden Schritten und Fehlerfortsetzung; zusätzlich 36 zuvor durchgeführte Abstandsprüfungen der Deinstallation. Diese UI-Prüfungen verwendeten temporäre Browserdarstellungen ohne Änderungen am Hauptshop.

Die erfolgreichen automatischen GitHub-Abfragen waren echt. Für reproduzierbare Browserprüfungen wurden anschließend ausschließlich die Cachezustände „Update verfügbar“, „Fehler“ und „aktuell“ im Wegwerfshop vorgegeben. Das belegt keine damalige Veröffentlichung einer zukünftigen Testversion. Paketdateien enthalten keine Testtransportlogik. Die zwei neuen Bilder der Updateverwaltung zeigen den abschließenden Cachezustand; die übrigen Funktionsbilder stammen vom Stand 0.46.1 / 0.11.1.

Keine erneute vollständige historische Update-/Wiederherstellungsmatrix und keine Erweiterung der Freigabe auf GX5, Honeygrid, PHP 8.3, MySQL 8.4 oder weitere Shopversionen. Unterverzeichnisse werden aus der Shopkonfiguration abgeleitet, waren in diesem Durchlauf aber kein neuer nativer Testfall. Kein unabhängiger Penetrationstest. Die Herkunftssignatur wird im Shop noch nicht kryptografisch geprüft.

[Maschinelle Ergebnisse und exakte Paketprüfsummen](test-results.json).
