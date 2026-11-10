# Installation von c1zz-ki für Gambio

## Voraussetzungen und Sicherung

Aktives c1zz-blog ab 0.45.0, Gambio GX26 und PHP ab 8.2 mit cURL, OpenSSL und ZIP. Tatsächlich geprüft sind GX26.11.0, PHP 8.2.31, MariaDB 10.10 und Malibu. Der Shop benötigt ausgehendes HTTPS zum gewählten Anbieter.

Vor Installation oder Update Datenbank, Moduldateien und Blogmedien sichern. Bei vorhandenen KI-Zugängen außerdem die geschützte Datei `includes/c1zz_blogai_secret.php` erhalten: Datenbank und Schlüsseldatei gehören zusammen. Nicht vor einem Update deinstallieren, da die Deinstallation Anbieterzugänge entfernt.

## Paket prüfen und installieren

`SHA256SUMS` gehört zum PHP-Installer aus demselben Paket. Mit `sha256sum -c SHA256SUMS` prüfen; alternativ auf macOS `shasum -a 256 -c SHA256SUMS`. Die mitgelieferte Prüfung `python3 tools/verify_release.py` kontrolliert zusätzlich alle 32 eingebetteten Dateien, ohne PHP auszuführen. Eine Prüfsumme allein ist kein unabhängiger Herkunftsnachweis.

Nur `c1zz-ai-install-0.12.1.php` in den Shopordner neben `shop.php` und `admin/` hochladen. Der Installer enthält das ZIP bereits. Das übrige Release-Verzeichnis gehört nicht in den Webroot.

Installer im Browser öffnen, nativ als Admin anmelden und den Ablauf starten. Admin- und Modul-Center-Schreibrechte sind erforderlich. Bei Fehlern den betroffenen Schritt prüfen und fortsetzen. Nach erfolgreicher Abschlussprüfung entfernt sich der unveränderte Root-Installer. Spätere Updates starten direkt unter Update / Aktualisieren.

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

## Übernahme der bisherigen Modulordner

Ab Blog 0.45.0 / KI 0.10.0 lauten die Ordner `GXModules/c1zz/c1zzblog` und `GXModules/c1zz/c1zzki`. Die Root-Installer übernehmen `StandaloneBlog` beziehungsweise `BlogAI`. Nicht manuell eine zweite Kopie daneben entpacken. Unbekannte Dateien, Symlinks und gleichzeitig vorhandene alte und neue Ordner blockieren den Vorgang. Zuerst Blog 0.45.0, danach KI 0.10.0 aktualisieren; währenddessen den KI-Assistenten nicht verwenden. Datenbanktabellen und Medien bleiben an ihren bisherigen Orten.

## Updates direkt in der Modulverwaltung

Nach der Erstinstallation unter **Update / Aktualisieren → Nach Updates suchen** die neue Version und ihre Hinweise prüfen, eine aktuelle Sicherung bestätigen und **Jetzt aktualisieren** wählen. Ein erneuter Root-Upload entfällt. Release Candidates erscheinen nur, wenn **Auch Testversionen anzeigen** ausgewählt ist. Ab diesem Stand ist die automatische Versionsprüfung nach der Adminanmeldung standardmäßig aktiv. Sie verwendet Gambios Menü-Erweiterungspunkte und einen gemeinsamen Cache je Modul: sechs Stunden bei Erfolg, 15 Minuten bei Fehlern. Unter **Update / Aktualisieren** lässt sie sich abschalten. Die Auswahl für Testversionen wird ebenfalls gespeichert; standardmäßig sind sie ausgeblendet. Ein Badge führt zu den Updatehinweisen; ein Ausrufezeichen kennzeichnet eine nicht bestätigte Prüfung. GitHub erhält die Server-IP und Abrufdaten, keine Artikel, Kunden- oder Zugangsdaten. Installationen starten ausschließlich nach deiner Bestätigung.

**Einmaliger Wechsel:** Ältere Blogstände bis 0.45.0 und KI-Stände bis 0.10.0 haben diesen Einstieg noch nicht. Einmal den neuen Root-Installer verwenden, um ihn einzurichten. Bei später gelöschten Modulordnern oder nicht erreichbarer Verwaltung bleibt der Root-Installer der Wiederherstellungsweg.

Jeder Schritt prüft native Admin-/Modul-Center-Rechte und Formularschutz. Downloads werden außerhalb des Webroots zwischengespeichert. Der heruntergeladene Installer wird als Datencontainer gelesen und niemals ausgeführt oder in den Shop-Root kopiert. HTTPS, feste GitHub-Quelle, Asset-Prüfsumme, Paketpfade und Dateihashes werden geprüft. **Eine kryptografische Herkunftssignatur wird im Shop noch nicht geprüft.** Der gesonderte [Herkunftsnachweis](../SECURITY.md) lässt sich außerhalb des Shops verifizieren.

Bei Fehlern stoppt die feste Fortschrittsanzeige. Nach erneutem Anmelden kann derselbe Lauf fortgesetzt werden. Vor der Dateiübernahme lässt sich die Vorbereitung verwerfen; danach ist die Wiederaufnahme vorgesehen. Es gibt kein automatisches Zurückrollen von Datenbankänderungen. Eine erfolgreiche native Wiederherstellung über den Root-Installer schließt einen passenden unterbrochenen Lauf ab.

Artikel, Medien, Einstellungen und KI-Zugänge bleiben beim Update erhalten. Lokale Änderungen, zusätzliche Dateien oder Symlinks im Modulordner blockieren die Übernahme. Beide Module teilen eine Updatesperre; zuerst den laufenden Vorgang abschließen. Das kleine, gegen HTTP-Zugriff geschützte Journal liegt unter `GXModules/c1zz/.c1zz-updates/`; erfolgreiche Downloads werden entfernt.

Für den Abruf braucht das Hosting PHP cURL und ZIP, ein privates PHP-Tempverzeichnis und ausgehendes HTTPS zu `api.github.com` und `release-assets.githubusercontent.com`. Es werden keine GitHub-Zugangsdaten benötigt. GitHub erhält die Server-IP und normale Abrufdaten, keine Artikel, Kunden- oder API-Zugangsdaten. Aktuell ist der neue Updateweg mit Gambio 26.11.0 geprüft.

## Vollständige Datenlöschung und Datenbankzustand

Blog und KI haben jeweils eine eigene, standardmäßig ausgeschaltete Löschbestätigung. Beim KI-Modul entfernt sie auch gespeicherte Themenvorschläge; beim Blog entfernt sie Bloginhalte und Medien. Beide entfernen ihre Update-Hinweiseinstellungen. Bereits in den Blog übernommene KI-Inhalte gehören zum Blog und werden durch die KI-Löschung erhalten. Ohne Löschhaken gilt weiterhin Datenerhalt, ausgenommen KI-Zugänge.

Auch nach vollständiger Datenlöschung ist die Shopdatenbank nicht bytegleich mit dem Zustand vor der Installation: Native inaktive Modulmarker, Cacheaufbau und fortgeschrittene Zähler bleiben. Modulcode und eigene redaktionelle Shopverknüpfungen werden nicht automatisch entfernt.
