from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from PySide6.QtWidgets import QWidget


class Lesson(QWidget):
    TITLE: str = ""
    CATEGORY: str = ""
    SUBCATEGORY: str = ""
    LEVEL: Literal["Básico", "Intermedio", "Avanzado"] = "Básico"
    TAGS: list[str] = []

    def summary(self) -> str:
        raise NotImplementedError

    def guide(self) -> str:
        raise NotImplementedError

    def tutorial(self) -> str:
        return self.guide()

    def guide_sections(self) -> list[dict] | None:
        return None

    def common_pitfalls(self) -> list[tuple[str, str]]:
        raise NotImplementedError

    def code_examples(self) -> list[tuple[str, str]]:
        raise NotImplementedError

    def exercises(self) -> list[dict]:
        raise NotImplementedError

    def requirements(self) -> list[str]:
        return []

    def build_demo(self) -> QWidget | None:
        return None


@dataclass(frozen=True)
class LessonInfo:
    lesson_cls: type[Lesson]
    title: str
    category: str
    subcategory: str
    level: str
    tags: list[str]
