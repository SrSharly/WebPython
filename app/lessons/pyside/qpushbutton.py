from __future__ import annotations

from PySide6.QtWidgets import (
    QCheckBox,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from app.lesson_base import Lesson


class QPushButtonLesson(Lesson):
    TITLE = "QPushButton"
    CATEGORY = "PySide6"
    SUBCATEGORY = "Controles"
    LEVEL = "Básico"
    TAGS = ["QPushButton", "signals", "click"]

    def summary(self) -> str:
        return (
            "QPushButton es el botón estándar de Qt. Aprende a manejar clicks, "
            "estados y señales para crear interacciones claras."
        )

    def guide(self) -> str:
        return """
- QPushButton dispara la señal clicked cuando se pulsa.
- Puedes conectar clicked a funciones o lambdas.
- setEnabled() deshabilita el botón.
- setCheckable() permite estados on/off.
- setText() cambia el texto dinámicamente.
- setIcon() añade un icono al botón.
- Usa tooltips para explicar acciones.
- Qt maneja el foco y accesibilidad automáticamente.
- Usa estilos con setStyleSheet para personalizar.
- Los botones deben tener parent o estar en un layout.
- Usa la señal toggled para botones checkables.
- Emite pressed y released para acciones avanzadas.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "No conectar señales",
                "El botón no hará nada si clicked no está conectado.",
            ),
            (
                "No usar setCheckable",
                "Si esperas un estado toggled debes marcarlo como checkable.",
            ),
            (
                "Falta de feedback",
                "Si una acción tarda, el usuario no sabe si se ejecutó.",
            ),
            (
                "Hacer trabajo pesado en clicked",
                "Bloquea la UI si la acción es costosa.",
            ),
            (
                "Texto ambiguo",
                "Evita etiquetas como 'OK' sin contexto.",
            ),
            (
                "No deshabilitar",
                "Si una acción no aplica, deshabilita el botón.",
            ),
            (
                "No manejar toggled",
                "Los botones checkables requieren lógica para estados.",
            ),
            (
                "Estilos inconsistentes",
                "Un estilo diferente al resto rompe coherencia visual.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Botón simple",
                """btn = QPushButton("Guardar")\nbtn.clicked.connect(lambda: print("Guardado"))""",
            ),
            (
                "Deshabilitar",
                """btn = QPushButton("Enviar")\nbtn.setEnabled(False)""",
            ),
            (
                "Botón checkable",
                """btn = QPushButton("Modo oscuro")\nbtn.setCheckable(True)\nbtn.toggled.connect(print)""",
            ),
            (
                "Tooltip",
                """btn = QPushButton("Ayuda")\nbtn.setToolTip("Muestra ayuda")""",
            ),
            (
                "Cambiar texto",
                """btn = QPushButton("Start")\nbtn.setText("Stop")""",
            ),
            (
                "Señales pressed/released",
                """btn = QPushButton("Grabando")\nbtn.pressed.connect(lambda: print("presionado"))\nbtn.released.connect(lambda: print("liberado"))""",
            ),
            (
                "Anidar en layout",
                """layout = QVBoxLayout()\nlayout.addWidget(QPushButton("Aceptar"))""",
            ),
            (
                "Estilos simples",
                """btn = QPushButton("Importante")\nbtn.setStyleSheet("font-weight: bold;")""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea un botón que imprima 'Hola' al hacer click.",
                "hints": ["Conecta clicked a una lambda"],
                "solution": "btn = QPushButton('Hola')\nbtn.clicked.connect(lambda: print('Hola'))",
            },
            {
                "question": "Convierte un botón en checkable y maneja toggled.",
                "hints": ["Usa setCheckable"],
                "solution": "btn = QPushButton('On/Off')\nbtn.setCheckable(True)\nbtn.toggled.connect(print)",
            },
            {
                "question": "Deshabilita un botón si un checkbox está desmarcado.",
                "hints": ["Conecta stateChanged"],
                "solution": "checkbox = QCheckBox('Activo')\nbtn = QPushButton('Acción')\ncheckbox.stateChanged.connect(lambda state: btn.setEnabled(state == 2))",
            },
        ]

    def requirements(self) -> list[str]:
        return []

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)

        info = QLabel("Demo: botón toggle con estado y feedback.")
        status = QLabel("Estado: apagado")
        toggle_btn = QPushButton("Activar")
        toggle_btn.setCheckable(True)

        def on_toggled(checked: bool) -> None:
            status.setText("Estado: encendido" if checked else "Estado: apagado")
            toggle_btn.setText("Desactivar" if checked else "Activar")

        toggle_btn.toggled.connect(on_toggled)

        demo_checkbox = QCheckBox("Habilitar botón")
        demo_checkbox.setChecked(True)
        demo_checkbox.stateChanged.connect(lambda state: toggle_btn.setEnabled(state == 2))

        layout.addWidget(info)
        layout.addWidget(status)
        layout.addWidget(toggle_btn)
        layout.addWidget(demo_checkbox)
        return widget
