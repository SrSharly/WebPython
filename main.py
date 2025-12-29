import sys

from PySide6 import QtCore, QtWidgets

from controls import CONTROL_MODULES


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Aprende controles con PySide6")
        self.resize(900, 560)

        container = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout(container)

        self.control_list = QtWidgets.QListWidget()
        self.control_list.setMinimumWidth(220)
        self.control_list.currentRowChanged.connect(self.update_details)

        self.detail_title = QtWidgets.QLabel("Selecciona un control")
        self.detail_title.setStyleSheet("font-size: 18px; font-weight: bold;")

        self.detail_description = QtWidgets.QLabel("")
        self.detail_description.setWordWrap(True)

        self.detail_uses = QtWidgets.QTextBrowser()
        self.detail_uses.setMinimumHeight(140)
        self.detail_uses.setStyleSheet("background-color: #f5f5f5;")

        self.detail_errors = QtWidgets.QTextBrowser()
        self.detail_errors.setMinimumHeight(140)
        self.detail_errors.setStyleSheet("background-color: #fff3f3;")

        detail_layout = QtWidgets.QVBoxLayout()
        detail_layout.addWidget(self.detail_title)
        detail_layout.addWidget(self.detail_description)
        detail_layout.addSpacing(12)
        detail_layout.addWidget(QtWidgets.QLabel("Usos recomendados"))
        detail_layout.addWidget(self.detail_uses)
        detail_layout.addWidget(QtWidgets.QLabel("Posibles errores"))
        detail_layout.addWidget(self.detail_errors)
        detail_layout.addStretch()

        layout.addWidget(self.control_list)
        layout.addLayout(detail_layout)
        self.setCentralWidget(container)

        self.controls = [module.CONTROL for module in CONTROL_MODULES]
        for control in self.controls:
            self.control_list.addItem(control["nombre"])

        if self.controls:
            self.control_list.setCurrentRow(0)

    def update_details(self, index: int) -> None:
        if index < 0 or index >= len(self.controls):
            return

        control = self.controls[index]
        self.detail_title.setText(control["nombre"])
        self.detail_description.setText(control["descripcion"])
        self.detail_uses.setHtml(self.format_list(control["usos"]))
        self.detail_errors.setHtml(self.format_list(control["errores"]))

    @staticmethod
    def format_list(items: list[str]) -> str:
        list_items = "".join(f"<li>{item}</li>" for item in items)
        return f"<ul>{list_items}</ul>"


def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
