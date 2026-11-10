# c1zz-ki 0.12.1-rc.1

Der Deinstallationsdialog bietet jetzt eine **standardmäßig ausgeschaltete rote Checkbox** für die vollständige KI-Datenlöschung. Erst nach deiner ausdrücklichen Bestätigung werden auch gespeicherte Themenvorschläge und KI-Update-Einstellungen dauerhaft entfernt. Bereits übernommene Blogartikel und Kategorien bleiben erhalten.

Ohne Haken bleibt die Ideenhistorie wie bisher für eine Wiederinstallation erhalten. KI-Zugänge werden bei jeder Deinstallation entfernt. Nach Deaktivierung lässt sich die vollständige Bereinigung weiterhin über **Verbliebene KI-Daten entfernen** öffnen. Unterbrochene Löschschritte können fortgesetzt werden; Dateien und Datenbankstruktur sind nicht atomar löschbar.

Der vollständige Datenbankvergleich mit Blog **0.47.2** und der Browserlauf sind bestanden. Nach bestätigter vollständiger Löschung bleiben keine eigenen Modultabellen oder Update-Einstellungen zurück. Gambios inaktive Modulmarker, Sprachcache, fortgeschrittene Zähler und die Moduldateien bleiben bestehen. [Prüfumfang und Grenzen](docs/TESTSTAND.md).

Zum Testen **Update / Aktualisieren → Auch Testversionen anzeigen → Nach Updates suchen** öffnen und nach einer Sicherung **Jetzt aktualisieren** wählen. Ein Update löscht keine gespeicherten Inhalte. Keine neue Kompatibilitätszusage und kein unabhängiges Codeaudit; der Shop prüft weiterhin keine kryptografische Herkunftssignatur.
