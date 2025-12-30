from __future__ import annotations

from app.utils.library_catalog import LIBRARIES


def build_search_text(library_key: str, item: dict) -> str:
    library = LIBRARIES[library_key]
    examples_text = " ".join(
        " ".join(
            [
                example.get("title", ""),
                example.get("learn", ""),
                example.get("do", ""),
                example.get("see", ""),
                example.get("why", ""),
                " ".join(example.get("pitfalls", [])),
            ]
        )
        for example in item.get("examples", [])
    )
    parts = [
        library.get("title", ""),
        library.get("summary", ""),
        " ".join(library.get("tags", [])),
        item.get("name", ""),
        item.get("kind", ""),
        item.get("category", ""),
        item.get("signature", ""),
        item.get("what", ""),
        " ".join(item.get("when", [])),
        " ".join(item.get("pitfalls", [])),
        examples_text,
    ]
    return " ".join(part for part in parts if part)


def iter_library_items() -> list[tuple[str, dict, dict]]:
    items: list[tuple[str, dict, dict]] = []
    for key, library in LIBRARIES.items():
        for item in library.get("items", []):
            items.append((key, library, item))
    return items
