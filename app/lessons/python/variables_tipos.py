from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class VariablesTiposLesson(Lesson):
    TITLE = "Variables y tipos"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["variables", "tipos", "mutabilidad", "tipado-dinámico"]

    def summary(self) -> str:
        return (
            "Aprende cómo Python maneja variables, tipos y mutabilidad. "
            "Esta lección cubre tipado dinámico, anotaciones, coerción y mejores "
            "prácticas para escribir código claro y seguro."
        )

    def guide(self) -> str:
        return """
- En Python, una variable es un nombre que referencia un objeto.
- El tipado es dinámico: el tipo está en el objeto, no en el nombre.
- Puedes reasignar una variable a un objeto de otro tipo.
- Los tipos básicos: int, float, str, bool, list, tuple, dict, set.
- Algunos tipos son mutables (list, dict, set) y otros inmutables (int, str, tuple).
- La mutabilidad impacta en el comportamiento al pasar valores a funciones.
- Usa isinstance(obj, Tipo) para validar tipos sin romper polimorfismo.
- Las anotaciones de tipo ayudan a documentación y herramientas estáticas.
- Las conversiones explícitas (int(), str()) son más seguras que la implícita.
- None representa la ausencia de valor, no es "0" ni "".
- Evita nombres ambiguos como data o temp si puedes ser específico.
- Usa constantes en MAYÚSCULAS para valores de configuración.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Confundir alias con copia",
                "Asignar b = a en listas no copia, solo crea un alias. Usa list(a) o a.copy().",
            ),
            (
                "Mezclar tipos en operaciones",
                """"3" + 4 produce error: str e int no se concatenan sin conversión.""",
            ),
            (
                "Mutabilidad en argumentos",
                "Listas o dicts mutables como valores por defecto en funciones se comparten.",
            ),
            (
                "Comparar con == en lugar de is",
                "Para comparar con None usa `is None`, no `== None`.",
            ),
            (
                "Shadowing de builtins",
                "Nombrar variables como list, dict o str sobrescribe funciones útiles.",
            ),
            (
                "Olvidar el orden de evaluación",
                "En expresiones complejas, paréntesis aclaran y evitan errores.",
            ),
            (
                "Asumir precisión exacta en float",
                "Los floats tienen errores de redondeo; usa round o decimal si es crítico.",
            ),
            (
                "Confundir tuplas de un elemento",
                "(1) es int; (1,) es tupla. La coma es clave.",
            ),
            (
                "Comparación de cadenas con mayúsculas",
                "Usa .lower()/.casefold() para comparar sin sensibilidad a mayúsculas.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Asignación y reasignación",
                """x = 10\nx = "texto"\nprint(x)""",
            ),
            (
                "Mutabilidad",
                """nums = [1, 2, 3]\nalias = nums\nalias.append(4)\nprint(nums)""",
            ),
            (
                "Copias seguras",
                """original = [1, 2, 3]\ncopia = original.copy()\ncopia.append(99)\nprint(original, copia)""",
            ),
            (
                "Anotaciones de tipo",
                """from typing import List\nvalues: List[int] = [1, 2, 3]\nprint(values)""",
            ),
            (
                "Uso de None",
                """value = None\nif value is None:\n    print("Sin valor")""",
            ),
            (
                "Conversión explícita",
                """num = int("42")\nprint(num + 1)""",
            ),
            (
                "Tupla de un elemento",
                """solo = (1,)\nprint(type(solo))""",
            ),
            (
                "Booleanos y truthy",
                """items = []\nif not items:\n    print("Lista vacía")""",
            ),
            (
                "Comparación robusta",
                """name = "Python"\nprint(name.casefold() == "python")""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Explica la diferencia entre una copia superficial y un alias.",
                "hints": ["Piensa en listas", "¿Qué pasa si modificas uno?"],
                "solution": "Un alias apunta al mismo objeto; una copia crea un objeto distinto.",
            },
            {
                "question": "Crea una tupla con un solo elemento 'python'.",
                "hints": ["La coma es obligatoria"],
                "solution": "tupla = (" + '"python"' + ",)",
            },
            {
                "question": "Convierte la cadena '3.14' en float y súmale 1.",
                "hints": ["Usa float()"],
                "solution": "valor = float('3.14')\nprint(valor + 1)",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Esta lección es conceptual y no requiere demo interactiva."))
        return widget
