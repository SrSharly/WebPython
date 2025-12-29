from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class BuclesLesson(Lesson):
    TITLE = "Bucles"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["for", "while", "loops", "range"]

    def summary(self) -> str:
        return (
            "Aprende a repetir tareas con bucles for y while, "
            "con ejemplos claros y buenas prácticas de control."
        )

    def guide(self) -> str:
        return """
## ¿Qué es un bucle?
Un **bucle** repite un bloque de código varias veces. Es útil para listas, conteos o procesos repetitivos.

## Bucle for (recorrer iterables)
```
frutas = ["manzana", "pera", "uva"]
for fruta in frutas:
    print(fruta)
```

## range para contar
```
for numero in range(3):
    print(numero)
```

## Bucle while (mientras se cumpla una condición)
```
contador = 0
while contador < 3:
    print(contador)
    contador += 1
```

## break y continue
- **break** sale del bucle.
- **continue** salta al siguiente ciclo.
```
for numero in range(5):
    if numero == 3:
        break
    print(numero)
```

## Buenas prácticas
- **PEP8**: 4 espacios de indentación.
- **Evita bucles infinitos**: actualiza la condición.
- **Claridad**: usa nombres como `contador`, `indice`.
- **No abuses de break**: intenta condiciones claras.

## Resumen de ejemplos
```
for letra in "hola":
    print(letra)
```
```
contador = 1
while contador <= 3:
    print(contador)
    contador += 1
```
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Bucle infinito",
                "Si no actualizas la condición en while, nunca termina.",
            ),
            (
                "Off-by-one",
                "range(3) produce 0,1,2. Ajusta el límite según necesites.",
            ),
            (
                "Modificar lista mientras iteras",
                "Puede saltarse elementos; crea una copia o usa índices.",
            ),
            (
                "Usar while cuando for es suficiente",
                "for es más legible para iterables.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "for con lista",
                """frutas = ["manzana", "pera"]  # Lista
for fruta in frutas:  # Bucle
    print(fruta)  # Mostramos""",
            ),
            (
                "for con range",
                """for numero in range(3):  # 0,1,2
    print(numero)  # Mostramos""",
            ),
            (
                "while",
                """contador = 0  # Inicio
while contador < 3:  # Condición
    print(contador)  # Mostramos
    contador += 1  # Incremento""",
            ),
            (
                "break",
                """for numero in range(5):  # Recorremos
    if numero == 3:  # Condición
        break  # Salimos
    print(numero)  # Mostramos""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Imprime los números del 1 al 5 usando for.",
                "hints": ["Usa range(1, 6)"],
                "solution": "for n in range(1, 6):\n    print(n)",
            },
            {
                "question": "Crea un while que sume números hasta llegar a 10.",
                "hints": ["Usa un acumulador"],
                "solution": "total = 0\nnumero = 1\nwhile total < 10:\n    total += numero\n    numero += 1",
            },
            {
                "question": "Recorre una lista y muestra solo elementos mayores a 5.",
                "hints": ["Usa if dentro del for"],
                "solution": "valores = [2, 6, 9]\nfor v in valores:\n    if v > 5:\n        print(v)",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Practica bucles simples en los ejemplos."))
        return widget
