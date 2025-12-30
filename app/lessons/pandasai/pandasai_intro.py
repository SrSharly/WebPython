from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson
from app.utils.optional_imports import optional_import


class PandasAILesson(Lesson):
    TITLE = "PandasAI intro"
    CATEGORY = "PandasAI"
    SUBCATEGORY = "IA en datos"
    LEVEL = "Intermedio"
    TAGS = ["pandasai", "nlp", "dataframes", "prompt"]

    def summary(self) -> str:
        return (
            "PandasAI permite consultar DataFrames con lenguaje natural. Aprende "
            "el flujo básico, configuración y límites de seguridad."
        )

    def guide(self) -> str:
        return """
- PandasAI combina LLMs con DataFrames para consultas en lenguaje natural.
- Necesita un modelo configurado (API Key o modelo local).
- Se integra con pandas para analizar tablas.
- Define prompts claros para resultados precisos.
- Controla los datos sensibles antes de enviarlos a un modelo.
- Usa ejemplos y contexto para guiar la respuesta.
- Valida los resultados antes de aplicarlos.
- Ideal para exploración rápida y prototipos.
- No reemplaza un pipeline reproducible.
- Documenta las consultas para auditoría.
- Limita el acceso a columnas sensibles.
- Combina con filtros previos en pandas.

## Operaciones y métodos más útiles
### DataFrame / Series (pandas)
1) `head()` ⭐  
Qué hace: muestra primeras filas.  
Así se escribe:
```py
df.head(3)
```
Error típico:
```py
df.head
```
Verás esto: filas iniciales.  
Por qué funciona: inspección rápida.  
Lo típico que sale mal: olvidar paréntesis; pensar que cambia el DataFrame.

2) `info()` ⭐  
Qué hace: resumen de tipos y nulos.  
Así se escribe:
```py
df.info()
```
Error típico:
```py
df.info
```
Verás esto: tipos y conteos.  
Por qué funciona: inspecciona columnas.  
Lo típico que sale mal: confundir con `describe`; olvidar paréntesis.

3) `describe()` ⭐  
Qué hace: estadísticas básicas.  
Así se escribe:
```py
df.describe()
```
Error típico:
```py
df.describe
```
Verás esto: media, percentiles.  
Por qué funciona: calcula stats numéricas.  
Lo típico que sale mal: esperar columnas no numéricas; olvidar paréntesis.

4) `loc` ⭐  
Qué hace: selección por etiquetas.  
Así se escribe:
```py
df.loc[df["ventas"] > 10, "ventas"]
```
Error típico:
```py
df.loc[df["ventas"] > 10]["ventas"] = 0
```
Verás esto: serie filtrada.  
Por qué funciona: selección segura.  
Lo típico que sale mal: asignación encadenada; columnas mal escritas.

5) `iloc` ⭐  
Qué hace: selección por posición.  
Así se escribe:
```py
df.iloc[0, 0]
```
Error típico:
```py
df.iloc["0", "0"]
```
Verás esto: un valor.  
Por qué funciona: usa índices enteros.  
Lo típico que sale mal: usar strings; salir de rango.

6) `groupby()` ⭐  
Qué hace: agrega por grupos.  
Así se escribe:
```py
df.groupby("region")["ventas"].sum()
```
Error típico:
```py
df.groupby("region").sum["ventas"]
```
Verás esto: suma por región.  
Por qué funciona: agrupa y agrega.  
Lo típico que sale mal: olvidar paréntesis en `sum`; grupo inexistente.

7) `dropna()` ⭐  
Qué hace: elimina faltantes.  
Así se escribe:
```py
df.dropna()
```
Error típico:
```py
df.dropna(axis="filas")
```
Verás esto: filas sin NaN.  
Por qué funciona: elimina según eje.  
Lo típico que sale mal: axis inválido; borrar demasiados datos.

8) `fillna()` ⭐  
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


## Micro-ejemplo incremental: consulta guiada con PandasAI

### Así se escribe
```py
import pandas as pd
from pandasai import SmartDataframe

ventas = pd.DataFrame({"mes": ["ene", "feb"], "total": [100, 140]})
sdf = SmartDataframe(ventas)
respuesta = sdf.chat("¿Cuál es el total mayor?")
print(respuesta)
```

### Error típico: pasar algo que no es DataFrame
```py
from pandasai import SmartDataframe

sdf = SmartDataframe([1, 2, 3])
```

```py
ValueError: data must be a pandas DataFrame
```

Explicación breve: `SmartDataframe` requiere un `pd.DataFrame` real.

### Error típico: columna mencionada que no existe
```py
import pandas as pd
from pandasai import SmartDataframe

ventas = pd.DataFrame({"mes": ["ene", "feb"], "total": [100, 140]})
sdf = SmartDataframe(ventas)
print(sdf.chat("Promedio de precio"))
```

```py
KeyError: 'precio'
```

Explicación breve: el modelo consulta sobre las columnas disponibles.

""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "No configurar LLM",
                "Sin modelo configurado, PandasAI no puede responder.",
            ),
            (
                "Envío de datos sensibles",
                "Evita enviar PII a un modelo externo.",
            ),
            (
                "Prompts ambiguos",
                "Consultas vagas generan respuestas incorrectas.",
            ),
            (
                "No validar resultados",
                "Los LLMs pueden inventar datos; valida siempre.",
            ),
            (
                "Uso sin contexto",
                "Explica qué representa cada columna.",
            ),
            (
                "Ignorar costes",
                "Las consultas pueden tener coste por tokens.",
            ),
            (
                "No manejar errores",
                "Captura errores de red o credenciales inválidas.",
            ),
            (
                "Confundir con BI",
                "PandasAI no sustituye dashboards ni pipelines.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Configuración básica",
                """from pandasai import SmartDataframe\nimport pandas as pd\n\ndf = pd.DataFrame({"ventas": [10, 20, 30]})\nsdf = SmartDataframe(df)\nprint(sdf.chat("Promedio de ventas"))""",
            ),
            (
                "Prompt específico",
                """sdf.chat("¿Cuál es la suma total de ventas?")""",
            ),
            (
                "Limitar columnas",
                """df = df[["ventas", "region"]]""",
            ),
            (
                "Validar con pandas",
                """respuesta = sdf.chat("Ventas máximas")\nprint(df["ventas"].max())""",
            ),
            (
                "Documentar consultas",
                """consultas = ["Promedio", "Máximo"]""",
            ),
            (
                "Errores comunes",
                """try:\n    sdf.chat("Consulta")\nexcept Exception as exc:\n    print(exc)""",
            ),
            (
                "Contexto adicional",
                """sdf.chat("ventas es monto en USD, region es país")""",
            ),
            (
                "Prototipo rápido",
                """print(sdf.chat("Grafica ventas por región"))""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "¿Qué medida tomarías antes de enviar datos sensibles a PandasAI?",
                "hints": ["PII", "Anonimizar"],
                "solution": "Anonimizar o eliminar columnas sensibles antes de la consulta.",
            },
            {
                "question": "Escribe un prompt claro para pedir la suma de ventas por región.",
                "hints": ["Menciona columnas"],
                "solution": "Devuelve la suma de ventas por región usando columnas ventas y region.",
            },
            {
                "question": "¿Por qué no debes confiar ciegamente en la respuesta del LLM?",
                "hints": ["Puede alucinar"],
                "solution": "Porque el modelo puede inventar datos; hay que validar con pandas.",
            },
        ]

    def requirements(self) -> list[str]:
        return ["pandasai", "pandas"]

    def build_demo(self) -> QWidget | None:
        ok, _, message = optional_import("pandasai")
        widget = QWidget()
        layout = QVBoxLayout(widget)
        if not ok:
            layout.addWidget(QLabel(message or "PandasAI no disponible."))
            return widget
        layout.addWidget(QLabel("PandasAI está disponible. Configura un modelo para usarlo."))
        return widget
