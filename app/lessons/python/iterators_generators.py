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
            "Comprende desde cero qué es un iterable, cómo funcionan los iteradores, "
            "y cómo crear generadores eficientes con ejemplos claros."
        )

    def guide(self) -> str:
        return """
## ¿Qué es un iterable?
Un **iterable** es un objeto que se puede recorrer elemento por elemento. Ejemplos comunes:
una **lista**, una **tupla** o un texto.

Ejemplo inmediato:
```
frutas = ["manzana", "pera", "uva"]  # lista iterable
for fruta in frutas:  # recorremos elemento por elemento
    print(fruta)  # print muestra cada valor
```

## ¿Qué es un iterador?
Un **iterador** es el objeto que recuerda en qué posición va el recorrido. Lo obtienes con `iter()`
y avanzas con `next()`.
```
colores = ["rojo", "azul"]  # lista iterable
it = iter(colores)  # iter crea un iterador
print(next(it))  # primer elemento
print(next(it))  # segundo elemento
```

## Conceptos previos (sin asumir nada)
- **objeto**: dato con estado y comportamiento.
- **método**: función asociada a un objeto (por ejemplo, `append`).
- **variable**: nombre que apunta a un valor.
- **función**: bloque reutilizable de código.
- **len**: función que devuelve la longitud de una colección.

### Buenas prácticas (CalloutBox: best_practice)
- Usa nombres en **snake_case**.
- Prefiere `for` para recorrer: es más legible que `next()` manual.
- Si necesitas memoria eficiente, usa generadores.

## Paso 1: Iterables + len()
`len()` cuenta cuántos elementos hay en una colección.
```
valores = [10, 20, 30]  # lista con 3 elementos
cantidad = len(valores)  # len cuenta elementos
print(cantidad)  # muestra 3
```

## Paso 2: Iterador con control manual
Si necesitas control paso a paso, usa `iter()` y `next()`.
```
letras = ["a", "b", "c"]  # lista iterable
it = iter(letras)  # iterador
print(next(it))  # a
print(next(it))  # b
```

## Paso 3: Generadores (yield)
Un **generador** es una función que produce valores de a uno con `yield`.
```
def contar_hasta(n):  # función generadora
    numero = 1  # variable inicial
    while numero <= n:  # condición
        yield numero  # entregamos un valor
        numero += 1  # actualizamos
```

## Paso 4: Recorrer un generador
Cuando lo usas en un `for`, el generador produce valores sin cargar todo en memoria.
```
for valor in contar_hasta(3):  # recorremos el generador
    print(valor)  # muestra 1, 2, 3
```

## Paso 5: Expresiones generadoras
Puedes crear un generador en una sola línea.
```
cuadrados = (n * n for n in range(5))  # generador
for valor in cuadrados:  # recorremos
    print(valor)  # muestra 0, 1, 4, 9, 16
```

## Paso 6: Enumerar con índice
`enumerate` añade índices al recorrido sin hacer listas extra.
```
nombres = ["Ana", "Luis"]  # lista de nombres
for indice, nombre in enumerate(nombres):  # iteramos con índice
    print(indice, nombre)  # mostramos índice y nombre
```

## Paso 7: Iteradores agotados
Un iterador se consume. Si necesitas recorrer otra vez, crea uno nuevo.
```
valores = [1, 2]  # lista
it = iter(valores)  # primer iterador
print(next(it))  # 1
print(next(it))  # 2
it = iter(valores)  # nuevo iterador
print(next(it))  # 1
```

## Más allá (nivel pro)
### Pro: Generadores para archivos grandes
```
def leer_lineas(ruta):  # función generadora
    with open(ruta, "r") as archivo:  # abrimos archivo
        for linea in archivo:  # iteramos línea por línea
            yield linea.strip()  # entregamos sin salto
```
**Warning real:** si conviertes el generador a lista con `list()`, pierdes la ventaja de memoria.

### Pro: StopIteration y control manual
```
valores = [1, 2]  # lista
it = iter(valores)  # iterador
try:
    while True:  # bucle infinito
        print(next(it))  # next avanza
except StopIteration:  # fin del iterador
    print("Fin del recorrido")  # mensaje final
```
**Warning real:** usar `next()` sin manejo puede lanzar StopIteration y detener tu programa.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Confundir iterable con iterador",
                "Solución: un iterable crea iteradores; un iterador se avanza con next().",
            ),
            (
                "Reutilizar un iterador agotado",
                "Solución: crea un nuevo iterador con iter() antes de recorrer otra vez.",
            ),
            (
                "Convertir generadores a listas sin necesidad",
                "Solución: recorre el generador directamente para ahorrar memoria.",
            ),
            (
                "Olvidar StopIteration",
                "Solución: usa for o maneja StopIteration si usas next().",
            ),
            (
                "Usar nombres poco claros",
                "Solución: usa snake_case y nombres descriptivos como iterador_nombres.",
            ),
            (
                "Pensar que yield devuelve todo",
                "Solución: yield entrega valores uno a uno, no una lista completa.",
            ),
            (
                "Modificar la lista mientras se itera",
                "Solución: crea una copia o acumula cambios en otra lista.",
            ),
            (
                "No documentar generadores",
                "Solución: agrega docstrings que expliquen qué produce el generador.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Iterador manual",
                """colores = ["rojo", "azul"]  # lista iterable
it = iter(colores)  # iterador
print(next(it))  # primer valor
print(next(it))  # segundo valor""",
            ),
            (
                "Generador con yield",
                """def contar_hasta(n):  # generador
    numero = 1  # valor inicial
    while numero <= n:  # condición
        yield numero  # entregamos valor
        numero += 1  # incremento
for valor in contar_hasta(3):  # recorremos
    print(valor)  # mostramos""",
            ),
            (
                "Expresión generadora",
                """cuadrados = (n * n for n in range(4))  # generador
for valor in cuadrados:  # recorremos
    print(valor)  # mostramos""",
            ),
            (
                "Enumerate con índice",
                """nombres = ["Ana", "Luis"]  # lista
for indice, nombre in enumerate(nombres):  # índice + valor
    print(indice, nombre)  # mostramos""",
            ),
            (
                "Iterador reiniciado",
                """valores = [1, 2]  # lista
it = iter(valores)  # iterador
print(next(it))  # 1
print(next(it))  # 2
it = iter(valores)  # nuevo iterador
print(next(it))  # 1""",
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
            {
                "question": "Crea un generador que lea líneas de un archivo (simulado).",
                "hints": ["Usa yield dentro de un for"],
                "solution": (
                    "def leer_lineas(lineas):\n"
                    "    for linea in lineas:\n"
                    "        yield linea.strip()"
                ),
            },
            {
                "question": "Usa enumerate para imprimir índice y valor de una lista.",
                "hints": ["Usa enumerate(lista)"],
                "solution": "nombres = ['Ana', 'Luis']\nfor i, nombre in enumerate(nombres):\n    print(i, nombre)",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Ejecuta los generadores en la pestaña de ejemplos."))
        return widget
