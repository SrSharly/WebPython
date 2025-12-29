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
            "Maneja errores de forma controlada usando excepciones. "
            "Aprenderás a capturar, lanzar y estructurar errores para construir "
            "aplicaciones resilientes."
        )

    def guide(self) -> str:
        return """
## Qué es
Una excepción es un evento que interrumpe el flujo normal del programa cuando ocurre un error.

## Cuándo se usa
Cuando necesitas controlar fallos esperables (por ejemplo, leer un archivo que puede no existir).

## Conceptos previos
- Funciones básicas y flujo de control.
- Diferencia entre error esperado y bug.

## Paso 1: Capturar errores concretos
```
try:
    edad = int("20")
except ValueError:
    print("No es un número")
```

## Paso 2: Usar else y finally
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

## Paso 3: Lanzar tus propias excepciones
```
def validar(edad):
    if edad < 0:
        raise ValueError("Edad inválida")
```

## Paso 4: Crear excepciones personalizadas
```
class DataError(Exception):
    pass
```

## Mini-reto
Mini-reto 1: Implementa una función que convierta texto a int y devuelva None si falla.
Solución:
```
def convertir(texto):
    try:
        return int(texto)
    except ValueError:
        return None
```

## Errores típicos (mal vs bien)
Mal: capturar Exception y ocultar el error.
```
try:
    1 / 0
except Exception:
    pass
```
Bien: capturar el error específico y registrar.
```
try:
    1 / 0
except ZeroDivisionError as exc:
    print("Error", exc)
```

## Nota
Nota: usa logging si necesitas guardar detalles para depuración.

## Advertencia
Advertencia: un except vacío puede esconder errores graves.

## Checklist final
- Capturo errores específicos.
- Uso else y finally correctamente.
- Sé lanzar y crear excepciones.
- No oculto errores sin registrar.

## Ver también
- Context managers
- Funciones
- Variables y tipos
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
            (
                "Capturar demasiadas líneas",
                "Un try grande es difícil de leer y de depurar.",
            ),
            (
                "Usar assert en producción",
                "Los asserts se desactivan con -O.",
            ),
            (
                "Ignorar stacktrace",
                "Registra el error antes de manejarlo o re-lanzarlo.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Try/except básico",
                """try:  # Iniciamos el bloque try
    valor = int("10")  # Convertimos a entero
    print(valor)  # Mostramos el valor
except ValueError as exc:  # Capturamos error específico
    print("Error:", exc)  # Informamos del error""",
            ),
            (
                "Try/except/else",
                """try:  # Iniciamos el bloque try
    resultado = 10 / 2  # División segura
except ZeroDivisionError:  # Capturamos división por cero
    print("No dividir por cero")  # Mensaje de error
else:  # Solo se ejecuta si no hay error
    print("Resultado:", resultado)  # Mostramos resultado""",
            ),
            (
                "Finally",
                """try:  # Iniciamos el bloque try
    archivo = open("datos.txt", "w")  # Abrimos archivo
    archivo.write("Hola")  # Escribimos en archivo
finally:  # Se ejecuta siempre
    archivo.close()  # Cerramos el archivo""",
            ),
            (
                "Raise personalizado",
                """def validar(edad):  # Definimos la función
    if edad < 0:  # Validamos la edad
        raise ValueError("Edad inválida")  # Lanzamos error
validar(5)  # Llamamos a la función""",
            ),
            (
                "Excepción custom",
                """class ConfigError(Exception):  # Creamos excepción
    pass  # No agregamos lógica
raise ConfigError("Falta API_KEY")  # Lanzamos el error""",
            ),
            (
                "Encadenar errores",
                """try:  # Intentamos convertir
    int("abc")  # Fuerza ValueError
except ValueError as exc:  # Capturamos ValueError
    raise RuntimeError("Entrada no válida") from exc  # Encadenamos""",
            ),
            (
                "Captura múltiple",
                """try:  # Iniciamos el bloque
    valor = int("x")  # Forzamos error
except (ValueError, TypeError):  # Capturamos múltiples errores
    print("Conversión inválida")  # Mensaje""",
            ),
            (
                "Context manager",
                """with open("datos.txt", "w") as archivo:  # Abrimos con with
    archivo.write("Seguro")  # Escribimos y cerramos""",
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
