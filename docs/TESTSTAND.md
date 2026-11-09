# Teststand und Grenzen

**KI 0.9.0-rc.1 / Blog 0.44.0-rc.1**

Geprüfte Kombination: **Gambio GX26.11.0, PHP 8.2.31, MariaDB 10.10, Malibu**. Stand: 9. November 2026.

## Aktuelle Releaseprüfung

- **47 Ablaufprüfungen und 17 Chromium-Prüfungen im frischen GX26-Shop:** beide exakten Installer, leere Neuinstallation, native Modulverwaltung, De-/Wiederinstallation mit Datenerhalt und Selbstentfernung der Root-Installer. Die einzige temporäre Umgebung einschließlich Datenbank-Volume und Netzwerk wurde entfernt. Der Hauptshop blieb dabei unverändert.
- **6 Browserprüfungen des Hauptshop-Updates:** beide Installer abgeschlossen und entfernt, beide Versionen korrekt in GX26, vorhandene geprüfte Anbieterzugänge erhalten.
- **11 Prüfungen der Artikelliste:** gemeinsamer Navigationseintrag, auffälliger Plus-Button links oberhalb der Suche, Statusmarkierungen, neuer/bestehender Editor, Papierkorb sowie 1440/900-Pixel-Ansichten.
- **25 Prüfungen der Bildhilfe:** ungespeicherte Artikeldaten, bearbeitete Beschreibung, Stilwechsel, ChatGPT/Gemini-Ziele, isolierter Tab, Kopier- und Popup-Ersatzwege, unverändertes Artikelformular und bestehender Upload. Kopieren und externe Tabs wurden simuliert; keine Anbieteraufrufe.
- **Bestandserhalt:** 17 geschützte Tabellen kontrolliert, ausschließlich der installierte Blogversionswert geändert. Inhalte, Sortiment, Medien, verschlüsselte KI-Zugänge und Vorschlagsverlauf erhalten. 11 geschützte Medien-/Shop-/Schlüsseldateien unverändert; alle 182 installierten Nutzdateien beider Module stimmen mit den Paketmanifesten überein.
- **Syntax und Paket:** 100 PHP-Dateien einschließlich beider fertigen Installer sowie 17 JavaScript-Dateien bestanden. Zwei isolierte Builderprüfungen bestanden, gemeinsamer Adminstil synchron. 152 eingebettete Blogdateien und 32 eingebettete KI-Dateien mit Pfad, Größe und SHA-256 kontrolliert.

Die tatsächliche Bilderstellung über den Browserweg hat der Nutzer bestätigt; der verwendete Anbieter wurde dabei nicht benannt. Die automatisierte Releaseabnahme erzeugt keine Bilder und tätigt keine echten KI-Anfragen. Details: [test-results.json](test-results.json).

## Frühere Nachweise

OpenAI-Entwürfe und Themenideen sowie Gemini-Modellliste, Entwürfe, Themenideen und gespeicherter Verlauf wurden bereits durch den Nutzer bestätigt. Anthropic ist weiterhin ausschließlich mit simulierten Antworten geprüft. Die 119 isolierten Anbieter-/Fehlerprüfungen (zuletzt 0.8.2), 187 nativen KI-Prüfungen (0.8.0) und 14 Vorschlagslistenprüfungen (0.8.3) sind frühere Nachweise, keine erneut ausgeführten Volltests dieses Releases.

## Grenzen

Keine pauschale Freigabe anderer Gambio-, PHP-, Datenbank- oder Theme-Versionen. Keine neue vollständige Prüfung in Shop-Unterverzeichnissen; für das KI-Modul liegt noch kein eigener Unterverzeichnisnachweis vor. Die GX4-Grundlage und frühere Firefox-/Chromium-Loginprüfungen sind historische Nachweise. Kein unabhängiges Sicherheitsaudit oder Gambio-Zertifikat.

Die Testdatenbank MariaDB 10.10 ist außer Wartung. Ein zusätzlicher Test mit MySQL 8.4 bleibt offen; keine Datenbankumstellung in diesem Release.

Die Bildhilfe erstellt lokal einen Text und öffnet die Anbieter-Webseite. Anmeldung, Einfügen, Bilderstellung und Download erfolgen dort manuell; anschließend wird der vorhandene Blogupload verwendet. Keine Bild-API, keine automatische Anmeldung im Modul, kein automatischer Import. Browserkonto und API-Konto haben getrennte Tarife und Limits. Ein erfolgreicher Modelllistentest bestätigt kein Guthaben.

Normale Deinstallation erhält Bloginhalte und gespeicherte Vorschläge; KI-Zugänge werden entfernt. Vollständige Blogdatenlöschung ist eine getrennte, ausdrücklich bestätigte Aktion. Eine eigene Löschfunktion für den gesamten KI-Vorschlagsverlauf fehlt weiterhin. Geplante Veröffentlichungen benötigen einen tatsächlich laufenden nativen Gambio-Aufgabenaufruf.
