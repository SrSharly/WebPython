from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class ExcepcionesLesson(Lesson):
    TITLE = "Excepciones"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Intermedio"
    TAGS = ["errores", "try/except", "raise", "finally"]

    def summary(self) -> str:
        return (
            "Aprende a manejar errores de forma controlada: desde fallos normales, "
            "hasta try/except, finally, else y excepciones personalizadas."
        )

    def guide(self) -> str:
        return """
## Errores normales: por qué pasan
Un programa falla cuando ocurre algo inesperado: dividir por cero, abrir un archivo inexistente, convertir texto a número.
Eso es normal. Las **excepciones** son la forma de Python de avisarte.

Ejemplo simple:
```
numero = int("hola")  # Esto lanza ValueError
```

## try/except: manejar lo esperable
Usa `try` para el código que puede fallar y `except` para reaccionar.
```
try:
    edad = int("20")
except ValueError:
    print("No es un número")
```

## else y finally (control fino)
- **else** se ejecuta si no hubo error.
- **finally** siempre se ejecuta (ideal para cerrar recursos).
```
try:
    valor = 10 / 2
except ZeroDivisionError:
    print("No dividir por cero")
else:
    print("Resultado", valor)
finally:
    print("Cerrar recursos")
```

## Lanzar errores propios (raise)
Si detectas un dato inválido, puedes lanzar una excepción.
```
def validar_edad(edad):
    if edad < 0:
        raise ValueError("Edad inválida")
```

## Excepciones personalizadas
Sirven para errores específicos de tu aplicación.
```
class DatosInvalidosError(Exception):
    pass
```

## Buenas prácticas expertas
- **PEP8**: `snake_case` y 4 espacios.
- **Errores específicos**: evita `except Exception` si puedes.
- **No uses excepciones como flujo normal**.
- **Claridad > trucos**: un try pequeño es más legible.
- **Docstrings** en funciones que lanzan errores.

## Resumen de ejemplos
```
try:
    print(1 / 0)
except ZeroDivisionError as error:
    print("Error", error)
```
```
class ConfigError(Exception):
    pass
```
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Capturar Exception",
                "Oculta errores reales; captura tipos específicos.",
            ),
            (
                "except vacío",
                "Silencia fallos y complica el debugging.",
            ),
            (
                "No liberar recursos",
                "Siempre usa finally o context managers para cerrar archivos.",
            ),
            (
                "Raise sin contexto",
                "`raise nuevo_error` sin `from exc` pierde información útil.",
            ),
            (
                "Confundir errores y estados",
                "No uses excepciones para flujo normal.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Try/except básico",
                """try:  # Bloque protegido
    valor = int("10")  # Convertimos
    print(valor)  # Mostramos
except ValueError as exc:  # Error específico
    print("Error:", exc)  # Mensaje""",
            ),
            (
                "Try/except/else",
                """try:  # Bloque protegido
    resultado = 10 / 2  # División
except ZeroDivisionError:  # Error
    print("No dividir por cero")  # Mensaje
else:  # Sin error
    print("Resultado:", resultado)  # Mostramos""",
            ),
            (
                "Finally",
                """try:  # Bloque protegido
    archivo = open("datos.txt", "w")  # Abrimos
    archivo.write("Hola")  # Escribimos
finally:  # Siempre se ejecuta
    archivo.close()  # Cerramos""",
            ),
            (
                "Raise personalizado",
                """def validar(edad):  # Función
    if edad < 0:  # Validamos
        raise ValueError("Edad inválida")  # Lanzamos
validar(5)  # Llamamos""",
            ),
            (
                "Excepción custom",
                """class ConfigError(Exception):  # Clase error
    pass  # Sin lógica extra
raise ConfigError("Falta API_KEY")  # Lanzamos""",
            ),
            (
                "Encadenar errores",
                """try:  # Intentamos
    int("abc")  # Forzamos ValueError
except ValueError as exc:  # Capturamos
    raise RuntimeError("Entrada no válida") from exc  # Encadenamos""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea una función que divida dos números y maneje ZeroDivisionError.",
                "hints": ["Devuelve None si hay error"],
                "solution": "def dividir(a, b):\n    try:\n        return a / b\n    except ZeroDivisionError:\n        return None",
            },
            {
                "question": "Define una excepción personalizada llamada DataError.",
                "hints": ["Hereda de Exception"],
                "solution": "class DataError(Exception):\n    pass",
            },
            {
                "question": "Usa finally para cerrar un recurso simulado.",
                "hints": ["Usa un try con print()"],
                "solution": "try:\n    print('abriendo')\nfinally:\n    print('cerrando')",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Explora los bloques try/except en los ejemplos."))
        return widget
