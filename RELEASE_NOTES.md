# c1zz-ki für Gambio · 0.9.0-rc.1

Blogbilder mit dem Browserkonto erstellen: Im Artikeleditor öffnet „Bild beim Anbieter erstellen“ eine bearbeitbare Bildbeschreibung aus Titel, Kurzbeschreibung und Kategorie.

- ChatGPT und Google Gemini werden bei erfolgreich geprüftem API-Zugang und aktiviertem Blogbereich angeboten.
- Illustration, Foto oder minimalistische Grafik wählen; Beschreibung und weitere Artikelauszüge selbst ergänzen.
- „Beschreibung kopieren & Anbieter öffnen“ öffnet die Anbieter-Webseite in einem getrennten Tab. Dort anmelden, Text einfügen, Bild erstellen und herunterladen; anschließend den bestehenden Blog-Bildupload nutzen.
- Keine Bild-API-Anfrage aus dem Modul. Browserkonto, Tarif und Limits gelten separat; API-Schlüssel melden nicht im Browser an.
- Bei blockierter Zwischenablage manuell kopieren, bei blockiertem Popup den Anbieterlink verwenden. Artikel und Medien bleiben unverändert; kein automatischer Import.
- Entwürfe, Vorschlagsverlauf und Anbieterzugänge bleiben beim Update erhalten.

Die Bilderstellung über diesen Browserweg wurde vom Nutzer bestätigt. Automatisierte Prüfungen simulieren Kopieren und Tabs; sie erzeugen keine Bilder beim Anbieter.

Modulstand und Installer: **0.9.0**. Voraussetzung: aktives c1zz-blog ab 0.42.0; gemeinsam geprüft mit **0.44.0**. Nur `c1zz-ai-install-0.9.0.php` hochladen und ohne vorherige Deinstallation aktualisieren. [Installation](docs/INSTALLATION.md) · [Teststand](docs/TESTSTAND.md) · [Bilderrundgang](docs/BILDERRUNDGANG.md).
