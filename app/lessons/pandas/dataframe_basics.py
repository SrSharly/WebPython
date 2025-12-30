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

## Operaciones y métodos más útiles
### DataFrame / Series
1) `head()` ⭐  
Qué hace: muestra las primeras filas.  
Así se escribe:
```py
df.head(3)
```
Error típico:
```py
df.head
```
Verás esto: 3 filas iniciales.  
Por qué funciona: `head` crea una vista rápida.  
Lo típico que sale mal: olvidar paréntesis; asumir que modifica el DataFrame.

2) `info()` ⭐  
Qué hace: resumen de columnas y tipos.  
Así se escribe:
```py
df.info()
```
Error típico:
```py
info = df.info
```
Verás esto: tipos, nulos y memoria.  
Por qué funciona: inspecciona estructura.  
Lo típico que sale mal: confundir con `describe`; olvidar paréntesis.

3) `describe()` ⭐  
Qué hace: estadísticos descriptivos.  
Así se escribe:
```py
df.describe()
```
Error típico:
```py
df.describe
```
Verás esto: media, percentiles, etc.  
Por qué funciona: calcula estadísticas numéricas.  
Lo típico que sale mal: esperar columnas no numéricas; olvidar paréntesis.

4) `loc` ⭐  
Qué hace: selección por etiquetas.  
Así se escribe:
```py
df.loc[df["edad"] > 25, "edad"]
```
Error típico:
```py
df.loc[df["edad"] > 25]["edad"] = 99
```
Verás esto: columna filtrada.  
Por qué funciona: `loc` selecciona y asigna seguro.  
Lo típico que sale mal: asignación encadenada; confundir filas/columnas.

5) `iloc` ⭐  
Qué hace: selección por posición.  
Así se escribe:
```py
df.iloc[0, 1]
```
Error típico:
```py
df.iloc["0", "1"]
```
Verás esto: un valor puntual.  
Por qué funciona: usa índices enteros.  
Lo típico que sale mal: usar strings; salir de rango.

6) `groupby()` ⭐  
Qué hace: agrupa para agregaciones.  
Así se escribe:
```py
df.groupby("nombre")["edad"].mean()
```
Error típico:
```py
df.groupby("nombre").mean["edad"]
```
Verás esto: promedio por grupo.  
Por qué funciona: crea grupos y aplica agregaciones.  
Lo típico que sale mal: olvidar `()` en `mean`; agrupar por columna inexistente.

7) `merge()` ⭐  
Qué hace: une tablas por claves.  
Así se escribe:
```py
df.merge(otros, on="id")
```
Error típico:
```py
df.merge(otros)
```
Verás esto: DataFrame combinado.  
Por qué funciona: alinea por clave.  
Lo típico que sale mal: duplicar columnas; claves con tipos distintos.

8) `concat()`  
Qué hace: concatena filas o columnas.  
Así se escribe:
```py
pd.concat([df1, df2], axis=0)
```
Error típico:
```py
df1.concat(df2)
```
Verás esto: DataFrame unido.  
Por qué funciona: `concat` es función de pandas.  
Lo típico que sale mal: usar método inexistente; índices desalineados.

9) `dropna()` ⭐  
Qué hace: elimina filas/columnas con NaN.  
Así se escribe:
```py
df.dropna()
```
Error típico:
```py
df.dropna(axis="filas")
```
Verás esto: DataFrame sin nulos.  
Por qué funciona: descarta NaN según el eje.  
Lo típico que sale mal: usar axis inválido; borrar datos sin copia.

10) `fillna()` ⭐  
Qué hace: rellena NaN con un valor.  
Así se escribe:
```py
df.fillna(0)
```
Error típico:
```py
df.fillna()
```
Verás esto: NaN reemplazados.  
Por qué funciona: asigna un valor por defecto.  
Lo típico que sale mal: olvidar el valor; mezclar tipos.

11) `astype()`  
Qué hace: convierte tipos de columnas.  
Así se escribe:
```py
df["edad"] = df["edad"].astype(int)
```
Error típico:
```py
df["edad"] = df["edad"].astype("numero")
```
Verás esto: columna convertida.  
Por qué funciona: `astype` cambia dtype.  
Lo típico que sale mal: tipos inválidos; valores no convertibles.

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


## Micro-ejemplo incremental: DataFrame en contexto

### Así se escribe
```py
import pandas as pd

df = pd.DataFrame({"producto": ["A", "B"], "precio": [10, 12]})
bonificado = df["precio"] * 0.9
print(bonificado)
```

### Error típico: acceder a una columna inexistente
```py
import pandas as pd

df = pd.DataFrame({"producto": ["A", "B"], "precio": [10, 12]})
print(df["coste"])
```

```py
KeyError: 'coste'
```

Explicación breve: la columna debe existir o debes crearla antes de usarla.

### Error típico: mezclar longitudes distintas
```py
import pandas as pd

df = pd.DataFrame({"producto": ["A", "B"], "precio": [10, 12]})
df["stock"] = [1, 2, 3]
```

```py
ValueError: Length of values (3) does not match length of index (2)
```

Explicación breve: el tamaño de la nueva columna debe coincidir con el índice.

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
