#!/usr/bin/env python3
"""Check that local links and assets in a built Jekyll site exist."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if name in {"href", "src"} and value:
                self.links.append(value)


def resolve_target(site_root: Path, page: Path, raw_url: str) -> Path | None:
    parsed = urlsplit(raw_url)
    if parsed.scheme or parsed.netloc or raw_url.startswith(("#", "mailto:", "tel:", "data:")):
        return None

    url_path = parsed.path
    if not url_path:
        return None

    if url_path == "/":
        target = site_root / "index.html"
    elif url_path.startswith("/"):
        target = site_root / url_path.lstrip("/")
    else:
        target = page.parent / url_path

    if url_path != "/" and url_path.endswith("/"):
        target /= "index.html"
    elif not target.suffix and not target.exists():
        target /= "index.html"

    return target.resolve()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("site_dir", type=Path)
    args = parser.parse_args()

    site_root = args.site_dir.resolve()
    errors: list[str] = []
    checked = 0

    for page in sorted(site_root.rglob("*.html")):
        link_parser = LinkParser()
        link_parser.feed(page.read_text(encoding="utf-8"))
        for raw_url in link_parser.links:
            target = resolve_target(site_root, page, raw_url)
            if target is None:
                continue
            checked += 1
            if site_root not in target.parents and target != site_root:
                errors.append(f"{page.relative_to(site_root)}: path escapes site: {raw_url}")
            elif not target.exists():
                errors.append(f"{page.relative_to(site_root)}: missing {raw_url}")

    if errors:
        print("\n".join(errors))
        return 1

    print(f"Checked {checked} local links and assets across the generated HTML.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
