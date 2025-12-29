from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import (
    QLabel,
    QMessageBox,
    QWidget,
)


def copy_to_clipboard(text: str, parent: QWidget | None = None) -> None:
    clipboard = QGuiApplication.clipboard()
    clipboard.setText(text)
    QMessageBox.information(parent, "Copiado", "El texto fue copiado al portapapeles.")


def badge(text: str, accent: str = "#2b6cb0") -> QLabel:
    label = QLabel(text)
    label.setAlignment(Qt.AlignCenter)
    label.setProperty("class", "Badge")
    label.setStyleSheet(f"QLabel[class='Badge'] {{ background-color: {accent}; }}")
    return label
