from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class StringsFStringsLesson(Lesson):
    TITLE = "Strings y f-strings"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["strings", "texto", "f-strings", "format"]

    def summary(self) -> str:
        return (
            "Aprende a trabajar con texto en Python: crear strings, unirlos, "
            "usar f-strings y aplicar buenas prácticas de legibilidad."
        )

    def guide(self) -> str:
        return """
## ¿Qué es un string?
Un **string** (cadena) es texto. Puedes usar comillas simples o dobles.
```
mensaje = "Hola"  # String
```

## Concatenación y repetición
Puedes unir strings con `+` y repetir con `*`.
```
nombre = "Ana"
saludo = "Hola, " + nombre
```

## f-strings: la forma moderna y clara
Con f-strings puedes insertar valores dentro del texto.
```
nombre = "Luis"
edad = 25
mensaje = f"{nombre} tiene {edad} años"
```

## Escapar caracteres especiales
Usa `\n` para salto de línea y `\t` para tabulación.
```
texto = "Línea 1\nLínea 2"
```

## Métodos útiles
- `.lower()` / `.upper()` para mayúsculas/minúsculas
- `.strip()` para quitar espacios
- `.replace()` para reemplazar texto

Ejemplo inmediato:
```
frase = "  Hola Mundo  "
limpia = frase.strip().lower()
```

## Buenas prácticas
- **PEP8**: nombres en `snake_case`.
- **Claridad**: f-strings son más legibles que concatenar muchas partes.
- **Evita magic numbers**: si repites texto, usa variables.

## Resumen de ejemplos
```
producto = "café"
precio = 2.5
mensaje = f"{producto} cuesta {precio}€"
```
```
texto = "hola"
mayus = texto.upper()
```
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Olvidar convertir a str",
                "No puedes concatenar string con int sin convertir.",
            ),
            (
                "Confundir comillas",
                "Si tu texto tiene comillas, escápalas o alterna simples/dobles.",
            ),
            (
                "No usar strip",
                "Espacios extra pueden romper comparaciones de texto.",
            ),
            (
                "Usar + en grandes textos",
                "Para muchas piezas, f-strings o join son más claros.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Concatenación",
                """nombre = "Ana"  # Nombre
saludo = "Hola, " + nombre  # Unimos texto
print(saludo)  # Mostramos""",
            ),
            (
                "f-strings",
                """producto = "café"  # Producto
precio = 2.5  # Precio
mensaje = f"{producto} cuesta {precio}€"  # f-string
print(mensaje)  # Mostramos""",
            ),
            (
                "Métodos básicos",
                """texto = "  Hola  "  # Texto con espacios
limpio = texto.strip()  # Quitamos espacios
mayus = limpio.upper()  # Mayúsculas
print(mayus)  # Mostramos""",
            ),
            (
                "Reemplazo",
                """frase = "Python es fácil"  # Texto
nueva = frase.replace("fácil", "genial")  # Reemplazo
print(nueva)  # Mostramos""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea un saludo que use f-strings con nombre y ciudad.",
                "hints": ["Usa f\"...\""],
                "solution": "nombre = 'Ana'\nciudad = 'Madrid'\nsaludo = f'Hola {nombre} desde {ciudad}'",
            },
            {
                "question": "Convierte un texto a minúsculas y quita espacios a los lados.",
                "hints": ["Usa strip() y lower()"],
                "solution": "texto = '  Hola  '\nlimpio = texto.strip().lower()",
            },
            {
                "question": "Reemplaza la palabra 'malo' por 'bueno' en una frase.",
                "hints": ["Usa replace()"],
                "solution": "frase = 'Esto es malo'\nmejor = frase.replace('malo', 'bueno')",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Juega con strings en los ejemplos rápidos."))
        return widget
