from __future__ import annotations

from PySide6.QtCore import QPoint, Qt
from PySide6.QtGui import QGuiApplication, QPalette
from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget


class InstantTooltipPopup(QFrame):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent, Qt.ToolTip | Qt.FramelessWindowHint)
        self.setObjectName("InstantTooltipPopup")
        self.setAttribute(Qt.WA_ShowWithoutActivating, True)
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)

        self._label = QLabel(self)
        self._label.setWordWrap(True)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 8, 12, 8)
        layout.addWidget(self._label)

        self._apply_theme(is_dark=False)

    def show_text(self, text: str, global_pos: QPoint, parent: QWidget) -> None:
        self._apply_theme(is_dark=self._is_dark_theme(parent))
        self._label.setText(text)
        self.adjustSize()

        target_pos = QPoint(global_pos.x() + 12, global_pos.y() + 18)
        available = QGuiApplication.primaryScreen().availableGeometry()
        max_x = available.right() - self.width()
        max_y = available.bottom() - self.height()
        target_pos.setX(min(max(target_pos.x(), available.left()), max_x))
        target_pos.setY(min(max(target_pos.y(), available.top()), max_y))

        self.move(target_pos)
        self.show()

    def hide_now(self) -> None:
        if self.isVisible():
            self.hide()

    def _apply_theme(self, is_dark: bool) -> None:
        if is_dark:
            background = "#1f1f1f"
            border = "#d4af37"
            text = "#f7f2e4"
        else:
            background = "#ffffff"
            border = "#d7dde8"
            text = "#1f2937"

        self.setStyleSheet(
            "QFrame#InstantTooltipPopup {"
            f"background-color: {background};"
            f"border: 1px solid {border};"
            "border-radius: 10px;"
            "}"
            f"QLabel {{ color: {text}; }}"
        )

    @staticmethod
    def _is_dark_theme(widget: QWidget) -> bool:
        color = widget.palette().color(QPalette.Window)
        return color.lightness() < 128
