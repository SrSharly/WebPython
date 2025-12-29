from __future__ import annotations

import html
import logging
import sys
from dataclasses import dataclass

from PySide6.QtCore import QSettings, Qt
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import (
    QApplication,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSplitter,
    QTabWidget,
    QTextBrowser,
    QTextEdit,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)

from app.lesson_base import Lesson
from app.registry import discover_lessons, get_load_errors
from app.ui.glossary_view import GlossaryView
from app.utils.code_runner import SnippetRunner
from app.utils.theme import apply_theme, toggle_theme
from app.utils.tooltipify import tooltipify_html
from app.utils.ui_components import CodeCard
from app.utils.ui_helpers import badge

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
    def __init__(self, app: QApplication, settings: QSettings, theme_name: str) -> None:
        super().__init__()
        self.app = app
        self.settings = settings
        self.current_theme = theme_name
        self.setWindowTitle("Pythonpedia")
        self.resize(1280, 800)
        self.runner = SnippetRunner()

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Buscar por título, tags o contenido...")
        self.search_input.setClearButtonEnabled(True)
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
        self.guide_text = QTextBrowser()
        self.guide_text.setOpenExternalLinks(True)
        self.guide_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.guide_text.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.guide_text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.guide_scroll = QScrollArea()
        self.guide_scroll.setWidgetResizable(True)
        self.guide_scroll.setWidget(self.guide_text)
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

        self.glossary_view = GlossaryView()

        self.tabs.addTab(self.guide_scroll, "Tutorial")
        self.tabs.addTab(self.summary_view, "Resumen")
        self.tabs.addTab(pitfalls_panel, "Errores típicos")
        self.tabs.addTab(self.examples_scroll, "Ejemplos")
        self.tabs.addTab(self.exercises_scroll, "Ejercicios")
        self.tabs.addTab(self.demo_scroll, "Demo")
        self.tabs.addTab(self.glossary_view, "Glosario")

        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        left_layout.addWidget(self.search_input)
        left_layout.addWidget(self.load_errors_box)
        left_layout.addWidget(self.tree)

        self.header_widget = QWidget()
        self.header_layout = QVBoxLayout(self.header_widget)
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setSpacing(4)
        self.header_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.title_label = QLabel("Selecciona una lección")
        self.title_label.setObjectName("HeaderTitle")
        header_row = QHBoxLayout()
        header_row.addWidget(self.title_label)
        header_row.addStretch()
        self.theme_toggle = QPushButton()
        self.theme_toggle.setProperty("secondary", True)
        self.theme_toggle.clicked.connect(self._toggle_theme)
        header_row.addWidget(self.theme_toggle)
        self.header_layout.addLayout(header_row)

        self.badge_row = QWidget()
        self.badge_layout = QHBoxLayout(self.badge_row)
        self.badge_layout.setAlignment(Qt.AlignLeft)
        self.badge_layout.setContentsMargins(0, 0, 0, 0)
        self.badge_layout.setSpacing(6)
        self.header_layout.addWidget(self.badge_row)

        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        right_layout.addWidget(self.header_widget)
        right_layout.addWidget(self.tabs)
        right_layout.setStretch(0, 0)
        right_layout.setStretch(1, 1)

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

        search_shortcut = QShortcut(QKeySequence("Ctrl+K"), self)
        search_shortcut.activated.connect(self.search_input.setFocus)
        self._update_theme_toggle()

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
            lesson.tutorial(),
        ]
        guide_sections = lesson.guide_sections()
        if guide_sections:
            for section in guide_sections:
                parts.append(section.get("title", ""))
                parts.append(section.get("content", ""))
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
            category_visible = True
            for j in range(category_item.childCount()):
                sub_item = category_item.child(j)
                sub_visible = False
                for k in range(sub_item.childCount()):
                    lesson_item = sub_item.child(k)
                    entry = lesson_item.data(0, Qt.UserRole)
                    if not query or query in entry.search_text:
                        lesson_item.setHidden(False)
                        sub_visible = True
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
        self.current_entry = entry
        lesson = entry.instance

        self._clear_badges()
        self.title_label.setText(entry.info_title)
        self.badge_layout.addWidget(badge(entry.info_category, "#2b6cb0"))
        self.badge_layout.addWidget(badge(entry.info_subcategory, "#3182ce"))
        self.badge_layout.addWidget(badge(entry.info_level, "#2f855a"))
        for tag in entry.info_tags:
            self.badge_layout.addWidget(badge(tag, "#805ad5"))
        reqs = lesson.requirements()
        if reqs:
            self.badge_layout.addWidget(badge("Requiere: " + ", ".join(reqs), "#c05621"))

        self.summary_view.setPlainText(lesson.summary())
        self._render_guide(lesson)
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

    def _guide_html_from_text(self, text: str) -> str:
        lines = text.splitlines()
        chunks: list[str] = []
        list_items: list[str] = []
        code_lines: list[str] = []
        in_code_block = False
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("```"):
                if in_code_block:
                    chunks.append(
                        '<pre class="code-block"><code>'
                        + html.escape("\n".join(code_lines))
                        + "</code></pre>"
                    )
                    code_lines = []
                    in_code_block = False
                else:
                    if list_items:
                        chunks.append("<ul>" + "".join(f"<li>{item}</li>" for item in list_items) + "</ul>")
                        list_items = []
                    in_code_block = True
                continue
            if in_code_block:
                code_lines.append(line)
                continue
            if stripped.startswith("### "):
                if list_items:
                    chunks.append("<ul>" + "".join(f"<li>{item}</li>" for item in list_items) + "</ul>")
                    list_items = []
                chunks.append(f"<h3>{html.escape(stripped[4:].strip())}</h3>")
                continue
            if stripped.startswith("## "):
                if list_items:
                    chunks.append("<ul>" + "".join(f"<li>{item}</li>" for item in list_items) + "</ul>")
                    list_items = []
                chunks.append(f"<h2>{html.escape(stripped[3:].strip())}</h2>")
                continue
            if stripped.startswith(("-", "*")):
                list_items.append(html.escape(stripped[1:].strip()))
                continue
            if list_items:
                chunks.append("<ul>" + "".join(f"<li>{item}</li>" for item in list_items) + "</ul>")
                list_items = []
            if stripped:
                chunks.append(f"<p>{html.escape(stripped)}</p>")
        if list_items:
            chunks.append("<ul>" + "".join(f"<li>{item}</li>" for item in list_items) + "</ul>")
        if code_lines:
            chunks.append('<pre class="code-block"><code>' + html.escape("\n".join(code_lines)) + "</code></pre>")
        return "".join(chunks)

    def _render_guide(self, lesson: Lesson) -> None:
        guide_sections = lesson.guide_sections()
        if guide_sections:
            sections_html = "<h1>Tutorial paso a paso</h1>" + "".join(
                f"<h2>{html.escape(section.get('title', ''))}</h2>"
                f"{self._guide_html_from_text(section.get('content', ''))}"
                for section in guide_sections
            )
        else:
            sections_html = f"<h1>Tutorial paso a paso</h1>{self._guide_html_from_text(lesson.tutorial())}"

        examples = lesson.code_examples()
        if examples:
            resumen = examples[:2]
            resumen_html = "<h2>Resumen de ejemplos</h2>" + "".join(
                f"<h3>{html.escape(title)}</h3><pre><code>{html.escape(code)}</code></pre>"
                for title, code in resumen
            )
        else:
            resumen_html = ""

        if self.current_theme == "dark":
            text_color = "#e6e6e6"
            code_text = "#e6e6e6"
            code_background = "#2a2a2a"
            code_border = "#3a3a3a"
            keyword_color = "#d6b86a"
            keyword_border = "#b8953d"
        else:
            text_color = "#1f2937"
            code_text = "#e2e8f0"
            code_background = "#0f172a"
            code_border = "#1e293b"
            keyword_color = "#3b5b8a"
            keyword_border = "#8aa0c8"

        html_content = f"""
        <html>
        <head>
        <style>
            body {{ font-family: 'Segoe UI'; color: {text_color}; }}
            h1 {{ font-size: 22px; margin-bottom: 8px; }}
            h2 {{ font-size: 18px; margin-top: 16px; }}
            h3 {{ font-size: 16px; margin-top: 14px; }}
            p {{ line-height: 1.5; color: {text_color}; }}
            ul {{ margin-left: 18px; color: {text_color}; }}
            .code-block {{
                background: {code_background};
                color: {code_text};
                padding: 12px;
                border-radius: 10px;
                border: 1px solid {code_border};
            }}
            code {{ font-family: "Consolas"; }}
            .kw {{
                color: {keyword_color};
                text-decoration: underline dotted {keyword_border};
                text-underline-offset: 3px;
                cursor: help;
            }}
        </style>
        </head>
        <body>
            {sections_html}
            {resumen_html}
        </body>
        </html>
        """
        html_content = tooltipify_html(html_content)
        self.guide_text.setHtml(html_content)
        self.guide_text.document().setTextWidth(self.guide_text.viewport().width())
        content_height = int(self.guide_text.document().size().height())
        self.guide_text.setMinimumHeight(content_height + 40)

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
            can_run, reason = self.runner.can_run(code)
            callback = self._run_snippet if can_run else None
            card = CodeCard(title, code, show_run=True, run_callback=callback)
            if card.output_view is not None and not can_run:
                card.output_view.setPlainText(reason or "No se puede ejecutar este snippet.")
                if card.run_button is not None:
                    card.run_button.setToolTip(reason or "No se puede ejecutar este snippet.")
            self.examples_layout.addWidget(card)

        self.examples_layout.addStretch()

    def _run_snippet(self, code: str, output_view: QTextEdit | None, _code_view: QTextEdit) -> None:
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
            box.setCheckable(True)
            box.setChecked(True)
            layout = QVBoxLayout(box)
            content = QWidget()
            content_layout = QVBoxLayout(content)
            question = QLabel(exercise.get("question", ""))
            question.setWordWrap(True)
            content_layout.addWidget(question)

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

            content_layout.addLayout(actions)
            content_layout.addWidget(hints_view)
            content_layout.addWidget(solution_view)
            layout.addWidget(content)
            box.toggled.connect(content.setVisible)
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

    def _update_theme_toggle(self) -> None:
        if self.current_theme == "dark":
            self.theme_toggle.setText("☀️")
            self.theme_toggle.setToolTip("Cambiar a tema claro")
        else:
            self.theme_toggle.setText("🌙")
            self.theme_toggle.setToolTip("Cambiar a tema oscuro")

    def _toggle_theme(self) -> None:
        self.current_theme = toggle_theme(self.current_theme)
        self.settings.setValue("ui/theme", self.current_theme)
        apply_theme(self.app, self.current_theme)
        self._update_theme_toggle()
        if hasattr(self, "current_entry"):
            self._render_guide(self.current_entry.instance)


def main() -> None:
    app = QApplication(sys.argv)
    style_hints = app.styleHints()
    style_hints.setToolTipWakeUpDelay(0)
    style_hints.setToolTipFallAsleepDelay(0)
    style_hints.setToolTipDuration(0)
    settings = QSettings("Pythonpedia", "Pythonpedia")
    theme_name = settings.value("ui/theme", "light")
    if not isinstance(theme_name, str):
        theme_name = "light"
    apply_theme(app, theme_name)
    window = MainWindow(app, settings, theme_name)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
