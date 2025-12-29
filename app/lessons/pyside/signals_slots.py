from __future__ import annotations

from functools import partial

from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from app.lesson_base import Lesson


class _CounterEmitter(QObject):
    count_changed = Signal(int)
    message = Signal(str)

    def __init__(self) -> None:
        super().__init__()
        self.count = 0

    def increment(self) -> None:
        self.count += 1
        self.count_changed.emit(self.count)
        self.message.emit(f"Contador en {self.count}")

    def reset(self) -> None:
        self.count = 0
        self.count_changed.emit(self.count)
        self.message.emit("Contador reiniciado")


class SignalsSlotsLesson(Lesson):
    TITLE = "Signals & Slots"
    CATEGORY = "PySide6"
    SUBCATEGORY = "Fundamentos UI"
    LEVEL = "Intermedio"
    TAGS = ["signals", "slots", "Signal", "QObject"]

    def summary(self) -> str:
        return (
            "Las señales y slots conectan eventos con acciones. Aprende a usar señales "
            "integradas, crear señales custom y gestionar conexiones seguras."
        )

    def guide(self) -> str:
        return """
TL;DR: Conecta señales a slots para reaccionar a eventos sin acoplar widgets.
- Las señales built-in vienen en widgets (clicked, textChanged, etc.).
- Las señales custom se declaran con Signal en clases QObject.
- connect enlaza una señal con una función (slot).
- disconnect permite liberar conexiones y evitar duplicados.
- Puedes conectar lambdas o funciones con functools.partial.
- Las señales pueden emitir argumentos (int, str, objetos).
- Un slot puede recibir solo los argumentos que necesita.
- Evita conectar múltiples veces sin limpiar.
- Guarda referencias a objetos que emiten señales.
- Si un widget se destruye, sus señales dejan de emitir.
- Usa Qt.QueuedConnection para hilos (avanzado).
- Documenta qué emite cada señal custom.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Conectar múltiples veces",
                "Si conectas en cada click, el slot se ejecuta duplicado.",
            ),
            (
                "Widget destruido",
                "Si se destruye el emisor, la señal deja de existir.",
            ),
            (
                "Capturas en lambdas",
                "Si usas variables mutables en lambdas, pueden cambiar inesperadamente.",
            ),
            (
                "No desconectar",
                "Mantiene referencias y puede causar efectos extraños.",
            ),
            (
                "Slot con firma incompatible",
                "Si el slot no acepta los args esperados, falla la conexión.",
            ),
            (
                "No guardar referencia al QObject",
                "Si se recolecta, la señal no se emite.",
            ),
            (
                "Olvidar emitir",
                "Declarar Signal no basta, hay que llamar emit().",
            ),
            (
                "Usar self.clicked mal",
                "Conecta a clicked, no lo llames como función.",
            ),
            (
                "Conectar slots costosos",
                "Slots lentos bloquean la UI; delega o usa hilos.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Señal built-in",
                """btn = QPushButton("OK")\nbtn.clicked.connect(lambda: print("click"))""",
            ),
            (
                "Señal custom",
                """class Emisor(QObject):\n    cambio = Signal(int)\n\nemisor = Emisor()\nemisor.cambio.connect(print)\nemisor.cambio.emit(3)""",
            ),
            (
                "Conectar slot con args",
                """def on_cambio(valor: int) -> None:\n    print(valor)\n\nemisor.cambio.connect(on_cambio)""",
            ),
            (
                "Lambda",
                """btn.clicked.connect(lambda: print("Hola"))""",
            ),
            (
                "functools.partial",
                """from functools import partial\n\nbtn.clicked.connect(partial(print, "evento"))""",
            ),
            (
                "Desconectar",
                """btn.clicked.disconnect()""",
            ),
            (
                "Señal con múltiples slots",
                """btn.clicked.connect(slot_a)\nbtn.clicked.connect(slot_b)""",
            ),
            (
                "Slot sin usar args",
                """def solo_log(*_):\n    print("evento")\n\nemisor.cambio.connect(solo_log)""",
            ),
            (
                "Señal personalizada con texto",
                """class Logger(QObject):\n    mensaje = Signal(str)""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Declara una clase QObject con Signal[str] llamado mensaje.",
                "hints": ["Signal", "QObject"],
                "solution": "class Emisor(QObject):\n    mensaje = Signal(str)",
            },
            {
                "question": "Conecta un QPushButton.clicked a una función que imprima 'ok'.",
                "hints": ["connect", "clicked"],
                "solution": "btn = QPushButton('OK')\nbtn.clicked.connect(lambda: print('ok'))",
            },
            {
                "question": "¿Cómo evitas conexiones duplicadas?",
                "hints": ["disconnect"],
                "solution": "Desconecta antes de volver a conectar o controla un flag de conexión.",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        info = QLabel("Demo: señales custom, contador y log.")
        contador = QLabel("Contador: 0")
        log = QTextEdit()
        log.setReadOnly(True)

        emitter = _CounterEmitter()
        connected = {"value": True}

        def update_count(value: int) -> None:
            contador.setText(f"Contador: {value}")

        emitter.count_changed.connect(update_count)
        emitter.message.connect(partial(log.append, "[Signal]"))

        inc_btn = QPushButton("Incrementar")
        reset_btn = QPushButton("Reset")
        toggle_btn = QPushButton("Desconectar señales")

        def toggle_connections() -> None:
            if connected["value"]:
                emitter.count_changed.disconnect(update_count)
                emitter.message.disconnect()
                toggle_btn.setText("Conectar señales")
                log.append("[Sistema] Señales desconectadas")
            else:
                emitter.count_changed.connect(update_count)
                emitter.message.connect(partial(log.append, "[Signal]"))
                toggle_btn.setText("Desconectar señales")
                log.append("[Sistema] Señales conectadas")
            connected["value"] = not connected["value"]

        inc_btn.clicked.connect(emitter.increment)
        reset_btn.clicked.connect(emitter.reset)
        toggle_btn.clicked.connect(toggle_connections)

        layout.addWidget(info)
        layout.addWidget(contador)
        layout.addWidget(inc_btn)
        layout.addWidget(reset_btn)
        layout.addWidget(toggle_btn)
        layout.addWidget(log)
        return widget
