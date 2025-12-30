from __future__ import annotations

import re
from urllib.parse import quote
from functools import lru_cache

from app.utils.glossary import GLOSSARY, KEYWORDS
from app.utils.mention_indexer import get_lesson_aliases

_SKIP_TAGS = {"code", "pre", "style", "script"}
_MAX_MATCHES_PER_TERM = 8
_KW_CLASS_RE = re.compile(r"class\s*=\s*[\"'][^\"']*\bkw\b[^\"']*[\"']", flags=re.IGNORECASE)


@lru_cache(maxsize=1)
def _keyword_pattern() -> re.Pattern[str]:
    terms = sorted(KEYWORDS, key=len, reverse=True)
    escaped = "|".join(re.escape(term) for term in terms)
    pattern = rf"(?<![\w.])({escaped})(?!\w)"
    return re.compile(pattern, flags=re.IGNORECASE)


def tooltipify_html(html_text: str, lesson=None) -> str:
    counts: dict[str, int] = {}
    alias_map = get_lesson_aliases(lesson) if lesson is not None else {}
    if alias_map:
        alias_terms = sorted(alias_map.keys(), key=len, reverse=True)
        combined_terms = list(dict.fromkeys(alias_terms + KEYWORDS))
        word_terms = [term for term in combined_terms if term[:1].isalnum() or term[:1] == "_"]
        symbol_terms = [term for term in combined_terms if term not in word_terms]
        parts = []
        if word_terms:
            escaped = "|".join(re.escape(term) for term in word_terms)
            parts.append(rf"(?<![\w.])({escaped})(?!\w)")
        if symbol_terms:
            escaped = "|".join(re.escape(term) for term in symbol_terms)
            parts.append(rf"({escaped})(?!\w)")
        pattern = re.compile("|".join(parts), flags=re.IGNORECASE)
    else:
        pattern = _keyword_pattern()

    def _replace(match: re.Match[str]) -> str:
        original = match.group(0)
        key = original.lower()
        term_id = alias_map.get(key)
        if term_id:
            current = counts.get(term_id, 0)
            if current >= _MAX_MATCHES_PER_TERM:
                return original
            counts[term_id] = current + 1
            term_id_encoded = quote(term_id)
            return f'<a href="tip:{term_id_encoded}" class="kw">{original}</a>'
        if key not in GLOSSARY:
            return original
        current = counts.get(key, 0)
        if current >= _MAX_MATCHES_PER_TERM:
            return original
        counts[key] = current + 1
        term_id_encoded = quote(key)
        return f'<a href="tip:{term_id_encoded}" class="kw">{original}</a>'

    parts = re.split(r"(<[^>]+>)", html_text)
    output: list[str] = []
    skip_tag_depth = 0
    kw_tag_depth = 0
    for part in parts:
        if part.startswith("<"):
            tag_name = part.strip("<>").split()[0].lower().strip("/")
            is_end_tag = part.startswith("</")
            if tag_name in _SKIP_TAGS:
                skip_tag_depth = skip_tag_depth - 1 if is_end_tag else skip_tag_depth + 1
                skip_tag_depth = max(skip_tag_depth, 0)
            if tag_name in {"span", "a"}:
                if not is_end_tag and _KW_CLASS_RE.search(part):
                    kw_tag_depth += 1
                elif is_end_tag and kw_tag_depth:
                    kw_tag_depth -= 1
            output.append(part)
            continue
        if skip_tag_depth or kw_tag_depth:
            output.append(part)
            continue
        output.append(pattern.sub(_replace, part))
    return "".join(output)
