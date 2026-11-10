# c1zz-ki 0.12.0-rc.1

Nach der Adminanmeldung prüft das Modul im Hintergrund auf neue Versionen und zeigt einen kleinen Hinweis direkt am Gambio-Menülink. Ein bestätigtes Update erhält eine „1“, eine fehlgeschlagene Prüfung ein „!“. Der Badge öffnet **Update / Aktualisieren**; ein Update startet weiterhin ausschließlich nach deiner Bestätigung.

Die automatische Prüfung ist standardmäßig aktiv und abschaltbar. Ergebnisse werden je Modul und installiertem Stand für sechs Stunden zwischengespeichert; bei Fehlern erfolgt frühestens nach 15 Minuten ein neuer Versuch. Die Auswahl für Testversionen wird gespeichert und ist standardmäßig ausgeschaltet. „Nach Updates suchen“ prüft sofort. GitHub erhält die Server-IP und Abrufdaten, keine Artikel, Kundendaten oder Zugangsschlüssel.

Abgeschlossene Updates erscheinen kompakt mit aufklappbaren Details. Laufende oder fehlgeschlagene Abläufe bleiben deutlich sichtbar. Der Deinstallationsbereich hat einen klaren Abstand zu den normalen Aktionen.

## Selbst aktualisieren

Von 0.11.1 aus **Update / Aktualisieren** öffnen, **Auch Testversionen anzeigen** aktivieren und **Nach Updates suchen** wählen. Nach einer Sicherung **Jetzt aktualisieren** starten. Kein erneuter Root-Upload erforderlich. Erstinstallation und Wiederherstellung bleiben über den Root-Installer möglich. Die neuen automatischen Hinweise stehen nach Installation dieses Updates zur Verfügung.

Prüfumfang und Grenzen: [Teststand](docs/TESTSTAND.md). Keine neue Zusage für weitere Gambio-/PHP-/Theme-Versionen. Der Shop prüft HTTPS und Paketintegrität; die kryptografische Herkunftssignatur wird dort weiterhin nicht lokal verifiziert.
