# Teststand und Grenzen

**Blog 0.47.2-rc.1 / KI 0.12.1-rc.1**, 10. November 2026.

Im frischen **Gambio 26.11.0 / PHP 8.2.31 / MariaDB 10.10 / Malibu** unter `/shop/` wurden die exakten eingebetteten Moduldateien beider Installer geprüft: Installation, normale Deinstallation, Wiederinstallation und vollständige Datenlöschung. Dabei wurden Struktur und Inhalt aller Datenbanktabellen verglichen. Der neue KI-Löschablauf wurde zusätzlich mit Chromium und echten Ajax-Schritten geprüft. Isolierte PHP-Regressionen, 18 KI-Löschschutzprüfungen, 30 Blog-Lösch-/Routingprüfungen und zwei Builderprüfungen bestanden.

Nach vollständiger Löschung sind wieder alle **259 ursprünglichen Tabellen** vorhanden, ohne eigene Blog-/KI-Tabellen und ohne deren Update-Einstellungen. **Kein bytegleicher Datenbankzustand:** Gambios zwei inaktive Modulmarker, der neu aufgebaute Sprachcache und ein fortgeschrittener AUTO_INCREMENT-Zähler bleiben. Modulcode bleibt vorhanden. Keine ursprüngliche Tabellenstruktur oder sonstigen fachlichen Shopdaten wurden verändert.

Die normale Deinstallation erhält Blogdaten, Bilder und KI-Ideen weiterhin; KI-Zugänge werden dabei entfernt. Die Löschtests verwenden ausschließlich künstliche Daten in einer getrennten Prüfdatenbank. Originaler Migrationsbestand und Haupttestshop bleiben unverändert. Prüfdatenbank, Prüfbenutzer und temporäre Dateikopien wurden entfernt.

Geprüft wurden native Modulabläufe und die exakten Paketdateien. Kein neuer vollständiger GitHub-Updatetest im Shop und kein erneuter Root-Installer-Test in diesem Lauf. Vorherige Nachweise bleiben versionsbezogen. Keine zusätzliche Freigabe für andere Gambio-/PHP-/Theme-Versionen, kein unabhängiges Codeaudit. Der Shop prüft Paketintegrität, weiterhin keine kryptografische Herkunftssignatur. [Maschineller Prüfbericht](test-results.json).
