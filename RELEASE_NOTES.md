# c1zz-ki für Gambio · 0.10.0-rc.1

Dieses Update behebt die Befunde des lokalen Audits und passt die Verwaltung an den gemeinsamen c1zz-Stil an.

- Das Schlüsselformular verwendet einen Feldnamen, den Gambios native Diagnose bereits vor dem Aufruf des Modulcontrollers maskiert. Schlüssel werden weiterhin nicht an den Browser zurückgegeben.
- Fehlgeschlagene Verbindungsprüfungen und andere Fehler erscheinen als rote Fehlermeldungen. Nicht eingerichtete Anbieter erhalten eine neutrale Darstellung.
- Eigenes Menüicon und gemeinsame Gestaltung mit dem Blogmodul.
- Die Bildhilfe bestätigt zuerst das Kopieren, bevor sie den Anbieter öffnet. Bei gesperrter Zwischenablage bleibt ein manueller Kopierweg verfügbar.
- Der Modulordner heißt jetzt `GXModules/c1zz/c1zzki`. Der Installer übernimmt `BlogAI`; unbekannte Dateien, Symlinks und doppelte Ordner blockieren die Übernahme.

**Zuerst Blog 0.45.0 installieren oder aktualisieren, danach KI 0.10.0.** Vorhandene Zugänge, geprüfte Verbindungszustände, Bereichseinstellungen und Themenideen bleiben beim Update erhalten. Keine automatischen Anbieteraufrufe beim Update.

Nur `c1zz-ai-install-0.10.0.php` in den Shopordner hochladen und den geführten Ablauf ausführen. Der Installer entfernt sich nach erfolgreichem Abschluss. [Installation](docs/INSTALLATION.md) · [Teststand](docs/TESTSTAND.md).
