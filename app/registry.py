from __future__ import annotations

import importlib
import logging
import pkgutil
from types import ModuleType
from typing import Iterable

from app.lesson_base import Lesson, LessonInfo

LOGGER = logging.getLogger(__name__)


def _iter_lesson_modules(package: ModuleType) -> Iterable[str]:
    for module in pkgutil.walk_packages(package.__path__, package.__name__ + "."):
        if not module.ispkg:
            yield module.name


def discover_lessons() -> list[LessonInfo]:
    lessons: list[LessonInfo] = []
    try:
        import app.lessons as lessons_pkg
    except Exception:  # pragma: no cover - startup guard
        LOGGER.exception("No se pudo importar el paquete de lecciones")
        return lessons

    for module_name in _iter_lesson_modules(lessons_pkg):
        try:
            module = importlib.import_module(module_name)
        except Exception:
            LOGGER.exception("No se pudo importar la lección %s", module_name)
            continue

        for obj in module.__dict__.values():
            if isinstance(obj, type) and issubclass(obj, Lesson) and obj is not Lesson:
                lessons.append(
                    LessonInfo(
                        lesson_cls=obj,
                        title=obj.TITLE,
                        category=obj.CATEGORY,
                        subcategory=obj.SUBCATEGORY,
                        level=obj.LEVEL,
                        tags=list(obj.TAGS),
                    )
                )
    lessons.sort(key=lambda info: (info.category, info.subcategory, info.title))
    return lessons
