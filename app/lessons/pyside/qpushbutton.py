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
## Qué es
QPushButton es el botón clásico de Qt para ejecutar acciones con un clic.

## Cuándo se usa
Cuando necesitas disparar una acción (guardar, enviar, confirmar) o activar/desactivar un estado.

## Conceptos previos
- Widgets básicos en PySide6.
- Señales y slots (conectar eventos).

## Paso 1: Crear un botón
```
btn = QPushButton("Guardar")
```

## Paso 2: Conectar la señal clicked
```
btn.clicked.connect(lambda: print("Guardado"))
```

## Paso 3: Botón checkable (on/off)
```
btn.setCheckable(True)
btn.toggled.connect(lambda estado: print(estado))
```

## Paso 4: Deshabilitar cuando no aplica
```
btn.setEnabled(False)
```

## Mini-reto
Mini-reto 1: Crea un botón que cambie su texto a “Listo” cuando se haga clic.
Solución:
```
btn = QPushButton("Procesar")
btn.clicked.connect(lambda: btn.setText("Listo"))
```

## Errores típicos (mal vs bien)
Mal: hacer trabajo pesado en clicked y congelar la UI.
```
btn.clicked.connect(lambda: tarea_lenta())
```
Bien: mover el trabajo pesado a otro hilo o mostrar feedback.
```
btn.clicked.connect(lambda: print("Procesando..."))
```

## Nota
Nota: usa tooltips si la acción no es obvia.

## Advertencia
Advertencia: un botón sin conexión no hace nada, siempre conecta señales.

## Checklist final
- Creo botones y conecto clicked.
- Uso setCheckable y toggled cuando necesito estado.
- Deshabilito acciones cuando no aplican.

## Ver también
- QLabel
- QLineEdit
- QComboBox
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
                """btn = QPushButton("Guardar")  # Creamos el botón
btn.clicked.connect(lambda: print("Guardado"))  # Conectamos clicked""",
            ),
            (
                "Deshabilitar",
                """btn = QPushButton("Enviar")  # Creamos el botón
btn.setEnabled(False)  # Lo deshabilitamos""",
            ),
            (
                "Botón checkable",
                """btn = QPushButton("Modo oscuro")  # Creamos botón
btn.setCheckable(True)  # Habilitamos estado
btn.toggled.connect(print)  # Mostramos el estado""",
            ),
            (
                "Tooltip",
                """btn = QPushButton("Ayuda")  # Botón de ayuda
btn.setToolTip("Muestra ayuda")  # Texto de ayuda""",
            ),
            (
                "Cambiar texto",
                """btn = QPushButton("Start")  # Texto inicial
btn.setText("Stop")  # Cambiamos el texto""",
            ),
            (
                "Señales pressed/released",
                """btn = QPushButton("Grabando")  # Creamos botón
btn.pressed.connect(lambda: print("presionado"))  # Señal pressed
btn.released.connect(lambda: print("liberado"))  # Señal released""",
            ),
            (
                "Anidar en layout",
                """layout = QVBoxLayout()  # Creamos layout
layout.addWidget(QPushButton("Aceptar"))  # Añadimos botón""",
            ),
            (
                "Estilos simples",
                """btn = QPushButton("Importante")  # Creamos botón
btn.setStyleSheet("font-weight: bold;")  # Aplicamos estilo""",
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
