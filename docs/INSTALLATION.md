# Installation von c1zz-ki für Gambio

## Voraussetzungen und Sicherung

Aktives c1zz-blog ab 0.42.0, Gambio GX26 und PHP ab 8.2 mit cURL, OpenSSL und ZIP. Tatsächlich geprüft sind GX26.11.0, PHP 8.2.31, MariaDB 10.10 und Malibu. Der Shop benötigt ausgehendes HTTPS zum gewählten Anbieter.

Vor Installation oder Update Datenbank, Moduldateien und Blogmedien sichern. Bei vorhandenen KI-Zugängen außerdem die geschützte Datei `includes/c1zz_blogai_secret.php` erhalten: Datenbank und Schlüsseldatei gehören zusammen. Nicht vor einem Update deinstallieren, da die Deinstallation Anbieterzugänge entfernt.

## Paket prüfen und installieren

`SHA256SUMS` gehört zum PHP-Installer aus demselben Paket. Mit `sha256sum -c SHA256SUMS` prüfen; alternativ auf macOS `shasum -a 256 -c SHA256SUMS`. Die mitgelieferte Prüfung `python3 tools/verify_release.py` kontrolliert zusätzlich alle 32 eingebetteten Dateien, ohne PHP auszuführen. Eine Prüfsumme allein ist kein unabhängiger Herkunftsnachweis.

Nur `c1zz-ai-install-0.9.0.php` in den Shopordner neben `shop.php` und `admin/` hochladen. Der Installer enthält das ZIP bereits. Das übrige Release-Verzeichnis gehört nicht in den Webroot.

Installer im Browser öffnen, nativ als Admin anmelden und den Ablauf starten. Admin- und Modul-Center-Schreibrechte sind erforderlich. Bei Fehlern den betroffenen Schritt prüfen und fortsetzen. Nach erfolgreicher Abschlussprüfung entfernt sich der unveränderte Root-Installer. Updates erfolgen durch Hochladen des neuen Installers.

## Anbieter verbinden

Schlüssel im jeweiligen API-Konto erstellen:

- [OpenAI](https://platform.openai.com/api-keys)
- [Anthropic Console](https://platform.claude.com/settings/keys)
- [Google AI Studio](https://aistudio.google.com/apikey)

Im KI-Modul Schlüssel speichern und **Verbindung testen** wählen. Speichern allein sendet keine Anfrage. Der Test liest die Modellliste, erzeugt keine Inhalte und bestätigt weder Guthaben noch verbleibendes Kontingent. Eine Anthropic-Workspace-ID ist nur für entsprechende Schlüssel nötig.

Für ausschließlich kostenlose Gemini-Tests ein geeignetes Google-Free-Tier-Projekt ohne aktivierte Abrechnung verwenden. Das Modul erkennt den Projekttarif nicht. Kosten, Kontingente und Verfügbarkeit beim Anbieter prüfen.

Unter **Aktive Bereiche** den Blog aktivieren. Redaktionelle Funktionen liegen im Blog bei **Artikel → Neuer Artikel → KI-Assistent**. API-Zugang und Chat-Abonnement sind getrennte Angebote.

## Vorschläge und Entwürfe

Nur ausdrücklich ausgewählte Quellen werden übertragen. Bei Blogartikeln sind das Titel, Teaser, Kategorie und Bearbeitungsstatus, keine vollständigen Artikel oder Sicherungen. Die optionale Shopübersicht enthält Shopname, höchstens 20 aktive Produktkategorien und 12 Produktnamen; keine Kunden, Bestellungen oder Preise.

Vorschläge bleiben je Admin gespeichert. Eine Idee kann als Entwurfsthema übernommen werden. Neue Blogartikel werden ausschließlich als Entwurf gespeichert; Inhalt und Fakten vor der Veröffentlichung prüfen. Bei einem Fehler erfolgen keine automatische Wiederholung und kein automatischer Modellwechsel.

## Deinstallation und Wiederinstallation

Die Deinstallation ist über GX26s Modulverwaltung oder den eigenen Modulstatus erreichbar. Sie deaktiviert die Integration, entfernt Anbieterzugänge, technische Auftragsdaten und die eigene Schlüsseldatei. Blogartikel und Medien bleiben erhalten. Der persönliche Vorschlagsverlauf bleibt für eine Wiederinstallation gespeichert; er wird nicht automatisch gelöscht.

Der eigene Modulcode bleibt vorhanden. Wiederinstallation über den Modulstatus; danach neue API-Schlüssel hinterlegen. GX26 zeigt in seiner gewöhnlichen Modulliste nur installierte Module. Es gibt in diesem Teststand keine separate Löschfunktion für den gesamten Vorschlagsverlauf.

## Bilder über das Browserkonto

Im Artikeleditor bei **Titelbild → Bild beim Anbieter erstellen** Beschreibung und Bildstil prüfen. Sie übernehmen Titel, Kurzbeschreibung und Kategorie aus dem aktuellen Formular; weitere Auszüge kannst du selbst ergänzen. Mit „Beschreibung kopieren & Anbieter öffnen“ ChatGPT oder Gemini öffnen. Dort selbst anmelden, Text einfügen, Bild erzeugen und herunterladen. Danach den vorhandenen Bildupload verwenden.

Die Anbieterwahl benötigt einen erfolgreich geprüften OpenAI-/Gemini-Zugang und den aktivierten Blogbereich. Der Browser nutzt seine eigene Anmeldung, seinen Tarif und seine Limits. Das Modul löst keine Bild-API-Anfrage aus und übernimmt keine Bilder automatisch. Die Beschreibung bleibt beim Auf-/Zuklappen erhalten, wird aber nicht gespeichert. Gesperrte Zwischenablage: Text manuell kopieren; gesperrtes Popup: Anbieterlink verwenden. Bei Deaktivierung/Deinstallation entfällt auch die Bildhilfe; es gibt dafür keine zusätzlichen gespeicherten Zugangsdaten.
