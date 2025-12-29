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
            "pasar argumentos, devolver valores y aplicar buenas prácticas de diseño."
        )

    def guide(self) -> str:
        return """
## Qué es
Una función es un bloque de código con nombre que ejecuta una tarea y puede devolver un resultado.

## Cuándo se usa
Cuando quieres reutilizar lógica, evitar repetición y dar claridad a tu programa.

## Conceptos previos
- Variables y tipos básicos.
- Indentación (sangría) en Python.

## Paso 1: Definir una función simple
```
def saludar(nombre):
    return f"Hola {nombre}"
```

## Paso 2: Llamar a la función
```
mensaje = saludar("Ana")
print(mensaje)
```

## Paso 3: Parámetros y valores por defecto
```
def potencia(base, exp=2):
    return base ** exp
```

## Paso 4: Argumentos variables
- *args recibe varios posicionales.
- **kwargs recibe varios nombrados.
```
def resumen(*args, **kwargs):
    return args, kwargs
```

## Paso 5: Alcance (scope)
Las variables dentro de la función son locales y no afectan al exterior.
```
contador = 0

def contar():
    contador_local = contador + 1
    return contador_local
```

## Mini-reto
Mini-reto 1: Crea una función que reciba dos números y devuelva el mayor.
Solución:
```
def mayor(a, b):
    return a if a > b else b
```

## Errores típicos (mal vs bien)
Mal: usar lista mutable como valor por defecto.
```
def agregar(item, lista=[]):
    lista.append(item)
    return lista
```
Bien: usar None y crear la lista dentro.
```
def agregar(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    return lista
```

## Nota
Nota: documenta con docstrings para que otros entiendan la función.

## Advertencia
Advertencia: evita funciones enormes; divide en funciones pequeñas.

## Checklist final
- Sé definir y llamar funciones.
- Uso parámetros con y sin default.
- Distingo *args y **kwargs.
- Comprendo el scope local.
- Documento mis funciones.

## Ver también
- Variables y tipos
- Excepciones
- Iteradores y generadores
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
            (
                "No validar entrada",
                "Agregar validaciones evita errores silenciosos en usos futuros.",
            ),
            (
                "Uso excesivo de lambda",
                "Si es compleja, usa def con nombre.",
            ),
            (
                "Modificar argumentos",
                "Alterar listas recibidas puede afectar al llamador.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Función básica",
                """def saludar(nombre):  # Definimos la función
    return f"Hola {nombre}"  # Retornamos un saludo
print(saludar("Ana"))  # Llamamos a la función""",
            ),
            (
                "Valores por defecto",
                """def potencia(base, exp=2):  # Exp tiene valor por defecto
    return base ** exp  # Calculamos la potencia
print(potencia(3))  # Usa exp=2
print(potencia(3, 3))  # Usa exp=3""",
            ),
            (
                "*args",
                """def suma(*nums):  # Recibe varios números
    return sum(nums)  # Sumamos todos
print(suma(1, 2, 3))  # Probamos la función""",
            ),
            (
                "**kwargs",
                """def crear_usuario(**data):  # Recibe pares clave-valor
    return data  # Retorna el dict
print(crear_usuario(nombre="Luis", rol="admin"))  # Ejemplo""",
            ),
            (
                "Funciones como argumentos",
                """def aplicar(x, fn):  # Recibe un valor y una función
    return fn(x)  # Aplica la función
print(aplicar(5, lambda n: n * 2))  # Usamos lambda""",
            ),
            (
                "Docstrings",
                """def promedio(valores):  # Definimos la función
    '''Calcula el promedio de una lista de números.'''  # Docstring
    return sum(valores) / len(valores)  # Retornamos el promedio
print(promedio([1, 2, 3]))  # Probamos la función""",
            ),
            (
                "Scope local",
                """x = 10  # Variable global
def mostrar():  # Definimos la función
    x = 5  # Variable local
    print(x)  # Imprime 5
mostrar()  # Ejecutamos la función
print(x)  # Imprime 10""",
            ),
            (
                "Argumentos nombrados",
                """def saludo(nombre, idioma="es"):  # Idioma por defecto
    return "Hola" if idioma == "es" else "Hello"  # Selección de saludo
print(saludo(nombre="Marta"))  # Llamada con nombre""",
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
