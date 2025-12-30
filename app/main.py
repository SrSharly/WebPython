from __future__ import annotations

import html
import logging
import re
import sys
from dataclasses import dataclass
from urllib.parse import quote

from PySide6.QtCore import QEvent, QObject, QPoint, QRect, QSettings, Qt
from PySide6.QtGui import QGuiApplication, QKeySequence, QShortcut
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
from app.ui.library_reference_view import LibraryReferenceView
from app.ui.method_reference_view import MethodReferenceView
from app.utils.glossary import GLOSSARY, definition_text, register_auto_terms
from app.utils.mention_indexer import (
    build_mention_index,
    get_related_terms,
    get_lesson_terms,
    get_term_label,
    get_term_meta,
    resolve_mention_index,
)
from app.utils.theme import apply_theme, toggle_theme
from app.utils.tooltip_controller import InstantTooltipController
from app.utils.tooltipify import tooltipify_html
from app.utils.ui_helpers import badge
from app.utils.validators import warn_if_short_example

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


@dataclass
class LessonEntry:
    info_title: str
    info_category: str
    info_subcategory: str
    info_level: str
    info_tags: list[str]
    info_badges: list[str]
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
        self.guide_text = QTextBrowser()
        self.guide_text.setLineWrapMode(QTextEdit.WidgetWidth)
        self.guide_text.setOpenExternalLinks(False)
        self.guide_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.guide_text.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.guide_text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self._tooltip_controller = InstantTooltipController(self.guide_text)
        self.guide_text.installEventFilter(self._tooltip_controller)
        self._tooltip_controller.termPinned.connect(self._on_term_pinned)
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
        self.pitfall_detail = QTextEdit()
        self.pitfall_detail.setReadOnly(True)
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

        self.glossary_view = GlossaryView()
        self.glossary_view.termSelected.connect(self._on_term_pinned)
        self.method_reference_view = MethodReferenceView()
        self.method_reference_view.termSelected.connect(self._on_term_pinned)
        self.library_reference_view = LibraryReferenceView()

        self.tabs.addTab(self.guide_scroll, "Tutorial")
        self.tabs.addTab(pitfalls_panel, "Errores típicos")
        self.tabs.addTab(self.exercises_scroll, "Ejercicios")
        self.tabs.addTab(self.method_reference_view, "Métodos y funciones")
        self.tabs.addTab(self.glossary_view, "Glosario")
        self.tabs.addTab(self.library_reference_view, "Librerías")

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

        self.definition_panel = QFrame()
        self.definition_panel.setObjectName("DefinitionPanel")
        definition_layout = QVBoxLayout(self.definition_panel)
        definition_layout.setContentsMargins(12, 12, 12, 12)
        definition_layout.setSpacing(8)
        self.definition_title = QLabel("Definición")
        self.definition_title.setObjectName("DefinitionTitle")
        self.definition_term = QLabel()
        self.definition_term.setObjectName("DefinitionTerm")
        self.definition_term.setVisible(False)
        self.definition_body = QTextBrowser()
        self.definition_body.setReadOnly(True)
        self.definition_body.setOpenExternalLinks(False)
        if hasattr(self.definition_body, "setOpenLinks"):
            self.definition_body.setOpenLinks(False)
        self.definition_body.setObjectName("DefinitionBody")
        definition_buttons = QHBoxLayout()
        self.definition_copy = QPushButton("Copiar")
        self.definition_close = QPushButton("Cerrar")
        self.definition_close.setProperty("secondary", True)
        self.definition_copy.clicked.connect(self._copy_definition)
        self.definition_close.clicked.connect(self._clear_definition_panel)
        definition_buttons.addWidget(self.definition_copy)
        definition_buttons.addWidget(self.definition_close)
        definition_buttons.addStretch()
        definition_layout.addWidget(self.definition_title)
        definition_layout.addWidget(self.definition_term)
        definition_layout.addWidget(self.definition_body, 1)
        definition_layout.addLayout(definition_buttons)

        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        right_layout.addWidget(self.header_widget)
        content_splitter = QSplitter()
        content_splitter.addWidget(self.tabs)
        content_splitter.addWidget(self.definition_panel)
        content_splitter.setSizes([860, 320])
        right_layout.addWidget(content_splitter)
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
        self._pinned_term: str | None = None
        self._clear_definition_panel()
        self.app.installEventFilter(self)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.MouseButtonPress and self._pinned_term:
            if self._click_inside_definition_panel(event):
                return super().eventFilter(watched, event)
            if self._click_on_tip_anchor(watched, event):
                return super().eventFilter(watched, event)
            self._clear_definition_panel()
        return super().eventFilter(watched, event)

    def _click_inside_definition_panel(self, event: QEvent) -> bool:
        global_pos = self._event_global_pos(event)
        if global_pos is None:
            return False
        top_left = self.definition_panel.mapToGlobal(QPoint(0, 0))
        rect = QRect(top_left, self.definition_panel.size())
        return rect.contains(global_pos)

    def _click_on_tip_anchor(self, watched: QObject, event: QEvent) -> bool:
        if watched not in {self.guide_text, self.guide_text.viewport()}:
            return False
        pos = self._event_local_pos(event)
        if pos is None:
            return False
        if watched is self.guide_text:
            pos = self.guide_text.viewport().mapFrom(self.guide_text, pos)
        anchor = self.guide_text.anchorAt(pos)
        return anchor.startswith("tip:")

    def _event_global_pos(self, event: QEvent) -> QPoint | None:
        if hasattr(event, "globalPosition"):
            return event.globalPosition().toPoint()
        if hasattr(event, "globalPos"):
            return event.globalPos()
        return None

    def _event_local_pos(self, event: QEvent) -> QPoint | None:
        if hasattr(event, "position"):
            return event.position().toPoint()
        if hasattr(event, "pos"):
            return event.pos()
        return None

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
                info_badges=self._extract_lesson_badges(info.lesson_cls),
                lesson_cls=info.lesson_cls,
                instance=instance,
                search_text=search_text,
            )
            self.lesson_entries.append(entry)

        if self.lesson_entries:
            build_mention_index([entry.instance for entry in self.lesson_entries])
            resolved = resolve_mention_index(GLOSSARY)
            register_auto_terms(resolved.auto_terms)
            self.glossary_view.load_terms(
                GLOSSARY,
                resolved.term_meta,
                resolved.term_labels,
                resolved.term_related,
            )
            self.method_reference_view.load_terms(
                GLOSSARY,
                resolved.term_meta,
                resolved.term_labels,
            )

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
            badge_prefix = self._badge_prefix(entry.info_badges)
            lesson_item = QTreeWidgetItem([f"{badge_prefix}{entry.info_title}"])
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

    def _extract_lesson_badges(self, lesson_cls: type[Lesson]) -> list[str]:
        badges = list(getattr(lesson_cls, "BADGES", []) or [])
        lesson_badge = str(getattr(lesson_cls, "LESSON_BADGE", "") or "")
        for icon in ("⭐", "🧠"):
            if icon in lesson_badge and icon not in badges:
                badges.append(icon)
        return badges

    def _badge_prefix(self, badges: list[str]) -> str:
        has_star = "⭐" in badges
        has_pro = "🧠" in badges
        if has_star and has_pro:
            return "⭐🧠 "
        if has_star:
            return "⭐ "
        if has_pro:
            return "🧠 "
        return ""

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

        self._render_guide(lesson)
        self._render_pitfalls(lesson)
        self._render_exercises(lesson)
        self._scroll_to_top()

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
        callout: dict[str, object] | None = None
        callout_list_items: list[str] = []
        section_index = 0
        callout_index = 0
        subsection_index = 0
        list_mode = "default"
        paragraph_lines: list[str] = []
        skip_section_level: int | None = None

        def normalize_title(title: str) -> str:
            cleaned = title.lower().strip()
            return (
                cleaned.replace("á", "a")
                .replace("é", "e")
                .replace("í", "i")
                .replace("ó", "o")
                .replace("ú", "u")
            )

        def should_skip_section(title: str) -> bool:
            normalized = normalize_title(title)
            return (
                "operaciones y metodos mas utiles" in normalized
                or "metodos mencionados" in normalized
            )

        callout_pattern = re.compile(
            r"^(?P<title>.+?)\s*\(CalloutBox:\s*(?P<variant>[a-z_]+)\s*\)$",
            re.IGNORECASE,
        )

        def render_callout(title: str, variant: str, body_html: str) -> str:
            nonlocal callout_index
            meta = {
                "best_practice": {"label": "Buenas prácticas", "icon": "✅", "class": "best"},
                "note": {"label": "Nota", "icon": "💡", "class": "note"},
                "warning": {"label": "Advertencia", "icon": "⚠️", "class": "warn"},
                "definition": {"label": "Definición", "icon": "📌", "class": "definition"},
            }
            info = meta.get(variant, {"label": title, "icon": "💬", "class": "note"})
            if variant == "best_practice":
                display_title = info["label"]
            else:
                display_title = title or info["label"]
            callout_index += 1
            alt_class = " alt" if callout_index % 2 == 0 else ""
            return (
                f"<div class=\"card callout {info['class']}{alt_class}\">"
                f"<div class=\"card-header\">"
                f"<span class=\"card-icon\">{info['icon']}</span>"
                f"<span class=\"card-title\">{html.escape(display_title)}</span>"
                "</div>"
                f"<div class=\"card-body\">{body_html}</div>"
                "</div>"
            )

        def render_code_card(code: str) -> str:
            return (
                "<div class=\"code-card\">"
                "<div class=\"code-head\">Código</div>"
                f"<pre class=\"code-body\">{html.escape(code)}</pre>"
                "</div>"
            )

        def flush_paragraph() -> None:
            nonlocal paragraph_lines
            if not paragraph_lines:
                return
            text_content = " ".join(part.strip() for part in paragraph_lines if part.strip())
            if text_content:
                if callout is not None:
                    body = callout.setdefault("body", [])
                    if isinstance(body, list):
                        body.append(f"<p>{html.escape(text_content)}</p>")
                else:
                    chunks.append(f"<p>{html.escape(text_content)}</p>")
            paragraph_lines = []

        def flush_list_items() -> None:
            nonlocal list_items
            if list_items:
                if list_mode == "pro":
                    chunks.append(
                        "<div class=\"pro-list\">"
                        + "".join(f"<div class=\"pro-item\">{item}</div>" for item in list_items)
                        + "</div>"
                    )
                else:
                    chunks.append("<ul>" + "".join(f"<li>{item}</li>" for item in list_items) + "</ul>")
                list_items = []

        def flush_callout_list() -> None:
            nonlocal callout_list_items
            if callout is not None and callout_list_items:
                body = callout.setdefault("body", [])
                if isinstance(body, list):
                    body.append("<ul>" + "".join(f"<li>{item}</li>" for item in callout_list_items) + "</ul>")
                callout_list_items = []

        def flush_callout() -> None:
            nonlocal callout
            if callout is None:
                return
            flush_callout_list()
            body_parts = callout.get("body", [])
            body_html = "".join(body_parts) if isinstance(body_parts, list) else ""
            chunks.append(
                render_callout(
                    str(callout.get("title", "")),
                    str(callout.get("variant", "note")),
                    body_html,
                )
            )
            callout = None

        for line in lines:
            stripped = line.strip()
            if stripped.startswith("```"):
                if in_code_block:
                    chunks.append(render_code_card("\n".join(code_lines)))
                    code_lines = []
                    in_code_block = False
                else:
                    flush_paragraph()
                    if callout is not None:
                        flush_callout()
                    flush_list_items()
                    in_code_block = True
                continue
            if in_code_block:
                code_lines.append(line)
                continue
            if stripped.startswith(("## ", "### ")):
                level = 2 if stripped.startswith("## ") else 3
                title = stripped[3 if level == 2 else 4 :].strip()
                if skip_section_level is not None:
                    if level <= skip_section_level:
                        skip_section_level = None
                    else:
                        continue
                if should_skip_section(title):
                    flush_paragraph()
                    flush_list_items()
                    if callout is not None:
                        flush_callout()
                    skip_section_level = level
                    continue
                if level == 3:
                    flush_paragraph()
                    flush_list_items()
                    if callout is not None:
                        flush_callout()
                    if subsection_index > 0:
                        chunks.append("<div class=\"subsection-divider\"></div>")
                    subsection_index += 1
                    list_mode = (
                        "pro"
                        if "consejo" in title.lower() and "pro" in title.lower()
                        else "default"
                    )
                    match = callout_pattern.match(title)
                    if match:
                        callout = {
                            "title": match.group("title").strip(),
                            "variant": match.group("variant").strip().lower(),
                            "body": [],
                        }
                    else:
                        if title.lower().startswith("paso") and ":" in title:
                            step, detail = title.split(":", 1)
                            chunks.append(
                                "<h3 class=\"step-title\">"
                                f"<span class=\"step-badge\">{html.escape(step.strip())}</span>"
                                f"{html.escape(detail.strip())}</h3>"
                            )
                        else:
                            chunks.append(f"<h3>{html.escape(title)}</h3>")
                    continue
                flush_paragraph()
                flush_list_items()
                if callout is not None:
                    flush_callout()
                if section_index > 0:
                    chunks.append("<div class=\"section-divider\"></div>")
                section_index += 1
                subsection_index = 0
                list_mode = (
                    "pro"
                    if "consejo" in title.lower() and "pro" in title.lower()
                    else "default"
                )
                chunks.append(f"<h2>{html.escape(title)}</h2>")
                continue
            if skip_section_level is not None:
                continue
            if stripped.startswith(("-", "*")):
                flush_paragraph()
                if callout is not None:
                    callout_list_items.append(html.escape(stripped[1:].strip()))
                else:
                    list_items.append(html.escape(stripped[1:].strip()))
                continue
            flush_list_items()
            if stripped:
                paragraph_lines.append(stripped)
            else:
                flush_paragraph()
        if list_items:
            flush_list_items()
        flush_paragraph()
        if callout is not None:
            flush_callout()
        if code_lines:
            chunks.append(render_code_card("\n".join(code_lines)))
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

        mentioned_html = self._mentioned_methods_html(lesson)
        examples_html = self._examples_html(lesson)

        if self.current_theme == "dark":
            theme_class = "theme-dark"
            text_color = "#e6e6e6"
            heading_color = "#f8f0d4"
            muted_text = "#cbd5e1"
            code_text = "#e5e7eb"
            code_background = "#0f172a"
            code_border = "#1f2937"
            keyword_color = "#d6b86a"
            keyword_border = "#b8953d"
            keyword_hover = "#e6c87b"
            card_border = "#2c2c2c"
            card_bg = "#141414"
            card_header = "#1f2937"
            accent_code = "#d4af37"
            accent_best = "#7cc992"
            accent_note = "#7aa2c7"
            accent_warn = "#d4a64a"
            accent_definition = "#b294ff"
            bg_best = "#1f2a22"
            bg_note = "#1f2a3a"
            bg_warn = "#3a2f1f"
            bg_definition = "#2d2639"
            divider = "#2f2f2f"
            summary_bg = "#1a2433"
        else:
            theme_class = "theme-light"
            text_color = "#1f2937"
            heading_color = "#0f172a"
            muted_text = "#4b5563"
            code_text = "#e2e8f0"
            code_background = "#0b1220"
            code_border = "#111827"
            keyword_color = "#3b5b8a"
            keyword_border = "#8aa0c8"
            keyword_hover = "#2f4c79"
            card_border = "#d7dde8"
            card_bg = "#ffffff"
            card_header = "#f3f6fb"
            accent_code = "#d4af37"
            accent_best = "#3f7a57"
            accent_note = "#4d6fa1"
            accent_warn = "#d4883a"
            accent_definition = "#7a63d2"
            bg_best = "#f2f7ef"
            bg_note = "#eef4ff"
            bg_warn = "#fff3e2"
            bg_definition = "#f3f0ff"
            divider = "#e2e8f0"
            summary_bg = "#edf2ff"

        summary_text = lesson.summary().strip()
        summary_html = ""
        if summary_text:
            summary_html = (
                "<div class=\"card summary-card\">"
                "<div class=\"card-header\">"
                "<span class=\"card-icon\">🧭</span>"
                "<span class=\"card-title\">Resumen rápido</span>"
                "</div>"
                f"<div class=\"card-body\"><p>{html.escape(summary_text)}</p></div>"
                "</div>"
            )

        html_content = f"""
        <html>
        <head>
        <style>
            body {{
                font-family: 'Segoe UI';
                color: {text_color};
                margin: 0;
                padding: 0;
            }}
            .content {{
                max-width: 920px;
                margin: 0 auto;
                padding: 16px 18px 24px;
            }}
            h1 {{
                font-size: 24px;
                margin: 4px 0 12px;
                color: {heading_color};
            }}
            h2 {{
                font-size: 19px;
                margin-top: 22px;
                color: {heading_color};
            }}
            h3 {{
                font-size: 16px;
                margin-top: 14px;
                color: {heading_color};
            }}
            p {{
                line-height: 1.6;
                color: {text_color};
                margin: 8px 0;
            }}
            ul {{
                margin: 10px 0 10px 22px;
                color: {text_color};
                padding: 0;
            }}
            li {{
                margin-bottom: 6px;
            }}
            .section-divider {{
                border-top: 1px solid {divider};
                margin: 18px 0 8px;
            }}
            .subsection-divider {{
                border-top: 1px solid {divider};
                margin: 14px 0 6px;
                opacity: 0.7;
            }}
            .card {{
                border-radius: 12px;
                padding: 0;
                border: 1px solid {card_border};
                margin: 16px auto;
                max-width: 860px;
                background: {card_bg};
                overflow: hidden;
                box-shadow: 0 6px 16px rgba(0, 0, 0, 0.08);
            }}
            .card-header {{
                display: flex;
                align-items: center;
                gap: 8px;
                font-weight: 600;
                padding: 10px 14px;
                background: {card_header};
                border-bottom: 1px solid {card_border};
                color: {heading_color};
            }}
            .card-body {{
                padding: 12px 14px 14px;
            }}
            .card-icon {{
                font-size: 14px;
            }}
            .code-card {{
                max-width: clamp(520px, 60%, 900px);
                margin: 14px auto;
                border-radius: 12px;
                overflow: hidden;
                border: 1px solid {code_border};
                background: {card_bg};
                box-shadow: 0 6px 16px rgba(0, 0, 0, 0.08);
            }}
            .code-head {{
                padding: 10px 12px;
                font-weight: 600;
                background: {card_header};
                border-bottom: 1px solid {code_border};
                color: {heading_color};
            }}
            .code-body {{
                margin: 0;
                padding: 12px 14px;
                font-family: "Consolas";
                font-size: 12px;
                white-space: pre;
                overflow-x: auto;
                background: {code_background};
                color: {code_text};
            }}
            .callout.best {{
                border-left: 4px solid {accent_best};
            }}
            .callout.note {{
                border-left: 4px solid {accent_note};
            }}
            .callout.warn {{
                border-left: 4px solid {accent_warn};
            }}
            .callout.definition {{
                border-left: 4px solid {accent_definition};
            }}
            .callout.best .card-body {{ background: {bg_best}; }}
            .callout.note .card-body {{ background: {bg_note}; }}
            .callout.warn .card-body {{ background: {bg_warn}; }}
            .callout.definition .card-body {{ background: {bg_definition}; }}
            .callout.alt {{
                border-left: none;
                border-right: 4px solid {accent_note};
            }}
            code {{ font-family: "Consolas"; }}
            a.kw {{
                color: {keyword_color};
                text-decoration: underline dotted {keyword_border};
                text-underline-offset: 3px;
                cursor: pointer;
            }}
            a.kw:hover {{
                color: {keyword_hover};
                text-decoration-color: {keyword_hover};
            }}
            .step-title {{
                display: flex;
                align-items: center;
                gap: 10px;
            }}
            .step-badge {{
                display: inline-flex;
                align-items: center;
                padding: 2px 10px;
                border-radius: 999px;
                background: {card_header};
                color: {heading_color};
                font-size: 12px;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.6px;
            }}
            .pro-list {{
                display: grid;
                gap: 10px;
                margin: 10px 0;
            }}
            .pro-item {{
                padding: 10px 12px;
                border-radius: 10px;
                border: 1px solid {card_border};
                background: {card_header};
                color: {text_color};
            }}
            .summary-card .card-body {{
                background: {summary_bg};
            }}
            .method-index.card {{
                border: 1px dashed {divider};
                border-radius: 12px;
                margin: 16px 0;
                background: {card_bg};
                overflow: hidden;
            }}
            .method-index .card-header {{
                background: {card_header};
                padding: 8px 12px;
                font-weight: 600;
                color: {heading_color};
            }}
            .method-index .card-body {{
                padding: 8px 12px 10px;
            }}
            .method-index-group {{
                display: flex;
                flex-wrap: wrap;
                gap: 6px 10px;
                align-items: center;
                margin-bottom: 6px;
            }}
            .method-index-group:last-child {{
                margin-bottom: 0;
            }}
            .method-index-owner {{
                font-weight: 600;
                color: {heading_color};
                margin-right: 4px;
            }}
        </style>
        </head>
        <body class="{theme_class}">
            <div class="content">
                {summary_html}
                {sections_html}
                {mentioned_html}
                {examples_html}
            </div>
        </body>
        </html>
        """
        html_content = tooltipify_html(html_content, lesson)
        self.guide_text.setHtml(html_content)
        self.guide_text.document().setTextWidth(self.guide_text.viewport().width())
        content_height = int(self.guide_text.document().size().height())
        self.guide_text.setMinimumHeight(content_height + 40)

    def _examples_html(self, lesson: Lesson) -> str:
        examples = lesson.code_examples()
        if not examples:
            return ""
        example_blocks = []
        for title, code in examples:
            warn_if_short_example(code, f"Lesson: {lesson.TITLE} - {title}")
            example_blocks.append(
                f"<h3>{html.escape(title)}</h3>"
                "<div class=\"code-card\">"
                "<div class=\"code-head\">Código</div>"
                f"<pre class=\"code-body\">{html.escape(code)}</pre>"
                "</div>"
            )
        return "<h2>Ejemplos guiados</h2>" + "".join(example_blocks)

    def _mentioned_methods_html(self, lesson: Lesson) -> str:
        term_ids = get_lesson_terms(lesson)
        if not term_ids:
            return ""

        method_ids: list[str] = []
        function_ids: list[str] = []
        for term_id in term_ids:
            meta = get_term_meta(term_id)
            kind = meta.get("kind")
            if kind == "method":
                method_ids.append(term_id)
            elif kind in {"function", "builtin"}:
                function_ids.append(term_id)

        if not method_ids and not function_ids:
            return ""

        groups: list[tuple[str, list[str]]] = []
        owner_map: dict[str, list[str]] = {}
        for term_id in method_ids:
            owner = get_term_meta(term_id).get("owner") or "métodos"
            owner_map.setdefault(owner, []).append(term_id)
        for owner in sorted(owner_map):
            groups.append((owner, owner_map[owner]))
        if function_ids:
            groups.append(("funciones", function_ids))

        total = sum(len(group_terms) for _group, group_terms in groups)
        group_html: list[str] = []
        for group, group_terms in groups:
            links = " ".join(
                f'<a href="tip:{quote(term_id)}" class="kw">{html.escape(get_term_label(term_id))}</a>'
                for term_id in sorted(group_terms, key=lambda tid: get_term_label(tid).lower())
            )
            group_label = f"{group} ({len(group_terms)})"
            group_html.append(
                "<div class=\"method-index-group\">"
                f"<span class=\"method-index-owner\">{html.escape(group_label)}:</span>"
                f"{links}"
                "</div>"
            )

        return (
            "<div class=\"method-index card\">"
            f"<div class=\"card-header\">Métodos/funciones mencionados en esta lección ({total})</div>"
            "<div class=\"card-body\">"
            + "".join(group_html)
            + "</div></div>"
        )

    def _render_pitfalls(self, lesson: Lesson) -> None:
        self.pitfalls_list.clear()
        self.pitfall_detail.clear()
        for title, detail in lesson.common_pitfalls():
            item = QListWidgetItem(title)
            item.setData(Qt.UserRole, detail)
            self.pitfalls_list.addItem(item)
        if self.pitfalls_list.count() > 0:
            self.pitfalls_list.setCurrentRow(0)

    def _scroll_to_top(self) -> None:
        if self.guide_scroll.verticalScrollBar():
            self.guide_scroll.verticalScrollBar().setValue(0)
        if self.exercises_scroll.verticalScrollBar():
            self.exercises_scroll.verticalScrollBar().setValue(0)

    def _on_pitfall_selected(self, current: QListWidgetItem, _previous: QListWidgetItem | None = None) -> None:
        if current is None:
            self.pitfall_detail.clear()
            return
        detail = current.data(Qt.UserRole)
        self.pitfall_detail.setPlainText(detail)

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
            hints_view = QTextEdit()
            hints_view.setReadOnly(True)
            hints_view.setPlainText("\n".join(exercise.get("hints", [])))
            hints_view.setVisible(False)
            hints_btn.clicked.connect(lambda _, v=hints_view: v.setVisible(not v.isVisible()))

            solution_btn = QPushButton("Ver solución")
            solution_view = QTextEdit()
            solution_view.setReadOnly(True)
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
        if self._pinned_term:
            data = GLOSSARY.get(self._pinned_term)
            if data:
                self.definition_body.setHtml(self._definition_html(self._pinned_term, data))

    def _on_term_pinned(self, term_id: str) -> None:
        data = GLOSSARY.get(term_id)
        if not data:
            return
        self._pinned_term = term_id
        self.definition_term.setVisible(False)
        self.definition_body.setHtml(self._definition_html(term_id, data))

    def _clear_definition_panel(self) -> None:
        self._pinned_term = None
        self.definition_term.clear()
        self.definition_term.setVisible(False)
        self.definition_body.setHtml(self._definition_empty_html())

    def _copy_definition(self) -> None:
        if not self._pinned_term:
            return
        data = GLOSSARY.get(self._pinned_term)
        if not data:
            return
        QGuiApplication.clipboard().setText(definition_text(data))

    def _definition_empty_html(self) -> str:
        return self._definition_html(
            "Definición",
            {"definition": "Haz clic en una palabra resaltada para fijar su definición."},
        )

    def _definition_html(self, term_id: str, data: dict[str, object]) -> str:
        if self.current_theme == "dark":
            text_color = "#e6e6e6"
            muted_text = "#c9c9c9"
            card_bg = "#262626"
            card_border = "#3a3a3a"
            chip_bg = "#2e2e2e"
            chip_text = "#f7f2e4"
            separator = "#3a3a3a"
            code_bg = "#0b1220"
            code_border = "#1f2937"
        else:
            text_color = "#1f2937"
            muted_text = "#4b5563"
            card_bg = "#f8f9fc"
            card_border = "#e1e5ef"
            chip_bg = "#eef1f7"
            chip_text = "#1f2937"
            separator = "#e2e8f0"
            code_bg = "#0b1220"
            code_border = "#111827"

        definition_parts = data.get("definition_parts")
        if not isinstance(definition_parts, dict):
            definition_parts = self._parse_legacy_definition(str(data.get("definition", "")).strip())

        sections_html = ""
        if definition_parts:
            sections_html = self._render_definition_sections(definition_parts)
        else:
            definition_text_raw = str(data.get("definition", "")).strip()
            sections_html = self._render_definition_paragraphs(definition_text_raw)

        related = get_related_terms(term_id)
        related_html = ""
        if related:
            links = " ".join(
                f'<a href="tip:{quote(related_id)}" class="kw">{html.escape(get_term_label(related_id))}</a>'
                for related_id in related
            )
            related_html = f"<div class=\"related\"><strong>Relacionado con:</strong> {links}</div>"

        return f"""
        <html>
        <head>
        <style>
            body {{ font-family: 'Segoe UI'; color: {text_color}; }}
            .definition-card {{
                background: {card_bg};
                border: 1px solid {card_border};
                border-radius: 14px;
                padding: 14px;
            }}
            .def-chip {{
                display: inline-block;
                background: {chip_bg};
                color: {chip_text};
                padding: 4px 12px;
                border-radius: 999px;
                font-weight: 600;
                margin-bottom: 10px;
            }}
            .def-section {{
                margin-top: 12px;
            }}
            .def-section h3 {{
                margin: 0 0 6px;
                font-size: 14px;
            }}
            .def-section p {{
                margin: 0 0 8px;
                color: {text_color};
            }}
            .def-list {{
                margin: 0 0 8px 18px;
                color: {text_color};
            }}
            .def-separator {{
                border: none;
                border-top: 1px solid {separator};
                margin: 10px 0;
            }}
            .def-muted {{
                color: {muted_text};
            }}
            .codebox {{
                background: {code_bg};
                color: #e2e8f0;
                padding: 10px;
                border-radius: 10px;
                border: 1px solid {code_border};
                font-family: "Consolas";
                font-size: 12px;
                margin: 0;
                white-space: pre-wrap;
            }}
            .related {{
                margin-top: 12px;
                font-size: 13px;
            }}
        </style>
        </head>
        <body>
            <div class="definition-card">
                <div class="def-chip">{html.escape(term_id)}</div>
                {sections_html}
                {related_html}
            </div>
        </body>
        </html>
        """

    def _render_definition_paragraphs(self, text: str) -> str:
        if not text:
            return "<p class=\"def-muted\">Sin contenido disponible.</p>"
        paragraphs = [html.escape(part.strip()) for part in re.split(r"(?<=[.!?])\s+", text) if part.strip()]
        return "".join(f"<p>{para}</p>" for para in paragraphs)

    def _parse_legacy_definition(self, text: str) -> dict[str, object] | None:
        if not text:
            return None
        sentences = re.split(r"(?<=[.!?])\s+", text)
        parts: dict[str, object] = {}
        que_es: list[str] = []
        para_que: list[str] = []
        ver_tambien: list[str] = []
        ejemplo = ""
        error_tipico = ""

        for sentence in sentences:
            cleaned = sentence.strip()
            if not cleaned:
                continue
            lowered = cleaned.lower()
            if lowered.startswith(("se usa", "se utiliza", "se emplea", "sirve para")):
                para_que.append(cleaned)
                continue
            if lowered.startswith("ejemplo"):
                ejemplo = re.sub(r"^ejemplo:?\s*", "", cleaned, flags=re.IGNORECASE)
                continue
            if lowered.startswith("error típico") or lowered.startswith("error tipico"):
                error_tipico = re.sub(r"^error típico:?\s*", "", cleaned, flags=re.IGNORECASE)
                error_tipico = re.sub(r"^error tipico:?\s*", "", error_tipico, flags=re.IGNORECASE)
                continue
            if lowered.startswith("ver también") or lowered.startswith("ver tambien"):
                raw = re.sub(r"^ver también:?\s*", "", cleaned, flags=re.IGNORECASE)
                raw = re.sub(r"^ver tambien:?\s*", "", raw, flags=re.IGNORECASE)
                ver_tambien.extend([item.strip() for item in raw.split(",") if item.strip()])
                continue
            que_es.append(cleaned)

        if not any([que_es, para_que, ejemplo, error_tipico, ver_tambien]):
            return None

        if que_es:
            parts["que_es"] = " ".join(que_es)
        if para_que:
            parts["para_que"] = para_que
        if ejemplo:
            parts["ejemplo"] = ejemplo
        if error_tipico:
            parts["error_tipico"] = error_tipico
        if ver_tambien:
            parts["ver_tambien"] = ver_tambien
        return parts

    def _render_definition_sections(self, parts: dict[str, object]) -> str:
        section_titles = {
            "que_es": "Qué es",
            "para_que": "Para qué sirve",
            "ejemplo": "Ejemplo",
            "error_tipico": "Error típico",
            "ver_tambien": "Ver también",
        }
        order = ["que_es", "para_que", "ejemplo", "error_tipico", "ver_tambien"]
        sections: list[str] = []

        for key in order:
            if key not in parts:
                continue
            content = parts[key]
            body_html = self._definition_section_body_html(key, content)
            sections.append(
                f"<div class=\"def-section\"><h3>{section_titles[key]}</h3>{body_html}</div>"
            )

        if not sections:
            return f"<p class=\"def-muted\">Sin contenido disponible.</p>"

        return "<hr class=\"def-separator\"/>".join(sections)

    def _definition_section_body_html(self, key: str, content: object) -> str:
        if isinstance(content, list):
            items = "".join(f"<li>{html.escape(str(item))}</li>" for item in content)
            return f"<ul class=\"def-list\">{items}</ul>"
        text = html.escape(str(content))
        if key == "ejemplo" and self._looks_like_code(str(content)):
            return f"<pre class=\"codebox\">{text}</pre>"
        return f"<p>{text}</p>"

    def _looks_like_code(self, text: str) -> bool:
        if "\n" in text:
            return True
        return bool(re.search(r"\b(def|class|print|for|if|while|return)\b|[=():]", text))


def main() -> None:
    app = QApplication(sys.argv)
    style_hints = app.styleHints()
    if hasattr(style_hints, "setToolTipWakeUpDelay"):
        style_hints.setToolTipWakeUpDelay(0)
    if hasattr(style_hints, "setToolTipFallAsleepDelay"):
        style_hints.setToolTipFallAsleepDelay(0)
    if hasattr(style_hints, "setToolTipDuration"):
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
