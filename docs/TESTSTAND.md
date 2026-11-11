# Teststand und Grenzen

**KI 0.12.2-rc.1**, 11. November 2026.

Die exakten eingebetteten Pakete wurden frisch auf **Gambio 26.11.0 / PHP 8.2.31 / MariaDB 10.10 / Malibu** unter `/shop/` nativ installiert. 68 HTTP-/Datenprüfungen und 19 angemeldete Chromiumprüfungen bestanden: Suchtreffer und Vorschläge, Produktbestand, Ausschluss privater/alter/gelöschter Fassungen, Einstellungen speichern, Modul deaktivieren, native Tastaturbedienung, mobiles Enter, 390/768/1440 px und Ergebnisse ohne JavaScript. KI-Version, Modulkopf und Menüdefinition wurden ebenfalls geprüft.

Danach wurden die exakten Root-Installer im bestehenden lokalen Migrationstestshop ausgeführt (Blog 0.47.4 → 0.48.0, KI 0.12.1 → 0.12.2). 31 Prüfungen bestätigen Abschluss, Installerentfernung, sämtliche Paketdateien und die Suche im vorhandenen Artikelbestand. Inhalte, Fassungen, Kategorien, Weiterleitungen, Medien, gespeicherte Darstellung, KI-Daten und Konfigurationsdateien bleiben erhalten. Der Haupttestshop erhielt kein Update.

Die ursprüngliche Migrationsdatenbank, Medien und Konfiguration blieben während des frischen Prüflaufs unverändert; Prüfdatenbank, Prüfbenutzer und Overlay wurden entfernt. Beim anschließenden beauftragten Update ändern sich erwartungsgemäß Modulstand und native Laufzeit-/Cachedaten; keine pauschale Datenbankgleichheit behauptet.

Zusätzlich bestanden die isolierte PHP-Suite (einschließlich 33 Suchchecks), zwei Builderprüfungen, 79 isolierte Chromium-DOM-/Editorprüfungen und die Syntaxprüfung beider fertigen Installer. [Maschineller Prüfbericht](test-results.json).

Kein erneuter vollständiger GitHub-Update- oder Deinstallationslauf. Historischer Löschtest: [Blog 0.47.2 / KI 0.12.1](https://github.com/c1zz/gambio-blog/blob/v0.47.2-rc.1/docs/KOMPATIBILITAET.md). Keine neuen externen KI-Anbieteraufrufe. Die Suche liest veröffentlichte Fassungen stapelweise; noch kein Suchindex und kein Lasttest. Alternative Suchanbieter wie Findologic, andere Themes und andere Gambio-/PHP-Versionen sind für die Suche ungeprüft. Malibu blendet mobile Live-Vorschläge nativ aus.

Keine pauschale Kompatibilitätszusage und kein unabhängiges Codeaudit. Der Shop prüft Paketintegrität, weiterhin keine kryptografische Herkunftssignatur.
