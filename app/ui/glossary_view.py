from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

from app.utils.glossary import TERMS


class GlossaryView(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Buscar por término o definición...")
        self.search_input.setClearButtonEnabled(True)
        self.search_input.textChanged.connect(self._apply_filter)

        self.terms_list = QListWidget()
        self.terms_list.currentItemChanged.connect(self._on_term_selected)

        self.detail_view = QTextBrowser()
        self.detail_view.setOpenExternalLinks(False)

        self.copy_button = QPushButton("Copiar definición")
        self.copy_button.clicked.connect(self._copy_definition)

        detail_layout = QVBoxLayout()
        detail_layout.addWidget(self.detail_view)
        detail_layout.addWidget(self.copy_button, alignment=Qt.AlignRight)
        detail_container = QWidget()
        detail_container.setLayout(detail_layout)

        content_layout = QHBoxLayout()
        content_layout.addWidget(self.terms_list, 1)
        content_layout.addWidget(detail_container, 2)

        layout = QVBoxLayout(self)
        layout.addWidget(self.search_input)
        layout.addLayout(content_layout)

        self._all_terms = sorted(TERMS.items(), key=lambda item: item[0].lower())
        self._filtered_terms = list(self._all_terms)
        self._populate_list()

    def _populate_list(self) -> None:
        self.terms_list.clear()
        for term, definition in self._filtered_terms:
            item = QListWidgetItem(term)
            item.setData(Qt.UserRole, definition)
            self.terms_list.addItem(item)
        if self.terms_list.count() > 0:
            self.terms_list.setCurrentRow(0)
        else:
            self.detail_view.setPlainText("No hay términos que coincidan.")

    def _apply_filter(self) -> None:
        query = self.search_input.text().strip().lower()
        if not query:
            self._filtered_terms = list(self._all_terms)
        else:
            self._filtered_terms = [
                (term, definition)
                for term, definition in self._all_terms
                if query in term.lower() or query in definition.lower()
            ]
        self._populate_list()

    def _on_term_selected(
        self,
        current: QListWidgetItem | None,
        _previous: QListWidgetItem | None = None,
    ) -> None:
        if current is None:
            self.detail_view.clear()
            return
        definition = current.data(Qt.UserRole)
        self.detail_view.setPlainText(definition)

    def _copy_definition(self) -> None:
        item = self.terms_list.currentItem()
        if item is None:
            return
        definition = item.data(Qt.UserRole)
        QGuiApplication.clipboard().setText(definition)
