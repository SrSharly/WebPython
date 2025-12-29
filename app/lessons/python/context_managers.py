from __future__ import annotations

import time
from contextlib import contextmanager

from PySide6.QtWidgets import QLabel, QPushButton, QTextEdit, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class ContextManagersLesson(Lesson):
    TITLE = "Context managers"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Intermedio"
    TAGS = ["with", "contextmanager", "ExitStack", "recursos"]

    def summary(self) -> str:
        return (
            "Los context managers controlan recursos y garantizan limpieza con "
            "with, incluso ante errores, usando __enter__/__exit__ o contextlib."
        )

    def guide(self) -> str:
        return """
TL;DR: Usa with para adquirir y liberar recursos de forma segura y legible.
- Un context manager implementa __enter__ y __exit__.
- with garantiza liberación aunque haya excepciones.
- __enter__ puede devolver un recurso a usar en el bloque.
- __exit__ recibe tipo/instancia/traceback de excepción.
- Si __exit__ devuelve True, la excepción se suprime.
- contextlib.contextmanager crea context managers con yield.
- ExitStack permite manejar múltiples contextos dinámicos.
- Usa context managers para locks, archivos, conexiones y temporizadores.
- Se pueden anidar with o usar múltiples en una línea.
- Evita lógica pesada en __enter__; prepara lo mínimo.
- Registra métricas (tiempo, contadores) con contextos sencillos.
- Los context managers mejoran la legibilidad de la gestión de recursos.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Suprimir excepciones sin querer",
                "Si __exit__ devuelve True, la excepción no se propaga.",
            ),
            (
                "__enter__ sin return",
                "Si necesitas el recurso, devuélvelo explícitamente.",
            ),
            (
                "Hacer trabajo pesado en __enter__",
                "Retrasa el bloque; mejor inicializar antes.",
            ),
            (
                "No liberar recursos",
                "Sin context manager puedes olvidar cerrar archivos o conexiones.",
            ),
            (
                "Confundir contextmanager con generator",
                "El yield marca el punto de ejecución del bloque.",
            ),
            (
                "Usar return en __exit__",
                "Debe devolver bool, no valores de negocio.",
            ),
            (
                "No manejar errores",
                "__exit__ puede registrar o transformar errores si es necesario.",
            ),
            (
                "ExitStack sin cerrar",
                "Siempre usa with ExitStack() para asegurar cleanup.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Context manager básico",
                """class Recurso:\n    def __enter__(self):\n        print("Abrir")\n        return self\n    def __exit__(self, exc_type, exc, tb):\n        print("Cerrar")\n\nwith Recurso():\n    print("Usar")""",
            ),
            (
                "contextmanager",
                """from contextlib import contextmanager\n\n@contextmanager\ndef temporizador(nombre):\n    inicio = time.perf_counter()\n    yield\n    fin = time.perf_counter()\n    print(f"{nombre}: {fin - inicio:.4f}s")""",
            ),
            (
                "ExitStack",
                """from contextlib import ExitStack\n\nwith ExitStack() as stack:\n    f1 = stack.enter_context(open("a.txt"))\n    f2 = stack.enter_context(open("b.txt"))""",
            ),
            (
                "Múltiples contextos",
                """with open("a.txt") as f, open("b.txt") as g:\n    data = f.read() + g.read()""",
            ),
            (
                "Lock",
                """import threading\nlock = threading.Lock()\nwith lock:\n    print("sección crítica")""",
            ),
            (
                "__exit__ y errores",
                """class Silenciador:\n    def __enter__(self):\n        return self\n    def __exit__(self, exc_type, exc, tb):\n        return isinstance(exc, ZeroDivisionError)""",
            ),
            (
                "Temporizador simple",
                """class Timer:\n    def __enter__(self):\n        self.start = time.perf_counter()\n        return self\n    def __exit__(self, exc_type, exc, tb):\n        self.elapsed = time.perf_counter() - self.start\n\nwith Timer() as t:\n    sum(range(100000))\nprint(t.elapsed)""",
            ),
            (
                "Recurso con __enter__",
                """class Repo:\n    def __enter__(self):\n        return {"estado": "ok"}\n    def __exit__(self, exc_type, exc, tb):\n        pass""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea un context manager que registre entrada y salida.",
                "hints": ["Implementa __enter__ y __exit__"],
                "solution": "class Registro:\n    def __enter__(self):\n        print('Entrar')\n        return self\n    def __exit__(self, exc_type, exc, tb):\n        print('Salir')",
            },
            {
                "question": "Usa contextlib.contextmanager para medir tiempo de un bloque.",
                "hints": ["yield", "perf_counter"],
                "solution": "@contextmanager\ndef medir():\n    inicio = time.perf_counter()\n    yield\n    print(time.perf_counter() - inicio)",
            },
            {
                "question": "¿Qué debes devolver en __exit__ para no suprimir excepciones?",
                "hints": ["False"],
                "solution": "Devuelve False (o None) para que la excepción se propague.",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Demo: context manager de temporizador."))
        run_button = QPushButton("Medir bloque")
        output = QTextEdit(readOnly=True)

        class Timer:
            def __init__(self) -> None:
                self.elapsed = 0.0

            def __enter__(self) -> "Timer":
                self._start = time.perf_counter()
                return self

            def __exit__(self, exc_type, exc, tb) -> bool:
                self.elapsed = time.perf_counter() - self._start
                return False

        @contextmanager
        def marcador(nombre: str):
            inicio = time.perf_counter()
            yield
            fin = time.perf_counter()
            output.append(f"{nombre}: {fin - inicio:.4f}s")

        def run_demo() -> None:
            output.clear()
            with Timer() as timer:
                sum(range(200_000))
            output.append(f"Timer class: {timer.elapsed:.4f}s")
            with marcador("contextmanager"):
                sum(range(100_000))

        run_button.clicked.connect(run_demo)
        layout.addWidget(run_button)
        layout.addWidget(output)
        return widget
