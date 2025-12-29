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
## Qué es
Un context manager es un objeto que prepara un recurso y garantiza su cierre con la palabra clave with.

## Cuándo se usa
Cuando trabajas con archivos, conexiones, locks o cualquier recurso que necesita limpieza al terminar.

## Conceptos previos
- Excepciones y bloque try/finally.
- Funciones y clases básicas.

## Paso 1: Usar with con archivos
```
with open("datos.txt", "w") as archivo:
    archivo.write("Hola")
```

## Paso 2: Implementar __enter__ y __exit__
```
class Recurso:
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc, tb):
        return False
```

## Paso 3: Crear context managers con contextlib
```
@contextmanager
def temporizador(nombre):
    inicio = time.perf_counter()
    yield
    fin = time.perf_counter()
    print(f"{nombre}: {fin - inicio:.4f}s")
```

## Paso 4: Manejar varios recursos con ExitStack
```
from contextlib import ExitStack
with ExitStack() as stack:
    f1 = stack.enter_context(open("a.txt"))
    f2 = stack.enter_context(open("b.txt"))
```

## Mini-reto
Mini-reto 1: Crea un context manager que imprima “entrar” y “salir”.
Solución:
```
class Registro:
    def __enter__(self):
        print("Entrar")
        return self
    def __exit__(self, exc_type, exc, tb):
        print("Salir")
        return False
```

## Errores típicos (mal vs bien)
Mal: olvidar devolver el recurso en __enter__.
```
class Malo:
    def __enter__(self):
        print("abro")
```
Bien: devolver el recurso para usarlo en with.
```
class Bueno:
    def __enter__(self):
        print("abro")
        return self
```

## Nota
Nota: __exit__ puede registrar errores y decidir si se propagan.

## Advertencia
Advertencia: si __exit__ devuelve True, la excepción se suprime.

## Checklist final
- Uso with para limpiar recursos.
- Sé implementar __enter__/__exit__.
- Puedo crear context managers con contextlib.
- Conozco ExitStack para múltiples recursos.

## Ver también
- Excepciones
- Funciones
- Iteradores y generadores
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
                """class Recurso:  # Definimos la clase
    def __enter__(self):  # Entramos al contexto
        print("Abrir")  # Abrimos recurso
        return self  # Devolvemos el recurso
    def __exit__(self, exc_type, exc, tb):  # Salimos del contexto
        print("Cerrar")  # Cerramos recurso
with Recurso():  # Usamos el contexto
    print("Usar")  # Trabajamos con el recurso""",
            ),
            (
                "contextmanager",
                """from contextlib import contextmanager  # Importamos helper
import time  # Importamos time
@contextmanager  # Decoramos como context manager
def temporizador(nombre):  # Definimos la función
    inicio = time.perf_counter()  # Tomamos inicio
    yield  # Cedemos el control al bloque
    fin = time.perf_counter()  # Tomamos fin
    print(f"{nombre}: {fin - inicio:.4f}s")  # Imprimimos duración""",
            ),
            (
                "ExitStack",
                """from contextlib import ExitStack  # Importamos ExitStack
with ExitStack() as stack:  # Creamos el stack
    f1 = stack.enter_context(open("a.txt"))  # Abrimos primer archivo
    f2 = stack.enter_context(open("b.txt"))  # Abrimos segundo archivo""",
            ),
            (
                "Múltiples contextos",
                """with open("a.txt") as f, open("b.txt") as g:  # Abrimos ambos
    data = f.read() + g.read()  # Leemos datos""",
            ),
            (
                "Lock",
                """import threading  # Importamos threading
lock = threading.Lock()  # Creamos un lock
with lock:  # Entramos a la sección crítica
    print("sección crítica")  # Ejecutamos trabajo seguro""",
            ),
            (
                "__exit__ y errores",
                """class Silenciador:  # Definimos la clase
    def __enter__(self):  # Entramos al contexto
        return self  # Retornamos el objeto
    def __exit__(self, exc_type, exc, tb):  # Salimos del contexto
        return isinstance(exc, ZeroDivisionError)  # Suprime ZeroDivisionError""",
            ),
            (
                "Temporizador simple",
                """class Timer:  # Definimos la clase
    def __enter__(self):  # Entramos al contexto
        self.start = time.perf_counter()  # Guardamos inicio
        return self  # Retornamos el objeto
    def __exit__(self, exc_type, exc, tb):  # Salimos del contexto
        self.elapsed = time.perf_counter() - self.start  # Calculamos tiempo
with Timer() as t:  # Usamos el temporizador
    sum(range(100000))  # Trabajo a medir
print(t.elapsed)  # Mostramos tiempo""",
            ),
            (
                "Recurso con __enter__",
                """class Repo:  # Definimos la clase
    def __enter__(self):  # Entramos al contexto
        return {"estado": "ok"}  # Devolvemos un recurso
    def __exit__(self, exc_type, exc, tb):  # Salimos del contexto
        pass  # No hacemos nada""",
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
