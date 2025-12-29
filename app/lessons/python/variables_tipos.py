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
## Qué es
Una variable en Python es un nombre que apunta a un objeto. El tipo pertenece al objeto, no al nombre.

## Cuándo se usa
Cada vez que guardas datos para reutilizarlos: números, textos, listas, resultados de cálculos, etc.

## Conceptos previos
- Saber qué es un objeto (algo que existe en memoria).
- Entender que Python es de tipado dinámico.

## Paso 1: Crear y reasignar variables
Puedes crear una variable simplemente asignando un valor.
```
nombre = "Ana"
```
Luego puedes reasignar a otro tipo sin problema.
```
nombre = 3.14
```

## Paso 2: Tipos básicos y cómo identificarlos
Tipos comunes: int, float, str, bool, list, tuple, dict, set.
```
edad = 30
print(type(edad))
```

## Paso 3: Mutabilidad (qué cambia y qué no)
Las listas y diccionarios se pueden modificar en el lugar (mutables). Las cadenas y tuplas no.
```
nums = [1, 2]
nums.append(3)
```

## Paso 4: Conversiones explícitas
Es mejor convertir de forma explícita para evitar errores inesperados.
```
texto = "42"
numero = int(texto)
```

## Paso 5: None como ausencia de valor
None significa “no hay valor todavía”.
```
resultado = None
if resultado is None:
    print("Falta calcular")
```

## Mini-reto
Mini-reto 1: Crea una variable con tu edad, conviértela a string y forma una frase.
Solución:
```
edad = 28
frase = "Tengo " + str(edad) + " años"
```

## Errores típicos (mal vs bien)
Mal: mezclar tipos sin convertir.
```
"3" + 4
```
Bien: convertir antes de operar.
```
"3" + str(4)
```

## Nota
Nota: usa nombres descriptivos (por ejemplo, total_ventas) para que tu código sea legible.

## Advertencia
Advertencia: no uses nombres como list o str porque sobrescribes funciones útiles.

## Checklist final
- Sé qué es una variable y qué es un objeto.
- Identifico tipos básicos con type().
- Distingo tipos mutables e inmutables.
- Convierto tipos de forma explícita.
- Uso None para ausencia de valor.

## Ver también
- Funciones
- Excepciones
- Iteradores y generadores
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Confundir alias con copia",
                "Asignar b = a en listas no copia, solo crea un alias. Usa list(a) o a.copy().",
            ),
            (
                "Mezclar tipos en operaciones",
                '"3" + 4 produce error: str e int no se concatenan sin conversión.',
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
                """x = 10  # Creamos un entero
x = "texto"  # Reasignamos a un string
print(x)  # Mostramos el valor actual""",
            ),
            (
                "Mutabilidad",
                """nums = [1, 2, 3]  # Lista mutable
alias = nums  # Creamos un alias
alias.append(4)  # Modificamos desde el alias
print(nums)  # La lista original cambia""",
            ),
            (
                "Copias seguras",
                """original = [1, 2, 3]  # Lista original
copia = original.copy()  # Copiamos la lista
copia.append(99)  # Modificamos la copia
print(original, copia)  # Original y copia son distintas""",
            ),
            (
                "Anotaciones de tipo",
                """from typing import List  # Importamos List
values: List[int] = [1, 2, 3]  # Anotamos el tipo
print(values)  # Mostramos la lista""",
            ),
            (
                "Uso de None",
                """value = None  # Indicamos ausencia de valor
if value is None:  # Comparamos con is
    print("Sin valor")  # Mostramos mensaje""",
            ),
            (
                "Conversión explícita",
                """num = int("42")  # Convertimos a entero
print(num + 1)  # Sumamos un valor""",
            ),
            (
                "Tupla de un elemento",
                """solo = (1,)  # Creamos una tupla de un elemento
print(type(solo))  # Mostramos el tipo""",
            ),
            (
                "Booleanos y truthy",
                """items = []  # Lista vacía
if not items:  # Evaluación truthy
    print("Lista vacía")  # Informamos""",
            ),
            (
                "Comparación robusta",
                """name = "Python"  # Cadena original
print(name.casefold() == "python")  # Comparamos sin mayúsculas""",
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
