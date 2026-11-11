# Sicherheit und Paketprüfung

## Vertrauen vor Installation

Dieses öffentliche Repository enthält Auslieferung, Dokumentation und Prüfwerkzeuge. Das Entwicklungsrepository bleibt privat. Keine Shopsoftware, Shopzugänge, Datenbanksicherungen oder Kundenbestände werden mitgeliefert.

## Prüfsumme und Paketinhalt

Installer und `SHA256SUMS` aus demselben Release herunterladen. `sha256sum --check SHA256SUMS` prüft die vollständige Datei. `python3 tools/verify_release.py` prüft zudem das eingebettete Archiv, Versionen, Pfade, Größen und Datei-Hashes, ohne PHP auszuführen. `--extract <neuer-Ordner>` entpackt den Modulcode zur Prüfung.

Eine Prüfsumme bestätigt die Übereinstimmung mit dem Vergleichswert. Werden Paket und Vergleichswert gemeinsam ausgetauscht, ist sie kein unabhängiger Herkunftsnachweis.

## Kryptografischer Herkunftsnachweis

Der öffentliche Release-Workflow attestiert die **gesamte unveränderte PHP-Datei**, einschließlich eingebettetem Archiv. Die Signatur verwendet die kurzlebige GitHub-Actions-/Sigstore-Identität; kein privater Signaturschlüssel liegt im Repository. Das zugehörige Sigstore-Bundle gehört zu den Release-Assets.

```bash
gh attestation verify c1zz-ai-install-0.12.6.php --repo c1zz/gambio-ki --signer-workflow c1zz/gambio-ki/.github/workflows/release.yml
```

Repository, Workflow und Release-Tag/Commit im Prüfergebnis mit der erwarteten Veröffentlichung vergleichen. Die [GitHub-Anleitung](https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations) beschreibt die Verifikation. Für die [Offline-Prüfung](https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/verify-attestations-offline) werden zusätzlich passende Vertrauensdaten benötigt.

Der Nachweis bestätigt die Zuordnung zum Veröffentlichungsworkflow. Er ist **keine Identitätsprüfung einer natürlichen Person, kein unabhängiges Codeaudit und keine Fehlerfreiheitsgarantie**. Der Workflow prüft einen bereitgestellten Installer; er behauptet keinen unabhängigen Neuaufbau aus einem öffentlichen Entwicklungsrepository. Die vorherigen privaten Releases enthielten keinen solchen Nachweis; er wird ihnen nicht rückwirkend zugeschrieben.

## Prüfung im Shop

Die native Updatefunktion verwendet feste öffentliche GitHub-Endpunkte über HTTPS. Sie prüft den von GitHub gelieferten SHA-256-Asset-Digest, Manifest und enthaltene Dateien, native Rechte und CSRF. Ein Download wird niemals als Root-PHP ausgeführt. **Die Herkunftssignatur wird im Shop derzeit nicht kryptografisch geprüft**; die Oberfläche weist darauf hin. Es gibt keine GitHub-Tokenverwaltung und keine Übertragung von Artikeln, Kunden- oder KI-Zugangsdaten. GitHub erhält technisch die Server-IP und normale Abrufdaten.

## Sicherheitslücke melden

Sicherheitsprobleme über [GitHubs private Meldung](https://github.com/c1zz/gambio-ki/security/advisories/new) melden. Keine API-Schlüssel, Sitzungstokens oder Shopzugangsdaten in öffentliche Issues einfügen. Prüfumfang und bekannte Grenzen stehen im Testbericht; ein unabhängiger Penetrationstest wurde nicht durchgeführt.

## Zurückgezogene Testreleases

Ältere Releases wurden aus dem Download- und Updateangebot entfernt. [Versionshistorie und dokumentierte sicherheitsrelevante Korrekturen](docs/HISTORIE.md) bleiben nachvollziehbar; die Entfernung eines Releases löscht keine bereits heruntergeladenen Kopien.
