from __future__ import annotations

from PySide6.QtCore import QEvent, QObject, Qt
from PySide6.QtWidgets import QTextBrowser

from app.utils.instant_tooltip import InstantTooltipPopup


class InstantTooltipController(QObject):
    def __init__(self, widget: QTextBrowser) -> None:
        super().__init__(widget)
        self._widget = widget
        self._current_tip_text: str | None = None
        self._popup = InstantTooltipPopup(widget)
        self._widget.setMouseTracking(True)
        self._widget.setAttribute(Qt.WA_Hover, True)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if watched is not self._widget:
            return super().eventFilter(watched, event)

        if event.type() in (QEvent.MouseMove, QEvent.HoverMove):
            cursor = self._widget.cursorForPosition(event.pos())
            char_format = cursor.charFormat()
            text = char_format.toolTip()
            if text:
                if text != self._current_tip_text:
                    self._popup.show_text(text, self._widget.mapToGlobal(event.pos()), self._widget)
                    self._current_tip_text = text
            elif self._current_tip_text is not None:
                self._popup.hide_now()
                self._current_tip_text = None

        elif event.type() in (QEvent.Leave, QEvent.HoverLeave):
            if self._current_tip_text is not None:
                self._popup.hide_now()
                self._current_tip_text = None

        return super().eventFilter(watched, event)
