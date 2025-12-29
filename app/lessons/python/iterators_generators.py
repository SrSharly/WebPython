from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class IteratorsGeneratorsLesson(Lesson):
    TITLE = "Iteradores y generadores"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Intermedio"
    TAGS = ["iteradores", "generadores", "yield", "iterable"]

    def summary(self) -> str:
        return (
            "Comprende cómo recorrer datos en Python con iteradores y generadores, "
            "desde cero y con ejemplos claros de memoria y rendimiento."
        )

    def guide(self) -> str:
        return """
## ¿Qué es un iterable?
Un **iterable** es un objeto que puedes recorrer con un `for`. Por ejemplo: listas, tuplas, strings.
```
frutas = ["manzana", "pera", "uva"]  # Lista iterable
for fruta in frutas:  # Recorremos
    print(fruta)
```

## ¿Qué es un iterador?
Un **iterador** es el objeto que recuerda en qué posición va el recorrido.
Puedes obtenerlo con `iter()` y avanzar con `next()`.
```
colores = ["rojo", "azul"]  # Lista iterable
it = iter(colores)  # Creamos el iterador
print(next(it))  # Primer elemento
print(next(it))  # Segundo elemento
```

### ¿Por qué importa?
El iterador permite recorrer datos **uno a uno** sin cargar todo de golpe, lo que ahorra memoria.

## Generadores: iteradores fáciles de crear
Un **generador** es una función con `yield`. Devuelve valores de a uno y "pausa" su estado.
```
def contar_hasta(n):
    numero = 1
    while numero <= n:
        yield numero
        numero += 1
```

Cuando lo recorres, produce valores paso a paso:
```
for valor in contar_hasta(3):
    print(valor)
```

## Generadores con expresiones
También puedes crear generadores en una sola línea:
```
cuadrados = (n * n for n in range(5))
```

## Buenas prácticas y claridad
- **PEP8**: nombres en `snake_case`.
- **Evita magic numbers**: usa constantes o parámetros.
- **Código legible**: un generador con `yield` es más claro que construir listas enormes.
- **Documenta el propósito**: usa docstrings simples.

## Resumen de ejemplos
```
def pares(maximo):
    numero = 0
    while numero <= maximo:
        yield numero
        numero += 2
```
```
valores = (n for n in range(3))
for v in valores:
    print(v)
```
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Confundir iterable con iterador",
                "Un iterable crea iteradores; un iterador avanza con next().",
            ),
            (
                "Reutilizar iteradores agotados",
                "Un iterador se consume; vuelve a crear uno si necesitas otro recorrido.",
            ),
            (
                "Cargar todo en memoria",
                "Construir listas enormes cuando un generador sería más eficiente.",
            ),
            (
                "Olvidar StopIteration",
                "next() lanza StopIteration cuando no hay más elementos.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Iterador manual",
                """colores = ["rojo", "azul"]  # Iterable
it = iter(colores)  # Iterador
print(next(it))  # Primer valor
print(next(it))  # Segundo valor""",
            ),
            (
                "Generador con yield",
                """def contar_hasta(n):  # Definimos generador
    numero = 1  # Valor inicial
    while numero <= n:  # Condición
        yield numero  # Entregamos valor
        numero += 1  # Incremento
for valor in contar_hasta(3):  # Recorremos
    print(valor)  # Mostramos""",
            ),
            (
                "Expresión generadora",
                """cuadrados = (n * n for n in range(4))  # Generador
for valor in cuadrados:  # Recorremos
    print(valor)  # Mostramos""",
            ),
            (
                "Iterador con enumerate",
                """nombres = ["Ana", "Luis"]  # Lista
for indice, nombre in enumerate(nombres):  # Iteramos con índice
    print(indice, nombre)  # Mostramos""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea un generador que produzca números impares hasta 9.",
                "hints": ["Usa yield", "Incrementa de 2 en 2"],
                "solution": "def impares():\n    n = 1\n    while n <= 9:\n        yield n\n        n += 2",
            },
            {
                "question": "Convierte una lista en iterador y lee dos valores con next().",
                "hints": ["Usa iter()"],
                "solution": "valores = [10, 20, 30]\nit = iter(valores)\nprint(next(it))\nprint(next(it))",
            },
            {
                "question": "Crea una expresión generadora que produzca dobles de 0 a 4.",
                "hints": ["Usa (expresion for ...)"],
                "solution": "dobles = (n * 2 for n in range(5))",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Ejecuta los generadores en la pestaña de ejemplos."))
        return widget
