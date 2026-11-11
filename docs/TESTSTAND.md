# Teststand und Grenzen

**KI 0.12.3-rc.1**, 11. November 2026.

Die exakten eingebetteten Pakete wurden frisch auf **Gambio 26.11.0 / PHP 8.2.31 / MariaDB 10.10 / Malibu** unter `/shop/` installiert. **15 fokussierte native Prüfungen** bestätigen Paketdateien und Versionen, leere und befüllte Kategorien, Artikel- und Bilderlisten, Versionsvorschau, KI-Verwaltung und öffentlichen Blog. Die separate Prüfdatenbank und temporären Dateien wurden danach entfernt; ursprüngliche Migrationsdatenbank, Medien und Konfiguration blieben unverändert.

Anschließend wurden die exakten Root-Installer im lokalen Migrationstestshop ausgeführt: Blog **0.48.3 → 0.48.4**, KI **0.12.2 → 0.12.3**. **35 Prüfungen** bestätigen Abschluss und Installerentfernung, Paketdateien sowie den Erhalt von Artikeln, Fassungen, Kategorien, Weiterleitungen, Medien, Darstellungswerten, KI-Daten und Konfigurationsdateien. **34 lesende Chromiumprüfungen** im aktualisierten Shop bei 1440/800 px bestätigen Tabellen, Buttons, Tastaturfokus und begrenzte Scrollbereiche. Die Kategorienliste wurde zusätzlich visuell kontrolliert.

Zuvor bestanden fünf Smarty-Kompilierungen und **32 Browserprüfungen** mit echten Tabellenfragmenten und Beispieldaten in einer temporären Vorschau, einschließlich Importvorschau. Zusätzlich bestanden zwei Buildertests und die Syntaxprüfungen beider fertigen Installer. [Maschineller Prüfbericht](test-results.json).

Der Haupttestshop wurde nicht aktualisiert. Kein erneuter vollständiger GitHub-Updatelauf, Deinstallationslauf oder Suchfunktionstest für diese Stilkorrektur; historische Suchtests sind unter [Blog 0.48.3](https://github.com/c1zz/gambio-blog/blob/v0.48.3-rc.1/docs/KOMPATIBILITAET.md), Löschtests unter [Blog 0.47.2 / KI 0.12.1](https://github.com/c1zz/gambio-blog/blob/v0.47.2-rc.1/docs/KOMPATIBILITAET.md) dokumentiert. Keine externen KI-Anbieteraufrufe und keine neuen Kompatibilitätszusagen für andere Themes oder Versionen.

Die Shopfunktion prüft Paketintegrität, keine kryptografische Herkunftssignatur. Kein unabhängiges Codeaudit.
