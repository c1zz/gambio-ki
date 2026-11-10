# Teststand und Grenzen

**Blog 0.45.0-rc.1 / KI 0.10.0-rc.1**, 10. November 2026.

Geprüfte Kombination: **Gambio GX26.11.0, PHP 8.2.31, MariaDB 10.10, Malibu**.

- Beide exakten Installer frisch installiert; 51 Ablauf- und 17 Browserprüfungen einschließlich De-/Wiederinstallation. Die temporäre Umgebung wurde vollständig entfernt.
- 353 native Blogprüfungen, 51 native Sicherheitsprüfungen und 187 native KI-Prüfungen mit getrennten Testtabellen und simulierten Anbietern bestanden.
- 9952 isolierte Blogprüfungen, 119 isolierte KI-Prüfungen, 79 isolierte Chromiumprüfungen und zwei Builderprüfungen bestanden. 99 PHP-Quelldateien und 18 JavaScript-Dateien syntaktisch geprüft.
- 8 Browserprüfungen des bestehenden Shopupdates sowie 6 Prüfungen der Auditkorrekturen, 14 des Kategorienmenüs und 32 der Bildhilfe bestanden.
- 19 Tabellen verglichen: ausschließlich der erwartete Blog-Paketversionswert geändert. Medien, echte KI-Zugänge und Einstellungen erhalten; 183 installierte Nutzdateien stimmen mit ihren Paketmanifesten überein. Die alten Modulordner sind entfernt.

Die native Rollenmatrix prüft die echten Zugriffswächter mit temporären Datenbankrollen, keine vollständige HTTP-Rollenmatrix. Externe Anbieter wurden nicht aufgerufen. Ein unabhängiger Penetrationstest liegt nicht vor. Es gibt keine neue Freigabe für GX5, Honeygrid, PHP 8.3 oder MySQL 8.4.

Die [maschinellen Ergebnisse](test-results.json) enthalten die Prüfumfänge und die SHA-256-Werte der tatsächlich getesteten Installer. Abbildungen im Bilderrundgang stammen teilweise aus früheren Versionen.
