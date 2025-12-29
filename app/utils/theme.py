from __future__ import annotations

from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication

QSS_LIGHT = """
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
QLabel[class='Badge'][variant='common'] {
    background: #c7d2fe;
    color: #1e3a8a;
}
QLabel[class='Badge'][variant='category'] {
    background: #e2e8f0;
    color: #1f2937;
}
QLabel[class='Badge'][variant='library'] {
    background: #bfdbfe;
    color: #1e3a8a;
}
QFrame#CalloutBox {
    background: #eef7ff;
    border: 1px solid #cfe3ff;
    border-radius: 12px;
}
QFrame#CalloutBox[variant="warning"] {
    background: #fff4e5;
    border: 1px solid #ffd4a3;
}
QFrame#CalloutBox[variant="best_practice"] {
    background: #ecfdf3;
    border: 1px solid #b7f0cd;
}
QFrame#CalloutBox[variant="definition"] {
    background: #f3f0ff;
    border: 1px solid #d9d1ff;
}
QFrame#CodeCard {
    background: #ffffff;
    border: 1px solid #e1e5ef;
    border-radius: 14px;
}
QFrame#CodeBox {
    background: #0b1220;
    border: 1px solid #111827;
    border-radius: 10px;
}
QFrame#DefinitionPanel {
    background: #ffffff;
    border: 1px solid #d7dde8;
    border-radius: 14px;
}
QFrame#LibraryDetailPanel {
    background: #ffffff;
    border: 1px solid #d7dde8;
    border-radius: 14px;
}
QFrame#SectionDivider {
    border: 1px solid #e5e7eb;
}
QLabel#LibraryItemTitle {
    font-weight: 600;
}
QLabel#DefinitionTitle {
    font-size: 16px;
    font-weight: 700;
}
QLabel#DefinitionTerm {
    background: #eef1f7;
    color: #1f2937;
    padding: 4px 10px;
    border-radius: 10px;
    font-weight: 600;
}
QPlainTextEdit#CodeBlock {
    background: transparent;
    color: #e2e8f0;
    border: none;
    font-family: "Consolas";
    font-size: 12px;
    padding: 2px;
}
QToolTip {
    background-color: #1f2937;
    color: #f9fafb;
    border: 1px solid #374151;
    padding: 6px;
    border-radius: 6px;
}
"""

QSS_DARK = """
QWidget {
    color: #e6e6e6;
    font-size: 13px;
}
QMainWindow {
    background-color: #202124;
}
QLineEdit {
    background: #2a2a2a;
    border: 1px solid #3a3a3a;
    border-radius: 10px;
    padding: 8px 10px;
}
QLineEdit:focus {
    border-color: #d4af37;
}
QTreeWidget, QListWidget {
    background: #2a2a2a;
    border: 1px solid #3a3a3a;
    border-radius: 12px;
    padding: 6px;
}
QTreeWidget::item, QListWidget::item {
    padding: 6px 8px;
    border-radius: 8px;
}
QTreeWidget::item:selected, QListWidget::item:selected {
    background: #333333;
    color: #f7f2e4;
}
QTabWidget::pane {
    border: 1px solid #3a3a3a;
    border-radius: 12px;
    background: #2a2a2a;
}
QTabBar::tab {
    background: #2e2e2e;
    border: 1px solid #3a3a3a;
    padding: 8px 14px;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    margin-right: 4px;
}
QTabBar::tab:selected {
    background: #2a2a2a;
    border-bottom-color: #2a2a2a;
    color: #f7f2e4;
}
QTextEdit, QTextBrowser {
    background: #2a2a2a;
    border: 1px solid #3a3a3a;
    border-radius: 10px;
    padding: 8px;
}
QPushButton {
    background: #d4af37;
    color: #1e1e1e;
    border: none;
    border-radius: 8px;
    padding: 6px 12px;
    font-weight: 600;
}
QPushButton:hover {
    background: #c39a2b;
}
QPushButton:pressed {
    background: #b58722;
}
QPushButton[secondary="true"] {
    background: #2e2e2e;
    color: #e6e6e6;
    border: 1px solid #3a3a3a;
}
QPushButton[secondary="true"]:hover {
    background: #363636;
}
QGroupBox, QFrame#Card {
    background: #2a2a2a;
    border: 1px solid #3a3a3a;
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
    color: #1e1e1e;
    padding: 2px 10px;
    border-radius: 10px;
    font-weight: 700;
}
QLabel[class='Badge'][variant='common'] {
    background: #d4af37;
    color: #1e1e1e;
}
QLabel[class='Badge'][variant='category'] {
    background: #3a3a3a;
    color: #f7f2e4;
}
QLabel[class='Badge'][variant='library'] {
    background: #4b5563;
    color: #f7f2e4;
}
QFrame#CalloutBox {
    background: #2c2b25;
    border: 1px solid #51442a;
    border-radius: 12px;
}
QFrame#CalloutBox[variant="warning"] {
    background: #3a2c1f;
    border: 1px solid #6a4b2e;
}
QFrame#CalloutBox[variant="best_practice"] {
    background: #1f3328;
    border: 1px solid #2c5a3a;
}
QFrame#CalloutBox[variant="definition"] {
    background: #2d2639;
    border: 1px solid #4b3a66;
}
QFrame#CodeCard {
    background: #2a2a2a;
    border: 1px solid #3a3a3a;
    border-radius: 14px;
}
QFrame#CodeBox {
    background: #0b1220;
    border: 1px solid #111827;
    border-radius: 10px;
}
QFrame#DefinitionPanel {
    background: #2a2a2a;
    border: 1px solid #3a3a3a;
    border-radius: 14px;
}
QFrame#LibraryDetailPanel {
    background: #2a2a2a;
    border: 1px solid #3a3a3a;
    border-radius: 14px;
}
QFrame#SectionDivider {
    border: 1px solid #3f3f3f;
}
QLabel#LibraryItemTitle {
    font-weight: 600;
}
QLabel#DefinitionTitle {
    font-size: 16px;
    font-weight: 700;
}
QLabel#DefinitionTerm {
    background: #2e2e2e;
    color: #f7f2e4;
    padding: 4px 10px;
    border-radius: 10px;
    font-weight: 700;
}
QPlainTextEdit#CodeBlock {
    background: transparent;
    color: #e6e6e6;
    border: none;
    font-family: "Consolas";
    font-size: 12px;
    padding: 2px;
}
QToolTip {
    background-color: #2a2a2a;
    color: #f7f2e4;
    border: 1px solid #d4af37;
    padding: 6px;
    border-radius: 6px;
}
"""

THEMES = {"light": QSS_LIGHT, "dark": QSS_DARK}


def apply_theme(app: QApplication, theme_name: str) -> None:
    theme = THEMES.get(theme_name, QSS_LIGHT)
    base_font = QFont("Segoe UI", 10)
    app.setFont(base_font)
    app.setStyleSheet(theme)


def toggle_theme(current: str) -> str:
    return "dark" if current == "light" else "light"
