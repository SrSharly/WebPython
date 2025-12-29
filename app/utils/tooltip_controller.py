from __future__ import annotations

from urllib.parse import unquote

from PySide6.QtCore import QEvent, QObject, Qt, Signal
from PySide6.QtWidgets import QTextBrowser

from app.utils.glossary import GLOSSARY
from app.utils.instant_tooltip import InstantTooltipPopup


class InstantTooltipController(QObject):
    termPinned = Signal(str)

    def __init__(self, widget: QTextBrowser) -> None:
        super().__init__(widget)
        self._widget = widget
        self._current_term_id: str | None = None
        self._popup = InstantTooltipPopup(widget)
        self._widget.setMouseTracking(True)
        self._widget.setAttribute(Qt.WA_Hover, True)
        self._widget.setOpenExternalLinks(False)
        if hasattr(self._widget, "setOpenLinks"):
            self._widget.setOpenLinks(False)
        self._widget.anchorClicked.connect(self._on_anchor_clicked)

    def _on_anchor_clicked(self, url) -> None:
        anchor = url.toString()
        if anchor.startswith("tip:"):
            term_id = unquote(anchor.removeprefix("tip:"))
            if term_id in GLOSSARY:
                self.termPinned.emit(term_id)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if watched is not self._widget:
            return super().eventFilter(watched, event)

        if event.type() in (QEvent.MouseMove, QEvent.HoverMove):
            anchor = self._widget.anchorAt(event.pos())
            term_id = None
            if anchor.startswith("tip:"):
                term_id = unquote(anchor.removeprefix("tip:"))
            if term_id and term_id in GLOSSARY:
                if term_id != self._current_term_id:
                    self._popup.show_text(
                        GLOSSARY[term_id]["tooltip"],
                        self._widget.mapToGlobal(event.pos()),
                        self._widget,
                    )
                    self._current_term_id = term_id
            elif self._current_term_id is not None:
                self._popup.hide_now()
                self._current_term_id = None

        elif event.type() in (QEvent.Leave, QEvent.HoverLeave):
            if self._current_term_id is not None:
                self._popup.hide_now()
                self._current_term_id = None

        return super().eventFilter(watched, event)
