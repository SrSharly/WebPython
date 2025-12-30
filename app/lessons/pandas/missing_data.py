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

## Operaciones y métodos más útiles
### DataFrame / Series (faltantes)
1) `isna()` ⭐  
Qué hace: detecta faltantes.  
Así se escribe:
```py
df.isna()
```
Error típico:
```py
df.isna
```
Verás esto: máscara booleana.  
Por qué funciona: marca NaN/NA como True.  
Lo típico que sale mal: olvidar paréntesis; comparar con `== None`.

2) `notna()`  
Qué hace: detecta valores presentes.  
Así se escribe:
```py
df.notna()
```
Error típico:
```py
df.notna
```
Verás esto: máscara booleana inversa.  
Por qué funciona: invierte la lógica de `isna`.  
Lo típico que sale mal: confundir con `not`; olvidar paréntesis.

3) `fillna()` ⭐  
Qué hace: rellena faltantes.  
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

4) `dropna()` ⭐  
Qué hace: elimina filas con faltantes.  
Así se escribe:
```py
df.dropna()
```
Error típico:
```py
df.dropna(axis="filas")
```
Verás esto: menos filas.  
Por qué funciona: elimina según el eje.  
Lo típico que sale mal: usar axis inválido; borrar demasiados datos.

5) `dropna(axis=1)`  
Qué hace: elimina columnas con faltantes.  
Así se escribe:
```py
df.dropna(axis=1)
```
Error típico:
```py
df.dropna(axis=2)
```
Verás esto: menos columnas.  
Por qué funciona: axis 1 apunta a columnas.  
Lo típico que sale mal: usar axis incorrecto; perder columnas útiles.

6) `isna().sum()` ⭐  
Qué hace: cuenta faltantes por columna.  
Así se escribe:
```py
df.isna().sum()
```
Error típico:
```py
df.isna.sum()
```
Verás esto: conteo por columna.  
Por qué funciona: suma True como 1.  
Lo típico que sale mal: olvidar paréntesis; aplicar en eje equivocado.

7) `astype()`  
Qué hace: ajusta tipos para NA.  
Así se escribe:
```py
df["edad"] = df["edad"].astype("Int64")
```
Error típico:
```py
df["edad"] = df["edad"].astype("int")
```
Verás esto: permite NA en enteros.  
Por qué funciona: tipos extendidos aceptan NA.  
Lo típico que sale mal: perder NA con int nativo; tipos incompatibles.


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
        area = QTextEdit()
        area.setReadOnly(True)
        area.setText("\n".join(texto))
        layout.addWidget(area)
        return widget
