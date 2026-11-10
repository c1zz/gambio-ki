#!/usr/bin/env python3
"""Inspect the complete release and embedded module without executing PHP."""
import argparse
import base64
import hashlib
import io
import json
from pathlib import Path
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'GXModules/c1zz/c1zzki/'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def verify_labels(root, release):
    tag = re.fullmatch(r'v(\d+\.\d+\.\d+)-(rc\.\d+)', release['tag'])
    require(tag and tag[1] == release['module_version'], 'Release tag/version mismatch')
    for name in ('README.md', 'RELEASE_NOTES.md', 'docs/BILDERRUNDGANG.md'):
        labels = re.findall(r'(?<![\w.])(?:v?\d+\.\d+\.\d+-)?rc\.\d+\b', (root / name).read_text())
        expected = {tag[2], tag[0], tag[0][1:]}
        require(labels and set(labels) <= expected, 'Release candidate labels differ: ' + name)


def inspect(root=ROOT):
    release = json.loads((root / 'release.json').read_text())
    verify_labels(root, release)
    name = release['installer']
    require(re.fullmatch(r'c1zz-ai-install-\d+\.\d+\.\d+\.php', name), 'Invalid installer filename')
    file = root / name
    require(not file.is_symlink() and file.is_file(), 'Installer must be a regular file')
    require(0 < file.stat().st_size <= 12 * 1024 * 1024, 'Unexpected installer size')
    raw = file.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    require(digest == release['sha256'] and len(raw) == release['bytes'], 'Complete installer checksum/size mismatch')
    require((root / 'SHA256SUMS').read_text() == digest + '  ' + name + '\n', 'SHA256SUMS differs from release metadata')
    encoded = re.findall(rb"json_decode\(base64_decode\('([A-Za-z0-9+/=]+)'\)", raw)
    payload = re.findall(rb"new C1zzAiArchiveInstaller\(\$root,\$package,base64_decode\('([A-Za-z0-9+/=]+)'", raw)
    require(len(encoded) == 1 and len(payload) == 1, 'Embedded archive/metadata missing or ambiguous')
    package = json.loads(base64.b64decode(encoded[0], validate=True))
    archive = base64.b64decode(payload[0], validate=True)
    require(package['version'] == release['module_version'] and package['installer'] == name, 'Embedded version/name mismatch')
    require(len(archive) <= 8 * 1024 * 1024 and hashlib.sha256(archive).hexdigest() == package['archive_sha256'], 'Archive checksum/size mismatch')
    require(0 < len(package['files']) <= 1000, 'Unexpected package file count')
    expected = {entry['path']: entry for entry in package['files']}
    require(len(expected) == len(package['files']) == release['package_files'], 'Duplicate or unexpected package files')
    require(sum(entry['bytes'] for entry in expected.values()) <= 16 * 1024 * 1024, 'Uncompressed package too large')
    contents = {}
    with zipfile.ZipFile(io.BytesIO(archive)) as zipped:
        require(len(zipped.infolist()) == len(expected), 'Archive entry count differs')
        seen = set()
        for entry in zipped.infolist():
            path = entry.filename
            require(path.startswith(PREFIX), 'Foreign archive path')
            relative = path[len(PREFIX):]
            require(re.fullmatch(r'(?:[a-zA-Z0-9_-][a-zA-Z0-9_.-]*/)*[a-zA-Z0-9_-][a-zA-Z0-9_.-]*', relative), 'Unsafe archive path')
            require(path.lower() not in seen, 'Duplicate or case-colliding archive path')
            seen.add(path.lower())
            require(path in expected and ((entry.external_attr >> 16) & 0o170000) != 0o120000, 'Unlisted file or symlink')
            info = expected[path]
            require(0 <= entry.file_size == info['bytes'] <= 10 * 1024 * 1024, 'Invalid file size')
            content = zipped.read(entry)
            require(hashlib.sha256(content).hexdigest() == info['sha256'], 'File checksum mismatch: ' + path)
            contents[path] = content
    receipt = contents[PREFIX + 'version_info.php'].decode('utf-8')
    native_version = re.search(r'^version:.*?(\d+\.\d+\.\d+)', receipt, re.M)
    require(native_version and native_version[1] == release['module_version'], 'GX26 version receipt differs')
    manifest = json.loads(contents[PREFIX + 'package-manifest.json'])
    require(manifest['version'] == release['module_version'], 'Module manifest version differs')
    require(manifest['files'] == [item for item in package['files'] if item['path'] != PREFIX + 'package-manifest.json'], 'Module manifest differs from installer files')
    return release, contents


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--extract', type=Path, help='Extract verified files into a new directory')
    args = parser.parse_args()
    release, contents = inspect()
    if args.extract:
        # mkdir without exist_ok prevents replacing an existing file, directory or symlink.
        args.extract.mkdir(mode=0o700, parents=False)
        for path, content in contents.items():
            output = args.extract / path
            output.parent.mkdir(parents=True, exist_ok=True)
            with output.open('xb') as file:
                file.write(content)
        print('Verified module extracted to:', args.extract)
    print('OK:', release['installer'], '—', len(contents), 'verified files; no PHP executed.')
    print('This checksum inspection checks consistency; it is not an independent proof of origin or a code audit.')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, KeyError, TypeError, zipfile.BadZipFile) as error:
        print('Verification failed:', error, file=sys.stderr)
        sys.exit(1)
