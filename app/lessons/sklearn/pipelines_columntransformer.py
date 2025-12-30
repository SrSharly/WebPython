from __future__ import annotations

from PySide6.QtWidgets import QLabel, QTextEdit, QVBoxLayout, QWidget

from app.lesson_base import Lesson
from app.utils.optional_imports import optional_import


class PipelinesColumnTransformerLesson(Lesson):
    TITLE = "Pipelines + ColumnTransformer"
    CATEGORY = "scikit-learn"
    SUBCATEGORY = "Modelado"
    LEVEL = "Intermedio"
    TAGS = ["Pipeline", "ColumnTransformer", "leakage", "train/test"]

    def summary(self) -> str:
        return (
            "Combina Pipeline y ColumnTransformer para preprocesar columnas numéricas "
            "y categóricas sin data leakage, con un flujo reproducible de entrenamiento."
        )

    def guide(self) -> str:
        return """
TL;DR: ColumnTransformer aplica transformaciones por tipo de columna y Pipeline encadena todo.
- Separa train/test antes de cualquier transformación dependiente de datos.
- ColumnTransformer aplica distintos pasos por columnas numéricas/categóricas.
- OneHotEncoder convierte categorías a variables binarias.
- StandardScaler normaliza columnas numéricas.
- Pipeline garantiza que fit/transform ocurren en orden correcto.
- Evita leakage manteniendo transformaciones dentro del pipeline.
- Usa train_test_split para validación rápida.
- Las métricas deben calcularse en el set de test.
- Puedes combinar imputación, escalado y modelo en una sola cadena.
- Pipelines facilitan reproducibilidad y despliegue.
- Usa predict_proba si necesitas probabilidades.
- Documenta columnas y tipos usados en el modelo.

## Operaciones y métodos más útiles
### Estimadores y pipelines (scikit-learn)
1) `fit()` ⭐  
Qué hace: entrena el modelo con datos.  
Así se escribe:
```py
modelo.fit(X_train, y_train)
```
Error típico:
```py
modelo.fit(X_train)
```
Verás esto: error por faltar `y`.  
Por qué funciona: aprende parámetros internos.  
Lo típico que sale mal: usar `fit` con X e y de distinto tamaño; ajustar con datos ya filtrados del test.

2) `predict()` ⭐  
Qué hace: genera predicciones.  
Así se escribe:
```py
pred = modelo.predict(X_test)
```
Error típico:
```py
pred = modelo.predict()
```
Verás esto: array de predicciones.  
Por qué funciona: aplica el modelo entrenado.  
Lo típico que sale mal: llamar antes de `fit`; columnas distintas al entrenamiento.

3) `score()`  
Qué hace: evalúa con métrica base.  
Así se escribe:
```py
score = modelo.score(X_test, y_test)
```
Error típico:
```py
score = modelo.score(X_test)
```
Verás esto: un número de desempeño.  
Por qué funciona: usa la métrica por defecto del estimador.  
Lo típico que sale mal: olvidar `y_test`; usarla como única métrica.

4) `transform()`  
Qué hace: transforma datos (preprocesadores).  
Así se escribe:
```py
X_proc = preprocesador.transform(X_test)
```
Error típico:
```py
X_proc = preprocesador.transform()
```
Verás esto: datos transformados.  
Por qué funciona: aplica parámetros aprendidos en `fit`.  
Lo típico que sale mal: llamar antes de `fit`; cambiar columnas.

5) `fit_transform()` ⭐  
Qué hace: ajusta y transforma en un paso.  
Así se escribe:
```py
X_proc = preprocesador.fit_transform(X_train)
```
Error típico:
```py
X_proc = preprocesador.fit_transform(X_test)
```
Verás esto: datos transformados.  
Por qué funciona: ajusta con entrenamiento y transforma.  
Lo típico que sale mal: usarlo en test (leakage); mezclar train/test.

6) `predict_proba()`  
Qué hace: probabilidades por clase.  
Así se escribe:
```py
proba = modelo.predict_proba(X_test)
```
Error típico:
```py
proba = modelo.predict_proba()
```
Verás esto: probabilidades por clase.  
Por qué funciona: modelos de clasificación exponen probabilidades.  
Lo típico que sale mal: usar en regresión; no calibrar probabilidades.

7) `get_params()`  
Qué hace: inspecciona hiperparámetros.  
Así se escribe:
```py
params = modelo.get_params()
```
Error típico:
```py
params = modelo.get_params
```
Verás esto: dict de parámetros.  
Por qué funciona: expone configuración del estimador.  
Lo típico que sale mal: olvidar paréntesis; modificar params sin reentrenar.

8) `set_params()`  
Qué hace: actualiza hiperparámetros.  
Así se escribe:
```py
modelo.set_params(C=1.0)
```
Error típico:
```py
modelo.set_params("C=1.0")
```
Verás esto: modelo reconfigurado.  
Por qué funciona: valida nombres de parámetros.  
Lo típico que sale mal: pasar string; olvidar volver a entrenar.


## Micro-ejemplo incremental: entrenamiento y validación

### Así se escribe
```py
from sklearn.linear_model import LinearRegression

X = [[1], [2], [3]]
y = [2, 4, 6]
modelo = LinearRegression()
modelo.fit(X, y)
print(modelo.predict([[4]]))
```

### Error típico: predecir antes de ajustar
```py
from sklearn.linear_model import LinearRegression

modelo = LinearRegression()
modelo.predict([[4]])
```

```py
NotFittedError: This LinearRegression instance is not fitted yet. Call 'fit' with appropriate arguments before using this estimator.
```

Explicación breve: primero se llama a `fit`, luego `predict`.

### Error típico: longitudes distintas en X e y
```py
from sklearn.linear_model import LinearRegression

X = [[1], [2]]
y = [2]
modelo = LinearRegression()
modelo.fit(X, y)
```

```py
ValueError: Found input variables with inconsistent numbers of samples: [2, 1]
```

Explicación breve: X e y deben tener la misma cantidad de muestras.

""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Leakage por preprocesar antes",
                "No apliques escalado/codificación antes del split.",
            ),
            (
                "Columnas mal definidas",
                "Si cambian los nombres, el pipeline falla.",
            ),
            (
                "OneHot sin handle_unknown",
                "Categorías nuevas rompen predicción si no se controla.",
            ),
            (
                "Mezclar tipos",
                "Columnas numéricas como texto dificultan el escalado.",
            ),
            (
                "Olvidar métricas",
                "Sin evaluación, no sabes si el modelo generaliza.",
            ),
            (
                "No fijar random_state",
                "Resultados no reproducibles en split o modelo.",
            ),
            (
                "Imputación fuera del pipeline",
                "Puede filtrar estadísticas del test.",
            ),
            (
                "Pipeline demasiado complejo",
                "Dificulta la interpretación y mantenimiento.",
            ),
            (
                "No guardar el pipeline",
                "Debes persistir el flujo completo, no solo el modelo.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "ColumnTransformer",
                """from sklearn.compose import ColumnTransformer\nfrom sklearn.preprocessing import OneHotEncoder, StandardScaler\n\npreprocess = ColumnTransformer([\n    ("num", StandardScaler(), ["edad", "ingresos"]),\n    ("cat", OneHotEncoder(handle_unknown="ignore"), ["ciudad"])\n])""",
            ),
            (
                "Pipeline",
                """from sklearn.pipeline import Pipeline\nfrom sklearn.linear_model import LogisticRegression\n\npipeline = Pipeline([\n    ("prep", preprocess),\n    ("model", LogisticRegression())\n])""",
            ),
            (
                "Train/test",
                """from sklearn.model_selection import train_test_split\n\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)""",
            ),
            (
                "Evaluar",
                """from sklearn.metrics import accuracy_score\n\npred = pipeline.predict(X_test)\nprint(accuracy_score(y_test, pred))""",
            ),
            (
                "Predict nuevo",
                """nuevo = pd.DataFrame({"edad": [30], "ingresos": [50000], "ciudad": ["A"]})\nprint(pipeline.predict(nuevo))""",
            ),
            (
                "Imputación",
                """from sklearn.impute import SimpleImputer\n\nnum_pipe = Pipeline([("imputer", SimpleImputer()), ("scaler", StandardScaler())])""",
            ),
            (
                "Feature names",
                """pipeline.named_steps["prep"].get_feature_names_out()""",
            ),
            (
                "Handle unknown",
                """OneHotEncoder(handle_unknown="ignore")""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Define columnas numéricas y categóricas para ColumnTransformer.",
                "hints": ["listas de columnas"],
                "solution": "num_cols = ['edad', 'ingresos']\ncat_cols = ['ciudad']",
            },
            {
                "question": "Crea un Pipeline con preprocess y LogisticRegression.",
                "hints": ["Pipeline([('prep', ...), ('model', ...)])"],
                "solution": "pipeline = Pipeline([('prep', preprocess), ('model', LogisticRegression())])",
            },
            {
                "question": "¿Por qué no debes escalar antes del train/test split?",
                "hints": ["leakage"],
                "solution": "Porque usarías estadísticas de todo el dataset, filtrando información del test.",
            },
        ]

    def requirements(self) -> list[str]:
        return ["sklearn", "pandas"]

    def build_demo(self) -> QWidget | None:
        ok_sklearn, _, msg_sklearn = optional_import("sklearn")
        ok_pandas, pd, msg_pandas = optional_import("pandas")
        widget = QWidget()
        layout = QVBoxLayout(widget)
        if not ok_sklearn or not ok_pandas:
            message = msg_sklearn or msg_pandas or "Dependencias no disponibles."
            layout.addWidget(QLabel(message))
            return widget

        import numpy as np
        from sklearn.compose import ColumnTransformer
        from sklearn.linear_model import LogisticRegression
        from sklearn.metrics import accuracy_score
        from sklearn.model_selection import train_test_split
        from sklearn.pipeline import Pipeline
        from sklearn.preprocessing import OneHotEncoder, StandardScaler

        rng = np.random.default_rng(42)
        ciudades = np.array(["A", "B", "C"])
        data = {
            "edad": rng.integers(18, 60, size=200),
            "ingresos": rng.integers(20000, 90000, size=200),
            "ciudad": rng.choice(ciudades, size=200),
        }
        df = pd.DataFrame(data)
        y = (
            (df["ingresos"] > 50000).astype(int)
            + (df["ciudad"] == "A").astype(int)
            + (df["edad"] < 30).astype(int)
        )
        y = (y > 1).astype(int)

        X_train, X_test, y_train, y_test = train_test_split(
            df, y, test_size=0.25, random_state=42, stratify=y
        )

        preprocess = ColumnTransformer(
            [
                ("num", StandardScaler(), ["edad", "ingresos"]),
                ("cat", OneHotEncoder(handle_unknown="ignore"), ["ciudad"]),
            ]
        )
        pipeline = Pipeline(
            [
                ("prep", preprocess),
                ("model", LogisticRegression(max_iter=200)),
            ]
        )
        pipeline.fit(X_train, y_train)
        pred = pipeline.predict(X_test)
        score = accuracy_score(y_test, pred)

        ejemplo = pd.DataFrame({"edad": [28], "ingresos": [62000], "ciudad": ["B"]})
        pred_ejemplo = pipeline.predict(ejemplo)[0]

        layout.addWidget(QLabel("Demo: Pipeline + ColumnTransformer con dataset sintético."))
        area = QTextEdit()
        area.setReadOnly(True)
        area.setText(
            "\n".join(
                [
                    f"Accuracy test: {score:.2f}",
                    f"Predicción ejemplo (edad=28, ingresos=62000, ciudad=B): {pred_ejemplo}",
                    "Nota: el preprocesamiento ocurre dentro del pipeline.",
                ]
            )
        )
        layout.addWidget(area)
        return widget
