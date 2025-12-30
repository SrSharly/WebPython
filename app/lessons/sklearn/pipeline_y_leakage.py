from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson
from app.utils.optional_imports import optional_import


class PipelineLeakageLesson(Lesson):
    TITLE = "Pipeline y leakage"
    CATEGORY = "scikit-learn"
    SUBCATEGORY = "Buenas prácticas"
    LEVEL = "Intermedio"
    TAGS = ["pipeline", "leakage", "modelos", "validacion"]

    def summary(self) -> str:
        return (
            "Aprende a construir pipelines con scikit-learn para evitar data leakage, "
            "mantener reproducibilidad y validar modelos correctamente."
        )

    def guide(self) -> str:
        return """
- Un pipeline encadena transformaciones y modelo.
- Evita leakage aplicando transformaciones dentro del pipeline.
- Separa train/test antes de cualquier transformación dependiente de datos.
- Usa ColumnTransformer para columnas numéricas y categóricas.
- Pipelines facilitan cross-validation.
- StandardScaler solo debe ajustarse con train.
- Usa train_test_split con random_state para reproducibilidad.
- Metrics correctas dependen del objetivo (accuracy, RMSE, etc.).
- Usa Pipeline + GridSearchCV para tuning.
- Documenta cada paso del pipeline.
- Usa sklearn.set_config para visualizar pipelines.
- Mantén pipelines simples y legibles.


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
                "Escalar antes de dividir",
                "Si escalas antes de split, filtras información del test.",
            ),
            (
                "Feature engineering fuera del pipeline",
                "Puede contaminar validación y métricas.",
            ),
            (
                "No fijar random_state",
                "Resultados no reproducibles.",
            ),
            (
                "Usar métricas incorrectas",
                "Una métrica inapropiada puede engañar sobre rendimiento.",
            ),
            (
                "No separar validación",
                "Entrenar y evaluar en el mismo set produce overfitting.",
            ),
            (
                "Leakage por target encoding",
                "Codificar categorías usando el target sin CV produce fuga.",
            ),
            (
                "Pipeline demasiado complejo",
                "Dificulta el mantenimiento y debugging.",
            ),
            (
                "No manejar valores faltantes",
                "Los modelos pueden fallar o sesgarse.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Pipeline básico",
                """from sklearn.pipeline import Pipeline\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.linear_model import LogisticRegression\n\npipeline = Pipeline([\n    ("scaler", StandardScaler()),\n    ("model", LogisticRegression())\n])""",
            ),
            (
                "Train/test split",
                """from sklearn.model_selection import train_test_split\n\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)""",
            ),
            (
                "Cross-validation",
                """from sklearn.model_selection import cross_val_score\n\nscores = cross_val_score(pipeline, X, y, cv=5)\nprint(scores.mean())""",
            ),
            (
                "ColumnTransformer",
                """from sklearn.compose import ColumnTransformer\nfrom sklearn.preprocessing import OneHotEncoder\n\npreprocessor = ColumnTransformer([\n    ("cat", OneHotEncoder(), ["sexo"]),\n    ("num", StandardScaler(), ["edad"])\n])""",
            ),
            (
                "GridSearchCV",
                """from sklearn.model_selection import GridSearchCV\n\nparam_grid = {"model__C": [0.1, 1, 10]}\nsearch = GridSearchCV(pipeline, param_grid, cv=3)""",
            ),
            (
                "Métricas",
                """from sklearn.metrics import accuracy_score\n\npred = pipeline.predict(X_test)\nprint(accuracy_score(y_test, pred))""",
            ),
            (
                "Set config",
                """from sklearn import set_config\nset_config(display="diagram")""",
            ),
            (
                "Imputación",
                """from sklearn.impute import SimpleImputer\n\npreprocess = Pipeline([("imputer", SimpleImputer())])""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "¿Qué es data leakage y por qué es peligroso?",
                "hints": ["Información del test en train"],
                "solution": "Es la fuga de información del set de test hacia el train, produce métricas infladas.",
            },
            {
                "question": "Escribe un pipeline con StandardScaler y LogisticRegression.",
                "hints": ["Pipeline([('scaler', ...), ('model', ...)])"],
                "solution": "pipeline = Pipeline([('scaler', StandardScaler()), ('model', LogisticRegression())])",
            },
            {
                "question": "¿Dónde debes aplicar el escalado para evitar leakage?",
                "hints": ["Dentro del pipeline"],
                "solution": "Dentro del pipeline, ajustado solo con datos de entrenamiento.",
            },
        ]

    def requirements(self) -> list[str]:
        return ["scikit-learn"]

    def build_demo(self) -> QWidget | None:
        ok, sklearn, message = optional_import("sklearn")
        widget = QWidget()
        layout = QVBoxLayout(widget)
        if not ok:
            layout.addWidget(QLabel(message or "scikit-learn no disponible."))
            return widget

        import numpy as np
        from sklearn.datasets import make_classification
        from sklearn.linear_model import LogisticRegression
        from sklearn.model_selection import train_test_split
        from sklearn.pipeline import Pipeline
        from sklearn.preprocessing import StandardScaler

        X, y = make_classification(n_samples=200, n_features=4, random_state=42)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
        pipeline = Pipeline([("scaler", StandardScaler()), ("model", LogisticRegression())])
        pipeline.fit(X_train, y_train)
        score = pipeline.score(X_test, y_test)

        layout.addWidget(QLabel("Demo: pipeline entrenado en dataset sintético."))
        layout.addWidget(QLabel(f"Accuracy de prueba: {score:.2f}"))
        return widget
