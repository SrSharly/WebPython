from __future__ import annotations

from PySide6.QtWidgets import (
    QComboBox,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from app.lesson_base import Lesson


class QComboBoxLesson(Lesson):
    TITLE = "QComboBox"
    CATEGORY = "PySide6"
    SUBCATEGORY = "Controles"
    LEVEL = "Básico"
    TAGS = ["QComboBox", "select", "items", "signals"]

    def summary(self) -> str:
        return (
            "QComboBox permite seleccionar un valor de una lista. Aprende a poblarla, "
            "escuchar cambios y permitir entradas personalizadas."
        )

    def guide(self) -> str:
        return """
- QComboBox muestra una lista desplegable de opciones.
- addItem() o addItems() agrega valores visibles.
- currentText() devuelve la opción seleccionada.
- currentIndexChanged se dispara al cambiar selección.
- setEditable(True) permite que el usuario escriba.
- Puedes usar insertItem() para colocar en un índice.
- removeItem() elimina entradas específicas.
- setPlaceholderText muestra un texto inicial.
- Usa setCurrentIndex() para selección programática.
- Guarda data extra con addItem(texto, data).
- Las señales editTextChanged y activated dan más control.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Lista vacía",
                "Si no agregas items, el combo se ve vacío; usa addItems().",
            ),
            (
                "No manejar cambios",
                "Sin currentIndexChanged no reaccionas a selección.",
            ),
            (
                "Editable sin validar",
                "Si habilitas escritura, valida el texto ingresado.",
            ),
            (
                "Usar índices mágicos",
                "Si cambian los items, los índices cambian; usa texto o data.",
            ),
            (
                "No definir selección inicial",
                "El usuario puede ver una opción incorrecta; setCurrentIndex.",
            ),
            (
                "No limpiar",
                "Al recargar datos, usa clear() para evitar duplicados.",
            ),
            (
                "Items duplicados",
                "Dificultan la selección; controla el contenido antes de agregar.",
            ),
            (
                "No mostrar placeholder",
                "Sin hint, el usuario no entiende qué elegir.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Agregar items",
                """combo = QComboBox()\ncombo.addItems(["Rojo", "Verde", "Azul"])""",
            ),
            (
                "Leer selección",
                """combo = QComboBox()\nprint(combo.currentText())""",
            ),
            (
                "Señal de cambio",
                """combo = QComboBox()\ncombo.currentIndexChanged.connect(print)""",
            ),
            (
                "Editable",
                """combo = QComboBox()\ncombo.setEditable(True)""",
            ),
            (
                "Agregar con data",
                """combo = QComboBox()\ncombo.addItem("Lima", "PE-LIM")""",
            ),
            (
                "Insertar al inicio",
                """combo = QComboBox()\ncombo.insertItem(0, "Selecciona...")""",
            ),
            (
                "Eliminar item",
                """combo = QComboBox()\ncombo.removeItem(2)""",
            ),
            (
                "Seleccionar índice",
                """combo = QComboBox()\ncombo.setCurrentIndex(1)""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea un QComboBox con tres colores.",
                "hints": ["Usa addItems"],
                "solution": "combo = QComboBox()\ncombo.addItems(['Rojo', 'Verde', 'Azul'])",
            },
            {
                "question": "Muestra en consola la opción seleccionada cuando cambie.",
                "hints": ["currentIndexChanged"],
                "solution": "combo = QComboBox()\ncombo.currentIndexChanged.connect(lambda: print(combo.currentText()))",
            },
            {
                "question": "Permite escritura y lee el texto editado.",
                "hints": ["setEditable", "editTextChanged"],
                "solution": "combo = QComboBox()\ncombo.setEditable(True)\ncombo.editTextChanged.connect(print)",
            },
        ]

    def requirements(self) -> list[str]:
        return []

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)

        title = QLabel("Demo: selección y edición en QComboBox.")
        status = QLabel("Selecciona una opción")

        combo = QComboBox()
        combo.setPlaceholderText("Elige una fruta")
        combo.addItems(["Manzana", "Banana", "Cereza"])

        add_btn = QPushButton("Agregar 'Mango'")
        edit_btn = QPushButton("Hacer editable")

        def update_status() -> None:
            status.setText(f"Actual: {combo.currentText()}")

        def add_item() -> None:
            if combo.findText("Mango") == -1:
                combo.addItem("Mango")
            update_status()

        def make_editable() -> None:
            combo.setEditable(True)
            status.setText("Editable: escribe una opción")

        combo.currentIndexChanged.connect(lambda _: update_status())
        combo.editTextChanged.connect(lambda text: status.setText(f"Editable: {text}"))
        add_btn.clicked.connect(add_item)
        edit_btn.clicked.connect(make_editable)

        layout.addWidget(title)
        layout.addWidget(combo)
        layout.addWidget(status)
        layout.addWidget(add_btn)
        layout.addWidget(edit_btn)
        return widget
