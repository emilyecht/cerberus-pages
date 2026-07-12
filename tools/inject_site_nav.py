#!/usr/bin/env python3
"""Inject a shared CERBERUS page switcher into deployed HTML files.

The source pages intentionally keep their page-specific layouts. During the Pages
build this script adds one accessible, fixed navigation surface to each major
interface so every page can reach every other page.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

NAV_START = "<!-- CERBERUS_GLOBAL_NAV_START -->"
NAV_END = "<!-- CERBERUS_GLOBAL_NAV_END -->"
CSS_LINK = '<link rel="stylesheet" href="site-nav.css">'

PAGES = {
    "index.html": "observatory",
    "scenarios.html": "incidents",
    "assurance-workbench.html": "workbench",
    "flight-kernel.html": "kernel",
}

ITEMS = (
    (
        "observatory",
        "index.html",
        "01",
        "Observatory",
        "Core model + FCOI",
    ),
    (
        "incidents",
        "scenarios.html",
        "02",
        "Incident Theatre",
        "Mission failure cases",
    ),
    (
        "workbench",
        "assurance-workbench.html",
        "03",
        "Assurance Workbench",
        "Policies + evidence",
    ),
    (
        "kernel",
        "flight-kernel.html",
        "04",
        "Flight Kernel",
        "Executable reference",
    ),
)


def navigation(current: str) -> str:
    links: list[str] = []
    for key, href, index, title, description in ITEMS:
        current_attr = ' aria-current="page"' if key == current else ""
        links.append(
            f'  <a href="{href}"{current_attr}>'
            f'<strong><span class="nav-index">{index}</span>{title}</strong>'
            f'<small>{description}</small></a>'
        )

    return "\n".join(
        (
            NAV_START,
            '<nav class="cerberus-page-nav" aria-label="CERBERUS page access">',
            *links,
            "</nav>",
            NAV_END,
        )
    )


def inject(path: Path, current: str) -> None:
    text = path.read_text(encoding="utf-8")

    if CSS_LINK not in text:
        if "</head>" not in text:
            raise ValueError(f"{path}: missing </head>")
        text = text.replace("</head>", f"{CSS_LINK}\n</head>", 1)

    nav = navigation(current)
    if NAV_START in text:
        pattern = re.compile(
            re.escape(NAV_START) + r".*?" + re.escape(NAV_END),
            flags=re.DOTALL,
        )
        text, count = pattern.subn(nav, text, count=1)
        if count != 1:
            raise ValueError(f"{path}: could not replace existing navigation")
    else:
        body = re.search(r"<body(?:\s[^>]*)?>", text, flags=re.IGNORECASE)
        if body is None:
            raise ValueError(f"{path}: missing <body>")
        insertion = body.end()
        text = text[:insertion] + "\n" + nav + text[insertion:]

    path.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Static-site root containing the CERBERUS HTML files",
    )
    args = parser.parse_args()
    root = Path(args.root).resolve()

    missing = [name for name in PAGES if not (root / name).is_file()]
    if missing:
        raise FileNotFoundError(
            "Missing required CERBERUS pages: " + ", ".join(sorted(missing))
        )

    for filename, current in PAGES.items():
        inject(root / filename, current)
        print(f"navigation injected: {filename} ({current})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
