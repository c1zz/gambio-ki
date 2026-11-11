# c1zz-ki 0.12.2-rc.1

Der Admin-Menülink heißt jetzt **c1zz-ki**. Hinter der Versionsnummer im Modulkopf entfällt der Zusatz **Teststand**. Diese Veröffentlichung bleibt ein Release Candidate; die Kennzeichnung und Prüfgrenzen sind weiterhin in den Releaseinformationen sichtbar.

Das exakte eingebettete Paket wurde zusammen mit Blog 0.48.0 frisch auf **GX26.11.0 / PHP 8.2.31 / MariaDB 10.10 / Malibu** unter `/shop/` installiert. Version, Modulkopf und Menüdefinition wurden geprüft. Anschließend wurde der bestehende lokale Migrationstestshop mit dem exakten Root-Installer von 0.12.1 auf 0.12.2 aktualisiert; gespeicherte KI-Daten und die Konfiguration blieben erhalten. [Prüfumfang und Grenzen](docs/TESTSTAND.md).

Unter **Update / Aktualisieren → Auch Testversionen anzeigen → Nach Updates suchen** das Update nach einer Sicherung selbst starten. Keine Änderung an KI-Anbieteraufrufen oder Datenlöschung; keine neuen externen KI-Aufrufe, keine erneute vollständige GitHub-Update- oder Deinstallationsprüfung. Die Shopfunktion prüft Paketintegrität, keine kryptografische Herkunftssignatur. Kein unabhängiges Codeaudit.
