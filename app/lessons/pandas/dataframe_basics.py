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
## Qué es
Un DataFrame es una tabla con filas y columnas, similar a una hoja de cálculo.

## Cuándo se usa
Cuando necesitas analizar, filtrar o transformar datos tabulares (CSV, Excel, bases de datos).

## Conceptos previos
- Listas y diccionarios en Python.
- Operaciones básicas con números.

## Paso 1: Crear un DataFrame
```
import pandas as pd
data = {"nombre": ["Ana", "Luis"], "edad": [30, 25]}
df = pd.DataFrame(data)
```

## Paso 2: Inspeccionar datos
```
print(df.head())
```

## Paso 3: Seleccionar columnas y filas
```
print(df["edad"])  # Columna
print(df.loc[0])  # Fila por etiqueta
```

## Paso 4: Filtrar con condiciones
```
mayores = df[df["edad"] > 25]
```

## Paso 5: Agregar columnas y agrupar
```
df = df.assign(nueva=df["edad"] + 1)
resumen = df.groupby("nombre")["edad"].mean()
```

## Mini-reto
Mini-reto 1: Crea un DataFrame con productos y precios, y filtra los mayores a 10.
Solución:
```
productos = {"producto": ["A", "B"], "precio": [8, 12]}
df = pd.DataFrame(productos)
print(df[df["precio"] > 10])
```

## Errores típicos (mal vs bien)
Mal: asignación encadenada.
```
df[df["edad"] > 25]["edad"] = 99
```
Bien: usa loc para asignar.
```
df.loc[df["edad"] > 25, "edad"] = 99
```

## Nota
Nota: usa .copy() si vas a modificar un subconjunto.

## Advertencia
Advertencia: los NaN propagan operaciones; limpia datos antes de calcular.

## Checklist final
- Creo DataFrames desde dicts.
- Selecciono con [] y loc/iloc.
- Filtro con máscaras booleanas.
- Agrego columnas con assign.
- Agrupo con groupby.

## Ver también
- Variables y tipos
- Iteradores y generadores
- Excepciones
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
                "df[df.col > 0][\"col\"] = 1 no garantiza cambios.",
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
                """import pandas as pd  # Importamos pandas
data = {"nombre": ["Ana", "Luis"], "edad": [30, 25]}  # Creamos dict
df = pd.DataFrame(data)  # Construimos el DataFrame
print(df)  # Mostramos la tabla""",
            ),
            (
                "Seleccionar columnas",
                """import pandas as pd  # Importamos pandas
df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})  # Creamos DataFrame
print(df["a"])  # Seleccionamos la columna a""",
            ),
            (
                "Filtrar filas",
                """import pandas as pd  # Importamos pandas
df = pd.DataFrame({"edad": [20, 30, 40]})  # Creamos DataFrame
print(df[df["edad"] > 25])  # Filtramos por edad""",
            ),
            (
                "loc vs iloc",
                """import pandas as pd  # Importamos pandas
df = pd.DataFrame({"valor": [10, 20]}, index=["a", "b"])  # DataFrame con índice
print(df.loc["a"])  # Selección por etiqueta
print(df.iloc[0])  # Selección por posición""",
            ),
            (
                "Agregar columna",
                """import pandas as pd  # Importamos pandas
df = pd.DataFrame({"x": [1, 2, 3]})  # DataFrame base
df = df.assign(y=df["x"] * 2)  # Creamos nueva columna
print(df)  # Mostramos el resultado""",
            ),
            (
                "Groupby",
                """import pandas as pd  # Importamos pandas
df = pd.DataFrame({"tipo": ["A", "A", "B"], "valor": [1, 2, 3]})  # DataFrame
print(df.groupby("tipo")["valor"].mean())  # Media por grupo""",
            ),
            (
                "Missing values",
                """import pandas as pd  # Importamos pandas
df = pd.DataFrame({"x": [1, None, 3]})  # DataFrame con NaN
print(df.fillna(0))  # Rellenamos NaN""",
            ),
            (
                "Reset index",
                """import pandas as pd  # Importamos pandas
df = pd.DataFrame({"a": [1, 2]}, index=["id1", "id2"])  # DataFrame con índice
print(df.reset_index())  # Reiniciamos índice""",
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
            layout.addWidget(QLabel("Instala pandas con: pip install pandas"))
            layout.addWidget(QLabel("Luego reinicia la aplicación para ver la demo."))
            return widget
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Pandas disponible. Revisa los ejemplos para explorar."))
        return widget
