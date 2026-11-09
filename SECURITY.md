# Sicherheit und Paketprüfung

Dieses Repository enthält ausschließlich das separate KI-Auslieferungspaket, Dokumentation und Prüfwerkzeuge. Keine Shopsoftware, Zugangsdaten oder Entwicklungshistorie.

`sha256sum --check SHA256SUMS` prüft den heruntergeladenen Installer. `python3 tools/verify_release.py` prüft außerdem jedes eingebettete Modulfile, Pfade, Größen, Versionen und Hashwerte, ohne PHP auszuführen. `--extract <neuer-Ordner>` entpackt das geprüfte Modul zur Codeprüfung.

Das Repository ist privat. Für dieses Release gibt es keinen GitHub-Attestierungsnachweis. Prüfsummen prüfen die Übereinstimmung mit dem veröffentlichten Wert; sie ersetzen weder einen unabhängigen Herkunftsnachweis noch eine Sicherheitsprüfung.

Sicherheitsprobleme über die privaten Meldefunktionen des Repositorys melden. Keine API-Schlüssel oder Shopzugangsdaten in Issues einfügen.
