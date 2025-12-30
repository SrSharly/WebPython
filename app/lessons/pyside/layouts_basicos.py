from __future__ import annotations

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from app.lesson_base import Lesson


class LayoutsBasicosLesson(Lesson):
    TITLE = "Layouts básicos"
    CATEGORY = "PySide6"
    SUBCATEGORY = "Fundamentos UI"
    LEVEL = "Básico"
    TAGS = ["layouts", "QVBoxLayout", "QHBoxLayout", "espaciado"]

    def summary(self) -> str:
        return (
            "Los layouts organizan widgets automáticamente. Aprende a usar "
            "QVBoxLayout, QHBoxLayout y a controlar espacios y alineación."
        )

    def guide(self) -> str:
        return """
- Un layout organiza widgets dentro de un contenedor.
- QVBoxLayout apila widgets verticalmente.
- QHBoxLayout los alinea en horizontal.
- addStretch() crea espacios flexibles.
- setContentsMargins() ajusta márgenes internos.
- Los layouts se asignan con setLayout().
- Un widget sin layout no reacciona a redimensionamientos.
- Puedes anidar layouts para construir composiciones complejas.
- Usa setSpacing() para controlar separación.
- QSizePolicy controla cómo crecen los widgets.
- Evita posiciones absolutas; los layouts son responsivos.
- QSpacerItem añade espacios fijos o expansibles.


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
                "No asignar layout",
                "Si no llamas setLayout(), el layout no aplica.",
            ),
            (
                "Usar posiciones absolutas",
                "Rompe la adaptabilidad al cambiar tamaño.",
            ),
            (
                "Sobrecargar un layout",
                "Demasiados widgets sin organización clara confunden al usuario.",
            ),
            (
                "No usar stretch",
                "Sin stretch los widgets pueden quedar comprimidos.",
            ),
            (
                "Olvidar márgenes",
                "Márgenes cero pueden hacer la UI demasiado pegada.",
            ),
            (
                "Widgets sin parent",
                "Un widget sin parent puede perderse o no mostrarse.",
            ),
            (
                "Anidar sin claridad",
                "Demasiados niveles de layouts dificultan el mantenimiento.",
            ),
            (
                "Espaciado inconsistente",
                "Usa setSpacing para mantener coherencia visual.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Layout vertical",
                """layout = QVBoxLayout()\nlayout.addWidget(QLabel("Arriba"))\nlayout.addWidget(QLabel("Abajo"))""",
            ),
            (
                "Layout horizontal",
                """layout = QHBoxLayout()\nlayout.addWidget(QPushButton("Izq"))\nlayout.addWidget(QPushButton("Der"))""",
            ),
            (
                "Espacio flexible",
                """layout = QVBoxLayout()\nlayout.addWidget(QLabel("A"))\nlayout.addStretch()\nlayout.addWidget(QLabel("B"))""",
            ),
            (
                "Márgenes",
                """layout = QVBoxLayout()\nlayout.setContentsMargins(10, 10, 10, 10)""",
            ),
            (
                "Espaciado",
                """layout = QHBoxLayout()\nlayout.setSpacing(12)""",
            ),
            (
                "Layout anidado",
                """main = QVBoxLayout()\nrow = QHBoxLayout()\nrow.addWidget(QLabel("Nombre"))\nrow.addWidget(QLabel("Valor"))\nmain.addLayout(row)""",
            ),
            (
                "Asignar layout",
                """widget = QWidget()\nlayout = QVBoxLayout(widget)\nwidget.setLayout(layout)""",
            ),
            (
                "QSizePolicy",
                """btn = QPushButton("Expandir")\nbtn.setSizePolicy(btn.sizePolicy().Expanding, btn.sizePolicy().Fixed)""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea un layout vertical con tres etiquetas y un stretch al final.",
                "hints": ["Usa QVBoxLayout", "addStretch"],
                "solution": "layout = QVBoxLayout()\nfor texto in ['A', 'B', 'C']:\n    layout.addWidget(QLabel(texto))\nlayout.addStretch()",
            },
            {
                "question": "¿Qué ventaja tiene un layout frente a posiciones absolutas?",
                "hints": ["Responsivo"],
                "solution": "Los layouts adaptan el tamaño y posición cuando la ventana cambia.",
            },
            {
                "question": "Anida un QHBoxLayout dentro de un QVBoxLayout.",
                "hints": ["addLayout"],
                "solution": "main = QVBoxLayout()\nrow = QHBoxLayout()\nmain.addLayout(row)",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Demo: cambia el orden y observa la distribución."))

        row = QHBoxLayout()
        row.addWidget(QPushButton("Botón 1"))
        row.addWidget(QPushButton("Botón 2"))
        row.addWidget(QPushButton("Botón 3"))

        layout.addLayout(row)
        layout.addStretch()
        return widget
