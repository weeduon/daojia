#!/usr/bin/env python3
"""Build a metadata-only catalog for daorenjia.com.

The script requests category listings and the site's checked-text index. It does
not download or store full scripture text.
"""

from __future__ import annotations

import argparse
import csv
import html
import io
import pathlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request


BASE_URL = "https://www.daorenjia.com/"
USER_AGENT = "daoist-advisor-catalog/1.0 (metadata index; respectful rate limit)"

CATEGORIES = {
    8: ("三洞真经", "洞真上清经"),
    9: ("三洞真经", "洞玄灵宝经"),
    10: ("三洞真经", "洞神三皇经"),
    11: ("三洞真经", "三洞经教"),
    12: ("四辅真经", "太平部诸经"),
    13: ("四辅真经", "太玄部经诀"),
    14: ("四辅真经", "正一部经籙"),
    15: ("四辅真经", "道德真经"),
    16: ("四辅真经", "四子真经"),
    17: ("四辅真经", "黄帝阴符经"),
    18: ("四辅真经", "道教易学"),
    19: ("四辅真经", "太清金丹经"),
    20: ("四辅真经", "太清摄养经"),
    21: ("道教论集", "诸子文集"),
    22: ("道教论集", "道学论著"),
    23: ("道教论集", "全真文集"),
    24: ("道教论集", "道教类书"),
    25: ("道法众术", "道法诸经"),
    26: ("道法众术", "道法总集"),
    27: ("道教科仪", "科戒威仪"),
    28: ("道教科仪", "灵宝诸斋仪"),
    29: ("道教科仪", "灯仪法忏章表"),
    30: ("道史仙传", "神仙高道传"),
    31: ("道史仙传", "仙境名山志"),
}

LINK_RE = re.compile(
    r'<a\s+[^>]*href=["\'](?P<href>/?daozang\d+-\d+)["\'][^>]*>'
    r'(?P<title>.*?)</a>',
    re.IGNORECASE | re.DOTALL,
)
TAG_RE = re.compile(r"<[^>]+>")


def fetch(path: str, timeout: float) -> str:
    url = urllib.parse.urljoin(BASE_URL, path)
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        content_type = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(content_type, errors="replace")


def parse_links(document: str) -> list[tuple[str, str]]:
    records: list[tuple[str, str]] = []
    seen: set[str] = set()
    for match in LINK_RE.finditer(document):
        path = "/" + match.group("href").lstrip("/")
        if path in seen:
            continue
        title = TAG_RE.sub("", match.group("title"))
        title = html.unescape(re.sub(r"\s+", " ", title)).strip()
        if not title:
            continue
        seen.add(path)
        records.append((path, title))
    return records


def build_catalog(delay: float, timeout: float) -> list[dict[str, str]]:
    checked = {path for path, _ in parse_links(fetch("/yjd", timeout))}
    records: list[dict[str, str]] = []
    seen: set[str] = set()

    for category_id, (group, category) in CATEGORIES.items():
        if delay:
            time.sleep(delay)
        document = fetch(f"/c{category_id}", timeout)
        for path, title in parse_links(document):
            if path in seen:
                continue
            seen.add(path)
            records.append(
                {
                    "group": group,
                    "category": category,
                    "title": title,
                    "url": urllib.parse.urljoin(BASE_URL, path),
                    "site_checked": "yes" if path in checked else "no",
                }
            )

    records.sort(key=lambda row: (row["group"], row["category"], row["url"]))
    return records


def write_tsv(records: list[dict[str, str]], output: pathlib.Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    buffer = io.StringIO()
    buffer.write("# Metadata-only catalog; no scripture bodies are stored.\n")
    buffer.write(f"# Source: {BASE_URL}\n")
    buffer.write("# site_checked reflects the site's own /yjd list, not independent review.\n")
    writer = csv.DictWriter(
        buffer,
        fieldnames=["group", "category", "title", "url", "site_checked"],
        dialect="excel-tab",
        lineterminator="\n",
    )
    writer.writeheader()
    writer.writerows(records)
    output.write_text(buffer.getvalue(), encoding="utf-8")


def self_test() -> None:
    sample = """
    <ol><li><a href="daozang11-446">太上老君说常清静妙经</a></li>
    <li><a href="/daozang15-646"><b>老子道德经</b></a></li></ol>
    """
    actual = parse_links(sample)
    expected = [
        ("/daozang11-446", "太上老君说常清静妙经"),
        ("/daozang15-646", "老子道德经"),
    ]
    if actual != expected:
        raise AssertionError(f"parse_links mismatch: {actual!r}")
    print("self-test passed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=pathlib.Path,
        default=pathlib.Path(__file__).resolve().parent.parent
        / "references"
        / "daorenjia-catalog.tsv",
    )
    parser.add_argument("--delay", type=float, default=0.35)
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return 0

    try:
        records = build_catalog(max(args.delay, 0.0), args.timeout)
    except (urllib.error.URLError, TimeoutError) as exc:
        print(f"catalog build failed: {exc}", file=sys.stderr)
        return 1

    if len(records) < 1000:
        print(
            f"catalog build refused: only {len(records)} records; expected at least 1000",
            file=sys.stderr,
        )
        return 2

    write_tsv(records, args.output)
    print(f"wrote {len(records)} records to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
