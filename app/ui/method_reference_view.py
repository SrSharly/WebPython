from __future__ import annotations

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QLineEdit,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)

from app.utils.glossary import definition_text


class MethodReferenceView(QWidget):
    termSelected = Signal(str)

    def __init__(self) -> None:
        super().__init__()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Buscar método o función...")
        self.search_input.setClearButtonEnabled(True)
        self.search_input.textChanged.connect(self._apply_filter)

        self.tree = QTreeWidget()
        self.tree.setHeaderHidden(True)
        self.tree.itemSelectionChanged.connect(self._on_term_selected)

        layout = QVBoxLayout(self)
        layout.addWidget(self.search_input)
        layout.addWidget(self.tree)

        self._glossary: dict[str, dict[str, object]] = {}
        self._term_meta: dict[str, dict[str, str | None]] = {}
        self._term_labels: dict[str, str] = {}
        self._terms: list[dict[str, str]] = []
        self._filtered_terms: list[dict[str, str]] = []

    def load_terms(
        self,
        glossary: dict[str, dict[str, object]],
        term_meta: dict[str, dict[str, str | None]],
        term_labels: dict[str, str],
    ) -> None:
        self._glossary = glossary
        self._term_meta = term_meta
        self._term_labels = term_labels
        self._rebuild_terms()
        self._apply_filter()

    def _rebuild_terms(self) -> None:
        self._terms = []
        for term_id, meta in self._term_meta.items():
            if meta.get("kind") not in {"method", "builtin", "function"}:
                continue
            label = self._term_labels.get(term_id, term_id)
            owner = meta.get("owner") or ""
            namespace = meta.get("namespace") or ""
            group = self._resolve_group(owner, meta.get("kind"), namespace)
            self._terms.append(
                {
                    "term_id": term_id,
                    "label": label,
                    "group": group,
                    "search": f"{label} {owner} {namespace} {term_id}",
                }
            )

    def _resolve_group(self, owner: str, kind: str | None, namespace: str) -> str:
        owner_lower = owner.lower()
        if owner_lower in {"str", "string"}:
            return "str"
        if owner_lower in {"list", "lista"}:
            return "list"
        if owner_lower in {"dict", "diccionario"}:
            return "dict"
        if kind == "builtin" or namespace == "builtin":
            return "builtin"
        return "otros"

    def _apply_filter(self) -> None:
        query = self.search_input.text().strip().lower()
        if not query:
            self._filtered_terms = list(self._terms)
        else:
            self._filtered_terms = [
                term
                for term in self._terms
                if query in term["search"].lower()
            ]
        self._build_tree()

    def _build_tree(self) -> None:
        self.tree.clear()
        group_order = [
            ("str", "str"),
            ("list", "list"),
            ("dict", "dict"),
            ("builtin", "builtin"),
            ("otros", "otros"),
        ]
        group_items: dict[str, QTreeWidgetItem] = {}
        for key, label in group_order:
            group_item = QTreeWidgetItem([label])
            group_item.setData(0, Qt.UserRole, None)
            self.tree.addTopLevelItem(group_item)
            group_items[key] = group_item

        for term in sorted(self._filtered_terms, key=lambda t: t["label"].lower()):
            parent = group_items.get(term["group"])
            if parent is None:
                parent = group_items["otros"]
            item = QTreeWidgetItem([term["label"]])
            item.setData(0, Qt.UserRole, term["term_id"])
            tooltip = definition_text(self._glossary.get(term["term_id"], {}))
            if tooltip:
                item.setToolTip(0, tooltip.splitlines()[0])
            parent.addChild(item)

        self.tree.expandAll()

    def _on_term_selected(self) -> None:
        item = self.tree.currentItem()
        if item is None:
            return
        term_id = item.data(0, Qt.UserRole)
        if not term_id:
            return
        self.termSelected.emit(term_id)
