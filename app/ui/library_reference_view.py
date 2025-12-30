from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from app.utils.library_catalog import LIBRARIES
from app.utils.library_search import build_search_text, iter_library_items
from app.utils.validators import warn_if_short_example
from app.utils.ui_components import CodeCard
from app.utils.ui_helpers import badge


class LibraryItemWidget(QWidget):
    def __init__(self, name: str, category: str, is_common: bool) -> None:
        super().__init__()
        layout = QHBoxLayout(self)
        layout.setContentsMargins(6, 2, 6, 2)
        layout.setSpacing(8)

        title = QLabel(name)
        title.setObjectName("LibraryItemTitle")
        layout.addWidget(title, 1)

        if is_common:
            common_badge = badge("COMÚN", accent=None, variant="common")
            layout.addWidget(common_badge, alignment=Qt.AlignRight)

        category_label = badge(category, accent=None, variant="category")
        layout.addWidget(category_label, alignment=Qt.AlignRight)


class LibraryReferenceView(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Buscar función/clase...")
        self.search_input.setClearButtonEnabled(True)
        self.search_input.textChanged.connect(self._apply_filter)

        self.library_filter = QComboBox()
        self.library_filter.currentIndexChanged.connect(self._apply_filter)

        self.common_only = QCheckBox("Solo comunes")
        self.common_only.stateChanged.connect(self._apply_filter)

        search_row = QHBoxLayout()
        search_row.addWidget(self.search_input, 3)
        search_row.addWidget(self.library_filter, 1)
        search_row.addWidget(self.common_only)

        self.library_list = QListWidget()
        self.library_list.currentItemChanged.connect(self._on_library_selected)

        self.items_list = QListWidget()
        self.items_list.currentItemChanged.connect(self._on_item_selected)

        self.detail_panel = QWidget()
        self.detail_panel.setObjectName("LibraryDetailPanel")
        self.detail_layout = QVBoxLayout(self.detail_panel)
        self.detail_layout.setContentsMargins(12, 12, 12, 12)
        self.detail_layout.setSpacing(10)

        self.detail_title = QLabel("Selecciona un ítem")
        self.detail_title.setObjectName("SectionTitle")
        self.detail_title.setWordWrap(True)
        self.detail_layout.addWidget(self.detail_title)

        self.detail_meta_row = QHBoxLayout()
        self.detail_meta_row.setAlignment(Qt.AlignLeft)
        self.detail_layout.addLayout(self.detail_meta_row)

        self.detail_summary = QLabel("")
        self.detail_summary.setWordWrap(True)
        self.detail_layout.addWidget(self.detail_summary)

        self.detail_layout.addWidget(self._make_divider())

        self.detail_what_title = QLabel("Qué es")
        self.detail_what_title.setObjectName("SectionTitle")
        self.detail_what = QLabel("")
        self.detail_what.setWordWrap(True)
        self.detail_layout.addWidget(self.detail_what_title)
        self.detail_layout.addWidget(self.detail_what)

        self.detail_layout.addWidget(self._make_divider())

        self.detail_when_title = QLabel("Cuándo se usa")
        self.detail_when_title.setObjectName("SectionTitle")
        self.detail_when = QLabel("")
        self.detail_when.setWordWrap(True)
        self.detail_layout.addWidget(self.detail_when_title)
        self.detail_layout.addWidget(self.detail_when)

        self.detail_layout.addWidget(self._make_divider())

        self.detail_pitfalls_title = QLabel("Errores típicos")
        self.detail_pitfalls_title.setObjectName("SectionTitle")
        self.detail_pitfalls = QLabel("")
        self.detail_pitfalls.setWordWrap(True)
        self.detail_layout.addWidget(self.detail_pitfalls_title)
        self.detail_layout.addWidget(self.detail_pitfalls)

        self.detail_layout.addWidget(self._make_divider())

        self.example_card = CodeCard("Ejemplo", "")
        self.detail_layout.addWidget(self.example_card)
        self.detail_layout.addStretch()

        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        left_layout.addWidget(QLabel("Librerías"))
        left_layout.addWidget(self.library_list)

        center_panel = QWidget()
        center_layout = QVBoxLayout(center_panel)
        center_layout.addWidget(QLabel("Funciones y clases"))
        center_layout.addWidget(self.items_list)

        content_row = QHBoxLayout()
        content_row.addWidget(left_panel, 1)
        content_row.addWidget(center_panel, 2)
        content_row.addWidget(self.detail_panel, 3)

        layout = QVBoxLayout(self)
        layout.addLayout(search_row)
        layout.addLayout(content_row)

        self._all_items = []
        self._filtered_items = []
        self._populate_libraries()
        self._load_items()
        self._apply_filter()

    def _make_divider(self) -> QFrame:
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setObjectName("SectionDivider")
        line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        return line

    def _populate_libraries(self) -> None:
        self.library_filter.blockSignals(True)
        self.library_filter.clear()
        self.library_filter.addItem("Todas", "all")
        self.library_list.clear()

        self.library_list.addItem(self._make_library_item("Todas", "all"))
        for key, data in LIBRARIES.items():
            title = data["title"]
            self.library_filter.addItem(title, key)
            self.library_list.addItem(self._make_library_item(title, key))

        self.library_filter.blockSignals(False)
        self.library_list.setCurrentRow(0)

    def _make_library_item(self, title: str, key: str) -> QListWidgetItem:
        item = QListWidgetItem(title)
        item.setData(Qt.UserRole, key)
        return item

    def _load_items(self) -> None:
        self._all_items = []
        for library_key, library, item in iter_library_items():
            entry = {
                "library_key": library_key,
                "library": library,
                "item": item,
                "search_text": build_search_text(library_key, item).lower(),
            }
            self._all_items.append(entry)

    def _apply_filter(self) -> None:
        query = self.search_input.text().strip().lower()
        selected_library = self.library_filter.currentData()
        common_only = self.common_only.isChecked()

        self._sync_library_list(selected_library)

        self._filtered_items = []
        for entry in self._all_items:
            if selected_library and selected_library != "all":
                if entry["library_key"] != selected_library:
                    continue
            if common_only and not entry["item"].get("common", False):
                continue
            if query and query not in entry["search_text"]:
                continue
            self._filtered_items.append(entry)

        self._populate_items()

    def _sync_library_list(self, selected_library: str | None) -> None:
        if selected_library is None:
            return
        for row in range(self.library_list.count()):
            item = self.library_list.item(row)
            if item.data(Qt.UserRole) == selected_library:
                if row != self.library_list.currentRow():
                    self.library_list.blockSignals(True)
                    self.library_list.setCurrentRow(row)
                    self.library_list.blockSignals(False)
                return

    def _populate_items(self) -> None:
        self.items_list.clear()
        for entry in self._filtered_items:
            item_data = entry["item"]
            list_item = QListWidgetItem()
            list_item.setData(Qt.UserRole, entry)
            widget = LibraryItemWidget(
                item_data["name"],
                item_data["category"],
                item_data.get("common", False),
            )
            list_item.setSizeHint(widget.sizeHint())
            self.items_list.addItem(list_item)
            self.items_list.setItemWidget(list_item, widget)

        if self.items_list.count() > 0:
            self.items_list.setCurrentRow(0)
        else:
            self._clear_detail_panel()

    def _on_library_selected(self, current: QListWidgetItem | None) -> None:
        if current is None:
            return
        key = current.data(Qt.UserRole)
        index = self.library_filter.findData(key)
        if index >= 0 and index != self.library_filter.currentIndex():
            self.library_filter.setCurrentIndex(index)
        else:
            self._apply_filter()

    def _on_item_selected(
        self,
        current: QListWidgetItem | None,
        _previous: QListWidgetItem | None = None,
    ) -> None:
        if current is None:
            self._clear_detail_panel()
            return
        entry = current.data(Qt.UserRole)
        if not entry:
            self._clear_detail_panel()
            return
        library = entry["library"]
        item = entry["item"]
        title = f"{item['name']} — {item['signature']}"
        self.detail_title.setText(title)

        self._clear_meta_row()
        if item.get("common", False):
            self.detail_meta_row.addWidget(badge("COMÚN", accent=None, variant="common"))
        self.detail_meta_row.addWidget(badge(item["category"], accent=None, variant="category"))
        self.detail_meta_row.addWidget(badge(library["title"], accent=None, variant="library"))
        self.detail_meta_row.addStretch()

        self.detail_summary.setText(library["summary"])
        self.detail_what.setText(item["what"])
        self.detail_when.setText(self._format_bullets(item.get("when", [])))
        self.detail_pitfalls.setText(self._format_bullets(item.get("pitfalls", [])))
        self.example_card.code_view.setPlainText(self._format_examples(item.get("examples", [])))

    def _format_bullets(self, items: list[str]) -> str:
        return "\n".join(f"• {value}" for value in items) if items else "-"

    def _format_examples(self, examples: list[dict]) -> str:
        if not examples:
            return ""
        total = len(examples)
        example = examples[0]
        warn_if_short_example(example.get("do", ""), f"Library: {example.get('title', '')}")
        pitfalls = example.get("pitfalls", [])
        pitfalls_text = "\n".join(f"- {pitfall}" for pitfall in pitfalls) if pitfalls else "-"
        return (
            f"Ejemplo 1 de {total}: {example.get('title', 'Ejemplo')}\n\n"
            "Aprende esto\n"
            f"{example.get('learn', '')}\n\n"
            "Haz esto\n"
            f"{example.get('do', '')}\n\n"
            "Verás esto\n"
            f"{example.get('see', '')}\n\n"
            "Por qué funciona\n"
            f"{example.get('why', '')}\n\n"
            "Lo típico que sale mal\n"
            f"{pitfalls_text}"
        )

    def _clear_detail_panel(self) -> None:
        self.detail_title.setText("No hay resultados")
        self.detail_summary.setText("")
        self.detail_what.setText("")
        self.detail_when.setText("")
        self.detail_pitfalls.setText("")
        self.example_card.code_view.setPlainText("")
        self._clear_meta_row()

    def _clear_meta_row(self) -> None:
        while self.detail_meta_row.count():
            item = self.detail_meta_row.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
