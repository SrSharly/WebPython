from __future__ import annotations

from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from app.lesson_base import Lesson


class QLineEditLesson(Lesson):
    TITLE = "QLineEdit"
    CATEGORY = "PySide6"
    SUBCATEGORY = "Controles"
    LEVEL = "Básico"
    TAGS = ["QLineEdit", "inputs", "signals", "validacion"]

    def summary(self) -> str:
        return (
            "QLineEdit permite capturar texto del usuario. Aprende señales, validación "
            "y formatos para crear formularios robustos."
        )

    def guide(self) -> str:
        return """
- QLineEdit captura texto en una sola línea.
- textChanged se emite al cambiar el texto.
- returnPressed se emite al presionar Enter.
- setPlaceholderText muestra ayuda contextual.
- setEchoMode permite ocultar contraseñas.
- setValidator valida entradas (numéricas, regex).
- Usa clear() para limpiar rápidamente.
- readOnly evita cambios del usuario.
- setMaxLength limita caracteres.
- Selecciona texto con selectAll().
- Puedes usar input masks para formatos.
- Conecta señales para validación en vivo.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "No validar",
                "Entradas libres pueden causar errores en lógica posterior.",
            ),
            (
                "Usar echo incorrecto",
                "No uses Normal para contraseñas; usa Password.",
            ),
            (
                "No manejar enter",
                "Si se espera envío, conecta returnPressed.",
            ),
            (
                "No limitar longitud",
                "Textos largos pueden romper layouts.",
            ),
            (
                "No usar placeholder",
                "El usuario no sabe qué escribir.",
            ),
            (
                "Validación tardía",
                "Validar al final genera fricción; valida en vivo.",
            ),
            (
                "No limpiar errores",
                "Si corriges, actualiza mensajes de error.",
            ),
            (
                "No deshabilitar",
                "Deshabilita si depende de otra entrada.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Placeholder",
                """line = QLineEdit()\nline.setPlaceholderText("Nombre")""",
            ),
            (
                "Capturar enter",
                """line = QLineEdit()\nline.returnPressed.connect(lambda: print(line.text()))""",
            ),
            (
                "Modo contraseña",
                """line = QLineEdit()\nline.setEchoMode(QLineEdit.Password)""",
            ),
            (
                "Limitar longitud",
                """line = QLineEdit()\nline.setMaxLength(12)""",
            ),
            (
                "Solo lectura",
                """line = QLineEdit()\nline.setReadOnly(True)""",
            ),
            (
                "Señal textChanged",
                """line = QLineEdit()\nline.textChanged.connect(lambda text: print(text))""",
            ),
            (
                "Limpiar input",
                """line = QLineEdit()\nline.clear()""",
            ),
            (
                "Seleccionar todo",
                """line = QLineEdit()\nline.selectAll()""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea un QLineEdit con placeholder 'Email'.",
                "hints": ["Usa setPlaceholderText"],
                "solution": "line = QLineEdit()\nline.setPlaceholderText('Email')",
            },
            {
                "question": "Conecta returnPressed para imprimir el texto.",
                "hints": ["line.text()"],
                "solution": "line = QLineEdit()\nline.returnPressed.connect(lambda: print(line.text()))",
            },
            {
                "question": "Configura un QLineEdit en modo contraseña.",
                "hints": ["QLineEdit.Password"],
                "solution": "line = QLineEdit()\nline.setEchoMode(QLineEdit.Password)",
            },
        ]

    def requirements(self) -> list[str]:
        return []

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        info = QLabel("Demo: validación simple de longitud.")
        line = QLineEdit()
        line.setPlaceholderText("Escribe al menos 5 caracteres")
        status = QLabel("Estado: esperando")
        submit = QPushButton("Enviar")
        submit.setEnabled(False)

        def on_change(text: str) -> None:
            ok = len(text) >= 5
            submit.setEnabled(ok)
            status.setText("Estado: listo" if ok else "Estado: mínimo 5 caracteres")

        line.textChanged.connect(on_change)
        submit.clicked.connect(lambda: status.setText(f"Enviado: {line.text()}"))

        layout.addWidget(info)
        layout.addWidget(line)
        layout.addWidget(submit)
        layout.addWidget(status)
        return widget
