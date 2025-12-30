from __future__ import annotations

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QGuiApplication
from urllib.parse import quote, unquote
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QTextBrowser,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)

from app.utils.glossary import GLOSSARY, definition_text, glossary_tooltip


class GlossaryView(QWidget):
    termSelected = Signal(str)

    def __init__(self) -> None:
        super().__init__()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Buscar por término o definición...")
        self.search_input.setClearButtonEnabled(True)
        self.search_input.textChanged.connect(self._apply_filter)

        self.tree = QTreeWidget()
        self.tree.setHeaderHidden(True)
        self.tree.itemSelectionChanged.connect(self._on_term_selected)

        self.detail_view = QTextBrowser()
        self.detail_view.setOpenExternalLinks(False)
        self.detail_view.anchorClicked.connect(self._on_detail_anchor)

        self.copy_button = QPushButton("Copiar definición")
        self.copy_button.clicked.connect(self._copy_definition)

        detail_layout = QVBoxLayout()
        detail_layout.addWidget(self.detail_view)
        detail_layout.addWidget(self.copy_button, alignment=Qt.AlignRight)
        detail_container = QWidget()
        detail_container.setLayout(detail_layout)

        content_layout = QHBoxLayout()
        content_layout.addWidget(self.tree, 1)
        content_layout.addWidget(detail_container, 2)

        layout = QVBoxLayout(self)
        layout.addWidget(self.search_input)
        layout.addLayout(content_layout)

        self._glossary = dict(GLOSSARY)
        self._term_meta: dict[str, dict[str, str | None]] = {}
        self._term_labels: dict[str, str] = {}
        self._term_related: dict[str, list[str]] = {}
        self._terms: list[tuple[str, str]] = []
        self._filtered_terms: list[tuple[str, str]] = []
        self._populate_tree()

    def load_terms(
        self,
        glossary: dict[str, dict[str, object]],
        term_meta: dict[str, dict[str, str | None]],
        term_labels: dict[str, str],
        term_related: dict[str, list[str]],
    ) -> None:
        self._glossary = glossary
        self._term_meta = term_meta
        self._term_labels = term_labels
        self._term_related = term_related
        self._populate_tree()

    def _populate_tree(self) -> None:
        self.tree.clear()
        self._terms = sorted(
            [(term_id, definition_text(self._glossary[term_id])) for term_id in self._glossary],
            key=lambda item: item[0].lower(),
        )
        self._filtered_terms = list(self._terms)
        self._build_tree(self._filtered_terms)

    def _build_tree(self, items: list[tuple[str, str]]) -> None:
        self.tree.clear()
        roots: dict[str, QTreeWidgetItem] = {}
        owners: dict[tuple[str, str], QTreeWidgetItem] = {}

        def get_root(label: str) -> QTreeWidgetItem:
            root = roots.get(label)
            if root is None:
                root = QTreeWidgetItem([label])
                root.setData(0, Qt.UserRole, None)
                roots[label] = root
                self.tree.addTopLevelItem(root)
            return root

        for term_id, definition in items:
            meta = self._term_meta.get(term_id)
            label = self._term_labels.get(term_id, term_id)
            if meta is None:
                root_label = "Conceptos"
                owner_label = None
            else:
                namespace = meta.get("namespace") or "manual"
                kind = meta.get("kind") or "concept"
                owner = meta.get("owner")
                if namespace == "builtin":
                    root_label = "Builtins"
                elif namespace == "pandas":
                    root_label = "Pandas"
                elif namespace == "manual":
                    root_label = "Conceptos"
                else:
                    root_label = namespace.title()
                if kind in {"method", "attribute"} and owner:
                    owner_label = owner
                elif kind in {"builtin", "function"} and namespace == "builtin":
                    owner_label = "Funciones"
                else:
                    owner_label = None

            root_item = get_root(root_label)
            parent = root_item
            if owner_label:
                owner_key = (root_label, owner_label)
                owner_item = owners.get(owner_key)
                if owner_item is None:
                    owner_item = QTreeWidgetItem([owner_label])
                    owner_item.setData(0, Qt.UserRole, None)
                    root_item.addChild(owner_item)
                    owners[owner_key] = owner_item
                parent = owner_item

            term_item = QTreeWidgetItem([label])
            term_item.setData(0, Qt.UserRole, term_id)
            term_item.setToolTip(0, glossary_tooltip(label, self._glossary[term_id]))
            parent.addChild(term_item)

        self.tree.expandAll()
        if self.tree.topLevelItemCount() == 0:
            self.detail_view.setPlainText("No hay términos que coincidan.")

    def _apply_filter(self) -> None:
        query = self.search_input.text().strip().lower()
        if not query:
            self._filtered_terms = list(self._terms)
        else:
            self._filtered_terms = [
                (term, definition)
                for term, definition in self._terms
                if query in term.lower() or query in definition.lower()
            ]
        self._build_tree(self._filtered_terms)

    def _on_term_selected(self) -> None:
        item = self.tree.currentItem()
        if item is None:
            self.detail_view.clear()
            return
        term_id = item.data(0, Qt.UserRole)
        if not term_id:
            return
        self._show_term(term_id)
        self.termSelected.emit(term_id)

    def _show_term(self, term_id: str) -> None:
        data = self._glossary.get(term_id)
        if not data:
            self.detail_view.setPlainText("No se encontró la definición.")
            return
        definition = definition_text(data)
        related = self._term_related.get(term_id, [])
        if related:
            related_links = " ".join(
                f'<a href="tip:{quote(related_id)}">{self._term_labels.get(related_id, related_id)}</a>'
                for related_id in related
            )
            html = (
                f"<p>{definition.replace(chr(10), '<br>')}</p>"
                f"<p><strong>Relacionado con:</strong> {related_links}</p>"
            )
            self.detail_view.setHtml(html)
        else:
            self.detail_view.setPlainText(definition)

    def _on_detail_anchor(self, url) -> None:
        anchor = url.toString()
        if anchor.startswith("tip:"):
            term_id = unquote(anchor.removeprefix("tip:"))
            self._show_term(term_id)
            self.termSelected.emit(term_id)

    def _copy_definition(self) -> None:
        item = self.tree.currentItem()
        if item is None:
            return
        term_id = item.data(0, Qt.UserRole)
        if not term_id:
            return
        data = self._glossary.get(term_id)
        if not data:
            return
        definition = definition_text(data)
        QGuiApplication.clipboard().setText(definition)
