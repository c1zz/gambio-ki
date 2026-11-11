# c1zz-ki 0.12.7-rc.1

Automatisch gefundene Updates erscheinen jetzt direkt mit Paketdetails und Startknopf auf **Update / Aktualisieren**. Eine zweite manuelle Suche ist nicht mehr nötig. Veraltete Details werden bei aktiver Automatik nachgeladen; „Erneut nach Updates suchen“ bleibt verfügbar.

Das **c1zz-systems-Logo steht links und der Modultitel rechts außen in derselben Kopfzeile**, auch in schmalen Ansichten. Die Screenshots im Bilderrundgang wurden mit diesen Paketständen erneuert.

Die Installation startet weiterhin ausschließlich nach ausdrücklicher Bestätigung und Sicherungshinweis. Rechte, CSRF, Paketprüfung und Datenerhalt bleiben erhalten. Keine neue KI-Anbieterfunktion und keine externen KI-Anfragen bei den Tests.

Geprüft auf **Gambio 26.11.0 / PHP 8.2.31 / MariaDB 10.10 / Malibu**: vollständige isolierte PHP-Suite, Cache-/Controller-/Sicherheitsprüfungen, PHP-Syntax, Buildertests, Chromium-Regression und frische Installation der exakten Pakete. Umfang und Grenzen stehen im verlinkten Testbericht.

Für dieses Update im bisherigen Modul **Update / Aktualisieren → Auch Testversionen anzeigen → Nach Updates suchen** verwenden und nach einer Sicherung selbst starten; zuerst den Blog aktualisieren. Die vereinfachte Bedienung greift nach Installation dieser Version. Die Shopfunktion prüft Integrität, noch keine kryptografische Herkunftssignatur. Der separate [Herkunftsnachweis](SECURITY.md) ersetzt kein unabhängiges Codeaudit.

[Prüfumfang und Grenzen](docs/TESTSTAND.md).
