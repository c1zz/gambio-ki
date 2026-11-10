# Teststand und Grenzen

**Blog 0.46.0-rc.1 / KI 0.11.0-rc.1**, 10. November 2026.

Geprüfte Kombination: **Gambio 26.11.0, PHP 8.2.31, MariaDB 10.10, Malibu**.

- Beide exakten Installer frisch installiert und anschließend über den neuen nativen Admin-Updateweg übernommen: 39 Ablaufprüfungen und 6 echte Chromiumprüfungen. Die einzige temporäre Umgebung wurde vollständig entfernt.
- Download-/Manifestprüfung, unveränderte Zielpakete, keine Root-Uploads beim Update, doppelte POST-Aufrufe, fremder Lauftoken, neue Anmeldung während des Updates und Wiederherstellung geprüft.
- Artikel, Bilder, Einstellungen, KI-Testzugang und Schlüsseldatei über Prüfsummen erhalten. Keine externen KI-Anfragen.
- 89 isolierte Updaterfälle, 42 isolierte Rechte-/CSRF-/Laufprüfungen, 9952 bisherige isolierte Blogprüfungen und 119 isolierte KI-Prüfungen bestanden.
- 79 bestehende Chromium-DOM-/Editorprüfungen und zwei Builderprüfungen bestanden. 107 PHP-Quelldateien, beide Installer und 20 JavaScript-Dateien syntaktisch geprüft.
- Im bestehenden GX26-Hauptshop beide neuen Installer über den nativen Browserablauf eingespielt: 8 Prüfungen bestanden. 19 Tabellen verglichen; ausschließlich der erwartete Blog-Paketversionswert änderte sich. Alle 11 geschützten Dateien und 195 ausgelieferten Nutzdateien geprüft.

Die GitHub-Antworten im frischen Shop waren ausschließlich in der temporären Vorgängerversion simuliert. Die tatsächlich übernommenen Zielpakete sind unverändert und enthalten keine Testtransportlogik. Dies ist kein Nachweis eines damaligen echten GitHub-Downloads. Die vorherige vollständige native Blog-/KI-Auditmatrix gehörte zu Blog 0.45.0 / KI 0.10.0; sie wurde für diese Ergänzung nicht als neuer Volltest ausgegeben.

Keine neue Freigabe für GX5, Honeygrid, PHP 8.3, MySQL 8.4 oder Unterverzeichnisinstallationen. Der neue Weg verwendet konfigurierte Shopverzeichnisse, wurde in diesem Durchlauf aber im Shop-Hauptverzeichnis geprüft. Kein unabhängiger Penetrationstest. Die Herkunftssignatur wird im Shop noch nicht kryptografisch geprüft.

[Maschinelle Ergebnisse und Paketprüfsummen](test-results.json). Die vorhandenen Screenshots zeigen weiterhin die jeweils im Bilderrundgang angegebenen älteren Oberflächenstände.

Nach der öffentlichen Freigabe: beide Installer mit dem echten Updater aus GX26 ohne GitHub-Zugangsdaten heruntergeladen und alle 197 Paketdateien geprüft, ohne Moduldateien zu verändern. Weitere 6 native Chromiumprüfungen bestätigen die echten GitHub-Abfragen beider Updatebereiche. Herkunftsnachweise mit der GitHub CLI gegen Repository, Workflow, Release-Tag und exakten Commit erfolgreich verifiziert. Veröffentlichte Assets stimmen mit den lokalen Prüfsummen überein; Vorgängerassets blieben unverändert.
