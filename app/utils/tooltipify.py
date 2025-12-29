from __future__ import annotations

import html
import re
from functools import lru_cache

from app.utils.glossary import KEYWORDS, TERMS

_SKIP_TAGS = {"code", "pre", "style", "script"}
_MAX_MATCHES_PER_TERM = 8
_KW_CLASS_RE = re.compile(r"class\s*=\s*[\"'][^\"']*\bkw\b[^\"']*[\"']", flags=re.IGNORECASE)


@lru_cache(maxsize=1)
def _keyword_pattern() -> re.Pattern[str]:
    terms = sorted(KEYWORDS, key=len, reverse=True)
    escaped = "|".join(re.escape(term) for term in terms)
    pattern = rf"(?<!\w)({escaped})(?!\w)"
    return re.compile(pattern, flags=re.IGNORECASE)


def tooltipify_html(html_text: str) -> str:
    counts: dict[str, int] = {}
    pattern = _keyword_pattern()

    def _replace(match: re.Match[str]) -> str:
        original = match.group(0)
        key = original.lower()
        definition = TERMS.get(key)
        if definition is None:
            return original
        current = counts.get(key, 0)
        if current >= _MAX_MATCHES_PER_TERM:
            return original
        counts[key] = current + 1
        safe_definition = html.escape(definition, quote=True)
        return f'<span class="kw" title="{safe_definition}">{original}</span>'

    parts = re.split(r"(<[^>]+>)", html_text)
    output: list[str] = []
    skip_tag_depth = 0
    kw_span_depth = 0
    for part in parts:
        if part.startswith("<"):
            tag_name = part.strip("<>").split()[0].lower().strip("/")
            is_end_tag = part.startswith("</")
            if tag_name in _SKIP_TAGS:
                skip_tag_depth = skip_tag_depth - 1 if is_end_tag else skip_tag_depth + 1
                skip_tag_depth = max(skip_tag_depth, 0)
            if tag_name == "span":
                if not is_end_tag and _KW_CLASS_RE.search(part):
                    kw_span_depth += 1
                elif is_end_tag and kw_span_depth:
                    kw_span_depth -= 1
            output.append(part)
            continue
        if skip_tag_depth or kw_span_depth:
            output.append(part)
            continue
        output.append(pattern.sub(_replace, part))
    return "".join(output)
