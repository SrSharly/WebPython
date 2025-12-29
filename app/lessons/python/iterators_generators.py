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
## Qué es
Un iterable es algo que puedes recorrer; un iterador es quien te da los valores uno a uno; un generador es una forma fácil de crear iteradores.

## Cuándo se usa
Cuando quieres procesar datos grandes sin cargarlos todos en memoria o crear pipelines de datos.

## Conceptos previos
- Listas y bucles for.
- Funciones y flujo básico.

## Paso 1: Diferenciar iterable vs iterador
```
data = [1, 2, 3]
it = iter(data)
```

## Paso 2: Avanzar con next()
```
print(next(it))
print(next(it))
```

## Paso 3: Crear un generador con yield
```
def cuenta(n):
    for i in range(n):
        yield i
```

## Paso 4: Pipelines perezosos
```
data = range(5)
cuadrados = (x * x for x in data)
pares = (x for x in cuadrados if x % 2 == 0)
```

## Mini-reto
Mini-reto 1: Genera los primeros 3 números impares.
Solución:
```
def impares(n):
    for i in range(n):
        yield i * 2 + 1
```

## Errores típicos (mal vs bien)
Mal: convertir a lista cuando no hace falta.
```
list(cuenta(1000000))
```
Bien: iterar perezosamente.
```
for valor in cuenta(3):
    print(valor)
```

## Nota
Nota: un iterador se consume una vez; si necesitas reusar, créalo de nuevo.

## Advertencia
Advertencia: modificar una colección mientras iteras puede saltarse elementos.

## Checklist final
- Distingo iterable, iterador y generador.
- Uso iter() y next().
- Creo generadores con yield.
- Aplico pipelines perezosos.

## Ver también
- Funciones
- Context managers
- Variables y tipos
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
                """data = [1, 2, 3]  # Iterable
it = iter(data)  # Obtenemos el iterador
print(next(it))  # Primer elemento
print(next(it))  # Segundo elemento""",
            ),
            (
                "StopIteration",
                """it = iter([1])  # Creamos iterador
try:  # Iniciamos el bloque try
    next(it)  # Primer valor
    next(it)  # Provoca StopIteration
except StopIteration:  # Capturamos el fin
    print("Se terminó")  # Mensaje""",
            ),
            (
                "Generador básico",
                """def cuenta(n):  # Definimos el generador
    for i in range(n):  # Recorremos el rango
        yield i  # Emitimos el valor
print(list(cuenta(3)))  # Materializamos para ver""",
            ),
            (
                "yield from",
                """def a():  # Definimos el generador
    yield from [1, 2, 3]  # Delegamos al iterable
print(list(a()))  # Mostramos resultados""",
            ),
            (
                "Pipeline perezoso",
                """data = range(5)  # Iterable base
cuadrados = (x * x for x in data)  # Generador de cuadrados
pares = (x for x in cuadrados if x % 2 == 0)  # Filtramos pares
print(list(pares))  # Materializamos para mostrar""",
            ),
            (
                "Iterador manual",
                """class Contador:  # Definimos la clase
    def __init__(self, tope):  # Inicializamos
        self.actual = 0  # Contador actual
        self.tope = tope  # Límite
    def __iter__(self):  # Devolvemos el iterador
        return self  # Retornamos self
    def __next__(self):  # Siguiente elemento
        if self.actual >= self.tope:  # Verificamos fin
            raise StopIteration  # Detenemos iteración
        valor = self.actual  # Guardamos valor
        self.actual += 1  # Incrementamos
        return valor  # Devolvemos valor
print(list(Contador(3)))  # Mostramos la lista""",
            ),
            (
                "send en generador",
                """def acumulador():  # Definimos el generador
    total = 0  # Inicializamos total
    while True:  # Bucle infinito
        valor = yield total  # Esperamos envío
        if valor is None:  # Señal de salida
            break  # Salimos del bucle
        total += valor  # Acumulamos
gen = acumulador()  # Creamos generador
print(next(gen))  # Primamos generador
print(gen.send(5))  # Enviamos 5
print(gen.send(3))  # Enviamos 3""",
            ),
            (
                "Lectura simulada de líneas",
                """def leer_lineas():  # Definimos generador
    for linea in ["a", "b", "c"]:  # Iteramos sobre lista
        yield linea  # Emitimos cada línea
for linea in leer_lineas():  # Recorremos el generador
    print(linea)  # Imprimimos la línea""",
            ),
            (
                "Recrear iterador",
                """data = [1, 2]  # Lista base
it = iter(data)  # Creamos iterador
list(it)  # Consumimos
it = iter(data)  # Recreamos iterador
print(list(it))  # Mostramos valores""",
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
