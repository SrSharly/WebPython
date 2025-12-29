from __future__ import annotations

from PySide6.QtCore import QEvent, QObject
from PySide6.QtGui import QCursor, QTextFormat
from PySide6.QtWidgets import QToolTip, QTextBrowser


class InstantTooltipController(QObject):
    def __init__(self, widget: QTextBrowser) -> None:
        super().__init__(widget)
        self._widget = widget
        self._last_text: str | None = None
        self._tooltip_visible = False
        self._widget.setMouseTracking(True)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if watched is not self._widget:
            return super().eventFilter(watched, event)

        if event.type() == QEvent.MouseMove:
            cursor = self._widget.cursorForPosition(event.pos())
            char_format = cursor.charFormat()
            text = char_format.toolTip()
            if not text:
                prop = char_format.property(QTextFormat.ToolTip)
                text = prop if isinstance(prop, str) else ""

            if text:
                if text != self._last_text or not self._tooltip_visible:
                    QToolTip.showText(QCursor.pos(), text, self._widget)
                    self._tooltip_visible = True
                    self._last_text = text
            else:
                if self._tooltip_visible:
                    QToolTip.hideText()
                    self._tooltip_visible = False
                    self._last_text = None

        elif event.type() in (QEvent.Leave, QEvent.HoverLeave):
            if self._tooltip_visible:
                QToolTip.hideText()
                self._tooltip_visible = False
                self._last_text = None

        return super().eventFilter(watched, event)
