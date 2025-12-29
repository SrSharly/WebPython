from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class ContextManagersLesson(Lesson):
    TITLE = "Context managers"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Intermedio"
    TAGS = ["with", "context manager", "recursos", "archivos"]

    def summary(self) -> str:
        return (
            "Aprende a usar context managers para abrir y cerrar recursos de forma segura "
            "con la sentencia with, desde cero y con buenas prácticas."
        )

    def guide(self) -> str:
        return """
## ¿Qué problema resuelven?
Cuando abres un archivo o una conexión, debes **cerrarla**. Si olvidas, puedes perder datos o bloquear recursos.

Ejemplo del problema:
```
archivo = open("datos.txt", "w")
archivo.write("Hola")
archivo.close()
```
Si ocurre un error antes de `close()`, el archivo queda abierto.

## Solución: context managers (with)
La sentencia `with` garantiza que el recurso se cierre aunque haya errores.
```
with open("datos.txt", "w") as archivo:
    archivo.write("Hola")
```

### ¿Qué es un context manager?
Es un objeto que define cómo **entrar** y **salir** de un bloque. En términos simples: “abre y luego limpia”.

## Ejemplo paso a paso
1. Entramos al bloque (`__enter__`).
2. Trabajamos con el recurso.
3. Salimos y se limpia (`__exit__`).

Ejemplo simple:
```
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
```

## Context managers propios (concepto)
Puedes crear uno con una clase y los métodos `__enter__` y `__exit__`.
```
class Temporizador:
    def __enter__(self):
        print("Inicio")
        return self

    def __exit__(self, exc_type, exc, traceback):
        print("Fin")
```

## Buenas prácticas
- **PEP8**: `snake_case` para funciones/variables.
- **Indentación**: 4 espacios.
- **Claridad**: `with` es más legible que `try/finally` manual.
- **Evita magic numbers**: usa nombres para rutas o tiempos.

## Resumen de ejemplos
```
with open("log.txt", "a") as archivo:
    archivo.write("registro\n")
```
```
class Bloque:
    def __enter__(self):
        print("Entrando")
        return self

    def __exit__(self, exc_type, exc, traceback):
        print("Saliendo")
```
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Olvidar cerrar recursos",
                "Sin with, necesitas cerrar manualmente cada recurso.",
            ),
            (
                "Usar try sin finally",
                "Un error puede evitar el cierre si no hay finally.",
            ),
            (
                "Ignorar excepciones",
                "Los context managers pueden recibir y manejar errores en __exit__.",
            ),
            (
                "Anidar sin necesidad",
                "Si tienes varios recursos, puedes usar una sola línea with con comas.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "with con archivo",
                """with open("datos.txt", "w") as archivo:  # Abrimos archivo
    archivo.write("Hola")  # Escribimos
print("Listo")  # Fuera del bloque""",
            ),
            (
                "with con lectura",
                """with open("datos.txt", "r") as archivo:  # Abrimos en lectura
    contenido = archivo.read()  # Leemos contenido
print(contenido)  # Mostramos""",
            ),
            (
                "Context manager propio",
                """class Temporizador:  # Definimos clase
    def __enter__(self):  # Entramos
        print("Inicio")  # Mensaje
        return self  # Retornamos
    def __exit__(self, exc_type, exc, traceback):  # Salimos
        print("Fin")  # Mensaje
with Temporizador() as t:  # Usamos with
    print("Trabajando")  # Acción""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Abre un archivo en modo append y escribe una línea usando with.",
                "hints": ["Usa open(..., 'a')"],
                "solution": "with open('log.txt', 'a') as f:\n    f.write('nuevo\n')",
            },
            {
                "question": "Crea un context manager simple que imprima 'inicio' y 'fin'.",
                "hints": ["Implementa __enter__ y __exit__"],
                "solution": "class CM:\n    def __enter__(self):\n        print('inicio')\n        return self\n    def __exit__(self, exc_type, exc, traceback):\n        print('fin')",
            },
            {
                "question": "Lee un archivo con with y guarda el contenido en una variable.",
                "hints": ["Usa .read()"],
                "solution": "with open('datos.txt', 'r') as f:\n    contenido = f.read()",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Prueba los ejemplos con archivos de texto simples."))
        return widget
