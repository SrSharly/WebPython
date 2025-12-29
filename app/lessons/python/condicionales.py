from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class CondicionalesLesson(Lesson):
    TITLE = "Condicionales"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["if", "elif", "else", "condiciones"]

    def summary(self) -> str:
        return (
            "Aprende a tomar decisiones en Python usando if/elif/else, "
            "con ejemplos claros y buenas prácticas desde cero."
        )

    def guide(self) -> str:
        return """
## ¿Para qué sirven los condicionales?
Un programa necesita decidir. Un **condicional** ejecuta un bloque si se cumple una condición.

## if: la decisión más simple
```
edad = 20
if edad >= 18:
    print("Eres mayor")
```

## else: el caso contrario
```
if edad >= 18:
    print("Eres mayor")
else:
    print("Eres menor")
```

## elif: varias opciones
```
nota = 7
if nota >= 9:
    print("Excelente")
elif nota >= 6:
    print("Aprobado")
else:
    print("Reprobado")
```

## Comparaciones y lógica
Puedes combinar condiciones con `and`, `or`, `not`.
```
usuario_activo = True
es_admin = False
if usuario_activo and es_admin:
    print("Acceso total")
```

## Buenas prácticas
- **PEP8**: sangría de 4 espacios.
- **Claridad**: condiciones cortas y legibles.
- **Evita anidar mucho**: usa elif para simplificar.
- **Nombres claros**: `es_mayor` es mejor que `em`.

## Resumen de ejemplos
```
clima = "lluvia"
if clima == "lluvia":
    print("Lleva paraguas")
```
```
valor = 5
mensaje = "alto" if valor > 3 else "bajo"
```
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Olvidar los dos puntos",
                "Las líneas if/elif/else terminan con ':'.",
            ),
            (
                "Indentación incorrecta",
                "Python usa la indentación para agrupar bloques.",
            ),
            (
                "Comparar strings con mayúsculas",
                "Normaliza con lower() antes de comparar.",
            ),
            (
                "Condiciones demasiado largas",
                "Divide o usa variables intermedias para claridad.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "if/else básico",
                """edad = 20  # Edad
if edad >= 18:  # Condición
    print("Mayor")  # Bloque verdadero
else:  # Caso contrario
    print("Menor")  # Bloque falso""",
            ),
            (
                "elif",
                """nota = 7  # Nota
if nota >= 9:  # Primer caso
    print("Excelente")  # Mensaje
elif nota >= 6:  # Segundo caso
    print("Aprobado")  # Mensaje
else:  # Último caso
    print("Reprobado")  # Mensaje""",
            ),
            (
                "Condición compuesta",
                """activo = True  # Estado
es_admin = False  # Rol
if activo and es_admin:  # Condición
    print("Acceso total")  # Mensaje
else:  # Caso contrario
    print("Acceso limitado")  # Mensaje""",
            ),
            (
                "Operador ternario",
                """valor = 5  # Valor
mensaje = "alto" if valor > 3 else "bajo"  # Ternario
print(mensaje)  # Mostramos""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea un condicional que imprima si un número es positivo, negativo o cero.",
                "hints": ["Usa if/elif/else"],
                "solution": "numero = 0\nif numero > 0:\n    print('positivo')\nelif numero < 0:\n    print('negativo')\nelse:\n    print('cero')",
            },
            {
                "question": "Decide si un usuario puede entrar: activo y con suscripción.",
                "hints": ["Usa and"],
                "solution": "activo = True\nsuscripcion = True\npuede_entrar = activo and suscripcion",
            },
            {
                "question": "Normaliza un texto y compara si es 'si'.",
                "hints": ["Usa lower()"],
                "solution": "respuesta = 'Si'\nif respuesta.lower() == 'si':\n    print('confirmado')",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Prueba decisiones simples en los ejemplos."))
        return widget
