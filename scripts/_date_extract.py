"""記事 HTML から公開日を ISO (YYYY-MM-DD) で抽出する共通ユーティリティ。

fetch_article.py / fetch_claude_article.py から共有される。
"""

from __future__ import annotations

import re
from datetime import datetime

from bs4 import BeautifulSoup

MONTHS = {
    "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
    "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12,
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "jun": 6, "jul": 7, "aug": 8,
    "sep": 9, "sept": 9, "oct": 10, "nov": 11, "dec": 12,
}
DATE_TEXT_RE = re.compile(r"\b([A-Z][a-z]{2,8})\s+(\d{1,2}),\s+(20\d{2})\b")


def extract_published_date(html: str) -> str | None:
    """優先順: <time datetime>, meta[published_time 系], 本文テキスト "Month DD, YYYY"。"""
    soup = BeautifulSoup(html, "html.parser")

    for t in soup.find_all("time"):
        dt = t.get("datetime") or t.get("content")
        if dt:
            m = re.match(r"(\d{4}-\d{2}-\d{2})", dt)
            if m:
                return m.group(1)

    for meta in soup.find_all("meta"):
        name = (meta.get("property") or meta.get("name") or "").lower()
        if name in {
            "article:published_time",
            "article:published",
            "datepublished",
            "publish-date",
            "publishdate",
            "pubdate",
        }:
            content = meta.get("content", "")
            m = re.match(r"(\d{4}-\d{2}-\d{2})", content)
            if m:
                return m.group(1)

    for text in soup.stripped_strings:
        m = DATE_TEXT_RE.search(text)
        if m:
            month_name, day, year = m.group(1), m.group(2), m.group(3)
            month = MONTHS.get(month_name.lower())
            if month:
                try:
                    return datetime(int(year), month, int(day)).strftime("%Y-%m-%d")
                except ValueError:
                    continue
    return None
