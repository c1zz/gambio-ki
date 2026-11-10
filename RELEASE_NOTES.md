# c1zz-ki 0.11.0-rc.1

Nach der Erstinstallation können neue Modulversionen direkt unter **Update / Aktualisieren** aus GitHub bezogen werden. Das erneute Kopieren einer PHP-Datei in den Shop-Root entfällt. Für den einmaligen Wechsel von älteren Ständen ohne Updatefunktion wird weiterhin der neue Root-Installer benötigt.

- Nach Updates suchen, Änderungen lesen, Sicherung bestätigen und ausdrücklich starten. Testversionen erscheinen nur nach bewusster Auswahl.
- HTTPS, feste GitHub-Quelle, GitHub-Asset-Prüfsumme, Paketinhalt und installierte Dateien prüfen. Heruntergeladene Installer werden nur als Datencontainer gelesen, nicht ausgeführt.
- Fortschritt bleibt bei Fehlern erhalten; eine neue Anmeldung kann den Lauf fortsetzen. Wiederholte erfolgreiche Schritte werden nicht erneut ausgeführt.
- Artikel, Medien, Einstellungen und KI-Zugänge erhalten. Lokale Moduländerungen und gleichzeitige c1zz-Updates blockieren die Übernahme.
- Erfolgreiche Wiederherstellung über den Root-Installer schließt unterbrochene Updatejournale ab. Kein automatisches Zurückrollen von Datenbankänderungen.
- Vertrauen vor Installation und hilfreiche Inhalte zur Unterstützung von Kaufentscheidungen als Produktleitlinien dokumentiert.

Geprüft in einem frischen **Gambio 26.11.0 mit PHP 8.2.31, MariaDB 10.10 und Malibu**: 39 native Ablaufprüfungen und 6 Chromiumprüfungen; 89 isolierte Updaterfälle und 42 isolierte Rechte-/CSRF-Prüfungen. Die vorhandenen isolierten Modul-, Builder- und Chromiumregressionen bestehen ebenfalls. GitHub-Antworten im frischen Shop waren simuliert; das Zielpaket entspricht exakt diesem Installer. Details: [Teststand](docs/TESTSTAND.md).

Der öffentliche Release-Workflow erstellt einen Herkunftsnachweis für die vollständige Installerdatei. **Im Shop wird diese Signatur noch nicht kryptografisch geprüft**; dort gelten HTTPS-Quellen- und Integritätsprüfungen. Ein unabhängiger Penetrationstest liegt nicht vor. Keine neue Freigabe für weitere Gambio-, PHP- oder Theme-Versionen.
