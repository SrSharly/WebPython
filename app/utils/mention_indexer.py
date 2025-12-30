from __future__ import annotations

from dataclasses import dataclass, field
import builtins
import re
from typing import Iterable
from urllib.parse import unquote

from app.lesson_base import Lesson
from app.utils.library_catalog import LIBRARIES


@dataclass(frozen=True)
class MentionKey:
    kind: str
    namespace: str
    owner: str | None
    name: str


@dataclass
class MentionedTerm:
    key: MentionKey
    aliases: set[str] = field(default_factory=set)


@dataclass
class MentionIndex:
    terms: dict[MentionKey, MentionedTerm]
    lesson_mentions: dict[str, set[MentionKey]]
    lesson_types: dict[str, set[str]]


@dataclass
class ResolvedMentionIndex:
    auto_terms: dict[str, dict[str, object]]
    term_meta: dict[str, dict[str, str | None]]
    term_labels: dict[str, str]
    term_related: dict[str, list[str]]
    lesson_terms: dict[str, set[str]]
    lesson_owner_terms: dict[str, dict[str, set[str]]]
    lesson_aliases: dict[str, dict[str, str]]
    lesson_types: dict[str, set[str]]


_MENTION_INDEX: MentionIndex | None = None
_RESOLVED_INDEX: ResolvedMentionIndex | None = None

_LIB_ALIAS_MAP = {
    "pd": "pandas",
    "np": "numpy",
    "plt": "matplotlib",
    "sns": "seaborn",
    "tf": "tensorflow",
    "torch": "pytorch",
    "sk": "sklearn",
}

_METHOD_OWNER_MAP = {
    "upper": "str",
    "lower": "str",
    "split": "str",
    "strip": "str",
    "join": "str",
    "replace": "str",
    "startswith": "str",
    "endswith": "str",
    "find": "str",
    "format": "str",
    "append": "list",
    "extend": "list",
    "insert": "list",
    "pop": "list",
    "remove": "list",
    "sort": "list",
    "count": "list",
    "index": "list",
    "get": "dict",
    "keys": "dict",
    "values": "dict",
    "items": "dict",
    "update": "dict",
    "clear": "dict",
    "copy": "dict",
    "setdefault": "dict",
    "head": "pandas.DataFrame",
    "loc": "pandas.DataFrame",
    "iloc": "pandas.DataFrame",
}

_ATTRIBUTE_OWNER_MAP = {
    "shape": "pandas.DataFrame",
    "dtype": "pandas.DataFrame",
}

_TYPE_ALIASES = {
    "str": "str",
    "string": "str",
    "strings": "str",
    "texto": "str",
    "textos": "str",
    "list": "list",
    "lista": "list",
    "listas": "list",
    "dict": "dict",
    "diccionario": "dict",
    "diccionarios": "dict",
    "set": "set",
    "sets": "set",
    "conjunto": "set",
    "conjuntos": "set",
    "tuple": "tuple",
    "tupla": "tuple",
    "tuplas": "tuple",
    "dataframe": "pandas.DataFrame",
    "dataframes": "pandas.DataFrame",
}

_METHOD_WORD_RE = re.compile(r"\b(" + "|".join(sorted(_METHOD_OWNER_MAP)) + r")\b", re.IGNORECASE)
_ATTRIBUTE_WORD_RE = re.compile(r"\b(" + "|".join(sorted(_ATTRIBUTE_OWNER_MAP)) + r")\b", re.IGNORECASE)

_LIB_CALL_RE = re.compile(r"\b(?P<prefix>[A-Za-z_]\w*)\.(?P<name>[A-Za-z_]\w*)\s*\(")
_METHOD_CALL_RE = re.compile(
    r"(?P<object>(?:\"[^\"]*\"|'[^']*'|\[[^\]]*\]|\{[^\}]*\}|\b[A-Za-z_]\w*\b))\.(?P<name>[A-Za-z_]\w*)\s*\("
)
_ATTR_RE = re.compile(
    r"(?P<object>(?:\"[^\"]*\"|'[^']*'|\[[^\]]*\]|\{[^\}]*\}|\b[A-Za-z_]\w*\b))\.(?P<name>[A-Za-z_]\w*)\b(?!\s*\()"
)
_FUNC_CALL_RE = re.compile(r"(?<!\.)\b([A-Za-z_]\w*)\s*\(")
_TIP_ANCHOR_RE = re.compile(r"tip:([A-Za-z0-9:_\.\-%]+)")
_KW_MARK_RE = re.compile(r"class\s*=\s*[\"'][^\"']*\bkw\b[^\"']*[\"'][^>]*>([^<]+)")

_BUILTIN_FUNCTIONS = {
    name.lower()
    for name, obj in builtins.__dict__.items()
    if callable(obj)
}


def _lesson_id(lesson: Lesson) -> str:
    return f"{lesson.__class__.__module__}.{lesson.__class__.__qualname__}"


def _infer_owner_from_object(obj: str, name: str) -> str | None:
    obj_clean = obj.strip()
    if obj_clean.startswith(("\"", "'")):
        return "str"
    if obj_clean.startswith("["):
        return "list"
    if obj_clean.startswith("{"):
        if name in {"get", "keys", "values", "items", "update", "setdefault", "pop"}:
            return "dict"
        return None
    obj_lower = obj_clean.lower()
    if obj_lower in {"str", "list", "dict", "set", "tuple"}:
        return obj_lower
    return _METHOD_OWNER_MAP.get(name)


def _namespace_from_owner(owner: str | None) -> str:
    if owner is None:
        return "unknown"
    if owner in {"str", "list", "dict", "set", "tuple"}:
        return "builtin"
    if owner.startswith("pandas."):
        return "pandas"
    return "unknown"


def _add_term(
    terms: dict[MentionKey, MentionedTerm],
    kind: str,
    namespace: str,
    owner: str | None,
    name: str,
    aliases: Iterable[str],
) -> MentionKey:
    key = MentionKey(kind=kind, namespace=namespace, owner=owner, name=name.lower())
    term = terms.get(key)
    if term is None:
        term = MentionedTerm(key=key)
        terms[key] = term
    for alias in aliases:
        alias_clean = alias.strip()
        if alias_clean:
            term.aliases.add(alias_clean.lower())
    return key


def _collect_lesson_texts(lesson: Lesson) -> list[str]:
    texts = [lesson.summary(), lesson.tutorial()]
    guide_sections = lesson.guide_sections()
    if guide_sections:
        for section in guide_sections:
            texts.append(section.get("title", ""))
            texts.append(section.get("content", ""))
    texts.extend([title + " " + detail for title, detail in lesson.common_pitfalls()])
    texts.extend([title + " " + code for title, code in lesson.code_examples()])
    for exercise in lesson.exercises():
        texts.append(exercise.get("question", ""))
        texts.append(" ".join(exercise.get("hints", [])))
        texts.append(exercise.get("solution", ""))
    return [text for text in texts if text]


def _detect_lesson_types(lesson: Lesson) -> set[str]:
    tokens = [lesson.TITLE, *lesson.TAGS]
    detected = set()
    for token in tokens:
        for raw in re.split(r"[^A-Za-z0-9_]+", token.lower()):
            if not raw:
                continue
            mapped = _TYPE_ALIASES.get(raw)
            if mapped:
                detected.add(mapped)
    return detected


def _extract_mentions_from_text(text: str, terms: dict[MentionKey, MentionedTerm]) -> set[MentionKey]:
    found: set[MentionKey] = set()
    for match in _TIP_ANCHOR_RE.finditer(text):
        term_id = unquote(match.group(1)).strip().lower()
        if term_id:
            key = _add_term(
                terms,
                kind="explicit",
                namespace="manual",
                owner=None,
                name=term_id,
                aliases={term_id},
            )
            found.add(key)

    for match in _KW_MARK_RE.finditer(text):
        term_text = match.group(1).strip()
        if term_text:
            term_id = term_text.lower()
            key = _add_term(
                terms,
                kind="explicit",
                namespace="manual",
                owner=None,
                name=term_id,
                aliases={term_text, term_id},
            )
            found.add(key)
    for match in _LIB_CALL_RE.finditer(text):
        prefix = match.group("prefix")
        if prefix not in _LIB_ALIAS_MAP:
            continue
        name = match.group("name").lower()
        namespace = _LIB_ALIAS_MAP[prefix]
        key = _add_term(
            terms,
            kind="function",
            namespace=namespace,
            owner=None,
            name=name,
            aliases={f"{prefix}.{name}", f"{prefix}.{name}()", name, f"{name}()"},
        )
        found.add(key)

    for match in _METHOD_CALL_RE.finditer(text):
        obj = match.group("object")
        if obj in _LIB_ALIAS_MAP:
            continue
        name = match.group("name").lower()
        owner = _infer_owner_from_object(obj, name)
        namespace = _namespace_from_owner(owner)
        key = _add_term(
            terms,
            kind="method",
            namespace=namespace,
            owner=owner,
            name=name,
            aliases={f".{name}", f".{name}()", name, f"{name}()"},
        )
        found.add(key)

    for match in _ATTR_RE.finditer(text):
        name = match.group("name").lower()
        if name in _METHOD_OWNER_MAP:
            owner = _METHOD_OWNER_MAP.get(name)
            namespace = _namespace_from_owner(owner)
            key = _add_term(
                terms,
                kind="method",
                namespace=namespace,
                owner=owner,
                name=name,
                aliases={f".{name}", f".{name}()", name, f"{name}()"},
            )
            found.add(key)
            continue
        owner = _ATTRIBUTE_OWNER_MAP.get(name)
        namespace = _namespace_from_owner(owner)
        key = _add_term(
            terms,
            kind="attribute",
            namespace=namespace,
            owner=owner,
            name=name,
            aliases={f".{name}", name},
        )
        found.add(key)

    for match in _FUNC_CALL_RE.finditer(text):
        name = match.group(1).lower()
        if name in _BUILTIN_FUNCTIONS:
            key = _add_term(
                terms,
                kind="builtin",
                namespace="builtin",
                owner=None,
                name=name,
                aliases={name, f"{name}()"},
            )
            found.add(key)
        else:
            key = _add_term(
                terms,
                kind="function",
                namespace="unknown",
                owner=None,
                name=name,
                aliases={name, f"{name}()"},
            )
            found.add(key)

    for match in _METHOD_WORD_RE.finditer(text):
        name = match.group(1).lower()
        owner = _METHOD_OWNER_MAP.get(name)
        namespace = _namespace_from_owner(owner)
        key = _add_term(
            terms,
            kind="method",
            namespace=namespace,
            owner=owner,
            name=name,
            aliases={name},
        )
        found.add(key)

    for match in _ATTRIBUTE_WORD_RE.finditer(text):
        name = match.group(1).lower()
        owner = _ATTRIBUTE_OWNER_MAP.get(name)
        namespace = _namespace_from_owner(owner)
        key = _add_term(
            terms,
            kind="attribute",
            namespace=namespace,
            owner=owner,
            name=name,
            aliases={name},
        )
        found.add(key)

    return found


def build_mention_index(lessons: Iterable[Lesson]) -> MentionIndex:
    terms: dict[MentionKey, MentionedTerm] = {}
    lesson_mentions: dict[str, set[MentionKey]] = {}
    lesson_types: dict[str, set[str]] = {}

    for lesson in lessons:
        lesson_key = _lesson_id(lesson)
        lesson_types[lesson_key] = _detect_lesson_types(lesson)
        mentions: set[MentionKey] = set()
        for text in _collect_lesson_texts(lesson):
            mentions.update(_extract_mentions_from_text(text, terms))
        lesson_mentions[lesson_key] = mentions

    for library_key, library in LIBRARIES.items():
        namespace = library_key
        for item in library.get("items", []):
            name = str(item.get("name", "")).strip().lower()
            if not name:
                continue
            aliases = {name}
            _add_term(
                terms,
                kind="function",
                namespace=namespace,
                owner=None,
                name=name,
                aliases=aliases,
            )
            for text in (
                item.get("signature", ""),
                item.get("what", ""),
                " ".join(item.get("when", [])),
                " ".join(item.get("pitfalls", [])),
                item.get("example", ""),
            ):
                _extract_mentions_from_text(str(text), terms)

    global _MENTION_INDEX, _RESOLVED_INDEX
    _MENTION_INDEX = MentionIndex(
        terms=terms,
        lesson_mentions=lesson_mentions,
        lesson_types=lesson_types,
    )
    _RESOLVED_INDEX = None
    return _MENTION_INDEX


def resolve_mention_index(glossary: dict[str, dict[str, object]]) -> ResolvedMentionIndex:
    if _MENTION_INDEX is None:
        raise RuntimeError("Mention index must be built before resolving.")

    term_meta: dict[str, dict[str, str | None]] = {}
    term_labels: dict[str, str] = {}
    term_related: dict[str, list[str]] = {}
    auto_terms: dict[str, dict[str, object]] = {}
    lesson_terms: dict[str, set[str]] = {key: set() for key in _MENTION_INDEX.lesson_mentions}
    lesson_owner_terms: dict[str, dict[str, set[str]]] = {key: {} for key in _MENTION_INDEX.lesson_mentions}
    lesson_aliases: dict[str, dict[str, str]] = {key: {} for key in _MENTION_INDEX.lesson_mentions}

    def term_label(name: str, kind: str) -> str:
        if kind in {"method", "function", "builtin"}:
            return f"{name}()"
        return name

    def build_term_id(key: MentionKey) -> str:
        if key.name in glossary:
            return key.name
        if key.kind == "explicit":
            return key.name
        if key.kind == "method":
            owner = key.owner or "unknown"
            return f"method:{owner}.{key.name}"
        if key.kind == "attribute":
            owner = key.owner or "unknown"
            return f"attr:{owner}.{key.name}"
        if key.kind == "builtin":
            return f"builtin:{key.name}"
        if key.namespace != "unknown":
            return f"{key.namespace}:{key.name}"
        return f"unknown:{key.name}"

    term_id_map: dict[MentionKey, str] = {}
    for key, term in _MENTION_INDEX.terms.items():
        term_id = build_term_id(key)
        term_id_map[key] = term_id
        label = term_label(key.name, key.kind)
        term_labels[term_id] = label
        term_meta[term_id] = {
            "name": key.name,
            "kind": key.kind,
            "owner": key.owner,
            "namespace": key.namespace,
            "label": label,
        }
        if term_id not in glossary:
            auto_terms[term_id] = {
                "tooltip": "Término detectado en las lecciones. Abre para ver detalles.",
                "definition_parts": {
                    "que_es": "Pendiente de documentar.",
                    "sintaxis": "Pendiente de documentar.",
                    "ejemplo": "Pendiente de documentar.",
                    "error_tipico": "Pendiente de documentar.",
                    "ver_tambien": "Pendiente de documentar.",
                },
            }

    owner_groups: dict[str, list[str]] = {}
    for term_id, meta in term_meta.items():
        owner = meta.get("owner")
        if owner:
            owner_groups.setdefault(owner, []).append(term_id)

    for owner, terms in owner_groups.items():
        sorted_terms = sorted(terms, key=lambda tid: term_labels.get(tid, tid))
        for term_id in terms:
            related = [tid for tid in sorted_terms if tid != term_id]
            if related:
                term_related[term_id] = related

    for lesson_key, mentions in _MENTION_INDEX.lesson_mentions.items():
        for mention in sorted(mentions, key=lambda k: (k.name, k.kind, k.owner or "")):
            term_id = term_id_map[mention]
            lesson_terms[lesson_key].add(term_id)
            owner = mention.owner
            if owner:
                lesson_owner_terms.setdefault(lesson_key, {}).setdefault(owner, set()).add(term_id)
            aliases = _MENTION_INDEX.terms[mention].aliases
            alias_map = lesson_aliases[lesson_key]
            for alias in sorted(aliases):
                alias_map.setdefault(alias, term_id)

    resolved = ResolvedMentionIndex(
        auto_terms=auto_terms,
        term_meta=term_meta,
        term_labels=term_labels,
        term_related=term_related,
        lesson_terms=lesson_terms,
        lesson_owner_terms=lesson_owner_terms,
        lesson_aliases=lesson_aliases,
        lesson_types=_MENTION_INDEX.lesson_types,
    )
    global _RESOLVED_INDEX
    _RESOLVED_INDEX = resolved
    return resolved


def get_resolved_index() -> ResolvedMentionIndex | None:
    return _RESOLVED_INDEX


def get_lesson_aliases(lesson: Lesson) -> dict[str, str]:
    if _RESOLVED_INDEX is None:
        return {}
    return _RESOLVED_INDEX.lesson_aliases.get(_lesson_id(lesson), {})


def get_lesson_owner_terms(lesson: Lesson) -> dict[str, set[str]]:
    if _RESOLVED_INDEX is None:
        return {}
    return _RESOLVED_INDEX.lesson_owner_terms.get(_lesson_id(lesson), {})


def get_lesson_terms(lesson: Lesson) -> set[str]:
    if _RESOLVED_INDEX is None:
        return set()
    return set(_RESOLVED_INDEX.lesson_terms.get(_lesson_id(lesson), set()))


def get_lesson_types(lesson: Lesson) -> set[str]:
    if _RESOLVED_INDEX is None:
        return set()
    return _RESOLVED_INDEX.lesson_types.get(_lesson_id(lesson), set())


def get_term_label(term_id: str) -> str:
    if _RESOLVED_INDEX is None:
        return term_id
    return _RESOLVED_INDEX.term_labels.get(term_id, term_id)


def get_term_meta(term_id: str) -> dict[str, str | None]:
    if _RESOLVED_INDEX is None:
        return {}
    return dict(_RESOLVED_INDEX.term_meta.get(term_id, {}))


def get_related_terms(term_id: str) -> list[str]:
    if _RESOLVED_INDEX is None:
        return []
    return list(_RESOLVED_INDEX.term_related.get(term_id, []))
