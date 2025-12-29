from __future__ import annotations

from typing import Callable

from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPlainTextEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class CalloutBox(QFrame):
    def __init__(
        self,
        title: str,
        body: str,
        variant: str = "note",
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self.setObjectName("CalloutBox")
        self.setProperty("variant", variant)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 10, 12, 10)
        header = QLabel(title)
        header.setObjectName("SectionTitle")
        content = QLabel(body)
        content.setWordWrap(True)
        layout.addWidget(header)
        layout.addWidget(content)


class CodeCard(QFrame):
    def __init__(
        self,
        title: str,
        code: str,
        parent: QWidget | None = None,
        show_run: bool = False,
        run_callback: Callable[[str, QPlainTextEdit | None, QPlainTextEdit], None] | None = None,
    ) -> None:
        super().__init__(parent)
        self.setObjectName("CodeCard")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(14, 12, 14, 12)
        header = QLabel(title)
        header.setObjectName("SectionTitle")
        layout.addWidget(header)

        code_box = QFrame()
        code_box.setObjectName("CodeBox")
        code_box_layout = QVBoxLayout(code_box)
        code_box_layout.setContentsMargins(8, 8, 8, 8)

        self.code_view = QPlainTextEdit()
        self.code_view.setObjectName("CodeBlock")
        self.code_view.setPlainText(code)
        self.code_view.setReadOnly(True)
        self.code_view.setMinimumHeight(120)
        code_box_layout.addWidget(self.code_view)
        layout.addWidget(code_box)

        actions = QHBoxLayout()

        self.run_button = None
        self.output_view = None
        if show_run:
            run_btn = QPushButton("Ejecutar")
            if run_callback is None:
                run_btn.setEnabled(False)
            else:
                run_btn.clicked.connect(lambda: run_callback(code, self.output_view, self.code_view))
            actions.addWidget(run_btn)
            self.run_button = run_btn
            self.output_view = QPlainTextEdit()
            self.output_view.setReadOnly(True)
            self.output_view.setPlaceholderText("Salida...")
            self.output_view.setMaximumHeight(120)
        actions.addStretch()
        layout.addLayout(actions)

        if self.output_view is not None:
            layout.addWidget(self.output_view)
