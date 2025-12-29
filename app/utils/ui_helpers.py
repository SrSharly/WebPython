from __future__ import annotations

from typing import Callable

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QGuiApplication
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
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


def apply_app_theme(app: QApplication) -> None:
    base_font = QFont("Segoe UI", 10)
    app.setFont(base_font)
    app.setStyleSheet(
        """
        QWidget {
            color: #1f2937;
            font-size: 13px;
        }
        QMainWindow {
            background-color: #f4f6fb;
        }
        QLineEdit {
            background: #ffffff;
            border: 1px solid #d7dde8;
            border-radius: 10px;
            padding: 8px 10px;
        }
        QLineEdit:focus {
            border-color: #4c8df6;
        }
        QTreeWidget, QListWidget {
            background: #ffffff;
            border: 1px solid #d7dde8;
            border-radius: 12px;
            padding: 6px;
        }
        QTreeWidget::item, QListWidget::item {
            padding: 6px 8px;
            border-radius: 8px;
        }
        QTreeWidget::item:selected, QListWidget::item:selected {
            background: #e0ecff;
            color: #1f2937;
        }
        QTabWidget::pane {
            border: 1px solid #d7dde8;
            border-radius: 12px;
            background: #ffffff;
        }
        QTabBar::tab {
            background: #eef1f7;
            border: 1px solid #d7dde8;
            padding: 8px 14px;
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
            margin-right: 4px;
        }
        QTabBar::tab:selected {
            background: #ffffff;
            border-bottom-color: #ffffff;
        }
        QTextEdit, QTextBrowser {
            background: #ffffff;
            border: 1px solid #d7dde8;
            border-radius: 10px;
            padding: 8px;
        }
        QPushButton {
            background: #3b82f6;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 6px 12px;
            font-weight: 600;
        }
        QPushButton:hover {
            background: #2563eb;
        }
        QPushButton:pressed {
            background: #1d4ed8;
        }
        QPushButton[secondary="true"] {
            background: #ffffff;
            color: #1f2937;
            border: 1px solid #d7dde8;
        }
        QPushButton[secondary="true"]:hover {
            background: #eef1f7;
        }
        QGroupBox, QFrame#Card {
            background: #ffffff;
            border: 1px solid #e1e5ef;
            border-radius: 14px;
            margin-top: 10px;
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top left;
            padding: 6px 10px;
            font-weight: 600;
        }
        QLabel#HeaderTitle {
            font-size: 20px;
            font-weight: 700;
        }
        QLabel#SectionTitle {
            font-size: 16px;
            font-weight: 700;
        }
        QLabel[class='Badge'] {
            color: #ffffff;
            padding: 2px 10px;
            border-radius: 10px;
            font-weight: 600;
        }
        QFrame#InfoBox {
            background: #eef7ff;
            border: 1px solid #cfe3ff;
            border-radius: 12px;
        }
        QFrame#InfoBox[variant="warning"] {
            background: #fff4e5;
            border: 1px solid #ffd4a3;
        }
        QFrame#CodeCard {
            background: #ffffff;
            border: 1px solid #e1e5ef;
            border-radius: 14px;
        }
        QTextEdit#CodeBlock {
            background: #0f172a;
            color: #e2e8f0;
            border: none;
            border-radius: 10px;
            font-family: "Consolas";
            font-size: 12px;
        }
        """
    )


class InfoBox(QFrame):
    def __init__(self, title: str, body: str, variant: str = "note", parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setObjectName("InfoBox")
        self.setProperty("variant", "warning" if variant == "warning" else "note")
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
        run_callback: Callable[[str, QTextEdit | None, QTextEdit], None] | None = None,
    ) -> None:
        super().__init__(parent)
        self.setObjectName("CodeCard")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(14, 12, 14, 12)
        header = QLabel(title)
        header.setObjectName("SectionTitle")
        layout.addWidget(header)

        self.code_view = QTextEdit()
        self.code_view.setObjectName("CodeBlock")
        self.code_view.setPlainText(code)
        self.code_view.setReadOnly(True)
        self.code_view.setMinimumHeight(120)
        layout.addWidget(self.code_view)

        actions = QHBoxLayout()
        copy_btn = QPushButton("Copiar")
        copy_btn.setProperty("secondary", True)
        copy_btn.clicked.connect(lambda: copy_to_clipboard(code, self))
        actions.addWidget(copy_btn)

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
            self.output_view = QTextEdit(readOnly=True)
            self.output_view.setPlaceholderText("Salida...")
            self.output_view.setMaximumHeight(120)
        actions.addStretch()
        layout.addLayout(actions)

        if self.output_view is not None:
            layout.addWidget(self.output_view)
