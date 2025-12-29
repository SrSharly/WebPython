from __future__ import annotations

from PySide6.QtWidgets import QLabel, QTextEdit, QVBoxLayout, QWidget

from app.lesson_base import Lesson
from app.utils.optional_imports import optional_import


class MissingDataLesson(Lesson):
    TITLE = "Missing data"
    CATEGORY = "Pandas"
    SUBCATEGORY = "Limpieza"
    LEVEL = "Intermedio"
    TAGS = ["NaN", "NA", "isna", "fillna", "dropna"]

    def summary(self) -> str:
        return (
            "Aprende a detectar y tratar valores faltantes en pandas con isna, "
            "fillna y dropna, evitando errores comunes en limpieza de datos."
        )

    def guide(self) -> str:
        return """
TL;DR: Pandas usa NaN/NA para faltantes; detecta con isna y decide si imputar o eliminar.
- NaN representa ausencia de datos en columnas numéricas.
- NA (pandas.NA) se usa en tipos extendidos.
- isna() y notna() ayudan a detectar faltantes.
- fillna() permite imputar con valores constantes o estrategias.
- dropna() elimina filas/columnas con faltantes.
- axis y how controlan el comportamiento de dropna.
- Mezclar tipos puede convertir a object y complicar NA.
- Comparar con NaN usando == siempre da False.
- Usa df.isna().sum() para contar faltantes por columna.
- Evita inplace=True; devuelve nuevos objetos más claros.
- SettingWithCopy puede aparecer al encadenar filtros.
- Documenta la estrategia de imputación para reproducibilidad.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Comparar con NaN",
                "NaN != NaN; usa isna() para detectar.",
            ),
            (
                "fillna inplace",
                "inplace=True es confuso; prefiere asignar el resultado.",
            ),
            (
                "Tipos mezclados",
                "Columnas object dificultan operaciones y NA.",
            ),
            (
                "SettingWithCopy",
                "Evita asignaciones encadenadas; usa .loc y .copy().",
            ),
            (
                "dropna agresivo",
                "Eliminar muchas filas puede sesgar resultados.",
            ),
            (
                "Imputar con cero",
                "Cero puede no ser un valor válido; evalúa contexto.",
            ),
            (
                "Ignorar NA en categóricas",
                "Categorical requiere manejo explícito de NA.",
            ),
            (
                "No medir faltantes",
                "Cuenta faltantes antes de decidir estrategia.",
            ),
            (
                "Confundir None con NaN",
                "Pandas convierte None a NaN en numéricas.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "isna",
                """import pandas as pd\n\ndf = pd.DataFrame({"a": [1, None, 3]})\nprint(df.isna())""",
            ),
            (
                "notna",
                """df = pd.DataFrame({"a": [1, None, 3]})\nprint(df.notna())""",
            ),
            (
                "fillna constante",
                """df = pd.DataFrame({"a": [1, None, 3]})\nprint(df.fillna(0))""",
            ),
            (
                "fillna con media",
                """df = pd.DataFrame({"a": [1, None, 3]})\nprint(df["a"].fillna(df["a"].mean()))""",
            ),
            (
                "dropna filas",
                """df = pd.DataFrame({"a": [1, None, 3], "b": [1, 2, None]})\nprint(df.dropna())""",
            ),
            (
                "dropna columnas",
                """df = pd.DataFrame({"a": [1, None], "b": [1, 2]})\nprint(df.dropna(axis=1))""",
            ),
            (
                "Contar faltantes",
                """df = pd.DataFrame({"a": [1, None, 3], "b": [None, 2, 3]})\nprint(df.isna().sum())""",
            ),
            (
                "Comparación correcta",
                """import numpy as np\n\nvalor = np.nan\nprint(pd.isna(valor))""",
            ),
            (
                "Evitar inplace",
                """df = pd.DataFrame({"a": [1, None]})\nlimpio = df.fillna(0)""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea un DataFrame con una columna que tenga un NaN.",
                "hints": ["None se convierte a NaN"],
                "solution": "df = pd.DataFrame({'a': [1, None, 3]})",
            },
            {
                "question": "Cuenta los NaN por columna.",
                "hints": ["isna", "sum"],
                "solution": "conteo = df.isna().sum()",
            },
            {
                "question": "Rellena NaN con el promedio de la columna.",
                "hints": ["fillna", "mean"],
                "solution": "df['a'] = df['a'].fillna(df['a'].mean())",
            },
        ]

    def requirements(self) -> list[str]:
        return ["pandas"]

    def build_demo(self) -> QWidget | None:
        ok, pd, message = optional_import("pandas")
        widget = QWidget()
        layout = QVBoxLayout(widget)
        if not ok:
            layout.addWidget(QLabel(message or "Pandas no disponible."))
            return widget

        df = pd.DataFrame(
            {
                "producto": ["A", "B", "C", "D"],
                "precio": [10.0, None, 15.0, None],
                "stock": [5, 0, None, 12],
            }
        )
        texto = [
            "DataFrame original:",
            df.to_string(index=False),
            "\nFaltantes por columna:",
            df.isna().sum().to_string(),
            "\nfillna(precio=media):",
            df.assign(precio=df["precio"].fillna(df["precio"].mean())).to_string(index=False),
            "\ndropna(filas con faltantes):",
            df.dropna().to_string(index=False),
        ]
        layout.addWidget(QLabel("Demo: estrategias de missing data."))
        area = QTextEdit(readOnly=True)
        area.setText("\n".join(texto))
        layout.addWidget(area)
        return widget
