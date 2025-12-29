from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson
from app.utils.optional_imports import optional_import


class DataFrameBasicsLesson(Lesson):
    TITLE = "DataFrame basics"
    CATEGORY = "Pandas"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Intermedio"
    TAGS = ["DataFrame", "pandas", "tablas", "index"]

    def summary(self) -> str:
        return (
            "Pandas DataFrame es la estructura tabular principal. Aprende a crear, "
            "seleccionar, filtrar y transformar datos de forma eficiente."
        )

    def guide(self) -> str:
        return """
- Un DataFrame es una tabla con filas y columnas.
- Puedes crearlo desde dicts, listas o archivos.
- El índice identifica filas; puede ser personalizado.
- Usa .loc para selección por etiqueta y .iloc por posición.
- Las columnas se acceden como df["col"] o df.col.
- Usa df.head() para inspeccionar datos.
- Las operaciones vectorizadas son más rápidas que loops.
- Los filtros usan máscaras booleanas.
- Usa df.assign() para añadir columnas.
- df.groupby() permite agregaciones.
- missing values se representan como NaN.
- Usa df.fillna() o df.dropna() para limpiar.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Confundir loc e iloc",
                "loc usa etiquetas; iloc usa posiciones.",
            ),
            (
                "Modificar vistas",
                "Una selección puede ser vista; usa .copy() si vas a editar.",
            ),
            (
                "Asignación encadenada",
                "df[df.col > 0]["col"] = 1 no garantiza cambios.",
            ),
            (
                "Index mal definido",
                "Un índice incorrecto rompe merges y joins.",
            ),
            (
                "Tipado inconsistente",
                "Columnas mixtas dificultan operaciones numéricas.",
            ),
            (
                "Operaciones con NaN",
                "NaN propaga; usa fillna o dropna.",
            ),
            (
                "No usar vectorización",
                "Bucles Python son lentos comparados con operaciones nativas.",
            ),
            (
                "Olvidar reset_index",
                "Después de groupby o filtering, el índice puede ser confuso.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Crear DataFrame",
                """import pandas as pd\n\ndata = {"nombre": ["Ana", "Luis"], "edad": [30, 25]}\ndf = pd.DataFrame(data)\nprint(df)""",
            ),
            (
                "Seleccionar columnas",
                """df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})\nprint(df["a"])""",
            ),
            (
                "Filtrar filas",
                """df = pd.DataFrame({"edad": [20, 30, 40]})\nprint(df[df["edad"] > 25])""",
            ),
            (
                "loc vs iloc",
                """df = pd.DataFrame({"valor": [10, 20]}, index=["a", "b"])\nprint(df.loc["a"])\nprint(df.iloc[0])""",
            ),
            (
                "Agregar columna",
                """df = pd.DataFrame({"x": [1, 2, 3]})\ndf = df.assign(y=df["x"] * 2)\nprint(df)""",
            ),
            (
                "Groupby",
                """df = pd.DataFrame({"tipo": ["A", "A", "B"], "valor": [1, 2, 3]})\nprint(df.groupby("tipo")["valor"].mean())""",
            ),
            (
                "Missing values",
                """df = pd.DataFrame({"x": [1, None, 3]})\nprint(df.fillna(0))""",
            ),
            (
                "Reset index",
                """df = pd.DataFrame({"a": [1, 2]}, index=["id1", "id2"])\nprint(df.reset_index())""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea un DataFrame con columnas 'producto' y 'precio'.",
                "hints": ["Usa un dict"],
                "solution": "df = pd.DataFrame({'producto': ['A', 'B'], 'precio': [10, 15]})",
            },
            {
                "question": "Filtra un DataFrame para obtener filas con precio > 10.",
                "hints": ["Usa una máscara booleana"],
                "solution": "df_filtrado = df[df['precio'] > 10]",
            },
            {
                "question": "Agrupa por 'categoria' y calcula la suma de 'ventas'.",
                "hints": ["groupby", "sum"],
                "solution": "resultado = df.groupby('categoria')['ventas'].sum()",
            },
        ]

    def requirements(self) -> list[str]:
        return ["pandas"]

    def build_demo(self) -> QWidget | None:
        ok, _, message = optional_import("pandas")
        if not ok:
            widget = QWidget()
            layout = QVBoxLayout(widget)
            layout.addWidget(QLabel(message or "Pandas no disponible."))
            return widget
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Pandas disponible. Revisa los ejemplos para explorar."))
        return widget
