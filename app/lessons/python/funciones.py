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
- Define funciones con `def nombre(params):`.
- Los parámetros pueden tener valores por defecto.
- Usa `*args` para argumentos posicionales variables.
- Usa `**kwargs` para argumentos nombrados variables.
- `return` finaliza la función y devuelve un valor.
- Una función sin return devuelve None.
- El scope local no afecta al global salvo `global`/`nonlocal`.
- Docstrings documentan el propósito y uso de la función.
- Mantén funciones pequeñas y con una sola responsabilidad.
- Considera type hints para mejorar legibilidad.
- Las funciones son objetos: se pueden pasar como parámetros.
- Las funciones lambda sirven para expresiones cortas.
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
                """def saludar(nombre):\n    return f"Hola {nombre}"\n\nprint(saludar("Ana"))""",
            ),
            (
                "Valores por defecto",
                """def potencia(base, exp=2):\n    return base ** exp\n\nprint(potencia(3))\nprint(potencia(3, 3))""",
            ),
            (
                "*args",
                """def suma(*nums):\n    return sum(nums)\n\nprint(suma(1, 2, 3))""",
            ),
            (
                "**kwargs",
                """def crear_usuario(**data):\n    return data\n\nprint(crear_usuario(nombre="Luis", rol="admin"))""",
            ),
            (
                "Funciones como argumentos",
                """def aplicar(x, fn):\n    return fn(x)\n\nprint(aplicar(5, lambda n: n * 2))""",
            ),
            (
                "Docstrings",
                """def promedio(valores):\n    """"Calcula el promedio de una lista de números.""""\n    return sum(valores) / len(valores)\n\nprint(promedio([1, 2, 3]))""",
            ),
            (
                "Scope local",
                """x = 10\n\ndef mostrar():\n    x = 5\n    print(x)\n\nmostrar()\nprint(x)""",
            ),
            (
                "Argumentos nombrados",
                """def saludo(nombre, idioma="es"):\n    return "Hola" if idioma == "es" else "Hello"\n\nprint(saludo(nombre="Marta"))""",
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
