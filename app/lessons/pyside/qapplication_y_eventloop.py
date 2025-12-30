from __future__ import annotations

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from app.lesson_base import Lesson


class QApplicationEventLoopLesson(Lesson):
    TITLE = "QApplication y event loop"
    CATEGORY = "PySide6"
    SUBCATEGORY = "Fundamentos UI"
    LEVEL = "Básico"
    TAGS = ["QApplication", "event-loop", "signals", "slots"]

    def summary(self) -> str:
        return (
            "QApplication inicia la app Qt y el event loop procesa eventos, señales "
            "y repintados. Sin él, la UI no responde."
        )

    def guide(self) -> str:
        return """
- QApplication gestiona el ciclo de vida de la aplicación.
- Solo debe existir una instancia de QApplication.
- El event loop comienza con app.exec().
- Las señales se encolan y se procesan en el loop.
- Usa QTimer para tareas periódicas sin bloquear la UI.
- Los widgets deben crearse después de QApplication.
- main() suele crear QApplication y la ventana principal.
- app.quit() cierra la aplicación.
- QApplication.processEvents() fuerza el procesamiento, úsalo con moderación.
- Evita operaciones largas en el hilo UI; usa QThread o QRunnable.
- El event loop también maneja input del usuario.
- Usa señales para comunicar entre widgets.


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
                "Crear widgets antes de QApplication",
                "Qt necesita QApplication creada antes de instanciar widgets.",
            ),
            (
                "Bloquear el hilo principal",
                "Loops largos sin dormir congelan la interfaz.",
            ),
            (
                "Usar sleep en la UI",
                "time.sleep detiene el event loop; usa QTimer.",
            ),
            (
                "Crear múltiples QApplication",
                "Solo debe existir una instancia por proceso.",
            ),
            (
                "No llamar a app.exec()",
                "La ventana se cierra inmediatamente sin event loop.",
            ),
            (
                "Señales sin conexión",
                "Si no conectas señales, los eventos no ejecutan acciones.",
            ),
            (
                "No cerrar ventanas",
                "Usa close() o app.quit() para terminar correctamente.",
            ),
            (
                "Eliminar widgets manualmente",
                "Qt gestiona memoria con parent-child; evita del directo.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Estructura mínima",
                """from PySide6.QtWidgets import QApplication, QLabel\nimport sys\n\napp = QApplication(sys.argv)\nlabel = QLabel("Hola Qt")\nlabel.show()\nsys.exit(app.exec())""",
            ),
            (
                "Uso de QTimer",
                """from PySide6.QtCore import QTimer\n\ncontador = 0\n\ndef tick():\n    global contador\n    contador += 1\n    print("Tick", contador)\n\nQTimer.singleShot(1000, tick)""",
            ),
            (
                "Cerrar aplicación",
                """from PySide6.QtWidgets import QApplication\n\napp = QApplication([])\napp.quit()""",
            ),
            (
                "Conectar señal",
                """from PySide6.QtWidgets import QPushButton\n\nbtn = QPushButton("Click")\nbtn.clicked.connect(lambda: print("Hola"))""",
            ),
            (
                "Procesar eventos",
                """from PySide6.QtWidgets import QApplication\n\napp = QApplication.instance()\nif app:\n    app.processEvents()""",
            ),
            (
                "Instancia única",
                """from PySide6.QtWidgets import QApplication\n\napp = QApplication.instance() or QApplication([])""",
            ),
            (
                "QTimer periódico",
                """timer = QTimer()\ntimer.setInterval(500)\ntimer.timeout.connect(lambda: print("tick"))\ntimer.start()""",
            ),
            (
                "Mostrar ventana",
                """from PySide6.QtWidgets import QWidget\n\nw = QWidget()\nw.setWindowTitle("Demo")\nw.show()""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "¿Por qué no debes usar time.sleep en el hilo UI?",
                "hints": ["Bloquea el event loop", "Piensa en la UI congelada"],
                "solution": "Porque detiene el event loop y la interfaz deja de responder.",
            },
            {
                "question": "Crea un QTimer que imprima 'Hola' cada segundo.",
                "hints": ["Usa setInterval y timeout.connect"],
                "solution": "timer = QTimer()\ntimer.setInterval(1000)\ntimer.timeout.connect(lambda: print('Hola'))\ntimer.start()",
            },
            {
                "question": "¿Qué hace QApplication.instance()?",
                "hints": ["Retorna la instancia actual"],
                "solution": "Devuelve la instancia de QApplication existente o None.",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        info = QLabel("Demo: un contador con QTimer que actualiza la UI.")
        counter_label = QLabel("Contador: 0")
        start_btn = QPushButton("Iniciar")
        stop_btn = QPushButton("Detener")
        stop_btn.setEnabled(False)

        timer = QTimer(widget)
        timer.setInterval(500)
        state = {"count": 0}

        def on_timeout() -> None:
            state["count"] += 1
            counter_label.setText(f"Contador: {state['count']}")

        def start() -> None:
            timer.start()
            start_btn.setEnabled(False)
            stop_btn.setEnabled(True)

        def stop() -> None:
            timer.stop()
            start_btn.setEnabled(True)
            stop_btn.setEnabled(False)

        timer.timeout.connect(on_timeout)
        start_btn.clicked.connect(start)
        stop_btn.clicked.connect(stop)

        layout.addWidget(info)
        layout.addWidget(counter_label)
        layout.addWidget(start_btn)
        layout.addWidget(stop_btn)
        return widget
