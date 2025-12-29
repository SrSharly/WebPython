from __future__ import annotations

import importlib
import logging
import pkgutil
from types import ModuleType
from typing import Iterable

from app.lesson_base import Lesson, LessonInfo

LOGGER = logging.getLogger(__name__)
_LESSON_CLASSES: list[type[Lesson]] | None = None
_LOAD_ERRORS: list[tuple[str, str]] | None = None


def _iter_lesson_modules(package: ModuleType) -> Iterable[str]:
    stack: list[ModuleType] = [package]
    while stack:
        current = stack.pop()
        yield current.__name__
        for module in pkgutil.iter_modules(current.__path__, current.__name__ + "."):
            yield module.name
            if module.ispkg:
                try:
                    stack.append(importlib.import_module(module.name))
                except Exception as exc:
                    LOGGER.exception("No se pudo importar el paquete %s", module.name)
                    _record_error(module.name, exc)


def _record_error(module_name: str, error: Exception) -> None:
    if _LOAD_ERRORS is not None:
        _LOAD_ERRORS.append((module_name, f"{type(error).__name__}: {error}"))


def _is_valid_lesson(obj: type) -> bool:
    return (
        issubclass(obj, Lesson)
        and obj is not Lesson
        and bool(getattr(obj, "TITLE", ""))
    )


def _discover_lessons() -> None:
    global _LESSON_CLASSES, _LOAD_ERRORS
    if _LESSON_CLASSES is not None and _LOAD_ERRORS is not None:
        return

    _LESSON_CLASSES = []
    _LOAD_ERRORS = []
    try:
        import app.lessons as lessons_pkg
    except Exception as exc:  # pragma: no cover - startup guard
        LOGGER.exception("No se pudo importar el paquete de lecciones")
        _record_error("app.lessons", exc)
        return

    for module_name in _iter_lesson_modules(lessons_pkg):
        try:
            module = importlib.import_module(module_name)
        except Exception as exc:
            LOGGER.exception("No se pudo importar la lección %s", module_name)
            _record_error(module_name, exc)
            continue

        for obj in module.__dict__.values():
            if isinstance(obj, type) and _is_valid_lesson(obj):
                _LESSON_CLASSES.append(obj)


def get_lessons() -> list[type[Lesson]]:
    _discover_lessons()
    return list(_LESSON_CLASSES or [])


def get_load_errors() -> list[tuple[str, str]]:
    _discover_lessons()
    return list(_LOAD_ERRORS or [])


def discover_lessons() -> list[LessonInfo]:
    lessons = [
        LessonInfo(
            lesson_cls=lesson_cls,
            title=lesson_cls.TITLE,
            category=lesson_cls.CATEGORY,
            subcategory=lesson_cls.SUBCATEGORY,
            level=lesson_cls.LEVEL,
            tags=list(lesson_cls.TAGS),
        )
        for lesson_cls in get_lessons()
    ]
    category_order = [
        "Python",
        "Bases de datos",
        "PySide6",
        "Pandas",
        "PandasAI",
        "scikit-learn",
        "TensorFlow",
        "PyTorch",
    ]
    category_rank = {name: idx for idx, name in enumerate(category_order)}
    python_curriculum = [
        "Variables y tipos",
        "Operadores y expresiones",
        "Strings y f-strings",
        "Condicionales",
        "Bucles",
        "Estructuras de datos",
        "Funciones",
        "Iteradores y generadores",
        "Context managers",
        "Excepciones",
    ]
    python_rank = {name: idx for idx, name in enumerate(python_curriculum)}
    databases_curriculum = [
        "¿Qué es una base de datos?",
        "SQLite con Python (sqlite3)",
        "PostgreSQL con Python (psycopg / asyncpg)",
        "MySQL / MariaDB con Python",
        "ORMs: SQLAlchemy",
        "NoSQL: MongoDB",
        "Buenas prácticas y seguridad",
        "Rendimiento y patrones reales",
    ]
    databases_rank = {name: idx for idx, name in enumerate(databases_curriculum)}

    def sort_key(info: LessonInfo) -> tuple[int, str, str, str]:
        order = category_rank.get(info.category, len(category_order))
        if info.category == "Python":
            if info.title in python_rank:
                return (order, 0, python_rank[info.title], info.title)
            return (order, 1, 0, info.title)
        if info.category == "Bases de datos":
            if info.title in databases_rank:
                return (order, 0, databases_rank[info.title], info.title)
            return (order, 1, 0, info.title)
        category_name = info.category if order == len(category_order) else ""
        return (order, category_name, info.subcategory, info.title)

    lessons.sort(key=sort_key)
    return lessons
