#!/usr/bin/env python3
"""Validate the navigation injected into the generated CERBERUS site."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path

EXPECTED = {
    "index.html": "index.html",
    "scenarios.html": "scenarios.html",
    "assurance-workbench.html": "assurance-workbench.html",
    "flight-kernel.html": "flight-kernel.html",
}
ALL_HREFS = set(EXPECTED.values())


class NavParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_nav = False
        self.nav_count = 0
        self.links: list[tuple[str | None, str | None]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "nav" and "cerberus-page-nav" in (values.get("class") or "").split():
            self.in_nav = True
            self.nav_count += 1
        elif tag == "a" and self.in_nav:
            self.links.append((values.get("href"), values.get("aria-current")))

    def handle_endtag(self, tag: str) -> None:
        if tag == "nav" and self.in_nav:
            self.in_nav = False


def validate(path: Path, expected_current: str) -> None:
    text = path.read_text(encoding="utf-8")
    if text.count('href="site-nav.css"') != 1:
        raise AssertionError(f"{path}: expected one site-nav.css link")

    parser = NavParser()
    parser.feed(text)
    if parser.nav_count != 1:
        raise AssertionError(f"{path}: expected one global page nav, got {parser.nav_count}")

    hrefs = {href for href, _ in parser.links if href}
    if hrefs != ALL_HREFS:
        raise AssertionError(f"{path}: nav links differ: {sorted(hrefs)}")

    current = [href for href, aria in parser.links if aria == "page"]
    if current != [expected_current]:
        raise AssertionError(
            f"{path}: expected current page {expected_current!r}, got {current!r}"
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()

    for filename, expected_current in EXPECTED.items():
        validate(root / filename, expected_current)
        print(f"navigation valid: {filename}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
