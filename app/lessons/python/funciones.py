from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class FuncionesLesson(Lesson):
    TITLE = "Funciones"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["funciones", "parametros", "retorno", "scope"]

    def summary(self) -> str:
        return (
            "Las funciones encapsulan lógica reutilizable. Aquí aprenderás a definirlas, "
            "pasar argumentos, devolver valores y aplicar buenas prácticas desde cero."
        )

    def guide(self) -> str:
        return """
## ¿Qué es una función?
Una **función** es un bloque de código con nombre que puedes reutilizar. Piensa en una receta: le das ingredientes (argumentos), hace pasos y devuelve un resultado.

### Partes básicas
- **def**: palabra clave para definir.
- **nombre**: identifica la función.
- **parámetros**: nombres que reciben datos.
- **return**: devuelve un resultado (si no hay return, devuelve `None`).

Ejemplo inmediato:
```
def saludar(nombre):  # nombre es un parámetro
    return f"Hola {nombre}"  # devolvemos un texto

mensaje = saludar("Ana")  # "Ana" es un argumento
```

## Parámetros vs argumentos (sin confusión)
- **Parámetro**: nombre dentro de la función (`nombre`).
- **Argumento**: valor que pasas al llamar (`"Ana"`).

## Scope (alcance) explicado simple
Las variables dentro de la función son **locales**. No afectan a las de afuera.
```
contador = 0  # Variable global

def sumar_uno():
    contador_local = contador + 1  # Usa la global, pero guarda en local
    return contador_local
```

## Valores por defecto
Si no pasas un argumento, se usa el default.
```
def potencia(base, exponente=2):
    return base ** exponente
```

### Advertencia sobre defaults mutables
Nunca uses listas o dicts como default.
```
def agregar(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    return lista
```

## *args y **kwargs sin miedo
- `*args`: captura varios argumentos posicionales.
- `**kwargs`: captura argumentos con nombre.
```
def resumen(*args, **kwargs):
    return args, kwargs
```

## Docstrings simples (documenta tu intención)
Una docstring es un texto que explica qué hace la función.
```
def promedio(valores):
    """Calcula el promedio de una lista de números."""
    return sum(valores) / len(valores)
```

## Type hints (gradual, sin abrumar)
Los hints no cambian la ejecución, pero ayudan a leer y detectar errores.
```
def area_cuadrado(lado: float) -> float:
    return lado * lado
```

## Buenas prácticas esenciales
- **PEP8**: `snake_case` para funciones, `PascalCase` para clases.
- **Indentación**: 4 espacios siempre.
- **Nombres claros**: `calcular_total` > `calc`.
- **Evita magic numbers**: usa constantes.
- **Código legible > trucos**: prioriza claridad.

## Resumen de ejemplos
```
def es_mayor(a, b):
    return a if a > b else b
```
```
def saludo(nombre, idioma="es"):
    return "Hola" if idioma == "es" else "Hello"
```
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Mutable como default",
                "`def f(x=[]):` comparte la misma lista en cada llamada.",
            ),
            (
                "Olvidar return",
                "Una función sin `return` devuelve None, lo que puede romper cálculos.",
            ),
            (
                "Orden de parámetros",
                "Parámetros con default deben ir después de los no default.",
            ),
            (
                "Confundir *args y **kwargs",
                "*args es tupla de posicionales; **kwargs es dict de nombrados.",
            ),
            (
                "Shadowing",
                "Si defines una variable igual que una función, pierdes la referencia.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Función básica",
                """def saludar(nombre):  # Definimos la función
    return f"Hola {nombre}"  # Retornamos saludo
print(saludar("Ana"))  # Llamamos a la función""",
            ),
            (
                "Valores por defecto",
                """def potencia(base, exponente=2):  # Default en exponente
    return base ** exponente  # Calculamos potencia
print(potencia(3))  # Usa default
print(potencia(3, 3))  # Usa 3""",
            ),
            (
                "*args y **kwargs",
                """def resumen(*args, **kwargs):  # Recibe varios datos
    return args, kwargs  # Devuelve ambos
print(resumen(1, 2, nombre="Luis"))  # Ejemplo""",
            ),
            (
                "Docstring",
                """def promedio(valores):  # Definimos función
    '''Calcula el promedio de números.'''  # Docstring
    return sum(valores) / len(valores)  # Calculamos
print(promedio([1, 2, 3]))  # Probamos""",
            ),
            (
                "Scope local",
                """x = 10  # Variable global
def mostrar():  # Función
    x = 5  # Variable local
    print(x)  # Imprime 5
mostrar()  # Ejecutamos
print(x)  # Imprime 10""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea una función que reciba una lista de números y devuelva el mayor.",
                "hints": ["Puedes usar max()", "Valida que la lista no esté vacía."],
                "solution": "def mayor(nums):\n    if not nums:\n        return None\n    return max(nums)",
            },
            {
                "question": "Escribe una función que acepte *args y devuelva la suma de pares.",
                "hints": ["Filtra con n % 2 == 0"],
                "solution": "def suma_pares(*nums):\n    return sum(n for n in nums if n % 2 == 0)",
            },
            {
                "question": "Crea una función que reciba nombre y apellido y devuelva 'Apellido, Nombre'.",
                "hints": ["Usa f-strings"],
                "solution": "def formato(nombre, apellido):\n    return f\"{apellido}, {nombre}\"",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Demo simple: prueba las funciones en los ejemplos."))
        return widget
