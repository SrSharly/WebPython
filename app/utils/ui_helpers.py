from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QLabel, QMessageBox, QWidget


def copy_to_clipboard(text: str, parent: QWidget | None = None) -> None:
    clipboard = QGuiApplication.clipboard()
    clipboard.setText(text)
    QMessageBox.information(parent, "Copiado", "El texto fue copiado al portapapeles.")


def badge(text: str, accent: str = "#2b6cb0") -> QLabel:
    label = QLabel(text)
    label.setAlignment(Qt.AlignCenter)
    label.setStyleSheet(
        "QLabel {"
        f"background-color: {accent};"
        "color: white;"
        "padding: 2px 8px;"
        "border-radius: 10px;"
        "font-weight: 600;"
        "}"
    )
    return label
