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
- Usa try/except para capturar errores esperados.
- Captura excepciones específicas en lugar de Exception.
- `else` en try se ejecuta solo si no hay error.
- `finally` se ejecuta siempre, ideal para liberar recursos.
- `raise` permite lanzar excepciones propias o reenviar.
- Crea excepciones personalizadas heredando de Exception.
- Usa `from` para encadenar excepciones.
- Evita silenciar errores con except vacío.
- Mantén los bloques try lo más pequeños posible.
- Usa logging para registrar detalles de fallos.
- `assert` es para tests, no para validaciones en producción.
- Documenta qué excepciones puede lanzar tu función.
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
                """try:\n    valor = int("10")\n    print(valor)\nexcept ValueError as exc:\n    print("Error:", exc)""",
            ),
            (
                "Try/except/else",
                """try:\n    resultado = 10 / 2\nexcept ZeroDivisionError:\n    print("No dividir por cero")\nelse:\n    print("Resultado:", resultado)""",
            ),
            (
                "Finally",
                """try:\n    archivo = open("datos.txt", "w")\n    archivo.write("Hola")\nfinally:\n    archivo.close()""",
            ),
            (
                "Raise personalizado",
                """def validar(edad):\n    if edad < 0:\n        raise ValueError("Edad inválida")\n\nvalidar(5)""",
            ),
            (
                "Excepción custom",
                """class ConfigError(Exception):\n    pass\n\nraise ConfigError("Falta API_KEY")""",
            ),
            (
                "Encadenar errores",
                """try:\n    int("abc")\nexcept ValueError as exc:\n    raise RuntimeError("Entrada no válida") from exc""",
            ),
            (
                "Captura múltiple",
                """try:\n    valor = int("x")\nexcept (ValueError, TypeError):\n    print("Conversión inválida")""",
            ),
            (
                "Context manager",
                """with open("datos.txt", "w") as archivo:\n    archivo.write("Seguro")""",
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
