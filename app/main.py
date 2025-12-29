from __future__ import annotations

import logging
import sys
from dataclasses import dataclass

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSplitter,
    QTabWidget,
    QTextEdit,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)

from app.lesson_base import Lesson
from app.registry import discover_lessons, get_load_errors
from app.utils.code_runner import SnippetRunner
from app.utils.ui_helpers import badge, copy_to_clipboard

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


@dataclass
class LessonEntry:
    info_title: str
    info_category: str
    info_subcategory: str
    info_level: str
    info_tags: list[str]
    lesson_cls: type[Lesson]
    instance: Lesson
    search_text: str


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Pythonpedia")
        self.resize(1280, 800)
        self.runner = SnippetRunner()

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Buscar por título, tags o contenido...")
        self.search_input.textChanged.connect(self._apply_filter)

        self.load_errors_box = QGroupBox("Errores de carga")
        self.load_errors_label = QLabel()
        self.load_errors_label.setWordWrap(True)
        load_errors_layout = QVBoxLayout(self.load_errors_box)
        load_errors_layout.addWidget(self.load_errors_label)
        self.load_errors_box.setVisible(False)

        self.tree = QTreeWidget()
        self.tree.setHeaderHidden(True)
        self.tree.itemSelectionChanged.connect(self._on_tree_selection)

        self.tabs = QTabWidget()
        self.summary_view = QTextEdit(readOnly=True)
        self.guide_view = QTextEdit(readOnly=True)
        self.examples_container = QWidget()
        self.examples_layout = QVBoxLayout(self.examples_container)
        self.examples_layout.setAlignment(Qt.AlignTop)
        self.examples_scroll = QScrollArea()
        self.examples_scroll.setWidgetResizable(True)
        self.examples_scroll.setWidget(self.examples_container)

        self.pitfalls_list = QListWidget()
        self.pitfall_detail = QTextEdit(readOnly=True)
        self.pitfalls_list.currentItemChanged.connect(self._on_pitfall_selected)

        pitfalls_panel = QWidget()
        pitfalls_layout = QHBoxLayout(pitfalls_panel)
        pitfalls_layout.addWidget(self.pitfalls_list, 1)
        pitfalls_layout.addWidget(self.pitfall_detail, 2)

        self.exercises_container = QWidget()
        self.exercises_layout = QVBoxLayout(self.exercises_container)
        self.exercises_layout.setAlignment(Qt.AlignTop)
        self.exercises_scroll = QScrollArea()
        self.exercises_scroll.setWidgetResizable(True)
        self.exercises_scroll.setWidget(self.exercises_container)

        self.demo_container = QWidget()
        self.demo_layout = QVBoxLayout(self.demo_container)
        self.demo_layout.setAlignment(Qt.AlignTop)
        self.demo_scroll = QScrollArea()
        self.demo_scroll.setWidgetResizable(True)
        self.demo_scroll.setWidget(self.demo_container)

        self.tabs.addTab(self.summary_view, "Resumen")
        self.tabs.addTab(self.guide_view, "Guía")
        self.tabs.addTab(pitfalls_panel, "Errores típicos")
        self.tabs.addTab(self.examples_scroll, "Ejemplos")
        self.tabs.addTab(self.exercises_scroll, "Ejercicios")
        self.tabs.addTab(self.demo_scroll, "Demo")

        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        left_layout.addWidget(self.search_input)
        left_layout.addWidget(self.load_errors_box)
        left_layout.addWidget(self.tree)

        self.badge_row = QWidget()
        self.badge_layout = QHBoxLayout(self.badge_row)
        self.badge_layout.setAlignment(Qt.AlignLeft)
        self.badge_layout.setContentsMargins(0, 0, 0, 0)

        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        right_layout.addWidget(self.badge_row)
        right_layout.addWidget(self.tabs)

        splitter = QSplitter()
        splitter.addWidget(left_panel)
        splitter.addWidget(right_panel)
        splitter.setSizes([300, 980])

        container = QWidget()
        container_layout = QVBoxLayout(container)
        container_layout.addWidget(splitter)
        self.setCentralWidget(container)

        self.lesson_entries: list[LessonEntry] = []
        self._load_lessons()
        if self.lesson_entries:
            self._select_first()

    def _load_lessons(self) -> None:
        self.tree.clear()
        self.lesson_entries.clear()
        for info in discover_lessons():
            try:
                instance = info.lesson_cls()
            except Exception:
                LOGGER.exception("No se pudo instanciar %s", info.title)
                continue
            search_text = self._build_search_text(instance, info)
            entry = LessonEntry(
                info_title=info.title,
                info_category=info.category,
                info_subcategory=info.subcategory,
                info_level=info.level,
                info_tags=info.tags,
                lesson_cls=info.lesson_cls,
                instance=instance,
                search_text=search_text,
            )
            self.lesson_entries.append(entry)

        categories: dict[str, QTreeWidgetItem] = {}
        subcategories: dict[tuple[str, str], QTreeWidgetItem] = {}
        for entry in self.lesson_entries:
            category_item = categories.get(entry.info_category)
            if category_item is None:
                category_item = QTreeWidgetItem([entry.info_category])
                categories[entry.info_category] = category_item
                self.tree.addTopLevelItem(category_item)
            sub_key = (entry.info_category, entry.info_subcategory)
            sub_item = subcategories.get(sub_key)
            if sub_item is None:
                sub_item = QTreeWidgetItem([entry.info_subcategory])
                subcategories[sub_key] = sub_item
                category_item.addChild(sub_item)
            lesson_item = QTreeWidgetItem([entry.info_title])
            lesson_item.setData(0, Qt.UserRole, entry)
            sub_item.addChild(lesson_item)

        self.tree.expandAll()
        self._update_load_errors()

    def _update_load_errors(self) -> None:
        errors = get_load_errors()
        if not errors:
            self.load_errors_box.setVisible(False)
            self.load_errors_label.clear()
            return
        details = "\n".join(f"{module}: {error}" for module, error in errors)
        self.load_errors_label.setText(details)
        self.load_errors_box.setVisible(True)

    def _select_first(self) -> None:
        first_item = self.tree.topLevelItem(0)
        if first_item and first_item.childCount() > 0:
            first_leaf = first_item.child(0)
            if first_leaf.childCount() > 0:
                self.tree.setCurrentItem(first_leaf.child(0))

    def _build_search_text(self, lesson: Lesson, info) -> str:
        parts = [
            info.title,
            info.category,
            info.subcategory,
            info.level,
            " ".join(info.tags),
            lesson.summary(),
            lesson.guide(),
        ]
        parts.extend([title + " " + detail for title, detail in lesson.common_pitfalls()])
        parts.extend([title + " " + code for title, code in lesson.code_examples()])
        for exercise in lesson.exercises():
            parts.append(exercise.get("question", ""))
            parts.append(" ".join(exercise.get("hints", [])))
            parts.append(exercise.get("solution", ""))
        return "\n".join(parts).lower()

    def _apply_filter(self) -> None:
        query = self.search_input.text().strip().lower()
        for i in range(self.tree.topLevelItemCount()):
            category_item = self.tree.topLevelItem(i)
            category_visible = False
            for j in range(category_item.childCount()):
                sub_item = category_item.child(j)
                sub_visible = False
                for k in range(sub_item.childCount()):
                    lesson_item = sub_item.child(k)
                    entry = lesson_item.data(0, Qt.UserRole)
                    if not query or query in entry.search_text:
                        lesson_item.setHidden(False)
                        sub_visible = True
                        category_visible = True
                    else:
                        lesson_item.setHidden(True)
                sub_item.setHidden(not sub_visible)
            category_item.setHidden(not category_visible)

    def _on_tree_selection(self) -> None:
        items = self.tree.selectedItems()
        if not items:
            return
        entry = items[0].data(0, Qt.UserRole)
        if not isinstance(entry, LessonEntry):
            return
        self._render_lesson(entry)

    def _clear_layout(self, layout: QVBoxLayout) -> None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    def _render_lesson(self, entry: LessonEntry) -> None:
        lesson = entry.instance

        self._clear_badges()
        self.badge_layout.addWidget(badge(entry.info_category, "#2b6cb0"))
        self.badge_layout.addWidget(badge(entry.info_subcategory, "#3182ce"))
        self.badge_layout.addWidget(badge(entry.info_level, "#2f855a"))
        for tag in entry.info_tags:
            self.badge_layout.addWidget(badge(tag, "#805ad5"))
        reqs = lesson.requirements()
        if reqs:
            self.badge_layout.addWidget(badge("Requiere: " + ", ".join(reqs), "#c05621"))

        self.summary_view.setPlainText(lesson.summary())
        self.guide_view.setPlainText(lesson.guide())
        self._render_pitfalls(lesson)
        self._render_examples(lesson)
        self._render_exercises(lesson)
        self._render_demo(lesson)

    def _clear_badges(self) -> None:
        while self.badge_layout.count():
            item = self.badge_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    def _render_pitfalls(self, lesson: Lesson) -> None:
        self.pitfalls_list.clear()
        self.pitfall_detail.clear()
        for title, detail in lesson.common_pitfalls():
            item = QListWidgetItem(title)
            item.setData(Qt.UserRole, detail)
            self.pitfalls_list.addItem(item)
        if self.pitfalls_list.count() > 0:
            self.pitfalls_list.setCurrentRow(0)
    def _on_pitfall_selected(self, current: QListWidgetItem, _previous: QListWidgetItem | None = None) -> None:
        if current is None:
            self.pitfall_detail.clear()
            return
        detail = current.data(Qt.UserRole)
        self.pitfall_detail.setPlainText(detail)

    def _render_examples(self, lesson: Lesson) -> None:
        self._clear_layout(self.examples_layout)
        for title, code in lesson.code_examples():
            card = QGroupBox(title)
            card_layout = QVBoxLayout(card)

            code_view = QTextEdit()
            code_view.setPlainText(code)
            code_view.setFontFamily("Courier")
            code_view.setReadOnly(True)
            code_view.setMinimumHeight(120)

            actions = QHBoxLayout()
            copy_btn = QPushButton("Copiar")
            copy_btn.clicked.connect(lambda _, c=code: copy_to_clipboard(c, self))
            actions.addWidget(copy_btn)

            run_btn = QPushButton("Ejecutar")
            can_run, reason = self.runner.can_run(code)
            if not can_run:
                run_btn.setEnabled(False)
                run_btn.setToolTip(reason or "No se puede ejecutar este snippet.")
            else:
                run_btn.clicked.connect(lambda _, c=code, v=code_view: self._run_snippet(c, v))
            actions.addWidget(run_btn)
            actions.addStretch()

            output_view = QTextEdit(readOnly=True)
            output_view.setPlaceholderText("Salida...")
            output_view.setMaximumHeight(120)

            card_layout.addWidget(code_view)
            card_layout.addLayout(actions)
            card_layout.addWidget(output_view)
            card.setProperty("output_view", output_view)
            self.examples_layout.addWidget(card)

        self.examples_layout.addStretch()

    def _run_snippet(self, code: str, code_view: QTextEdit) -> None:
        parent_card = code_view.parentWidget()
        if parent_card is None:
            return
        output_view = parent_card.property("output_view")
        if output_view is None:
            return
        result = self.runner.run(code)
        if result.ok:
            output_view.setPlainText(result.output or "(Sin salida)")
        else:
            output_view.setPlainText(f"Error: {result.error}\n{result.output}")

    def _render_exercises(self, lesson: Lesson) -> None:
        self._clear_layout(self.exercises_layout)
        for idx, exercise in enumerate(lesson.exercises(), start=1):
            box = QGroupBox(f"Ejercicio {idx}")
            layout = QVBoxLayout(box)
            question = QLabel(exercise.get("question", ""))
            question.setWordWrap(True)
            layout.addWidget(question)

            hints_btn = QPushButton("Ver pistas")
            hints_view = QTextEdit(readOnly=True)
            hints_view.setPlainText("\n".join(exercise.get("hints", [])))
            hints_view.setVisible(False)
            hints_btn.clicked.connect(lambda _, v=hints_view: v.setVisible(not v.isVisible()))

            solution_btn = QPushButton("Ver solución")
            solution_view = QTextEdit(readOnly=True)
            solution_view.setPlainText(exercise.get("solution", ""))
            solution_view.setVisible(False)
            solution_btn.clicked.connect(lambda _, v=solution_view: v.setVisible(not v.isVisible()))

            actions = QHBoxLayout()
            actions.addWidget(hints_btn)
            actions.addWidget(solution_btn)
            actions.addStretch()

            layout.addLayout(actions)
            layout.addWidget(hints_view)
            layout.addWidget(solution_view)
            self.exercises_layout.addWidget(box)

        self.exercises_layout.addStretch()

    def _render_demo(self, lesson: Lesson) -> None:
        self._clear_layout(self.demo_layout)
        demo_widget = lesson.build_demo()
        if demo_widget is None:
            note = QLabel("No hay demo disponible para esta lección.")
            note.setWordWrap(True)
            self.demo_layout.addWidget(note)
        else:
            self.demo_layout.addWidget(demo_widget)


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
