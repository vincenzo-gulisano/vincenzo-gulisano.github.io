#!/usr/bin/env python3
"""Import the WordPress export into static Jekyll pages."""

from __future__ import annotations

import datetime as dt
import html
import json
import re
import shutil
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
EXPORT = ROOT / "vincenzogulisanophd.WordPress.2026-06-30.xml"
POSTS_DIR = ROOT / "_posts"

NS = {
    "content": "http://purl.org/rss/1.0/modules/content/",
    "dc": "http://purl.org/dc/elements/1.1/",
    "wp": "http://wordpress.org/export/1.2/",
}

PAGE_ROUTES = {
    "home": ("index.md", "/", "Home"),
    "publications": ("publications.md", "/publications/", "Publications"),
    "teaching": ("teaching.md", "/teaching/", "Teaching"),
    "theses-projects": ("supervision.md", "/theses-projects/", "Supervision"),
    "aboutme": ("miscellaneous.md", "/aboutme/", "Miscellaneous"),
}


@dataclass(frozen=True)
class Item:
    title: str
    post_id: str
    post_type: str
    status: str
    slug: str
    post_date: str
    link: str
    guid: str
    content: str
    categories: tuple[str, ...]
    tags: tuple[str, ...]
    attachment_url: str


def text(element: ET.Element, path: str, default: str = "") -> str:
    value = element.findtext(path, default=default, namespaces=NS)
    return value or default


def parse_items() -> list[Item]:
    root = ET.parse(EXPORT).getroot()
    channel = root.find("channel")
    if channel is None:
        raise RuntimeError("WordPress export does not contain a channel")

    items: list[Item] = []
    for element in channel.findall("item"):
        categories: list[str] = []
        tags: list[str] = []
        for category in element.findall("category"):
            domain = category.attrib.get("domain")
            value = (category.text or "").strip()
            if not value:
                continue
            if domain == "category":
                categories.append(value)
            elif domain == "post_tag":
                tags.append(value)

        items.append(
            Item(
                title=text(element, "title"),
                post_id=text(element, "wp:post_id"),
                post_type=text(element, "wp:post_type"),
                status=text(element, "wp:status"),
                slug=text(element, "wp:post_name"),
                post_date=text(element, "wp:post_date"),
                link=text(element, "link"),
                guid=text(element, "guid"),
                content=text(element, "content:encoded"),
                categories=tuple(categories),
                tags=tuple(tags),
                attachment_url=text(element, "wp:attachment_url"),
            )
        )
    return items


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def yaml_list(values: tuple[str, ...]) -> str:
    if not values:
        return "[]"
    return "[" + ", ".join(yaml_string(value) for value in values) + "]"


def parse_date(value: str) -> dt.datetime:
    return dt.datetime.strptime(value, "%Y-%m-%d %H:%M:%S")


def post_permalink(item: Item) -> str:
    date = parse_date(item.post_date)
    return f"/{date:%Y/%m/%d}/{item.slug}/"


def page_permalink(item: Item) -> str:
    route = PAGE_ROUTES.get(item.slug)
    if route:
        return route[1]
    return f"/{item.slug}/"


def upload_path_from_url(url: str) -> str | None:
    parsed = urlsplit(html.unescape(url))
    path = parsed.path
    if parsed.netloc in {"vincenzogulisano.com", "www.vincenzogulisano.com"}:
        prefix = "/wp-content/uploads/"
        if path.startswith(prefix):
            return "/assets/uploads/" + path[len(prefix) :]
    if parsed.netloc == "vgulisano.files.wordpress.com":
        if re.match(r"^/\d{4}/\d{2}/", path):
            return "/assets/uploads" + path
    return None


def add_url_mapping(mapping: dict[str, str], source: str, target: str) -> None:
    if not source or not target:
        return
    source = html.unescape(source)
    mapping[source] = target
    if source.endswith("/"):
        mapping[source[:-1]] = target
    else:
        mapping[source + "/"] = target


def build_url_mapping(items: list[Item]) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for item in items:
        target = ""
        if item.post_type == "attachment":
            target = upload_path_from_url(item.attachment_url) or ""
        elif item.post_type == "post" and item.status == "publish":
            target = post_permalink(item)
        elif item.post_type == "page" and item.status == "publish":
            target = page_permalink(item)

        if not target:
            continue

        for source in (item.link, item.guid, item.attachment_url):
            add_url_mapping(mapping, source, target)

        if item.post_id:
            for host in (
                "https://vincenzogulisano.com",
                "http://vincenzogulisano.com",
                "https://vgulisano.wordpress.com",
                "http://vgulisano.wordpress.com",
            ):
                if item.post_type == "page":
                    add_url_mapping(mapping, f"{host}/?page_id={item.post_id}", target)
                else:
                    add_url_mapping(mapping, f"{host}/?p={item.post_id}", target)

    add_url_mapping(mapping, "https://vincenzo-gulisano.github.io/index", "/liebre/")
    add_url_mapping(mapping, "https://vincenzogulisano.com/home/liebre/", "/liebre/")
    add_url_mapping(mapping, "http://vincenzogulisano.com/liebre/", "/liebre/")
    return mapping


def rewrite_attr_urls(content: str, mapping: dict[str, str]) -> str:
    attr_re = re.compile(r"""(?P<prefix>\b(?:href|src)=["'])(?P<url>[^"']+)(?P<suffix>["'])""")

    def replace(match: re.Match[str]) -> str:
        url = html.unescape(match.group("url"))
        target = upload_path_from_url(url)
        if target is None:
            target = mapping.get(url)
        if target is None:
            target = mapping.get(url.split("#", 1)[0])
        if target is None:
            target = url
        return f"{match.group('prefix')}{target}{match.group('suffix')}"

    return attr_re.sub(replace, content)


def rewrite_plain_urls(content: str, mapping: dict[str, str]) -> str:
    for source in sorted(mapping, key=len, reverse=True):
        content = content.replace(source, mapping[source])
        content = content.replace(html.escape(source), mapping[source])

    upload_re = re.compile(
        r"https?://(?:vincenzogulisano\.com/wp-content/uploads|vgulisano\.files\.wordpress\.com)"
        r"/[^\s\"'<>]+"
    )

    def replace_upload(match: re.Match[str]) -> str:
        url = match.group(0).rstrip(").,]")
        suffix = match.group(0)[len(url) :]
        return (upload_path_from_url(url) or url) + suffix

    return upload_re.sub(replace_upload, content)


def clean_content(content: str, mapping: dict[str, str]) -> str:
    content = content.replace("\r\n", "\n").replace("\r", "\n")
    content = rewrite_attr_urls(content, mapping)
    content = rewrite_plain_urls(content, mapping)
    content = re.sub(r"<!--\s*/?wp:[^>]*-->\n?", "", content)
    content = re.sub(r"\?w=\d+", "", content)
    content = re.sub(r"<p>\s*</p>", "", content)
    content = re.sub(r"<h([1-6])>\s*</h\1>", "", content)
    content = re.sub(r"\n{3,}", "\n\n", content)
    return content.strip() + "\n"


def clean_home_content(content: str, mapping: dict[str, str]) -> str:
    content = clean_content(content, mapping)
    affiliation = (
        "Distributed Computing and Systems Research Group\n"
        "Department of Computer Science and engineering\n"
        "Chalmers University of Technology\n"
        "SE - 412 96, Gothenburg, Sweden\n"
        "vincenzo dot gulisano at chalmers dot se\n"
        'You can find my CV <a href="/assets/uploads/2021/10/cv.pdf">here</a>'
    )
    content = content.replace(
        affiliation,
        '<p class="contact-block">'
        "Distributed Computing and Systems Research Group<br>\n"
        "Department of Computer Science and engineering<br>\n"
        "Chalmers University of Technology<br>\n"
        "SE - 412 96, Gothenburg, Sweden<br>\n"
        "vincenzo dot gulisano at chalmers dot se<br>\n"
        'You can find my CV <a href="/assets/uploads/2021/10/cv.pdf">here</a>'
        "</p>",
    )
    education = (
        "2012 Ph.D. Degree, Technical University of Madrid\n"
        "2008 Master's Degree, University of Trieste.\n"
        "2006 Bachelor's Degree, University of Trieste."
    )
    content = content.replace(
        education,
        "<ul>\n"
        "<li>2012 Ph.D. Degree, Technical University of Madrid</li>\n"
        "<li>2008 Master's Degree, University of Trieste.</li>\n"
        "<li>2006 Bachelor's Degree, University of Trieste.</li>\n"
        "</ul>",
    )
    return content


def front_matter(fields: dict[str, object]) -> str:
    lines = ["---"]
    for key, value in fields.items():
        if isinstance(value, bool):
            lines.append(f"{key}: {'true' if value else 'false'}")
        elif isinstance(value, tuple):
            lines.append(f"{key}: {yaml_list(value)}")
        else:
            lines.append(f"{key}: {yaml_string(str(value))}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def write_page(item: Item, mapping: dict[str, str]) -> None:
    filename, permalink, title = PAGE_ROUTES[item.slug]
    fields: dict[str, object] = {
        "layout": "page",
        "title": title,
        "permalink": permalink,
    }
    if item.slug == "home":
        fields["hide_title"] = True
        fields["body_class"] = "home-page"

    path = ROOT / filename
    if item.slug == "home":
        content = clean_home_content(item.content, mapping)
    else:
        content = clean_content(item.content, mapping)
    path.write_text(front_matter(fields) + content, encoding="utf-8")


def write_blog_page() -> None:
    body = """<div class="post-list">
{% for post in site.posts %}
  <article class="post-list-item">
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %-d, %Y" }}</time>
    <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
    <p>{{ post.excerpt | strip_html | normalize_whitespace | truncatewords: 42 }}</p>
  </article>
{% endfor %}
</div>
"""
    fields = {
        "layout": "page",
        "title": "Blog",
        "permalink": "/blog/",
    }
    (ROOT / "blog.md").write_text(front_matter(fields) + body, encoding="utf-8")


def write_post(item: Item, mapping: dict[str, str]) -> None:
    date = parse_date(item.post_date)
    path = POSTS_DIR / f"{date:%Y-%m-%d}-{item.slug}.md"
    fields: dict[str, object] = {
        "layout": "post",
        "title": item.title,
        "date": item.post_date,
        "categories": item.categories,
        "tags": item.tags,
    }
    path.write_text(front_matter(fields) + clean_content(item.content, mapping), encoding="utf-8")


def write_liebre_page() -> None:
    body = """![Liebre](/docs/images/liebre.jpg)

Here you can find documentation about the [Liebre stream processing engine](https://github.com/vincenzo-gulisano/Liebre).
Some motivation about this project can be found [here](/2017/07/09/the-liebre-stream-processing-engine/).

If you have any questions, please write to [info@vincenzogulisano.com](mailto:info@vincenzogulisano.com)

Documentation:

1. [Basic concepts](/docs/basics/)
2. [Sources, operators and sinks](/docs/sourcesopssinks/)
3. [Statistics](/docs/stats/)

Please notice: you probably want to have a look at some of the papers you can find in my webpage (and the references they cite) to get familiar with some of the concepts discussed in the documentation (e.g., *deterministic* processing).
"""
    fields = {
        "layout": "page",
        "title": "Liebre",
        "permalink": "/liebre/",
    }
    (ROOT / "liebre.md").write_text(front_matter(fields) + body, encoding="utf-8")


def reset_generated_posts() -> None:
    if POSTS_DIR.exists():
        shutil.rmtree(POSTS_DIR)
    POSTS_DIR.mkdir()


def main() -> None:
    items = parse_items()
    mapping = build_url_mapping(items)

    reset_generated_posts()
    for item in items:
        if item.post_type == "page" and item.status == "publish" and item.slug in PAGE_ROUTES:
            write_page(item, mapping)
        elif item.post_type == "post" and item.status == "publish":
            write_post(item, mapping)

    write_blog_page()
    write_liebre_page()


if __name__ == "__main__":
    main()
