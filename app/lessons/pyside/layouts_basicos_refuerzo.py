from __future__ import annotations

from PySide6.QtWidgets import (
    QComboBox,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)

from app.lesson_base import Lesson


class LayoutsBasicosRefuerzoLesson(Lesson):
    TITLE = "Layouts básicos (refuerzo)"
    CATEGORY = "PySide6"
    SUBCATEGORY = "Fundamentos UI"
    LEVEL = "Básico"
    TAGS = ["layouts", "QVBoxLayout", "QHBoxLayout", "QGridLayout", "spacers"]

    def summary(self) -> str:
        return (
            "Refuerza el uso de layouts con ejemplos de QVBoxLayout, QHBoxLayout y "
            "QGridLayout, además de stretch y spacers para controlar el espacio."
        )

    def guide(self) -> str:
        return """
TL;DR: Los layouts organizan widgets y los spacers controlan el espacio sobrante.
- QVBoxLayout apila widgets en vertical.
- QHBoxLayout organiza widgets en horizontal.
- QGridLayout usa filas/columnas para crear grillas.
- addStretch() empuja widgets hacia extremos.
- QSpacerItem permite espacios fijos o expansibles.
- setLayout() aplica el layout a un widget contenedor.
- Anidar layouts permite crear UIs complejas.
- QSizePolicy controla expansión y contracción.
- setSpacing() define separación entre widgets.
- setContentsMargins() ajusta márgenes internos.
- Evita posiciones absolutas para mantener responsividad.
- Un widget sin layout no se ajusta al redimensionar.


## Micro-ejemplo incremental: widgets y ciclo de eventos

### Así se escribe
```py
app = QApplication([])
label = QLabel("Hola Qt")
label.show()
app.exec()
```

### Error típico: crear un widget antes de QApplication
```py
label = QLabel("Hola Qt")
app = QApplication([])
```

```py
QWidget: Must construct a QApplication before a QWidget
```

Explicación breve: el motor de Qt necesita `QApplication` antes de cualquier widget.

### Error típico: olvidar mostrar el widget
```py
app = QApplication([])
label = QLabel("Hola Qt")
app.exec()
```

```py
(no window appears)
```

Explicación breve: si no llamas a `show()`, el widget no se pinta en pantalla.

""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Widget sin layout",
                "No responderá bien al redimensionar la ventana.",
            ),
            (
                "Layout sin setLayout",
                "Si no lo asignas al contenedor, no se muestra.",
            ),
            (
                "Ignorar QSizePolicy",
                "Los widgets no se expanden como esperas.",
            ),
            (
                "Exceso de anidación",
                "Demasiados niveles dificultan mantenimiento.",
            ),
            (
                "No usar stretch",
                "Los widgets quedan pegados sin espacio flexible.",
            ),
            (
                "Confundir grid",
                "Las filas y columnas mal definidas rompen la alineación.",
            ),
            (
                "Márgenes cero",
                "La UI puede verse demasiado comprimida.",
            ),
            (
                "No limpiar layouts",
                "Al cambiar de layout, widgets antiguos permanecen.",
            ),
            (
                "Spacer fijo mal usado",
                "Si necesitas flexibilidad, usa Expanding.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "QVBoxLayout",
                """layout = QVBoxLayout()\nlayout.addWidget(QLabel("Arriba"))\nlayout.addWidget(QLabel("Abajo"))""",
            ),
            (
                "QHBoxLayout",
                """layout = QHBoxLayout()\nlayout.addWidget(QPushButton("Izq"))\nlayout.addWidget(QPushButton("Der"))""",
            ),
            (
                "QGridLayout",
                """layout = QGridLayout()\nlayout.addWidget(QLabel("A"), 0, 0)\nlayout.addWidget(QLabel("B"), 0, 1)""",
            ),
            (
                "Stretch",
                """layout = QHBoxLayout()\nlayout.addWidget(QPushButton("A"))\nlayout.addStretch()\nlayout.addWidget(QPushButton("B"))""",
            ),
            (
                "Spacer",
                """layout = QVBoxLayout()\nspacer = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)\nlayout.addItem(spacer)""",
            ),
            (
                "Márgenes",
                """layout = QVBoxLayout()\nlayout.setContentsMargins(8, 8, 8, 8)""",
            ),
            (
                "Spacing",
                """layout = QGridLayout()\nlayout.setSpacing(12)""",
            ),
            (
                "Anidar layouts",
                """main = QVBoxLayout()\nrow = QHBoxLayout()\nrow.addWidget(QLabel("Nombre"))\nrow.addWidget(QLabel("Valor"))\nmain.addLayout(row)""",
            ),
            (
                "QSizePolicy",
                """btn = QPushButton("Expandir")\nbtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea un QGridLayout con 2 filas y 2 columnas.",
                "hints": ["addWidget", "fila/col"],
                "solution": "layout = QGridLayout()\nlayout.addWidget(QLabel('A'), 0, 0)\nlayout.addWidget(QLabel('B'), 0, 1)\nlayout.addWidget(QLabel('C'), 1, 0)\nlayout.addWidget(QLabel('D'), 1, 1)",
            },
            {
                "question": "Añade un stretch a un QVBoxLayout.",
                "hints": ["addStretch"],
                "solution": "layout = QVBoxLayout()\nlayout.addWidget(QLabel('Arriba'))\nlayout.addStretch()",
            },
            {
                "question": "Configura un spacer expansible en vertical.",
                "hints": ["QSpacerItem", "QSizePolicy.Expanding"],
                "solution": "spacer = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Demo: alterna layouts para el mismo contenido."))

        selector = QComboBox()
        selector.addItems(["Vertical", "Horizontal", "Grid"])
        layout.addWidget(selector)

        container = QWidget()
        layout.addWidget(container)

        def clear_layout(target: QWidget) -> None:
            existing = target.layout()
            if not existing:
                return
            while existing.count():
                item = existing.takeAt(0)
                widget_item = item.widget()
                if widget_item is not None:
                    widget_item.setParent(None)

        def build_layout(tipo: str) -> None:
            clear_layout(container)
            if tipo == "Vertical":
                inner = QVBoxLayout(container)
                inner.addWidget(QPushButton("A"))
                inner.addWidget(QPushButton("B"))
                inner.addStretch()
                inner.addWidget(QPushButton("C"))
            elif tipo == "Horizontal":
                inner = QHBoxLayout(container)
                inner.addWidget(QPushButton("Izq"))
                inner.addStretch()
                inner.addWidget(QPushButton("Centro"))
                inner.addItem(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))
                inner.addWidget(QPushButton("Der"))
            else:
                inner = QGridLayout(container)
                inner.addWidget(QPushButton("1"), 0, 0)
                inner.addWidget(QPushButton("2"), 0, 1)
                inner.addWidget(QPushButton("3"), 1, 0)
                inner.addWidget(QPushButton("4"), 1, 1)
                inner.setRowStretch(2, 1)
                inner.setColumnStretch(2, 1)

        selector.currentTextChanged.connect(build_layout)
        build_layout("Vertical")
        return widget
