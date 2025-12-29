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
    lessons.sort(key=lambda info: (info.category, info.subcategory, info.title))
    return lessons
