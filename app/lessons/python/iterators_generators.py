from __future__ import annotations

import sys
import time

from PySide6.QtWidgets import QLabel, QPushButton, QTextEdit, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class IteratorsGeneratorsLesson(Lesson):
    TITLE = "Iteradores y generadores"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Intermedio"
    TAGS = ["iter", "next", "generators", "yield", "lazy"]

    def summary(self) -> str:
        return (
            "Los iteradores y generadores permiten recorrer datos de forma eficiente, "
            "con evaluación perezosa y patrones útiles para pipelines y streams."
        )

    def guide(self) -> str:
        return """
TL;DR: Iteradores y generadores consumen datos paso a paso, ahorrando memoria y facilitando pipelines.
- Un iterable es cualquier objeto con __iter__ (listas, strings, dicts).
- Un iterador es el objeto devuelto por iter(), con __next__.
- next(it) avanza y lanza StopIteration al terminar.
- Iterables pueden producir múltiples iteradores; iteradores se consumen una vez.
- Las funciones generator usan yield para producir valores en secuencia.
- yield from delega la iteración a otro iterable o generador.
- Los generadores son perezosos: calculan cuando se necesitan.
- send(valor) permite enviar datos a un generador pausado (uso avanzado).
- Los generadores son ideales para streams y archivos grandes.
- Evita convertir a lista si no necesitas todo el resultado.
- Usa pipelines de generadores para transformar datos en etapas.
- Maneja StopIteration si implementas iteradores manuales.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Consumir un generador",
                "Una vez iterado, no puedes reutilizarlo sin recrearlo.",
            ),
            (
                "Reusar un iterador",
                "Un iterador agotado no vuelve a empezar.",
            ),
            (
                "Convertir a lista sin querer",
                "list(...) materializa todo y puede agotar memoria.",
            ),
            (
                "Confundir iterable vs iterador",
                "Un iterable crea iteradores; un iterador ya está en progreso.",
            ),
            (
                "Olvidar StopIteration",
                "next(it) sin control puede romper el flujo.",
            ),
            (
                "Mutar mientras iteras",
                "Modificar la colección puede saltar elementos.",
            ),
            (
                "Usar send sin primar",
                "Hay que avanzar hasta el primer yield antes de send().",
            ),
            (
                "Hacer eager sin necesidad",
                "Usar list en pipelines rompe la evaluación perezosa.",
            ),
            (
                "No cerrar generadores",
                "Generadores con recursos deben cerrarse o usarse con context managers.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Iterable vs iterador",
                """data = [1, 2, 3]\nit = iter(data)\nprint(next(it))\nprint(next(it))""",
            ),
            (
                "StopIteration",
                """it = iter([1])\ntry:\n    next(it)\n    next(it)\nexcept StopIteration:\n    print("Se terminó")""",
            ),
            (
                "Generador básico",
                """def cuenta(n):\n    for i in range(n):\n        yield i\n\nprint(list(cuenta(3)))""",
            ),
            (
                "yield from",
                """def a():\n    yield from [1, 2, 3]\n\nprint(list(a()))""",
            ),
            (
                "Pipeline perezoso",
                """data = range(5)\ncuadrados = (x * x for x in data)\npares = (x for x in cuadrados if x % 2 == 0)\nprint(list(pares))""",
            ),
            (
                "Iterador manual",
                """class Contador:\n    def __init__(self, tope):\n        self.actual = 0\n        self.tope = tope\n    def __iter__(self):\n        return self\n    def __next__(self):\n        if self.actual >= self.tope:\n            raise StopIteration\n        valor = self.actual\n        self.actual += 1\n        return valor\n\nprint(list(Contador(3)))""",
            ),
            (
                "send en generador",
                """def acumulador():\n    total = 0\n    while True:\n        valor = yield total\n        if valor is None:\n            break\n        total += valor\n\ngen = acumulador()\nprint(next(gen))\nprint(gen.send(5))\nprint(gen.send(3))""",
            ),
            (
                "Lectura simulada de líneas",
                """def leer_lineas():\n    for linea in ["a", "b", "c"]:\n        yield linea\n\nfor linea in leer_lineas():\n    print(linea)""",
            ),
            (
                "Recrear iterador",
                """data = [1, 2]\nit = iter(data)\nlist(it)\nit = iter(data)\nprint(list(it))""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea un generador que produzca los primeros n números pares.",
                "hints": ["Usa yield", "Incrementa de 2 en 2"],
                "solution": "def pares(n):\n    for i in range(n):\n        yield i * 2",
            },
            {
                "question": "Convierte un iterable en iterador y usa next() tres veces.",
                "hints": ["iter()", "next()"],
                "solution": "data = [10, 20, 30, 40]\nit = iter(data)\nprint(next(it))\nprint(next(it))\nprint(next(it))",
            },
            {
                "question": "Implementa un iterador manual que recorra una lista al revés.",
                "hints": ["__iter__", "__next__"],
                "solution": "class Reverso:\n    def __init__(self, data):\n        self.data = data\n        self.idx = len(data) - 1\n    def __iter__(self):\n        return self\n    def __next__(self):\n        if self.idx < 0:\n            raise StopIteration\n        valor = self.data[self.idx]\n        self.idx -= 1\n        return valor",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Demo: pipeline perezoso vs lista materializada."))
        run_button = QPushButton("Ejecutar comparación")
        output = QTextEdit(readOnly=True)

        def run_demo() -> None:
            data = list(range(200_000))
            start_list = time.perf_counter()
            lista_pipeline = [n * 2 for n in data]
            suma_lista = sum(n for n in lista_pipeline if n % 3 == 0)
            tiempo_lista = time.perf_counter() - start_list
            memoria_lista = sys.getsizeof(lista_pipeline)

            start_gen = time.perf_counter()
            gen_pipeline = (n * 2 for n in data)
            suma_gen = sum(n for n in gen_pipeline if n % 3 == 0)
            tiempo_gen = time.perf_counter() - start_gen
            memoria_gen = sys.getsizeof(gen_pipeline)

            output.setText(
                "\n".join(
                    [
                        "Resultados (datos sintéticos):",
                        f"Lista -> suma: {suma_lista}, tiempo: {tiempo_lista:.4f}s, tamaño: {memoria_lista} bytes",
                        f"Generator -> suma: {suma_gen}, tiempo: {tiempo_gen:.4f}s, tamaño: {memoria_gen} bytes",
                        "Nota: el generador se consume una vez; recrea si necesitas reusar.",
                    ]
                )
            )

        run_button.clicked.connect(run_demo)
        layout.addWidget(run_button)
        layout.addWidget(output)
        return widget
