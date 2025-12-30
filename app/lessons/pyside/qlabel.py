from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QCheckBox,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from app.lesson_base import Lesson


class QLabelLesson(Lesson):
    TITLE = "QLabel"
    CATEGORY = "PySide6"
    SUBCATEGORY = "Controles"
    LEVEL = "Básico"
    TAGS = ["QLabel", "texto", "alineacion", "richtext"]

    def summary(self) -> str:
        return (
            "QLabel muestra texto o imágenes estáticas. Aprende a formatear, alinear "
            "y actualizar etiquetas para comunicar información clara al usuario."
        )

    def guide(self) -> str:
        return """
## Qué es
QLabel es un widget de solo lectura para mostrar texto o imágenes dentro de una interfaz.

## Cuándo se usa
Para títulos, mensajes de estado, instrucciones o etiquetas de campos de formulario.

## Conceptos previos
- Widgets básicos de PySide6.
- Uso de layouts para organizar la interfaz.

## Paso 1: Mostrar texto simple
```
label = QLabel("Hola mundo")
```

## Paso 2: Alinear y permitir word wrap
```
label.setAlignment(Qt.AlignCenter)
label.setWordWrap(True)
```

## Paso 3: Texto enriquecido (HTML simple)
```
label.setText("<b>Negrita</b>")
label.setTextFormat(Qt.RichText)
```

## Paso 4: Actualizar el contenido en tiempo real
```
label.setText("Estado: procesando")
```

## Mini-reto
Mini-reto 1: Crea un QLabel que muestre “Listo” en verde.
Solución:
```
label = QLabel("Listo")
label.setStyleSheet("color: #1b5e20;")
```

## Errores típicos (mal vs bien)
Mal: texto largo sin word wrap.
```
label.setText("Un texto muy largo que se corta...")
```
Bien: activar word wrap.
```
label.setWordWrap(True)
```

## Nota
Nota: QLabel no es editable; para entrada de texto usa QLineEdit.

## Advertencia
Advertencia: si usas HTML, configura el formato como RichText.

## Checklist final
- Muestro texto con QLabel.
- Ajusto alineación y wrap.
- Uso HTML simple cuando necesito formato.

## Ver también
- QLineEdit
- QPushButton
- QComboBox


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
                "Olvidar word wrap",
                "El texto largo se corta; activa setWordWrap(True).",
            ),
            (
                "Usar HTML sin setTextFormat",
                "Si no usas RichText, el HTML se muestra como texto plano.",
            ),
            (
                "Actualizar sin refrescar estado",
                "Si dependes de datos dinámicos, conecta señales para refrescar.",
            ),
            (
                "Usar QLabel como input",
                "No es editable; usa QLineEdit o QTextEdit.",
            ),
            (
                "No alinear",
                "El contenido puede quedar desordenado; usa setAlignment.",
            ),
            (
                "Texto demasiado pequeño",
                "Evita tamaños ilegibles; ajusta con estilos o fonts.",
            ),
            (
                "Reutilizar QLabel para imágenes sin setPixmap",
                "El texto no se oculta; usa setPixmap o limpia con clear().",
            ),
            (
                "No definir tamaño mínimo",
                "Si el layout colapsa, el texto se corta. Ajusta sizePolicy.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Texto básico",
                """label = QLabel("Hola mundo")  # Creamos el label""",
            ),
            (
                "Alineación centrada",
                """label = QLabel("Centro")  # Creamos el label
label.setAlignment(Qt.AlignCenter)  # Centramos el texto""",
            ),
            (
                "Word wrap",
                """label = QLabel("Texto largo...")  # Creamos el label
label.setWordWrap(True)  # Permitimos salto de línea""",
            ),
            (
                "Texto enriquecido",
                """label = QLabel("<b>Negrita</b>")  # HTML básico
label.setTextFormat(Qt.RichText)  # Indicamos RichText""",
            ),
            (
                "Actualizar texto",
                """label = QLabel("Estado: listo")  # Texto inicial
label.setText("Estado: procesando")  # Actualizamos texto""",
            ),
            (
                "Cambiar estilo",
                """label = QLabel("Error")  # Texto de error
label.setStyleSheet("color: #b00020;")  # Estilo rojo""",
            ),
            (
                "Limpiar contenido",
                """label = QLabel("Mensaje")  # Texto inicial
label.clear()  # Limpiamos contenido""",
            ),
            (
                "Asignar buddy",
                """label = QLabel("Nombre:")  # Label de campo
label.setBuddy(nombre_input)  # Asociamos el input""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea un QLabel con texto 'Bienvenido'.",
                "hints": ["Usa QLabel con el texto inicial"],
                "solution": "label = QLabel('Bienvenido')",
            },
            {
                "question": "Centra un QLabel dentro de su layout.",
                "hints": ["Usa setAlignment"],
                "solution": "label = QLabel('Centro')\nlabel.setAlignment(Qt.AlignCenter)",
            },
            {
                "question": "Muestra un mensaje largo que haga word wrap.",
                "hints": ["setWordWrap(True)"],
                "solution": "label = QLabel('Texto largo...')\nlabel.setWordWrap(True)",
            },
        ]

    def requirements(self) -> list[str]:
        return []

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)

        title = QLabel("Demo: QLabel dinámico con estilos y wrap.")
        title.setStyleSheet("font-weight: bold;")

        label = QLabel("Estado: esperando acción")
        label.setWordWrap(True)
        label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        btn_success = QPushButton("Mostrar éxito")
        btn_warning = QPushButton("Mostrar aviso")
        wrap_toggle = QCheckBox("Activar word wrap")
        wrap_toggle.setChecked(True)

        def show_success() -> None:
            label.setText("Éxito: se guardaron los cambios correctamente.")
            label.setStyleSheet("color: #1b5e20;")

        def show_warning() -> None:
            label.setText("Aviso: faltan datos obligatorios. Revisa el formulario.")
            label.setStyleSheet("color: #b26a00;")

        def toggle_wrap(checked: bool) -> None:
            label.setWordWrap(checked)

        btn_success.clicked.connect(show_success)
        btn_warning.clicked.connect(show_warning)
        wrap_toggle.toggled.connect(toggle_wrap)

        layout.addWidget(title)
        layout.addWidget(label)
        layout.addWidget(btn_success)
        layout.addWidget(btn_warning)
        layout.addWidget(wrap_toggle)
        return widget
