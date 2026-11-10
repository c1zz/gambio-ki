# c1zz-ki 0.11.1-rc.1

Die Update-Seite zeigt jetzt die installierte Version und einen deutlichen Versionsstatus: noch nicht geprüft, aktuell für die geprüfte Auswahl, Update verfügbar oder Prüfung nicht bestätigt. Die letzte erfolgreiche Prüfung und die Berücksichtigung von Testversionen bleiben nachvollziehbar. Ergebnisse gelten höchstens 30 Minuten und für den geprüften Paketstand; bloßes Öffnen der Seite fragt GitHub weiterhin nicht ab.

## Selbst über die Modulverwaltung aktualisieren

Von KI 0.11.0 aus **Update / Aktualisieren** öffnen, **Auch Testversionen anzeigen** aktivieren und **Nach Updates suchen** wählen. Nach einer Sicherung **Jetzt aktualisieren** starten. Kein erneuter Root-Upload erforderlich. Der Root-Installer bleibt für Erstinstallation und Wiederherstellung verfügbar.

Prüfung mit Gambio 26.11.0, PHP 8.2.31, MariaDB 10.10 und Malibu: siehe [Teststand](docs/TESTSTAND.md). Keine neue Zusage für weitere Gambio-/PHP-/Theme-Versionen. Der Shop prüft HTTPS und Paketintegrität; die kryptografische Herkunftssignatur wird dort weiterhin nicht lokal verifiziert.
