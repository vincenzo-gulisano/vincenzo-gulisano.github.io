#!/usr/bin/env python3
"""Lightweight checks that do not require Jekyll to be installed."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
KNOWN_ROUTES = {
    "/",
    "/publications/",
    "/teaching/",
    "/theses-projects/",
    "/aboutme/",
    "/blog/",
    "/liebre/",
}


def content_files() -> list[Path]:
    return (
        sorted(ROOT.glob("*.md"))
        + sorted(ROOT.glob("_posts/*.md"))
        + sorted(ROOT.glob("docs/*.md"))
    )


def check_front_matter(errors: list[str]) -> None:
    for path in content_files():
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append(f"{path.relative_to(ROOT)}: missing front matter")
            continue
        end = text.find("\n---", 4)
        if end == -1:
            errors.append(f"{path.relative_to(ROOT)}: missing closing front matter")
            continue
        try:
            yaml.safe_load(text[4:end])
        except Exception as exc:  # pragma: no cover - diagnostic script
            errors.append(f"{path.relative_to(ROOT)}: YAML error: {exc}")


def route_exists(url: str) -> bool:
    clean = url.split("#", 1)[0].split("?", 1)[0]
    if clean in KNOWN_ROUTES:
        return True
    if clean.startswith("/20"):
        return True
    local = ROOT / clean.lstrip("/")
    if local.exists():
        return True
    if clean.endswith("/") and (ROOT / clean.strip("/") / "index.html").exists():
        return True
    return False


def check_local_links(errors: list[str]) -> None:
    attr_re = re.compile(r"""(?:href|src)=["']([^"']+)["']""")
    files = content_files() + sorted(ROOT.glob("_layouts/*.html"))
    for path in files:
        text = path.read_text(encoding="utf-8")
        for match in attr_re.finditer(text):
            url = match.group(1)
            if url.startswith(("http://", "https://", "mailto:", "#", "{{")):
                continue
            if url.startswith("/") and not route_exists(url):
                errors.append(f"{path.relative_to(ROOT)}: unresolved local URL {url}")


def main() -> int:
    errors: list[str] = []
    check_front_matter(errors)
    check_local_links(errors)
    if errors:
        print("\n".join(errors))
        return 1
    print("offline checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
