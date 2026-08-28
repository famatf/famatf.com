#!/usr/bin/env python3
"""Create a double-clickable, offline preview ZIP from Jekyll output."""

from __future__ import annotations

import argparse
import re
import shutil
import tempfile
import zipfile
from pathlib import Path


ROOT_URL = re.compile(r"(?P<prefix>\b(?:href|src)=)(?P<quote>[\"'])(?P<url>/[^\"']*)(?P=quote)")


def make_portable(page: Path, bundle_root: Path) -> None:
    depth = len(page.relative_to(bundle_root).parents) - 1
    prefix = "../" * depth

    def replace(match: re.Match[str]) -> str:
        url = match.group("url")
        target = "index.html" if url == "/" else url.lstrip("/")
        return f"{match.group('prefix')}{match.group('quote')}{prefix}{target}{match.group('quote')}"

    page.write_text(ROOT_URL.sub(replace, page.read_text(encoding="utf-8")), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("site_dir", type=Path)
    parser.add_argument("output_zip", type=Path)
    args = parser.parse_args()

    source = args.site_dir.resolve()
    output = args.output_zip.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as temp_dir:
        bundle_root = Path(temp_dir) / "famatf.com-preview"
        shutil.copytree(source, bundle_root)

        for page in bundle_root.rglob("*.html"):
            make_portable(page, bundle_root)

        (bundle_root / "README.txt").write_text(
            "famatf.com Jekyll preview\n\n"
            "Open index.html in a browser. The theme, KaTeX scripts, and KaTeX fonts "
            "are included, so the preview works without a network connection.\n",
            encoding="utf-8",
        )

        with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for path in sorted(bundle_root.rglob("*")):
                if path.is_file():
                    archive.write(path, path.relative_to(bundle_root.parent))

    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
