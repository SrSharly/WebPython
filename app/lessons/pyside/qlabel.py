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
- QLabel es un widget de solo lectura para texto o imágenes.
- setText() actualiza el contenido en tiempo real.
- setWordWrap(True) permite texto largo sin romper el layout.
- setAlignment() controla la alineación horizontal y vertical.
- setTextFormat() define si interpreta texto enriquecido (HTML).
- setPixmap() muestra imágenes en lugar de texto.
- setBuddy() permite asociar un label a un input.
- Ajusta el tamaño con setMinimumWidth o sizePolicy.
- Usa estilos con setStyleSheet para resaltar mensajes.
- QLabel no es editable; para texto editable usa QLineEdit.
- Puedes usar HTML simple para resaltar partes específicas.
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
                """label = QLabel("Hola mundo")""",
            ),
            (
                "Alineación centrada",
                """label = QLabel("Centro")\nlabel.setAlignment(Qt.AlignCenter)""",
            ),
            (
                "Word wrap",
                """label = QLabel("Texto largo...")\nlabel.setWordWrap(True)""",
            ),
            (
                "Texto enriquecido",
                """label = QLabel("<b>Negrita</b>")\nlabel.setTextFormat(Qt.RichText)""",
            ),
            (
                "Actualizar texto",
                """label = QLabel("Estado: listo")\nlabel.setText("Estado: procesando")""",
            ),
            (
                "Cambiar estilo",
                """label = QLabel("Error")\nlabel.setStyleSheet("color: #b00020;")""",
            ),
            (
                "Limpiar contenido",
                """label = QLabel("Mensaje")\nlabel.clear()""",
            ),
            (
                "Asignar buddy",
                """label = QLabel("Nombre:")\nlabel.setBuddy(nombre_input)""",
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
